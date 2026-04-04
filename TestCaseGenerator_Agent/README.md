# Test Case Generator Agent

An AI-powered test case generation tool that creates comprehensive test cases from requirements documents.

## Features

- **Multi-format Input**: Supports text, PDF, and image inputs
- **AI-Powered Generation**: Uses LLM to generate structured test cases
- **API Testing Support**: Automatically detects and generates API test cases with Postman collections
- **Quality Assurance**: Applies QA intelligence, deduplication, and coverage validation
- **Multiple Outputs**: Generates Excel test cases, Postman collections, and RTM reports

## Directory Structure

```
TestCaseGenerator_Agent/
├── main.py                    # Main application entry point
├── requirements.txt           # Python dependencies
├── constraints.md            # Generation constraints and rules
├── sample_api_docs.txt       # Sample API documentation
├── API_README.md             # API-specific documentation
├── agents/                   # AI agent modules
├── models/                   # LLM integration
├── utils/                    # Utility modules
├── Assets/                   # Static assets
├── output/                   # Output directory
│   ├── *.xlsx               # Excel test case files
│   ├── *.postman_collection.json  # Postman collections
│   └── *_RTM.xlsx           # Requirements Traceability Matrix
└── .env                      # Environment variables
```

## Usage

```bash
python main.py
```

Enter your requirements as text, or provide a file path to a PDF/image document.

## API Testing

The tool automatically detects API-related content and generates:
- Postman collections for API testing
- Comprehensive API test cases
- Real API execution and validation

See `API_README.md` for detailed API testing documentation.

## Output

All generated files are saved to `output/` with timestamps for uniqueness.