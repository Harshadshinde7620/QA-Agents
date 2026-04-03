def detect_coverage(test_cases):
    coverage = {
        "functional": False,
        "negative": False,
        "edge": False,
        "security": False,
        "ui": False
    }

    for tc in test_cases:
        scenario = tc[1].lower()

        if "valid" in scenario:
            coverage["functional"] = True

        if any(word in scenario for word in ["invalid", "error", "empty", "fail"]):
            coverage["negative"] = True

        if any(word in scenario for word in ["boundary", "limit", "max", "min"]):
            coverage["edge"] = True

        if any(word in scenario for word in ["security", "xss", "sql", "unauthorized"]):
            coverage["security"] = True

        if any(word in scenario for word in ["ui", "alignment", "responsive"]):
            coverage["ui"] = True

    return coverage


def add_missing_coverage(test_cases, coverage):
    counter = len(test_cases) + 1

    if not coverage["functional"]:
        test_cases.append([
            f"TC_{counter}",
            "Valid input scenario",
            "System ready",
            "Provide valid input; Submit",
            "Operation successful",
            "",
            "Medium",
            "Functional"
        ])
        counter += 1

    if not coverage["negative"]:
        test_cases.append([
            f"TC_{counter}",
            "Invalid input scenario",
            "System ready",
            "Provide invalid input; Submit",
            "Error message displayed",
            "",
            "High",
            "Negative"
        ])
        counter += 1

    if not coverage["edge"]:
        test_cases.append([
            f"TC_{counter}",
            "Boundary input scenario",
            "System ready",
            "Enter max/min values",
            "Handled correctly",
            "",
            "Medium",
            "Edge"
        ])
        counter += 1

    if not coverage["security"]:
        test_cases.append([
            f"TC_{counter}",
            "Security validation",
            "System ready",
            "Attempt unauthorized access",
            "Access denied",
            "",
            "High",
            "Security"
        ])
        counter += 1

    if not coverage["ui"]:
        test_cases.append([
            f"TC_{counter}",
            "UI responsiveness",
            "System loaded",
            "Resize screen",
            "UI adapts correctly",
            "",
            "Low",
            "UI"
        ])
        counter += 1

    return test_cases


def apply_coverage_validation(test_cases):
    coverage = detect_coverage(test_cases)
    return add_missing_coverage(test_cases, coverage)