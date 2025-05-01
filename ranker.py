from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_resumes(job_description, resumes):
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embeddings = model.encode(resumes, convert_to_tensor=True)
    similarities = util.cos_sim(jd_embedding, resume_embeddings)[0]
    return sorted(zip(resumes, similarities.tolist()), key=lambda x: x[1], reverse=True)
