"""Validation utilities for entities and relationships"""

def validate_entity(entity: dict) -> bool:
    """Validate entity structure. Entity must be a dict containing 'id' (or 'entity_id') and 'type'."""
    if not isinstance(entity, dict):
        return False

    entity_id = entity.get('id') or entity.get('entity_id')
    entity_type = entity.get('type') or entity.get('entity_type')

    if not entity_id or not isinstance(entity_id, str):
        return False
    if not entity_type or not isinstance(entity_type, str):
        return False

    return True

def validate_relationship(relationship: dict) -> bool:
    """Validate relationship structure. Must contain 'source', 'target', and 'type'."""
    if not isinstance(relationship, dict):
        return False

    source = relationship.get('source')
    target = relationship.get('target')
    rel_type = relationship.get('type') or relationship.get('relationship_type')

    if not source or not isinstance(source, str):
        return False
    if not target or not isinstance(target, str):
        return False
    if not rel_type or not isinstance(rel_type, str):
        return False

    return True
