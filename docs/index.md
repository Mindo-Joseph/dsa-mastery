---
layout: default
title: "DSA Mastery"
---

<div class="hero">
  <h1>Data Structures & Algorithms</h1>
  <p class="lead">Twelve weeks. First principles. Google L5+ engineering standards.</p>
  <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
    <a href="#progress" class="button-primary">View Progress</a>
    <a href="infrastructure.html" class="button-secondary">Infrastructure</a>
  </div>
</div>

<div class="section" id="progress">
  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-value" id="stat-days">—</div>
      <div class="stat-label">Days</div>
    </div>

    <div class="stat-card">
      <div class="stat-value" id="stat-problems">—</div>
      <div class="stat-label">Problems</div>
    </div>

    <div class="stat-card">
      <div class="stat-value" id="stat-streak">—</div>
      <div class="stat-label">Streak</div>
    </div>

    <div class="stat-card">
      <div class="stat-value" id="stat-writeups">—</div>
      <div class="stat-label">Writeups</div>
    </div>
  </div>

  <div class="card mt-12">
    <h4 class="card-title" id="current-pattern-title">Two Pointers</h4>
    <div class="progress-bar">
      <div class="progress-fill" id="pattern-progress" style="width: 0%"></div>
    </div>
    <p style="font-size: 15px; color: var(--text-tertiary); margin: 16px 0 0 0;">
      <span id="patterns-completed">0</span> of <span id="total-patterns">15</span> patterns complete
    </p>
  </div>
</div>

<div class="section">
  <h2>Infrastructure</h2>
  <p class="section-subtitle">Production-grade Claude Code infrastructure with auto-activating skills, AI specialist agents, and automated quality enforcement.</p>

  <div class="feature-grid">
    <div class="feature-card">
      <div class="feature-icon">🎯</div>
      <h3 class="feature-title">Auto-Activating Skills</h3>
      <p class="feature-description">Context-aware guidance that loads on demand. Pattern recognition, complexity analysis, and review standards — exactly when needed.</p>
    </div>

    <div class="feature-card">
      <div class="feature-icon">🤖</div>
      <h3 class="feature-title">Specialist Agents</h3>
      <p class="feature-description">Pattern analyzer explains why algorithms work. Complexity prover delivers rigorous proofs. Rust reviewer enforces L6 standards.</p>
    </div>

    <div class="feature-card">
      <div class="feature-icon">🛡️</div>
      <h3 class="feature-title">Quality Guardrails</h3>
      <p class="feature-description">Tests must pass. Complexity must be proven. Git operations must be safe. Automation enforces engineering discipline.</p>
    </div>

    <div class="feature-card">
      <div class="feature-icon">📚</div>
      <h3 class="feature-title">Zero Hallucination RAG</h3>
      <p class="feature-description">Query CLRS, EPI, and CTCI directly. Every answer comes with citations. No speculation, only authoritative sources.</p>
    </div>
  </div>
</div>

<div class="section">
  <h2>Patterns</h2>
  <p class="section-subtitle">Fifteen core patterns. Hundreds of problems. One systematic approach.</p>

  <div class="pattern-list">
    <a href="patterns/two-pointers.html" class="pattern-card">
      <div>
        <div class="pattern-title">Two Pointers</div>
        <div class="pattern-meta">Opposite ends · Same direction · Fast and slow</div>
      </div>
      <span class="badge badge-info">Active</span>
    </a>

    <a href="patterns/sliding-window.html" class="pattern-card">
      <div>
        <div class="pattern-title">Sliding Window</div>
        <div class="pattern-meta">Fixed size · Variable size · Optimization</div>
      </div>
      <span class="badge badge-warning">Next</span>
    </a>

    <a href="patterns/binary-search.html" class="pattern-card">
      <div>
        <div class="pattern-title">Binary Search</div>
        <div class="pattern-meta">Classic · Rotated · Search space</div>
      </div>
      <span class="badge">Locked</span>
    </a>

    <a href="patterns.html" class="pattern-card">
      <div>
        <div class="pattern-title">View all patterns</div>
        <div class="pattern-meta">Fast & Slow · Islands · Trees · Graphs · DP</div>
      </div>
      <span style="color: var(--accent); font-weight: 600;">→</span>
    </a>
  </div>
</div>

<div class="section">
  <h2>Workflow</h2>
  <p class="section-subtitle">Automated end-to-end. From problem selection to production-ready code.</p>

  <div class="grid grid-2">
    <div class="card">
      <h5 style="color: var(--text-tertiary); font-size: 14px; margin-bottom: 12px;">01 — SELECT</h5>
      <h4 style="margin: 0 0 8px 0;">Choose problem from catalog</h4>
      <p style="font-size: 15px; margin: 0;">Gemini RAG provides first principles from CLRS. Theory before implementation.</p>
    </div>

    <div class="card">
      <h5 style="color: var(--text-tertiary); font-size: 14px; margin-bottom: 12px;">02 — IMPLEMENT</h5>
      <h4 style="margin: 0 0 8px 0;">Write idiomatic Rust solution</h4>
      <p style="font-size: 15px; margin: 0;">Skills auto-activate. Comprehensive tests. Complexity with proof.</p>
    </div>

    <div class="card">
      <h5 style="color: var(--text-tertiary); font-size: 14px; margin-bottom: 12px;">03 — VALIDATE</h5>
      <h4 style="margin: 0 0 8px 0;">Safe commit with guardrails</h4>
      <p style="font-size: 15px; margin: 0;">Tests enforced. Complexity validated. Git safety automatic.</p>
    </div>

    <div class="card">
      <h5 style="color: var(--text-tertiary); font-size: 14px; margin-bottom: 12px;">04 — REVIEW</h5>
      <h4 style="margin: 0 0 8px 0;">L6 code review verdict</h4>
      <p style="font-size: 15px; margin: 0;">PASS, REVISE, or FAIL. Specific action items. Production standards.</p>
    </div>
  </div>
</div>

<div class="section">
  <h2>Standards</h2>
  <p class="section-subtitle">Every solution meets Google L5+ quality bar.</p>

  <div class="grid grid-2">
    <div class="card">
      <h4 class="card-title">Optimal complexity</h4>
      <p style="margin: 0; font-size: 15px; color: var(--text-secondary);">Time and space with rigorous proofs. Lower bounds for optimality. No hand-waving.</p>
    </div>

    <div class="card">
      <h4 class="card-title">Production code</h4>
      <p style="margin: 0; font-size: 15px; color: var(--text-secondary);">Idiomatic Rust. Clean, maintainable, documented. Interview-ready implementations.</p>
    </div>

    <div class="card">
      <h4 class="card-title">Comprehensive testing</h4>
      <p style="margin: 0; font-size: 15px; color: var(--text-secondary);">Edge cases. Boundary values. Property tests. 95%+ coverage standard.</p>
    </div>

    <div class="card">
      <h4 class="card-title">First principles</h4>
      <p style="margin: 0; font-size: 15px; color: var(--text-secondary);">WHY patterns work, not just HOW. Theory-backed. Deep understanding.</p>
    </div>
  </div>
</div>

<div class="section">
  <div class="card" style="background: var(--surface); border: none; padding: 48px 32px;">
    <div style="max-width: 640px; margin: 0 auto; text-align: center;">
      <h3 style="margin: 0 0 16px 0;">Reusable Infrastructure</h3>
      <p style="margin: 0 auto 32px; max-width: 55ch;">
        This system adapts to any project type. The master template at
        <code style="font-size: 14px;">~/.claude-infrastructure-master/</code>
        installs skills, agents, and hooks for DSA, frontend, systems, or research.
      </p>
      <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
        <a href="https://github.com/yourusername/dsa-mastery" class="button-primary">View Repository</a>
        <a href="infrastructure.html" class="button-secondary">Documentation</a>
      </div>
    </div>
  </div>
</div>

<script>
// Load and display progress stats
(async function() {
  try {
    const response = await fetch('data/progress.json');
    const data = await response.json();

    // Animate numbers
    function animateValue(id, end) {
      const el = document.getElementById(id);
      const duration = 1200;
      const start = 0;
      const startTime = performance.now();

      function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(1 - progress, 3); // ease-out cubic
        const current = Math.floor(start + (end - start) * easeProgress);
        el.textContent = current;

        if (progress < 1) {
          requestAnimationFrame(update);
        } else {
          el.textContent = end;
        }
      }

      requestAnimationFrame(update);
    }

    // Update stats with animation
    animateValue('stat-days', data.days);
    animateValue('stat-problems', data.problems_solved);
    animateValue('stat-streak', data.streak);
    animateValue('stat-writeups', data.writeups);

    // Update pattern progress
    document.getElementById('current-pattern-title').textContent = data.current_pattern || 'Two Pointers';
    document.getElementById('patterns-completed').textContent = data.patterns_completed || 0;
    document.getElementById('total-patterns').textContent = data.total_patterns || 15;

    const progressPercent = ((data.patterns_completed || 0) / (data.total_patterns || 15)) * 100;
    setTimeout(() => {
      document.getElementById('pattern-progress').style.width = progressPercent + '%';
    }, 200);

  } catch (err) {
    // Graceful degradation if data unavailable
    ['stat-days', 'stat-problems', 'stat-streak', 'stat-writeups'].forEach(id => {
      document.getElementById(id).textContent = '0';
    });
  }
})();

// Mouse tracking for feature cards
document.querySelectorAll('.feature-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    card.style.setProperty('--mouse-x', x + '%');
    card.style.setProperty('--mouse-y', y + '%');
  });
});
</script>
