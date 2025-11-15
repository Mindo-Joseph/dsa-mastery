---
layout: default
title: "AI Infrastructure - Skills, Agents & Guardrails"
---

<div class="hero">
  <h1>AI-Enhanced Infrastructure</h1>
  <p class="lead">Production-grade Claude Code infrastructure for automated guidance, quality enforcement, and expert analysis. Built once, adaptable everywhere.</p>
</div>

<div class="section">
  <div class="section-header">
    <h2 class="section-title">Auto-Activating Skills</h2>
    <p class="section-subtitle">Context-aware modules that load exactly when needed, no manual configuration required</p>
  </div>

  <div class="card mb-8">
    <h4 class="card-title">How Skills Activate</h4>
    <div class="grid grid-3 mt-6" style="gap: 24px;">
      <div>
        <h6>File Patterns</h6>
        <code style="display: block; margin-top: 8px;">src/patterns/**/*.rs</code>
        <p class="text-secondary mt-2 mb-0" style="font-size: 0.875rem;">Auto-activates problem-solver when editing pattern files</p>
      </div>
      <div>
        <h6>Keywords</h6>
        <p class="text-secondary" style="font-size: 0.875rem; margin: 8px 0 0 0;">"pattern", "complexity", "optimize", "first principles"</p>
      </div>
      <div>
        <h6>Intent Patterns</h6>
        <p class="text-secondary" style="font-size: 0.875rem; margin: 8px 0 0 0;">"solve this problem", "explain from theory", "is this optimal"</p>
      </div>
    </div>
  </div>

  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-icon" style="background: linear-gradient(135deg, #1a73e8, #4285f4);">
        <span style="filter: grayscale(100%) brightness(10);">🎯</span>
      </div>
      <h3 class="feature-title">problem-solver</h3>
      <p class="feature-description">Comprehensive DSA guidance with pattern recognition, complexity analysis, Rust idioms, testing strategies, and L5+ review standards.</p>
      <div class="mt-4">
        <span class="badge badge-info" style="margin-right: 8px;">Auto-activating</span>
        <span class="text-tertiary" style="font-size: 0.75rem;">~2,000 lines</span>
      </div>
    </div>

    <div class="feature-card">
      <div class="feature-icon" style="background: linear-gradient(135deg, #34a853, #5bb974);">
        <span style="filter: grayscale(100%) brightness(10);">📚</span>
      </div>
      <h3 class="feature-title">gemini-rag-integration</h3>
      <p class="feature-description">Query CLRS, EPI, CTCI directly. Zero hallucinations through document-only responses with citations from authoritative sources.</p>
      <div class="mt-4">
        <span class="badge badge-success" style="margin-right: 8px;">RAG-powered</span>
        <span class="text-tertiary" style="font-size: 0.75rem;">Citation-backed</span>
      </div>
    </div>

    <div class="feature-card">
      <div class="feature-icon" style="background: linear-gradient(135deg, #ea4335, #ff6659);">
        <span style="filter: grayscale(100%) brightness(10);">✅</span>
      </div>
      <h3 class="feature-title">pr-review-standards</h3>
      <p class="feature-description">Google L5+ review automation. PASS ✅ / REVISE 🔄 / FAIL ❌ verdicts with specific action items for correctness, complexity, and quality.</p>
      <div class="mt-4">
        <span class="badge badge-error" style="margin-right: 8px;">L6 Standards</span>
        <span class="text-tertiary" style="font-size: 0.75rem;">Strict enforcement</span>
      </div>
    </div>

    <div class="feature-card">
      <div class="feature-icon" style="background: linear-gradient(135deg, #fbbc04, #ffd666);">
        <span style="filter: grayscale(100%) brightness(10);">🛠️</span>
      </div>
      <h3 class="feature-title">skill-developer</h3>
      <p class="feature-description">Meta-skill for creating custom skills. Teaches modular design, activation rules, progressive disclosure, and multi-project adaptation.</p>
      <div class="mt-4">
        <span class="badge badge-warning" style="margin-right: 8px;">Meta-skill</span>
        <span class="text-tertiary" style="font-size: 0.75rem;">Reusable templates</span>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <h2 class="section-title">AI Specialist Agents</h2>
    <p class="section-subtitle">Autonomous expert agents for deep analysis and rigorous proofs</p>
  </div>

  <div class="grid grid-3">
    <div class="card">
      <h4 class="card-title">pattern-analyzer</h4>
      <p class="card-description">Deep first principles analysis explaining WHY patterns work, not just HOW to implement them.</p>
      <h6 class="mt-6 mb-3">Provides</h6>
      <ul style="font-size: 0.875rem; margin: 0; padding-left: 20px;">
        <li>Pattern identification with justification</li>
        <li>First principles explanation</li>
        <li>Complexity proof</li>
        <li>Similar problem recommendations</li>
        <li>Edge case analysis</li>
      </ul>
    </div>

    <div class="card">
      <h4 class="card-title">complexity-prover</h4>
      <p class="card-description">Rigorous mathematical complexity proofs with tight bounds and optimality arguments.</p>
      <h6 class="mt-6 mb-3">Analyzes</h6>
      <ul style="font-size: 0.875rem; margin: 0; padding-left: 20px;">
        <li>Time complexity (tight bounds)</li>
        <li>Space complexity (auxiliary only)</li>
        <li>Recurrence relations</li>
        <li>Amortized analysis</li>
        <li>Lower bound arguments</li>
      </ul>
    </div>

    <div class="card">
      <h4 class="card-title">rust-reviewer</h4>
      <p class="card-description">Google L6 code review standards for correctness, complexity, quality, and testing.</p>
      <h6 class="mt-6 mb-3">Reviews For</h6>
      <ul style="font-size: 0.875rem; margin: 0; padding-left: 20px;">
        <li>Correctness (all edge cases)</li>
        <li>Optimal complexity (with proof)</li>
        <li>Idiomatic Rust</li>
        <li>Comprehensive testing</li>
        <li>Clear documentation</li>
      </ul>
    </div>
  </div>

  <div class="card mt-8" style="background: var(--grey-50);">
    <h5 class="mb-4">Example Agent Output</h5>
    <pre style="margin: 0; background: var(--white);"><code>## Pattern: Two Pointers

### Why This Pattern
Sorted arrays allow O(1) decisions to eliminate possibilities.
When sum is too high, moving right pointer left can only decrease sum.
This property enables linear search instead of O(n²) brute force.

### Complexity Proof
Time: O(n) - Single pass, each element visited once
- Left pointer moves right ≤ n times
- Right pointer moves left ≤ n times
- Total operations ≤ 2n = O(n)

Space: O(1) - Only two integer pointers

### Verdict: OPTIMAL ✅</code></pre>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <h2 class="section-title">Quality Guardrails</h2>
    <p class="section-subtitle">Automated hooks that enforce engineering standards at every step</p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h4 class="card-title">Git Safety</h4>
      <p class="card-description mb-4">Prevents destructive operations and enforces safe workflows.</p>
      <div class="mt-4">
        <h6 class="mb-3">BLOCKED Operations</h6>
        <div style="display: flex; flex-direction: column; gap: 8px;">
          <code style="display: block; background: rgba(234, 67, 53, 0.05); border-left: 3px solid var(--google-red);">git reset  # Destructive</code>
          <code style="display: block; background: rgba(234, 67, 53, 0.05); border-left: 3px solid var(--google-red);">git clean  # Destructive</code>
          <code style="display: block; background: rgba(234, 67, 53, 0.05); border-left: 3px solid var(--google-red);">git add .  # Use commit-solution.sh</code>
        </div>
      </div>
      <div class="mt-6">
        <h6 class="mb-3">SAFE Alternative</h6>
        <code style="display: block; background: rgba(52, 168, 83, 0.05); border-left: 3px solid var(--google-green);">./scripts/commit-solution.sh "message" file.rs</code>
      </div>
    </div>

    <div class="card">
      <h4 class="card-title">Test Enforcement</h4>
      <p class="card-description mb-4">All tests must pass before any commit is created.</p>
      <div class="mt-4">
        <h6 class="mb-3">Validates</h6>
        <ul style="font-size: 0.875rem; margin: 0; padding-left: 20px;">
          <li>All unit tests pass</li>
          <li>No compilation errors</li>
          <li>Pattern-specific tests succeed</li>
          <li>No failing assertions</li>
        </ul>
      </div>
      <div class="mt-6">
        <h6 class="mb-3">Command</h6>
        <code style="display: block;">cargo test --lib</code>
        <p class="text-tertiary mt-2 mb-0" style="font-size: 0.75rem;">Runs automatically before each commit</p>
      </div>
    </div>

    <div class="card">
      <h4 class="card-title">Complexity Validation</h4>
      <p class="card-description mb-4">Every solution must have documented time and space complexity.</p>
      <div class="mt-4">
        <h6 class="mb-3">Required Format</h6>
        <pre style="margin: 0; background: var(--grey-50);"><code>// Time: O(n)
// Space: O(1)
pub fn two_sum(nums: &[i32]) -> Vec<i32> {
    // implementation
}</code></pre>
      </div>
    </div>

    <div class="card">
      <h4 class="card-title">Skill Activation</h4>
      <p class="card-description mb-4">Suggests relevant skills based on prompt analysis.</p>
      <div class="mt-4">
        <h6 class="mb-3">Triggers On</h6>
        <ul style="font-size: 0.875rem; margin: 0; padding-left: 20px;">
          <li>File patterns (*.rs in patterns/)</li>
          <li>Keywords in prompts</li>
          <li>Intent detection</li>
          <li>Context analysis</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <h2 class="section-title">Minimal Tools Approach</h2>
    <p class="section-subtitle">Context-efficient tools instead of bloated MCP servers</p>
  </div>

  <div class="card">
    <div class="grid grid-2" style="gap: 40px;">
      <div>
        <h4 class="mb-4">gemini-query Tool</h4>
        <p class="text-secondary mb-4">Quick RAG queries to your curated book library</p>
        <pre style="margin: 0;"><code>gemini-query "explain two pointers"
gemini-query "what does CLRS say about DP"
gemini-query "find similar problems"</code></pre>
        <div class="mt-4 mb-0">
          <span class="badge badge-success">< 50 tokens</span>
          <span class="text-tertiary ml-2" style="font-size: 0.75rem;">vs 13,000 for MCP equivalents</span>
        </div>
      </div>
      <div>
        <h4 class="mb-4">Why Not MCP?</h4>
        <ul style="font-size: 0.9375rem; line-height: 1.8;">
          <li>MCP servers add 10,000+ tokens to every request</li>
          <li>Most capabilities are rarely needed</li>
          <li>Simple bash tools are faster and lighter</li>
          <li>Progressive disclosure = better efficiency</li>
        </ul>
        <p class="text-secondary mt-4 mb-0" style="font-size: 0.875rem;">Total context saved: ~10,000+ tokens per session</p>
      </div>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header">
    <h2 class="section-title">Infrastructure Stats</h2>
  </div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value">4</div>
      <div class="stat-label">Active Skills</div>
      <div class="stat-sublabel">~2,000 lines total</div>
    </div>

    <div class="stat-card">
      <div class="stat-value">3</div>
      <div class="stat-label">AI Agents</div>
      <div class="stat-sublabel">~1,500 lines total</div>
    </div>

    <div class="stat-card">
      <div class="stat-value">5</div>
      <div class="stat-label">Guardrail Hooks</div>
      <div class="stat-sublabel">~500 lines total</div>
    </div>

    <div class="stat-card">
      <div class="stat-value">1</div>
      <div class="stat-label">Minimal Tools</div>
      <div class="stat-sublabel">~50 lines total</div>
    </div>
  </div>

  <div class="card mt-8">
    <h4 class="card-title">Skill vs Agent vs Hook</h4>
    <div style="overflow-x: auto;">
      <table>
        <thead>
          <tr>
            <th>Aspect</th>
            <th>Skill</th>
            <th>Agent</th>
            <th>Hook</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>When</strong></td>
            <td>Auto-suggests based on context</td>
            <td>Explicitly invoked</td>
            <td>Runs at events</td>
          </tr>
          <tr>
            <td><strong>How</strong></td>
            <td>Loaded progressively (<500 lines)</td>
            <td>Autonomous task execution</td>
            <td>Shell/TS script</td>
          </tr>
          <tr>
            <td><strong>Purpose</strong></td>
            <td>Provide guidance</td>
            <td>Perform analysis</td>
            <td>Enforce standards</td>
          </tr>
          <tr>
            <td><strong>Example</strong></td>
            <td>Pattern recognition guide</td>
            <td>Deep pattern analysis</td>
            <td>Test validation</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="section">
  <div class="section-header text-center">
    <h2 class="section-title">Reusable Master Template</h2>
    <p class="section-subtitle" style="margin: 0 auto;">Built once, adapt everywhere for any project type</p>
  </div>

  <div class="card" style="background: var(--google-blue-light); border-color: var(--google-blue);">
    <h4 class="mb-4" style="color: var(--google-blue);">Install to Any Project</h4>
    <pre style="margin: 0 0 20px 0; background: var(--white);"><code>cd ~/my-frontend-project
~/.claude-infrastructure-master/scripts/install.sh frontend-dev</code></pre>
    <p class="text-secondary mb-6">Master template location: <code>~/.claude-infrastructure-master/</code></p>

    <h5 class="mb-3">Create New Project Type</h5>
    <ol style="line-height: 1.8; margin-bottom: 24px;">
      <li>Add config: <code>project-configs/my-type.json</code></li>
      <li>Create skills: <code>templates/skills/my-type/</code></li>
      <li>Create agents: <code>templates/agents/my-type/</code></li>
      <li>Install: <code>./scripts/install.sh my-type</code></li>
    </ol>

    <div style="display: flex; gap: 12px; flex-wrap: wrap;">
      <a href="#" class="button-primary">Setup Guide</a>
      <a href="index.html" class="button-secondary">← Back to Home</a>
    </div>
  </div>
</div>

<style>
.ml-2 { margin-left: 8px; }
</style>
