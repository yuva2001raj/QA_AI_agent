from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

def index_docs(pages):
    texts = []
    urls = []
    for url, content in pages.items():
        for chunk in content.split("\n\n"):
            chunk = chunk.strip()
            if len(chunk) > 50:
                texts.append(chunk)
                urls.append(url)

    embeddings = model.encode(texts)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    return index, texts, urls
