# Getting Started

## Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

## Installation
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the Application
```bash
python -m uvicorn src.api.app:app --reload
```

Visit http://localhost:8000/docs for API documentation.
