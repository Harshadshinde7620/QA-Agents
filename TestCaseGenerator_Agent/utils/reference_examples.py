def get_reference_test_cases():
    return """
| Test Case ID | Scenario | Precondition | Steps | Expected Result | Actual result | Priority | Test Case Type |
|--------------|----------|--------------|-------|----------------|---------------|----------|----------------|
| TC_01 | Valid Login | User exists | Enter username; Enter password; Click login | Login successful |  | High | Functional |
| TC_02 | Invalid Password | User exists | Enter username; Enter wrong password; Click login | Error message shown |  | High | Negative |
"""