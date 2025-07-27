# Approach Explanation – Challenge 1B: Persona-Driven Document Intelligence

## Problem Statement

The task involves extracting the most relevant content from a collection of PDFs using two inputs:
- A specific **persona**
- A **job-to-be-done** linked to that persona

The system must extract, prioritize, and return a ranked list of content from the documents that best fulfills the intent of the persona.

---

## Methodology

### 1. **Input Parsing**
The system begins by loading the `challenge1b_input.json` file. This file contains:
- A textual **persona description**
- A **job-to-be-done** prompt

We concatenate both fields and treat them as a query to match relevant document sections.

---

### 2. **Document Preprocessing**
Each PDF from the collection is:
- Loaded using `PyMuPDF` (fitz)
- Split into individual pages
- Each page's text is cleaned and stored for scoring

---

### 3. **Chunking and Scoring**
We break the text into semantic chunks (paragraphs or sentences), then evaluate each chunk’s relevance to the persona's job using:
- **TF-IDF** vector similarity between chunk and the combined persona+job string
- Optional enhancements:
  - Keyword matching
  - Sentence embeddings using lightweight NLP models (`SentenceTransformers`)

Each chunk is assigned a **relevance score**.

---

### 4. **Ranking**
Chunks are ranked by score. The top N results are selected with:
- Page number
- Extracted content
- Relevance score
- Source PDF name

This data is saved into `challenge1b_output.json`.

---

## Output Schema

The output JSON contains:
- Metadata (persona, job, timestamp, input files)
- A ranked list of relevant sections

Each result includes:
- `content`: Text chunk
- `score`: Relevance score
- `page_number`: Source location
- `source_pdf`: File name

---

## Runtime Constraints Handling

- The code runs **fully offline** and processes PDFs in ≤ 60 seconds (tested on 5 PDFs).
- It uses only **CPU-compatible** libraries.
- No model larger than 200MB is used.
- All libraries are open-source.

---

## Tools and Libraries

- `PyMuPDF` – PDF reading and page-wise text extraction
- `scikit-learn` – TF-IDF vectorizer and cosine similarity
- `NLTK` – Tokenization (optional)
- `datetime`, `json`, `os` – Utilities for handling files

---

## Future Improvements

- Integrate sentence embeddings or BERT for better semantic relevance
- Add domain-specific rules for different persona types
- Allow summarization for long answers

---

## Conclusion

This approach ensures a light, CPU-only, offline-compatible pipeline that tailors document analysis to persona needs, while staying within Adobe's challenge constraints.
