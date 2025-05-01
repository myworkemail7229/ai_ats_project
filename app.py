import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from ranker import rank_resumes

st.set_page_config(page_title="AI ATS", layout="wide")
st.title("AI ATS: Resume Ranking Based on Job Description")

job_desc = st.text_area("Paste Job Description", height=200)

uploaded_files = st.file_uploader("Upload Resumes (PDF or DOCX)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Rank Resumes") and uploaded_files and job_desc:
    resumes = []
    for file in uploaded_files:
        if file.name.endswith(".pdf"):
            text = extract_text_from_pdf(file)
        elif file.name.endswith(".docx"):
            text = extract_text_from_docx(file)
        else:
            continue
        resumes.append(text)

    results = rank_resumes(job_desc, resumes)

    st.subheader("Ranked Resumes:")
    for idx, (text, score) in enumerate(results, 1):
        st.markdown(f"### Rank {idx} — Score: {score:.4f}")
        st.write(text[:500] + "...")
