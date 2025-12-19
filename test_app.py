"""
Tests for the dummy Python application.
"""

import unittest
from app import greet


class TestGreet(unittest.TestCase):
    """Test cases for the greet function."""
    
    def test_greet_default(self):
        """Test greet with default parameter."""
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greet with a custom name."""
        self.assertEqual(greet("Alice"), "Hello, Alice!")
    
    def test_greet_with_empty_string(self):
        """Test greet with an empty string."""
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
