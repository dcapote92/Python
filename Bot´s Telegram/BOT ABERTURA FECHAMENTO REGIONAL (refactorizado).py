############################################################################################
# @SystemAberturaCE_bot by: Emanuel Douglas                                                #
# refactorized by: dcapote92                                                               #
############################################################################################
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import telebot, os


botTOKEN = ''
bot = Bot(botTOKEN)
dp = Dispatcher(bot)
bott = telebot.TeleBot(botTOKEN,parse_mode='html')
sistema = os.name
usuario = os.path.expanduser('~')

lojas = {'32':'MIX TIMON','41':'MIX CAXIAS','97':'MIX CEASA','211':'SUPER PIRIPIRI','251':'MIX PARNAIBA','252':'MIX NOVAFAPI','264':'MIX TIANGUÁ',
         '266':'MIX SOBRAL','271':'MIX FLORIANO','275':'MIX ALBORADA','280':'MIX ITAPIPOCA','285':'SUPER CRATEÚS','290':'SUPER QUIXERAMOBIN',
         '503':'MIX MARACANAÚ','506':'MIX HENRIQUE JORGE','507':'MIX JUAZEIRO DO NORTE','514':'MIX MARANGUAPE','516':'MIX CANINDÉ','520':'MIX ARACATI'}



button1 = KeyboardButton('☀️Abertura')
button2 = KeyboardButton('🌚Fechamento')
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button1, button2)

#BOTÕES LOJAS ABERTURA
buttons_abertura =[]
for l in lojas:
    locals()['button'+l] = KeyboardButton('SM'+l)
    buttons_abertura.append(locals()['button'+l])
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons_abertura) 

#BOTÕES LOJAS FECHAMENTO
buttons_fechamento =[]
for l in lojas:
    locals()['button'+l] = KeyboardButton('SM-'+l)
    buttons_fechamento.append(locals()['button'+l])
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*buttons_fechamento)

photo_ids = []

@bott.message_handler(content_types=['photo'])
def handle_photo(message):
    # Obtém o ID da foto
    photo_id = message.photo[-1].file_id
    if photo_id not in photo_ids:
        photo_ids.append(photo_id)
    bot.send_photo(message.chat.id, photo_id)  # Envia a foto de volta para o usuário
    bot.delete_message(message.chat.id, message.message_id) # Deleta a foto original do usuário


#BOTÕES CONCLUIR DA ABERTURA
for l in lojas:
    locals()['buttonconcluir'+l] = KeyboardButton('Concluir Abertura SM'+l+' ✅')
    globals()['keyboard'+l] = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(locals()['buttonconcluir'+l])

#BOTÕES CONSISTENCIA OK E FALHA CONSISTENCIA
for l in lojas:
    locals()['buttonconsisok'+l] = KeyboardButton('Consistencia SM'+l+' OK ✅')
    locals()['buttonconsisf'+l] = KeyboardButton('Falha Consistencia SM'+l+' ❌')
    globals()['keyboardFX'+l] = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(locals()['buttonconsisok'+l],locals()['buttonconsisf'+l])

#COMANDOS INICIAIS
@dp.message_handler(commands=['start', 'iniciar'])
async def welcome(message: types.Message):
    user_name = message.from_user.first_name
    resposta = f"Ola, {user_name}! Bem-vindo ao assistente de Abertura e Fechamento da Regional Piauí e Ceará!"
    await message.answer(resposta, reply_markup=keyboard1)

#AQUI COMEÇAM AS INFO DE LOJA DOS PROCESSOS ABERTURA  E FECHAMENTO 
@dp.message_handler()
async def kb_answer(message: types.Message):
    user_name = message.from_user.first_name
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
    

    pos = 0
    for l in lojas:  
        if message.text == 'SM'+l:
            resposta = '⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n' + 'SM'+l + ' - ' + lojas[l] + '\n' + 'POR FAVOR ANEXAR TODOS OS PRINTS\n' + '⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️'
            await message.answer(resposta,reply_markup=globals()['keyboard'+l])
            
        
        elif message.text == 'Concluir Abertura SM'+l + ' ✅':
            photo = open(r''+usuario+'/01.png','rb')
            # send = bot.send_message(message.from_user.id, 'Send your pics...')
            # bott.register_next_step_handler(send, get_user_pics)
            resposta ='\nPROCESSO DE ABERTURA FINALIZADO COM SUCESSO.\n' + '◾ABERTURA ✅\n' + '◾LOJA '+l+'.' + lojas[l]+'\n' + f'◾👨‍💻T.I: {user_name}!\n' + 'ÓTIMO DIA, E BOM TRABALHO!\n'
            await message.reply_photo(photo,caption = resposta, reply_markup=keyboard1, reply=False)

        elif message.text == 'SM-'+l:
            resposta = 'Loja SM'+l + ' - ' + lojas[l] + 'SELECIONADA ✅\n' + '⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n' + 'FAÇA O ANEXO DOS SEGUINTES PRINTS: PAINEL TERMINAL, ALTERAÇÃO GMCORE, CARGA DAS BALANÇAS E CONSISTÊNCIA.'
            resposta += ' EM CASOS DE HAVER ALGUM PDV COM ERRO NA CONSISTÊNCIA CLIQUE EM\n' + 'ERRO CONSISTÊNCIA  ❌\n' + 'OU SE TODOS OBTERAM SUCESSO CLIQUE EM CONSISTÊNCIA OK ✅ \n' +'⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️\n'
            await message.answer(resposta, reply_markup=globals()['keyboardFX'+l])

        elif message.text == 'Consistencia SM'+l +' OK ✅':
            resposta = '️️️️️️️️️️PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n' + '️️️️️️️️️️◾ CONSISTÊNCIA ✅\n' + '️️️️️️️️️️◾ ALTERAÇÃO ✅\n' + '️️️️️️️️️◾ PAINEL TERMINAL ✅\n' + '◾ LOJA '+l+'. ' + lojas[l]+'\n' 
            resposta += f'◾👨‍💻T.I: {user_name} !\n' + 'BOM DESCANSO\n'
            await message.answer(resposta, reply_markup=keyboard1)

        elif message.text == 'Falha Consistencia SM'+l + ' ❌':
            resposta = 'PROCESSO DE FECHAMENTO FINALIZADO COM SUCESSO.\n' + '◾CONSISTÊNCIA ❌\n' + '◾ ALTERAÇÃO ✅\n' + '◾ PAINEL TERMINAL ✅\n' + '◾LOJA '+l+'. ' + lojas[l]+'\n' 
            resposta += f'‍◾👨‍💻T.I:{user_name} !\n' + 'BOM DESCANSO!\n'
            await message.answer(resposta, reply_markup=keyboard1)        

        pos+=1
print(photo_ids)        
# bott.polling()
executor.start_polling(dp)

