import os
from models.llm import call_llm
from utils.formatter import parse_llm_output
from utils.excel_writer import save_to_excel
from utils.image_reader import extract_text_from_image
from utils.pdf_reader import extract_text_from_pdf
from utils.validator import validate_output
from utils.qa_intelligence import apply_qa_intelligence
from utils.dedup_coverage import apply_dedup_and_coverage
from utils.coverage_validator import apply_coverage_validation
from utils.execution_engine import execute_test_cases
from utils.report_generator import generate_report

# 🔥 RTM
from utils.rtm_generator import extract_requirements, map_test_cases_to_requirements
from utils.rtm_excel_writer import save_rtm_to_excel

# 🆕 API Support
from utils.api_parser import detect_api_content, parse_api_endpoints
from utils.postman_builder import create_postman_collection, save_collection_to_file
from utils.api_execution_engine import execute_api_test_cases, generate_api_test_report

from agents.test_case_generator import build_prompt


def clean_llm_output(output):
    output = output.replace("```", "")
    return "\n".join([line for line in output.split("\n") if "|" in line])


def get_user_input():
    user_input = input("Enter requirement OR paste file path (image/pdf): ").strip()

    if os.path.isfile(user_input) and user_input.lower().endswith((".png", ".jpg", ".jpeg")):
        return extract_text_from_image(user_input)

    elif os.path.isfile(user_input) and user_input.lower().endswith(".pdf"):
        text = extract_text_from_pdf(user_input)
        print("\n📄 Extracted PRD:\n", text[:1000])
        return text

    return user_input


def generate_file_name(user_input):
    name = user_input.lower().replace(" ", "_")
    name = "".join(c for c in name if c.isalnum() or c == "_")
    return name[:30] if name else "test_cases"


def apply_severity(test_cases):
    for tc in test_cases:
        scenario = tc[1].lower()

        if any(word in scenario for word in ["security", "xss", "sql"]):
            severity = "Critical"
        elif any(word in scenario for word in ["fail", "error", "invalid"]):
            severity = "High"
        else:
            severity = "Medium"

        tc.append(severity)

    return test_cases


def main():
    user_input = get_user_input()

    # 🆕 Check if input contains API content
    api_endpoints = []
    if detect_api_content(user_input):
        print("🔍 API content detected! Generating Postman collection...")

        # Parse API endpoints
        api_endpoints = parse_api_endpoints(user_input)

        if api_endpoints:
            # Generate Postman collection
            collection_name = generate_file_name(user_input)
            collection = create_postman_collection(api_endpoints, collection_name)
            collection_path = save_collection_to_file(collection, collection_name)

            print(f"✅ Postman collection saved at: {collection_path}")
            print(f"📊 Generated {len(api_endpoints)} API test cases")

            # Still generate traditional test cases as backup
            print("\n📋 Also generating traditional test cases...")
        else:
            print("⚠️ API content detected but no endpoints found. Falling back to traditional test case generation.")

    prompt = build_prompt(user_input)

    response = call_llm(prompt)
    cleaned = clean_llm_output(response)

    print("\n🧠 Cleaned Output:\n", cleaned)

    validated = validate_output(cleaned)
    parsed = parse_llm_output(validated)

    if not parsed:
        print("⚠️ No structured test cases found.")
        return

    # 🆕 API-specific execution
    if detect_api_content(user_input) and api_endpoints:
        print("\n🔬 Executing API tests...")
        api_results = execute_api_test_cases(api_endpoints)
        api_report = generate_api_test_report(api_results)

        print("\n📊 API Test Report:")
        print(f"Total Tests: {api_report['total_tests']}")
        print(f"Passed: {api_report['passed']}")
        print(f"Failed: {api_report['failed']}")
        print(".1f")
        print(".1f")

        # Continue with traditional test case processing
        print("\n📋 Processing traditional test cases...")

    enhanced = apply_qa_intelligence(parsed)
    deduped = apply_dedup_and_coverage(enhanced)
    coverage_complete = apply_coverage_validation(deduped)
    final_data = apply_severity(coverage_complete)

    executed = execute_test_cases(final_data)

    # 📊 REPORT
    report = generate_report(executed)
    print("\n📊 Report:")
    for k, v in report.items():
        print(f"{k}: {v}")

    # 💾 SAVE TEST CASES
    file_name = generate_file_name(user_input)
    testcase_path = save_to_excel(executed, file_name)

    print(f"\n✅ Test Cases saved at: {testcase_path}")

    # 🔥 RTM GENERATION
    requirements = extract_requirements(user_input)
    rtm_data = map_test_cases_to_requirements(requirements, executed)

    rtm_path = save_rtm_to_excel(rtm_data, file_name)

    print(f"\n📌 RTM saved at: {rtm_path}")


if __name__ == "__main__":
    main()