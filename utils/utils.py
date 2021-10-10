import pygame

def render_image(window, img_path, point):
    img = pygame.image.load(img_path)
    window.blit(img, (point.x, point.y))

def render_text(window, text, point):

    font = pygame.font.SysFont("arial", 20)
    text = font.render(text, True, (0, 0, 0))

    text_rect = text.get_rect()
    text_rect.center = (point.x, point.y)

    window.blit(text, text_rect)
