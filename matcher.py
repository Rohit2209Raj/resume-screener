import numpy as np
import spacy
from sentence_transformers import SentenceTransformer,util

# model loading
model=SentenceTransformer('all-MiniLM-L6-v2')
nlp=spacy.load('en_core_web_sm')

def find_keywords(des:str)->list:
    keywords=[]
    doc=nlp(des)
    for chunk in doc.noun_chunks:
        keywords.append(chunk.text.lower())
    return keywords

def missing_skills(des:str,resume:str)->list:
    # jd_skills=find_keywords(jd)
    # resume_skills=find_keywords(resume)

    # missing=[]

    # for ele in jd_skills:
    #     if ele not in resume_skills:
    #         missing.append(ele)

    # return f'Missing skills: {missing}'

    # jd_skills = find_keywords(jd)
    # resume_lower = resume.lower()  # raw text, not chunks

    # missing = []
    # for skill in jd_skills:
    #     if skill not in resume_lower:  # check in raw text
    #         missing.append(skill)

    # return f'Missing skills: {missing}'

    
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

    # return f'Matching Score: {round(float(similarity) * 100, 1)}'
    return round(float(similarity) * 100, 1)


# testing
if __name__=="__main__":
    resume = "Python developer with machine learning experience"
    jd = "Hiring Python programmer with ML background"

    score=compute_match_score(resume,jd)
    miss=missing_skills(jd,resume)
    print(score)
    print(miss)

    