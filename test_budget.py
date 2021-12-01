import logging
import unittest
from unittest import mock
from datetime import date

from budget_service import BudgetService
from budget_service import BudgetOjbect


class Test_budgetCase(unittest.TestCase):
    def setUp(self):
        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)
        self.budget_service = BudgetService()                        

    def tearDown(self):
        self.args = None

    def test_query_with_opposite_start_end_date(self):
        fake_budget_list = [BudgetOjbect("202105", 3100)]

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 6), date(2021, 5, 5))
        self.assertEqual(test_result, 0)

    def test_query_with_one_month(self):
        fake_budget_list = [BudgetOjbect("202105", 3100)]

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 1), date(2022, 5, 31))
        self.assertEqual(test_result, 3100)

    def test_query_with_two_month(self):
        fake_budget_list = [BudgetOjbect("202105", 3100),
                            BudgetOjbect("202106", 0)]        

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 1), date(2021, 6, 30))
        self.assertEqual(test_result, 3100)

    def test_query_with_partial_month(self):
        fake_budget_list = [BudgetOjbect("202104", 6000),
                            BudgetOjbect("202105", 3100)] 
        
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 4, 30), date(2021, 5, 2))
        self.assertEqual(test_result, 400)

    def test_query_with_non_existed_month(self):
        fake_budget_list = [BudgetOjbect("202104", 6000)]
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 5, 1), date(2021, 5, 2))
        self.assertEqual(test_result, 0)

    def test_query_with_existed_month_with_zero_budget(self):
        fake_budget_list = [BudgetOjbect("202104", 0)]
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 4, 16), date(2021, 4, 17))
        self.assertEqual(test_result, 0)        

    def test_query_with_partial_two_years(self):
        fake_budget_list = [BudgetOjbect("202105", 3100),
                            BudgetOjbect("202106", 9000),
                            BudgetOjbect("202107", 0),
                            BudgetOjbect("202108", 3100),
                            BudgetOjbect("202109", 6000),
                            BudgetOjbect("202110", 6200),
                            BudgetOjbect("202111", 6000),
                            BudgetOjbect("202112", 6200),
                            BudgetOjbect("202201", 3100)]
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 5, 31), date(2022, 1, 1))
        self.assertEqual(test_result, 36700)

if __name__ == '__main__':
    unittest.main(verbosity=1)
