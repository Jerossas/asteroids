from constants import ASTEROID_KINDS, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class GameStats:

    def __init__(self) -> None:
        self.__score: int = 0

    def update_score(self, score_weight: int) -> None:
        
        self.__score += score_weight

    def get_score(self) -> int:

        return self.__score
