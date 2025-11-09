"""
Problem Template for DSA Mastery

Usage:
    python scripts/new_problem.py "problem-name" "pattern-name"
"""

TEMPLATE = '''"""
Problem: {problem_name}
Pattern: {pattern}
Difficulty: {difficulty}
Date: {date}

Problem Statement:
{problem_statement}

Examples:
{examples}

Constraints:
{constraints}

Source: {source}
"""

def solution({params}):
    """
    Approach:
    {approach}

    Time Complexity: O({time_complexity})
    Space Complexity: O({space_complexity})

    Pattern Applied: {pattern}
    Key Insights:
    {insights}
    """
    pass


def test_solution():
    """Test cases"""
    test_cases = [
        # (input, expected_output)
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = solution(input_data)
        status = "✓" if result == expected else "✗"
        print(f"Test {{i+1}}: {{status}} | Input: {{input_data}} | Expected: {{expected}} | Got: {{result}}")


if __name__ == "__main__":
    test_solution()
'''

if __name__ == "__main__":
    import sys
    from datetime import datetime

    if len(sys.argv) < 3:
        print("Usage: python scripts/new_problem.py <problem-name> <pattern-name> [difficulty]")
        sys.exit(1)

    problem_name = sys.argv[1]
    pattern = sys.argv[2]
    difficulty = sys.argv[3] if len(sys.argv) > 3 else "medium"

    content = TEMPLATE.format(
        problem_name=problem_name,
        pattern=pattern,
        difficulty=difficulty,
        date=datetime.now().strftime("%Y-%m-%d"),
        problem_statement="[INSERT PROBLEM STATEMENT]",
        examples="[INSERT EXAMPLES]",
        constraints="[INSERT CONSTRAINTS]",
        source="NotebookLM / LeetCode",
        params="",
        approach="[DESCRIBE YOUR APPROACH]",
        time_complexity="?",
        space_complexity="?",
        insights="[KEY INSIGHTS]"
    )

    filename = f"patterns/{pattern}/{problem_name}.py"
    with open(filename, 'w') as f:
        f.write(content)

    print(f"Created: {filename}")
