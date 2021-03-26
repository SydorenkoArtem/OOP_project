# import datetime
# import traceback
#
# from models import Programmer
from models import Candidate
# from models import Vacancy
# from models import Recruiter
# from models import Employee

if __name__ == '__main__':
#     try:
#         egor = Programmer('Egor', 150, 'egor@gmail.com', ['JS', 'Python', 'PHP', 'HTML', 'SQL'])
#         veniamin = Programmer('Veniamin', 100, 'veniamin@gmail.com', ['JS', 'Python', 'SQL'])
#         andrey = Candidate('Ivanov Andrey', 'ivanova@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
#                            ['Python: middle', 'SQL: middle', 'JS: middle'])
#         ivan = Candidate('Ivan', 'ivan@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
#                          ['Python: middle', 'SQL: middle', 'JS: middle'])
#         veronika = Candidate('Veronica', 'veronica@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
#                              ['Python: middle', 'SQL: middle', 'JS: middle'])
#         irina = Recruiter('Irina', 200, 'irina@gmail.com')
#         soft_dev = Vacancy('Software Developer', ['Python', 'SQL', 'GitHub', 'SQL Alchemy', 'JS'],
#                            ['Python: middle', 'SQL: middle', 'JS: middle'])
#         full_stack = Vacancy('FullStack Developer', ['Python', 'SQL', 'SQL Alchemy', 'JS', 'React', 'Swift'],
#                              ['Python: middle', 'SQL: middle', 'JS: middle'])
#         viktor = Employee('Viktor', 150, 'viktor@gmail.com')
#     except Exception as err:
#         with open('logs.txt', 'a') as file:
#             message = '{}    {}:\n {}\n \n'.format(datetime.datetime.now(), err.__class__.__name__,
#                                                    traceback.format_exc())
#             file.write(message)
#
# veronika = Candidate('Veronica', 'veronica@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
#                      ['Python: middle', 'SQL: middle', 'JS: middle'])
#
# def some_deco(func):
#     def wrapper():
#         result = func()
#         result =
#
# try:
#     veronika.work()
# except Exception as err:
#     with open('logs.txt', 'a') as f:
#         message = '{}    {}:\n {}\n \n'.format(datetime.datetime.now(), err.__class__.__name__,
#                                                traceback.format_exc())
#         f.write(message)
#
#     viktor = Programmer('Viktor', 150, 'viktor@gmail.com', ['JS', 'Python', 'SQL'])
#     print(viktor.full_info)

    Candidate.create_candidate()
