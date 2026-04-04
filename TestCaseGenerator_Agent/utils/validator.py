def validate_output(output):
    if "Test Case ID" not in output:
        raise ValueError("Invalid format: Missing table header")

    if "[ASSUMPTION]" in output:
        print("⚠️ Assumptions detected in output")

    return output