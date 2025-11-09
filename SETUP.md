# Setup Instructions

## System Built ✅

Your DSA Mastery system is ready with:

1. **Rust workspace** - Professional structure
2. **PR template** - Senior-level review format
3. **Workflow documentation** - Optimized for speed
4. **NotebookLM skill** - Installed and ready

## Quick Setup Required

### 1. Install Build Tools
```bash
sudo apt-get update
sudo apt-get install -y build-essential
```

### 2. Verify Rust Works
```bash
cd ~/dsa-mastery
source "$HOME/.cargo/env"
cargo build
cargo test
```

### 3. Set up Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. Set up NotebookLM
In Claude Code:
```
"Set up NotebookLM authentication"
```

Then add your notebooks:
```
"Add my leetcode notebook to library: [URL]"
"Add my algorithm design book to library: [URL]"
"Add my architecture book to library: [URL]"
```

---

## Start Learning

Once setup is complete:

```
"Start pattern 1: Two Pointers"
```

I will:
1. Query your NotebookLM for first principles
2. Create a comprehensive writeup
3. Give you a problem to solve
4. Review your PR as a Google senior interviewer would
5. Iterate until optimal
6. Move to next problem

---

## The System

### File Structure
```
dsa-mastery/
├── src/
│   ├── lib.rs                          # Module declarations
│   └── patterns/
│       └── two_pointers.rs             # Pattern implementations
├── writeups/                           # Pattern writeups (I create these)
├── .github/PULL_REQUEST_TEMPLATE/
│   └── solution_pr.md                  # PR template for solutions
├── Cargo.toml                          # Rust project config
├── SENIOR_WORKFLOW.md                  # Complete workflow guide
└── SETUP.md                            # This file
```

### Workflow Per Problem
1. You solve in `src/patterns/<pattern>/<problem>.rs`
2. Create branch: `git checkout -b pattern/<pattern>/problem-X`
3. Commit & push
4. Create PR using template
5. I review as senior interviewer
6. You optimize based on feedback
7. Merge when optimal
8. Next problem

### My Review Standard
- ✅ PASS: Google L5+ ready
- 🔄 REVISE: Close, needs refinement
- ❌ FAIL: Not senior level

---

## Key Features

### NotebookLM Integration
- Query for theory, problems, explanations
- Source-grounded answers (no hallucinations)
- Your curated resources on-demand

### Senior-Level Feedback
Every review checks:
- Correctness & edge cases
- Optimal complexity with proof
- Clean, idiomatic Rust
- Clear communication
- Trade-off analysis

### Efficiency
- 45-60 min per problem
- 2-3 days per pattern
- 5-7 problems per pattern
- 12 weeks to interview-ready

---

**Goal**: Google Senior Engineer offer
**Timeline**: 12 weeks
**Standard**: Every solution must be interview-ready

Ready to start after setup!
