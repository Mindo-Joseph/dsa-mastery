#!/bin/bash
# Generate Manim visualization for your solution
# Usage: ./scripts/visualize.sh <problem_file.rs> <input> <target>

set -e

if [ -z "$1" ]; then
    echo "Usage: ./scripts/visualize.sh <problem_file.rs> <input> [target]"
    echo ""
    echo "Example:"
    echo "  ./scripts/visualize.sh src/patterns/two_pointers/problem_001.rs \"[1,2,3,4,5]\" 6"
    exit 1
fi

PROBLEM_FILE="$1"
INPUT="$2"
TARGET="$3"

echo "========================================"
echo "🎨 GENERATING VISUALIZATION"
echo "========================================"
echo ""
echo "Problem: $(basename "$PROBLEM_FILE")"
echo "Input: $INPUT"
echo "Target: $TARGET"
echo ""

# Check if Manim is installed
if ! command -v manim &> /dev/null; then
    echo "❌ Manim not installed"
    echo ""
    echo "Install with:"
    echo "  pip3 install manim"
    exit 1
fi

# TODO: Generate trace data from solution
echo "📊 Step 1: Generating execution trace..."
echo "(This would run your solution with instrumentation)"
echo ""

# For now, use existing Manim script
echo "🎬 Step 2: Creating animation with Manim..."
manim scripts/visualize/callstack_viz.py TwoPointersScene -pql

echo ""
echo "========================================"
echo "✅ VISUALIZATION COMPLETE"
echo "========================================"
echo ""
echo "📹 Video saved to: media/videos/"
echo "🎥 Open and watch the step-by-step execution!"
echo ""
