from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.students.router import router as router_students
from app.majors.router import router as router_majors
from app.users.router import router as router_users
from app.privileges.router import router as router_privileges
from app.pages.router import router as router_pages

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "hello, world!"}


app.include_router(router_students)
app.include_router(router_majors)
app.include_router(router_users)
app.include_router(router_privileges)
app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='app/static'), 'static')
