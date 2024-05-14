import pygame
from system import init_window
from board import draw_board
from event import handle_events

def main():
    # 初期化
    screen, clock = init_window()

    # プレイヤー設定
    player_pos = [screen.get_width() // 2, screen.get_height() // 2]
    player_speed = 5

    # メインゲームループ
    running = True
    while running:
        running = handle_events(player_pos, player_speed)
        draw_board(screen, player_pos)
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
