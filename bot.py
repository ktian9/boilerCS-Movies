import discord
from discord.ext import commands
import datetime
dt = datetime.datetime.today()
import random
import os
import asyncio


TOKEN = 'NzkyNDM0NDgwNzM2NTAxNzYx.X-dqHg.VU4Usm3oD85KwkwmyMYe9bcmWq0'
client = commands.Bot(command_prefix = "!bcs ")



# Determines if bot is active or not
@client.event
async def on_ready():
    game = discord.Game("Type !bcs help for help")
    await client.change_presence(status=discord.Status.online, activity=game)
    print('bcs movie bot is ready!')


@client.command()
async def info(client, *message):
    embedVar = discord.Embed(
        title="boilerCS Movie Bot - Information", description="Stats and Movie Nights!", color=0xceb888)
    embedVar.add_field(name="Kevin", value="Sophomore @ Purdue University" +"\n" + "Kevin is Double majoring in Data Science and Statistics", inline=False)
    embedVar.add_field(name="Github", value="https://github.com/ktian9/boilerCS-Movies", inline=False)
    await client.send(embed=embedVar)

@client.command()
async def movieList(client, *message):
    embedVar = discord.Embed(
        title="boilerCS Movie List", description="List of Movies", color=0xceb888)
    for i in range(0, len(movieList)):
        if movieList[i]["status"] == "watched":
            embedVar.add_field(name= "[WATCHED] " +movieList[i]["movieTitle"],
                               value="ID: " + str(movieList[i]["id"]) + "\n" + "Suggested By: " + movieList[i]["suggestor"] +"\n" +
                               "Date Watched: " + str(movieList[i]["dateSeen"]),

                               inline=False)
        else:
            embedVar.add_field(name=movieList[i]["movieTitle"],
                               value="ID: " + str(movieList[i]["id"]) + "\n" + "Suggested By: " + movieList[i][
                                   "suggestor"] + "\n" +
                                     "Date Watched: " + str(movieList[i]["dateSeen"]),

                               inline=False)
    embedVar.set_footer(text = "◀ Back || Forwards ▶")

    sent = await client.send(embed=embedVar)
    await client.add_reaction(sent, emoji="\U000125C0")  # use the message object to add the reaction to
    await client.add_reaction(sent, emoji="\U000125B6")

@client.command()
#Format: !bcs add (0)title,(1),suggestor,(2)status,(3)date seen
async def add(client, *message):
    temp = message.split[","]
    if temp[2].lower() == "watched":
        formattedEntry = {"id": str(len(movieList)+1),
                          "movieTitle": temp[0],
                          "suggestor": temp[1],
                          "status": temp[2],
                          "dateSeen":temp[3]}
    else:
        formattedEntry = {"id": str(len(movieList) + 1),
                          "movieTitle": temp[0],
                          "suggestor": temp[1],
                          "status": "not watched",
                          "dateSeen": "NA"}
    movieList.append(formattedEntry)
    writeListToFile()
    openMovieList()
    await client.send("Movie added!")

# help command
@client.command()
async def h(client, *message):
    embedVar = discord.Embed(
        title="Blue Buff - Help", description="Commands", color=0x734f96)
    embedVar.add_field(name="!bbcreate <region> <summoner name>",
                       value="Creates an exercise routine",
                       inline=False)
    embedVar.add_field(name="!bbinfo",
                       value="Displays information about the bot and it's creators",
                       inline=False)
    embedVar.add_field(name="!bbcalc",
                       value="Displays formula and weighting used to generate workout",
                       inline=False)
    embedVar.add_field(name="!bbh",
                       value="Displays this page",
                       inline=False)
    await client.send(embed=embedVar)



### Helper Methods


#format:  id,movieTitle,suggestor,status,date watched (NA if not watched?)

#example:  1,Weathering With You,sorairo,watched,12/2/2001
movieList = []
def openMovieList():
    # Reads in movie list from file
    movieListFile = open("movielist.txt", "r")
    global movieList
    movieList = movieListFile.read().splitlines()
    print(movieList)
    movieListFile.close()
    for i in range(0, len(movieList)):
        temp = movieList[i].split(',')
        formattedEntry = { "id":temp[0],
                           "movieTitle":temp[1],
                           "suggestor": temp[2],
                           "status": temp[3],
                           "dateSeen":temp[4]}
        movieList[i] = formattedEntry

    print(movieList)

def writeListToFile():
    movieListFile = open("movielist.txt", "w")

    for i in range(0, len(movieList)):
        if movieList[i]["status"] == "watched":
            formattedEntry = movieList[i]["id"] + "," + movieList[i]["movieTitle"] \
                         + "," + movieList[i]["suggestor"] + "," + movieList[i]["status"] + "," + "NA" + "\n"
        else:
            formattedEntry = movieList[i]["id"] + "," + movieList[i]["movieTitle"] \
                             + "," + movieList[i]["suggestor"] + "," + movieList[i]["status"] + "," + movieList[i]["dateSeen"] + "\n"
        movieListFile.write(formattedEntry)
    movieListFile.close()




    #def createNewEntry(movieTitle, suggestor)

openMovieList()
print(len(movieList))

client.run(TOKEN)