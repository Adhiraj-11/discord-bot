import discord
from discord import user
from discord.ext import commands
from PIL import  Image
from io import BytesIO
import random
import os

# bot = commands.Bot('yuzu ')

bot = commands.Bot(command_prefix=["yuzu ","Yuzu "])

# @bot.event
# async def on_message(message):
#     if bot.user.mentioned_in(message):
#         await message.channel.send('okay')

@bot.command()
async def hello(ctx):                       #asyncronus func, ansyc libray    #ctx context have everything u need to interact with user
    await ctx.reply("hello!")


@bot.command()
async def hi(ctx):                      
    await ctx.reply("hii")



@bot.command()
async def Help(ctx):                      
    await ctx.reply("I missed the part where thats my problem")


@bot.command()
async def avatar(ctx):
    if avatar.content == '!avatar':
        clientProfilePicture = avatar.author.avatar_url
        await avatar.channel.send(clientProfilePicture)


@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)


# @bot.event
# async def on_message(message):
#     mention = f'<@!{bot.user.id}>'
#     if mention in message.content:
#            await message.channel.send("My prefix is 'yuzu' :D")


@bot.command()
async def add(ctx, num1:int, num2:int):                      
    await ctx.reply(num1 + num2)


@bot.command()
async def purge(ctx, amount:int):
    if amount >100:
        await ctx.reply("limit's of 100;-;")
    else:
        await ctx.channel.purge(limit= amount)


@bot.command()
async def saanp(ctx, user : discord.Member = None):
    if user == None:
        await ctx.reply("Who is... the snake?")
    #user = ctx.author

    Snake = Image.open("snake1.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((449, 449))
    Snake.paste(pfp, (132, 10))

    #Snake.paste(pfp, (132:int, 10:int))

    Snake.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))

@bot.command()
async def rps(ctx):
    await ctx.reply("Choose, rock/paper/scissors")
    RPS = ["rock", "paper", "scissors"]

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in RPS

    user_choice = (await bot.wait_for('message', check=check)).content

    comp_choice = random.choice(RPS)

    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'sigh we tied..\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'HAH i won loser!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, fine you won that time!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'Lmaoo loserr\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f';-; We just tied. I call a rematch.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"ugh You win..\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA BICH!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')

token = os.environ['BOT_TOKEN']
bot.run(token)
#132 10
#449 449

   
















