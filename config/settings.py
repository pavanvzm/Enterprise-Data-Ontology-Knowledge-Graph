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
