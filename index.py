#!/usr/bin/python
# -*- coding: utf-8 -*-
import discord
import datetime
import os
import sys
import Password.make_password as make_password
import Password.deconvert_password as deconvert_password
import Dict.findwords as findwords
import function.weather as weather
import function.get_tkb as get_tkb
import function.getnews as getnews


def get_token():
    with open('filetxt/token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()


clinet = discord.Client()


@clinet.event
async def on_ready():
    print('The bot is ready !!')
    activiti = discord.Game(name="I'm Bot")
    await clinet.change_presence(status=discord.Status.online, activity=activiti)


@clinet.event
async def on_message(message):
    id = clinet.get_guild(688410531417161793)
    channels = ['cmd_channels', 'bot']
    valid_users = ['Huyền Chi#0157', 'bql0711#8318']
    sms = message.content.lower()
    commands_key = ['help', '!command', 'key']
    # url = message.attachments[0].url
    if str(message.channel) in channels and str(message.author) in valid_users:
        if sms in findwords.hello_words:
            await message.channel.send('Hello there!!')
        if sms.find('your name') != -1:
            await  message.channel.send("I'm Bot, my name is Huyền Chi")
        if sms in commands_key:
            embed = discord.Embed(title="Help on BOT", description="Some useful commands")
            embed.add_field(name="!make_password", value="!make_password:<your string>")
            embed.add_field(name="!deconvert_password", value="!deconvert_password:<your password + key>")
            embed.add_field(name="!weather", value="!weather:<location>")
            embed.add_field(name="!time", value="!time:<location>")
            embed.add_field(name="!say_my_love", value="!say_my_love:<name>")
            embed.add_field(name="!infor", value="BOT information")
            embed.add_field(name="!tkb", value="!tkb:<day of week>")
            embed.add_field(name="!news", value="Báo Zing.vn")
            embed.add_field(name="!tech", value="Báo Genk.vn")
            embed.add_field(name="!covid19", value="!covid19:<country>")
            await message.channel.send(content=None, embed=embed)
        if sms.find('!make_password') != -1:
            str_in = message.content.split(':')
            check_password = str_in[1].split(' ')
            if len(check_password) != 3:
                if len(check_password) > 3:
                    await message.channel.send('Your Passsword is to long, intype another string vs 3 words')
                else:
                    await  message.channel.send('Your Password is to short, intype another string vs 3 words')
            else:
                passwords = make_password.converter(str_in[1])
                await message.channel.send('Your full encode: ' + passwords[0])
                await message.channel.send('Your key: ' + passwords[1])
                await message.channel.send('Your password: ' + passwords[2])
        if sms.find('!deconvert_password') != -1:
            str_in = message.content.split(':')
            # print(str_in)
            str_out = deconvert_password.make_string(str_in[1])
            await message.channel.send('Your string after decode: ' + str_out)
        if sms.find('!info') != -1:
            await message.channel.send("My name is Huyền Chi. \n"
                                       "I'm the bot and my Boss has name Nguyễn Viết Cường. \n"
                                       "My Boss is a development, he is Male and 23 years old. \n"
                                       "He create me at 03/14/2020 22:00:00 GMT+7. \n"
                                       "I'm trying to better and alway learning from you. \n"
                                       "I'm use DNN and CNN to define and learning. \n"
                                       "Thank you to asking my info. Have a good day!!")
        if sms.find('!mylove') != -1:
            await message.channel.send("Đây là một tính năng ẩn (hide function): \n"
                                       "Chúc mừng bạn vì đã tìm thấy tên của người yêu tôi \n"
                                       "Cô ấy tên My. \n"
                                       "Cậu có thể ghép chữ â trong từ 'Anh đây' vào giữa tên cô ấy. \n"
                                       "Lúc đó tên cô ấy sẽ đại diện cho những đám mây trên bầu trời. \n"
                                       "Bởi vì cô ấy dịu nhẹ, ấm áp và trong sáng như đám mây mùa thu. \n"
                                       "Cậu cũng có thể nhận ra, 'My' là một từ trong 'My love <3' \n"
                                       "Cô ấy là người mà boss của tôi rất yêu!! \n"
                                       "Tên cô ấy cũng luôn xuất hiện trên từ ngữ mà bạn hay dùng. \n"
                                       "Hãy hỏi giúp boss của tôi cô ấy có thật không, một ánh nắng cũng là cô ấy,"
                                       " vì cả bầu trời này luôn có tình yêu của ông chủ tôi. ")
        if sms.find('!weather') != -1:
            str_in = message.content.split(':')
            str_weather = weather.weather(str_in[1])
            await message.channel.send(str_weather)
        if sms.find('!time') != -1:
            str_a = str(datetime.datetime.now())
            await message.channel.send(str_a)
        if sms.find('!tkb') != -1:
            str_in = sms.split(':')
            str_out = get_tkb.tkb_today(str_in[1])
            await message.channel.send(str_out)
        if sms.find('fuck') != -1:
            await message.delete()
        if sms.find('!news') != -1:
            for str_out in getnews.get_news():
                await message.channel.send(str_out)
        if sms.find('!tech') != -1:
            str_out = getnews.get_tech()
            str_out = str_out[1:]
            for str_out in str_out:
                await message.channel.send(str_out)
        # if sms.find('!covid19') != -1:
        #     country = message.content.split(':')
        #     str_out = getnews.covid19(country[1])
        #     for key, value in str_out.items():
        #         await message.channel.send(key+': '+value)
        # if sms.find('!License_plates') != -1:
        #     if url.find('/attachments/') != -1:
        #
                
# @clinet.event
# async def on_message(message):
#     print(message.attachments[0].url)

clinet.run(get_token())
