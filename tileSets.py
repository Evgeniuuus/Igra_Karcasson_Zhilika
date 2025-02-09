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


# ---------- Повтор всех карточек

tile73 = Tile('tiles.png', 256 * 0, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 0)
tile74 = Tile('tiles.png', 256 * 1, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile75 = Tile('tiles.png', 256 * 2, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile76 = Tile('tiles.png', 256 * 3, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile77 = Tile('tiles.png', 256 * 4, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile78 = Tile('tiles.png', 256 * 5, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile79 = Tile('tiles.png', 256 * 6, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile80 = Tile('tiles.png', 256 * 7, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile81 = Tile('tiles.png', 256 * 8, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile82 = Tile('tiles.png', 256 * 9, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile83 = Tile('tiles.png', 256 * 10, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile84 = Tile('tiles.png', 256 * 11, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile85 = Tile('tiles.png', 256 * 12, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile86 = Tile('tiles.png', 256 * 13, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 0)
tile87 = Tile('tiles.png', 256 * 14, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)
tile88 = Tile('tiles.png', 256 * 15, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)

tile89 = Tile('tiles.png', 256 * 0, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile90 = Tile('tiles.png', 256 * 1, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile91 = Tile('tiles.png', 256 * 2, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile92 = Tile('tiles.png', 256 * 3, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile93 = Tile('tiles.png', 256 * 4, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile94 = Tile('tiles.png', 256 * 5, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile95 = Tile('tiles.png', 256 * 6, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile96 = Tile('tiles.png', 256 * 7, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile97 = Tile('tiles.png', 256 * 8, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile98 = Tile('tiles.png', 256 * 9, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile99 = Tile('tiles.png', 256 * 10, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile100 = Tile('tiles.png', 256 * 11, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile101 = Tile('tiles.png', 256 * 12, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile102 = Tile('tiles.png', 256 * 13, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile103 = Tile('tiles.png', 256 * 14, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile104 = Tile('tiles.png', 256 * 15, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)

tile105 = Tile('tiles.png', 256 * 0, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile106 = Tile('tiles.png', 256 * 1, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile107 = Tile('tiles.png', 256 * 2, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile108 = Tile('tiles.png', 256 * 3, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile109 = Tile('tiles.png', 256 * 4, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile110 = Tile('tiles.png', 256 * 5, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile111 = Tile('tiles.png', 256 * 6, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile112 = Tile('tiles.png', 256 * 7, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile113 = Tile('tiles.png', 256 * 8, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile114 = Tile('tiles.png', 256 * 9, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile115 = Tile('tiles.png', 256 * 10, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile116 = Tile('tiles.png', 256 * 11, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile117 = Tile('tiles.png', 256 * 12, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile118 = Tile('tiles.png', 256 * 13, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile119 = Tile('tiles.png', 256 * 14, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile120 = Tile('tiles.png', 256 * 15, 256 * 2, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)

tile121 = Tile('tiles.png', 256 * 0, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile122 = Tile('tiles.png', 256 * 1, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile123 = Tile('tiles.png', 256 * 2, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile124 = Tile('tiles.png', 256 * 3, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile125 = Tile('tiles.png', 256 * 4, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile126 = Tile('tiles.png', 256 * 5, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile127 = Tile('tiles.png', 256 * 6, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile128 = Tile('tiles.png', 256 * 7, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile129 = Tile('tiles.png', 256 * 8, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile130 = Tile('tiles.png', 256 * 9, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile131 = Tile('tiles.png', 256 * 10, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile132 = Tile('tiles.png', 256 * 11, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile133 = Tile('tiles.png', 256 * 12, 256 * 3, [], [['ENE', 'NNE'], ['WSW', 'SSW'], ['ESE', 'SSE'], ['WNW', 'NNW']],
              [['E', 'C'], ['W', 'C'], ['S', 'C'], ['N', 'C']], 0, 0)
tile134 = Tile('tiles.png', 256 * 13, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile135 = Tile('tiles.png', 256 * 14, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile136 = Tile('tiles.png', 256 * 15, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)

tile137 = Tile('tiles.png', 256 * 0, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile138 = Tile('tiles.png', 256 * 1, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile139 = Tile('tiles.png', 256 * 2, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile140 = Tile('tiles.png', 256 * 3, 256 * 4, [['N', 'E', 'S', 'W']], [], [], 0, 1)
tile141 = Tile('tiles.png', 256 * 4, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile142 = Tile('tiles.png', 256 * 5, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile143 = Tile('tiles.png', 256 * 6, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile144 = Tile('tiles.png', 256 * 7, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 1)


# ---------- Повтор всех карточек

tile145 = Tile('tiles.png', 256 * 0, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 0)
tile146 = Tile('tiles.png', 256 * 1, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile147 = Tile('tiles.png', 256 * 2, 256 * 0, [['N', 'W', 'E']], [['SSE'], ['SSW']], [['C', 'S']], 0, 1)
tile148 = Tile('tiles.png', 256 * 3, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile149 = Tile('tiles.png', 256 * 4, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile150 = Tile('tiles.png', 256 * 5, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile151 = Tile('tiles.png', 256 * 6, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile152 = Tile('tiles.png', 256 * 7, 256 * 0, [['N', 'W']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 1)
tile153 = Tile('tiles.png', 256 * 8, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile154 = Tile('tiles.png', 256 * 9, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile155 = Tile('tiles.png', 256 * 10, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 0)
tile156 = Tile('tiles.png', 256 * 11, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile157 = Tile('tiles.png', 256 * 12, 256 * 0, [['N', 'W']], [['SSW', 'ENE'], ['ESE', 'SSE']], [['E', 'S']], 0, 1)
tile158 = Tile('tiles.png', 256 * 13, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 0)
tile159 = Tile('tiles.png', 256 * 14, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)
tile160 = Tile('tiles.png', 256 * 15, 256 * 0, [['E', 'W']], [['SSE', 'SSW'], ['NNW', 'NNE']], [], 0, 1)

tile161 = Tile('tiles.png', 256 * 0, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile162 = Tile('tiles.png', 256 * 1, 256 * 1, [['W'], ['N']], [['SSE', 'SSW', 'ENE', 'ESE']], [], 0, 0)
tile163 = Tile('tiles.png', 256 * 2, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile164 = Tile('tiles.png', 256 * 3, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile165 = Tile('tiles.png', 256 * 4, 256 * 1, [['S'], ['N']], [['WNW', 'WSW', 'ENE', 'ESE']], [], 0, 0)
tile166 = Tile('tiles.png', 256 * 5, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile167 = Tile('tiles.png', 256 * 6, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile168 = Tile('tiles.png', 256 * 7, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile169 = Tile('tiles.png', 256 * 8, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile170 = Tile('tiles.png', 256 * 9, 256 * 1, [['N']], [['WNW', 'WSW', 'ENE', 'ESE', 'SSW', 'SSE']], [], 0, 0)
tile171 = Tile('tiles.png', 256 * 10, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile172 = Tile('tiles.png', 256 * 11, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile173 = Tile('tiles.png', 256 * 12, 256 * 1, [['N']], [['WSW', 'SSW'], ['WNW', 'ENE', 'ESE', 'SSE']], [['W', 'S']], 0,
              0)
tile174 = Tile('tiles.png', 256 * 13, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile175 = Tile('tiles.png', 256 * 14, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)
tile176 = Tile('tiles.png', 256 * 15, 256 * 1, [['N']], [['ESE', 'SSE'], ['ENE', 'WNW', 'WSW', 'SSW']], [['E', 'S']], 0,
              0)

tile177 = Tile('tiles.png', 256 * 0, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile178 = Tile('tiles.png', 256 * 1, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile179 = Tile('tiles.png', 256 * 2, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile180 = Tile('tiles.png', 256 * 3, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile181 = Tile('tiles.png', 256 * 4, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile182 = Tile('tiles.png', 256 * 5, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile183 = Tile('tiles.png', 256 * 6, 256 * 2, [['N']], [['ENE', 'WNW'], ['WSW', 'SSW', 'ESE', 'SSE']], [['W', 'E']], 0,
              0)
tile184 = Tile('tiles.png', 256 * 7, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile185 = Tile('tiles.png', 256 * 8, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile186 = Tile('tiles.png', 256 * 9, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile187 = Tile('tiles.png', 256 * 10, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile188 = Tile('tiles.png', 256 * 11, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile189 = Tile('tiles.png', 256 * 12, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile190 = Tile('tiles.png', 256 * 13, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile191 = Tile('tiles.png', 256 * 14, 256 * 2, [], [['NNW', 'WNW', 'WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE']],
              [['N', 'S']], 0, 0)
tile192 = Tile('tiles.png', 256 * 15, 256 * 2, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)

tile193 = Tile('tiles.png', 256 * 0, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile194 = Tile('tiles.png', 256 * 1, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile195 = Tile('tiles.png', 256 * 2, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile196 = Tile('tiles.png', 256 * 3, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile197 = Tile('tiles.png', 256 * 4, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile198 = Tile('tiles.png', 256 * 5, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile199 = Tile('tiles.png', 256 * 6, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile200 = Tile('tiles.png', 256 * 7, 256 * 3, [], [['WSW', 'SSW'], ['NNE', 'ENE', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['W', 'S']], 0, 0)
tile201 = Tile('tiles.png', 256 * 8, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile202 = Tile('tiles.png', 256 * 9, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile203 = Tile('tiles.png', 256 * 10, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile204 = Tile('tiles.png', 256 * 11, 256 * 3, [], [['ENE', 'WNW', 'NNE', 'NNW'], ['WSW', 'SSW'], ['ESE', 'SSE']],
              [['E', 'C'], ['W', 'C'], ['S', 'C']], 0, 0)
tile205 = Tile('tiles.png', 256 * 12, 256 * 3, [], [['ENE', 'NNE'], ['WSW', 'SSW'], ['ESE', 'SSE'], ['WNW', 'NNW']],
              [['E', 'C'], ['W', 'C'], ['S', 'C'], ['N', 'C']], 0, 0)
tile206 = Tile('tiles.png', 256 * 13, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile207 = Tile('tiles.png', 256 * 14, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile208 = Tile('tiles.png', 256 * 15, 256 * 3, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)

tile209 = Tile('tiles.png', 256 * 0, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']], [], 1, 0)
tile210 = Tile('tiles.png', 256 * 1, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile211 = Tile('tiles.png', 256 * 2, 256 * 4, [], [['ENE', 'NNE', 'WSW', 'SSW', 'ESE', 'SSE', 'WNW', 'NNW']],
              [['C', 'S']], 1, 0)
tile212 = Tile('tiles.png', 256 * 3, 256 * 4, [['N', 'E', 'S', 'W']], [], [], 0, 1)
tile213 = Tile('tiles.png', 256 * 4, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile214 = Tile('tiles.png', 256 * 5, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile215 = Tile('tiles.png', 256 * 6, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 0)
tile216 = Tile('tiles.png', 256 * 7, 256 * 4, [['N', 'E', 'W']], [['SSE', 'SSW']], [], 0, 1)
