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
