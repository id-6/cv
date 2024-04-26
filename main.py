from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me a story link to download it.')

def download_story(update: Update, context: CallbackContext) -> None:
    story_link = update.message.text
    # Add code here to download the story from the link
    update.message.reply_text(f'Downloading story from {story_link}...')

def main() -> None:
    updater = Updater("6044876527:AAH9DdgcP9xhAK2HcWu9HGgw_Dx4qjF4P7E", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_story))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
