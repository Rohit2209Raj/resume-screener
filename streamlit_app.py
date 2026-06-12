import threading
import uvicorn
from main import app as fastapi_app
import streamlit as st
import requests

# Start FastAPI in background thread
def run_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

thread = threading.Thread(target=run_fastapi, daemon=True)
thread.start()

# Page config
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="centered"
)

# title
st.title("AI Resume Analyser")
st.write("Upload your resume and paste the job description to see how well you match")

st.divider()

col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

with col2:
    st.write("")

jd_text = st.text_area("Paste Job Description here", height=200)

st.divider()

if st.button("Analyze"):
    if not resume:
        st.error("Upload your resume file")
    elif not jd_text.strip():
        st.error("Paste the job description")
    else:
        with st.spinner("Analyzing your resume..."):
            response = requests.post(
                "http://localhost:8000/match",
                data={"jd_text": jd_text},
                files={"resume": resume}
            )
            result = response.json()

        st.subheader("Results")

        score = float(result['match_score'])

        if score >= 70:
            st.success(f"✅ Match Score: {score}%")
        elif score >= 50:
            st.warning(f"⚠️ Match Score: {score}%")
        else:
            st.error(f"❌ Match Score: {score}%")

        st.subheader("Missing Keywords")

        missing = result["missing_skills"]
        if missing:
            for skill in missing:
                st.write(f"• {skill}")
        else:
            st.write("✅ No missing keywords found!")