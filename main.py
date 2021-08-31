import discord
import requests
import json
import os
import random
from keep_alive import keep_alive
client=discord.Client()
fav_list=[]
@client.event
async def on_ready():
  print(f"Bot Has Successfully Logged In As {client.user}")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='^help'))
@client.event
async def on_message(message):
  msg=message.content
  if message.content.startswith("^hello") or msg.startswith("^hi"):
    await message.channel.send("Hello !")
  if msg.startswith("^info"):
    name=msg.replace("^info","")
    embed=discord.Embed(title=f"{name.title()}")
    name=name.replace(" ","")
    api=requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text
    try:
      api=json.loads(api)
    except:
      new_embed=discord.Embed(title=f"{name.title()}",description=f"Cannot Find {name.title()} :frowning:")
      new_embed.set_footer(text=f"Requested By : {message.author.name}")
      await message.reply(embed=new_embed)
    t=api["abilities"]
    try:
      for i in t[0]["ability"].values():
        first_ability=i
        break
      for i in t[1]["ability"].values():
        second_ability=i
        break
    except:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      embed.set_thumbnail(url=front_image)
      back_image=api["sprites"]["back_default"]
      embed.add_field(name="First Ability",value=first_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience,inline=False)
      embed.set_footer(text=f"Requested By : {message.author.name}")
    else:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      embed.set_thumbnail(url=front_image)
      back_image=api["sprites"]["back_default"]
      embed.add_field(name="First Ability",value=first_ability,inline=False)
      embed.add_field(name="Second Ability",value=second_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience,inline=False)
      embed.set_footer(text=f"Requested By : {message.author.name}")
    await message.reply(embed=embed)
  if msg.startswith("^help"):
    embed=discord.Embed(title="Commands")
    embed.add_field(name="^hello",value="Bot Will Say Hello !",inline=False)
    embed.add_field(name="^spawn",value="Bot Will Spawn A Random Pokémon",inline=False)
    embed.add_field(name="^info {Pokémon name(string)}",value="Bot Will Return Provided Pokémon's Info",inline=False)
    embed.add_field(name="^code",value="Bot Will Return It's Source Code",inline=False)
    embed.add_field(name="^about",value="Bot Will Return About It")
    embed.add_field(name="^random",value="Bot Will Return Name Of Random Pokémon",inline=False)
    embed.add_field(name="^fav {Pokémon Name(string)}",value="Bot Will Add Provided Pokémon's Name In Database",inline=False)
    embed.add_field(name="^show fav",value="Bot Will Return List Of Favourite Pokémons",inline=False)
    embed.add_field(name="^remove {Index(integer)}",value="Bot Will Remove Provided Pokémon Name From Favourites",inline=False)
    embed.add_field(name="^total",value="Bot Will Return Total Number Of Pokémons",inline=False)
    embed.set_footer(text=f"Requested By : {message.author.name}")
    await message.reply(embed=embed)
  if msg.startswith("^about"):
    about="PokéBot\nCopyright Abhimanyu Sharma AKA N1nja0p #8172\nAn Open Source Pokédex Using PokéAPI\nCoded In 100% Pure Python, Using DiscordPy\nCheck My Other Softwares Too :\nhttps://angry-dijkstra-87d8ed.netlify.app/"
    embed.set_footer(text=f"Requested By : {message.author.name}")
    embed=discord.Embed(title="About",description=about)
    await message.reply(embed=embed)
  if msg.startswith("^code"):
    embed=discord.Embed(title="Repo Link", description='https://replit.com/@N1nja0p/PokeBot#main.py')
    embed.set_footer(text=f"Requested By : {message.author.name}")
    await message.channel.send(embed=embed)
  if msg.startswith("^random"):
    a=requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit=1118").text
    a=json.loads(a)
    pokemonlist=[]
    for i in a["results"]:
      pokemonlist.append(i["name"])
    name=random.choice(pokemonlist)
    embed=discord.Embed(title=f"{name.title()}")
    embed.set_footer(text=f"Requested By : {message.author.name}")
    api=requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").text
    api=json.loads(api)
    t=api["abilities"]
    try:
      for i in t[0]["ability"].values():
        first_ability=i
        break
      for i in t[1]["ability"].values():
        second_ability=i
        break
    except:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      embed.set_thumbnail(url=front_image)
      back_image=api["sprites"]["back_default"]
      embed.add_field(name="First Ability",value=first_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience,inline=False)
      embed.set_footer(text=f"Requested By : {message.author.name}")
    else:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      embed.set_thumbnail(url=front_image)
      back_image=api["sprites"]["back_default"]
      embed.add_field(name="First Ability",value=first_ability,inline=False)
      embed.add_field(name="Second Ability",value=second_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience,inline=False)
      embed.set_footer(text=f"Requested By : {message.author.name}")
    await message.reply(embed=embed)
  if msg.startswith("^fav"):
    msg=msg.replace("^fav","")
    msg=msg.replace(" ","")
    if msg in fav_list:
        err_embed=discord.Embed(title=f"{msg.title()}",description="Is Already In Your Favourites List. Must Be A Typo :smile:")
        err_embed.set_footer(text=f"Requested By : {message.author.name}")
        await message.reply(embed=err_embed)
    else:
        embed=discord.Embed(title=f"{msg.title()}",description="Added To Your Favourites :smile:")
        embed.set_footer(text=f"Requested By : {message.author.name}")
        embed.add_field(name="To View Your Favourites, Type",value="^show fav",inline=False)
    fav_list.append(msg)
    await message.reply(embed=embed)
  if msg.startswith("^show fav"):
      embed=discord.Embed(title="Favourites List",description=fav_list)
      embed.set_footer(text=f"Requested By : {message.author.name}")
      await message.reply(embed=embed)
  if msg.startswith("^remove"):
    msg=msg.replace("^remove","")
    msg=msg.replace(" ","")
    embed=discord.Embed()
    embed.set_footer(text=f"Requested By : {message.author.name}")
    try:
      del fav_list[int(msg)]
    except:
      embed.add_field(name="It Looks Like You Have'nt Added Anything To Your Favourites :frowning:",value=" To Add One, Type \"^fav {Pokémon Name}\" To Add :smile:")
    else:
      embed.add_field(name="Pokémon Name Was Successfully Removed From Your Favourites\nNow Your Favourite Pokémon List Looks Like This :smile: :",value=fav_list)
    await message.reply(embed=embed)
  if msg.startswith("^total"):
    embed=discord.Embed()
    a=requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit={1118}").text
    a=json.loads(a)
    embed.add_field(name="Total Pokémons",value=str(a["count"]),inline=False)
    embed.set_footer(text=f"Requested By : {message.author.name}")
    await message.reply(embed=embed)
  if msg.startswith("^spawn"):
    embed=discord.Embed(title="A Wild Pokémon Appeared :face_with_monocle: :star_struck:. Catch To View Its Stats").set_footer(f"Requested By {message.author.name}")
    embed.set_image(url="https://cdn.discordapp.com/attachments/882239270809657425/882282576742600744/giphy.gif")
    embed.add_field(name="Catch?",value="^Y/^N (Case Sensetive!)",inline=False)
    await message.reply(embed=embed)
  if msg.startswith("^Y"):
    a=requests.get(f"https://pokeapi.co/api/v2/pokemon/?limit=1118").text
    a=json.loads(a)
    pokemonlist=[]
    for i in a["results"]:
      pokemonlist.append(i["name"])
    random_poke=random.choice(pokemonlist)
    api=requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_poke}").text
    api=json.loads(api)
    t=api["abilities"]
    embed=discord.Embed(title=f"{random_poke.title()}")
    try:
      for i in t[0]["ability"].values():
        first_ability=i
        break
      for i in t[1]["ability"].values():
        second_ability=i
        break
    except:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      back_image=api["sprites"]["back_default"]
      embed.set_thumbnail(url=front_image)
      embed.add_field(name="First Ablity",value=first_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience)
      embed.set_footer(text=f"Requested By : {message.author.name}")
      embed.add_field(name="Congratulations :partying_face: !",value=f"You Catched {random_poke} !",inline=False)
    else:
      base_experience=api["base_experience"]
      height=api["height"]/1000
      weight=api["weight"]/1000
      front_image=api["sprites"]["front_default"]
      back_image=api["sprites"]["back_default"]
      embed.set_thumbnail(url=front_image)
      embed.add_field(name="First Ablity",value=first_ability,inline=False)
      embed.add_field(name="Second Ablity",value=second_ability,inline=False)
      embed.add_field(name="Height",value=height,inline=False)
      embed.add_field(name="Weight",value=weight,inline=False)
      embed.add_field(name="Base Experience",value=base_experience)
      embed.set_footer(text=f"Requested By : {message.author.name}")
      embed.add_field(name="Congratulations :partying_face: !",value=f"You Catched {random_poke} !",inline=False)
    await message.reply(embed=embed)
  if msg.startswith("^N"):
    new_embed=discord.Embed(title="Denied :pensive:")
    await message.channel.send(embed=new_embed)
if __name__ == "__main__":
  keep_alive()
  client.run(os.getenv("TOKEN"))
