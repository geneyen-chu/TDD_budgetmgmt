import unittest
from unittest import mock
from datetime import date

from budget_service import BudgetService
from budget_service import BudgetOjbect


class Test_budgetCase(unittest.TestCase):
    def setUp(self):
        self.budget_service = BudgetService()
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_query_with_opposite_start_end_date_should_return_zero_budget(self):
        fake_budget_list = [BudgetOjbect("202105", 3100)]

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 6), date(2022, 5, 5))
        self.assertEqual(test_result, 0)

    def test_query_with_one_month_should_return_correct_budget(self):
        fake_budget_list = [BudgetOjbect("202105", 3100)]

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 1), date(2022, 5, 31))
        self.assertEqual(test_result, 3100)

    def test_query_with_two_month_should_return_correct_budget(self):
        fake_budget_list = [BudgetOjbect("202105", 3100),
                            BudgetOjbect("202106", 0)]        

        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value

        test_result = self.budget_service.query(date(2021, 5, 1), date(2022, 6, 30))
        self.assertEqual(test_result, 3100)

    def test_query_with_partial_month_should_return_correct_budget(self):
        fake_budget_list = [BudgetOjbect("202104", 6000),
                            BudgetOjbect("202105", 3100)] 
        
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 4, 31), date(2022, 5, 2))
        self.assertEqual(test_result, 400)

    def test_query_with_non_existed_month_should_return_zero_budget(self):
        fake_budget_list = [BudgetOjbect("202104", 6000)]
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 5, 1), date(2022, 5, 2))
        self.assertEqual(test_result, 0)

    def test_query_with_existed_month_with_zero_budget_should_return_zero_budget(self):
        fake_budget_list = [BudgetOjbect("202104", 0)]
        self.budget_service.get_all_budget = mock.Mock(return_value=fake_budget_list)
        self.result = self.budget_service.get_all_budget.return_value
        test_result = self.budget_service.query(date(2021, 4, 16), date(2022, 4, 17))
        self.assertEqual(test_result, 0)        

    def test_queryBudget(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
