
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

"""
Created embeding 
"""
def create_embeding(data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(data).tolist()
    return embedding


"""
Updating vector database with embedings of travel_knowldge_base
"""
def update_vector_db_with_embeding(rows):
    ids = [row[0] for row in rows]
    embeddings = np.array([eval(row[1]) for row in rows]).astype('float32')
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)