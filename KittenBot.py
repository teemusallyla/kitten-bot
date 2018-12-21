import discord
from RedditApi import *

with open("token.txt") as f:
    token = f.read()

class KittenClient(discord.Client):

    async def on_message(self, message):
        if message.content == "k!kittens":
            url = await get_random_kitten()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(message.channel, content="Kittens incoming!", embed=emb)
        elif message.content == "k!cats":
            url = await get_random_cat()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(message.channel, content="Cats incoming!", embed=emb)
        elif message.content == "k!refresh":
            await initialize_kittens()
            await initialize_cats()
            await self.send_message(message.channel, "Done!")
        elif message.content == "k!help":
            await self.send_message(message.channel, "I have only two commands: k!kittens and k!cats")

    async def on_ready(self):
        print("Kitten bot ready for action!")


kittenClient = KittenClient()

kittenClient.run(token)
print("Kitten bot down! Send reinforcements!")
