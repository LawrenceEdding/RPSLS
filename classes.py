

class Character:
    def __init__(self):
        self.points = 0
        self.chosen_move = Gesture()

    def showdown(self, opponent):
        outcome = self.chosen_move.check_match(self.chosen_move, opponent.chosen_move)
        # run function for gesture


class Player(Character):
    def __init__(self):
        super().__init__()


class Cpu(Character):
    def __init__(self):
        super().__init__()


class Gesture:
    def __init__(self):
        self.name = ''
        self.wins_vs = []
        self.loses_vs = []

    def assign_gesture(self, name, wins, loses):
        self.name = name
        self.wins_vs = wins
        self.loses_vs = loses

    def check_match(self, opposing_gesture):
        if opposing_gesture.name in self.wins_vs:
            return 'win'
        if opposing_gesture.name in self.loses_vs:
            return 'loss'
        if self.name == opposing_gesture.name:
            return 'tie'


class Game:
    def __init__(self):
        self.p1 = Character()
        self.p2 = Character()
        self.match = 0


class Rock(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('rock', ['scissors', 'lizard'], ['paper', 'spock'])


class Paper(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('paper', ['rock', 'spock'], ['scissors', 'lizard'])


class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('scissors', ['paper', 'lizard'], ['rock', 'spock'])


class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('lizard', ['spock', 'paper'], ['rock', 'scissors'])


class Spock(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('spock', ['scissors', 'rock'], ['paper', 'lizard'])
