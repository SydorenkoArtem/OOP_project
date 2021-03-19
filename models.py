from datetime import timedelta, datetime
from enum import Enum


class WeekDays(Enum):
    Saturday = 6
    Sunday = 7


class Employee:

    def __init__(self, name: str, salary_day: int, email: str):
        self.string_date_format: str = '%Y-%m-%d'
        self.name: str = name
        self.salary_day: int = salary_day
        self.email: str = email

    def work(self):
        return "I come to the office"

    def check_salary(self):
        counted_days: int = self.count_days()
        return counted_days * self.salary_day

    def count_days(self):
        days_list = [date for date in self.datetime_range()]
        counter = 0

        for day in days_list:
            if day.isoweekday() == WeekDays.Saturday.value or day.isoweekday() == WeekDays.Sunday.value:
                counter += 1
        return len(days_list) - counter

    def datetime_range(self):
        finish_date = datetime.now()
        start_date = datetime(finish_date.year, finish_date.month, 1)
        span = finish_date - start_date
        for i in iter(range(span.days + 1)):
            yield start_date + timedelta(days=i)

    def convert_to_datetime_format(self, date: str):
        return datetime.strptime(date, self.string_date_format)

    def compare_salary(self):
        if self.salary_day < 150:
            return 'Low salary'
        elif 150 <= self.salary_day < 200:
            return 'Middle salary'
        else:
            return 'High salary'


class Recruiter(Employee):

    def __str__(self):
        return f"Должность: {__class__.__name__}"

    def work(self):
        return "I come to the office and start to hiring."


class Programmer(Employee):

    def __init__(self, name: str, salary_day: int, email: str, tech_stack: list):
        super().__init__(name, salary_day, email)
        self.tech_stack: list = tech_stack

    def __str__(self):
        return f"Должность: {__class__.__name__}"

    def work(self):
        return "I come to the office and start to coding."

    def compare_tech_stack(self):
        count_skills = 0
        for i in self.tech_stack:
            count_skills += 1
        if count_skills <= 3:
            return 'Junior skills'
        elif 3 < count_skills < 6:
            return 'Middle skills'
        else:
            return 'Senior skills'


class Candidate:

    def __init__(self, full_name: str, email: str, technologies: list, main_skill: list, main_skill_grade: list):
        self.full_name: str = full_name
        self.email: str = email
        self.technologies: list = technologies
        self. main_skill: list = main_skill
        self.main_skill_grade: list = main_skill_grade


class Vacancy:

    def __init__(self, title: str, main_skill: list, main_skill_level: list):
        self.title: str = title
        self.main_skill: list = main_skill
        self.main_skill_level: list = main_skill_level




