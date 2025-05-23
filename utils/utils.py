from database.database import SessionLocal
from models.models import User, Task
from aiogram.types import Message

async def send_task_notification(bot, user_id: int, task: Task):
    msg = f"Вам назначена новая задача (ID: {task.task_id}):\n{task.description}"
    try:
        await bot.send_message(user_id, msg)
    except Exception as e:
        print(f"Ошибка отправки уведомления пользователю {user_id}: {e}")

def is_admin(user_id: int) -> bool:
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        return user.is_admin if user else False
    finally:
        session.close()