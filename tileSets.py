# =============================================================================================================
# ==== Здесь происходит описание игровых карточек =============================================================
# =============================================================================================================

import pygame

pygame.init()


class Tile:
    def __init__(self, filename, x, y, cities, fields, roads, cloister, shield):
        self.filename = filename
        self.x = x
        self.y = y
        self.cities = cities
        self.fields = fields
        self.roads = roads
        self.cloister = cloister
        self.shield = shield

    # Base Tile Set Representation (72 tiles)


tile1 = Tile('tiles.png', 256 * 0, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 0)
tile2 = Tile('tiles.png', 256 * 1, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile3 = Tile('tiles.png', 256 * 2, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile4 = Tile('tiles.png', 256 * 3, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile5 = Tile('tiles.png', 256 * 4, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile6 = Tile('tiles.png', 256 * 5, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile7 = Tile('tiles.png', 256 * 6, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile8 = Tile('tiles.png', 256 * 7, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile9 = Tile('tiles.png', 256 * 8, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile10 = Tile('tiles.png', 256 * 9, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile11 = Tile('tiles.png', 256 * 10, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile12 = Tile('tiles.png', 256 * 11, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile13 = Tile('tiles.png', 256 * 12, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile14 = Tile('tiles.png', 256 * 13, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 0)
tile15 = Tile('tiles.png', 256 * 14, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)
tile16 = Tile('tiles.png', 256 * 15, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)

tile17 = Tile('tiles.png', 256 * 0, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile18 = Tile('tiles.png', 256 * 1, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile19 = Tile('tiles.png', 256 * 2, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile20 = Tile('tiles.png', 256 * 3, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile21 = Tile('tiles.png', 256 * 4, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile22 = Tile('tiles.png', 256 * 5, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile23 = Tile('tiles.png', 256 * 6, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile24 = Tile('tiles.png', 256 * 7, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile25 = Tile('tiles.png', 256 * 8, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile26 = Tile('tiles.png', 256 * 9, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile27 = Tile('tiles.png', 256 * 10, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile28 = Tile('tiles.png', 256 * 11, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile29 = Tile('tiles.png', 256 * 12, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile30 = Tile('tiles.png', 256 * 13, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile31 = Tile('tiles.png', 256 * 14, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile32 = Tile('tiles.png', 256 * 15, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)

tile33 = Tile('tiles.png', 256 * 0, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile34 = Tile('tiles.png', 256 * 1, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile35 = Tile('tiles.png', 256 * 2, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile36 = Tile('tiles.png', 256 * 3, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile37 = Tile('tiles.png', 256 * 4, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile38 = Tile('tiles.png', 256 * 5, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile39 = Tile('tiles.png', 256 * 6, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile40 = Tile('tiles.png', 256 * 7, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile41 = Tile('tiles.png', 256 * 8, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile42 = Tile('tiles.png', 256 * 9, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile43 = Tile('tiles.png', 256 * 10, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile44 = Tile('tiles.png', 256 * 11, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile45 = Tile('tiles.png', 256 * 12, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile46 = Tile('tiles.png', 256 * 13, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile47 = Tile('tiles.png', 256 * 14, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile48 = Tile('tiles.png', 256 * 15, 256 * 2, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)

tile49 = Tile('tiles.png', 256 * 0, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile50 = Tile('tiles.png', 256 * 1, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile51 = Tile('tiles.png', 256 * 2, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile52 = Tile('tiles.png', 256 * 3, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile53 = Tile('tiles.png', 256 * 4, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile54 = Tile('tiles.png', 256 * 5, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile55 = Tile('tiles.png', 256 * 6, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile56 = Tile('tiles.png', 256 * 7, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile57 = Tile('tiles.png', 256 * 8, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile58 = Tile('tiles.png', 256 * 9, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile59 = Tile('tiles.png', 256 * 10, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile60 = Tile('tiles.png', 256 * 11, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile61 = Tile('tiles.png', 256 * 12, 256 * 3, [], [['ENE', 'NNE'], ['WSW', 'SSW'], ['ESE', 'SSE'], ['WNW', 'NNW']],
              [['E', 'C'], ['W', 'C'], ['S', 'C'], ['N', 'C']], 0, 0)
tile62 = Tile('tiles.png', 256 * 13, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile63 = Tile('tiles.png', 256 * 14, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile64 = Tile('tiles.png', 256 * 15, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)

tile65 = Tile('tiles.png', 256 * 0, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile66 = Tile('tiles.png', 256 * 1, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile67 = Tile('tiles.png', 256 * 2, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile68 = Tile('tiles.png', 256 * 3, 256 * 4, [['N', 'E', 'S', 'W']], [], [], 0, 1)
tile69 = Tile('tiles.png', 256 * 4, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile70 = Tile('tiles.png', 256 * 5, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile71 = Tile('tiles.png', 256 * 6, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile72 = Tile('tiles.png', 256 * 7, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 1)

