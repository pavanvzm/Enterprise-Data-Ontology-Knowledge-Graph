"""Build and manage the enterprise data ontology"""

class OntologyBuilder:
    def __init__(self):
        self.entities = {}
        self.relationships = []
    
    def add_entity(self, entity_id: str, entity_type: str, properties: dict = None) -> dict:
        """Add or overwrite an entity in ontology"""
        entity = {
            'id': entity_id,
            'type': entity_type,
            'properties': properties or {}
        }
        self.entities[entity_id] = entity
        return entity

    def get_entity(self, entity_id: str) -> dict | None:
        """Get an entity by ID"""
        return self.entities.get(entity_id)

    def update_entity(self, entity_id: str, entity_type: str = None, properties: dict = None) -> dict | None:
        """Update an existing entity's type or properties"""
        if entity_id not in self.entities:
            return None
        if entity_type is not None:
            self.entities[entity_id]['type'] = entity_type
        if properties is not None:
            self.entities[entity_id]['properties'].update(properties)
        return self.entities[entity_id]

    def delete_entity(self, entity_id: str) -> bool:
        """Delete an entity and associated relationships"""
        if entity_id not in self.entities:
            return False
        del self.entities[entity_id]
        # Remove relationships involving entity_id
        self.relationships = [
            r for r in self.relationships
            if r['source'] != entity_id and r['target'] != entity_id
        ]
        return True

    def list_entities(self, entity_type: str = None) -> list[dict]:
        """List entities, optionally filtered by type"""
        if entity_type:
            return [e for e in self.entities.values() if e['type'].lower() == entity_type.lower()]
        return list(self.entities.values())
    
    def add_relationship(self, source: str, target: str, relationship_type: str, rel_id: str = None, properties: dict = None) -> dict:
        """Add relationship between entities"""
        rel = {
            'id': rel_id or f"{source}_{relationship_type}_{target}",
            'source': source,
            'target': target,
            'type': relationship_type,
            'properties': properties or {}
        }
        # Avoid duplicate exact relationships
        existing = [
            r for r in self.relationships
            if r['source'] == source and r['target'] == target and r['type'] == relationship_type
        ]
        if not existing:
            self.relationships.append(rel)
            return rel
        else:
            existing[0]['properties'].update(properties or {})
            return existing[0]

    def get_relationship(self, rel_id: str) -> dict | None:
        """Get relationship by ID"""
        for rel in self.relationships:
            if rel.get('id') == rel_id:
                return rel
        return None

    def delete_relationship(self, rel_id: str) -> bool:
        """Delete relationship by ID"""
        initial_len = len(self.relationships)
        self.relationships = [r for r in self.relationships if r.get('id') != rel_id]
        return len(self.relationships) < initial_len

    def list_relationships(self, relationship_type: str = None, source: str = None, target: str = None) -> list[dict]:
        """List relationships with optional filters"""
        results = self.relationships
        if relationship_type:
            results = [r for r in results if r['type'].lower() == relationship_type.lower()]
        if source:
            results = [r for r in results if r['source'] == source]
        if target:
            results = [r for r in results if r['target'] == target]
        return results

    def clear(self):
        """Clear all entities and relationships"""
        self.entities.clear()
        self.relationships.clear()
