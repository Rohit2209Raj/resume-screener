import streamlit as st
import requests

# Page config — add this at the very top
st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="centered"
)

# title
st.title("AI resume analyser")

st.write("Upload your resume and paste the job description to see how well you match")

# Add a divider
st.divider()

# Two columns for inputs
col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

with col2:
    st.write("")  # spacing

jd_text = st.text_area("Paste Job Description here", height=200)

st.divider()


# checking if both resume and jd_text exist
if st.button("Analyze"):
    if not resume:
        st.error("Upload your resume file")
    if not jd_text.strip():
        st.error("Paste the job description")
    else:
        with st.spinner("Analyzing your resume..."):
            st.success("Both inputs received. Ready to analyze.")
            response=requests.post(
                "http://localhost:8000/match",
                data={"jd_text":jd_text},
                files={"resume":resume}
            )
            result=response.json()

            st.subheader("Results..")

            # Based on score output the result

            score = float(result['match_score'])

            if score >= 70:
                st.success(f"✅ Match Score: {score}%")
            elif score >= 50:
                st.warning(f"⚠️ Match Score: {score}%")
            else:
                st.error(f"❌ Match Score: {score}%")
            
            st.subheader("Missing_keywords")

            # output the missing keywords if any

            missing = result["Missing_keywords"]
            if missing:
                for skill in missing:
                    st.write(f"• {skill}")
            else:
                st.write("✅ No missing keywords found!")


