from datetime import date, datetime, timedelta
import calendar

class BudgetOjbect:
    date = ""
    budget = 0
    def __init__(self, date, budget) -> None:
        self.date = date
        self.budget = budget
class BudgetService:
    def __init__(self) -> None:
        self.budget_list = self.get_all_budget()

    def query(self, s_date, e_date):
        if s_date > e_date:
            return 0

        if s_date.month == e_date.month:
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_monthly_budget(s_date) / month_days
            return daily_budget*(e_date.day-s_date.day+1)

        total = 0
        while s_date.strftime("%Y%m") <= e_date.strftime("%Y%m"):            
            print(s_date.strftime("%Y%m"), e_date.strftime("%Y%m"))
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_monthly_budget(s_date) / month_days
            
            if s_date.month < e_date.month:                
                rest_day = (month_days-s_date.day+1)
            else:
                rest_day = (e_date.day)
            print("rest_day", rest_day)
            print("daily_budget", daily_budget)

            print('total', total)
            total += rest_day*daily_budget
            s_date = s_date + timedelta(days=month_days)
        
        return total
    
    def get_monthly_budget(self, date):                
        for item in self.budget_list:
            if item.date == date.strftime("%Y%m"):
                return item.budget
        return 0

    def get_all_budget(self):
        return [BudgetOjbect("202105", 3100),
                BudgetOjbect("202106", 0)]        

if __name__ == __name__:
    b = BudgetService()
    print(b.query(date(2021, 5, 1), date(2022, 6, 30)))