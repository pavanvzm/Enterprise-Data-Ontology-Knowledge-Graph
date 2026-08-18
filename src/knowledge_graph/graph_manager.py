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
