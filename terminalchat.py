#!/usr/bin/env python3
# TerminalChat, Twitch Chat In Linux Terminal

# Requirements
import os
import npyscreen
from twitchio.ext import commands


# Pulling chat
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=os.environ['TMI_TOKEN'],client_id=os.environ['CLIENT_ID'],nick=os.environ['BOT_NICK'], prefix=os.environ['BOT_PREFIX'],initial_channels=[os.environ['CHANNEL']])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        Author = (message.author.name)
        Message = (message.content)
        print(Author + ": " + Message)

# Pulling chat list


# Pull Twitch Badages
async def get_userbadges()


# Creating UI layout
class FormObject(npyscreen.Form):
    def create(self):
        pass

    def afterEditing(self):
    	self.parentApp.setNextForm(None)

class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', FormObject, name = "TerminalChat | Twitch Chat In Linux Terminal")


if( __name__ == "__main__" ):
    #app = App().run()
    bot = Bot()
    bot.run()




# Chat message input&send
