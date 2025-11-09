# Google Docs Integration for Living Writeups

**Enable collaborative learning with inline comments and questions**

---

## Why Google Docs?

- **Inline comments**: Ask questions directly on specific sections
- **Suggestions mode**: Propose improvements to writeups
- **Real-time updates**: Changes sync to GitHub Pages automatically
- **Collaborative**: Share with mentors, study partners
- **Living document**: Evolves as you learn

---

## Quick Setup (5 minutes per pattern)

### Step 1: Create Google Doc from Markdown

**Option A: Manual (Recommended)**
1. Open [Google Docs](https://docs.google.com)
2. Create new document: "DSA Mastery - Two Pointers Pattern"
3. Copy content from `docs/patterns/01-two-pointers.md`
4. Paste into Google Doc
5. Format headings (Ctrl+Alt+1 for H1, Ctrl+Alt+2 for H2, etc.)
6. Format code blocks (use `Consolas` or `Courier New` font, light gray background)

**Option B: Use Converter (Faster)**
1. Install [Docs Markdown](https://workspace.google.com/marketplace/app/docs_markdown/340130888934)
2. Open new Google Doc
3. Extensions → Docs Markdown → Import Markdown
4. Paste markdown content
5. Click "Import"

### Step 2: Publish to Web

1. In your Google Doc, click **File → Share → Publish to web**
2. Choose "**Embed**" tab
3. Click "**Publish**"
4. Copy the `<iframe>` code (looks like):
   ```html
   <iframe src="https://docs.google.com/document/d/e/LONG_ID_HERE/pub?embedded=true"></iframe>
   ```
5. Extract the URL from the iframe (the part in `src="..."`)

### Step 3: Update GitHub Pages

Edit `docs/patterns/01-two-pointers.md`:

```markdown
---
layout: default
title: Two Pointers Pattern
---

# Two Pointers Pattern - Living Document

**[Open in Google Docs to Comment →](YOUR_PUBLISHED_URL_HERE)**

<iframe src="YOUR_PUBLISHED_URL_HERE" width="100%" height="800px" frameborder="0"></iframe>

---

## Offline Version

If the embedded doc doesn't load, here's the static version:

[Rest of current markdown content...]
```

### Step 4: Share for Editing (Optional)

If you want others to edit/comment:
1. Click **Share** button (top right)
2. Change to "**Anyone with the link can comment**"
3. Or add specific people as "**Editor**" or "**Commenter**"

---

## Template for All Patterns

Use this structure for each pattern:

```markdown
---
layout: default
title: [Pattern Name]
---

# [Pattern Name] - Living Document

**[Open in Google Docs to Comment →](GOOGLE_DOC_URL)**

<iframe src="GOOGLE_DOC_URL?embedded=true" width="100%" height="800px" frameborder="0"></iframe>

---

## Offline Version
[Markdown fallback content]
```

---

## Workflow with Comments

### As You Learn:
1. Read the writeup in Google Docs
2. Highlight confusing parts
3. Add comment: "Why does this work?"
4. Tag yourself or collaborators
5. Discuss in comment thread

### After Solving Problems:
1. Add your insights to the doc
2. Use "Suggesting" mode (not "Editing")
3. Add examples that helped you
4. Share edge cases you discovered

### PR Reviews:
1. Reference Google Doc sections in PR
2. Ask reviewer to comment on specific parts
3. Update doc based on feedback

---

## Auto-Sync GitHub Pages (Advanced)

**Make Google Docs the single source of truth:**

### Option 1: Embedded Only (Simple)
- Just embed the iframe (already covered above)
- Pros: No syncing needed
- Cons: Comments not visible on GitHub Pages

### Option 2: Export to Markdown (Automated)
```bash
# Install clasp (Google Apps Script CLI)
npm install -g @google/clasp

# Create Apps Script to auto-export
# (See scripts/gdocs_sync/ for automation)
```

This is more complex - stick with Option 1 (embedded) for now.

---

## Example: Two Pointers Pattern

Here's what your `docs/patterns/01-two-pointers.md` should look like:

```markdown
---
layout: default
title: Two Pointers Pattern
---

# Two Pointers Pattern

**[📝 Open in Google Docs to Comment](https://docs.google.com/document/d/YOUR_ID/edit)**

<iframe
  src="https://docs.google.com/document/d/e/YOUR_ID/pub?embedded=true"
  width="100%"
  height="1200px"
  style="border: 1px solid #ccc; border-radius: 4px;"
></iframe>

---

## Quick Links
- [Problems](../../src/patterns/two_pointers/)
- [Visualizations](../../visualizations/two_pointers/)
- [Progress](../../progress.md#two-pointers)

---

<details>
<summary>Offline Markdown Version (click to expand)</summary>

[Current markdown content as fallback]

</details>
```

---

## Best Practices

### Document Naming:
- `DSA Mastery - [Pattern Name]`
- Example: `DSA Mastery - Two Pointers Pattern`

### Folder Organization:
Create Google Drive folder:
```
DSA Mastery/
├── Patterns/
│   ├── 01-Two-Pointers.gdoc
│   ├── 02-Sliding-Window.gdoc
│   └── ...
├── Solutions/
│   └── [problem-specific notes]
└── Resources/
    └── [algorithm books, etc.]
```

### Comment Etiquette:
- **Question**: Highlight text, add `?` in comment
- **Insight**: Add suggestion with "💡" prefix
- **Clarification needed**: Tag with "TODO:"
- **Resolved**: Click "Resolve" when answered

---

## All Patterns Checklist

- [ ] Two Pointers → Google Doc created + published + embedded
- [ ] Sliding Window → Google Doc created + published + embedded
- [ ] Fast/Slow Pointers → Google Doc created + published + embedded
- [ ] Merge Intervals → Google Doc created + published + embedded
- [ ] Cyclic Sort → Google Doc created + published + embedded
- [ ] In-place Reversal (LinkedList) → Google Doc created + published + embedded
- [ ] Tree BFS → Google Doc created + published + embedded
- [ ] Tree DFS → Google Doc created + published + embedded
- [ ] Two Heaps → Google Doc created + published + embedded
- [ ] Subsets (Backtracking) → Google Doc created + published + embedded
- [ ] Modified Binary Search → Google Doc created + published + embedded
- [ ] Top K Elements → Google Doc created + published + embedded
- [ ] Dynamic Programming → Google Doc created + published + embedded

---

## Troubleshooting

### Iframe not showing:
- Check URL is published (not just shared)
- Use "Publish to web" not just "Get link"
- Make sure URL includes `?embedded=true`

### Can't comment:
- Open the "Edit" link (not embedded version)
- Check share settings allow commenting

### Doc too long:
- Split into multiple docs (Basics, Advanced, Problems)
- Link between them

---

## Next Steps

1. **Create your first Google Doc** for Two Pointers pattern
2. **Publish it** and get the embed URL
3. **Update** `docs/patterns/01-two-pointers.md` with iframe
4. **Commit and push** to GitHub
5. **Check GitHub Pages** - should see embedded doc
6. **Test commenting** - add a question to verify it works

---

**Living documents unlock collaborative learning. Your writeups evolve as you grow.** 📚✨
