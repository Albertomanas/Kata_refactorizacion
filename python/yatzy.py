class Yatzy:
    def __init__(self, *dices):
        self.dices = list(dices)

    @staticmethod
    def chance(*dices):
        total = 0
        for die in dices:
            total += die
        return total

    @staticmethod
    def yatzy(dices):
        for die in dices:
            value = dices[0]
            value -= die
            if value != 0:
                return 0
        return 50

    @staticmethod
    def ones(*dices):
        total = 0
        ONE = 1
        for die in dices:
            if die == ONE:
                total += die
        return total

    @staticmethod
    def twos(*dices):
        total = 0
        TWO = 2
        for die in dices:
            if die == TWO:
                total += die
        return total

    @staticmethod
    def threes(*dices):
        total = 0
        THREE = 3
        for die in dices:
            if die == THREE:
                total += die
        return total

    @staticmethod
    def fours(*dices):
        total = 0
        FOUR = 4
        for die in dices:
            if die == FOUR:
                total += die
        return total

    @staticmethod
    def fives(*dices):
        total = 0
        FIVE = 5
        for die in dices:
            if die == FIVE:
                total += die
        return total

    @staticmethod
    def sixes(*dices):
        total = 0
        SIX = 6
        for die in dices:
            if die == SIX:
                total += die
        return total

    @staticmethod
    def score_pair(*dices):
        lista = []
        for die in dices:
            if dices.count(die) > 1:
                if lista.count(die) == 0:
                    lista.append(die)
        if lista == []:
            return 0
        else:
            lista.sort()
            return lista[-1] * 2

    @staticmethod
    def two_pair(*dices):
        pairs = 0
        score = 0
        number = 1
        while pairs <= 2 and number <= (len(dices) + 1):
            if dices.count(number) >= 2:
                pairs += 1
                score += 2 * number
            number += 1
            if pairs == 2:
                return score
        return 0

    @staticmethod
    def three_of_a_kind(*dices):
        THREE = 3
        for die in range(len(dices), 0, -1):
            if dices.count(die) >= THREE:
                return THREE * die
        return 0

    @staticmethod
    def four_of_a_kind(*dices):
        FOUR = 4
        for die in range(len(dices), 0, -1):
            if dices.count(die) >= FOUR:
                return FOUR * die
        return 0

    @staticmethod
    def small_straight(*dices):
        for die in range(1, len(dices)):
            if dices.count(die) != 1:
                return 0
        return 15

    @staticmethod
    def large_straight(*dices):
        for die in range(2, 7):
            if dices.count(die) != 1:
                return 0
        return 20

    @staticmethod
    def full_house(*dices):
        number_list = []
        for die in dices:
            if dices.count(die) in (2, 3):
                number_list.append(die)
        return sum(number_list)
