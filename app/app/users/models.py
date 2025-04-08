from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from sqlalchemy import select 
from passlib.hash import bcrypt # Для хеширования паролей

from config import get_db_url

DATABASE_URL =  get_db_url()

engine = create_async_engine(DATABASE_URL, echo=True)

Base = declarative_base()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# pwd_context = CryptContext(
#     bcrypt__rounds=12, # Или другое значение rounds
#     deprecated="auto"
# )

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.hashed_password)


async def get_db():
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
    
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def validate_user(username, password, db: AsyncSession):
    """Проверяет имя пользователя и пароль."""
    query = select(User).where(User.username == username)
    result = await db.execute(query)
    user = result.scalars().first()

    if not user:
        return False, "Неверное имя пользователя или пароль."

   
    if not pwd_context.verify(password, user.hashed_password):
        return False, "Неверное имя пользователя или пароль."

    return True, user # Возвращаем True и объект User, если всё ОК

async def create_user(username, password, role, db: AsyncSession):
    """Создает нового пользователя в базе данных."""
    hashed_password = pwd_context.hash(password) # Хешируем пароль bcrypt
    new_user = User(username=username, hashed_password=hashed_password, role=role)  # Сохраняем хешированный пароль
    db.add(new_user)
    try:
        await db.commit()
        await db.refresh(new_user) # Обновляем объект чтобы получить ID из БД
        return new_user
    except IntegrityError:
        await db.rollback()  # Откатываем транзакцию в случае ошибки
        return "Имя пользователя уже занято." # Возвращаем сообщение об ошибке
    except Exception as e:
        await db.rollback()
        print(f"Ошибка при создании пользователя: {e}")
        return "Произошла ошибка при создании пользователя."