import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, MessageReactionUpdated

TOKEN = "8834663877:AAHawW6aHk3hrKJr5YLlOQ5mDvgJxdnzd_c"

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Отправь мне сообщение, а потом поставь на него реакцию (например 🔥).")

@router.message_reaction()
async def handle_reaction(event: MessageReactionUpdated):
    user = event.user.full_name

    def reaction_to_text(r):
        if r.type == "emoji":  # обычный смайлик
            return r.emoji
        elif r.type == "custom_emoji":  # премиум реакция
            return f"[custom:{r.custom_emoji_id}]"
        return "[unknown]"

    # Новые реакции
    if event.new_reaction:
        emojis = ", ".join(reaction_to_text(r) for r in event.new_reaction)
        print(f"{user} поставил реакцию {emojis}")

    # Удалённые реакции
    if event.old_reaction:
        emojis = ", ".join(reaction_to_text(r) for r in event.old_reaction)
        print(f"{user} убрал реакцию {emojis}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
