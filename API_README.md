# Test Case Generator Agent - API Support

## Overview
This enhanced test case generator now supports automatic API test case generation and Postman collection creation from API documentation.

## New Features

### 🔍 API Detection
- Automatically detects API-related content in input documents
- Supports various API documentation formats (BRD, PRD, plain text)

### 📋 API Test Case Generation
- Parses API endpoints, methods, parameters, and headers
- Generates comprehensive test cases covering:
  - Happy path scenarios
  - Negative testing
  - Boundary testing
  - Security testing
  - Error handling

### 📮 Postman Collection Generation
- Creates valid Postman v2.1 collections
- Includes pre-configured test scripts for validation
- Supports all HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Includes authentication headers and request bodies

### 🔬 API Test Execution
- Real API testing capabilities using the `requests` library
- Response validation (status codes, JSON structure, response times)
- Comprehensive test reporting

## Usage

### For API Documentation
1. Provide API documentation as text input, PDF, or image
2. The system will:
   - Detect API content
   - Parse endpoints and specifications
   - Generate Postman collection (.postman_collection.json)
   - Execute API tests (if endpoints are accessible)
   - Generate traditional Excel test cases as backup

### Sample API Documentation Format
```
GET /users - Retrieve all users
POST /users - Create new user
  Body: {"name": "string", "email": "string"}
PUT /users/{id} - Update user
DELETE /users/{id} - Delete user
```

## Files Added/Modified

### New Files
- `utils/api_parser.py` - API content detection and parsing
- `utils/postman_builder.py` - Postman collection generation
- `utils/api_execution_engine.py` - API test execution
- `sample_api_docs.txt` - Sample API documentation

### Modified Files
- `main.py` - Added API detection and processing logic
- `agents/test_case_generator.py` - API-specific prompts
- `requirements.txt` - Added requests library

## Output Directory Structure

All generated test cases are saved directly to the `output/` folder:

```
output/
├── {name}_{timestamp}.xlsx                 # Excel test cases
├── {name}_{timestamp}.postman_collection.json  # Postman collections
└── {name}_RTM.xlsx                         # Requirements Traceability Matrix
```

## Dependencies
- requests (for API testing)
- All existing dependencies

## Testing
Run with sample API docs:
```bash
python main.py
# Enter: sample_api_docs.txt (or paste API documentation)
```

## Future Enhancements
- Support for OpenAPI/Swagger specifications
- Integration with more API testing frameworks
- Automated test script generation for various languages
- API mocking capabilities</content>
<parameter name="filePath">d:\AI Tester\Visual Studio Code\TestCaseGenerator_Agent\API_README.md