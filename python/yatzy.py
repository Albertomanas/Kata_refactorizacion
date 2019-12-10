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

    def fours(*dices):
        total = 0
        FOUR = 4
        for die in dices:
            if die == FOUR:
                total += die
        return total

    def fives(*dices):
        total = 0
        FIVE = 5
        for die in dices:
            if die == FIVE:
                total += die
        return total

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
                else:
                    continue

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
        for die in range(6, 0, -1):
            if dices.count(die) >= THREE:
                return THREE * die
        return 0

    @staticmethod
    def four_of_a_kind(*dices):
        FOUR = 4
        for die in range(6, 0, -1):
            if dices.count(die) >= FOUR:
                return FOUR * die
        return 0

    @staticmethod
    def small_straight(*dices):
        for die in range(1, 6):
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
    def full_house(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
