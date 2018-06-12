from calendar import HTMLCalendar
from flask import url_for


class CustomCalendar(HTMLCalendar):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def month_name(self):
        names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return names[self.month-1]

    def month_toggle(self, direction):
        if direction == "up":
            if self.month == 12:
                return url_for('business_profile', year=self.year+1, month=1, day=0)
            else:
                return url_for('business_profile', year=self.year, month=self.month+1, day=0)
            # Should be return url_for('business_profile', year=self.year, month=self.month+1)
            # ie. I want to pass in the url and the parameters instead of building a string here. But I think
            # the problem might be that the calendar object itself is shared among users and causing the bug? I'm not sure.
        else:
            if self.month == 1:
                return url_for('business_profile', year=self.year-1, month=12, day=0)
            else:
                return url_for('business_profile', year=self.year, month=self.month-1, day=0)

    def year_toggle(self, direction):
        if direction == "up":
            if self.month == 12:
                return self.year+1
            else:
                return self.year
        else:
            if self.month == 1:
                return self.year-1
            else:
                return self.year
