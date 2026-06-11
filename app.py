import streamlit as st
import requests

# title
st.title("AI resume analyser")

st.write("Upload your resume and paste the job description to see how well you match")


# file uploader
resume=st.file_uploader("Upload your resume in pdf",type='pdf')

# JD text area
jd_text = st.text_area("Paste the job description here", height=200)


# checking

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
            # st.write(result)

            st.subheader("Results..")

            score = float(result['match_score'])

            if score >= 70:
                st.success(f"Match Score: {score}%")
            elif score >= 50:
                st.warning(f"Match Score: {score}%")
            else:
                st.error(f"Match Score: {score}%")
            
            st.subheader("Missing_keywords")

            missing = result["Missing_keywords"]
            if missing:
                for skill in missing:
                    st.write(f"• {skill}")
            else:
                st.write("No missing keywords found!")


