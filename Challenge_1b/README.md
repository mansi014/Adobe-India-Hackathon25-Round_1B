# Challenge 1B: Connecting the Dots (Persona-Driven Document Intelligence)

## Overview

This repository contains the solution to **Challenge 1B** of the **Adobe India Hackathon 2025**. The task is to build a content extraction system that uses *persona information* and *job-to-be-done context* to analyze a collection of PDFs and extract relevant sections, ranking them by relevance.

## Objective

- Use structured inputs (persona + job description) to personalize content analysis.
- Extract, score, and rank relevant content from a collection of unstructured PDF documents.
- Return a structured output in JSON format that summarizes the most useful PDF chunks for the given input.

---

## How It Works

1. **Input:** A `challenge1b_input.json` file with persona and job-to-be-done.
2. **Processing:**
   - PDFs are tokenized into semantic chunks.
   - Each chunk is scored based on relevance using heuristics or NLP techniques.
3. **Output:** A ranked list of text chunks (with source, page number, and score) in `challenge1b_output.json`.

---

## Project Structure

```
Challenge_1b/
├── Collection_1/                            # Financial Reports
│   ├── PDFs/
│   │   ├── report_2021.pdf
│   │   ├── report_2022.pdf
│   │   └── report_2023.pdf
│   ├── challenge1b_input.json              # Input: Persona + Job-to-be-Done
│   └── challenge1b_output.json             # Output: Extracted Sections + Metadata

├── Collection_2/                            # Product Manuals
│   ├── PDFs/
│   │   ├── product_guide_A.pdf
│   │   └── product_guide_B.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json

├── Collection_3/                            # Educational Content
│   ├── PDFs/
│   │   ├── organic_chemistry_chapter1.pdf
│   │   ├── organic_chemistry_chapter2.pdf
│   │   └── organic_chemistry_chapter3.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json

├── approach_explanation.md                  # 300–500 words: how the system works
├── process_documents.py                     # Code that processes all collections
└── README.md                                # Full documentation, commands, instructions
```

---

## Input Format (`challenge1b_input.json`)

```json
{
  "persona": "An undergraduate chemistry student preparing for exams",
  "job_to_be_done": "Identify key concepts and mechanisms related to reaction kinetics from textbooks"
}
```

---

## Output Format (`challenge1b_output.json`)

```json
{
  "results": [
    {
      "content": "The rate law for SN1 reactions is independent of nucleophile concentration...",
      "score": 0.91,
      "page_number": 4,
      "source_pdf": "organic_chemistry_chapter2.pdf"
    },
    {
      "content": "Catalysis plays a key role in reducing activation energy for reaction pathways...",
      "score": 0.88,
      "page_number": 6,
      "source_pdf": "organic_chemistry_chapter3.pdf"
    }
  ]
}
```

---

## Docker Instructions

Build the Docker image:

```bash
docker build --platform linux/amd64 -t challenge1b-processor .
```

Run the processor:

```bash
docker run --rm \
  -v $(pwd)/Collection_3/PDFs:/app/input:ro \
  -v $(pwd)/Collection_3:/app/config \
  -v $(pwd)/Collection_3:/app/output \
  challenge1b-processor
```

---

## Constraints

- Model size must not exceed 1GB
- Process should complete within 60 seconds for 3–5 PDFs
- No internet access allowed at runtime
- Must run on AMD64 architecture (CPU only)
- Libraries and tools must be open source

---

## Validation Checklist

- [x] Input JSON is parsed correctly
- [x] PDFs are chunked and scored
- [x] Output is ranked and matches schema
- [x] Processing works offline and within resource limits
- [x] Code containerized via Docker

---

## Acknowledgements

- Open-source libraries: `PyMuPDF`, `NLTK`, `scikit-learn`, `transformers (if applicable)`
- Dataset PDF content used for demonstration purposes only

---

## Contact

For queries or issues, please raise an issue on this GitHub repository.
