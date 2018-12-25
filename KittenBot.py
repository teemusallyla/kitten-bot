import discord
import datetime
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
            await self.send_typing(message.channel)
            url = await get_random_kitten()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(
                message.channel,
                content="Kittens incoming!",
                embed=emb)
            with open("log.log", "a+") as f:
                f.write("{}: k!kittens by {} in {}\n".format(
                    datetime.datetime.now(),
                    message.author.name,
                    message.server))

        elif message.content in cat_commands:
            await self.send_typing(message.channel)
            url = await get_random_cat()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            await self.send_message(
                message.channel,
                content="Cats incoming!",
                embed=emb)
            with open("log.log", "a+") as f:
                f.write("{}: k!cats by {} in {}\n".format(
                    datetime.datetime.now(),
                    message.author.name,
                    message.server))

        elif message.content == "k!refresh" and message.author == self.owner:
            await self.send_typing(message.channel)
            await refresh_lists()
            await self.send_message(message.channel, "Done!")

        elif message.content == "k!help":
            await self.send_message(
                message.channel,
                "I have only two commands: k!kittens and k!cats")

        elif message.content == "k!logs" and message.author == self.owner:
            log_length = 30
            with open("log.log") as f:
                lines = f.readlines()
                await self.send_message(
                    message.channel,
                    "```" + "".join(lines[-log_length:]) + "```")

    async def on_ready(self):
        game = discord.Game(name="k!kittens")
        print("Kitten bot ready for action!")
        await self.change_presence(game=game)
        appinfo = await self.application_info()
        self.owner = appinfo.owner


kittenClient = KittenClient()
kittenClient.run(token)
print("Kitten bot down! Send reinforcements!")
