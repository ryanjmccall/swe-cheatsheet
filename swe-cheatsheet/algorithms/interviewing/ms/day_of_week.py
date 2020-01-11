class DayOfWeek(object):
    def __init__(self):
        self.num_to_days = {
            0: 'sun', 1: 'mon', 2: 'tues', 3: 'wed', 4: 'thurs', 5: 'fri', 6: 'sat'
        }
        self.default_year = 2015
        # 2015 5 16 is a thursday
        self.start_day = 4
        self.offset_days = self._get_days_between_same_year_dates(
            year=2015, first_month=1, first_day=1, sec_month=5, sec_day=16
        )
        self.month_to_days = {
            1: 31, 2: 28, 3: 31, 4: 30,
        }

    def get_day_of_week(self, date: str) -> str:
        year, month, day = [str(n) for n in date.split(' ')]
        requested_year_days = self._get_days_between_same_year_dates(year=year, first_month=1, first_day=1,
                                                                     sec_month=month, sec_day=day)
        bw_years = self._get_days_between_years(self.default_year, second_year=year)
        total_days = self.start_day - self.offset_days + bw_years + requested_year_days
        return self.num_to_days[total_days % 7]


    def _get_days_between_years(self, first_year: int, second_year: int) -> int:
        days = 0
        for y in range(first_year, second_year):
            days += 365 if y % 4 else 365
        return days

    def _get_days_between_same_year_dates(
        self, year, first_month: int, first_day: int, sec_month: int, sec_day: int
    ) -> int:
        if first_month == sec_month:
            return sec_day - first_day

        days = self._get_month_days(first_month, year) - first_day
        for month in range(first_month + 1, sec_month):
            days += self._get_month_days(first_month, year)
        return days + sec_day

    def _get_month_days(self, month, year) -> int:
        if month == 2:
            return 29 if year % 4 == 0 else 28
        return self.month_to_days[month]


def test():
    # Given a date, return the day of the week
    dow = DayOfWeek()
    date = '2015 5 16'
    print(dow.get_day_of_week(date))


test()
