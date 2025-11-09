# Complete Learning Workflow

## Your Daily DSA Practice System

### Morning: Theory & Planning (15 minutes)

1. **Check Progress Dashboard**
   ```bash
   cd ~/dsa-mastery
   python scripts/log_progress.py stats
   ```

2. **Check Reviews Due**
   ```bash
   python scripts/log_progress.py reviews
   ```

3. **Plan Today's Pattern**
   - Pick pattern from PATTERNS.md based on your schedule
   - Set goal: Learn theory + solve 2-3 problems

---

### Deep Work Session 1: Pattern Learning (60-90 minutes)

#### Step 1: Query NotebookLM for Theory (5 min)

In Claude Code, ask:
```
"Query my algorithm design book about [PATTERN NAME] pattern:
- When should I use this pattern?
- What's the time and space complexity?
- What are the key insights that make it work?
- Give me the most common variations"
```

I'll automatically invoke the NotebookLM skill and bring back the theory.

#### Step 2: Implement Pattern Template (15 min)

Together we'll create a reusable template:
```python
# You: "Help me implement a [PATTERN] template with examples"
# Me: Creates template in patterns/[pattern]/template.py
```

#### Step 3: Get Practice Problem from NotebookLM (2 min)

```
"Query my leetcode notebook for an easy [PATTERN] problem with:
- Problem statement
- Example inputs/outputs
- Constraints"
```

#### Step 4: Solve with Claude (30-40 min)

**The collaboration loop:**

1. **Understand**: You read the problem
2. **Identify**: "This looks like a [pattern] problem because..."
3. **Plan**: We discuss approach together
4. **Code**: You attempt first, I provide hints
5. **Test**: Run against examples
6. **Debug**: Fix issues together
7. **Optimize**: Analyze complexity, improve if needed
8. **Explain**: You explain why it works (Feynman technique)

```bash
# Create problem file
cd ~/dsa-mastery
python scripts/problem_template.py "problem-name" "pattern-name" "easy"

# Then we implement together in that file
```

#### Step 5: Log Progress (2 min)

```bash
python scripts/log_progress.py log \
  "pattern-name" \
  "problem-name" \
  "easy" \
  "35" \
  "success" \
  "Tricky edge case with empty array"
```

#### Step 6: Repeat for Problem 2 & 3

Same flow, increase difficulty.

---

### Deep Work Session 2: Application & Review (60 minutes)

#### Step 7: Query Architecture Connection

```
"Ask my architecture book how the [PATTERN] pattern relates to:
- System design concepts
- Real-world applications
- Performance optimization in production systems"
```

This deepens understanding beyond just solving leetcode problems.

#### Step 8: Create Concise Notes

```bash
# I help you create a 1-page summary
# Saved in notes/[pattern].md
```

Include:
- Pattern definition
- When to use (decision criteria)
- Template code
- Common pitfalls
- Problems solved today

#### Step 9: Review Yesterday's Problems

```bash
# Get problems due for review
python scripts/log_progress.py reviews

# Re-solve without looking at solution
# If stuck > 10 min, review your old solution
```

---

### Evening: Commit & Reflect (10 minutes)

```bash
cd ~/dsa-mastery

# Review what changed
git status
git diff

# Commit the day's work
git add .
git commit -m "Day X: Mastered [PATTERN] - solved [N] problems

Problems:
- problem-1 (easy) - 25min
- problem-2 (medium) - 45min

Key learning: [Your insight]"

# View progress
python scripts/log_progress.py stats
```

---

## Weekly Workflow

### Sunday: Planning Week

1. **Review last week's stats**
   ```bash
   python scripts/log_progress.py stats
   ```

2. **Plan this week's patterns**
   - Week 1-2: Two Pointers, Sliding Window, Binary Search
   - Week 3-4: Linked Lists, Trees
   - etc. (see PATTERNS.md)

3. **Query NotebookLM for weekly problems**
   ```
   "Give me a curated list of 15-20 problems for mastering
   [PATTERN 1], [PATTERN 2], and [PATTERN 3] patterns,
   distributed across easy, medium, and hard difficulties"
   ```

4. **Create weekly plan**
   - Save problem list
   - Set daily targets
   - Schedule mock interview (Friday)

### Friday: Mock Interview

```
"Give me a medium-hard mixed pattern problem from my leetcode notebook
that combines [patterns learned this week]"

# Solve under time pressure (45 min)
# Then optimize and discuss
```

---

## NotebookLM Integration Patterns

### Research Queries

**Problem Understanding:**
```
"Explain this problem from my leetcode notebook: [paste problem]
What pattern does it use and why?"
```

**Theory Deep-Dive:**
```
"From my algorithm design book, explain [specific algorithm]
with time complexity proof and when to use it"
```

**Architecture Context:**
```
"How does [algorithm/data structure] relate to system design?
Check my architecture book"
```

**Similar Problems:**
```
"Find 3 more problems similar to [problem name] from my
leetcode notebook with varying difficulty"
```

### Getting Unstuck

**When stuck > 15 min:**
```
"I'm stuck on this [PATTERN] problem: [describe problem]
My approach: [what you tried]
What am I missing? Query my resources"
```

**Understanding Solutions:**
```
"Why does this solution work: [paste solution]
Explain the intuition from first principles using my algo book"
```

---

## Agent & Skills Usage

### When I Use the NotebookLM Skill

I automatically invoke it when you:
- Mention "query my notebook"
- Ask about theory from your books
- Request practice problems
- Need explanation of concepts
- Want architecture context

### When I Use Task Agents

For complex workflows:
- Setting up test environments
- Analyzing multiple files simultaneously
- Complex refactoring
- Building automation scripts

### When I Use Linux Environment

- Running test cases
- Timing solutions
- Git operations
- File management
- Script automation

---

## Speed Optimization Tips

### 1. Parallel Learning
Query NotebookLM while thinking about previous problem

### 2. Template Reuse
Build pattern templates once, modify for each problem

### 3. Automated Testing
```python
# Add to each solution
if __name__ == "__main__":
    test_solution()  # Instant feedback
```

### 4. Spaced Repetition
Let the system schedule reviews automatically

### 5. Claude Collaboration
- Ask me to generate test cases
- Get complexity analysis instantly
- Quick debugging help
- Code review and optimization

---

## Measuring Velocity

### Metrics to Track

Your progress dashboard shows:
- **Problems/day**: Target 2-3 initially, 4-5 after week 3
- **Time/problem**: Should decrease as pattern recognition improves
- **Success rate**: First-attempt solve rate (target >70%)
- **Pattern coverage**: How many patterns have >5 problems
- **Streak**: Consecutive days of practice

### Velocity Indicators

**You're learning fast when:**
- Time per problem decreasing each week
- Recognize patterns within 2-3 minutes
- Solve easy problems in <20 min
- Solve medium problems in <40 min
- Success rate >80% for practiced patterns

**Adjust if:**
- Time per problem increasing → Review fundamentals
- Success rate <50% → Go back to easier problems
- Stuck often → More theory from NotebookLM
- Bored → Skip to harder problems

---

## Next Steps

1. **Now: Set up NotebookLM**
   - Authenticate: "Set up NotebookLM authentication"
   - Add your notebooks: "Add my leetcode notebook to library"

2. **Today: Start Pattern 1**
   - Pick Two Pointers (easiest to start)
   - Query theory
   - Solve 2 easy problems

3. **This Week: Build Momentum**
   - Daily practice
   - Track everything
   - Build the habit

4. **This Month: Master Fundamentals**
   - Complete first 6 patterns
   - 50+ problems solved
   - Strong foundation

---

**Remember**: The system works only if you use it daily. Consistency > intensity.

Let's start! What pattern do you want to master first?
