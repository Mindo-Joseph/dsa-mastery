# Callstack & Algorithm Visualization System

**Visualize exactly what happens in your code - frame by frame.**

## 🎯 What This Does

For every problem you solve, generate:
1. **Callstack animation** - See function calls, stack frames, variables
2. **Algorithm execution** - Watch pointers move, arrays change, recursion unfold
3. **Complexity visualization** - See why O(n) vs O(n²) matters

**Output**: MP4 video you can watch, share, and review

---

## 🛠️ Technology Stack

- **Manim** - Mathematical animation engine (3Blue1Brown quality)
- **ffmpeg** - Video encoding
- **Your code** - Instrumented Rust/Ruby to generate visualization data

---

## 📦 Setup (5 minutes)

### Install Manim Community Edition

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev python3-pip

# Install Manim
pip3 install manim

# Verify installation
manim --version
```

### Install Ruby (for dual-language support)

```bash
# Install Ruby
sudo apt-get install -y ruby-full

# Verify
ruby --version

# Install gems for visualization
gem install rouge  # Syntax highlighting
```

---

## 🎬 Quick Start - Generate Your First Visualization

### Example: Two Pointers Algorithm

```bash
cd ~/dsa-mastery

# Run your solution with tracing enabled
python3 scripts/visualize/trace_solution.py \
  --solution src/patterns/two_pointers/problem_001_two_sum_ii.rs \
  --input "[2,7,11,15]" \
  --target 9

# This generates: trace_data.json

# Create animation
manim scripts/visualize/callstack_viz.py TwoPointersScene -pql

# Output: media/videos/callstack_viz/480p15/TwoPointersScene.mp4
```

**Open the video** - Watch your algorithm execute step by step!

---

## 📁 File Structure

```
scripts/visualize/
├── README.md                    ← You are here
├── trace_solution.py            ← Instrument code to generate trace
├── callstack_viz.py             ← Manim scenes for callstack
├── algorithm_viz.py             ← Algorithm-specific visualizations
├── templates/
│   ├── two_pointers.py          ← Two pointers animation
│   ├── sliding_window.py        ← Sliding window animation
│   ├── recursion_tree.py        ← Recursion tree visualization
│   └── ...
└── examples/                    ← Example outputs
```

---

## 🎨 What You Can Visualize

### 1. Callstack Execution
```
┌─────────────────┐
│  main()         │  ← Current frame
│  - nums: [...]  │
│  - target: 9    │
├─────────────────┤
│  two_sum()      │  ← Function call
│  - left: 0      │
│  - right: 3     │
│  - sum: 17      │
└─────────────────┘
```

Watch the stack grow/shrink with each function call.

### 2. Variable Changes
See variables update in real-time:
- `left = 0 → 1 → 2`
- `right = 3 → 2`
- `sum = 17 → 13 → 9` ✓

### 3. Array/Pointer Movement
Visual representation:
```
[2, 7, 11, 15]
 ↑          ↑    sum = 17 (too large)
 ↑       ↑       sum = 13 (too large)
 ↑    ↑          sum = 9  (found!)
```

### 4. Recursion Trees
For recursive algorithms, see the call tree:
```
              fib(4)
             /      \
        fib(3)      fib(2)
       /     \      /    \
   fib(2)  fib(1) fib(1) fib(0)
   /   \
fib(1) fib(0)
```

### 5. Time Complexity Animation
Watch algorithm run with different input sizes:
- n=10: X operations
- n=100: Y operations
- n=1000: Z operations

Visualize O(n) vs O(n²) growth.

---

## 🦀 Rust + 🔴 Ruby Dual Language Support

### Your Workflow

**Option 1: Rust Implementation**
```rust
// src/patterns/two_pointers/problem_001_two_sum_ii.rs
pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    // Your Rust solution
}
```

**Option 2: Ruby Implementation**
```ruby
# src/patterns/two_pointers/problem_001_two_sum_ii.rb
def two_sum(numbers, target)
  # Your Ruby solution
end
```

**Both generate the same visualization!**

---

## 📝 How It Works

### Step 1: Instrument Your Code

Add trace points to your solution:

**Rust:**
```rust
#[cfg(feature = "trace")]
fn trace_state(msg: &str, vars: &HashMap<String, Value>) {
    println!("TRACE: {}: {:?}", msg, vars);
}

pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    #[cfg(feature = "trace")]
    trace_state("init", hashmap!{
        "left" => left.into(),
        "right" => right.into(),
    });

    while left < right {
        let sum = numbers[left] + numbers[right];

        #[cfg(feature = "trace")]
        trace_state("iteration", hashmap!{
            "left" => left.into(),
            "right" => right.into(),
            "sum" => sum.into(),
        });

        // ... rest of solution
    }
}
```

**Ruby:**
```ruby
def two_sum(numbers, target, trace: false)
  left = 0
  right = numbers.length - 1

  trace_state("init", {left: left, right: right}) if trace

  while left < right
    sum = numbers[left] + numbers[right]

    trace_state("iteration", {
      left: left,
      right: right,
      sum: sum
    }) if trace

    # ... rest of solution
  end
end

def trace_state(event, vars)
  puts "TRACE: #{event}: #{vars.inspect}"
end
```

### Step 2: Run with Tracing

```bash
# Rust
cargo run --features trace --bin trace_runner -- \
  problem_001_two_sum_ii \
  "[2,7,11,15]" \
  9 \
  > trace_data.json

# Ruby
ruby scripts/trace_runner.rb \
  src/patterns/two_pointers/problem_001_two_sum_ii.rb \
  "[2,7,11,15]" \
  9 \
  > trace_data.json
```

### Step 3: Generate Video

```bash
python3 scripts/visualize/generate_video.py \
  --trace trace_data.json \
  --pattern two_pointers \
  --output two_sum_visualization.mp4
```

**Done!** Watch your algorithm execute visually.

---

## 🎥 Example Visualizations

### Two Pointers - Two Sum II

**Frame 1: Initial State**
```
Array: [2, 7, 11, 15]
        ↑           ↑
      left=0    right=3

Callstack:
┌─────────────────┐
│  two_sum()      │
│  left: 0        │
│  right: 3       │
└─────────────────┘
```

**Frame 2: First Iteration**
```
Array: [2, 7, 11, 15]
        ↑           ↑
      left=0    right=3

sum = 2 + 15 = 17
17 > 9 → Move right pointer left

Callstack:
┌─────────────────┐
│  two_sum()      │
│  left: 0        │
│  right: 3       │
│  sum: 17        │ ← New variable
└─────────────────┘
```

**Frame 3: Second Iteration**
```
Array: [2, 7, 11, 15]
        ↑       ↑
      left=0  right=2

sum = 2 + 11 = 13
13 > 9 → Move right pointer left

Callstack:
┌─────────────────┐
│  two_sum()      │
│  left: 0        │
│  right: 2  ←── │
│  sum: 13   ←── │
└─────────────────┘
```

**Frame 4: Solution Found**
```
Array: [2, 7, 11, 15]
        ↑   ↑
      left=0 right=1

sum = 2 + 7 = 9 ✓
return [1, 2]  (1-indexed)

Callstack:
┌─────────────────┐
│  two_sum()      │
│  left: 0        │
│  right: 1       │
│  sum: 9    ✓    │
│  return: [1,2]  │
└─────────────────┘
```

---

## 🧪 Advanced: Complexity Visualization

### Compare O(n) vs O(n²)

```python
# scripts/visualize/complexity_comparison.py
manim -pql complexity_comparison.py CompareComplexity

# Shows:
# - Two Sum (Brute Force): O(n²)
# - Two Sum (Two Pointers): O(n)
#
# Side-by-side with input size scaling
```

**Output**: Graph showing how execution time grows

---

## 🎓 When to Use This

### During Learning
- **Understand** how algorithm actually executes
- **Debug** why your solution doesn't work
- **See** the difference between O(n) and O(n²)

### For Review
- **Show me** the visualization when asking for help
- **Include** in your PR for complex solutions
- **Reference** when explaining your approach

### For Sharing
- **Publish** to your GitHub Pages
- **Embed** in writeups
- **Tweet** your progress with visuals

---

## 📋 Quick Reference

### Generate Visualization

```bash
# Full command
python3 scripts/visualize/generate_video.py \
  --language rust \  # or ruby
  --solution src/patterns/two_pointers/problem_001.rs \
  --input "[2,7,11,15]" \
  --args "9" \
  --pattern two_pointers \
  --output visualizations/two_sum.mp4 \
  --quality high  # low/medium/high

# Shorthand for common case
./scripts/visualize/quick_viz.sh \
  two_pointers/problem_001 \
  "[2,7,11,15]" \
  9
```

### Watch Output

```bash
# Open video
xdg-open visualizations/two_sum.mp4

# Or copy to your public site
cp visualizations/*.mp4 docs/visualizations/
git add docs/visualizations/
git commit -m "Add algorithm visualizations"
git push  # Auto-publishes to GitHub Pages
```

---

## 🔧 Configuration

### Customize Animation Style

Edit `scripts/visualize/config.py`:

```python
# Animation settings
FPS = 30  # Frames per second
QUALITY = "high"  # low/medium/high
DURATION_PER_STEP = 1.5  # seconds

# Visual style
THEME = "dark"  # dark/light
HIGHLIGHT_COLOR = "#00ff00"
CALLSTACK_POSITION = UP * 2
ARRAY_POSITION = DOWN * 2

# Code display
SHOW_SOURCE_CODE = True
SYNTAX_HIGHLIGHTING = True
```

---

## 🚀 Integration with Workflow

### Updated Daily Workflow

```
1. Query NotebookLM for problem
2. Solve in Rust (30 min)
3. Solve in Ruby (15 min) - OPTIONAL but recommended
4. Generate visualization (5 min)
5. Watch video, understand execution
6. Create PR (5 min)
7. Include visualization in PR description
8. Get review
9. Optimize
```

### PR Template Updated

Your PR should now include:

```markdown
## Visualization

[Watch the algorithm execute](../visualizations/two_sum.mp4)

Key insights from visualization:
- Pointer movement pattern
- Why O(n) is optimal
- Edge cases handled
```

---

## 💡 Why This Matters for Senior Level

### Google interviews expect you to:

1. **Explain execution** - Not just "it works"
2. **Visualize in your head** - Walk through step-by-step
3. **Prove complexity** - Show why it's O(n)
4. **Debug live** - Trace through code during interview

**These visualizations train you to do exactly that.**

You'll develop the ability to "see" the algorithm execute in your mind - critical for senior-level performance.

---

## 📚 Next Steps

1. **Install Manim** (see Setup above)
2. **Run example** (I'll create one when you start)
3. **Watch output** - See what's possible
4. **Integrate** into your daily workflow

---

**Visual understanding separates senior engineers from everyone else.**

**Let's make your algorithms visible.** 🎬
