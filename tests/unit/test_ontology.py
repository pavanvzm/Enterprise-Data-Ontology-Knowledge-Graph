"""Tests for ontology module"""

import unittest
from src.ontology.ontology_builder import OntologyBuilder

class TestOntologyBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = OntologyBuilder()
    
    def test_add_entity(self):
        self.builder.add_entity('e1', 'Person', {'name': 'John'})
        self.assertIn('e1', self.builder.entities)
    
    def test_add_relationship(self):
        self.builder.add_entity('e1', 'Person')
        self.builder.add_entity('e2', 'Organization')
        self.builder.add_relationship('e1', 'e2', 'works_for')
        self.assertEqual(len(self.builder.relationships), 1)

if __name__ == '__main__':
    unittest.main()
