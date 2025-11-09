#!/usr/bin/env python3
"""
Automated PR Testing
Runs solution against test cases and provides feedback
"""

import subprocess
import sys
import json
from pathlib import Path


class AutoTester:
    """Automatically test PR solutions against test cases"""

    def __init__(self, problem_file: str):
        self.problem_file = Path(problem_file)
        self.test_results = []

    def extract_test_cases(self):
        """Extract test cases from problem file comments"""
        # Test cases should be in comments like:
        # /* TEST_CASE: input=[1,2,3], expected=6 */

        test_cases = []
        with open(self.problem_file) as f:
            content = f.read()

            # Parse test case comments
            import re
            pattern = r'/\*\s*TEST_CASE:\s*(.+?)\s*\*/'
            matches = re.findall(pattern, content, re.DOTALL)

            for match in matches:
                # Parse test case
                try:
                    # Simple eval for now (in production, use safer parsing)
                    test_case = eval(f"{{{match}}}")
                    test_cases.append(test_case)
                except:
                    print(f"Warning: Could not parse test case: {match}")

        return test_cases

    def run_cargo_test(self):
        """Run cargo test for the problem"""
        print(f"\n🧪 Running tests for {self.problem_file.stem}...")

        try:
            result = subprocess.run(
                ['cargo', 'test', '--', self.problem_file.stem],
                capture_output=True,
                text=True,
                timeout=30
            )

            success = result.returncode == 0

            return {
                'success': success,
                'stdout': result.stdout,
                'stderr': result.stderr
            }

        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Test timed out (>30s) - possible infinite loop or O(n²) on large input'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def analyze_complexity(self):
        """Static analysis of code complexity"""
        with open(self.problem_file) as f:
            code = f.read()

        warnings = []

        # Check for nested loops (potential O(n²))
        if code.count('for') + code.count('while') >= 2:
            # Simple heuristic - count nesting
            lines = code.split('\n')
            indent_stack = []
            max_loop_nesting = 0
            current_nesting = 0

            for line in lines:
                if 'for ' in line or 'while ' in line:
                    current_nesting += 1
                    max_loop_nesting = max(max_loop_nesting, current_nesting)
                elif line.strip().startswith('}'):
                    current_nesting = max(0, current_nesting - 1)

            if max_loop_nesting >= 2:
                warnings.append({
                    'type': 'COMPLEXITY',
                    'severity': 'WARNING',
                    'message': f'Detected {max_loop_nesting} nested loops - verify time complexity'
                })

        # Check for .clone() calls (potential inefficiency)
        if '.clone()' in code:
            warnings.append({
                'type': 'PERFORMANCE',
                'severity': 'INFO',
                'message': 'Using .clone() - verify if necessary or can use borrowing'
            })

        # Check for unwrap() (not production-ready)
        if '.unwrap()' in code:
            warnings.append({
                'type': 'SAFETY',
                'severity': 'INFO',
                'message': 'Using .unwrap() - acceptable for leetcode but handle errors in production'
            })

        return warnings

    def generate_feedback(self, test_result: dict, warnings: list):
        """Generate automated review feedback"""
        feedback = []

        if test_result['success']:
            feedback.append("✅ **All tests passed!**")
        else:
            feedback.append("❌ **Tests failed**")
            if 'error' in test_result:
                feedback.append(f"\nError: {test_result['error']}")
            else:
                feedback.append(f"\n```\n{test_result['stderr']}\n```")

        if warnings:
            feedback.append("\n## Static Analysis")
            for warning in warnings:
                emoji = "⚠️" if warning['severity'] == 'WARNING' else "ℹ️"
                feedback.append(f"{emoji} **{warning['type']}**: {warning['message']}")

        return "\n".join(feedback)

    def run_full_review(self):
        """Run complete automated review"""
        print(f"\n{'='*60}")
        print(f"🤖 AUTOMATED PR REVIEW")
        print(f"{'='*60}\n")

        # Run tests
        test_result = self.run_cargo_test()

        # Static analysis
        warnings = self.analyze_complexity()

        # Generate feedback
        feedback = self.generate_feedback(test_result, warnings)

        print(feedback)

        # Save to file for PR comment
        feedback_file = Path('.pr_feedback.md')
        with open(feedback_file, 'w') as f:
            f.write(feedback)

        return test_result['success']


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 auto_test_pr.py <problem_file.rs>")
        sys.exit(1)

    problem_file = sys.argv[1]

    tester = AutoTester(problem_file)
    success = tester.run_full_review()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
