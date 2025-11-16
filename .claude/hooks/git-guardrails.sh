#!/usr/bin/env bash

# Git Guardrails Hook
# Prevents destructive git operations and enforces safe practices
# Adapted from steipete/agent-scripts

set -euo pipefail

# Check if this is a git command
if [[ "${TOOL_NAME:-}" != "Bash" ]]; then
    exit 0
fi

COMMAND="${BASH_COMMAND:-$*}"

# Extract git subcommand if present
if [[ ! "$COMMAND" =~ git[[:space:]] ]]; then
    exit 0
fi

# Parse git subcommand
GIT_SUBCOMMAND=$(echo "$COMMAND" | sed -n 's/.*git[[:space:]]\+\([a-z-]\+\).*/\1/p')

# Destructive operations - BLOCK
DESTRUCTIVE_COMMANDS=("reset" "clean" "restore" "filter-branch" "fast-import")
for cmd in "${DESTRUCTIVE_COMMANDS[@]}"; do
    if [[ "$GIT_SUBCOMMAND" == "$cmd" ]]; then
        echo "❌ BLOCKED: git $cmd is destructive!"
        echo ""
        echo "This operation can lose data permanently."
        echo ""
        echo "If you REALLY need this, use:"
        echo "  ALLOW_DESTRUCTIVE_GIT=1 <your command>"
        echo ""
        exit 1
    fi
done

# Guarded operations - REQUIRE CONSENT
GUARDED_COMMANDS=("push" "pull" "merge" "rebase" "cherry-pick")
for cmd in "${GUARDED_COMMANDS[@]}"; do
    if [[ "$GIT_SUBCOMMAND" == "$cmd" ]]; then
        if [[ "${ALLOW_GIT_PUSH:-}" != "1" && "${GIT_CONSENT:-}" != "1" ]]; then
            echo "⚠️  CONSENT REQUIRED: git $cmd"
            echo ""
            echo "This operation affects remote/branches."
            echo ""
            echo "To proceed:"
            echo "  GIT_CONSENT=1 <your command>"
            echo ""
            echo "Or for push specifically:"
            echo "  ALLOW_GIT_PUSH=1 git push"
            echo ""
            exit 1
        fi
    fi
done

# Commit/Add operations - REQUIRE COMMIT HELPER
if [[ "$GIT_SUBCOMMAND" == "add" || "$GIT_SUBCOMMAND" == "commit" ]]; then
    # Allow if using commit helper
    if [[ "${USING_COMMIT_HELPER:-}" == "1" ]]; then
        exit 0
    fi

    echo "❌ BLOCKED: Direct git $GIT_SUBCOMMAND"
    echo ""
    echo "Use the safe commit helper instead:"
    echo "  ./scripts/commit-solution.sh \"Your message\" file1.rs file2.rs"
    echo ""
    echo "This ensures:"
    echo "  - Staged changes are explicit"
    echo "  - Commit messages are meaningful"
    echo "  - Tests pass before committing"
    echo ""
    exit 1
fi

# Checkout/switch - WARN but allow with -b for new branches
if [[ "$GIT_SUBCOMMAND" == "checkout" || "$GIT_SUBCOMMAND" == "switch" ]]; then
    if [[ ! "$COMMAND" =~ -b ]]; then
        echo "⚠️  WARNING: git $GIT_SUBCOMMAND without -b"
        echo "This can discard uncommitted changes."
        echo ""
        echo "Consider: git stash first, or use -b for new branch"
        echo ""
        echo "Proceeding in 3 seconds... (Ctrl+C to cancel)"
        sleep 3
    fi
fi

# Stash - WARN about drop/clear
if [[ "$GIT_SUBCOMMAND" == "stash" ]]; then
    if [[ "$COMMAND" =~ (drop|clear) ]]; then
        echo "⚠️  WARNING: git stash drop/clear is permanent!"
        echo ""
        echo "Proceeding in 3 seconds... (Ctrl+C to cancel)"
        sleep 3
    fi
fi

exit 0
