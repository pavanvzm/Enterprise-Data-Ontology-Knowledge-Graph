"""Unit tests for OntologyBuilder, KnowledgeGraphManager, and validators"""

import unittest
from src.ontology.ontology_builder import OntologyBuilder
from src.knowledge_graph.graph_manager import KnowledgeGraphManager
from src.utils.validators import validate_entity, validate_relationship

class TestOntologyBuilderExtended(unittest.TestCase):
    def setUp(self):
        self.builder = OntologyBuilder()

    def test_add_and_get_entity(self):
        self.builder.add_entity('e1', 'Person', {'name': 'Alice'})
        entity = self.builder.get_entity('e1')
        self.assertIsNotNone(entity)
        self.assertEqual(entity['type'], 'Person')
        self.assertEqual(entity['properties']['name'], 'Alice')

    def test_update_entity(self):
        self.builder.add_entity('e1', 'Person', {'name': 'Alice'})
        updated = self.builder.update_entity('e1', entity_type='Employee', properties={'role': 'Engineer'})
        self.assertEqual(updated['type'], 'Employee')
        self.assertEqual(updated['properties']['name'], 'Alice')
        self.assertEqual(updated['properties']['role'], 'Engineer')

    def test_delete_entity_cascades_relationships(self):
        self.builder.add_entity('e1', 'Person')
        self.builder.add_entity('e2', 'Company')
        self.builder.add_relationship('e1', 'e2', 'WORKS_FOR')
        self.assertEqual(len(self.builder.relationships), 1)

        deleted = self.builder.delete_entity('e1')
        self.assertTrue(deleted)
        self.assertIsNone(self.builder.get_entity('e1'))
        self.assertEqual(len(self.builder.relationships), 0)

    def test_list_entities_filter(self):
        self.builder.add_entity('e1', 'Person')
        self.builder.add_entity('e2', 'Company')
        self.builder.add_entity('e3', 'Person')

        persons = self.builder.list_entities(entity_type='Person')
        self.assertEqual(len(persons), 2)


class TestKnowledgeGraphManagerExtended(unittest.TestCase):
    def setUp(self):
        self.kg = KnowledgeGraphManager()

    def test_add_node_and_edge(self):
        self.kg.add_node('n1', 'Customer')
        self.kg.add_node('n2', 'Order')
        self.kg.add_edge('n1', 'n2', 'PLACED')

        self.assertEqual(len(self.kg.nodes), 2)
        self.assertEqual(len(self.kg.edges), 1)

    def test_get_neighbors(self):
        self.kg.add_node('n1', 'Customer')
        self.kg.add_node('n2', 'Order')
        self.kg.add_edge('n1', 'n2', 'PLACED', edge_id='rel1')

        neighbors = self.kg.get_neighbors('n1')
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0]['node']['id'], 'n2')
        self.assertEqual(neighbors[0]['direction'], 'outgoing')

    def test_get_statistics(self):
        self.kg.add_node('n1', 'Customer')
        self.kg.add_node('n2', 'Order')
        self.kg.add_edge('n1', 'n2', 'PLACED')

        stats = self.kg.get_statistics()
        self.assertEqual(stats['total_nodes'], 2)
        self.assertEqual(stats['total_edges'], 1)
        self.assertEqual(stats['node_type_counts']['Customer'], 1)
        self.assertEqual(stats['average_degree'], 1.0)


class TestValidators(unittest.TestCase):
    def test_validate_entity(self):
        valid_e = {'id': 'e1', 'type': 'User'}
        invalid_e = {'id': 'e1'}
        self.assertTrue(validate_entity(valid_e))
        self.assertFalse(validate_entity(invalid_e))

    def test_validate_relationship(self):
        valid_r = {'source': 'e1', 'target': 'e2', 'type': 'KNOWS'}
        invalid_r = {'source': 'e1', 'target': 'e2'}
        self.assertTrue(validate_relationship(valid_r))
        self.assertFalse(validate_relationship(invalid_r))

if __name__ == '__main__':
    unittest.main()
