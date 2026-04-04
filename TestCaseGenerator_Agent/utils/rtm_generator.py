import re


def extract_requirements(prd_text):
    """
    Basic requirement extraction from PRD text.
    Splits by numbered points or bullet-like patterns.
    """

    # Split by common patterns: numbers, bullets, sentences
    lines = re.split(r'\n|\.\s|\d+\.\s', prd_text)

    requirements = []
    counter = 1

    for line in lines:
        clean = line.strip()

        if len(clean) > 20:  # filter noise
            requirements.append({
                "id": f"REQ_{counter}",
                "text": clean
            })
            counter += 1

    return requirements


def map_test_cases_to_requirements(requirements, test_cases):
    """
    Map test cases based on keyword matching.
    """

    rtm = []

    for req in requirements:
        matched_tc_ids = []

        for tc in test_cases:
            scenario = tc[1].lower()

            # simple keyword overlap
            if any(word in scenario for word in req["text"].lower().split()):
                matched_tc_ids.append(tc[0])

        rtm.append({
            "Requirement ID": req["id"],
            "Requirement": req["text"],
            "Test Cases": ", ".join(matched_tc_ids) if matched_tc_ids else "Not Covered",
            "Coverage": "Covered" if matched_tc_ids else "Gap"
        })

    return rtm