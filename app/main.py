from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pages.router import router as pages_router



app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(pages_router)


# Ссылки на главном меню
@app.get('/myapplication') # Мои заявки
async def myapplication():
    return {'data': 'ok'}

@app.get('/frequent') # Частые заявки
async def frequent():
    return {'data': 'ok'}

@app.get('/reviews') # Отзывы
async def reviews():
    return {'data': 'ok'}

@app.get('/faq') # Часто задаваемые вопросы
async def faq():
    return {'data': 'ok'}

# Кнопки снизу
@app.get("/")
async def home():
    return {'data': 'ok'}


@app.get('/allapplication')
async def allapplication():
    return {'data': 'ok'}

@app.get('/profile')
async def profgile():
    return {'data': 'ok'}
