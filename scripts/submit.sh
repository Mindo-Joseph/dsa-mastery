#!/bin/bash
# Submit solution for automated review
# Usage: ./scripts/submit.sh src/patterns/two_pointers/problem_001.rs

set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/submit.sh <problem_file.rs>"
    exit 1
fi

PROBLEM_FILE="$1"
PROBLEM_NAME=$(basename "$PROBLEM_FILE" .rs)

echo "========================================"
echo "📤 SUBMITTING: $PROBLEM_NAME"
echo "========================================"
echo ""

# Step 1: Run tests
echo "🧪 Step 1: Running tests..."
cargo test --lib -- "$PROBLEM_NAME" --nocapture

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Tests failed. Fix errors and try again."
    exit 1
fi

echo "✅ All tests passed!"
echo ""

# Step 2: Create PR
echo "📝 Step 2: Creating pull request..."

# Get current branch or create new one
CURRENT_BRANCH=$(git branch --show-current)

if [ "$CURRENT_BRANCH" = "main" ]; then
    # Create new branch
    BRANCH_NAME="solution/$PROBLEM_NAME"
    git checkout -b "$BRANCH_NAME"
    echo "Created branch: $BRANCH_NAME"
fi

# Commit
git add "$PROBLEM_FILE"
git commit -m "Solve: $PROBLEM_NAME" || true
git push -u origin HEAD

# Create PR
gh pr create --fill --body "## Solution: $PROBLEM_NAME

### Tests
✅ All tests passing

### Complexity Analysis
<!-- Add your complexity analysis here -->
- Time: O(?)
- Space: O(?)

### Trade-offs
<!-- Explain your approach and trade-offs -->

---
*Ready for review* 🚀
" || echo "PR might already exist"

echo ""
echo "========================================"
echo "✅ SUBMISSION COMPLETE"
echo "========================================"
echo ""
echo "🎯 Next steps:"
echo "1. PR created - waiting for review"
echo "2. Want visualization? Run: ./scripts/visualize.sh $PROBLEM_FILE \"[1,2,3]\" 6"
echo "3. After PR approved, merge and continue to next problem"
echo ""
