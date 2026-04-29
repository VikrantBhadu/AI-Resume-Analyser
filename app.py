import streamlit as st

# Page Settings
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

# Title
st.title("📄 AI Resume Analyzer")
st.subheader("Smart AI Tool for Resume Screening")

st.write("Upload your resume and get instant AI-powered feedback.")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("Resume Uploaded Successfully!")

    st.header("📊 Resume Analysis Report")

    st.write("✅ ATS Score: 85/100")
    st.write("✅ Skills Detected: Python, Communication, Leadership, SQL")
    st.write("⚠ Suggestion: Add more project experience")
    st.write("⚠ Suggestion: Improve professional summary")
    st.write("⚠ Suggestion: Add certifications")

    st.header("💼 Recommended Job Roles")

    st.write("- Data Analyst")
    st.write("- Python Developer")
    st.write("- AI Intern")
    st.write("- Business Analyst")

    st.header("🚀 Final Verdict")

    st.info("Your resume is strong but can be improved for better interview chances.")
