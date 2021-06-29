from cortex import Cortex
import webbrowser
# import sub_data
# import train
# import facial_expression
# import train_advance 
# import live_advance
# import record 
# import marker

# from pynput.mouse import Button, Controller

# This is the main file that will execute the tic-tac-toe game 
# try to finish this by end of next week 7/1

# TODO
# WRITE CODE TO RECIEVE TRAINING DATA
# WRITE CODE TO TRANSLATE TRAINING DATA PROVIDED FROM EMOTIV FLEX INTO MOUSE ACTIONS
# FIRST PLAY GAME AGAINST COMPUTER
# NEXT TRY TO PLAY 2-PLAYER VERSION OF GAME PROVIDED ON WEBSITE WITH TWO EPOC FLEX DEVICES!



class userSession():
    def __init__(self):
        user = {'client_id': 'BN6wnwY8b9ZKYAQmTUCJLHBx0UVQ1VE52QN4I9Ha', 'client_secret' : 'WSdbaAxrMqkNvqRvMYW8ZsLXWNuNb3XJGk4cnxXebQb3A43bl7L21AEvr7aiQqOepIo01K74ixfDSKPb1QBhUPPX9EOewegV4kYZCJceDiGBZFfAKrSN5MIpTQroOhg6', 
        'license' : 'd5b584b8-883e-421f-8bf5-cbe4bcb0ac72', 'debit' : 0}
        self.userSession = Cortex(user)

    # creates a session for the user
    def openSession(self):
        # request access
        self.userSession.request_access()
        # query headset
        self.userSession.query_headset()
        # control device
        self.userSession.connect_headset()
        # authorize 
        authToken = self.userSession.authorize()
        # create session
        self.userSession.create_session(authToken, "active")


    # open website where tictactoe game will be played
    def openWebsite(self):
        webbrowser.open('https://playtictactoe.org/')





if __name__ == "__main__":
    openSession = userSession()
    openSession.openSession()
    openSession.openWebsite()



