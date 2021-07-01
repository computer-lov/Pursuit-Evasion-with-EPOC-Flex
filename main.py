from cortex import Cortex
import webbrowser
from pynput.mouse import Button, Controller
import time
import subprocess

# This is the main file that will execute the tic-tac-toe game 

# TODO
# is it possible to use both the mental commands and the facial expressions in the same application?
# FIRST PLAY GAME AGAINST COMPUTER
# NEXT TRY TO PLAY 2-PLAYER VERSION OF GAME PROVIDED ON WEBSITE WITH TWO EPOC FLEX DEVICES!


class userSession():
    def __init__(self):
        user = {'client_id': 'BN6wnwY8b9ZKYAQmTUCJLHBx0UVQ1VE52QN4I9Ha', 'client_secret' : 'WSdbaAxrMqkNvqRvMYW8ZsLXWNuNb3XJGk4cnxXebQb3A43bl7L21AEvr7aiQqOepIo01K74ixfDSKPb1QBhUPPX9EOewegV4kYZCJceDiGBZFfAKrSN5MIpTQroOhg6', 
        'license' : 'd5b584b8-883e-421f-8bf5-cbe4bcb0ac72', 'debit' : 100}
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

    def determineAction(self, output):
        action = "neutral"
        desiredAction = str(output.strip())
        if "com" and "sid" and "time" in desiredAction:
            dataParse = desiredAction.split('"')
            action = dataParse[3]
        return action

    def executeAction(self, action):
        print("Execute: ", action)
        # go left
        if action == "left":
            self.moveMouseLeft()
        # go right
        elif action == "right":
            self.moveMouseRight()
        # go up
        elif action == "lift":
            self.moveMouseUp()
        # go down
        elif action == "drop":
            self.moveMouseDown()
        # left click on mouse
        elif action == "push":
            self.leftClickMouse()
        # else: neutral do nothing

    def close(self):
        self.userSession.disconnect_headset()
        self.userSession.close_session()


if __name__ == '__main__':
    openSession = userSession()
    openSession.openSession()
    # openSession.openWebsite()
    cont = True
    start = time.time()
    # runs live_advance.py file
    process = subprocess.Popen('live_advance.py', shell = True, stdout=subprocess.PIPE)
    count = 0
    actionList = []
    while cont:
        end = time.time() - start
        # collect each line of stdout from live_advance.py
        output = process.stdout.readline()
        time.sleep(0.1)
        if process.poll() is not None and output == '':
            cont = False
        if end >= 300: # if time > 5 mins
            cont = False
        if output:
            # determines action to be taken
            action = openSession.determineAction(output)
            # keeps track of amount of times action has occured
            actionList.append(action)
            if count == 0:
                count += 1
            elif actionList[count] == actionList[count-1]:
                count += 1
                # if it occurs over 10 times execute action
                if count >= 10:
                    count = 0
                    actionList.clear()
                    openSession.executeAction(action)
            else: # actionList[count] != actionList[count=1]
                count = 0
                actionList.clear()

    retval = process.poll()
    openSession.close()