# Visual Debugging & Understanding Guide

**See your algorithms execute - frame by frame.**

---

## 🎯 Why Visualize?

### Senior-Level Expectation:
In Google interviews, you must **explain your solution while walking through execution**.

Visualizations train you to:
- See the algorithm in your head
- Explain execution step-by-step
- Debug efficiently
- Prove complexity visually

---

## 🛠️ Quick Setup

```bash
# Install visualization tools
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev
pip3 install manim

# Install Ruby (optional, for dual-language)
sudo apt-get install -y ruby-full
cd ~/dsa-mastery/src_ruby && bundle install

# Verify
manim --version
ruby --version
```

---

## ⚡ Quick Start - Generate Your First Video

### Example: Two Pointers Visualization

```bash
cd ~/dsa-mastery

# Generate animation
manim scripts/visualize/callstack_viz.py TwoPointersScene -pql

# Output location
ls media/videos/callstack_viz/480p15/TwoPointersScene.mp4

# Watch it
xdg-open media/videos/callstack_viz/480p15/TwoPointersScene.mp4
```

**What you'll see:**
- Array visualization with moving pointers
- Callstack showing variable changes
- Step-by-step algorithm execution
- Complexity analysis

---

## 📊 What You Can Visualize

### 1. Callstack Execution
Watch function calls, stack frames, variable updates

### 2. Data Structure Changes
See arrays, linked lists, trees transform in real-time

### 3. Pointer Movement
Visualize two pointers, sliding windows, fast/slow pointers

### 4. Recursion Trees
See recursive calls build and unwind

### 5. Complexity Growth
Watch O(n) vs O(n²) performance difference

---

## 🔄 Dual Language Workflow

### Option 1: Rust Only (Recommended)
```
Solve in Rust → Generate visualization → PR review → Merge
```

### Option 2: Rust + Ruby (Advanced)
```
Solve in Rust → PR review → Merge
     ↓
Solve in Ruby → Compare approaches → Generate visualization → Deeper understanding
```

**When to use Ruby:**
- Want different perspective on algorithm
- Stuck on Rust implementation
- Rapid prototyping of ideas
- Teaching/explaining to others

---

## 📝 Implementation Templates

### Rust with Tracing

```rust
#[cfg(feature = "trace")]
use std::collections::HashMap;

pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    #[cfg(feature = "trace")]
    trace!("init", {
        "left" => left,
        "right" => right
    });

    while left < right {
        let sum = numbers[left] + numbers[right];

        #[cfg(feature = "trace")]
        trace!("iteration", {
            "left" => left,
            "right" => right,
            "sum" => sum
        });

        match sum.cmp(&target) {
            Ordering::Equal => return vec![(left + 1) as i32, (right + 1) as i32],
            Ordering::Less => left += 1,
            Ordering::Greater => right -= 1,
        }
    }

    vec![]
}
```

### Ruby with Tracing

```ruby
require_relative '../../lib/tracer'

class Solution
  include Tracer

  def two_sum(numbers, target)
    left = 0
    right = numbers.length - 1

    trace(:init, {left: left, right: right})

    while left < right
      sum = numbers[left] + numbers[right]

      trace(:iteration, {left: left, right: right, sum: sum})

      return [left + 1, right + 1] if sum == target

      sum < target ? left += 1 : right -= 1
    end

    []
  end
end
```

---

## 🎬 Generate Visualization

### From Rust
```bash
# Build with tracing
cargo run --features trace -- \
  two_sum_ii \
  "[2,7,11,15]" \
  9 \
  > trace_data.json

# Generate video
python3 scripts/visualize/generate_from_trace.py \
  --input trace_data.json \
  --output visualizations/two_sum_rust.mp4
```

### From Ruby
```bash
# Run with tracing
Tracer.enable!
solution = Solution.new
result = solution.two_sum([2,7,11,15], 9)
File.write('trace_data.json', Tracer.export_json)

# Generate video (same script)
python3 scripts/visualize/generate_from_trace.py \
  --input trace_data.json \
  --output visualizations/two_sum_ruby.mp4
```

### Direct Animation (No Trace File)
```bash
# Use pre-built Manim scenes
manim scripts/visualize/callstack_viz.py TwoPointersScene -pqh

# Quality options:
# -ql : Low quality (faster)
# -qm : Medium quality
# -qh : High quality (best)
```

---

## 🎨 Visualization Types

### 1. Two Pointers
**File**: `scripts/visualize/callstack_viz.py`
**Scene**: `TwoPointersScene`

Shows:
- Array with two pointers moving
- Callstack with variables
- Sum calculation
- Decision logic

### 2. Sliding Window
**File**: `scripts/visualize/sliding_window_viz.py`
**Scene**: `SlidingWindowScene`

Shows:
- Window expanding/contracting
- Window state maintenance
- Optimal subarray tracking

### 3. Recursion Tree
**File**: `scripts/visualize/recursion_viz.py`
**Scene**: `RecursionTreeScene`

Shows:
- Call tree structure
- Stack frame creation/destruction
- Base case reaching
- Result propagation

### 4. Dynamic Programming
**File**: `scripts/visualize/dp_viz.py`
**Scene**: `DPTableScene`

Shows:
- DP table filling
- State transitions
- Memoization benefits
- Optimal substructure

---

## 📋 Updated Daily Workflow

### Enhanced Problem-Solving Process

```
1. Query NotebookLM for problem (10 min)
2. Solve in Rust (30 min)
3. Generate visualization (5 min) ← NEW
4. Watch & understand execution (5 min) ← NEW
5. Optional: Solve in Ruby for comparison (15 min) ← NEW
6. Create PR with visualization link (5 min)
7. Get review (10 min)
8. Optimize (10 min)
9. Merge & publish (5 min)
```

**Total**: ~90-105 minutes (with optional Ruby)

---

## 💡 How to Use Visualizations

### During Learning
```
1. Solve problem
2. Generate visualization
3. Watch execution
4. If confused → Re-watch specific frames
5. Understand WHY it works
6. Proceed with confidence
```

### During Debugging
```
1. Solution failing tests
2. Generate visualization
3. Watch where it breaks
4. See the exact frame where logic fails
5. Fix the issue
6. Re-generate to verify
```

### During PR Review
```
1. Create PR
2. Include visualization link:
   "Watch execution: ../visualizations/two_sum.mp4"
3. Reference specific frames in explanation
4. Show complexity visually
```

### For Interview Prep
```
1. Generate visualizations for key problems
2. Watch repeatedly
3. Practice explaining execution
4. Develop "mind's eye" for algorithms
5. In interview: Visualize mentally while explaining
```

---

## 🌐 Publishing Visualizations

### Add to GitHub Pages

```bash
# Generate visualization
manim scripts/visualize/callstack_viz.py TwoPointersScene -pqh

# Copy to docs
cp media/videos/callstack_viz/1080p60/TwoPointersScene.mp4 \
   docs/visualizations/two_pointers_two_sum.mp4

# Commit
git add docs/visualizations/
git commit -m "Add Two Pointers visualization"
git push

# Now available at:
# https://YOUR_USERNAME.github.io/dsa-mastery/visualizations/two_pointers_two_sum.mp4
```

### Embed in Writeups

In your pattern writeups:

```markdown
## Visual Execution

[Watch the algorithm execute](../visualizations/two_pointers_two_sum.mp4)

Key frames:
- 0:05 - Initial state with pointers at both ends
- 0:15 - First comparison, sum too large
- 0:25 - Right pointer moves left
- 0:35 - Solution found!
```

---

## 🎓 Senior-Level Insights

### What Google Interviewers Look For:

**Junior**: "Here's my code, it works"
**Senior**: "Let me walk you through the execution..."

*Draws on whiteboard or explains verbally while visualizing mentally*

### How Visualizations Help:

1. **Pattern Recognition** - See patterns across problems
2. **Complexity Intuition** - Visualize why O(n) beats O(n²)
3. **Debug Skills** - Trace execution efficiently
4. **Communication** - Explain clearly with visual metaphors
5. **Confidence** - Know exactly how your code executes

---

## 🔧 Customization

### Create Your Own Visualizations

```python
# scripts/visualize/my_custom_viz.py

from manim import *

class MyProblemScene(Scene):
    def construct(self):
        # Your custom visualization
        title = Text("My Problem Solution")
        self.play(Write(title))

        # Add your logic
        # Use ArrayVisualization, CallStackFrame classes
        # Or build custom animations

        self.wait(2)
```

### Render Your Scene

```bash
manim scripts/visualize/my_custom_viz.py MyProblemScene -pqh
```

---

## 📚 Examples Provided

Check `scripts/visualize/examples/` for:
- Two Pointers (Two Sum II)
- Sliding Window (Max Subarray)
- Binary Search (Search in Rotated Array)
- Recursion (Fibonacci)
- Dynamic Programming (Coin Change)

**Run them all:**
```bash
./scripts/visualize/generate_all_examples.sh
```

---

## 🎯 Success Metrics

You've mastered visualization when:
- ✓ Can generate visualization for any problem
- ✓ Understand execution by watching video
- ✓ Can explain algorithm referencing visual frames
- ✓ Create custom visualizations for complex problems
- ✓ Visualize algorithm mentally during interviews

---

## 🆘 Troubleshooting

### Manim Not Installed
```bash
pip3 install manim
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev
```

### Video Not Generated
```bash
# Check Manim version
manim --version

# Try low quality first
manim script.py SceneName -pql

# Check output location
ls media/videos/
```

### Ruby Tracer Not Working
```bash
cd src_ruby
bundle install
ruby -I lib your_solution.rb
```

---

## 📞 Integration with Claude

### Ask Me:
```
"Generate visualization for this problem"
"Show me the callstack for my solution"
"Create a side-by-side comparison of Rust vs Ruby"
"Make a recursion tree visualization"
```

**I'll create custom Manim scenes for your specific problem.**

---

**Visual understanding is the secret weapon of senior engineers.**

**See the algorithm. Understand the algorithm. Master the algorithm.** 🎬
