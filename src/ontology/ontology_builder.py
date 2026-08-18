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
