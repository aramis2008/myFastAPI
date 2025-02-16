from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from app.user.router import router as router_users

app = FastAPI()

#app.mount('/static', StaticFiles(directory='app/static'), 'static')


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_users)