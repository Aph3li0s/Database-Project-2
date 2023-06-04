import random
import source.data.schoolname as data_schools
import source.data.streetname as data_street
import source.generator.address as gen_add
import source.generator.date as gen_date
import source.generator.name as gen_name
import source.generator.cccd as gen_cccd
import source.generator.score as gen_score

class School:
    def __init__(self, size):
        self.size = size
        self.school_id = []
        self.school_name = []
        self.school_address = []

    def gen_school_data(self):
        self.school_id = random.sample(range(100, 999), self.size)
        self.school_name = random.sample(data_schools.school_lst, k=self.size)

        street_lst = random.sample(data_street.street_lst, self.size)
        address_lst = gen_add.get_school_address(self.size)

        self.school_address = [
            f"{random.randint(1, 300)} {street}, {address}"
            for street, address in zip(street_lst, address_lst)
        ]

        return self.school_id, self.school_name, self.school_address


class Student(School):
    def __init__(self, size):
        super().__init__(size)
        self.student_id = []
        self.student_first = []
        self.student_last = []
        self.student_date = []
        self.cccd = []
        self.student_address = []

    def gen_student(self, school_ids):
        for head_id in school_ids:
            tail_id = random.sample(range(10000, 100000), self.size)
            for i in range(self.size):
                self.student_id.append(str(head_id) + str(tail_id[i]))
        first, last = gen_name.gen_name()
        self.student_first = random.choices(first, k=self.size * len(school_ids))
        self.student_last = random.choices(last, k=self.size * len(school_ids))
        self.cccd = list(gen_cccd.rand_cccd(self.size * len(school_ids)))
        self.student_date = gen_date.rand_year(self.size * len(school_ids))
        self.student_address = gen_add.get_student_address(self.size * len(school_ids))
        return self.student_id, self.student_last, self.student_first, self.cccd, self.student_date, self.student_address

class Score(Student):
    def __init__(self):
        self.school_id = []
        self.student_id = []
        self.school_year = []
        self.scores = []
        self.grades = []
        self.results = []

    def get_school_year(self, num_results):
        year = ['2023', '2022', '2021']
        school_years = year[:num_results]
        return school_years

    def check_result(self, score):
        grade_lst = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
        result_lst = ["Hoàn thành", "Chưa hoàn thành"]

        if score >= 9:
            grade = grade_lst[0]
        elif score >= 8:
            grade = grade_lst[1]
        elif score >= 6.5:
            grade = grade_lst[2]
        elif score >= 5:
            grade = grade_lst[3]
        else:
            grade = grade_lst[-1]

        if score >= 5:
            result = result_lst[0]
        else:
            result = result_lst[-1]

        return grade, result

    def gen_score(self, stud_id, dob):
        years = [int(birthday[:4]) for birthday in dob]
        cnt = 0

        for year in years:
            if year == 2005:
                num_results = 3
            elif year == 2006:
                num_results = 2
            elif year == 2007:
                num_results = 1
            else:
                num_results = 0
            num_results_lst = gen_score.get_score(num_results)
            for i in range(num_results):
                self.student_id.append(stud_id[cnt])
                self.school_id.append(stud_id[cnt][:3])
            cnt += 1

            self.scores.extend(num_results_lst)
            self.school_year.extend(self.get_school_year(num_results))

        for score in self.scores:
            grade, result = self.check_result(score)
            self.grades.append(grade)
            self.results.append(result)

        return self.school_id, self.student_id, self.school_year, self.scores, self.grades, self.results

