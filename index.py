from fastapi import FastAPI , Path
from routes.student import student

app = FastAPI()
app.include_router(student)


