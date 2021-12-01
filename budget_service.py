from datetime import date, datetime, timedelta
import calendar
class BudgetService:
    def __init__(self) -> None:
        pass

    def query(self, s_date, e_date):
        if s_date > e_date:
            return 0

        if s_date.month == e_date.month:
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_all_budget()[s_date.strftime("%Y%m")] / month_days
            return daily_budget*(e_date.day-s_date.day+1)

        total = 0
        while s_date.strftime("%Y%m") <= e_date.strftime("%Y%m"):            
            month_days = calendar.monthrange(s_date.year, s_date.month)[1]
            daily_budget = self.get_all_budget()[s_date.strftime("%Y%m")] / month_days
            
            if s_date.month < e_date.month:                
                rest_day = (month_days-s_date.day+1)
            else:
                rest_day = (e_date.day)
            print("rest_day", rest_day)
            total += rest_day*daily_budget
            s_date = s_date + timedelta(days=month_days)
        
        return total

    def get_all_budget(self):
        return {"202101":3100,
                "202102":2800,
                "202103":6200}


if __name__ == __name__:
    b = BudgetService()
    print(b.query(date(2021,1,1), date(2021,3,10)))