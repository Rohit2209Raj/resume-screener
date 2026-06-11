import numpy as np
import spacy
from sentence_transformers import SentenceTransformer,util

# model loading
model=SentenceTransformer('all-MiniLM-L6-v2')
nlp=spacy.load('en_core_web_sm')

# keyword finding 
def find_keywords(des:str)->list:
    keywords=[]
    doc=nlp(des)
    for chunk in doc.noun_chunks:
        keywords.append(chunk.text.lower())
    return keywords

#  finding missing skills between resume and jd_text
def missing_skills(des:str,resume:str)->list:
    
    des = des.replace('\n', ' ').replace('|', ' ').replace('-', ' ')  # add this line
    keywords = []
    doc = nlp(des)
    for chunk in doc.noun_chunks:
        parts = chunk.text.lower().split(',')
        for part in parts:
            cleaned = part.strip()
            if cleaned:
                keywords.append(cleaned)
    return keywords


# computing match score between resume and jd using sentence tranformers
def compute_match_score(jd_text:str,resume_text: str)->float:
    '''
    Takes resume text and jd text
    and return similarity score between 0 and 100
    '''
    if not resume_text or not jd_text:
        return 0.0
    
    emb_resume=model.encode(resume_text)
    emb_jd=model.encode(jd_text)

    similarity=util.cos_sim(emb_resume,emb_jd)

    return round(float(similarity) * 100, 1)


    