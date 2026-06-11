from fastapi import FastAPI,File,UploadFile,Form,HTTPException
from pydantic import BaseModel
import shutil,os
from matcher import compute_match_score,missing_skills
from utils import extract_words

app = FastAPI()

class JDINPUT(BaseModel):
    jd_text:str

@app.get("/")
def home():
    return {'message':'FastAPI is running successfully'}

@app.post('/test')
def end_point(jd:JDINPUT):
    return {'received':jd.jd_text}

@app.post('/match')
async def match_resume( resume:UploadFile=File(...), jd_text:str=Form(...)):
    # step 1 save uploaded pdf temporarly

    if not resume.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only pdf files are allowed"
        )
    
    if not jd_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Job decription cannot be empty"
        )

    temp_path=f"temp_{resume.filename}"
    with open(temp_path,'wb') as f:
        shutil.copyfileobj(resume.file,f)

    # step 2 extract text from temp_path

    resume_text = extract_words(temp_path)

    if not resume_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from PDF. Make sure it is not a scanned image."
        )
    # step 3 remove/delete temp path

    os.remove(temp_path)

    # step 4 compute matching socre and missing

    score = compute_match_score(jd_text,resume_text)
    miss = missing_skills(jd_text,resume_text)

    return{
        'resume_text: ':resume_text,
        'matching score is: ':score,
        'Missing keywords ':miss
    }
    