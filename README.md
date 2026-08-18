# Enterprise Data Ontology Knowledge Graph

A comprehensive enterprise data ontology and knowledge graph system for managing complex business data structures and relationships.

## Project Overview

This project provides a flexible framework for:
- Defining enterprise data ontologies
- Building and managing knowledge graphs
- Querying relationships and entities
- Visualizing data structures

## Features

- 🏗️ Modular architecture with clear separation of concerns
- 🔗 Flexible entity and relationship definitions
- 🌐 RESTful API for programmatic access
- 📊 Support for complex business relationships
- 🧪 Comprehensive test coverage
- 📚 Detailed documentation

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd Enterprise-Data-Ontology-Knowledge-Graph

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API

```bash
python -m uvicorn src.api.app:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
.
├── src/                       # Source code
│   ├── ontology/             # Ontology definitions
│   ├── knowledge_graph/       # Knowledge graph implementation
│   ├── api/                  # REST API
│   └── utils/                # Utility functions
├── tests/                    # Test suite
│   ├── unit/                 # Unit tests
│   └── integration/          # Integration tests
├── docs/                     # Documentation
│   ├── design/               # Design documents
│   ├── api/                  # API documentation
│   └── examples/             # Usage examples
├── data/                     # Data files
├── config/                   # Configuration
├── notebooks/                # Jupyter notebooks
├── scripts/                  # Utility scripts
├── docker/                   # Docker configuration
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/unit/test_ontology.py
```

### Code Quality

```bash
# Format code
black src tests

# Check code style
flake8 src tests

# Type checking
mypy src
```

## API Endpoints

### Health Check
- `GET /health` - Check API health status

### Entities
- `GET /api/v1/entities` - Get all entities
- `POST /api/v1/entities` - Create new entity
- `GET /api/v1/entities/{id}` - Get entity by ID
- `PUT /api/v1/entities/{id}` - Update entity
- `DELETE /api/v1/entities/{id}` - Delete entity

### Relationships
- `GET /api/v1/relationships` - Get all relationships
- `POST /api/v1/relationships` - Create new relationship
- `GET /api/v1/relationships/{id}` - Get relationship by ID

## Contributing

1. Create a feature branch
2. Make your changes
3. Write tests
4. Submit a pull request

## License

See LICENSE file for details.

## Support

For issues and questions, please open an issue on GitHub.
