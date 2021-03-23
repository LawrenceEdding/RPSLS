

class Character:
    def __init__(self):
        self.points = 0
        self.chosen_move = Gesture()

    def showdown(self, opponent):
        outcome = self.chosen_move.check_match(self.chosen_move, opponent.chosen_move)
        if outcome == 'win':
            self.points += 1
            self.chosen_move.win_term(opponent.chosen_move.name)
        elif outcome == 'loss':
            opponent.points += 1
            opponent.chosen_move.win_term(self.chosen_move.name)

        elif outcome == 'tie':
            print(f'DRAW!')
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
        self.win_text = []

    def assign_gesture(self, name, wins, loses, text):
        self.name = name
        self.wins_vs = wins
        self.loses_vs = loses
        self.win_text = text

    def win_term(self, loser_name):
        victory_index = self.loses_vs.index(loser_name)
        print(f'{self.name} {self.win_text[victory_index]} {loser_name}')

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
        super().assign_gesture('rock', ['scissors', 'lizard'], ['paper', 'spock'], ['crushes', 'crushes'])


class Paper(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('paper', ['rock', 'spock'], ['scissors', 'lizard'], ['covers', 'disproves'])


class Scissors(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('scissors', ['paper', 'lizard'], ['rock', 'spock'], ['cuts', 'decapitates'])


class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('lizard', ['spock', 'paper'], ['rock', 'scissors'], ['poisons', 'eats'])


class Spock(Gesture):
    def __init__(self):
        super().__init__()
        super().assign_gesture('spock', ['scissors', 'rock'], ['paper', 'lizard'], ['smashes', 'vaporizes'])
