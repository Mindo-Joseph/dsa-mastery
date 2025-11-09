# Gemini File Search Integration

This document explains how to use Gemini API's File Search as a replacement for NotebookLM in your DSA mastery journey.

## What is Gemini File Search?

Gemini File Search is a **fully managed RAG (Retrieval Augmented Generation) system** built directly into the Gemini API. It automatically:
- Uploads and stores your documents
- Chunks them intelligently
- Creates embeddings for semantic search
- Retrieves relevant context for your queries
- Provides cited, grounded responses

## Advantages over NotebookLM

| Feature | NotebookLM | Gemini File Search |
|---------|------------|-------------------|
| **Integration** | Browser-based, manual | Programmatic API |
| **Automation** | Manual queries | Scriptable workflows |
| **Context** | 50 sources max | Unlimited (1GB free) |
| **Citations** | Basic | Detailed grounding metadata |
| **Cost** | Free | $0.15/1M tokens (indexing only) |
| **Storage** | Not programmable | Persistent, queryable |

## Setup (One-Time)

### 1. Get API Key

Visit [Google AI Studio](https://aistudio.google.com/apikey) and create an API key.

### 2. Set Environment Variable

```bash
export GEMINI_API_KEY='your-api-key-here'

# Make it permanent
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 3. Install Dependencies

```bash
pip3 install --user google-genai
```

### 4. Initialize Store

```bash
cd ~/dsa-mastery
./scripts/setup_gemini_search.sh
```

This creates a persistent file search store called `dsa-mastery-store`.

### 5. Upload Your Content

```bash
# Upload all markdown, text, and Rust files
python3 scripts/gemini_file_search.py upload --dir .
```

This will index:
- All writeups (`writeups/*.md`)
- Pattern documentation (`patterns/*.md`)
- Notes (`notes/*.md`)
- Implementation code (`src/**/*.rs`)
- All documentation files

Files are automatically tagged with metadata based on their location.

## Daily Usage

### Quick Queries

```bash
# Simple question
./scripts/quick_query.sh "Explain the two pointers pattern"

# Get problem examples
./scripts/quick_query.sh "Show me sliding window problems"

# Theory questions
./scripts/quick_query.sh "What's the time complexity of quicksort?"
```

### Advanced Queries

```bash
# Filter by category
python3 scripts/gemini_file_search.py query \
  --question "Show me tree traversal examples" \
  --filter "category=patterns"

# Use different model
python3 scripts/gemini_file_search.py query \
  --question "Explain dynamic programming" \
  --model "gemini-2.5-pro"
```

### Python Integration

```python
from scripts.gemini_file_search import GeminiFileSearch

# Initialize
fs = GeminiFileSearch()
fs.get_or_create_store()

# Query
result = fs.query("What are the key insights for two sum problems?")
print(result['answer'])

# With metadata filter
result = fs.query(
    "Show binary search problems",
    metadata_filter="category=patterns"
)
```

## Workflow Integration

Replace the NotebookLM step in your workflow:

### Old Workflow
```
Query NotebookLM (manual) → Solve → PR → Review → Merge
```

### New Workflow
```bash
# 1. Query for context
./scripts/quick_query.sh "Explain sliding window technique"

# 2. Get specific problem guidance
./scripts/quick_query.sh "How to solve max subarray sum?"

# 3. Solve problem
# ... write your solution ...

# 4. Verify approach
./scripts/quick_query.sh "Is this the optimal approach for max subarray?"

# 5. Continue with PR workflow
git checkout -b pattern/sliding-window/problem-003
cargo test
# ... etc
```

## Metadata Filtering

Files are automatically tagged with metadata:

| Metadata Key | Values | Use Case |
|-------------|--------|----------|
| `category` | `pattern`, `notes`, `writeup`, `implementation`, `documentation` | Filter by content type |
| `filetype` | `rust`, `markdown`, `text` | Filter by file format |

**Examples:**

```bash
# Only search pattern documentation
python3 scripts/gemini_file_search.py query \
  --question "Two pointers examples" \
  --filter "category=patterns"

# Only search Rust implementations
python3 scripts/gemini_file_search.py query \
  --question "Show me working code" \
  --filter "filetype=rust"
```

## Updating the Index

When you add new content (solutions, notes, writeups):

```bash
# Re-upload everything (incremental, won't duplicate)
python3 scripts/gemini_file_search.py upload --dir .

# Or upload specific directory
python3 scripts/gemini_file_search.py upload --dir writeups
```

## Management Commands

```bash
# List all stores
python3 scripts/gemini_file_search.py list

# Delete store (if you want to start fresh)
python3 scripts/gemini_file_search.py delete
```

## Pricing

- **Indexing**: $0.15 per 1 million tokens (one-time when uploading)
- **Storage**: Free (1GB included, more with paid tiers)
- **Queries**: Standard Gemini API rates for tokens retrieved
- **Embedding generation at query time**: Free

**Estimated costs for DSA mastery:**
- Initial upload (~500 documents): ~$0.05
- Weekly updates (50 new files): ~$0.01
- Queries: ~$0.10/month (at 100 queries)

**Total: < $1/month for complete system**

## Citations and Grounding

Every response includes citation metadata showing which documents were used:

```python
result = fs.query("Explain binary search")

# Access grounding metadata
print(result['grounding_metadata'])

# Citations are automatically included
for citation in result['citations']:
    print(f"Source: {citation['source']}")
```

This ensures you can:
- Verify information accuracy
- Go back to source documents
- Track which materials are most useful

## Troubleshooting

### API Key Issues

```bash
# Check if set
echo $GEMINI_API_KEY

# Re-set if needed
export GEMINI_API_KEY='your-key'
```

### Import Errors

```bash
# Reinstall package
pip3 install --upgrade --user google-genai
```

### Upload Failures

Files over 100MB are not supported. For large files:
1. Split into smaller chunks
2. Upload separately
3. Or exclude from indexing

### Query Not Finding Content

```bash
# Re-upload with verbose output
python3 scripts/gemini_file_search.py upload --dir .

# Check store exists
python3 scripts/gemini_file_search.py list
```

## Best Practices

1. **Upload early**: Index your content immediately after setup
2. **Update regularly**: Re-run upload after adding significant content
3. **Use filters**: Narrow searches with metadata filters for faster, more relevant results
4. **Cite sources**: Always check grounding metadata to verify information
5. **Start broad**: Ask general questions first, then drill down
6. **Iterate queries**: Refine your questions based on initial responses

## Example Session

```bash
# Setup (one time)
./scripts/setup_gemini_search.sh
python3 scripts/gemini_file_search.py upload --dir .

# Daily use
./scripts/quick_query.sh "What's the two pointers pattern?"
# ... read response ...

./scripts/quick_query.sh "Show me code examples of two pointers"
# ... get Rust implementations ...

./scripts/quick_query.sh "Common mistakes with two pointers?"
# ... learn pitfalls ...

# Now solve your problem with full context!
```

## Integration with Claude

When working with Claude Code, you can reference File Search results:

```
"I queried my File Search and got this about sliding window:
[paste result]

Now help me solve this problem using that pattern..."
```

Or ask Claude to query for you:

```
"Run a File Search query for 'binary search tree traversal'
and use the results to guide my implementation"
```

## Resources

- [Gemini File Search Docs](https://ai.google.dev/gemini-api/docs/file-search)
- [Google AI Studio](https://aistudio.google.com/)
- [Pricing Details](https://ai.google.dev/pricing)

---

**You now have a programmatic, citation-backed knowledge base for your entire DSA journey.**

Query it before solving problems, during debugging, and when reviewing patterns. It's like having a senior engineer's library instantly searchable.

**Let's go!** 🚀
