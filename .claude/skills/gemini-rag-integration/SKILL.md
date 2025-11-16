---
name: gemini-rag-integration
description: Query your curated DSA resources (CLRS, EPI, CTCI, LeetCode PDFs) using Gemini RAG for zero-hallucination theory and first principles explanations.
---

# Gemini RAG Integration

## Purpose

Query YOUR uploaded books and materials for theory, first principles, and problem sets. No hallucinations - only answers from your curated sources.

## When to Use

- "What does CLRS say about dynamic programming?"
- "Find similar problems to Two Sum"
- "Explain graph traversal from first principles"
- "Query my books about complexity analysis"

## Quick Commands

```bash
# Query all uploaded materials
gemini-query "explain two pointers from first principles"

# Query specific book
gemini-query "CLRS: dynamic programming optimal substructure"

# Find similar problems
gemini-query "problems similar to longest substring without repeating"
```

## Integration

This skill works with:
- `scripts/gemini_file_search.py` in your dsa-mastery
- Uploaded PDFs (CLRS, EPI, CTCI, LeetCode)
- GEMINI_API_KEY environment variable

## Workflow

1. Upload your PDFs once (already done in dsa-mastery)
2. Query anytime during problem-solving
3. Get theory-backed explanations
4. Zero hallucinations - only from your sources

---

**Query your knowledge base. Learn from YOUR books.**
