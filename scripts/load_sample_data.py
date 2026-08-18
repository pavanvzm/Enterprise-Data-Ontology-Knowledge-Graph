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
