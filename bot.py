from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from gingerit.gingerit import GingerIt

ginger_parser = GingerIt()


def start(bot, update):
    """Send a message when the command /start is issued."""
    user = update.message.from_user
    print(user)
    uname = user['first_name']
    text = f'''
            Hi {uname}!
Welcome to grammar check bot, just enter text want to check
            '''
    update.message.reply_text(text)


def echo(bot, update):
    msg = ""
    message_user = update.message.text
    ginger_grammar_results = ginger_parser.parse(message_user)
    ginger_corrections = ginger_grammar_results['corrections']
    if len(ginger_corrections) != 0:
        msg += "\nNumber of grammar issues found: " + str(len(ginger_corrections)) + "\n"
        for correction in ginger_corrections:
            msg += "Use '" + correction['correct'] + "' instead of '" + correction['text'] + "'" + "\n"
        msg += "\nCorrections: " + ginger_grammar_results['result']
    else:
        msg += "Seems your grammar is correct"
    update.message.reply_text(msg)


def main():
    updater = Updater("1002883569:AAFACRjWSU0_t0_6G9rQjlWzjK69qocMzPw", use_context=False)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    
    updater.idle()
    
if __name__ == "__main__":
    main()