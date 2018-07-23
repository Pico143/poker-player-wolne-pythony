import json
import traceback


class Player:
    VERSION = "The easily winning poker robot V7"

    def betRequest(self, game_state):
        playerIndex = game_state['in_action']
        activ
        try:
            if self.checkPairs(game_state):
                return 99999
            return 0
        except:
            traceback.print_exc()
            return 999999

    def showdown(self, game_state):
        pass

    def checkPairs(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank']:
                    return True

    def checkFigures(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                for card in player['hole_cards']:
                    if card['rank'] in ["A", "K", "Q", "J"]:
                        return True
        return False


                


