from utils.prompt_loader import load_constraints
from utils.reference_examples import get_reference_test_cases
from utils.api_parser import detect_api_content


def build_prompt(user_input):
    constraints = load_constraints()
    examples = get_reference_test_cases()

    # 🆕 Use different prompt for API content
    if detect_api_content(user_input):
        return build_api_prompt(user_input, constraints)
    else:
        return build_general_prompt(user_input, constraints, examples)


def build_general_prompt(user_input, constraints, examples):
    return f"""
ROLE:
You are a QA Automation Expert.

IMPORTANT:
- The input provided is the ONLY source of truth.
- It may contain PRD, UI, API, or plain text.
- You MUST generate test cases from it.
- NEVER say "no data provided"

CONSTRAINTS:
{constraints}

REFERENCE FORMAT:
{examples}

STRICT RULES:
- Output ONLY table
- No explanation
- No markdown
- No extra text

OUTPUT:
| Test Case ID | Scenario | Precondition | Steps | Expected Result | Actual result | Priority | Test Case Type |

INPUT:
{user_input}
"""


def build_api_prompt(user_input, constraints):
    return f"""
ROLE:
You are an API Testing Expert specializing in REST API test case generation.

IMPORTANT:
- Generate comprehensive API test cases covering positive, negative, and edge cases
- Focus on HTTP methods, status codes, request/response validation
- Include authentication, authorization, and security testing
- Cover parameter validation, boundary testing, and error handling

CONSTRAINTS:
{constraints}

API TEST CASE REQUIREMENTS:
- Happy path scenarios (valid requests)
- Negative testing (invalid inputs, missing parameters)
- Boundary testing (min/max values, edge cases)
- Security testing (authentication, authorization)
- Error handling (4xx, 5xx status codes)
- Data validation (required fields, data types)
- Performance considerations (response times)

OUTPUT FORMAT:
| Test Case ID | Scenario | Precondition | Steps | Expected Result | Actual result | Priority | Test Case Type |

STRICT RULES:
- Output ONLY table
- No explanation
- No markdown
- No extra text

INPUT:
{user_input}
"""