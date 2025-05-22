from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_question(question, index, texts, urls, top_k=3, threshold=0.3):
    query_vec = model.encode([question])
    D, I = index.search(np.array(query_vec), top_k)

    results = []
    for i in I[0]:
        if i < len(texts):
            results.append((texts[i], urls[i]))
    return results
