import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update):
    keyboard1 = [[InlineKeyboardButton("Post", callback_data='Post'),
                 InlineKeyboardButton("Net", callback_data='Net'),
                 InlineKeyboardButton("Phone", callback_data='Phone'),
                 InlineKeyboardButton("Bank", callback_data='Bank'),
                 InlineKeyboardButton("Other", callback_data='Other')]]

    reply_markup = InlineKeyboardMarkup(keyboard1)

    bot.sendMessage(update.message.chat_id, text="What do you need help with?", reply_markup=reply_markup)

    keyboard2 = [[InlineKeyboardButton("Accounts", callback_data='Accounts'),
                 InlineKeyboardButton("Cards", callback_data='Cards'),
                 InlineKeyboardButton("Other", callback_data='Other')]]

    reply_markup = InlineKeyboardMarkup(keyboard2)

    bot.sendMessage(update.message.chat_id, text="What would you like to know about banking?", reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    bot.editMessageText(text="Alright, I'll help you with %sing" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)

    bot.sendMessage(chat_id=update.message.chat_id,
                text="")

def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text="Use /start to test this bot.")


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("232175939:AAHZ-wqUv6fuXp7E1V8JOIdvrPzT-uyIF-I")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()
