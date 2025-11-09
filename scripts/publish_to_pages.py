#!/usr/bin/env python3
"""
Publish writeups to GitHub Pages
Converts markdown to beautiful Notion + Linear styled pages
"""

import json
from pathlib import Path
from datetime import datetime


def publish_writeup(writeup_path: str):
    """
    Publish a writeup to GitHub Pages

    Args:
        writeup_path: Path to writeup markdown file
    """
    writeup_file = Path(writeup_path)

    if not writeup_file.exists():
        print(f"❌ Writeup not found: {writeup_path}")
        return False

    # Read writeup content
    with open(writeup_file) as f:
        content = f.read()

    # Extract title from first line
    lines = content.split('\n')
    title = lines[0].replace('#', '').strip() if lines else "Untitled"

    # Determine output path
    pattern_slug = writeup_file.stem.replace('_', '-')
    output_file = Path(f"docs/patterns/{pattern_slug}.md")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Add Jekyll front matter with styling
    front_matter = f"""---
layout: default
title: "{title}"
show_breadcrumb: true
category: "Patterns"
category_url: "/#-pattern-writeups"
---

"""

    # Enhance content with styling classes
    enhanced_content = enhance_markdown(content)

    # Write to docs folder
    with open(output_file, 'w') as f:
        f.write(front_matter)
        f.write(enhanced_content)

    print(f"✅ Published: {output_file}")
    print(f"   URL: /patterns/{pattern_slug}.html")

    # Update index page
    update_index_page(pattern_slug, title)

    return True


def enhance_markdown(content: str) -> str:
    """Add styling classes to markdown content"""
    lines = content.split('\n')
    enhanced = []
    in_code_block = False

    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            enhanced.append(line)
            continue

        # Don't modify code blocks
        if in_code_block:
            enhanced.append(line)
            continue

        # Add card styling to sections
        if line.startswith('## '):
            enhanced.append('<div class="card">')
            enhanced.append('')
            enhanced.append(line)
            # Close previous card
            if enhanced and enhanced[-4] == '</div>':
                pass
            elif len(enhanced) > 1:
                enhanced.insert(-2, '')
                enhanced.insert(-2, '</div>')
                enhanced.insert(-2, '')

        # Add badges for keywords
        line = line.replace('**Easy**', '<span class="badge badge-success">Easy</span>')
        line = line.replace('**Medium**', '<span class="badge badge-warning">Medium</span>')
        line = line.replace('**Hard**', '<span class="badge badge-info">Hard</span>')
        line = line.replace('*Easy*', '<span class="badge badge-success">Easy</span>')
        line = line.replace('*Medium*', '<span class="badge badge-warning">Medium</span>')
        line = line.replace('*Hard*', '<span class="badge badge-info">Hard</span>')

        enhanced.append(line)

    # Close last card if needed
    if enhanced and not enhanced[-1].strip() == '</div>':
        enhanced.append('')
        enhanced.append('</div>')

    return '\n'.join(enhanced)


def update_index_page(pattern_slug: str, pattern_title: str):
    """Update index page with new pattern"""
    index_file = Path("docs/index.md")

    if not index_file.exists():
        print("⚠️  Index file not found")
        return

    with open(index_file) as f:
        content = f.read()

    # Update pattern link status
    pattern_link = f"[{pattern_title}](patterns/{pattern_slug}.html)"
    content = content.replace(
        f"[Two Pointers](patterns/01-two-pointers.html) - *In Progress*",
        f"{pattern_link} - <span class=\"badge badge-success\">Active</span>"
    )

    # Update statistics
    content = content.replace(
        "**Current Pattern**: Two Pointers",
        f"**Current Pattern**: {pattern_title}"
    )

    # Update last modified
    content = content.replace(
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d')}",
        f"*Last Updated: {datetime.now().strftime('%Y-%m-%d')}"
    )

    with open(index_file, 'w') as f:
        f.write(content)

    print(f"✅ Updated index page")


def update_progress_display():
    """Update progress statistics on index page"""
    # Load progress
    progress_file = Path("progress/daily_progress.json")
    if progress_file.exists():
        with open(progress_file) as f:
            progress = json.load(f)

        day = progress.get("day", 0)
        completed = len(progress.get("patterns_completed", []))

        print(f"📊 Progress: Day {day}, {completed} patterns completed")


def main():
    """Publish all writeups"""
    import sys

    if len(sys.argv) > 1:
        # Publish specific writeup
        writeup_path = sys.argv[1]
        publish_writeup(writeup_path)
    else:
        # Publish all writeups
        writeups_dir = Path("writeups")
        if not writeups_dir.exists():
            print("❌ No writeups directory found")
            return

        print("📤 Publishing all writeups to GitHub Pages...\n")

        count = 0
        for writeup_file in writeups_dir.glob("*.md"):
            if publish_writeup(str(writeup_file)):
                count += 1

        print(f"\n✅ Published {count} writeups")
        print("\n📊 Updating progress...")
        update_progress_display()

        print("\n🚀 Ready to push:")
        print("   git add docs/")
        print("   git commit -m 'Published writeups to GitHub Pages'")
        print("   git push")


if __name__ == '__main__':
    main()
