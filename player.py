import json

class Player:
    VERSION = "The easily winning poker robot V2"
     
    def betRequest(self, game_state):
        print game_state
        return 500000

    def showdown(self, game_state):
        pass

    def evaluateHand(self, gameStateObject):
        playersList = gameStateObject.players
        for player in playersList:
            if player.name == "Wolne Pythony":
                if player.hole_cards[0].rank == player.hole_cards[1].rank:
                    return True
                for card in player.hole_cards:
                    if card.rank in ["A","K","Q","J"]:
                        return True
        return False

                


