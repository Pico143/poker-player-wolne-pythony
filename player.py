import json

class Player:
    VERSION = "The easily winning poker robot V4"
     
    def betRequest(self, game_state):
        if self.evaluateHand(game_state):
            return 500000
        else:
            return 0

    def showdown(self, game_state):
        pass

    def evaluateHand(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                print "NAME WAS WOLNE PYTHONY"
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank']:
                    print "RANKS WERE THE SAME"
                    return True
                for card in player.hole_cards:
                    if card.rank in ["A","K","Q","J"]:
                        print "WE HAD A FIGURE"
                        return True
        return False

                


