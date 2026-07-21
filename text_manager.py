import pygame

class TextManager():

    def __init__(self):
        
        self.font: pygame.font.Font = pygame.font.SysFont(None, 32, False, False)
    
    def create_text_image(self, text: str, color: tuple[int, int, int], antialias = True, background = None) -> pygame.Surface:        
        return self.font.render(text, antialias, color, background)

