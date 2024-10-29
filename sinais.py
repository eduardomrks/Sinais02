import random
import datetime
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Configurações do bot (substitua pelos seus dados)
api_token = '7731646908:AAHfFCFYkt5cce1sNGcvoaY1wlvYpqlID3o'  # Substitua pelo seu token
chat_id = '-1002205711968'  # Substitua pelo ID do grupo

# Inicializando o bot
bot = Bot(token=api_token)

# Função para gerar horários com intervalo de 10 a 15 minutos, começando a partir de um horário fixo
def gerar_horarios():
    base_time = datetime.datetime.now().replace(second=0, microsecond=0, minute=5)  # Define o minuto inicial como 05
    horarios = [base_time]
    
    for i in range(5):  # Gerar mais 5 horários (total de 6), alternando intervalos de 10 e 15 minutos
        intervalo = 10 if i % 2 == 0 else 15  # Alterna entre 10 e 15 minutos
        next_time = horarios[-1] + datetime.timedelta(minutes=intervalo)
        horarios.append(next_time)
    return horarios

# Função para formatar horários em colunas
def formatar_horarios(horarios):
    linha1 = ' | '.join([h.strftime('%H:%M') for h in horarios[:3]])  # Primeira linha (3 horários)
    linha2 = ' | '.join([h.strftime('%H:%M') for h in horarios[3:]])  # Segunda linha (3 horários)
    return f"⏰  {linha1}\n⏰  {linha2}"

# Função para enviar a mensagem de sinais
async def enviar_sinais(jogo, data_valida):
    horarios = gerar_horarios()

    # Mensagem sem escapar caracteres
    msg_sinais = f"""
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: {jogo}
{formatar_horarios(horarios)}
📅 VÁLIDO ATÉ: {data_valida}


🚨 PLATAFORMA REGULARIZADA ⬇️
🎰 Plataforma: https://abrir.ai/SlotsOfc
⚠️ NÃO TENTE EM OUTRO SITE ⬆️

👇 APLICATIVO DOS SLOTS 👇
📲 https://robos.top/Ofc 📲
🔞 Jogue com responsabilidade!
"""

    # Criar botões
    keyboard = [
        [InlineKeyboardButton("🚨JOGUE AQUI🚨", url="https://abrir.ai/SlotsOfc")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar a mensagem com imagem e botões
    with open('Cadastre-img.png', 'rb') as image:
        await bot.send_photo(chat_id=chat_id, photo=image, caption=msg_sinais, reply_markup=reply_markup)

# Função para enviar a mensagem de finalização
async def enviar_finalizacao():
    msg_finalizacao = """
⌛️ MINUTOS FINALIZADOS ⌛️
✅✅✅ VITÓRIA ✅✅✅
"""

    # Criar botões para a mensagem de finalização
    keyboard = [
        [InlineKeyboardButton("🎁CADASTRE-SE🎁", url="https://abrir.ai/SlotsOfc")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar a mensagem de finalização com botões
    await bot.send_message(chat_id=chat_id, text=msg_finalizacao, reply_markup=reply_markup)

# Função principal que coordena o envio das mensagens a cada 1h com a finalização 5 minutos antes
async def main_loop():
    while True:  # Loop infinito
        data_valida = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

        # Lista de jogos e suas respectivas mensagens
        jogos = [
            "🐯 Fortune Tiger 🐯",
            "🐭 Fortune Mouse 🐭",
            "🐂 Fortune OX 🐂",
            "🐲 Fortune Dragon 🐲",
            "🐰 Fortune Rabbit 🐰"
        ]

        for jogo in jogos:
            await enviar_sinais(jogo, data_valida)  # Enviar a mensagem de sinais

            # Esperar 55 minutos antes de enviar a mensagem de finalização
            await asyncio.sleep(55 * 60)

            await enviar_finalizacao()  # Enviar a mensagem de finalização

            # Esperar mais 5 minutos até enviar os próximos sinais
            await asyncio.sleep(5 * 60)

# Executar o loop principal
asyncio.run(main_loop())
