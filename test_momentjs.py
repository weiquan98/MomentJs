# test_momentjs.py
"""
Tests for MomentJs module.
"""

import unittest
from momentjs import MomentJs

class TestMomentJs(unittest.TestCase):
    """Test cases for MomentJs class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MomentJs()
        self.assertIsInstance(instance, MomentJs)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MomentJs()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
