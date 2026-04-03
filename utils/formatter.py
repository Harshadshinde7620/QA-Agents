def parse_llm_output(output):
    lines = output.strip().split("\n")

    test_cases = []

    for line in lines:
        if "|" in line and "Test Case ID" not in line:
            parts = [p.strip() for p in line.split("|") if p.strip()]

            if len(parts) == 4:
                test_cases.append(parts)

    return test_cases