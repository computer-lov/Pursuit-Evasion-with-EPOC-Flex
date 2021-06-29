from cortex import Cortex
import webbrowser
from pynput.mouse import Button, Controller
import time

# This is the main file that will execute the tic-tac-toe game 
# try to finish this by end of next week 7/1

# TODO
# NEED TO WRITE CODE TO ENABLE LEFT-CLICK DURING GAME PLAY
# FIRST PLAY GAME AGAINST COMPUTER
# NEXT TRY TO PLAY 2-PLAYER VERSION OF GAME PROVIDED ON WEBSITE WITH TWO EPOC FLEX DEVICES!


class userSession():
    def __init__(self):
        user = {'client_id': 'BN6wnwY8b9ZKYAQmTUCJLHBx0UVQ1VE52QN4I9Ha', 'client_secret' : 'WSdbaAxrMqkNvqRvMYW8ZsLXWNuNb3XJGk4cnxXebQb3A43bl7L21AEvr7aiQqOepIo01K74ixfDSKPb1QBhUPPX9EOewegV4kYZCJceDiGBZFfAKrSN5MIpTQroOhg6', 
        'license' : 'd5b584b8-883e-421f-8bf5-cbe4bcb0ac72', 'debit' : 0}
        self.userSession = Cortex(user)
        self.mouse = Controller()

    # creates a session for the user
    def openSession(self):
        # request access / query headset / control device / authorize / create session
           self.userSession.do_prepare_steps()

    # open website where tictactoe game will be played
    def openWebsite(self):
        self.mouse.position = (1277, 672)
        webbrowser.open('https://playtictactoe.org/')

    # starts live session
    def goLive(self, profile_name):
        # go live
        self.userSession.setup_profile(profile_name, status='load')
        self.userSession.sub_request(stream=['com'])
        
    # moves the mouse to the left
    def moveMouseLeft(self):
        self.mouse.move(-205, 0)
        if (self.mouse.position[0] <= 965):
            self.mouse.position[0] += 637

    # moves the mouse to the right
    def moveMouseRight(self):
        self.mouse.move(205, 0)
        if (self.mouse.position[0] >= 1602):
            self.mouse.position[0] -= 637

    # moves the mouse up
    def moveMouseUp(self):
        self.mouse.move(0, -212)
        if (self.mouse.position[1] <= 362):
            self.mouse.position[1] += 616

    # moves the mouse down
    def moveMouseDown(self):
        self.mouse.move(0, 212)
        if (self.mouse.position[1] >= 978):
            self.mouse.position[1] -= 616

    # press and release left mouse button
    def leftClickMouse(self):
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    def determineAction(self):
        desiredAction = self.userSession.get_mental_command_active_action()
    
        for action in desiredAction['result']:
            if action == "push":
                self.moveMouseLeft()
            elif action == "pull":
                self.moveMouseRight()
            elif action == "lift":
                self.moveMouseUp()
            elif action == "drop":
                self.mouseMouseDown()
            # else:  neutral do nothing

        # need to write code to determine left-click action

    def close(self):
        self.userSession.disconnect_headset()
        self.userSession.close_session()


if __name__ == '__main__':
    openSession = userSession()
    openSession.openSession()
    openSession.openWebsite()
    openSession.goLive('EmotivBCI-Andrew Paul Mayer')
    cont = True;
    start = time.time()
    while cont:
        openSession.determineAction()
        end = time.time() - start
        if end >= 60:
            cont = False

    openSession.close()



