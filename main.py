from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


from routers import router as site

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(site)