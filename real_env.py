from matcher import find_keywords,missing_skills,compute_match_score
from utils import extract_words
# my_resume='''
# Languages: Python, C++
# Core CS: Data Structures & Algorithms, Object-Oriented Programming, DBMS
# Data Science & Analytics: NumPy, Pandas, Matplotlib, Seaborn, Exploratory Data Analysis (EDA) ,
# Scikit-learn , Data Preprocessing
# Databases: PostgreSQL, SQL
# Tools: Jupyter Notebook, Google Colab, Git, GitHub, VS Code, Power BI, MS Excel


# '''
path=r'D:\resume-screener\test_resume.pdf'
my_resume=extract_words(path)

real_jd='''

Job Description — Data Science Intern
Analytics India Pvt Ltd
We are looking for a curious and motivated Data Science Intern to join our analytics team. This is a great opportunity for students who want to apply their machine learning knowledge on real business problems.
Responsibilities:

Perform Exploratory Data Analysis on structured datasets
Build basic machine learning models for classification and regression problems
Clean and preprocess raw data using Python
Create visualizations to communicate insights
Work with SQL databases to extract and manipulate data
Document findings and present results to the team

Required Skills:

Python programming
NumPy and Pandas
Exploratory Data Analysis
Linear Regression
Logistic Regression
Data Visualization using Matplotlib and Seaborn
Basic SQL
Jupyter Notebook

Good to Have:

Scikit-learn
Git and GitHub
Power BI or Excel

Role: Data Science Intern
Duration: 3-6 months
Stipend: 8,000 - 15,000/month
Education: B.Tech CSE or related field currently pursuing
Location: Remote / Hybrid

Use this as your jd_text and test against your resume. This JD should give you a high match score since your resume has most of these skills.
Tell me what score you get.
'''

score=compute_match_score(real_jd,my_resume)
miss=missing_skills(real_jd,my_resume)

print(score)
print(miss)