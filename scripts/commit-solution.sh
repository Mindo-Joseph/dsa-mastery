#!/usr/bin/env bash

# Safe Commit Helper for DSA Solutions
# Enforces testing and complexity validation before commits

set -euo pipefail

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <commit-message> <file1> [file2 ...]"
    echo ""
    echo "Example:"
    echo "  $0 'Solve: Two Sum II' src/patterns/two_pointers/problem_001.rs"
    exit 1
fi

COMMIT_MESSAGE="$1"
shift
FILES=("$@")

echo "🔍 Pre-commit validation..."

# Check if files exist
for file in "${FILES[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "❌ File not found: $file"
        exit 1
    fi
done

# Run tests
echo "🧪 Running tests..."
if ! cargo test --lib 2>&1 | tee /tmp/test-output.log; then
    echo ""
    echo "❌ Tests failed! Fix before committing."
    exit 1
fi

echo "✅ Tests passed"

# Check complexity annotations
echo "📊 Checking complexity annotations..."
for file in "${FILES[@]}"; do
    if [[ "$file" =~ src/patterns/.*\.rs ]]; then
        if ! grep -q "// Time:" "$file" || ! grep -q "// Space:" "$file"; then
            echo "❌ Missing complexity annotations in $file"
            echo ""
            echo "Add comments like:"
            echo "  // Time: O(n)"
            echo "  // Space: O(1)"
            exit 1
        fi
    fi
done

echo "✅ Complexity annotations present"

# Safe commit
echo "💾 Committing..."

export USING_COMMIT_HELPER=1

git restore --staged :/ 2>/dev/null || true
git add --force "${FILES[@]}"

if git diff --staged --quiet; then
    echo "⚠️  No changes to commit"
    exit 1
fi

git commit -m "$COMMIT_MESSAGE"

echo "✅ Committed successfully!"
echo ""
echo "Files committed:"
for file in "${FILES[@]}"; do
    echo "  - $file"
done
