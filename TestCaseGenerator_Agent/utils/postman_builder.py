import json
import uuid
from typing import Dict, List
from datetime import datetime


def create_postman_collection(api_endpoints: List[Dict], collection_name: str = "Generated API Tests") -> Dict:
    """Create a Postman collection from parsed API endpoints"""

    collection = {
        "info": {
            "name": collection_name,
            "description": "Automatically generated API test collection",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            "created": datetime.now().isoformat(),
            "updated": datetime.now().isoformat()
        },
        "item": [],
        "variable": [
            {
                "key": "baseUrl",
                "value": "https://api.example.com",
                "type": "string"
            }
        ]
    }

    for endpoint in api_endpoints:
        item = create_request_item(endpoint)
        collection["item"].append(item)

    return collection


def create_request_item(endpoint: Dict) -> Dict:
    """Create a Postman request item from endpoint data"""

    method = endpoint.get('method', 'GET')
    path = endpoint.get('path', '/')
    description = endpoint.get('description', 'API test case')

    # Create the request
    request = {
        "method": method,
        "header": create_headers(endpoint.get('headers', [])),
        "url": create_url(path),
        "description": description
    }

    # Add body for POST/PUT/PATCH
    if method in ['POST', 'PUT', 'PATCH']:
        request["body"] = create_request_body(endpoint.get('body'))

    # Create the item
    item = {
        "name": f"{method} {path}",
        "request": request,
        "response": [],
        "event": [
            {
                "listen": "test",
                "script": {
                    "exec": create_test_script(endpoint),
                    "type": "text/javascript"
                }
            }
        ]
    }

    return item


def create_headers(headers: List[Dict]) -> List[Dict]:
    """Create Postman headers from header data"""
    postman_headers = []

    for header in headers:
        postman_headers.append({
            "key": header.get('name', ''),
            "value": header.get('value', ''),
            "description": header.get('description', ''),
            "type": "text"
        })

    # Add default headers if not present
    default_headers = [
        {"key": "Content-Type", "value": "application/json", "type": "text"},
        {"key": "Accept", "value": "application/json", "type": "text"}
    ]

    for default in default_headers:
        if not any(h.get('key') == default['key'] for h in postman_headers):
            postman_headers.append(default)

    return postman_headers


def create_url(path: str) -> Dict:
    """Create Postman URL object"""
    # Remove leading slash if present
    path = path.lstrip('/')

    return {
        "raw": "{{baseUrl}}/" + path,
        "host": ["{{baseUrl}}"],
        "path": path.split('/') if path else []
    }


def create_request_body(body: Dict) -> Dict:
    """Create Postman request body"""
    if not body:
        return {
            "mode": "raw",
            "raw": "{}",
            "options": {
                "raw": {
                    "language": "json"
                }
            }
        }

    if 'example' in body:
        return {
            "mode": "raw",
            "raw": body['example'],
            "options": {
                "raw": {
                    "language": "json"
                }
            }
        }

    return {
        "mode": "raw",
        "raw": json.dumps(body, indent=2),
        "options": {
            "raw": {
                "language": "json"
            }
        }
    }


def create_test_script(endpoint: Dict) -> List[str]:
    """Create Postman test scripts"""
    scripts = [
        "// Basic response validation",
        "pm.test(\"Status code is not 5xx\", function () {",
        "    pm.expect(pm.response.code).to.not.be.oneOf([500, 501, 502, 503, 504, 505]);",
        "});",
        "",
        "pm.test(\"Response time is less than 5000ms\", function () {",
        "    pm.expect(pm.response.responseTime).to.be.below(5000);",
        "});"
    ]

    # Add content-type validation
    if endpoint.get('method') in ['POST', 'PUT', 'PATCH']:
        scripts.extend([
            "",
            "pm.test(\"Content-Type header is present\", function () {",
            "    pm.response.to.have.header(\"Content-Type\");",
            "});"
        ])

    # Add JSON validation for API responses
    scripts.extend([
        "",
        "pm.test(\"Response has valid JSON\", function () {",
        "    try {",
        "        const jsonData = pm.response.json();",
        "        pm.expect(jsonData).to.be.an('object');",
        "    } catch (e) {",
        "        pm.expect.fail('Response is not valid JSON');",
        "    }",
        "});"
    ])

    return scripts


def save_collection_to_file(collection: Dict, filename: str) -> str:
    """Save Postman collection to JSON file"""
    import os
    from datetime import datetime

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(output_dir, f"{filename}_{timestamp}.postman_collection.json")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(collection, f, indent=2, ensure_ascii=False)

    return file_path