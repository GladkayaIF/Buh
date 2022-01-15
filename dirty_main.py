from datetime import datetime
from application import *
from application.db import *


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    day = datetime.today()
    print(day.date())