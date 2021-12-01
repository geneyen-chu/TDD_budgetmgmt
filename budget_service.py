from datetime import date, datetime, timedelta
import calendar
import logging

class BudgetOjbect:
    date = ""
    budget = 0
    def __init__(self, date, budget) -> None:
        self.date = date
        self.budget = budget
class BudgetService:
    def __init__(self) -> None:
        # self.budget_list = self.get_all_budget()
        pass

    def query(self, s_date, e_date):
        self.budget_list = self.get_all_budget()
        if s_date > e_date:
            return 0

        if s_date.month == e_date.month:
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_monthly_budget(s_date) / month_days
            return daily_budget*(e_date.day-s_date.day+1)

        total = 0        
        while s_date.strftime("%Y%m") <= e_date.strftime("%Y%m"):                        
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_monthly_budget(s_date) / month_days
            
            if s_date.month < e_date.month:                
                rest_day = (month_days-s_date.day+1)
            else:
                rest_day = (e_date.day)
            logging.debug("---rest_day {}".format(rest_day))
            logging.debug(">>>daily_budget {}".format(daily_budget))
            logging.debug('***total {}'.format(total))
            total += rest_day*daily_budget
            s_date = s_date + timedelta(month_days-s_date.day+1)
        
        return total
    
    def get_monthly_budget(self, date):                
        for item in self.budget_list:
            logging.debug("item {}".format(item))
            if item.date == date.strftime("%Y%m"):                
                return item.budget
        return 0

    def get_all_budget(self):
        return [BudgetOjbect("202104", 6000),
                BudgetOjbect("202105", 3100),
                BudgetOjbect("202106", 3000)] 
           

if __name__ == __name__:
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    b = BudgetService()
    print(b.query(date(2021, 4, 21), date(2021, 6, 30)))
    