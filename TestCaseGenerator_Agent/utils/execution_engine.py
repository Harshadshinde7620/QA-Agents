import random


def execute_test_cases(test_cases):
    results = []

    for tc in test_cases:
        # Simulate execution (for now)
        status = random.choice(["Pass", "Fail"])

        # Append result to Actual Result column
        tc[5] = status

        results.append(tc)

    return results