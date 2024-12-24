import hashlib
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse



from functions import validate_token
from config import site_url_and_port, key

router = APIRouter()

templates = Jinja2Templates(directory="templates")




@router.get("/login")
async def page_(request: Request):    
    return templates.TemplateResponse(
        "login.html",
         {
            "request": request,
            "title": "Войти",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/logout")
async def page_(request: Request, response: Response):
    response = RedirectResponse(url="/login")      
    response.delete_cookie("Bearer")
    return response


@router.get("/register")
async def page_(request: Request):    
    return templates.TemplateResponse(
        "register.html",
         {
            "request": request,
            "title": "Регистрация",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/referral_register/{id}_personal_number{personal_number}")
async def referral_register_page(
    id: int,
    personal_number: str,
    request: Request
    ):
    return templates.TemplateResponse(
        "referral_register.html",
        {
            "request": request,
            "title": "Регистрация по реферальному коду",
            "site_url_and_port": site_url_and_port,
            "sponsor_id": id,  # Передаем ID спонсора
            "sponsor_personal_number": personal_number  # Передаем номер спонсора
        }
    )

@router.get("/")
async def page_(request: Request):
    
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "index.html",
         {
            "request": request,
            "title": "Главная",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/structure")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "structure.html",
         {
            "request": request,
            "title": "Структура",
            "token": session_key,
            "key": key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )


@router.get("/structure/{securePath}/{id}/{securePath2}{securePath3}")
async def page_(id: int, request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")

    return templates.TemplateResponse(
        "structure_one.html",
         {
            "request": request,
            "title": "Структура",
            "token": session_key,
            "id": id,
            "key": key,
            "current_path": "/structure",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/gift")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "gift.html",
         {
            "request": request,
            "title": "Подарочные",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/balance")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "balance.html",
         {
            "request": request,
            "title": "Баланс",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )

# 

@router.get("/sponsored")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "sponsored_in.html",
         {
            "request": request,
            "title": "Личники в структуре",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/new/sponsored")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "sponsored_none.html",
         {
            "request": request,
            "title": "Новые личники",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )


@router.get("/rewards")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "rewards.html",
         {
            "request": request,
            "title": "Вознаграждения",
            "token": session_key,
            "current_path": request.url.path,
            "site_url_and_port": site_url_and_port
        }
    )


@router.get("/rewards/binar")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/binar.html",
         {
            "request": request,
            "title": "Бинар",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/referal")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/referal.html",
         {
            "request": request,
            "title": "Вознаграждения",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/cheque")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/cheque.html",
         {
            "request": request,
            "title": "Вознаграждения",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/status")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/status.html",
         {
            "request": request,
            "title": "Вознаграждения",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )


@router.get("/rewards/sponsor")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/sponsor.html",
         {
            "request": request,
            "title": "Вознаграждения",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/surprise")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/surprise.html",
         {
            "request": request,
            "title": "Неожиданный",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/tour")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/tour.html",
         {
            "request": request,
            "title": "Туристический",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/auto")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/auto.html",
         {
            "request": request,
            "title": "Автопрограмма",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/rewards/business")
async def page_(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "components/rewards/business.html",
         {
            "request": request,
            "title": "Бизнес",
            "token": session_key,
            "current_path": "/rewards",
            "site_url_and_port": site_url_and_port
        }
    )

@router.get("/sanctions")
async def sanctions_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "sanctions.html",
        {
            "request": request,
            "title": "Cанкции",
            "token": session_key,
            "current_path": "/sanctions",
        }
    )

@router.get("/sanctions/file")
async def sanctions_file():
    file_path = "file/sanctions.pdf"  # Укажите путь к вашему PDF
    return FileResponse(file_path, media_type="application/pdf")


@router.get("/catalog")
async def catalog_page(request: Request):
    session_key = request.cookies.get("Bearer")
    if session_key is None:
        return RedirectResponse(url="/login")
    
    status = await validate_token(session_key)
    if status != 200:
        return RedirectResponse(url="/login")
    
    return templates.TemplateResponse(
        "catalog.html",
        {
            "request": request,
            "title": "Каталог",
            "token": session_key,
            "current_path": "/catalog",
        }
    )


@router.get("/catalog/file")
async def catalog_file():
    file_path = "file/catalog.pdf"  # Укажите путь к вашему PDF
    return FileResponse(file_path, media_type="application/pdf")