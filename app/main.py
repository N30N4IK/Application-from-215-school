from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles




app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')



# Ссылки на главном меню
@app.get('/myapplications')
async def myapplication():
    return {'data': 'ok'}

@app.get('/frequent')
async def frequent():
    return {'data': 'ok'}

@app.get('/reviews')
async def reviews():
    return {'data': 'ok'}

@app.get('/faq')
async def faq():
    return {'data': 'ok'}

# Кнопки снизу
@app.get("/")
async def home():
    return {'data': 'ok'}

@app.get('/completed')
async def completed():
    return {'data': 'ok'}

@app.get('/')