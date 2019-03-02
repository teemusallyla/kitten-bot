import discord
import datetime
from RedditApi import get_random_cat, get_random_kitten, refresh_lists
from RedditApi import get_premium_kitten, get_premium_cat, add_premium_kitten
from RedditApi import add_premium_cat

with open("token.txt") as f:
    token = f.readline().rstrip()
    dev_channel = f.readline().rstrip()

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

kitten_text = "Kittens incoming!"
cat_text = "Cats incoming!"

class KittenClient(discord.Client):
    async def on_message(self, message):
        if message.content.lower() in kitten_commands:
            await self.send_typing(message.channel)
            if message.channel.id == dev_channel:
                url = await get_random_kitten()
            else:
                url = await get_premium_kitten()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            msg = await self.send_message(
                message.channel,
                content=kitten_text,
                embed=emb)
            if message.channel.id == dev_channel:
                await self.add_reaction(msg, "👍")
            else:
                with open("log.log", "a+") as f:
                    f.write("{}: k!kittens by {} in {}\n".format(
                        datetime.datetime.now(),
                        message.author.name,
                        message.server))

        elif message.content.lower() in cat_commands:
            await self.send_typing(message.channel)
            if message.channel.id == dev_channel:
                url = await get_random_cat()
            else:
                url = await get_premium_cat()
            emb = discord.Embed(
                color=12127009
            ).set_image(url=url)
            msg = await self.send_message(
                message.channel,
                content=cat_text,
                embed=emb)
            if message.channel.id == dev_channel:
                await self.add_reaction(msg, "👍")
            else:
                with open("log.log", "a+") as f:
                    f.write("{}: k!cats by {} in {}\n".format(
                        datetime.datetime.now(),
                        message.author.name,
                        message.server))

        elif message.content.lower() == "k!refresh" and message.author == self.owner:
            await self.send_typing(message.channel)
            await refresh_lists()
            await self.send_message(message.channel, "Done!")

        elif message.content.lower() == "k!help":
            await self.send_message(
                message.channel,
                "I have only two commands: k!kittens and k!cats")

        elif message.content.lower() == "k!logs" and message.author == self.owner:
            log_length = 30
            with open("log.log") as f:
                lines = f.readlines()
                await self.send_message(
                    message.channel,
                    "```" + "".join(lines[-log_length:]) + "```")

    async def on_reaction_add(self, reaction, user):
        if reaction.message.author == self.user and user != self.user and reaction.emoji == "👍":
            msg = reaction.message
            if msg.embeds:
                url = msg.embeds[0]["image"]["url"]
                if url:
                    if msg.content == kitten_text:
                        await add_premium_kitten(url)
                    elif msg.content == cat_text:
                        await add_premium_cat(url)
                    await self.add_reaction(reaction.message, "✅")

    async def on_ready(self):
        game = discord.Game(name="k!kittens")
        print("Kitten bot ready for action!")
        await self.change_presence(game=game)
        appinfo = await self.application_info()
        self.owner = appinfo.owner


kittenClient = KittenClient()
kittenClient.run(token)
print("Kitten bot down! Send reinforcements!")
