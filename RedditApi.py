import aiohttp
import random
import time

headers = {"User-Agent": "KittenBot v0.1 u/thesimpsonss"}
kitten_url = "https://api.reddit.com/r/kittens"
cat_url = "https://api.reddit.com/r/cats"
kittens = []
cats = []
last_kitten_fetch = None
last_cat_fetch = None

async def initialize_kittens():
    global kittens
    global last_kitten_fetch
    last_kitten_fetch = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(kitten_url, headers=headers) as resp:
            jso = await resp.json()
            posts = jso["data"]["children"]
            kittens = []
            for post in posts:
                if ("post_hint" in post["data"] and
                    post["data"]["post_hint"] == "image"):
                    kittens.append(post["data"]["url"])
                    

async def initialize_cats():
    global cats
    global last_cat_fetch
    last_cat_fetch = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(cat_url, headers=headers) as resp:
            jso = await resp.json()
            posts = jso["data"]["children"]
            cats = []
            for post in posts:
                if ("post_hint" in post["data"] and
                    post["data"]["post_hint"] == "image"):
                    cats.append(post["data"]["url"])

async def get_random_kitten():
    if not last_kitten_fetch or time.time() > last_kitten_fetch + 1*60*60:
        await initialize_kittens()
    return random.choice(kittens)

async def get_random_cat():
    if not last_cat_fetch or time.time() > last_cat_fetch + 1*60*60:
        await initialize_cats()
    return random.choice(cats)
