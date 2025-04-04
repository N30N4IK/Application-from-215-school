from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import jinja2



router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get('/myapplication')
async def myapplication(request: Request):
    return templates.TemplateResponse('myapplication.html', {'request': request})

@router.get('/myapplication/create')
async def create(request: Request):
        return templates.TemplateResponse('create_application.html', {'request': request})

@router.get('/profile')
async def profile(request: Request):
     return templates.TemplateResponse('profile.html', {"request": request})

@router.get('/profile/settings')
async def progile_sett(request: Request):
     return templates.TemplateResponse('profile_settings.html', {"request": request})

@router.get('/frequent')
async def frequent(request: Request):
     return templates.TemplateResponse('frequent.html', {"request": request})

@router.get('/myapplication/filter')
async def filters(request: Request):
     return templates.TemplateResponse('application_filter.html', {"request": request})
     
