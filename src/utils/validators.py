"""Validation utilities"""

def validate_entity(entity):
    """Validate entity structure"""
    required_fields = ['id', 'type']
    return all(field in entity for field in required_fields)

def validate_relationship(relationship):
    """Validate relationship structure"""
    required_fields = ['source', 'target', 'type']
    return all(field in relationship for field in required_fields)
