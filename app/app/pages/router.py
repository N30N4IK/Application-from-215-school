from fastapi import APIRouter, Request, Depends, Response, HTTPException, FastAPI, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from users.models import User, get_db, validate_user, create_user
import jinja2
import uuid

# Sample user data (replace with your authentication system)
users = {
    "admin": {"role": "admin", "name": "Admin"},
    "user": {"role": "user", "name": "User"},
    "tech": {'role': 'tech', 'name': 'Technician'},
    "guest": {"role": "guest", "name": "Guest"},
}

role_specific_cookies = {
     "админ": {"username": "username", "value": "admin"},
     "пользователь": {"username": "username", "value": "user"},
     "техник": {"username": "username", "value": "tech"},
     "гость": {"username": "username", "value": "guest"},
}

async def get_user(request: Request): # Функция
    username = request.cookies.get("username") # Запрос файлов cookie со стороны клиента, чтобы определить значение
    if username == "user": # Условие, если файл имеет значение "user"
        return {"username": "user", "role": "user"} # Отправление файлов cookie уже клиенту и их присваивание
    elif username == "admin": # Условие, если файл имеет значение "admin"
        return {"username": "admin", "role": "admin"} # Отправление файлов cookie уже клиенту и их присваивание
    elif username == 'tech': # Условие, если файл имеет значение "tech"
        return {"username": "tech", "role": "tech"} # Отправление файлов cookie уже клиенту и их присваивание
    else: # Если ни одно условие не выполнено, будет присваиваться роль guest(Гость)
        return {"username": "guest", "role": "guest"} # Отправление файлов cookie уже клиенту и их присваивание
    

app = FastAPI()
router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, user: dict = Depends(get_user)):
    if user['role'] in ['admin', 'user']:
     return templates.TemplateResponse("home.html", {"request": request, "user": user})
    elif user['role'] == 'tech':
        return templates.TemplateResponse('myapplication.html', {"request": request, 'user': user})
    else:
        return templates.TemplateResponse('home.html', {'request': request, 'user': user})

@router.get('/myapplication', response_class=HTMLResponse)
async def myapplication(request: Request, user: dict = Depends(get_user)):
    return templates.TemplateResponse('myapplication.html', {'request': request, "user": user})

@router.get('/myapplication/create', response_class=HTMLResponse)
async def create(request: Request, user: dict = Depends(get_user)):
    return templates.TemplateResponse('create_application.html', {'request': request, "user": user})

@router.get('/myapplication/create/complete', response_class=HTMLResponse)
async def application_create_complete(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('myapplication_create_complete.html', {'request': request, "user": user})

@router.get('/profile', response_class=HTMLResponse)
async def profile(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('profile.html', {"request": request, "user": user})

@router.get('/profile/settings', response_class=HTMLResponse)
async def progile_sett(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('profile_settings.html', {"request": request, "user": user})

@router.get('/profile/settings/add-user', response_class=HTMLResponse)
async def add_user_page(request: Request, user: dict = Depends(get_user)):
    return templates.TemplateResponse('reg.html', {"request": request, "user": user})

@router.post("/add-user")
async def add_user(request: Request, db: AsyncSession = Depends(get_db)):
    """Регистрирует нового пользователя."""
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")
    confirm_password = form_data.get("confirm_password")
    role = form_data.get('role')

    if not username or not password or not confirm_password or not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Необходимо указать имя пользователя, пароль и подтверждение пароля",
        )

    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пароли не совпадают",
        )

    # Создаем пользователя
    user_or_error = await create_user(username, password, role, db)

    if isinstance(user_or_error, str):  # Проверяем, вернулась ли строка ошибки
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=user_or_error  # Передаем сообщение об ошибке
        )
    else:
    # Успешная регистрация.  Здесь можно перенаправить пользователя или вернуть JWT
      return RedirectResponse('/profile', status_code=status.HTTP_303_SEE_OTHER)

@router.get('/frequent', response_class=HTMLResponse)
async def frequent(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('frequent.html', {"request": request, "user": user})

@router.get('/frequent/requests', response_class=HTMLResponse)
async def frequent_requests(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('frequent_requests.html', {"request": request, "user": user})

@router.get('/myapplication/filter', response_class=HTMLResponse)
async def filters(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('application_filter.html', {"request": request, "user": user})
     
@router.get('/reviews/create', response_class=HTMLResponse)
async def reviews_create(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('reviews.html', {"request": request, "user": user})

@router.get('/reviews', response_class=HTMLResponse)
async def reviews_list(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('reviews_list.html', {"request": request, "user": user})

@router.get('/reviews/complete', response_class=HTMLResponse)
async def reviews_complete(request: Request, user: dict = Depends(get_user)):
     return templates.TemplateResponse('reviews1.html', {"request": request, "user": user})

@router.get("/logout", response_class=HTMLResponse)
async def logout_page(request: Request):
     response = templates.TemplateResponse("profile_exit.html", {"request": request})

     response.delete_cookie("username", path="/")
     response.set_cookie("username", "guest") # Set the cookie *after* deleting. No `max_age` or `expires` if you want it to expire with the session.
     return response

@router.get("/login-page", response_class=HTMLResponse)
async def login_page(request: Request, user: dict = Depends(get_user)):
    return templates.TemplateResponse('login.html', {"request": request, 'user': user})

@router.post("/login", response_class=HTMLResponse)  # Указываем response_class
async def login(request: Request, db: AsyncSession = Depends(get_db)):
    print("Endpoint /login был вызван!")
    """Форма входа в аккаунт"""
    form_data = await request.form() 
    username = form_data.get("username")
    password = form_data.get("password")

    if not username or not password: # Ошибка, если не полностью заполнили форму входа
        return templates.TemplateResponse("login.html", {"request": request, "error": "Необходимо указать имя пользователя и пароль"})

    # Вызываем функцию валидации
    is_valid, user_or_error = await validate_user(username, password, db) # Определение переменных, из которых первая отвечает за удачный вход, а вторая - за ошибку

    if not is_valid:
        return templates.TemplateResponse("login.html", {"request": request, "error": user_or_error}) # Вывод ошибки при неверных данных

    user = user_or_error  # Получаем объект User (если валидация прошла успешно)
    
    response = RedirectResponse("../", status_code=status.HTTP_302_FOUND) # перенаправляем на / (При успешной валидации/верификации)

    role_cookie_name = "user_role"  # Имя cookie для роли
    response.set_cookie(key=role_cookie_name, value=user.role, httponly=True)  # user.role является значением в таблице базы данных, и значение из ... значения будет таким

    return response # Переадресация на другой url 


app.include_router(router)

@app.middleware("http")
async def redirect_guest_middleware(request: Request, call_next):
    user = await get_user(request)
    is_login_post = request.url.path == "/login" and request.method == "POST" # Проверяем path и метод

    if user["role"] == "guest" and request.url.path not in ["/", "/login", "/register", "/logout"] and not is_login_post:
        return RedirectResponse("/")

    response = await call_next(request)
    return response
