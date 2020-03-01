import env_file
import discord
from Draw import Draw
from Poker import Poker
from Player import Player

class MyClient(discord.Client):
    game = None
    drawing = Draw()

    def seekUsers(self,ids):
        for i in range(len(ids)):
            if type(ids[i]) is str:
                data = ids[i].split("#")
                ids[i] = discord.utils.get(self.get_all_members(), name=data[0], discriminator=data[1])
        return ids

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print(str(message.author)+": "+message.content)
        if message.author == self.user or message.guild == None or message.guild.id != 166679130228785152:
            return
        
        if message.content == '#init' or message.content == "#play" or message.content == "#start":
            if self.game == None:
                ids = self.seekUsers(["Satsuwu#4597",message.author,"Knowle#3321"])
                self.game = Poker([Player(x) for x in ids])
                self.game.start()
                for player in self.game.players:
                    image = discord.File(self.drawing.draw(player.cards,player.id.id))
                    await player.id.send("Those are your cards",file=image)
            else:
                await message.channel.send("A game is already in progress")
        elif message.content == '#pass' or message.content == '#next':
            if self.game != None:
                result = self.game.next()
                if result == None:
                    image = discord.File(self.drawing.draw(self.game.tableCards))
                    await message.channel.send("Current table cards",file=image)
                else:
                    await message.channel.send("The winners are: "+", ".join([str(p.id) for p in result]))
                    self.game = None
            else:
                await message.channel.send("There is no game in progress")

enviroment = env_file.get()
client = MyClient()
client.run(enviroment.get("DISCORD_TOKEN"))