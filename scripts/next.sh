#!/bin/bash
# Show what to do next in your learning journey

set -e

echo "=========================================="
echo "📚 DSA Mastery - What's Next?"
echo "=========================================="
echo ""

# Check progress
if [ -f "progress/daily_progress.json" ]; then
    DAY=$(python3 -c "import json; print(json.load(open('progress/daily_progress.json'))['day'])")
    echo "📅 Day $DAY of your journey"
    echo ""
fi

# Check if writeup exists for today
if [ -f "writeups/two_pointers.md" ]; then
    echo "✅ Today's writeup is ready!"
    echo ""
    echo "📖 Step 1: Read the writeup"
    echo "   Local:  cat writeups/two_pointers.md"
    echo "   Online: https://mindo-joseph.github.io/dsa-mastery/patterns/two-pointers.html"
    echo ""
    echo "⏱️  Time: 30 minutes"
    echo "   - Understand first principles"
    echo "   - Study the key insight"
    echo "   - Review complexity analysis"
    echo "   - Check example problems"
    echo ""
else
    echo "⚠️  No writeup yet. Generate one:"
    echo "   ./scripts/daily.sh"
    echo ""
    exit 0
fi

# Check for problems to solve
if [ -f "daily-problems/two_pointers_problems.md" ]; then
    echo "🎯 Step 2: Pick a problem to solve"
    echo "   cat daily-problems/two_pointers_problems.md"
    echo ""
fi

# Check how many problems solved
SOLVED=$(git log --oneline --grep="Solve:" 2>/dev/null | wc -l)
echo "📊 Your Progress:"
echo "   Problems solved: $SOLVED"
echo "   Target today: 2-3 problems"
echo ""

# What to do next
if [ "$SOLVED" -eq 0 ]; then
    echo "🚀 Next Step: Solve your first problem!"
    echo ""
    echo "1. Query for a problem:"
    echo "   python3 scripts/gemini_rag.py query --question \"Give me an easy two pointers problem with description and test cases\""
    echo ""
    echo "2. Create solution file:"
    echo "   git checkout -b two-pointers/problem-001"
    echo "   mkdir -p src/patterns/two_pointers"
    echo "   vim src/patterns/two_pointers/problem_001.rs"
    echo ""
    echo "3. Write solution + tests"
    echo ""
    echo "4. Test it:"
    echo "   cargo test problem_001"
    echo ""
    echo "5. Submit for review:"
    echo "   ./scripts/submit.sh src/patterns/two_pointers/problem_001.rs"
    echo ""
    echo "📖 Full guide: cat DAILY_WORKFLOW.md"
    echo ""
elif [ "$SOLVED" -lt 3 ]; then
    echo "💪 Great start! Continue solving problems."
    echo ""
    echo "Next problem:"
    echo "1. git checkout -b two-pointers/problem-$(printf '%03d' $((SOLVED + 1)))"
    echo "2. Create src/patterns/two_pointers/problem_$(printf '%03d' $((SOLVED + 1))).rs"
    echo "3. Solve, test, submit!"
    echo ""
else
    echo "🎉 Excellent! You've solved $SOLVED problems!"
    echo ""
    echo "Consider:"
    echo "- Review your solutions"
    echo "- Try a harder problem"
    echo "- Visualize a solution:"
    echo "  ./scripts/visualize.sh <problem_file.rs> \"[input]\" target"
    echo ""
fi

echo "=========================================="
echo "💡 Quick Commands"
echo "=========================================="
echo ""
echo "Query for hints:"
echo "  python3 scripts/gemini_rag.py query -q \"your question\""
echo ""
echo "Check tests:"
echo "  cargo test"
echo ""
echo "Submit solution:"
echo "  ./scripts/submit.sh <file.rs>"
echo ""
echo "Visualize:"
echo "  ./scripts/visualize.sh <file.rs> \"[input]\" target"
echo ""
echo "=========================================="
