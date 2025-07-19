main.py

import logging from aiogram import Bot, Dispatcher, types, executor from utils import get_movie_results, generate_verification_link, verify_user, send_movie_file

API_TOKEN = '8032468458:AAHa43tmVZgJvaprKNynTlG63x2-wGztGRQ' ADMIN_ID = 5058539166  # Replace with your Telegram ID

logging.basicConfig(level=logging.INFO) bot = Bot(token=API_TOKEN) dp = Dispatcher(bot)

user_states = {}

@dp.message_handler(commands=['start']) async def send_welcome(message: types.Message): await message.answer("👋 Welcome to Rozibot!\nSend me any movie name to begin.")

@dp.message_handler() async def movie_search(message: types.Message): query = message.text.strip() results = await get_movie_results(query)

if not results:
    await message.reply("❌ No results found.")
    return

buttons = []
for i, (caption, _) in enumerate(results):
    buttons.append([
        types.InlineKeyboardButton(
            text=f"🔗 Get Link {i+1}",
            callback_data=f"getlink_{i}"
        )
    ])

keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
result_text = f"🔍 Results for *{query}*:\n\n" + "\n".join([
    f"{i+1}. {caption}" for i, (caption, _) in enumerate(results)
])
await message.reply(result_text, parse_mode="Markdown", reply_markup=keyboard)
user_states[message.from_user.id] = results

@dp.callback_query_handler(lambda c: c.data.startswith("getlink_")) async def handle_link_request(callback_query: types.CallbackQuery): user_id = callback_query.from_user.id index = int(callback_query.data.split("_")[1]) results = user_states.get(user_id)

if not results or index >= len(results):
    await callback_query.answer("Invalid request")
    return

# Verification
short_url = await generate_verification_link(user_id)
text = f"✅ To get the movie, verify yourself by clicking below:\n{short_url}"
await bot.send_message(user_id, text)

user_states[user_id] = ("pending_verification", results[index][1])
await callback_query.answer("Verification link sent!")

@dp.message_handler(lambda message: message.text.startswith("/verified")) async def after_verification(message: types.Message): user_id = message.from_user.id status = user_states.get(user_id) if not status or status[0] != "pending_verification": await message.reply("❌ No pending verification.") return

verified = await verify_user(user_id)
if verified:
    file_id = status[1]
    await send_movie_file(bot, user_id, file_id)
    await message.reply("🎉 Movie sent successfully!")
    del user_states[user_id]
else:
    await message.reply("❌ Verification failed. Please try again.")

if name == 'main': executor.start_polling(dp, skip_updates=True)

main.py

import logging from aiogram import Bot, Dispatcher, types, executor from utils import get_movie_results, generate_verification_link, verify_user, send_movie_file

API_TOKEN = '8032468458:AAHa43tmVZgJvaprKNynTlG63x2-wGztGRQ' ADMIN_ID = 5058539166  # Replace with your Telegram ID

logging.basicConfig(level=logging.INFO) bot = Bot(token=API_TOKEN) dp = Dispatcher(bot)

user_states = {}

@dp.message_handler(commands=['start']) async def send_welcome(message: types.Message): await message.answer("👋 Welcome to Rozibot!\nSend me any movie name to begin.")

@dp.message_handler() async def movie_search(message: types.Message): query = message.text.strip() results = await get_movie_results(query)

if not results:
    await message.reply("❌ No results found.")
    return

buttons = []
for i, (caption, _) in enumerate(results):
    buttons.append([
        types.InlineKeyboardButton(
            text=f"🔗 Get Link {i+1}",
            callback_data=f"getlink_{i}"
        )
    ])

keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
result_text = f"🔍 Results for *{query}*:\n\n" + "\n".join([
    f"{i+1}. {caption}" for i, (caption, _) in enumerate(results)
])
await message.reply(result_text, parse_mode="Markdown", reply_markup=keyboard)
user_states[message.from_user.id] = results

@dp.callback_query_handler(lambda c: c.data.startswith("getlink_")) async def handle_link_request(callback_query: types.CallbackQuery): user_id = callback_query.from_user.id index = int(callback_query.data.split("_")[1]) results = user_states.get(user_id)

if not results or index >= len(results):
    await callback_query.answer("Invalid request")
    return

# Verification
short_url = await generate_verification_link(user_id)
text = f"✅ To get the movie, verify yourself by clicking below:\n{short_url}"
await bot.send_message(user_id, text)

user_states[user_id] = ("pending_verification", results[index][1])
await callback_query.answer("Verification link sent!")

@dp.message_handler(lambda message: message.text.startswith("/verified")) async def after_verification(message: types.Message): user_id = message.from_user.id status = user_states.get(user_id) if not status or status[0] != "pending_verification": await message.reply("❌ No pending verification.") return

verified = await verify_user(user_id)
if verified:
    file_id = status[1]
    await send_movie_file(bot, user_id, file_id)
    await message.reply("🎉 Movie sent successfully!")
    del user_states[user_id]
else:
    await message.reply("❌ Verification failed. Please try again.")

if name == 'main': executor.start_polling(dp, skip_updates=True)

