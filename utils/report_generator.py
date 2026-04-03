def generate_report(test_cases):
    total = len(test_cases)
    passed = sum(1 for tc in test_cases if tc[5] == "Pass")
    failed = sum(1 for tc in test_cases if tc[5] == "Fail")

    report = {
        "Total": total,
        "Passed": passed,
        "Failed": failed,
        "Pass %": round((passed / total) * 100, 2) if total > 0 else 0
    }

    return report