import json
import re
from typing import Dict, List, Optional


def detect_api_content(text: str) -> bool:
    """Detect if input contains API-related content"""
    api_indicators = [
        r'endpoint', r'api', r'rest', r'http', r'get|post|put|delete|patch',
        r'json', r'xml', r'request', r'response', r'header', r'parameter',
        r'authentication', r'token', r'bearer', r'oauth', r'url|uri'
    ]

    text_lower = text.lower()
    return any(re.search(indicator, text_lower) for indicator in api_indicators)


def parse_api_endpoints(text: str) -> List[Dict]:
    """Parse API endpoints from text/BRD"""
    endpoints = []

    # Look for common API documentation patterns
    endpoint_patterns = [
        r'\*\*(\w+)\s+(/[\w/-]+)\*\*',  # **GET /users**
        r'(\w+)\s+(/[\w/-]+)',  # GET /users
        r'Endpoint:\s*(\w+)\s+(/[\w/-]+)',  # Endpoint: GET /users
        r'API:\s*(/[\w/-]+)\s*\((\w+)\)',  # API: /users (GET)
    ]

    for pattern in endpoint_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if len(match) == 2:
                method, path = match
            else:
                method, path = match[1], match[0]

            endpoints.append({
                'method': method.upper(),
                'path': path,
                'description': extract_description(text, path),
                'parameters': extract_parameters(text, path),
                'headers': extract_headers(text, path),
                'body': extract_request_body(text, path)
            })

    return endpoints


def extract_description(text: str, endpoint: str) -> str:
    """Extract description for an endpoint"""
    # Look for text after endpoint definition
    pattern = rf'{re.escape(endpoint)}\s*[:\-]?\s*([^\n\r]+)'
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else "API endpoint test"


def extract_parameters(text: str, endpoint: str) -> List[Dict]:
    """Extract parameters for an endpoint"""
    params = []

    # Look for parameter definitions near the endpoint
    param_patterns = [
        r'param(?:eter)?\s*:\s*(\w+)\s*\((\w+)\)\s*-\s*([^\n\r]+)',
        r'(\w+)\s*\((\w+)\)\s*:\s*([^\n\r]+)',
    ]

    for pattern in param_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if len(match) == 3:
                name, param_type, description = match
                params.append({
                    'name': name,
                    'type': param_type,
                    'description': description.strip(),
                    'required': 'required' in description.lower()
                })

    return params


def extract_headers(text: str, endpoint: str) -> List[Dict]:
    """Extract headers for an endpoint"""
    headers = []

    # Common headers
    header_patterns = [
        r'Authorization:\s*Bearer',
        r'Content-Type:\s*application/json',
        r'Accept:\s*application/json'
    ]

    for pattern in header_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            header_name = pattern.split(':')[0]
            header_value = pattern.split(':')[1].strip()
            headers.append({
                'name': header_name,
                'value': header_value,
                'description': f"{header_name} header"
            })

    return headers


def extract_request_body(text: str, endpoint: str) -> Optional[Dict]:
    """Extract request body schema"""
    # Look for JSON examples or schema definitions
    json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
    match = re.search(json_pattern, text)

    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return {"example": match.group()}

    return None