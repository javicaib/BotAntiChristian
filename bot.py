from main import SRNI
import os
import telebot
import dotenv
dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN_BOT'))

authorized_users = [
    # Javier
    731096143,
]

# Define el decorador para el acceso restringido


def restricted_access(func):
    def wrapper(message):
        user_id = message.from_user.id

        # Verifica si el usuario está autorizado o es miembro del grupo permitido
        if user_id in authorized_users:
            return func(message)
        else:
            bot.reply_to(
                message, 'Lo siento, no estás autorizado para ejecutar este comando.')
            log = f'Usuario jugando con el bot: ID: {user_id} , ' \
                  f'USER: @{message.from_user.username} ,' \
                  f' NAME : {message.from_user.full_name}'
            print(log)

    return wrapper


@bot.message_handler(commands=['start', ])
def cmd_start(msg):
    welcome = f"¡Bienvenido @{msg.chat.username} a <strong>AntiChristian Control</strong> ! \n " \
              f"Este bot es una herramienta especializada que te ayudará a  estar " \
              f"al tanto de cuando Christian use tu cuenta. "
    bot.reply_to(msg, welcome, parse_mode='html')


@bot.message_handler(commands=['status'])
@restricted_access
def cmd_status(msg):
    javi = SRNI()
    lastCon = javi.getLasChristianConnection()
    output = f'Christian a usado tu cuenta por ultima ves a las <strong>{lastCon}</strong>'
    bot.send_message(
        msg.chat.id, output, parse_mode='html')


def start_bot():
    print('INICIANDO BOT')
    bot.set_my_commands([
        telebot.types.BotCommand('/start', 'Inicia el BOT'),
        telebot.types.BotCommand(
            '/status', 'Muestra la ultima hora que Christian uso tu cuenta'),

    ])

    bot.infinity_polling()


start_bot()
