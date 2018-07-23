import json

class Player:
    VERSION = "The easily winning poker robot V1"
     
    def betRequest(self, game_state):
        gameStateObject = json.load(game_state)
        return 500000

    def showdown(self, game_state):
        pass

