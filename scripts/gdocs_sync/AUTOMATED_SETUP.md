# Automated Google Docs Sync - Complete Setup

**Fully automatic markdown → Google Docs → GitHub Pages pipeline**

---

## 🎯 What This Does

After setup, your workflow becomes:

```bash
# 1. Edit writeup
vim writeups/01_two_pointers.md

# 2. Commit
git add writeups/01_two_pointers.md
git commit -m "Updated two pointers writeup"

# 3. 🎉 AUTOMATIC:
#    ✅ Creates/updates Google Doc
#    ✅ Publishes to web
#    ✅ Updates GitHub Pages with embed
#    ✅ You can comment/edit in Google Docs
#    ✅ Changes visible on your website
```

**Zero manual steps after initial setup!**

---

## ⚡ Quick Setup (15 minutes, one-time only)

### Step 1: Install Python Libraries

```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Step 2: Get Google API Credentials

**A. Create Project**
1. Go to https://console.cloud.google.com/
2. Click "Select a project" → "New Project"
3. Name: `DSA-Mastery-Docs`
4. Click "Create"

**B. Enable APIs**
1. In search bar, type "Google Docs API"
2. Click "Enable"
3. Search "Google Drive API"
4. Click "Enable"

**C. Create OAuth Credentials**
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure consent screen:
   - User Type: External
   - App name: `DSA Mastery Sync`
   - Your email
   - Save
4. Application type: **Desktop app**
5. Name: `DSA Mastery Sync`
6. Click "Create"

**D. Download Credentials**
1. Click download icon (⬇️) next to your new OAuth client
2. File downloads as `client_secret_XXX.json`
3. Rename to `credentials.json`

**E. Move to Project**
```bash
mv ~/Downloads/credentials.json ~/dsa-mastery/scripts/gdocs_sync/credentials.json
```

### Step 3: First-Time Authentication

```bash
cd ~/dsa-mastery
python3 scripts/gdocs_sync/auto_sync.py
```

**What happens:**
1. Browser opens automatically
2. Login with your Google account
3. Grant permissions:
   - "See, edit, create, and delete your Google Docs"
   - "See, edit, create, and delete your Google Drive files"
4. Click "Allow"
5. Script creates Google Doc from your first writeup
6. Token saved for future use

**You'll see:**
```
🔄 DSA Mastery - Automatic Google Docs Sync
============================================================

🔐 Authenticating...
✅ Authenticated successfully

📚 Found 1 writeups to sync

────────────────────────────────────────────────────────────
📄 Creating new doc: Two Pointers Pattern - First Principles to Mastery
✅ Created Google Doc: Two Pointers Pattern - First Principles to Mastery
   ID: 1a2b3c4d5e6f7g8h9i0j
✅ Updated GitHub Pages: /home/joemindo/dsa-mastery/docs/patterns/01_two_pointers.md

✨ Synced 1 documents!

📋 Summary:

  • Two Pointers Pattern - First Principles to Mastery
    Edit: https://docs.google.com/document/d/1a2b3c4d5e6f7g8h9i0j/edit
```

### Step 4: Install Git Hooks (Automation!)

```bash
cd ~/dsa-mastery
./scripts/gdocs_sync/install_hooks.sh
```

**Installs:**
- Pre-commit hook: Auto-syncs before each commit
- Post-commit hook: Shows sync confirmation
- Manual sync script

### Step 5: Commit and Push

```bash
cd ~/dsa-mastery
git add .
git commit -m "Add automated Google Docs sync"
git push
```

**Done! ✨**

---

## 🔄 Daily Workflow (Fully Automated)

### Option A: Auto-sync on Commit (Recommended)

```bash
# 1. Edit writeup
vim writeups/01_two_pointers.md

# 2. Add insights, examples, clarifications
# ...

# 3. Commit
git add writeups/01_two_pointers.md
git commit -m "Added edge cases section"

# 🎉 Hook runs automatically:
# 📝 Detected writeup changes, syncing to Google Docs...
# 🔄 Syncing: writeups/01_two_pointers.md
# ✅ Updated Google Doc: 1a2b3c4d5e6f7g8h9i0j
# ✅ Updated GitHub Pages: docs/patterns/01_two_pointers.md
# ✅ Google Docs sync complete

# 4. Push
git push
```

**GitHub Pages updates in ~1 minute!**

### Option B: Manual Sync (When Needed)

```bash
# Sync all writeups
./scripts/gdocs_sync/sync_now.sh

# Sync specific file
./scripts/gdocs_sync/sync_now.sh writeups/01_two_pointers.md

# Then commit the updated docs/ files
git add docs/patterns/
git commit -m "Synced writeups to Google Docs"
git push
```

---

## 🎨 How It Works

### Architecture

```
writeups/01_two_pointers.md (Source of Truth)
        ↓
    [Git Commit]
        ↓
    [Pre-commit Hook]
        ↓
scripts/gdocs_sync/auto_sync.py
        ↓
    ┌───────────────────────────────┐
    │  1. Parse markdown            │
    │  2. Convert to Docs API calls │
    │  3. Create/update Google Doc  │
    │  4. Publish to web            │
    │  5. Get embed URL             │
    └───────────────────────────────┘
        ↓
docs/patterns/01-two-pointers.md (GitHub Pages)
        ↓
    [Contains iframe embed]
        ↓
    [Deploys to GitHub Pages]
        ↓
YOUR_USERNAME.github.io/dsa-mastery/patterns/01-two-pointers
        ↓
    [Readers see Google Doc embedded]
    [Can click to open and comment]
```

### Bidirectional Sync

**Markdown → Google Docs:**
- Edit `writeups/*.md`
- Commit
- Auto-syncs to Google Docs

**Google Docs → Markdown (manual):**
```bash
# Export from Google Docs
# File → Download → Markdown
# Replace writeups/file.md
# Commit
```

(We could automate this too with Google Docs API webhooks, but manual is simpler for now)

---

## 📁 File Structure

```
dsa-mastery/
├── writeups/                          # ✏️ Edit these (source of truth)
│   ├── 01_two_pointers.md
│   ├── 02_sliding_window.md
│   └── ...
├── docs/patterns/                     # 🤖 Auto-generated (don't edit directly)
│   ├── 01-two-pointers.md            # Contains Google Docs embed
│   ├── 02-sliding-window.md
│   └── ...
├── scripts/gdocs_sync/
│   ├── auto_sync.py                  # Main sync script
│   ├── credentials.json              # Google API credentials (gitignored)
│   ├── token.pickle                  # Auth token (gitignored)
│   ├── doc_mappings.json             # Markdown → Doc ID mapping
│   ├── install_hooks.sh              # Hook installer
│   └── sync_now.sh                   # Manual sync command
└── .git/hooks/
    ├── pre-commit                     # Auto-sync on commit
    └── post-commit                    # Show confirmation
```

---

## 🔒 Security & Privacy

### What's Gitignored

```gitignore
# In .gitignore
scripts/gdocs_sync/credentials.json   # Your OAuth credentials
scripts/gdocs_sync/token.pickle       # Your access token
```

**Safe to commit:**
- `scripts/gdocs_sync/doc_mappings.json` - Just document IDs (public anyway)
- `docs/patterns/*.md` - Public embed codes

### Permissions

The script requests:
- **Google Docs**: Create, read, update your docs
- **Google Drive**: Publish docs, manage permissions

**It does NOT:**
- Access your email
- Read other docs
- Access calendar, contacts, etc.

### Revoke Access

Anytime: https://myaccount.google.com/permissions
- Find "DSA Mastery Sync"
- Click "Remove Access"
- Delete `token.pickle` to re-authenticate

---

## 🐛 Troubleshooting

### "credentials.json not found"
```bash
# Download from Google Cloud Console (Step 2 above)
# Make sure saved to:
ls ~/dsa-mastery/scripts/gdocs_sync/credentials.json
```

### "Authentication failed"
```bash
# Remove old token and re-authenticate
rm ~/dsa-mastery/scripts/gdocs_sync/token.pickle
python3 scripts/gdocs_sync/auto_sync.py
```

### "Hook not running"
```bash
# Check hook is executable
ls -la .git/hooks/pre-commit

# Should show: -rwxr-xr-x (x = executable)

# If not:
chmod +x .git/hooks/pre-commit
```

### "Google Doc created but not updating"
```bash
# Check mappings
cat scripts/gdocs_sync/doc_mappings.json

# Should show:
# {
#   "writeups/01_two_pointers.md": {
#     "doc_id": "1a2b3c...",
#     ...
#   }
# }

# If corrupted, delete and re-sync:
rm scripts/gdocs_sync/doc_mappings.json
./scripts/gdocs_sync/sync_now.sh
```

### "Markdown not converting correctly"
The converter is simplified and handles:
- Headings (H1, H2, H3)
- Regular paragraphs
- Code blocks (basic)

For complex markdown:
1. Create Google Doc manually
2. Copy/paste from rendered markdown
3. Get doc ID from URL
4. Add to `doc_mappings.json`:
   ```json
   {
     "writeups/your_file.md": {
       "doc_id": "YOUR_DOC_ID",
       "title": "Your Title",
       "created": "2025-11-09T12:00:00"
     }
   }
   ```

---

## ⚡ Advanced Features

### Sync Specific Pattern

```bash
# Only sync two pointers
./scripts/gdocs_sync/sync_now.sh writeups/01_two_pointers.md
```

### Disable Auto-sync Temporarily

```bash
# Skip hooks for one commit
git commit --no-verify -m "WIP: draft writeup"
```

### Batch Sync All Patterns

```bash
# Sync everything
./scripts/gdocs_sync/sync_now.sh

# Commit all updates
git add docs/patterns/
git commit -m "Synced all writeups"
git push
```

### Custom Document Settings

Edit `auto_sync.py` to customize:
- Document font (line ~200)
- Heading styles (line ~150)
- Code block formatting (line ~180)

---

## 🎯 Complete Example

Let's sync your first writeup end-to-end:

```bash
# 1. Ensure credentials are set up
ls scripts/gdocs_sync/credentials.json  # Should exist

# 2. First-time sync (creates Google Docs)
python3 scripts/gdocs_sync/auto_sync.py

# Output:
# 📄 Creating new doc: Two Pointers Pattern
# ✅ Created Google Doc
# ✅ Updated GitHub Pages

# 3. Install hooks
./scripts/gdocs_sync/install_hooks.sh

# 4. Commit
git add .
git commit -m "Add Google Docs sync"
git push

# 5. Edit writeup
vim writeups/01_two_pointers.md
# Add: "### My New Section\nThis is a new insight..."

# 6. Commit (auto-syncs!)
git add writeups/01_two_pointers.md
git commit -m "Added new insights"

# Hook runs:
# 📝 Detected writeup changes, syncing to Google Docs...
# 🔄 Syncing: writeups/01_two_pointers.md
# ✅ Updated Google Doc
# ✅ Google Docs sync complete

# 7. Push
git push

# 8. Open Google Doc to comment
# Visit the URL printed by the script
# Highlight "My New Section"
# Add comment: "This helped me understand!"

# 9. Check GitHub Pages
# https://YOUR_USERNAME.github.io/dsa-mastery/patterns/01-two-pointers
# See embedded doc with your new section!
```

---

## 📊 Comparison: Before vs After

### Before (Manual)
```
1. Write markdown
2. Create Google Doc manually
3. Copy/paste content
4. Publish to web
5. Get embed URL
6. Update GitHub Pages markdown
7. Commit and push
8. Repeat for EVERY change
```
**~10 minutes per update** 😰

### After (Automated)
```
1. Write markdown
2. git commit
```
**~10 seconds per update** 🚀

**60x faster!**

---

## 🎓 Learning Benefits

### For You:
- **Comment** directly on confusing sections
- **Track** your understanding over time
- **Share** with mentors easily
- **Collaborate** with study partners

### For Readers:
- **Ask questions** inline
- **Suggest improvements**
- **See evolution** of your learning
- **Living documentation** that grows

---

## 🚀 Next Steps

1. **Run first sync** (creates all your current writeups as Google Docs)
   ```bash
   python3 scripts/gdocs_sync/auto_sync.py
   ```

2. **Install hooks** (enables auto-sync)
   ```bash
   ./scripts/gdocs_sync/install_hooks.sh
   ```

3. **Commit and push**
   ```bash
   git add .
   git commit -m "Set up automated Google Docs sync"
   git push
   ```

4. **Test it!**
   ```bash
   # Add something to a writeup
   echo "\n\n## Test Section\nThis is a test!" >> writeups/01_two_pointers.md

   # Commit (should auto-sync)
   git add writeups/01_two_pointers.md
   git commit -m "Test auto-sync"

   # Check Google Docs - should see "Test Section"!
   ```

5. **Share your docs** with study partners or mentors for collaborative learning

---

**Automation unlocks focus. Spend time learning, not managing documents.** ⚡📚
