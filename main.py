from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class JDINPUT(BaseModel):
    jd_text:str

@app.get("/")
def home():
    return {'message':'FastAPI is running successfully'}

@app.post('/test')
def end_point(jd:JDINPUT):
    return {'received':jd.jd_text}