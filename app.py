from models import Programmer
from models import Candidate
from models import Vacancy
from models import Recruiter


egor = Programmer('Egor', 150, 'egor@gmail.com', ['JS', 'Python', 'PHP', 'HTML', 'SQL'])
veniamin = Programmer('Veniamin', 100, 'veniamin@gmail.com', ['JS', 'Python', 'SQL'])
andrey = Candidate('Ivanov Andrey', 'ivanova@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
                   ['Python: middle', 'SQL: middle', 'JS: middle'])
ivan = Candidate('Ivan', 'ivan@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
                 ['Python: middle', 'SQL: middle', 'JS: middle'])
veronica = Candidate('Veronica', 'veronica@gmail.com', ['Python', 'SQL', 'JS'], ['Python', 'SQL', 'JS'],
                     ['Python: middle', 'SQL: middle', 'JS: middle'])
irina = Recruiter('Irina', 200, 'irina@gmail.com')
soft_dev = Vacancy('Software Developer', ['Python', 'SQL', 'GitHub', 'SQL Alchemy', 'JS'],
                   ['Python: middle', 'SQL: middle', 'JS: middle'])
full_stack = Vacancy('FullStack Developer', ['Python', 'SQL', 'SQL Alchemy', 'JS', 'React', 'Swift'],
                     ['Python: middle', 'SQL: middle', 'JS: middle'])
