import discord
from discord import user
from discord.ext import commands
from PIL import  Image
from io import BytesIO
import random

bot = commands.Bot('yuzu ')

@bot.command()
async def hello(ctx):                       #asyncronus func, ansyc libray    #ctx context have everything u need to interact with user
    await ctx.reply("hello!")

@bot.command()
async def hi(ctx):                      
    await ctx.reply("hello!")

@bot.command()
async def h(ctx):                      
    await ctx.reply("hello!")

# @bot.command()
# async def on_message(message):
#     mention = f'<@!{bot.user.id}>'
#     if mention in message.content:
#         await message.channel.send("My prefix is 'yuzu' :D")

@bot.command()
async def add(ctx, num1:int, num2:int):                      
    await ctx.reply(num1 + num2)


@bot.command()
async def saanp(ctx, user : discord.Member = None):
    if user == None:
        await ctx.reply("Who is...the snake?")
    user = ctx.author

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

    # if user_choice == 'rock':
    #     if comp_choice == 'rock':
    #         await ctx.reply('Well, that was weird. We tied.\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'paper':
    #         await ctx.reply('HAH, I won that time!!\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'scissors':
    #         await ctx.reply("Aw, you beat me. It won't happen again!\nYour choice: ", user_choice, '\nMy choice: ', comp_choice)
    # elif user_choice == 'paper':
    #     if comp_choice == 'rock':
    #         await ctx.reply('The pen beats the sword? More like the paper beats the rock!!\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'paper':
    #         await ctx.reply('Oh, wacky. We just tied. I call a rematch!!\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'scissors':
    #         await ctx.reply("Aw man, you actually managed to beat me.\nYour choice: ", user_choice, '\nMy choice: ', comp_choice)

    # elif user_choice == 'scissors':
    #     if comp_choice == 'rock':
    #         await ctx.reply('HEH!! I JUST CRUSHED YOU!! I rock!!\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'paper':
    #         await ctx.reply('Bruh. >: |\nYour choice: ', user_choice, '\nMy choice: ', comp_choice)
    #     elif comp_choice == 'scissors':
    #         await ctx.reply("Oh well, we tied.\nYour choice: ", user_choice, '\nMy choice: ', comp_choice)




bot.run("OTA0Mjk0MzA0Nzk1NzQyMjQ5.YX5bsw.4OUYIiZSWh-DyOgax4yp7kXeUTI")
#132 10
#449 449

   
















