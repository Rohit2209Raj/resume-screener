import numpy as np
from sentence_transformers import SentenceTransformer,util

# model loading
model=SentenceTransformer('all-MiniLM-L6-v2')

def compute_match_score(resume_text:str,jd_text: str)->float:
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

# testing
if __name__=="__main__":
    resume = "Python developer with machine learning experience"
    jd = "Hiring Python programmer with ML background"

    score=compute_match_score(resume,jd)
    print(score)

    