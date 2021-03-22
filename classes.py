

class Character:
    def __init__(self):
        points = 0
        chosen_move = Gesture()

    def showdown(self, opponent):
        # run function for gesture


class Player(Character):
    def __init__(self):
        super().__init__()


class Cpu(Character):
    def __init__(self):
        super().__init__()


class Gesture:
    def __init__(self):
        name = ''
        wins_vs = []
        loses_vs = []

    def check_match(self, opposing_gesture):
        if opposing_gesture.name in self.wins_vs:
            return 'win'
        if opposing_gesture.name in self.loses_vs:
            return 'loss'
        if self.name == opposing_gesture.name:
            return 'tie'


class Game:
    def __init__(self):
        p1 = Character()
        p2 = Character()
        match = 0


class Rock(Gesture):
    def __init__(self):
        super().__init__()
        win_vs = ['']


class Paper(Gesture):
    def __init__(self):
        super().__init__()


class Scissors(Gesture):
    def __init__(self):
        super().__init__()


class Lizard(Gesture):
    def __init__(self):
        super().__init__()


class Spock(Gesture):
    def __init__(self):
        super().__init__()
