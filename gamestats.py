from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class GameStats:

    def __init__(self) -> None:
        self.__score: int = 0
        self.__lives: int = 3

    def update_score(self, score_weight: int) -> None:
        
        self.__score += score_weight

    def get_score(self) -> int:

        return self.__score
    
    def update_lives(self, value: int) -> None:

        self.__lives += value

    def get_lives(self) -> int:

        return self.__lives
