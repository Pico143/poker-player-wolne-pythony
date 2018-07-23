import json
import traceback

class Player:
    VERSION = "The easily winning poker robot V6"

    def betRequest(self, game_state):
        index = game_state['in_action']
        try:
            if self.checkPairs(game_state):
                return 99999
            if self.checkFigures(game_state):
                return game_state['current_buy_in'] - game_state['players'][index]['bet'] + 11
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
                    if card['rank'] in ["A","K","Q","J"]:
                        return True
        return False

                


