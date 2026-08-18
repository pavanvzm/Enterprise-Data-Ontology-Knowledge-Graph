#!/bin/bash

# Bootstrap script for Enterprise Data Ontology Knowledge Graph

echo "🚀 Starting Enterprise Data Ontology Knowledge Graph project setup..."

# Create directory structure
mkdir -p src/{ontology,knowledge_graph,api,utils}
mkdir -p docs/{design,api,examples}
mkdir -p tests/{unit,integration}
mkdir -p data/{raw,processed,ontology_files}
mkdir -p config
mkdir -p notebooks
mkdir -p scripts
mkdir -p docker

echo "📁 Created directory structure"

# Create Python source files
cat > src/__init__.py << 'EOF'
"""Enterprise Data Ontology Knowledge Graph Package"""
__version__ = "0.1.0"
EOF

cat > src/ontology/__init__.py << 'EOF'
"""Ontology module for knowledge graph management"""
EOF

cat > src/ontology/ontology_builder.py << 'EOF'
"""Build and manage the enterprise data ontology"""

class OntologyBuilder:
    def __init__(self):
        self.entities = {}
        self.relationships = []
    
    def add_entity(self, entity_id, entity_type, properties=None):
        """Add entity to ontology"""
        self.entities[entity_id] = {
            'type': entity_type,
            'properties': properties or {}
        }
    
    def add_relationship(self, source, target, relationship_type):
        """Add relationship between entities"""
        self.relationships.append({
            'source': source,
            'target': target,
            'type': relationship_type
        })
EOF

cat > src/knowledge_graph/__init__.py << 'EOF'
"""Knowledge graph implementation"""
EOF

cat > src/knowledge_graph/graph_manager.py << 'EOF'
"""Manage knowledge graph operations"""

class KnowledgeGraphManager:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node_id, node_type, attributes=None):
        """Add node to knowledge graph"""
        self.nodes[node_id] = {
            'type': node_type,
            'attributes': attributes or {}
        }
    
    def add_edge(self, source, target, edge_type, weight=1.0):
        """Add edge to knowledge graph"""
        self.edges.append({
            'source': source,
            'target': target,
            'type': edge_type,
            'weight': weight
        })
EOF

cat > src/api/__init__.py << 'EOF'
"""API module for knowledge graph access"""
EOF

cat > src/api/app.py << 'EOF'
"""FastAPI application for knowledge graph API"""

from fastapi import FastAPI

app = FastAPI(title="Enterprise Data Ontology Knowledge Graph API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/v1/entities")
def get_entities():
    return {"entities": []}

@app.get("/api/v1/relationships")
def get_relationships():
    return {"relationships": []}
EOF

cat > src/utils/__init__.py << 'EOF'
"""Utility functions"""
EOF

cat > src/utils/validators.py << 'EOF'
"""Validation utilities"""

def validate_entity(entity):
    """Validate entity structure"""
    required_fields = ['id', 'type']
    return all(field in entity for field in required_fields)

def validate_relationship(relationship):
    """Validate relationship structure"""
    required_fields = ['source', 'target', 'type']
    return all(field in relationship for field in required_fields)
EOF

echo "✅ Created Python source files"

# Create configuration files
cat > config/settings.py << 'EOF'
"""Configuration settings for the knowledge graph"""

# Database configuration
DATABASE_URL = "sqlite:///./kg.db"
REDIS_URL = "redis://localhost:6379"

# API configuration
API_TITLE = "Enterprise Data Ontology Knowledge Graph API"
API_VERSION = "0.1.0"
DEBUG = True

# Graph configuration
MAX_DEPTH = 10
CACHE_TTL = 3600
EOF

cat > config/__init__.py << 'EOF'
"""Configuration module"""
EOF

echo "✅ Created configuration files"

# Create test files
cat > tests/__init__.py << 'EOF'
"""Test package"""
EOF

cat > tests/unit/__init__.py << 'EOF'
"""Unit tests"""
EOF

cat > tests/unit/test_ontology.py << 'EOF'
"""Tests for ontology module"""

import unittest
from src.ontology.ontology_builder import OntologyBuilder

class TestOntologyBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = OntologyBuilder()
    
    def test_add_entity(self):
        self.builder.add_entity('e1', 'Person', {'name': 'John'})
        self.assertIn('e1', self.builder.entities)
    
    def test_add_relationship(self):
        self.builder.add_entity('e1', 'Person')
        self.builder.add_entity('e2', 'Organization')
        self.builder.add_relationship('e1', 'e2', 'works_for')
        self.assertEqual(len(self.builder.relationships), 1)

if __name__ == '__main__':
    unittest.main()
EOF

cat > tests/integration/__init__.py << 'EOF'
"""Integration tests"""
EOF

echo "✅ Created test files"

# Create documentation files
cat > docs/README.md << 'EOF'
# Enterprise Data Ontology Knowledge Graph Documentation

## Overview
This project implements a comprehensive enterprise data ontology and knowledge graph system for managing complex business relationships and data structures.

## Features
- Flexible entity and relationship definitions
- RESTful API for graph operations
- Support for multiple data sources
- Graph visualization and analysis tools

## Quick Start
See the [getting-started guide](./getting-started.md) for setup instructions.
EOF

cat > docs/getting-started.md << 'EOF'
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
EOF

cat > docs/design/architecture.md << 'EOF'
# System Architecture

## Components

### Ontology Module
Defines entities, properties, and relationships in the knowledge domain.

### Knowledge Graph Module
Manages the actual graph data structure and relationships.

### API Module
Provides RESTful endpoints for accessing and manipulating the knowledge graph.

### Utilities
Common utilities for validation, transformation, and helper functions.
EOF

echo "✅ Created documentation files"

# Create requirements.txt
cat > requirements.txt << 'EOF'
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
redis==5.0.1
pydantic==2.5.0
pytest==7.4.3
pytest-cov==4.1.0
black==23.12.0
flake8==6.1.0
mypy==1.7.1
EOF

echo "✅ Created requirements.txt"

# Create README.md
cat > README.md << 'EOF'
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
EOF

echo "✅ Created README.md"

# Create .gitignore
cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule file
celerybeat-schedule

# SageMath parsed files
.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Database
*.db
*.sqlite
*.sqlite3

# Redis
dump.rdb

# Docker
docker-compose.override.yml
EOF

echo "✅ Created .gitignore"

# Create docker files
cat > docker/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

cat > docker/docker-compose.yml << 'EOF'
version: '3.8'

services:
  api:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./kg.db
      - REDIS_URL=redis://redis:6379
    volumes:
      - ..:/app
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
EOF

echo "✅ Created Docker configuration"

# Create example script
cat > scripts/load_sample_data.py << 'EOF'
"""Load sample data into the knowledge graph"""

from src.ontology.ontology_builder import OntologyBuilder
from src.knowledge_graph.graph_manager import KnowledgeGraphManager

def main():
    # Initialize managers
    ontology = OntologyBuilder()
    kg = KnowledgeGraphManager()
    
    # Add sample entities
    print("Loading sample data...")
    
    # Add persons
    ontology.add_entity('p1', 'Person', {'name': 'Alice', 'title': 'CEO'})
    ontology.add_entity('p2', 'Person', {'name': 'Bob', 'title': 'Developer'})
    
    # Add organizations
    ontology.add_entity('org1', 'Organization', {'name': 'TechCorp'})
    ontology.add_entity('org2', 'Organization', {'name': 'DataSystems'})
    
    # Add relationships
    ontology.add_relationship('p1', 'org1', 'leads')
    ontology.add_relationship('p2', 'org1', 'works_for')
    ontology.add_relationship('org1', 'org2', 'partners_with')
    
    print(f"✅ Loaded {len(ontology.entities)} entities and {len(ontology.relationships)} relationships")

if __name__ == '__main__':
    main()
EOF

echo "✅ Created example scripts"

# Create .env.example
cat > .env.example << 'EOF'
# Database Configuration
DATABASE_URL=sqlite:///./kg.db

# Redis Configuration
REDIS_URL=redis://localhost:6379

# API Configuration
DEBUG=True
LOG_LEVEL=INFO

# Server Configuration
HOST=0.0.0.0
PORT=8000
EOF

echo "✅ Created .env.example"

# Create GitHub Actions workflow
mkdir -p .github/workflows

cat > .github/workflows/tests.yml << 'EOF'
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest tests/
    - name: Generate coverage report
      run: |
        pytest --cov=src tests/
EOF

echo "✅ Created GitHub Actions workflows"

echo ""
echo "════════════════════════════════════════════════════════════"
echo "✨ Project setup complete!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📦 Created project structure:"
echo "   ✓ Source code (src/)"
echo "   ✓ Tests (tests/)"
echo "   ✓ Documentation (docs/)"
echo "   ✓ Configuration (config/)"
echo "   ✓ Docker setup (docker/)"
echo "   ✓ GitHub Actions workflows (.github/)"
echo ""
echo "📋 Next steps:"
echo "   1. cd /workspaces/Enterprise-Data-Ontology-Knowledge-Graph"
echo "   2. python -m venv venv"
echo "   3. source venv/bin/activate"
echo "   4. pip install -r requirements.txt"
echo "   5. python -m pytest tests/"
echo "   6. python -m uvicorn src.api.app:app --reload"
echo ""
echo "════════════════════════════════════════════════════════════"
