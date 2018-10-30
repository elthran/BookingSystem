from calendar import HTMLCalendar
from flask import url_for
from datetime import datetime


class CustomCalendar(HTMLCalendar):
    def __init__(self, year, month, day):
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def month_name(self):
        names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                 "November", "December"]
        return names[self.month - 1]

    def month_toggle(self, direction, location):
        if direction == "up":
            if self.month == 12:
                return url_for('business_calendar', location_id=location, year=self.year + 1, month=1, day=0)
            else:
                return url_for('business_calendar', location_id=location, year=self.year, month=self.month + 1, day=0)
        else:
            if self.month == 1:
                return url_for('business_calendar', location_id=location, year=self.year - 1, month=12, day=0)
            else:
                return url_for('business_calendar', location_id=location, year=self.year, month=self.month - 1, day=0)

    @staticmethod
    def return_to_today(location):
        return url_for('business_calendar', location_id=location, year=datetime.now().year, month=datetime.now().month,
                       day=datetime.now().day)
