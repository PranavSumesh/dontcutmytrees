import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    @staticmethod
    def get_right_hand_image():
        return pygame.image.load(ASSETS_DIR / "right_csaw.png").convert_alpha()

    @staticmethod
    def get_left_hand_image():
        return pygame.image.load(ASSETS_DIR / "left_csaw.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "tree1.png").convert_alpha()

    @staticmethod
    def get_dotted_line():
        return pygame.image.load(ASSETS_DIR / "dotted_line.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_main_hand():
        return pygame.image.load(ASSETS_DIR / "main_hand.png").convert_alpha()

    @staticmethod
    def get_score_backing():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_key.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title1.png").convert_alpha()

    @staticmethod
    def get_holding_gift_image():
        return pygame.image.load(MENU_DIR / "holding_gift.png").convert_alpha()

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 12)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 26)

    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Don't Cut My Trees")
        gift = VisualizationService.get_player_image()
        pygame.display.set_icon(gift)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualizationService.get_score_font()
        best_score = score_font.render(f"Best: {max_score}", True, (0, 0, 0))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 220))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 100)
        title = VisualizationService.get_title_image()
        screen.blit(title, (0, y))

    @staticmethod
    def draw_press_key(screen, press_y):
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (0, press_y))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)
