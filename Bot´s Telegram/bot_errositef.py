'''
Maio, 2023
Daniel V. Capote
TI
Mix Henrique Jorge
Grupo Mateus
'''
import telebot
BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN)

erro = 'Código: '
descricao = '\nDescrição ⚠️🖥️:  '
acao = '\nAção:\n'
retentativa_ok = '\nPermite Retentativa: 👍'
retentativa_nao = '\nPermite Retentativa: 👎'


#Baseado na documentação oferecida pelo Gerente de Telecomunicações do Grupo Mateus, Arthur Turrini
erros = {'00':descricao+'Transação Nacional Autorizada com Sucesso '+acao+'N/A',
         '01':descricao+'01 Transção referida pelo emissor.'+acao+'Oriente o portador a contatar o emissor do cartão.'+retentativa_nao,
         '02':descricao+'02 Transção referida pelo emissor.'+acao+'Oriente o portador a contatar o emissor do cartão.'+retentativa_nao,
         '03':descricao+'03 Não foi encontrada a transação.'+acao+'Este erro pode ser:\n-número de parcelas ultrapassa o permitido.\n-código de segurança inválido.\n-número de cartão inválido.\n-inestabilidade no sistema da adquirente.'+retentativa_ok,
         '04':descricao+'04 Cartão com restrição.'+acao+'Oriente o portador a contatar o emissor do cartão (Problemas como cartão).'+retentativa_nao,
         '05':descricao+'05 Transação não autorizada.'+acao+'Oriente o portador a contatar o emissor do cartão (Não autorizada pelo emissor).'+retentativa_nao,
         '06':descricao+'06 Tente novamente.'+acao+'Problemas ocorridos na transação eletrônica, instabilidade da adquirente.'+retentativa_ok,
         '07':descricao+'07 Cartão com restrição.'+acao+'Oriente o portador a contatar o emissor do cartão (Problemas com o cartão).'+retentativa_nao,
         '08':descricao+'08 Código de segurança inválido.'+acao+'O código de segurança foi informado errado no momento da compra.'+retentativa_nao,
         '10':descricao+'10 Não é permitido o envio do cartão.'+acao+'Adquirente está com os serviços instáveis, caso o erro continue ocorrendo entre em contato com nosso suporte técnico.'+retentativa_nao,
         '11':descricao+'11 Transação Internacional Autorizada com sucesso.'+acao+'N/A.'+retentativa_nao,
         '12':descricao+'12 Transação inválida.'+acao+'Venda não autorizada pelo banco emissor do cartão. Cartão informado no momento da compra está incorreto.'+retentativa_nao,
         '13':descricao+'13 Valor inválido.'+acao+'Verifique valor mínimo de R$5,00 para parcelamento.'+retentativa_nao,
         '14':descricao+'14 Cartão inválido'+acao+'N/A.'+retentativa_nao,
         '15':descricao+'15 Emissor inválido'+acao+'Emissor sem comunicação.'+retentativa_ok,
         '19':descricao+'19 Refaça a transação ou tente novamente mais tarde.'+acao+'Não foi possível processar a transação. Refaça a transação ou tente novamente mais tarde.'+retentativa_ok,
         '21':descricao+'21 Cancelamento não efetuado'+acao+'Não foi possível processar o cancelamento.'+retentativa_nao,
         '22':descricao+'22 Parcelamento inválido. Número de parcelas inválidas'+acao+'Não foi possível processar a transação. Valor inválido. Refazer a transação confirmando os dados informados.'+retentativa_nao,
         '24':descricao+'24 Quantidade de parcelas inválido.'+acao+'Não foi possível processar a transação. Quantidade de parcelas inválido.'+retentativa_nao,
         '30':descricao+'30 Não foi possível processar a transação. Solicite ao portador que reveja os dados e tente novamente.'+acao+'Não foi possível processar a transação. Solicite ao portador que reveja os dados e tente novamente. Se o erro persistir, entre em contato com a loja virtual.'+retentativa_nao,
         '39':descricao+'39 Transação não autorizada. Erro nobanco emissor.'+acao+'Transação não autorizada. Entre em contato com seu banco emissor.'+retentativa_nao,
         '41':descricao+'41 Cartão com restrição.'+acao+'Oriente o portador a contatar o emissor do cartão (Problemas com o cartão).'+retentativa_nao,
         '43':descricao+'43 Cartão com restrição.'+acao+'Oriente o portador a contatar o emissor do cartão (Problemas com o cartão).'+retentativa_nao,
         '51':descricao+'51 Saldo insuficiente'+acao+'Cliente deve entrar em contato com o banco.'+retentativa_ok,
         '52':descricao+'52 Cartão com dígito de controle inválido'+acao+'Não foi possível processar a transação. Cartão com dígito de controle inválido.'+retentativa_nao,
         '54':descricao+'54 Cartão vencido'+acao+'Caso os dados informados estejam corretos, cliente deve entrar em contato com o banco para verificar se cartão ainda é válido.'+retentativa_nao,
         '55':descricao+'55 Senha inválida.'+acao+'Senha informada está errada.'+retentativa_nao,
         '57':descricao+'57 Transação não permitida ou não autorizada'+acao+'Venda não autorizada pelo emissor do cartão, pois o cartão utilizado não faz parte da rede Verified by Visa ou o sistema de prevenção do banco não autorizou a compra, neste caso o cliente deverá realizar contato com banco emissor do cartão e informar que está tentando realizar uma compra no valor R$XXX e não está sendo autorizada.'+retentativa_nao,
         '58':descricao+'58 Transaçãonão permitida'+acao+'N/A'+retentativa_nao,
         '60':descricao+'60 Transação não autorizada'+acao+'Oriente o portador a contatar o emissor do cartão.'+retentativa_nao,
         '61':descricao+'61 Banco emissor Visa indisponível'+acao+'Transação não autorizada. Tente novamente. Se o erro persistir, entre em contato com seu banco emissor.'+retentativa_ok,
         '62':descricao+'62 Cartão com restrição'+acao+'Oriente o portador a contatar o emissor do cartão. Cartão com algum bloqueio para transações online.'+retentativa_nao,
         '63':descricao+'63 Cartão com restrição'+acao+'Oriente o portador a contatar o emissor do cartão. Possível erro de segurança ao tentar processar.'+retentativa_nao,
         '65':descricao+'65 Cartão com restrição'+acao+'Transação negada. oriente o portador a contatar o emissor do cartão (Problemas como cartão).'+retentativa_nao,
         '67':descricao+'67 Transação não autorizada'+acao+'Transação não autorizada. Cartão bloqueado para compras hoje. Bloqueio pode ter ocorrido por excesso de tentativas inválidas.'+retentativa_ok,
         '70':descricao+'70 Transação não autorizada. Limite excedido / Sem saldo.'+acao+'Transação não autorizada. Entre em contato com seu banco emissor.'+retentativa_ok,
         '74':descricao+'74 Transação não autorizada.'+acao+'Transação não autorizada. A senha está vencida'+retentativa_nao,
         '75':descricao+'75 Cartão com restrição'+acao+'Motivo provável, bloqueio de senha. Oriente o portador a contatar o emissor do cartão.'+retentativa_nao,
         '76':descricao+'76 Tente novamente'+acao+'N/A'+retentativa_ok,
         '77':descricao+'77 Cancelamento não efetuado'+acao+'Cancelamento não efectuado. Não foi localizado a transação original.'+retentativa_nao,
         '78':descricao+'78 Cartão não foi desbloqueado pelo portador'+acao+'Cartão bloqueado. Oriente o portador a desbloqueá-lo junto ao emissor do cartão.'+retentativa_nao,
         '80':descricao+'80 Transação não autorizada'+acao+'Transação não autorizada. Data da transação ou data do primeiro pagamento inválida. Refazer confirmando dados.'+retentativa_nao,
         '81':descricao+'81 Transação negada'+acao+'N/A'+retentativa_nao,
         '82':descricao+'82 Transação inválida'+acao+'Provável código de segurança incorreto ou inválido.'+retentativa_nao,
         '85':descricao+'85 Transação não permitida. Falha da operação.'+acao+'Transação não permitida. Houve um erro no processamento. Solicite ao portador que digite novamente os dados do cartão.'+retentativa_nao,
         '88':descricao+'88 Erro na transação'+acao+'Transação não autorizada. Erro na transação. O portador deve tentar novamente e se o erro persistir, entrar em contato com o banco emissor.'+retentativa_ok,
         '90':descricao+'90 Transação não permitida. Falha da operação.'+acao+'Transação não permitida. Houve um erro no processamento. Solicite ao portador que digite novamente os dados do cartão.'+retentativa_nao,
         '91':descricao+'91 Banco indisponível.'+acao+'Emissor sem comunicação. Oriente cliente a aguardar alguns minutos e tente novamente.'+retentativa_ok,
         '92':descricao+'92 Transação não autorizada. Tempo de comunicação excedido.'+acao+'Transação não autorizada. Tempo de comunicação excedido.'+retentativa_nao,
         '94':descricao+'94 Transação não autorizada'+acao+'Transação desfeita pela bandeira.'+retentativa_nao,
         '96':descricao+'96 Tente novamente'+acao+'Provável venda abaixo de R$ 1,00. Falha no envio da autorização.'+retentativa_ok,
         '99':descricao+'99 Sistema do banco temporariamente fora de operação.'+acao+'Tente novamente mais tarde.'+retentativa_nao,
         'AA':descricao+'AA Tempo Excedido.'+acao+'Tempo excedido na comunicação com o banco emissor. Oriente oportador a tentar novamente,se o erro persistir será necessário que o portador contate seu banco emissor.'+retentativa_ok,
         'AC':descricao+'AC Cartão de débito sendo usado como crédito.'+acao+'Cartão de débito sendo usado como crédito. Portador deve usar um cartão de crédito.'+retentativa_nao,
         'AE':descricao+'AE Tente mais tarde.'+acao+'Tempo excedido na comunicação com o banco emissor. Oriente o portador a tentar novamente.'+retentativa_ok,
         'AF':descricao+'AF Transação não permitida. Falha da operação.'+acao+'Transação não permitida. Houve um erro no processamento. Solicite ao portador que digite novamente os dados do cartão.'+retentativa_nao,
         'AG':descricao+'AG Transação não permitida. Falha da operação.'+acao+'Transação não permitida. Houve um erro no processamento. Solicite ao portador que digite novamente os dados do cartão.'+retentativa_nao,
         'AI':descricao+'AI Transação não autorizada. Autenticação não foi realizada'+acao+'Transação não autorizada. autenticação não foi realizada. O portador não concluiu a autenticação.'+retentativa_nao,
         'AV':descricao+'AV Transação não autorizada. Dados inválidos.'+acao+'Falha na validação dos dados da transação. Oriente o portador a rever os dados e tentar novamente.'+retentativa_ok,
         'BD':descricao+'BD Transação não permitida. Falha da operação.'+acao+'Transação não permitida. Houveum erro noprocessamento. Solicite ao portador que digite novemante os dados do cartão.'+retentativa_nao,
         'BL':descricao+'BL Transação não autorizada. Limite diário excedido.'+acao+'Transação não autorizada. Limite diário excedido. Solicite ao portador que entre em contato com seu banco emissor.'+retentativa_nao,
         'BM':descricao+'BM Transação não autorizada. Cartão inválido.'+acao+'Transação não autorizada. Cartão inválido. Pode ser bloqueio do cartão no banco emissor.'+retentativa_nao,
         'BN':descricao+'BN Transação não autorizada. Cartão ou conta bloqueado.'+acao+'Transação não autorizada. O cartão ou a conta do portador está bloqueada. Solicite aoportador que entre em contato com seu banco emissor.'+retentativa_nao,
         'BV':descricao+'BV Transação não autorizada. Cartão vencido.'+acao+'Transação não autorizada. Cartão vencido.'+retentativa_nao,
         'CF':descricao+'CF Transação não autorizada. Falha na validação dos dados.'+acao+'Transação não autorizada. Falha na validação dos dados. Solicite ao portador que entre em contato com o banco emissor.'+retentativa_nao,
         'EE':descricao+'EE Transação não permitida. Valor da parcela inferior ao mínimo permitido.'+acao+'Transação não permitida. Valor da parcela inferior ao mínimo permitido. Não é permitido parcelas inferiores a R$ 5,00. Necessário rever calculo para parcelas.'+retentativa_nao,
         'FA':descricao+'FA Transação não autorizada.'+acao+'Transação não autorizada AMEX.'+retentativa_nao,
         'FC':descricao+'FC Transação não autorizada. Ligue emissor'+acao+'Transação não autorizada. Oriente o portador a entrar em contato com o banco emissor.'+retentativa_nao,
         'GA':descricao+'GA Transação não autorizada.'+acao+'Referida pelo Cielo. Oriente o portador a aguardar alguns instantes e tentar novamente'+retentativa_ok,
         'GD':descricao+'GD Transação não permitida.'+acao+'Transação não é possível ser processada no estabelecimento.Entre em contato com a administradora do cartão para obter mais detalhes.'+retentativa_ok,
         'KA':descricao+'KA Transação não permitida. Falha na validação dos dados.'+acao+'Transação não permitida. Houve uma falha na validação dos dados. Solicite ao portador que reveja os dados e tente novamente.'+retentativa_ok,
         'KE':descricao+'KE Transação não autorizada. Falha na validação dos dados.'+acao+'Transação não autorizada. Falha na validação dos dados.'+retentativa_nao,
         'N7':descricao+'N7 Transação não autorizada. Código de segurança inválido.'+acao+'Transação não autorizada. Código de segurança inválido. Oriente o portador corrigir os dados e tentar novamente.'+retentativa_ok,

         'TEF':descricao+'TEF - Solicitar Assinatura.'+acao+'Operador deve pressionar Enter.'+retentativa_nao,
         'DAI':descricao+'Data abertura invalida.'+acao+'PDV com fechamento parcial. Fazer o procedimento de fechamento para logo dar entrada ao operador.'+retentativa_ok,

         }

@bot.message_handler(commands=['iniciar','start'])
def send_welcome(message):
    bot.reply_to(message, 'Bem-vindo, esse nosso bot da T.I chegou para facilitar a nossa vida!\nPara começar digite o código do erro que aparece na tela do PDV.')

@bot.message_handler(func=lambda message:'00')
def send_message(message):
    for e in erros.keys():
        if message.text == e:
            bot.reply_to(message,erros[e])




bot.infinity_polling()
