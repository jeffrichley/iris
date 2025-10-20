#!/usr/bin/env python3
"""
Safety Policy Checker

Implements risk-based security policy for dependency vulnerabilities:
- Production dependencies: CRITICAL/HIGH blocks merge
- Dev dependencies: CRITICAL/HIGH blocks merge, MEDIUM/LOW warns only
"""

import json
import sys
from pathlib import Path
from typing import Any


def load_safety_report(report_path: Path) -> dict[str, Any]:
    """Load and parse Safety JSON report."""
    with open(report_path) as f:
        return json.load(f)


def classify_dependency(package_name: str, dev_deps: set[str]) -> str:
    """Classify dependency as 'production' or 'development'."""
    return "development" if package_name.lower() in dev_deps else "production"


def get_dev_dependencies() -> set[str]:
    """Extract development dependencies from pyproject.toml."""
    dev_deps = {
        "ruff",
        "mypy",
        "pytest",
        "pytest-cov",
        "coverage",
        "bandit",
        "safety",
        "pre-commit",
        "commitizen",
    }
    return {dep.lower() for dep in dev_deps}


def check_vulnerabilities(report: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Check vulnerabilities against risk-based policy.

    Returns:
        (should_block, warnings): Tuple of blocking status and warning messages
    """
    dev_deps = get_dev_dependencies()
    should_block = False
    warnings = []

    vulnerabilities = report.get("vulnerabilities", [])

    for vuln in vulnerabilities:
        package = vuln.get("package_name", "unknown")
        severity = vuln.get("severity", "UNKNOWN").upper()
        cve = vuln.get("vulnerability_id", "N/A")
        affected_version = vuln.get("analyzed_version", "N/A")
        dep_type = classify_dependency(package, dev_deps)

        # Production dependencies: CRITICAL/HIGH blocks
        if dep_type == "production":
            if severity in ["CRITICAL", "HIGH"]:
                should_block = True
                print(
                    f"❌ BLOCKING: {severity} vulnerability in PRODUCTION dependency"
                )
                print(f"   Package: {package} ({affected_version})")
                print(f"   CVE: {cve}")
                print(
                    "   Policy: Production dependencies must have no "
                    "CRITICAL/HIGH vulnerabilities"
                )
            else:
                warnings.append(
                    f"⚠️  {severity} vulnerability in {package} ({affected_version}) - CVE: {cve}"
                )

        # Dev dependencies: CRITICAL/HIGH blocks, MEDIUM/LOW warns
        elif dep_type == "development":
            if severity in ["CRITICAL", "HIGH"]:
                should_block = True
                print(
                    f"❌ BLOCKING: {severity} vulnerability in DEVELOPMENT dependency"
                )
                print(f"   Package: {package} ({affected_version})")
                print(f"   CVE: {cve}")
                print(
                    "   Policy: Even dev dependencies cannot have CRITICAL/HIGH vulnerabilities"
                )
            else:
                warnings.append(
                    f"⚠️  {severity} vulnerability in DEV dependency "
                    f"{package} ({affected_version}) - CVE: {cve}"
                )
                warnings.append(
                    "   Policy: MEDIUM/LOW in dev dependencies can be "
                    "addressed in follow-up"
                )

    return should_block, warnings


def main() -> int:
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python safety-policy-check.py <safety-report.json>")
        return 1

    report_path = Path(sys.argv[1])

    if not report_path.exists():
        print(f"Error: Report file not found: {report_path}")
        return 1

    report = load_safety_report(report_path)

    print("=" * 60)
    print("Safety Policy Check - Risk-Based Vulnerability Assessment")
    print("=" * 60)

    should_block, warnings = check_vulnerabilities(report)

    # Print warnings
    if warnings:
        print("\nWarnings (non-blocking):")
        for warning in warnings:
            print(warning)

    # Final verdict
    print("\n" + "=" * 60)
    if should_block:
        print("❌ POLICY VIOLATION: Critical vulnerabilities detected")
        print("   Merge blocked until vulnerabilities are resolved")
        print("=" * 60)
        return 1
    elif warnings:
        print("✅ POLICY COMPLIANT: No blocking vulnerabilities")
        print(f"   ({len(warnings)} warnings - can be addressed in follow-up)")
        print("=" * 60)
        return 0
    else:
        print("✅ POLICY COMPLIANT: No vulnerabilities detected")
        print("=" * 60)
        return 0


if __name__ == "__main__":
    sys.exit(main())

