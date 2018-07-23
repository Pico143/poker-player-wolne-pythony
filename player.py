import json
import traceback


class Player:
    VERSION = "The easily winning poker robot V9"

    def betRequest(self, game_state):
        playerIndex = game_state['in_action']
        try:
            if self.checkHigherPairs(game_state) or self.top10Hand(game_state, playerIndex):
                return 99999
            if self.checkFigures(game_state) or checkLowerPairs(game_state):
                if current_buy_in - players[playerIndex]['bet'] <= 300:
                    return current_buy_in - players[playerIndex]['bet']
            return 0
        except:
            traceback.print_exc()
            return 999999

    def showdown(self, game_state):
        pass

    def checkLowerPairs(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank'] and player['hole_cards'][0]['rank'] in ["2","3","4","5","6"]:
                    return True

    def checkHigherPairs(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                if player['hole_cards'][0]['rank'] == player['hole_cards'][1]['rank'] and player['hole_cards'][0]['rank'] not in ["2","3","4","5","6"]:
                    return True

    def checkFigures(self, game_state):
        playersList = game_state['players']
        for player in playersList:
            if player['name'] == "Wolne Pythony":
                for card in player['hole_cards']:
                    if card['rank'] in ["A", "K", "Q", "J"]:
                        return True
        return False

    def top10Hand(self, game_state, playerIndex):
        player = game_state['players'][playerIndex]
        if str(player['hole_cards'][0]) in ["A", "K", "Q", "J", "10"]:
            if str(player['hole_cards'][1]) in ["A", "K", "Q", "J", "10"]:
                return True
        return False

                
    def activePlayers(self, game_state):
        numberOfPlayers = 0
        for player in game_state['players']:
            if player['status'] == 'active':
                numberOfPlayers += 1
        return numberOfPlayers



