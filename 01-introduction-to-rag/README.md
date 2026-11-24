# Lesson 01 — Introduction to RAG

## Overview

This lesson introduces Retrieval-Augmented Generation (RAG) by implementing a basic end-to-end pipeline using Python and the Groq API, without relying on AI orchestration frameworks.

## Learning Objectives

- Understand the fundamentals of RAG.
- Implement keyword-based document retrieval.
- Construct context-aware prompts.
- Integrate an LLM for answer generation.
- Understand the limitations of lexical search.

## Architecture

User Query → Retrieval → Augmentation → Generation → Final Answer

## Implementation

| Function | Responsibility |
|---|---|
| `tokenize()` | Normalize text and extract unique words |
| `retrieve()` | Rank documents using keyword overlap |
| `augment()` | Construct a prompt with retrieved context |
| `generate()` | Generate an answer using an LLM |
| `rag()` | Orchestrate the complete pipeline |

## Getting Started

From the repository root, install the dependencies:

`pip install -r 01-introduction-to-rag/requirements.txt`

Create a `.env` file using `.env.example` as a reference and configure your Groq API key.

Run the application:

`python 01-introduction-to-rag/main.py`

## Example

**Query:** Which tyres provide high grip?

**Expected answer:** Soft tyres provide high grip but generally degrade faster.

## Limitations

- Keyword matching does not understand semantic meaning.
- Common words can distort relevance scores.
- The knowledge base is static.
- Generated answers are not guaranteed to be factually correct.
- No vector database or document indexing is implemented.

## Practice Exercises

1. Expand the knowledge base with ten additional documents.
2. Remove common stop words before calculating relevance scores.
3. Experiment with different top-k values.
4. Display retrieved documents alongside generated answers.
5. Compare results for queries containing synonyms.

## Key Takeaway

RAG does not require retraining an LLM. It retrieves relevant external information and provides it to the model at inference time.

## Next Lesson

Lesson 02 — Text Embeddings: Representing the meaning of text using numerical vectors.