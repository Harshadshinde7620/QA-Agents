def normalize_text(text):
    return text.lower().strip()


def remove_duplicates(test_cases):
    seen = set()
    unique_cases = []

    for tc in test_cases:
        scenario_key = normalize_text(tc[1])  # Scenario column

        if scenario_key not in seen:
            seen.add(scenario_key)
            unique_cases.append(tc)

    return unique_cases


def ensure_coverage(test_cases):
    scenarios = [tc[1].lower() for tc in test_cases]

    coverage_rules = [
        ("empty input", "Negative"),
        ("invalid input", "Negative"),
        ("boundary", "Edge"),
        ("valid input", "Functional")
    ]

    existing = " ".join(scenarios)

    tc_id_counter = len(test_cases) + 1

    for keyword, test_type in coverage_rules:
        if keyword not in existing:
            test_cases.append([
                f"TC_{tc_id_counter}",
                f"{keyword} scenario",
                "Not specified in requirements",
                "Not specified in requirements",
                "System should handle gracefully",
                "",
                "Medium",
                test_type
            ])
            tc_id_counter += 1

    return test_cases


def apply_dedup_and_coverage(test_cases):
    unique = remove_duplicates(test_cases)
    enhanced = ensure_coverage(unique)
    return enhanced