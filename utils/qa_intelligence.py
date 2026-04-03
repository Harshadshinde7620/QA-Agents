def assign_priority_and_type(test_case):
    scenario = test_case[1].lower()

    priority = "Medium"
    test_type = "Functional"

    if any(word in scenario for word in ["error", "invalid", "fail"]):
        test_type = "Negative"
        priority = "High"

    elif any(word in scenario for word in ["boundary", "limit", "max", "min"]):
        test_type = "Edge"

    elif any(word in scenario for word in ["security", "xss", "sql"]):
        test_type = "Security"
        priority = "High"

    return priority, test_type


def apply_qa_intelligence(test_cases):
    enhanced = []

    for tc in test_cases:
        priority, test_type = assign_priority_and_type(tc)

        tc[6] = priority if not tc[6] else tc[6]
        tc[7] = test_type if not tc[7] else tc[7]

        enhanced.append(tc)

    return enhanced