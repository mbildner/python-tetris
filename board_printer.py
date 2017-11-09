class BoardPrinter(object):
    def __init__(self, number_of_cols):
        self.number_of_cols = number_of_cols

    def print_game_state(self, game_state):
        output = ""

        for row in game_state:
            output += "\n|"
            for col in row:
                if col:
                    output += str(int(col))
                else: output += " "
                output += " "
            output += "|"

        output += "\n"
        for _ in range(2 + (self.number_of_cols * 2)):
            output += "_"

        return output
