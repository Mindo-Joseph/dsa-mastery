#!/bin/bash
#
# Install Git Hooks for Automatic Google Docs Sync
#
# This script installs hooks that automatically sync writeups to Google Docs
# whenever you commit changes to markdown files.

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"

echo "🔧 Installing automatic Google Docs sync hooks..."
echo

# Pre-commit hook: Sync changed writeups before commit
cat > "$HOOKS_DIR/pre-commit" << 'EOF'
#!/bin/bash
#
# Pre-commit hook: Auto-sync writeups to Google Docs
#

# Get list of staged markdown files in writeups/
CHANGED_WRITEUPS=$(git diff --cached --name-only --diff-filter=ACM | grep '^writeups/.*\.md$' || true)

if [ -n "$CHANGED_WRITEUPS" ]; then
    echo "📝 Detected writeup changes, syncing to Google Docs..."
    echo

    cd "$(git rev-parse --show-toplevel)"

    for file in $CHANGED_WRITEUPS; do
        echo "🔄 Syncing: $file"
        python3 scripts/gdocs_sync/auto_sync.py "$file"
        echo
    done

    # Stage the updated GitHub Pages files
    git add docs/patterns/

    echo "✅ Google Docs sync complete"
    echo
fi
EOF

chmod +x "$HOOKS_DIR/pre-commit"

echo "✅ Installed pre-commit hook"
echo

# Post-commit hook: Show sync summary
cat > "$HOOKS_DIR/post-commit" << 'EOF'
#!/bin/bash
#
# Post-commit hook: Show Google Docs links
#

# Check if any docs were synced in this commit
if git diff HEAD~1 --name-only | grep -q '^docs/patterns/'; then
    echo
    echo "📚 Your writeups are now in Google Docs!"
    echo "   Check: https://YOUR_USERNAME.github.io/dsa-mastery/patterns/"
    echo
fi
EOF

chmod +x "$HOOKS_DIR/post-commit"

echo "✅ Installed post-commit hook"
echo

# Create manual sync command
cat > "$REPO_ROOT/scripts/gdocs_sync/sync_now.sh" << 'EOF'
#!/bin/bash
#
# Manual Google Docs Sync
#
# Usage:
#   ./scripts/gdocs_sync/sync_now.sh              # Sync all writeups
#   ./scripts/gdocs_sync/sync_now.sh <file.md>    # Sync specific file
#

cd "$(dirname "$0")/../.."

if [ -n "$1" ]; then
    echo "🔄 Syncing: $1"
    python3 scripts/gdocs_sync/auto_sync.py "$1"
else
    echo "🔄 Syncing all writeups..."
    python3 scripts/gdocs_sync/auto_sync.py
fi

echo
echo "✨ Sync complete!"
echo "   Don't forget to commit the updated docs/ files"
EOF

chmod +x "$REPO_ROOT/scripts/gdocs_sync/sync_now.sh"

echo "✅ Created manual sync script"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Installation complete!"
echo
echo "How it works:"
echo "  1. Edit any file in writeups/"
echo "  2. Run: git add writeups/your_file.md"
echo "  3. Run: git commit -m 'Updated writeup'"
echo "  4. 🎉 Automatically syncs to Google Docs and updates GitHub Pages!"
echo
echo "Manual sync:"
echo "  ./scripts/gdocs_sync/sync_now.sh                 # All writeups"
echo "  ./scripts/gdocs_sync/sync_now.sh writeups/01_two_pointers.md   # Single file"
echo
echo "First-time setup:"
echo "  1. Get credentials from Google Cloud Console"
echo "  2. Save as: scripts/gdocs_sync/credentials.json"
echo "  3. Run: python3 scripts/gdocs_sync/auto_sync.py"
echo "  4. Authenticate once in browser"
echo "  5. Future syncs are automatic!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
EOF

chmod +x "$REPO_ROOT/scripts/gdocs_sync/install_hooks.sh"

echo "✅ Created hook installer script"
