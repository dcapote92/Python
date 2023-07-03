

############################################################################################
# @SystemAberturaCE_bot by: Emanuel Douglas                                                    #
############################################################################################


from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
import telebot
from telebot import types


bot = Bot(token='5962658535:AAFF6qckVwYP-5OmTXlaKZK7wL5HDJLMXmE')
dp = Dispatcher(bot)
bot = telebot.TeleBot

button1 = KeyboardButton('☀️Abertura')
button2 = KeyboardButton('🌚Fechamento')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2)

#BOTÕES LOJAS ABERTURA

button32 = KeyboardButton('SM32')
button41 = KeyboardButton('SM41')
button97 = KeyboardButton('SM97')
button211 = KeyboardButton('SM211')
button251 = KeyboardButton('SM251')
button252 = KeyboardButton('SM252')
button264 = KeyboardButton('SM264')
button266 = KeyboardButton('SM266')
button271 = KeyboardButton('SM271')
button275 = KeyboardButton('SM275')
button280 = KeyboardButton('SM280')
button285 = KeyboardButton('SM285')
button290 = KeyboardButton('SM290')
button503 = KeyboardButton('SM503')
button506 = KeyboardButton('SM506')
button507 = KeyboardButton('SM507')
button514 = KeyboardButton('SM514')
button516 = KeyboardButton('SM516')
button520 = KeyboardButton('SM520')

keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button32, button41, button97, button211, button251, button252, button264, button266, button271, button275, button280, button285, button290, button503, button506, button507, button514, button516, button520)

#BOTÕES LOJAS FECHAMENTO

button32 = KeyboardButton('SM-32')
button41 = KeyboardButton('SM-41')
button97 = KeyboardButton('SM-97')
button211 = KeyboardButton('SM-211')
button251 = KeyboardButton('SM-251')
button252 = KeyboardButton('SM-252')
button264 = KeyboardButton('SM-264')
button266 = KeyboardButton('SM-266')
button271 = KeyboardButton('SM-271')
button275 = KeyboardButton('SM-275')
button280 = KeyboardButton('SM-280')
button285 = KeyboardButton('SM-285')
button290 = KeyboardButton('SM-290')
button503 = KeyboardButton('SM-503')
button506 = KeyboardButton('SM-506')
button507 = KeyboardButton('SM-507')
button514 = KeyboardButton('SM-514')
button516 = KeyboardButton('SM-516')
button520 = KeyboardButton('SM-520')
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button32, button41, button97, button211, button251, button252, button264, button266, button271, button275, button280, button285, button290, button503, button506, button507, button514, button516, button520)

#BOTÕES CONCLUIR DA ABERTURA

buttonconcluir32 = KeyboardButton('Concluir Abertura SM32 ✅')
keyboard32 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir32)

buttonconcluir41 = KeyboardButton('Concluir Abertura SM41 ✅')
keyboard41 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir41)

buttonconcluir97 = KeyboardButton('Concluir Abertura SM97 ✅')
keyboard97 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir97)

buttonconcluir211 = KeyboardButton('Concluir Abertura SM211 ✅')
keyboard211 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir211)

buttonconcluir251 = KeyboardButton('Concluir Abertura SM251 ✅')
keyboard251 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir251)

buttonconcluir252 = KeyboardButton('Concluir Abertura SM252 ✅')
keyboard252 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir252)

buttonconcluir264 = KeyboardButton('Concluir Abertura SM264 ✅')
keyboard264 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir264)

buttonconcluir266 = KeyboardButton('Concluir Abertura SM266 ✅')
keyboard266 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir266)

buttonconcluir271 = KeyboardButton('Concluir Abertura SM271 ✅')
keyboard271 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir271)

buttonconcluir275 = KeyboardButton('Concluir Abertura SM275 ✅')
keyboard275 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir275)

buttonconcluir280 = KeyboardButton('Concluir Abertura SM280 ✅')
keyboard280 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir280)

buttonconcluir285 = KeyboardButton('Concluir Abertura SM285 ✅')
keyboard285 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir285)

buttonconcluir290 = KeyboardButton('Concluir Abertura SM290 ✅')
keyboard290 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir290)

buttonconcluir503 = KeyboardButton('Concluir Abertura SM503 ✅')
keyboard503 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir503)

buttonconcluir506 = KeyboardButton('Concluir Abertura SM506 ✅')
keyboard506 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir506)

buttonconcluir507 = KeyboardButton('Concluir Abertura SM507 ✅')
keyboard507 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir507)

buttonconcluir514 = KeyboardButton('Concluir Abertura SM514 ✅')
keyboard514 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir514)

buttonconcluir516 = KeyboardButton('Concluir Abertura SM516 ✅')
keyboard516 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir516)

buttonconcluir520 = KeyboardButton('Concluir Abertura SM520 ✅')
keyboard520 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconcluir520)




#BOTÕES CONSISTENCIA OK E FALHA CONSISTENCIA

#SM32
buttonconsisok32 = KeyboardButton('Consistencia SM32 OK ✅')
buttonconsisf32 = KeyboardButton('Falha Consistencia SM32 ❌')
keyboardFX32 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok32, buttonconsisf32)

#SM41
buttonconsisok41 = KeyboardButton('Consistencia SM41 OK ✅')
buttonconsisf41 = KeyboardButton('Falha Consistencia SM41 ❌')
keyboardFX41 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok41, buttonconsisf41)

#SM97
buttonconsisok97 = KeyboardButton('Consistencia SM97 OK ✅')
buttonconsisf97 = KeyboardButton('Falha Consistencia SM97 ❌')
keyboardFX97 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok97, buttonconsisf97)

#SM211
buttonconsisok211 = KeyboardButton('Consistencia SM211 OK ✅')
buttonconsisf211 = KeyboardButton('Falha Consistencia SM211 ❌')
keyboardFX211 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok211, buttonconsisf211)

#SM251
buttonconsisok251 = KeyboardButton('Consistencia SM251 OK ✅')
buttonconsisf251 = KeyboardButton('Falha Consistencia SM251 ❌')
keyboardFX251 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok251, buttonconsisf251)

#SM252
buttonconsisok252 = KeyboardButton('Consistencia SM252 OK ✅')
buttonconsisf252 = KeyboardButton('Falha Consistencia SM252 ❌')
keyboardFX252 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok252, buttonconsisf252)

#SM264
buttonconsisok264 = KeyboardButton('Consistencia SM264 OK ✅')
buttonconsisf264 = KeyboardButton('Falha Consistencia SM264 ❌')
keyboardFX264 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok252, buttonconsisf264)

#SM266
buttonconsisok266 = KeyboardButton('Consistencia SM266 OK ✅')
buttonconsisf266 = KeyboardButton('Falha Consistencia SM266 ❌')
keyboardFX266 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok266, buttonconsisf266)

#SM271
buttonconsisok271 = KeyboardButton('Consistencia SM271 OK ✅')
buttonconsisf271 = KeyboardButton('Falha Consistencia SM271 ❌')
keyboardFX271 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok271, buttonconsisf271)

#SM275
buttonconsisok275 = KeyboardButton('Consistencia SM275 OK ✅')
buttonconsisf275 = KeyboardButton('Falha Consistencia SM275 ❌')
keyboardFX275 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok275, buttonconsisf275)

#SM280
buttonconsisok280 = KeyboardButton('Consistencia SM280 OK ✅')
buttonconsisf280 = KeyboardButton('Falha Consistencia SM280 ❌')
keyboardFX280 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok280, buttonconsisf280)

#SM285
buttonconsisok285 = KeyboardButton('Consistencia SM285 OK ✅')
buttonconsisf285 = KeyboardButton('Falha Consistencia SM285 ❌')
keyboardFX285 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok285, buttonconsisf285)

#SM290
buttonconsisok290 = KeyboardButton('Consistencia SM290 OK ✅')
buttonconsisf290 = KeyboardButton('Falha Consistencia SM290 ❌')
keyboardFX290 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok290, buttonconsisf290)

#SM503
buttonconsisok503 = KeyboardButton('Consistencia SM503 OK ✅')
buttonconsisf503 = KeyboardButton('Falha Consistencia SM503 ❌')
keyboardFX503 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok503, buttonconsisf503)

#SM506
buttonconsisok506 = KeyboardButton('Consistencia SM506 OK ✅')
buttonconsisf506 = KeyboardButton('Falha Consistencia SM506 ❌')
keyboardFX506 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok506, buttonconsisf506)

#SM507
buttonconsisok507 = KeyboardButton('Consistencia SM507 OK ✅')
buttonconsisf507 = KeyboardButton('Falha Consistencia SM507 ❌')
keyboardFX507 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok507, buttonconsisf507)

#SM514
buttonconsisok514 = KeyboardButton('Consistencia SM514 OK ✅')
buttonconsisf514 = KeyboardButton('Falha Consistencia SM514 ❌')
keyboardFX514 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok514, buttonconsisf514)

#SM516
buttonconsisok516 = KeyboardButton('Consistencia SM516 OK ✅')
buttonconsisf516 = KeyboardButton('Falha Consistencia SM516 ❌')
keyboardFX516 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok516, buttonconsisf516)

#SM520
buttonconsisok520 = KeyboardButton('Consistencia SM520 OK ✅')
buttonconsisf520 = KeyboardButton('Falha Consistencia SM520 ❌')
keyboardFX520 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(buttonconsisok520, buttonconsisf520)



@dp.message_handler(commands=['start', 'help', 'iniciar'])
async def welcome(message: types.Message):
    user_name = message.from_user.first_name
    resposta = f"Ola, {user_name}! Bem-vindo ao assistente de Abertura e Fechamento da Regional Piauí e Ceará!"
    await message.answer(resposta, reply_markup=keyboard1)

@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '☀️Abertura':
        resposta = "OK, BOM DIA!\n"
        resposta += "VOCÊ SELECIONOU ABERTURA\n"
        resposta += "VAMOS COMECAR PROCEDIMENTO DE ABERTURA.\n"
        resposta += "SELECIONE SUA FILIAL PARA INICIAR O PROCESSO ABERTURA DE LOJA.\n"
        await message.answer(resposta, reply_markup=keyboard2)
    elif message.text == '🌚Fechamento':
        resposta = "OK, ÓTIMA NOITE!\n"
        resposta += "VOCÊ SELECIONOU FECHAMENTO\n"
        resposta += "VAMOS COMECAR PROCEDIMENTO DE FECHAMENTO DA LOJA.\n"
        resposta += "SELECIONE SUA FILIAL PARA INICIAR O PROCESSO DE FECHAMENTO DA LOJA.\n"
        await message.answer(resposta, reply_markup=keyboard3)

#AQUI COMEÇA AS INFO DE LOJA DO PORCESSO ABERTURA
#SM32

    elif message.text == 'SM32':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM32 - MIX TIMON\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard32)
    elif message.text == 'Concluir Abertura SM32 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 32. MIX TIMON\n"
        resposta += "◾Timon - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)
        

#SM41

    elif message.text == 'SM41':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM41 - MIX CAXIAS\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard41)
    elif message.text == 'Concluir Abertura SM41 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 41 - MIX CAXIAS\n"
        resposta += "◾CAXIAS - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM97

    elif message.text == 'SM97':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM97 - MIX CEASA\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard97)
    elif message.text == 'Concluir Abertura SM97 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 97 - MIX CEASA\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM211

    elif message.text == 'SM211':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM211 - SUPER PIRIPIRI\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard211)
    elif message.text == 'Concluir Abertura SM211 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 211 - SUPER PIRIPIRI\n"
        resposta += "◾PIRIPIRI - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM251

    elif message.text == 'SM251':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM251 - MIX PARNAIBA\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard251)
    elif message.text == 'Concluir Abertura SM251 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 251 - MIX PARNAIBA\n"
        resposta += "◾PARNAIBA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM252

    elif message.text == 'SM252':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM252 - MIX PARNAIBA\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard252)
    elif message.text == 'Concluir Abertura SM252 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 252 - MIX NOVAFAPI\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM264

    elif message.text == 'SM264':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM264 - MIX TIANGUÁ\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard264)
    elif message.text == 'Concluir Abertura SM264 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 264 - MIX TIANGUÁ\n"
        resposta += "◾TIANGUÁ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM266

    elif message.text == 'SM266':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM266 - MIX SOBRAL\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard266)
    elif message.text == 'Concluir Abertura SM266 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 266 - MIX SOBRAL\n"
        resposta += "◾SOBRAL - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM271

    elif message.text == 'SM271':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM271 - MIX FLORIANO\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard271)
    elif message.text == 'Concluir Abertura SM271 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 271 - MIX FLORIANO\n"
        resposta += "◾FLORIANO - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM275

    elif message.text == 'SM275':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM275 - MIX ALVORADA\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard275)
    elif message.text == 'Concluir Abertura SM275 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 275 - MIX ALVORADA\n"
        resposta += "◾TIMON - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM280

    elif message.text == 'SM280':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM280 - MIX ITAPIPOCA\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard280)
    elif message.text == 'Concluir Abertura SM280 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 280 - MIX ITAPIPOCA\n"
        resposta += "◾ITAPIPOCA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM285

    elif message.text == 'SM285':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM285 - SUPER CRATEÚS\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard285)
    elif message.text == 'Concluir Abertura SM285 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 285 - MIX CRATEÚS\n"
        resposta += "◾CRATEÚS - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM290

    elif message.text == 'SM290':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM290 - SUPER QUIXERAMOBIM\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard290)
    elif message.text == 'Concluir Abertura SM290 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 290 - SUPER QUIXERAMOBIM\n"
        resposta += "◾QUIXERAMOBIM - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM503

    elif message.text == 'SM503':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM503 - MIX MARACANAÚ\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard503)
    elif message.text == 'Concluir Abertura SM503 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 503 - MIX MARACANAÚ\n"
        resposta += "◾MARACANAÚ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM506

    elif message.text == 'SM506':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM506 - MIX HENRIQUE JORGE\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard506)
    elif message.text == 'Concluir Abertura SM506 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 506 - MIX HENRIQUE JORGE\n"
        resposta += "◾FOTALEZA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM507
 
    elif message.text == 'SM507':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM507 - MIX JUAZEIRO DO NORTE\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard507)
    elif message.text == 'Concluir Abertura SM507 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 507 - MIX JUAZEIRO DO NORTE\n"
        resposta += "◾JUAZEIRO DO NORTE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM514

    elif message.text == 'SM514':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM514 - MIX MARANGUAPE\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard514)
    elif message.text == 'Concluir Abertura SM514 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 514 - MIX MARANGUAPE\n"
        resposta += "◾MARANGUAPE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM516

    elif message.text == 'SM516':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM516 - MIX CANINDÉ\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard516)
    elif message.text == 'Concluir Abertura SM516 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 516 - MIX CANINDÉ\n"
        resposta += "◾CANINDÉ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM520

    elif message.text == 'SM520':
        resposta = "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "SM520 - MIX ARACATI\n"
        resposta += "POR FAVOR ANEXAR TODOS OS PRINTS\n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️"
        await message.answer(resposta, reply_markup=keyboard520)
    elif message.text == 'Concluir Abertura SM520 ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n"
        resposta +=  "◾ABERTURA ✅\n" 
        resposta += "◾LOJA 520 - MIX ARACATI\n"
        resposta += "◾ARACATI - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "ÓTIMO DIA, E BOM TRABALHO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#AQUI COMEÇA AS INFO DE LOJA PROCESSO DE FECHAMENTO
#SM32

    elif message.text == 'SM-32':
        resposta = ".LOJA SM32 - MIX TIMON SELECIONADA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX32)


        

    elif message.text == 'Consistencia SM32 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA 32. MIX TIMON\n"
        resposta += "◾Timon - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM32 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA 32. MIX TIMON\n"
        resposta += "◾Timon - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM41


    elif message.text == 'SM-41':
        resposta = ".LOJA SM41 - MIX CAXIAS SELECIONADA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX41)
        

    elif message.text == 'Consistencia SM41 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA 41. MIX CAXIAS\n"
        resposta += "◾CAXIAS - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM41 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA 41. MIX CAXIAS\n"
        resposta += "◾CAXIAS - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM97


    elif message.text == 'SM-97':
        resposta = ".LOJA SM97 - MIX CEASA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX97)
        

    elif message.text == 'Consistencia SM97 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM97 - MIX CEASA\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM97 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM97 - MIX CEASA\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM211


    elif message.text == 'SM-211':
        resposta = ".LOJA SM211 - SUPER PIRIPIRI ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX211)
        

    elif message.text == 'Consistencia SM211 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM211 - SUPER PIRIPIRI\n"
        resposta += "◾PIRIPIRI - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM211 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM211 - SUPER PIRIPIRI\n"
        resposta += "◾PIRIPIRI - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM251


    elif message.text == 'SM-251':
        resposta = ".LOJA SM251 - MIX PARNAIBA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX251)
        

    elif message.text == 'Consistencia SM251 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM251 - MIX PARNAIBA\n"
        resposta += "◾PPARNAIBA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM251 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM251 - MIX PARNAIBA\n"
        resposta += "◾PARNAIBA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM252


    elif message.text == 'SM-252':
        resposta = ".LOJA SM252 - MIX NOVAFAPI ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX252)
        

    elif message.text == 'Consistencia SM252 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM252 - MIX NOVAFAPI\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM252 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM252 - MIX NOVAFAPI\n"
        resposta += "◾TERESINA - PI\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM264

    elif message.text == 'SM-264':
        resposta = ".LOJA SM264 - MIX TIANGUÁ ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX264)
        

    elif message.text == 'Consistencia SM264 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM264 - MIX TIANGUÁ\n"
        resposta += "◾TIANGUÁ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM264 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM264 - MIX TIANGUÁ\n"
        resposta += "◾TIANGUÁ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM266

    elif message.text == 'SM-266':
        resposta = ".LOJA SM266 - MIX SOBRAL ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX266)
        

    elif message.text == 'Consistencia SM266 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM266 - MIX SOBAL\n"
        resposta += "◾SOBRAL - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM266 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM266 - MIX SOBAL\n"
        resposta += "◾SOBRAL - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM271

    elif message.text == 'SM-271':
        resposta = ".LOJA SM271 - MIX FLORIANO ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX271)
        

    elif message.text == 'Consistencia SM271 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM271 - MIX FLORIANO\n"
        resposta += "◾FLORIANO - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM271 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM271 - MIX FLORIANO\n"
        resposta += "◾FLORIANO - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM275

    elif message.text == 'SM-275':
        resposta = ".LOJA SM275 - MIX ALVORADA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX275)
        

    elif message.text == 'Consistencia SM275 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM275 - MIX ALVORADA \n"
        resposta += "◾TIMON - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM275 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM275 - MIX ALVORADA \n"
        resposta += "◾TIMON - MA\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM280

    elif message.text == 'SM-280':
        resposta = ".LOJA SM280 - MIX ITAPIPOCA ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX280)
        

    elif message.text == 'Consistencia SM280 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM280 - MIX ITAPIPOCA \n"
        resposta += "◾ITAPIPOCA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM280 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM280 - MIX ITAPIPOCA \n"
        resposta += "◾ITAPIPOCA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM285

    elif message.text == 'SM-285':
        resposta = ".LOJA SM285 - SUPER CRATEÚS ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX285)
        

    elif message.text == 'Consistencia SM285 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM285 - SUPER CRATEÚS \n"
        resposta += "◾CRATEÚS - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM285 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM285 - SUPER CRATEÚS \n"
        resposta += "◾CRATEÚS - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM290

    elif message.text == 'SM-290':
        resposta = ".LOJA SM290 - SUPER QUIXERAMOBIM ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX290)
        

    elif message.text == 'Consistencia SM290 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM290 - SUPER QUIXERAMOBIM \n"
        resposta += "◾QUIXERAMOBIM - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM290 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM290 - SUPER QUIXERAMOBIM \n"
        resposta += "◾QUIXERAMOBIM - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM503

    elif message.text == 'SM-503':
        resposta = ".LOJA SM503 - MIX MARACANAU ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX503)
        

    elif message.text == 'Consistencia SM503 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM503 - MIX MARACANAU \n"
        resposta += "◾MARACANAU - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM503 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM503 - MIX MARACANAU \n"
        resposta += "◾MARACANAU - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM506

    elif message.text == 'SM-506':
        resposta = ".LOJA SM506 - MIX HENRIQUE JORGE ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX506)
        

    elif message.text == 'Consistencia SM506 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM506 - MIX HENRIQUE JORGE\n"
        resposta += "◾FORTALEZA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM506 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM506 - MIX HENRIQUE JORGE\n"
        resposta += "◾FORTALEZA - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM507

    elif message.text == 'SM-507':
        resposta = ".LOJA SM507 - MIX JUAZEIRO DO NORTE ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX507)
        

    elif message.text == 'Consistencia SM507 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM507 - MIX JUAZEIRO DO NORTE\n"
        resposta += "◾JUAZEIRO DO NORTE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM507 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM507 - MIX JUAZEIRO DO NORTE\n"
        resposta += "◾JUAZEIRO DO NORTE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM514

    elif message.text == 'SM-514':
        resposta = ".LOJA SM514 - MIX MARANGUAPE ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX514)
        

    elif message.text == 'Consistencia SM514 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM514 - MIX MARANGUAPE\n"
        resposta += "◾MARANGUAPE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM514 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM514 - MIX MARANGUAPE\n"
        resposta += "◾MARANGUAPE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM514

    elif message.text == 'SM-514':
        resposta = ".LOJA SM514 - MIX MARANGUAPE ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX514)
        

    elif message.text == 'Consistencia SM514 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM514 - MIX MARANGUAPE\n"
        resposta += "◾MARANGUAPE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM514 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM514 - MIX MARANGUAPE\n"
        resposta += "◾MARANGUAPE - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)


#SM516

    elif message.text == 'SM-516':
        resposta = ".LOJA SM516 - MIX CANINDÉ ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX516)
        

    elif message.text == 'Consistencia SM516 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM516 - MIX CANINDÉ\n"
        resposta += "◾CANINDÉ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM516 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM516 - MIX CANINDÉ\n"
        resposta += "◾CANINDÉ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)

#SM520

    elif message.text == 'SM-520':
        resposta = ".LOJA SM520 - MIX ARACATI ✅\n" 
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        resposta += "FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA. EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n"
        resposta += "ERRO CONSISTÊNCIA  ❌\n"
        resposta += "OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n"
        resposta += "⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n"
        await message.answer(resposta, reply_markup=keyboardFX520)
        

    elif message.text == 'Consistencia SM520 OK ✅':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ✅\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM520 - MIX CANINDÉ\n"
        resposta += "◾CANINDÉ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO"
        await message.answer(resposta, reply_markup=keyboard1)

    
    elif message.text == 'Falha Consistencia SM520 ❌':
        user_name = message.from_user.first_name
        resposta = "PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n"
        resposta += "◾CONSISTÊNCIA ❌\n"
        resposta += "◾ ALTERAÇÃO ✅\n"
        resposta += "◾ PAINEL TERMINAL ✅\n"
        resposta += "◾LOJA SM520 - MIX CANINDÉ\n"
        resposta += "◾CANINDÉ - CE\n"
        resposta += f"◾👨‍💻T.I: {user_name}!\n"
        resposta += "BOM DESCANSO!\n"
        await message.answer(resposta, reply_markup=keyboard1)




    else:
        await message.reply(f"Your message is: {message.text}")

executor.start_polling(dp)

