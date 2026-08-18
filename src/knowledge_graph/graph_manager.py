"""Manage knowledge graph operations"""

class KnowledgeGraphManager:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    
    def add_node(self, node_id: str, node_type: str, attributes: dict = None) -> dict:
        """Add node to knowledge graph"""
        node = {
            'id': node_id,
            'type': node_type,
            'attributes': attributes or {}
        }
        self.nodes[node_id] = node
        return node
    
    def get_node(self, node_id: str) -> dict | None:
        """Get node by ID"""
        return self.nodes.get(node_id)

    def delete_node(self, node_id: str) -> bool:
        """Delete node and connected edges"""
        if node_id not in self.nodes:
            return False
        del self.nodes[node_id]
        self.edges = [e for e in self.edges if e['source'] != node_id and e['target'] != node_id]
        return True

    def add_edge(self, source: str, target: str, edge_type: str, edge_id: str = None, weight: float = 1.0, properties: dict = None) -> dict:
        """Add edge to knowledge graph"""
        edge = {
            'id': edge_id or f"{source}_{edge_type}_{target}",
            'source': source,
            'target': target,
            'type': edge_type,
            'weight': weight,
            'properties': properties or {}
        }
        self.edges.append(edge)
        return edge

    def get_neighbors(self, node_id: str) -> list[dict]:
        """Get neighboring nodes and connecting edge info"""
        neighbors = []
        for edge in self.edges:
            if edge['source'] == node_id and edge['target'] in self.nodes:
                neighbors.append({
                    'node': self.nodes[edge['target']],
                    'direction': 'outgoing',
                    'edge_type': edge['type'],
                    'edge_id': edge['id']
                })
            elif edge['target'] == node_id and edge['source'] in self.nodes:
                neighbors.append({
                    'node': self.nodes[edge['source']],
                    'direction': 'incoming',
                    'edge_type': edge['type'],
                    'edge_id': edge['id']
                })
        return neighbors

    def get_statistics(self) -> dict:
        """Calculate summary statistics for the graph"""
        entity_type_counts = {}
        for node in self.nodes.values():
            ntype = node['type']
            entity_type_counts[ntype] = entity_type_counts.get(ntype, 0) + 1

        relationship_type_counts = {}
        for edge in self.edges:
            etype = edge['type']
            relationship_type_counts[etype] = relationship_type_counts.get(etype, 0) + 1

        degree_dict = {}
        for node_id in self.nodes:
            degree_dict[node_id] = 0
        for edge in self.edges:
            if edge['source'] in degree_dict:
                degree_dict[edge['source']] += 1
            if edge['target'] in degree_dict:
                degree_dict[edge['target']] += 1

        avg_degree = (sum(degree_dict.values()) / len(self.nodes)) if self.nodes else 0.0

        return {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'node_type_counts': entity_type_counts,
            'edge_type_counts': relationship_type_counts,
            'average_degree': round(avg_degree, 2)
        }

    def sync_from_ontology(self, ontology_builder) -> None:
        """Sync graph nodes and edges from an OntologyBuilder instance"""
        self.nodes.clear()
        self.edges.clear()
        for entity_id, entity in ontology_builder.entities.items():
            self.add_node(
                node_id=entity_id,
                node_type=entity['type'],
                attributes=entity.get('properties', {})
            )
        for rel in ontology_builder.relationships:
            self.add_edge(
                source=rel['source'],
                target=rel['target'],
                edge_type=rel['type'],
                edge_id=rel.get('id'),
                properties=rel.get('properties', {})
            )

    def clear(self):
        """Clear nodes and edges"""
        self.nodes.clear()
        self.edges.clear()
