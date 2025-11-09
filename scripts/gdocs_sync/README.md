# Google Docs Integration - Simple & Automated

**Edit in Google Docs, sync to GitHub automatically**

---

## 🎯 Philosophy

**Google Docs = Source of Truth**

- You edit Google Docs (rich editing, comments, collaboration)
- Script pulls changes to markdown
- Markdown commits to GitHub
- GitHub Pages shows both embedded doc + markdown fallback

**Benefits:**
- Edit anywhere (phone, tablet, browser)
- Inline comments on your own notes
- Share with mentors for feedback
- Rich formatting (tables, images, links)
- No manual markdown syntax

---

## ⚡ Quick Start (10 minutes)

### Step 1: Install Dependencies

```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Step 2: Get Google API Credentials

1. **Go to:** https://console.cloud.google.com/
2. **Create project:** "DSA-Mastery-Docs"
3. **Enable APIs:**
   - Search "Google Docs API" → Enable
   - Search "Google Drive API" → Enable
4. **Create credentials:**
   - APIs & Services → Credentials
   - Create Credentials → OAuth client ID
   - Application type: **Desktop app**
   - Download JSON
5. **Save credentials:**
   ```bash
   mv ~/Downloads/client_secret_*.json ~/dsa-mastery/scripts/gdocs_sync/credentials.json
   ```

### Step 3: Create Initial Google Docs

```bash
cd ~/dsa-mastery
python3 scripts/gdocs_sync/setup_initial_docs.py
```

**What happens:**
- Browser opens for authentication
- Creates Google Doc for each writeup
- Prints URLs for all docs
- Saves URLs to `GOOGLE_DOCS_LINKS.md`

**Output:**
```
✨ Created 1 Google Docs!

📋 YOUR DOCUMENTS:
════════════════════════════════════════════════════════════

📄 Two Pointers Pattern - First Principles to Mastery
   https://docs.google.com/document/d/ABC123.../edit

🎯 NEXT STEPS:
Bookmark these URLs and edit them as you learn!
```

### Step 4: Edit Your Docs

1. Open the URLs (saved in `GOOGLE_DOCS_LINKS.md`)
2. Edit in Google Docs:
   - Add your insights
   - Reorganize sections
   - Add examples that helped you
   - Comment on confusing parts
3. Save automatically (Google Docs auto-saves)

### Step 5: Pull Changes Back

```bash
# Pull all docs
python3 scripts/gdocs_sync/pull_from_docs.py

# Or pull specific doc
python3 scripts/gdocs_sync/pull_from_docs.py <DOC_ID>
```

**Output:**
```
📥 Pull Updates from Google Docs
════════════════════════════════════════════════════════════

🔐 Authenticating...
✅ Authenticated

📚 Pulling 1 documents...

────────────────────────────────────────────────────────────
📥 Pulling: Two Pointers Pattern - First Principles to Mastery
   Last modified: 2025-11-09T14:32:15.000Z
✅ Updated: /home/joemindo/dsa-mastery/writeups/01_two_pointers.md
✅ Updated GitHub Pages: /home/joemindo/dsa-mastery/docs/patterns/01_two_pointers.md

════════════════════════════════════════════════════════════
✨ Successfully pulled 1/1 documents

Next steps:
  git add writeups/ docs/
  git commit -m 'Synced from Google Docs'
  git push
```

### Step 6: Commit and Push

```bash
git add writeups/ docs/
git commit -m "Updated from Google Docs"
git push
```

**Done!** Changes are now on GitHub Pages.

---

## 📅 Daily Workflow

### 1. Learn & Edit

```
Open Google Doc → Add insights as you learn → Auto-saves
```

### 2. Sync Periodically

```bash
# After each learning session or daily
python3 scripts/gdocs_sync/pull_from_docs.py

# Commit
git add .
git commit -m "Synced: added insights on two pointers"
git push
```

**That's it!** 2 commands to sync.

---

## 🔄 Complete Example

```bash
# Morning: Start learning
# Open: https://docs.google.com/document/d/YOUR_DOC_ID/edit

# In Google Docs, add notes:
# "### My Insight
#  I realized two pointers works because..."

# After learning session (evening):
cd ~/dsa-mastery
python3 scripts/gdocs_sync/pull_from_docs.py

# Commit
git add .
git commit -m "Added two pointers insights"
git push

# Check GitHub Pages - sees your updates!
# https://YOUR_USERNAME.github.io/dsa-mastery/patterns/01-two-pointers
```

---

## 📂 How It Works

### File Flow

```
Google Docs (you edit)
    ↓
[pull_from_docs.py]
    ↓
writeups/01_two_pointers.md (markdown)
    ↓
docs/patterns/01-two-pointers.md (with embedded doc)
    ↓
GitHub Pages (readers see embedded + fallback)
```

### What Gets Updated

When you run `pull_from_docs.py`:

1. **Exports Google Doc** as plain text
2. **Preserves formatting** (headings, bold, italic, code)
3. **Updates writeups/**.md (pure markdown)
4. **Updates docs/**.md (markdown + embedded iframe)
5. **Saves mapping** (doc ID → file path)

---

## 🎨 GitHub Pages Result

Your published page shows:

```markdown
# Two Pointers Pattern

[📝 Edit in Google Docs] ← Click to edit

┌─────────────────────────────────────┐
│                                     │
│  [Google Doc Embedded]              │
│  (live, always up to date)          │
│                                     │
└─────────────────────────────────────┘

## Markdown Version
[Full markdown below as fallback]
```

**Readers can:**
- Read embedded doc
- Click to open in Google Docs
- See markdown fallback if iframe blocked

---

## 🛠️ Scripts Reference

### `setup_initial_docs.py`
**Run once** - Creates Google Docs from markdown

```bash
python3 scripts/gdocs_sync/setup_initial_docs.py
```

Creates:
- Google Doc for each `writeups/*.md`
- Saves doc IDs to `doc_mappings.json`
- Prints URLs
- Creates `GOOGLE_DOCS_LINKS.md`

### `pull_from_docs.py`
**Run often** - Pulls edits from Google Docs

```bash
# Pull all docs
python3 scripts/gdocs_sync/pull_from_docs.py

# Pull specific doc
python3 scripts/gdocs_sync/pull_from_docs.py 1a2b3c4d5e6f7g8h9i0j
```

Updates:
- `writeups/*.md` (markdown)
- `docs/patterns/*.md` (GitHub Pages)

---

## 🔒 Security

### Credentials (Never Commit!)

`.gitignore` should contain:
```
scripts/gdocs_sync/credentials.json
scripts/gdocs_sync/token.pickle
```

### Permissions

OAuth requests:
- Read/write Google Docs you created
- Manage their Drive permissions

Does NOT access:
- Other people's docs
- Your email, calendar, etc.

### Revoke Access

https://myaccount.google.com/permissions
- Find "DSA-Mastery-Docs"
- Remove access
- Delete `token.pickle` to re-auth

---

## 🐛 Troubleshooting

### "credentials.json not found"

```bash
# Download from Google Cloud Console
# Save to:
~/dsa-mastery/scripts/gdocs_sync/credentials.json
```

### "Authentication failed"

```bash
# Remove token and re-authenticate
rm scripts/gdocs_sync/token.pickle
python3 scripts/gdocs_sync/setup_initial_docs.py
```

### "No documents tracked yet"

```bash
# Run initial setup first
python3 scripts/gdocs_sync/setup_initial_docs.py
```

### "Formatting looks wrong"

The markdown converter is simplified. For complex formatting:
- Use Google Docs built-in styles (Heading 1, 2, 3)
- Use Courier New for code
- Keep it simple - favor content over complex styling

### "Want to add new writeup"

```bash
# 1. Create markdown in writeups/
echo "# New Pattern" > writeups/03_new_pattern.md

# 2. Create Google Doc from it
python3 scripts/gdocs_sync/setup_initial_docs.py

# Or create manually and add to doc_mappings.json
```

---

## 💡 Tips

### Organize in Google Drive

Create folder structure:
```
Google Drive/
└── DSA Mastery/
    ├── 01-Two-Pointers
    ├── 02-Sliding-Window
    └── ...
```

Move docs to folders for easy access.

### Use Comments

Highlight confusing sections and add comments:
- "Why does this work?"
- "Need example here"
- "Remember to review"

### Share with Mentors

```
Share → Anyone with link can comment
```

Send link to mentors for feedback.

### Mobile Editing

Google Docs app lets you edit on phone:
- Add quick insights while commuting
- Review before interviews
- Sync when back at computer

---

## 🚀 Advanced

### Automated Sync (Cron)

```bash
# Add to crontab (sync every 4 hours)
0 */4 * * * cd ~/dsa-mastery && python3 scripts/gdocs_sync/pull_from_docs.py && git add . && git commit -m "Auto-sync from Google Docs" && git push

# Or use Git hook
```

### Watch for Changes (Live Sync)

Google Docs API doesn't support webhooks, but you can poll:

```bash
# Sync every 30 minutes while working
watch -n 1800 'cd ~/dsa-mastery && python3 scripts/gdocs_sync/pull_from_docs.py && git add . && git commit -m "Auto-sync" && git push'
```

---

## 📚 Files Created

After setup:

```
scripts/gdocs_sync/
├── README.md                  # This file
├── setup_initial_docs.py      # One-time: create Google Docs
├── pull_from_docs.py          # Regular: pull edits back
├── credentials.json           # Your OAuth creds (gitignored)
├── token.pickle               # Auth token (gitignored)
└── doc_mappings.json          # Markdown ↔ Doc ID map

GOOGLE_DOCS_LINKS.md           # Quick reference to all your docs
```

---

## ✨ Summary

**One-time setup:**
```bash
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib
# Get credentials from Google Cloud Console
python3 scripts/gdocs_sync/setup_initial_docs.py
```

**Daily workflow:**
```bash
# 1. Edit Google Docs as you learn
# 2. Sync back:
python3 scripts/gdocs_sync/pull_from_docs.py
git add .
git commit -m "Synced from Google Docs"
git push
```

**That's it!** Focus on learning, not file management.

---

**Questions? Add them as comments in your Google Docs!** 💬
