import pygame

# 色の定義
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw_board(screen, player_pos):
    # 画面を白で塗りつぶす
    screen.fill(WHITE)

    # プレイヤーを描画
    player_size = 50
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    # 画面更新
    pygame.display.flip()
