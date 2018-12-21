import discord
from RedditApi import get_random_cat, get_random_kitten, refresh_lists

with open("token.txt") as f:
    token = f.read()

kitten_commands = [
    "k!kittens",
    "k!kitten",
    "k!kitty",
    "k!kitties"
]
cat_commands = [
    "k!cats",
    "k!cat",
    "k!catty",
    "k!catties"
]

class KittenClient(discord.Client):
    async def on_message(self, message):
        if message.content in kitten_commands:
            url = await get_random_kitten()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(message.channel, content="Kittens incoming!", embed=emb)
        elif message.content in cat_commands:
            url = await get_random_cat()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(message.channel, content="Cats incoming!", embed=emb)
        elif message.content == "k!refresh":
            await refresh_lists()
            await self.send_message(message.channel, "Done!")
        elif message.content == "k!help":
            await self.send_message(message.channel, "I have only two commands: k!kittens and k!cats")

    async def on_ready(self):
        print("Kitten bot ready for action!")


kittenClient = KittenClient()
kittenClient.run(token)
print("Kitten bot down! Send reinforcements!")
