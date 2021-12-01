import unittest
from budget_service import BudgetService

class Test_budgetCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_queryBedget(self):        
        self.assertEqual(True, True);


unittest.main(verbosity=2)