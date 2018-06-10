from calendar import HTMLCalendar

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
                return 1
            else:
                return self.month+1
        else:
            if self.month == 1:
                return 12
            else:
                return self.month-1

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
