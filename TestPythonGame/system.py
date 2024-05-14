import pygame

def init_window():
    # ゲーム初期化
    pygame.init()

    # 画面サイズ設定
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Simple RPG Game')

    # クロックオブジェクト
    clock = pygame.time.Clock()

    return screen, clock
