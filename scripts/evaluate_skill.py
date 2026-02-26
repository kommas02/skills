#!/usr/bin/env python3
"""
Skill Evaluation Runner

This script runs evaluation cases for skills and reports results.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List


def load_evaluation_case(case_path: Path) -> Dict[str, Any]:
    """Load an evaluation case from a JSON file."""
    with open(case_path, 'r') as f:
        return json.load(f)


def load_evaluation_config(config_path: Path) -> Dict[str, Any]:
    """Load evaluation configuration."""
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}


def evaluate_case(case: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluate a single test case.
    
    This is a placeholder for actual evaluation logic.
    In a real implementation, this would:
    1. Run the skill with the input prompt
    2. Compare the output to expected_output
    3. Calculate metrics
    """
    result = {
        'case_id': case.get('id', 'unknown'),
        'case_name': case.get('name', 'unknown'),
        'passed': True,
        'metrics': case.get('metrics', {}),
        'notes': 'Placeholder evaluation - implement actual LLM-based evaluation'
    }
    return result


def evaluate_skill(skill_path: Path, verbose: bool = False) -> Dict[str, Any]:
    """Evaluate all cases for a skill."""
    skill_name = skill_path.name
    eval_dir = skill_path / 'evaluation'
    
    if not eval_dir.exists():
        return {
            'skill_name': skill_name,
            'has_evaluation': False,
            'error': 'No evaluation directory found'
        }
    
    cases_dir = eval_dir / 'cases'
    if not cases_dir.exists():
        return {
            'skill_name': skill_name,
            'has_evaluation': False,
            'error': 'No evaluation/cases directory found'
        }
    
    config = load_evaluation_config(eval_dir / 'config.json')
    
    case_files = sorted(cases_dir.glob('*.json'))
    if not case_files:
        return {
            'skill_name': skill_name,
            'has_evaluation': False,
            'error': 'No evaluation case files found'
        }
    
    min_cases = config.get('min_required_cases', 2)
    if len(case_files) < min_cases:
        return {
            'skill_name': skill_name,
            'has_evaluation': True,
            'passed': False,
            'error': f'Only {len(case_files)} cases found, minimum {min_cases} required'
        }
    
    results = []
    for case_file in case_files:
        case = load_evaluation_case(case_file)
        result = evaluate_case(case)
        results.append(result)
        if verbose:
            print(f"  Case {result['case_id']}: {'PASSED' if result['passed'] else 'FAILED'}")
    
    all_passed = all(r.get('passed', True) for r in results)
    
    return {
        'skill_name': skill_name,
        'has_evaluation': True,
        'passed': all_passed,
        'case_count': len(case_files),
        'results': results
    }


def find_all_skills(base_path: Path) -> List[Path]:
    """Find all skill directories."""
    skills = []
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            skill_md = item / 'SKILL.md'
            if skill_md.exists():
                skills.append(item)
    return skills


def main():
    parser = argparse.ArgumentParser(description='Run skill evaluations')
    parser.add_argument('path', nargs='?', help='Path to skill directory or skills/')
    parser.add_argument('--all', action='store_true', help='Evaluate all skills')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--output', '-o', help='Output results to JSON file')
    
    args = parser.parse_args()
    
    base_path = Path('skills')
    
    if args.all:
        skills = find_all_skills(base_path)
        print(f"Found {len(skills)} skills to evaluate")
        
        all_results = []
        for skill in skills:
            if args.verbose:
                print(f"\nEvaluating {skill.name}...")
            result = evaluate_skill(skill, args.verbose)
            all_results.append(result)
        
        passed = sum(1 for r in all_results if r.get('passed', False))
        failed = sum(1 for r in all_results if not r.get('passed', True))
        no_eval = sum(1 for r in all_results if not r.get('has_evaluation', False))
        
        print(f"\n=== Summary ===")
        print(f"Total skills: {len(all_results)}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"No evaluation: {no_eval}")
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(all_results, f, indent=2)
            print(f"\nResults written to {args.output}")
        
        sys.exit(0 if failed == 0 else 1)
    
    elif args.path:
        skill_path = Path(args.path)
        if not skill_path.exists():
            print(f"Error: Path {args.path} does not exist")
            sys.exit(2)
        
        if skill_path.is_dir():
            result = evaluate_skill(skill_path, args.verbose)
            
            if not result.get('has_evaluation', False):
                print(f"No evaluation found for {result['skill_name']}")
                print(f"Reason: {result.get('error', 'Unknown')}")
                sys.exit(1)
            
            print(f"\n=== {result['skill_name']} ===")
            print(f"Cases: {result['case_count']}")
            print(f"Passed: {result.get('passed', False)}")
            
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(result, f, indent=2)
                print(f"\nResults written to {args.output}")
            
            sys.exit(0 if result.get('passed', False) else 1)
        else:
            print(f"Error: {args.path} is not a directory")
            sys.exit(2)
    else:
        parser.print_help()
        sys.exit(2)


if __name__ == '__main__':
    main()
