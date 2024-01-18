import datetime

class Person:
    def __init__(self, row: str) -> None:
        splitted = row.split(',')
        self.first_name = splitted[0]
        self.last_name = splitted[1]
        self.email = splitted[2]
        self.birthdate_str = splitted[3]
        self.birthdate = datetime.datetime.strptime(self.birthdate_str,"%Y-%m-%d")
        self.birthtime = splitted[4]

        splitted_time = self.birthtime.split(':')
        self.birthtime_minutes = int(splitted_time[0]) * 60 + int(splitted_time[1])
    
        splitted_date = self.birthdate_str.split('-')
        year = int(splitted_date[0])

        now = datetime.datetime.now()

        self.age =  now.year - year