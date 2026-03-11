from telethon import TelegramClient, events

api_id = 6339346924
api_hash = "YOUR_API_HASH"

group = "tc1minute"
user = "@Piyush_20067"

win_count = 0

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=group))
async def handler(event):
    global win_count

    text = event.raw_text.upper()

    if "WIN" in text:
        win_count += 1

        if win_count >= 5:
            await client.send_message(user,"🔥 5 Continuous WIN ho gaye!")
            win_count = 0

    else:
        if "PERIOD ID" in text:
            win_count = 0

client.start()
client.run_until_disconnected()
