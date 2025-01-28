from pyrogram import Client

app = Client("my_bot")

@app.on_message()
async def handle_message(client, message):
    await message.reply("Hello, I'm your bot!")

# Running the bot
if __name__ == "__main__":
    app.run()  # Ensure no 'use_qr' is passed
