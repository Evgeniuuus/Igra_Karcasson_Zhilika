# =============================================================================================================
# ==== Добрейших вечерочков господамы =========================================================================
# =========== Перед вами предстала настольная игра "КАРКАССОН" ================================================
# =============================================================================================================

import copy
import math
import pygame
import pygame_menu
import random
import sys
from pygame.locals import *

import tileSets as ts


import os


def get_resource_path(relative_path):
    # Получить путь к ресурсу, будь то dev или EXE.
    if hasattr(sys, '_MEIPASS'):
        # Путь, если программа запущена из EXE
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Пример использования:
textures_path = get_resource_path("textures")
if not os.path.exists(textures_path):
    print(f"Ошибка: папка {textures_path} не найдена!")
else:
    print(f"Папка {textures_path} успешно загружена.")

pygame.init()

FPS = 144
FramePerSec = pygame.time.Clock()

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Каркассон Жилика")

tileset = pygame.image.load("textures/tiles.png").convert()
blueMeeple = pygame.image.load("textures/blue-meeple.png").convert_alpha()
greenMeeple = pygame.image.load("textures/green-meeple.png").convert_alpha()
redMeeple = pygame.image.load("textures/red-meeple.png").convert_alpha()
yellowMeeple = pygame.image.load("textures/yellow-meeple.png").convert_alpha()

font = pygame.font.SysFont('calibri', 24)


class App:
    def __init__(self):
        self.mouseLeftClicked = 0
        self.mouseRightClicked = 0
        self.mouseMoving = 0

    class Game:
        def __init__(self):
            self.boardSize = 71
            self.hasStarted = 0
            self.hasEnded = 0
            self.turnState = "tile"
            self.gameStateMenuWidth = 300
            self.relativeX = -(math.floor(self.boardSize / 2) * 128) + math.floor(
                ((SCREEN_WIDTH - self.gameStateMenuWidth) / 128 / 2)) * 128
            self.relativeY = -(math.floor(self.boardSize / 2) * 128) + math.floor((SCREEN_HEIGHT / 128 / 2)) * 128
            self.placedTile = None
            self.placedTiles = []
            for i in range(self.boardSize):
                self.placedTiles.append([])
                for j in range(self.boardSize):
                    self.placedTiles[i].append(None)
            self.availableSpots = []
            self.meepleSpots = []
            self.tileStack = []
            self.drawNextTile = 1
            self.currentRotation = 0
            self.playerTurn = 0
            self.playerCount = 2
            self.playerNames = []
            self.playerColors = (blueMeeple, greenMeeple, redMeeple, yellowMeeple)
            self.playerMeeples = [7, 7, 7, 7]
            self.meeplePositions = [[], [], [], []]
            self.playerPoints = [0, 0, 0, 0]
            self.drawSkip = 0
            self.drawWinner = 0

        def start(self):
            self.hasStarted = 1
            self.setPlayerNames()
            self.gamesetup()
            for widget in settingsMenu.get_widgets():
                settingsMenu.remove_widget(widget)

        def endGame(self):
            if self.hasEnded:
                self.scoreAll()
                self.drawWinner = 1

        def launchsettingsMenu(self):
            menu.toggle()
            settingsMenu.toggle()

        def setPlayerCount(self, x, value):
            self.playerCount = value
            for n, widget in enumerate(settingsMenu.get_widgets()):
                if n != 0 and n != 1 and n != 2:
                    settingsMenu.remove_widget(widget)
            for i in range(self.playerCount):
                settingsMenu.add.text_input("", default="Zhilik " + str(i + 1), repeat_keys_interval_ms=10,
                                            maxchar=20)
            settingsMenu.add.label('')
            settingsMenu.add.button('---Вперед---', game.start)

        def setPlayerNames(self):
            for i in range(self.playerCount):
                self.playerNames.append(settingsMenu.get_widgets()[3 + i].get_value())

        def gamesetup(self):
            tileOrder = []
            for i in range(game_mode):
                tileOrder.append(i + 1)
            tileOrder.pop(tileOrder.index(36))
            self.tileStack.clear
            for i in range(game_mode-1):
                randIndex = random.randint(0, len(tileOrder) - 1)
                self.tileStack.append(tileOrder[randIndex])
                tileOrder.pop(randIndex)
            halfBoardSize = math.floor(self.boardSize / 2)
            self.placedTiles[halfBoardSize][halfBoardSize] = self.Tile(ts.tile36, halfBoardSize, halfBoardSize)
            # for i in range(len(self.tileStack) - 0):
            #     self.tileStack.pop(0)
            self.nextTile = self.Tile(getattr(ts, 'tile' + str(self.tileStack[0])), 0, 0)
            self.checkAvaiableSpots()

        def drawsettingsMenu(self):
            settingsMenu.draw(screen)
            settingsMenu.update(events)

        def drawMenu(self):
            menu.draw(screen)
            menu.update(events)

        def getSidePos(self, side, size):
            if side == 'N': return 64 - size / 2, 10
            if side == 'S': return 64 - size / 2, 118 - size
            if side == 'E': return 118 - size, 64 - size / 2
            if side == 'W': return 10, 64 - size / 2

            if side == 'C': return 64 - size / 2, 64 - size / 2

            if side == 'NNW': return 5, 5
            if side == 'NNE': return 123 - size, 5
            if side == 'ENE': return 123 - size, 5
            if side == 'ESE': return 123 - size, 123 - size
            if side == 'SSE': return 123 - size, 123 - size
            if side == 'SSW': return 5, 123 - size
            if side == 'WSW': return 5, 123 - size
            if side == 'WNW': return 5, 5

        def drawGame(self):
            if self.hasStarted:
                screen.fill((46, 46, 46))
                for col in self.placedTiles:
                    for tile in col:
                        if tile is not None:
                            x = tile.col * 128 + math.floor(self.relativeX)
                            y = tile.row * 128 + math.floor(self.relativeY)
                            tileTxt = tileset.subsurface(tile.txtPosX, tile.txtPosY, 256, 256)
                            scaledTxt = pygame.transform.scale(tileTxt, (128, 128))
                            screen.blit(pygame.transform.rotate(scaledTxt, -90 * tile.rotation), (x, y))
                for n, player in enumerate(self.meeplePositions):
                    for meeple in player:
                        scaledTxt = pygame.transform.scale(self.playerColors[n], (40, 40))
                        side = self.getSidePos(meeple[2], 40)
                        x = meeple[0] * 128 + math.floor(self.relativeX) + side[0]
                        y = meeple[1] * 128 + math.floor(self.relativeY) + side[1]
                        screen.blit(scaledTxt, (x, y))
                if self.turnState == 'meeple':
                    for spot in self.meepleSpots:
                        side = self.getSidePos(spot[2], 20)
                        x = spot[0] * 128 + math.floor(self.relativeX) + side[0]
                        y = spot[1] * 128 + math.floor(self.relativeY) + side[1]
                        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 20, 20))
                if self.turnState == 'tile' and not self.hasEnded:
                    for i in range(self.boardSize):
                        for j in range(self.boardSize):
                            if 1 in self.availableSpots[i][j]:
                                x = i * 128 + math.floor(self.relativeX)
                                y = j * 128 + math.floor(self.relativeY)
                                pygame.draw.rect(screen, (76, 76, 76), pygame.Rect(x, y, 128, 128))
                                if self.availableSpots[i][j][self.currentRotation]:
                                    pygame.draw.rect(screen, (0, 153, 0), pygame.Rect(x, y, 128, 128))
                if self.drawSkip:
                    infoX = (SCREEN_WIDTH - self.gameStateMenuWidth) / 2 - 120
                    infoY = 16
                    infoWidth = 240
                    infoHeight = 64
                    pygame.draw.rect(screen, (252, 177, 3), pygame.Rect(infoX, infoY, infoWidth, infoHeight))
                    text = font.render("Пропуск размещения", True, (0, 0, 0))
                    screen.blit(text, text.get_rect(center=((SCREEN_WIDTH - self.gameStateMenuWidth) / 2, infoY + 32)))
            if self.hasEnded and self.drawWinner:
                infoWidth = 480
                infoHeight = 64
                infoX = (SCREEN_WIDTH - self.gameStateMenuWidth) / 2 - infoWidth / 2
                infoY = SCREEN_HEIGHT - infoHeight - 16
                pygame.draw.rect(screen, (252, 177, 3), pygame.Rect(infoX, infoY, infoWidth, infoHeight))
                high = max(self.playerPoints)
                tmp = ""
                multipleWinners = 0
                for n, player in enumerate(self.playerNames):
                    if self.playerPoints[n] == high:
                        if len(tmp) > 0:
                            tmp += ", "
                            multipleWinners = 1
                        tmp += player
                if multipleWinners:
                    tmp += " Победители."
                else:
                    tmp += " Победитель."
                text = font.render(tmp, True, (0, 0, 0))
                screen.blit(text, text.get_rect(center=((SCREEN_WIDTH - self.gameStateMenuWidth) / 2, infoY + 32)))

        def checkSkip(self, mousePos):
            if pygame.Rect.collidepoint(pygame.Rect((SCREEN_WIDTH - self.gameStateMenuWidth) / 2 - 120, 16, 240, 64),
                                        mousePos):
                self.scoreCloisters(self.placedTile)
                self.scoreRoads(self.placedTile)
                self.scoreCities(self.placedTile)
                self.playerTurn = 0 if self.playerTurn + 1 > self.playerCount - 1 else self.playerTurn + 1
                self.turnState = 'tile'
                self.drawSkip = 0
                if len(self.tileStack) == 0:
                    self.hasEnded = 1
                    self.endGame()

        def drawGameState(self):
            pygame.draw.rect(screen, (57, 105, 56),
                             pygame.Rect(SCREEN_WIDTH - self.gameStateMenuWidth, 0, self.gameStateMenuWidth,
                                         SCREEN_HEIGHT))
            pygame.draw.rect(screen, (77, 40, 0),
                             pygame.Rect(SCREEN_WIDTH - 128 - ((self.gameStateMenuWidth - 128) / 2) - 4, 64 - 4,
                                         128 + 2 * 4, 128 + 2 * 4))
            text = font.render('Следующая карточка:', True, (0, 0, 0))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH - self.gameStateMenuWidth / 2, 32)))
            if len(self.tileStack) > 0:
                text = font.render('Осталось: ' + str(len(self.tileStack) - 1), True, (0, 0, 0))
            else:
                text = font.render('Осталось: ' + str(len(self.tileStack)), True, (0, 0, 0))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH - self.gameStateMenuWidth / 2, 230)))
            if self.playerTurn < len(self.playerNames):
                text = font.render(f"Ход: {self.playerNames[self.playerTurn]}", True, (0, 0, 0))
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH - self.gameStateMenuWidth / 2, SCREEN_HEIGHT - 32)))
            if self.drawNextTile:
                tileTxt = tileset.subsurface(self.nextTile.txtPosX, self.nextTile.txtPosY, 256, 256)
                scaledTxt = pygame.transform.scale(tileTxt, (128, 128))
                screen.blit(pygame.transform.rotate(scaledTxt, -90 * self.nextTile.rotation),
                            (SCREEN_WIDTH - 128 - ((self.gameStateMenuWidth - 128) / 2), 64))
            for n, name in enumerate(self.playerNames):
                infoX = SCREEN_WIDTH - self.gameStateMenuWidth + 16
                infoY = 320 + n * 80
                infoWidth = self.gameStateMenuWidth - 32
                infoHeight = 64
                pygame.draw.rect(screen, (77, 40, 0), pygame.Rect(infoX - 4, infoY - 4, infoWidth + 8, infoHeight + 8))
                if n == self.playerTurn:
                    pygame.draw.rect(screen, (3, 252, 244), pygame.Rect(infoX, infoY, infoWidth, infoHeight))
                else:
                    pygame.draw.rect(screen, (252, 177, 3), pygame.Rect(infoX, infoY, infoWidth, infoHeight))
                text = font.render(name, True, (0, 0, 0))
                screen.blit(text, text.get_rect(center=(SCREEN_WIDTH - self.gameStateMenuWidth / 2 - 26, infoY + 18)))
                text = font.render(str(self.playerPoints[n]), True, (0, 0, 0))
                screen.blit(text, text.get_rect(center=(SCREEN_WIDTH - 44, infoY + infoHeight / 2 + 2)))
                scaledTxt = pygame.transform.scale(self.playerColors[n], (24, 24))
                for i in range(self.playerMeeples[n]):
                    screen.blit(scaledTxt, (infoX + 12 + i * 28, infoY + infoHeight - 28))

        def drawAll(self):
            if menu.is_enabled():
                self.drawMenu()
            if settingsMenu.is_enabled():
                self.drawsettingsMenu()
            if self.hasStarted:
                self.drawGame()
                self.drawGameState()

                exit_text = font.render("Для выхода нажмите ESC", True, (0, 0, 0))
                text_rect = exit_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 65))
                screen.blit(exit_text, text_rect)


        def placeTile(self, mousePos):
            if len(self.tileStack) > 0:
                posX = mousePos[0] - self.relativeX
                posY = mousePos[1] - self.relativeY
                x = math.floor(posX / 128)
                y = math.floor(posY / 128)
                if self.availableSpots[x][y][self.currentRotation]:
                    self.placedTiles[x][y] = self.nextTile.rotateTile(self.currentRotation)
                    self.placedTiles[x][y].col = x
                    self.placedTiles[x][y].row = y
                    self.placedTile = self.placedTiles[x][y]

                    self.tileStack.pop(0)
                    self.currentRotation = 0
                    if len(self.tileStack) > 0:
                        self.nextTile = self.Tile(getattr(ts, 'tile' + str(self.tileStack[0])), 0, 0)
                    else:
                        self.drawNextTile = 0
                    self.checkMeepleSpots()
                    if len(self.meepleSpots) > 0:
                        self.turnState = 'meeple'
                    else:
                        self.scoreCloisters(self.placedTile)
                        self.scoreRoads(self.placedTile)
                        self.scoreCities(self.placedTile)
                        self.playerTurn = 0 if self.playerTurn + 1 > self.playerCount - 1 else self.playerTurn + 1
                        if len(self.tileStack) == 0:
                            self.hasEnded = 1
                            self.endGame()
                    self.checkAvaiableSpots()

        def checkAvaiableSpots(self):
            self.availableSpots.clear()
            for i in range(self.boardSize):
                self.availableSpots.append([])
                for j in range(self.boardSize):
                    self.availableSpots[i].append([0, 0, 0, 0])
            for x in range(1, self.boardSize - 1):
                for y in range(1, self.boardSize - 1):
                    if self.placedTiles[x][y] is None:
                        top = self.getTile(x, y - 1)
                        right = self.getTile(x + 1, y)
                        bot = self.getTile(x, y + 1)
                        left = self.getTile(x - 1, y)

                        for rot in range(4):
                            curr = self.nextTile.rotateTile(rot)
                            if top is None and right is None and bot is None and left is None:
                                break
                            fits = True
                            for side in ['N', 'E', 'S', 'W']:
                                terrainType = curr.getTerrain(side)
                                if side == 'N':
                                    fitsTop = top is None or top.getTerrain('S') == terrainType
                                    fits = fits and fitsTop
                                elif side == 'E':
                                    fitsRight = right is None or right.getTerrain('W') == terrainType
                                    fits = fits and fitsRight
                                elif side == 'S':
                                    fitsBot = bot is None or bot.getTerrain('N') == terrainType
                                    fits = fits and fitsBot
                                else:
                                    fitsLeft = left is None or left.getTerrain('E') == terrainType
                                    fits = fits and fitsLeft
                            if fits:
                                self.availableSpots[x][y][rot] = True

        def placeMeeple(self, mousePos):
            posX = mousePos[0]
            posY = mousePos[1]

            if self.playerMeeples[self.playerTurn] > 0:
                for spot in self.meepleSpots:
                    side = self.getSidePos(spot[2], 20)
                    x = spot[0] * 128 + math.floor(self.relativeX) + side[0]
                    y = spot[1] * 128 + math.floor(self.relativeY) + side[1]
                    if pygame.Rect.collidepoint(pygame.Rect(x, y, 20, 20), (posX, posY)):
                        self.meeplePositions[self.playerTurn].append(
                            [self.placedTile.col, self.placedTile.row, spot[2]])
                        self.scoreCloisters(self.placedTile)
                        self.scoreRoads(self.placedTile)
                        self.scoreCities(self.placedTile)
                        self.playerMeeples[self.playerTurn] -= 1
                        self.playerTurn = 0 if self.playerTurn + 1 > self.playerCount - 1 else self.playerTurn + 1
                        self.turnState = 'tile'
                        self.drawSkip = 0
                        if len(self.tileStack) == 0:
                            self.hasEnded = 1
                            self.endGame()
            else:
                self.scoreCloisters(self.placedTile)
                self.scoreRoads(self.placedTile)
                self.scoreCities(self.placedTile)
                self.playerTurn = 0 if self.playerTurn + 1 > self.playerCount - 1 else self.playerTurn + 1
                self.turnState = 'tile'
                self.drawSkip = 0
                if len(self.tileStack) == 0:
                    self.hasEnded = 1
                    self.endGame()

        def checkMeepleSpots(self):
            self.meepleSpots.clear()

            self.checkCloisters(self.placedTile)
            self.checkRoads(self.placedTile)
            self.checkCities(self.placedTile)
            self.checkFields(self.placedTile)

            if len(self.meepleSpots) > 0 and self.playerMeeples[self.playerTurn] > 0:
                self.drawSkip = 1

        def checkCloisters(self, tile):
            if tile.cloister:
                self.meepleSpots.append((tile.col, tile.row, 'C'))

        def scoreCloisters(self, tile):
            tilesAround = []
            for i in range(3):
                for j in range(3):
                    tilesAround.append(self.placedTiles[tile.col - 1 + i][tile.row - 1 + j])
            for tile2 in tilesAround:
                if tile2 != None and tile2.cloister:
                    cloisterCompleted = 1
                    for i in range(3):
                        for j in range(3):
                            if self.placedTiles[tile2.col - 1 + i][tile2.row - 1 + j] is None:
                                cloisterCompleted = 0
                                break
                    if cloisterCompleted:
                        pos = [tile2.col, tile2.row, 'C']
                        for n, player in enumerate(self.meeplePositions):
                            if pos in player:
                                self.playerPoints[n] += 9
                                self.playerMeeples[n] += 1
                                player.remove(pos)

        def checkRoads(self, tile):
            x = tile.col
            y = tile.row

            for road in tile.roads:
                isAvailable = 1
                for side in road:
                    if side != 'C':
                        startingPos = [x, y, side]
                        pos = [x, y, side]
                        pos2 = [x, y, 0]
                        for i in road:
                            if side in i:
                                tmp = road.copy()
                                tmp.remove(side)
                                pos2[2] = tmp[0]
                        roadNotEnded = 1
                        while roadNotEnded and isAvailable:
                            for i in range(self.playerCount):
                                if pos in self.meeplePositions[i] or pos2 in self.meeplePositions[i]:
                                    isAvailable = 0
                                    break
                            opp = self.getOppositeSide(pos[2])
                            if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                                if len(self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]].roads) > 0:
                                    for road2 in self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]].roads:
                                        if opp[2] in road2:
                                            if 'C' in road2:
                                                roadNotEnded = 0
                                                pos2 = [pos[0] + opp[0], pos[1] + opp[1], opp[2]]
                                                for i in range(self.playerCount):
                                                    if pos2 in self.meeplePositions[i]:
                                                        isAvailable = 0
                                                break
                                            else:
                                                pos2 = [pos[0] + opp[0], pos[1] + opp[1], opp[2]]
                                                tmp = road2.copy()
                                                tmp.remove(opp[2])
                                                pos = [pos[0] + opp[0], pos[1] + opp[1], tmp[0]]
                            else:
                                roadNotEnded = 0
                                break
                if isAvailable:
                    self.meepleSpots.append(startingPos)

        def scoreRoads(self, tile):
            x = tile.col
            y = tile.row

            for road in tile.roads:
                isFinished = True
                uncheckedPositions = set()
                checkedPositions = set()
                for side in road:
                    if side != 'C':
                        uncheckedPositions.add((x, y, side))
                while len(uncheckedPositions) > 0 and isFinished:
                    positionsToAdd = []
                    positionsToRemove = []
                    for pos in uncheckedPositions:
                        opp = self.getOppositeSide(pos[2])
                        oppPos = []
                        if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                            oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                            oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                            for side in self.getRoad(oppTile, oppPos[2]):
                                positionsToAdd.append((oppPos[0], oppPos[1], side))
                        else:
                            isFinished = False
                            break
                        checkedPositions.add(pos)
                        positionsToRemove.append(pos)

                    for pos in positionsToRemove:
                        uncheckedPositions.remove(pos)
                    for pos in positionsToAdd:
                        if pos not in checkedPositions:
                            uncheckedPositions.add(pos)

                if isFinished:
                    roadTiles = []
                    meeplesCount = [0, 0, 0, 0]
                    meeplesToRemove = []
                    for pos in checkedPositions:
                        for i in range(self.playerCount):
                            if list(pos) in self.meeplePositions[i]:
                                meeplesToRemove.append(list(pos))
                                meeplesCount[i] += 1
                        tile = self.placedTiles[pos[0]][pos[1]]
                        if tile not in roadTiles:
                            roadTiles.append(tile)

                    roadScore = 0
                    for tile in roadTiles:
                        roadScore += 1

                    high = max(meeplesCount)
                    for n, i in enumerate(meeplesCount):
                        self.playerMeeples[n] += i
                        if i == high and i != 0:
                            self.playerPoints[n] += roadScore
                    for meeple in meeplesToRemove:
                        for player in self.meeplePositions:
                            if meeple in player:
                                player.remove(meeple)

        def checkCities(self, tile):
            x = tile.col
            y = tile.row

            for city in tile.cities:
                isAvailable = 1
                startingPos = [x, y, city[0]]
                uncheckedPositions = set()
                checkedPositions = set()
                for side in city:
                    uncheckedPositions.add((x, y, side))
                while len(uncheckedPositions) > 0 and isAvailable:
                    positionsToAdd = []
                    positionsToRemove = []
                    for pos in uncheckedPositions:
                        for player in self.meeplePositions:
                            if list(pos) in player:
                                isAvailable = False
                                break
                        opp = self.getOppositeSide(pos[2])
                        oppPos = []
                        if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                            oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                            oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                            for side in self.getCity(oppTile, oppPos[2]):
                                positionsToAdd.append((oppPos[0], oppPos[1], side))
                        checkedPositions.add(pos)
                        positionsToRemove.append(pos)

                    for pos in positionsToRemove:
                        uncheckedPositions.remove(pos)
                    for pos in positionsToAdd:
                        if pos not in checkedPositions:
                            uncheckedPositions.add(pos)
                if isAvailable:
                    self.meepleSpots.append(startingPos)

        def scoreCities(self, tile):
            x = tile.col
            y = tile.row

            for city in tile.cities:
                isFinished = True
                uncheckedPositions = set()
                checkedPositions = set()
                for side in city:
                    uncheckedPositions.add((x, y, side))
                while len(uncheckedPositions) > 0 and isFinished:
                    positionsToAdd = []
                    positionsToRemove = []
                    for pos in uncheckedPositions:
                        opp = self.getOppositeSide(pos[2])
                        oppPos = []
                        if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                            oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                            oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                            for side in self.getCity(oppTile, oppPos[2]):
                                positionsToAdd.append((oppPos[0], oppPos[1], side))
                        else:
                            isFinished = False
                            break
                        checkedPositions.add(pos)
                        positionsToRemove.append(pos)

                    for pos in positionsToRemove:
                        uncheckedPositions.remove(pos)
                    for pos in positionsToAdd:
                        if pos not in checkedPositions:
                            uncheckedPositions.add(pos)

                if isFinished:
                    cityTiles = []
                    meeplesCount = [0, 0, 0, 0]
                    meeplesToRemove = []
                    for pos in checkedPositions:
                        for i in range(self.playerCount):
                            if list(pos) in self.meeplePositions[i]:
                                meeplesToRemove.append(list(pos))
                                meeplesCount[i] += 1
                        tile = self.placedTiles[pos[0]][pos[1]]
                        if tile not in cityTiles:
                            cityTiles.append(tile)

                    cityScore = 0
                    for tile in cityTiles:
                        cityScore += 4 if tile.shield else 2

                    high = max(meeplesCount)
                    for n, i in enumerate(meeplesCount):
                        self.playerMeeples[n] += i
                        if i == high and i != 0:
                            self.playerPoints[n] += cityScore
                    for meeple in meeplesToRemove:
                        for player in self.meeplePositions:
                            if meeple in player:
                                player.remove(meeple)

        def checkFields(self, tile):
            x = tile.col
            y = tile.row

            for field in tile.fields:
                isAvailable = 1
                startingPos = [x, y, field[0]]
                uncheckedPositions = set()
                checkedPositions = set()
                for side in field:
                    uncheckedPositions.add((x, y, side))
                while len(uncheckedPositions) > 0 and isAvailable:
                    positionsToAdd = []
                    positionsToRemove = []
                    for pos in uncheckedPositions:
                        for player in self.meeplePositions:
                            if list(pos) in player:
                                isAvailable = False
                                break
                        opp = self.getOppositeSide(pos[2])
                        oppPos = []
                        if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                            oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                            oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                            for side in self.getField(oppTile, oppPos[2]):
                                positionsToAdd.append((oppPos[0], oppPos[1], side))
                        checkedPositions.add(pos)
                        positionsToRemove.append(pos)

                    for pos in positionsToRemove:
                        uncheckedPositions.remove(pos)
                    for pos in positionsToAdd:
                        if pos not in checkedPositions:
                            uncheckedPositions.add(pos)
                if isAvailable:
                    self.meepleSpots.append(startingPos)

        def scoreAll(self):
            while len(self.meeplePositions[0]) > 0 or len(self.meeplePositions[1]) > 0 or len(
                    self.meeplePositions[2]) > 0 or len(self.meeplePositions[3]) > 0:
                playerIndex = 0
                for n, player in enumerate(self.meeplePositions):
                    if len(player) > 0:
                        playerIndex = n
                        break
                meeple = self.meeplePositions[playerIndex][0]
                tile = self.placedTiles[meeple[0]][meeple[1]]
                if meeple[2] == 'C':
                    self.endScoreCloisters(tile)
                elif len(meeple[2]) == 3:
                    self.endScoreFields(tile, meeple[2])
                else:
                    for city in tile.cities:
                        if meeple[2] in city:
                            self.endScoreCities(tile, meeple[2])
                    for road in tile.roads:
                        if meeple[2] in road:
                            self.endScoreRoads(tile, meeple[2])

        def endScoreCloisters(self, tile):
            tilesAround = []
            cloisterScore = 0
            for i in range(3):
                for j in range(3):
                    tilesAround.append(self.placedTiles[tile.col - 1 + i][tile.row - 1 + j])
            for tile2 in tilesAround:
                if tile2 != None:
                    cloisterScore += 1
            pos = [tile.col, tile.row, 'C']
            for n, player in enumerate(self.meeplePositions):
                if pos in player:
                    self.playerPoints[n] += cloisterScore
                    self.playerMeeples[n] += 1
                    player.remove(pos)

        def endScoreRoads(self, tile, meepleSide):
            x = tile.col
            y = tile.row

            uncheckedPositions = set()
            checkedPositions = set()
            for side in self.getRoad(tile, meepleSide):
                uncheckedPositions.add((x, y, side))
            while len(uncheckedPositions) > 0:
                positionsToAdd = []
                positionsToRemove = []
                for pos in uncheckedPositions:
                    opp = self.getOppositeSide(pos[2])
                    oppPos = []
                    if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                        oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                        oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                        for side in self.getRoad(oppTile, oppPos[2]):
                            positionsToAdd.append((oppPos[0], oppPos[1], side))
                    checkedPositions.add(pos)
                    positionsToRemove.append(pos)

                for pos in positionsToRemove:
                    uncheckedPositions.remove(pos)
                for pos in positionsToAdd:
                    if pos not in checkedPositions:
                        uncheckedPositions.add(pos)

            roadTiles = []
            meeplesCount = [0, 0, 0, 0]
            meeplesToRemove = []
            for pos in checkedPositions:
                for i in range(self.playerCount):
                    if list(pos) in self.meeplePositions[i]:
                        meeplesToRemove.append(list(pos))
                        meeplesCount[i] += 1
                tile = self.placedTiles[pos[0]][pos[1]]
                if tile not in roadTiles:
                    roadTiles.append(tile)

            roadScore = 0
            for tile in roadTiles:
                roadScore += 1

            high = max(meeplesCount)
            for n, i in enumerate(meeplesCount):
                self.playerMeeples[n] += i
                if i == high and i != 0:
                    self.playerPoints[n] += roadScore
            for meeple in meeplesToRemove:
                for player in self.meeplePositions:
                    if meeple in player:
                        player.remove(meeple)

        def endScoreCities(self, tile, meepleSide):
            x = tile.col
            y = tile.row

            uncheckedPositions = set()
            checkedPositions = set()
            for side in self.getCity(tile, meepleSide):
                uncheckedPositions.add((x, y, side))
            while len(uncheckedPositions) > 0:
                positionsToAdd = []
                positionsToRemove = []
                for pos in uncheckedPositions:
                    opp = self.getOppositeSide(pos[2])
                    oppPos = []
                    if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                        oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                        oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                        for side in self.getCity(oppTile, oppPos[2]):
                            positionsToAdd.append((oppPos[0], oppPos[1], side))
                    checkedPositions.add(pos)
                    positionsToRemove.append(pos)

                for pos in positionsToRemove:
                    uncheckedPositions.remove(pos)
                for pos in positionsToAdd:
                    if pos not in checkedPositions:
                        uncheckedPositions.add(pos)

            cityTiles = []
            meeplesCount = [0, 0, 0, 0]
            meeplesToRemove = []
            for pos in checkedPositions:
                for i in range(self.playerCount):
                    if list(pos) in self.meeplePositions[i]:
                        meeplesToRemove.append(list(pos))
                        meeplesCount[i] += 1
                tile = self.placedTiles[pos[0]][pos[1]]
                if tile not in cityTiles:
                    cityTiles.append(tile)

            cityScore = 0
            for tile in cityTiles:
                cityScore += 2 if tile.shield else 1

            high = max(meeplesCount)
            for n, i in enumerate(meeplesCount):
                self.playerMeeples[n] += i
                if i == high and i != 0:
                    self.playerPoints[n] += cityScore
            for meeple in meeplesToRemove:
                for player in self.meeplePositions:
                    if meeple in player:
                        player.remove(meeple)

        def endScoreFields(self, tile, meepleSide):
            finishedCities = self.findFinishedCities()
            x = tile.col
            y = tile.row

            uncheckedPositions = set()
            checkedPositions = set()
            for side in self.getField(tile, meepleSide):
                uncheckedPositions.add((x, y, side))
            while len(uncheckedPositions) > 0:
                positionsToAdd = []
                positionsToRemove = []
                for pos in uncheckedPositions:
                    opp = self.getOppositeSide(pos[2])
                    oppPos = []
                    if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                        oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                        oppTile = self.placedTiles[oppPos[0]][oppPos[1]]
                        for side in self.getField(oppTile, oppPos[2]):
                            positionsToAdd.append((oppPos[0], oppPos[1], side))
                    checkedPositions.add(pos)
                    positionsToRemove.append(pos)

                for pos in positionsToRemove:
                    uncheckedPositions.remove(pos)
                for pos in positionsToAdd:
                    if pos not in checkedPositions:
                        uncheckedPositions.add(pos)

            fieldTiles = set()
            meeplesCount = [0, 0, 0, 0]
            meeplesToRemove = []
            for pos in checkedPositions:
                for i in range(self.playerCount):
                    if list(pos) in self.meeplePositions[i]:
                        meeplesToRemove.append(list(pos))
                        meeplesCount[i] += 1
                tile = self.placedTiles[pos[0]][pos[1]]
                tmp = (tile.col, tile.row)
                fieldTiles.add(tmp)

            fieldScore = 0
            for curTile in fieldTiles:
                citiesToRemove = []
                for finCity in finishedCities:
                    if curTile in finCity:
                        fieldScore += 3
                        citiesToRemove.append(finCity)
                for finCity in citiesToRemove:
                    finishedCities.remove(finCity)

            high = max(meeplesCount)
            for n, i in enumerate(meeplesCount):
                self.playerMeeples[n] += i
                if i == high and i != 0:
                    self.playerPoints[n] += fieldScore
            for meeple in meeplesToRemove:
                for player in self.meeplePositions:
                    if meeple in player:
                        player.remove(meeple)

        def findFinishedCities(self):
            finishedCities = []

            for x, col in enumerate(self.placedTiles):
                for y, tile in enumerate(col):
                    if tile is not None:
                        isValid = 1
                        for fin in finishedCities:
                            if (x, y) in fin:
                                isValid = 0
                        if isValid:
                            for city in tile.cities:
                                isFinished = True
                                uncheckedPositions = set()
                                checkedPositions = set()
                                for side in city:
                                    uncheckedPositions.add((x, y, side))
                                while len(uncheckedPositions) > 0 and isFinished:
                                    positionsToAdd = []
                                    positionsToRemove = []
                                    for pos in uncheckedPositions:
                                        opp = self.getOppositeSide(pos[2])
                                        oppPos = []
                                        if self.placedTiles[pos[0] + opp[0]][pos[1] + opp[1]] is not None:
                                            oppPos = (pos[0] + opp[0], pos[1] + opp[1], opp[2])
                                            self.pos_ = self.placedTiles[oppPos[0]][oppPos[1]]
                                            for side in self.getCity(self.pos_, oppPos[2]):
                                                positionsToAdd.append((oppPos[0], oppPos[1], side))
                                        else:
                                            isFinished = False
                                            break
                                        checkedPositions.add(pos)
                                        positionsToRemove.append(pos)

                                    for pos in positionsToRemove:
                                        uncheckedPositions.remove(pos)
                                    for pos in positionsToAdd:
                                        if pos not in checkedPositions:
                                            uncheckedPositions.add(pos)

                                if isFinished:
                                    finishedCities.append(set())
                                    for pos in checkedPositions:
                                        finishedCities[-1].add((pos[0], pos[1]))
            return finishedCities

        def getOppositeSide(self, side):
            if side == 'N': return [0, -1, 'S']
            if side == 'S': return [0, 1, 'N']
            if side == 'E': return [1, 0, 'W']
            if side == 'W': return [-1, 0, 'E']

            if side == 'NNW': return [0, -1, 'SSW']
            if side == 'NNE': return [0, -1, 'SSE']
            if side == 'ENE': return [1, 0, 'WNW']
            if side == 'ESE': return [1, 0, 'WSW']
            if side == 'SSE': return [0, 1, 'NNE']
            if side == 'SSW': return [0, 1, 'NNW']
            if side == 'WSW': return [-1, 0, 'ESE']
            if side == 'WNW': return [-1, 0, 'ENE']

        def getRoad(self, tile, side):
            for road in tile.roads:
                tmp = road.copy()
                if side in tmp:
                    if 'C' in tmp:
                        tmp.remove('C')
                    return tmp

        def getCity(self, tile, side):
            for city in tile.cities:
                tmp = city.copy()
                if side in tmp:
                    return tmp

        def getField(self, tile, side):
            for field in tile.fields:
                tmp = field.copy()
                if side in tmp:
                    return tmp
            print(tile.txtPosX, tile.txtPosY)

        def getTile(self, x, y):
            return self.placedTiles[x][y]

        class Tile:
            def __init__(self, id, col, row):
                self.id = id
                self.txtPosX = self.id.x
                self.txtPosY = self.id.y
                self.rotation = 0
                self.col = col
                self.row = row
                self.cities = self.id.cities
                self.fields = self.id.fields
                self.roads = self.id.roads
                self.cloister = self.id.cloister
                self.shield = self.id.shield

            def rotateTileImage(self):
                self.rotation = (self.rotation + 1) % 4

            def rotateTile(self, rotations):
                rotatePattern = ['N', 'E', 'S', 'W']
                rotatePatternExtended = ['NNE', 'ENE', 'ESE', 'SSE', 'SSW', 'WSW', 'WNW', 'NNW']
                rotatedTile = copy.deepcopy(self)
                for i in range(len(rotatedTile.cities)):
                    for j in range(len(rotatedTile.cities[i])):
                        rotatedTile.cities[i][j] = rotatePattern[
                            (rotatePattern.index(rotatedTile.cities[i][j]) + rotations) % len(rotatePattern)]
                for i in range(len(rotatedTile.fields)):
                    for j in range(len(rotatedTile.fields[i])):
                        rotatedTile.fields[i][j] = rotatePatternExtended[
                            (rotatePatternExtended.index(rotatedTile.fields[i][j]) + rotations * 2) % len(
                                rotatePatternExtended)]
                for i in range(len(rotatedTile.roads)):
                    for j in range(len(rotatedTile.roads[i])):
                        if rotatedTile.roads[i][j] != 'C':
                            rotatedTile.roads[i][j] = rotatePattern[
                                (rotatePattern.index(rotatedTile.roads[i][j]) + rotations) % len(rotatePattern)]
                return rotatedTile

            def getTerrain(self, side):
                for i in self.roads:
                    if side in i:
                        return 'road'
                for i in self.cities:
                    if side in i:
                        return 'city'
                return 'field'


def set_game_mode(mode):
    global game_mode
    game_mode = mode
    menu.toggle()
    settingsMenu.toggle()


def disable_dlc():
    dlc_button.set_title("Его пока НЕТ!!!")


app = App()
game = app.Game()

pygame.mixer.init()

music_path = get_resource_path("background.mp3")
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
else:
    print("Ошибка: Файл музыки не найден!")


game_mode = None

menu = pygame_menu.Menu('Выберите длительность игры', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Короткая  (72 тайла)', lambda: set_game_mode(72))
menu.add.button('Средняя  (144 тайла)', lambda: set_game_mode(144))
menu.add.button('Длинная (216 тайлов)', lambda: set_game_mode(216))
menu.add.label('')

dlc_button = menu.add.button('DLC', disable_dlc, font_color=(255, 0, 0))


settingsMenu = pygame_menu.Menu('', SCREEN_WIDTH, SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
settingsMenu.toggle()
settingsMenu.add.selector('Счетчик игроков: ', [('2', 2), ('3', 3), ('4', 4)], default=game.playerCount - 2,
                          onchange=game.setPlayerCount)
settingsMenu.add.label('')
settingsMenu.add.label('Введите имя игроков:')
settingsMenu.add.label('')
settingsMenu.add.button('ВПЕРЕД-->', game.start)
game.setPlayerCount('', 2)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEMOTION:
            app.mouseMoving = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: app.mouseLeftClicked = 1
            if event.button == 3: app.mouseRightClicked = 1

        if game.hasStarted:
            if app.mouseMoving and app.mouseLeftClicked:
                game.relativeX += event.rel[0]
                game.relativeY += event.rel[1]
                mouseMoved = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not app.mouseMoving and not mouseMoved:
                if game.turnState == 'tile':
                    game.placeTile(pygame.mouse.get_pos())
                elif game.turnState == 'meeple':
                    game.placeMeeple(pygame.mouse.get_pos())
                    game.checkSkip(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and not app.mouseMoving and not mouseMoved:
                game.nextTile.rotateTileImage()
                game.currentRotation = (game.currentRotation + 1) % 4
            if game.hasEnded:
                pass

        if event.type == pygame.MOUSEMOTION:
            app.mouseMoving = 0
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: app.mouseLeftClicked = 0
            if event.button == 3: app.mouseRightClicked = 0
            mouseMoved = 0

    game.drawAll()
    pygame.display.update()

    FramePerSec.tick(FPS)
