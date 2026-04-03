import requests
import json
import time
from typing import Dict, List, Tuple


def execute_api_test_cases(endpoints: List[Dict], base_url: str = "https://jsonplaceholder.typicode.com") -> List[Tuple]:
    """
    Execute API test cases against real endpoints
    Returns list of (endpoint, status, response_time, result)
    """
    results = []

    for endpoint in endpoints:
        try:
            result = execute_single_api_call(endpoint, base_url)
            results.append(result)
        except Exception as e:
            results.append((endpoint, "Error", 0, f"Execution failed: {str(e)}"))

    return results


def execute_single_api_call(endpoint: Dict, base_url: str) -> Tuple:
    """Execute a single API call and return results"""

    method = endpoint.get('method', 'GET')
    path = endpoint.get('path', '/')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    # Construct full URL
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"

    # Prepare request
    request_kwargs = {
        'headers': headers,
        'timeout': 10
    }

    # Add body for applicable methods
    if method in ['POST', 'PUT', 'PATCH'] and body:
        if isinstance(body, dict):
            request_kwargs['json'] = body
        else:
            request_kwargs['data'] = body

    # Execute request
    start_time = time.time()

    try:
        response = requests.request(method, url, **request_kwargs)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        # Determine test result
        result = determine_test_result(response, endpoint)

        return (endpoint, response.status_code, response_time, result)

    except requests.exceptions.RequestException as e:
        response_time = (time.time() - start_time) * 1000
        return (endpoint, "Connection Error", response_time, f"Request failed: {str(e)}")


def determine_test_result(response, endpoint: Dict) -> str:
    """Determine if the API test passed or failed based on response"""

    # Basic validations
    if response.status_code >= 500:
        return "Fail - Server Error"

    if response.status_code >= 400:
        return "Fail - Client Error"

    if response.status_code >= 200 and response.status_code < 300:
        # Additional validations for successful responses
        try:
            if response.headers.get('content-type', '').startswith('application/json'):
                json_data = response.json()
                # Check if response has expected structure (basic check)
                if isinstance(json_data, (dict, list)):
                    return "Pass"
                else:
                    return "Fail - Invalid JSON structure"
            else:
                return "Pass"
        except json.JSONDecodeError:
            return "Fail - Invalid JSON response"
    else:
        return f"Fail - Unexpected status code: {response.status_code}"


def generate_api_test_report(results: List[Tuple]) -> Dict:
    """Generate a summary report for API test execution"""

    total_tests = len(results)
    passed = sum(1 for _, _, _, result in results if result.startswith("Pass"))
    failed = total_tests - passed

    total_response_time = sum(result[2] for result in results if isinstance(result[2], (int, float)))
    avg_response_time = total_response_time / total_tests if total_tests > 0 else 0

    return {
        "total_tests": total_tests,
        "passed": passed,
        "failed": failed,
        "pass_rate": (passed / total_tests * 100) if total_tests > 0 else 0,
        "average_response_time": avg_response_time,
        "results": results
    }