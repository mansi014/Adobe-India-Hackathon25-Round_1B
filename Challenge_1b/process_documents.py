import os
import fitz  # PyMuPDF
import json
import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if text.strip():
            chunks.append({
                "page_number": page_num + 1,
                "content": text.strip()
            })
    return chunks

def score_chunks(chunks, query):
    texts = [chunk["content"] for chunk in chunks]
    vectorizer = TfidfVectorizer().fit([query] + texts)
    vectors = vectorizer.transform([query] + texts)
    query_vec = vectors[0]
    chunk_vecs = vectors[1:]
    similarities = cosine_similarity(query_vec, chunk_vecs).flatten()
    
    for idx, score in enumerate(similarities):
        chunks[idx]["score"] = round(float(score), 4)
    return sorted(chunks, key=lambda x: x["score"], reverse=True)

def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_dir = os.path.join(collection_path, "PDFs")

    with open(input_path, 'r') as f:
        query_data = json.load(f)

    query = query_data["persona"] + " " + query_data["job_to_be_done"]
    results = []
    for pdf_file in os.listdir(pdf_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, pdf_file)
            chunks = extract_text_chunks(pdf_path)
            scored = score_chunks(chunks, query)
            top_chunks = scored[:3]  # Top 3 per PDF

            for item in top_chunks:
                results.append({
                    "content": item["content"][:500],  # truncate for brevity
                    "score": item["score"],
                    "page_number": item["page_number"],
                    "source_pdf": pdf_file
                })

    output = {
        "persona": query_data["persona"],
        "job_to_be_done": query_data["job_to_be_done"],
        "timestamp": str(datetime.datetime.now()),
        "results": results
    }

    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)

if __name__ == "__main__":
    for folder in ["Collection_1", "Collection_2", "Collection_3"]:
        if os.path.isdir(folder):
            print(f"Processing {folder}...")
            process_collection(folder)
