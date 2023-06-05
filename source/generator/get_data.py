import random
import source.data.schoolname as data_schools
import source.data.streetname as data_street
import source.generator.address as gen_add
import source.generator.date as gen_date
import source.generator.name as gen_name
import source.generator.cccd as gen_cccd
import source.generator.score as gen_score

# Tạo 3 class School, Student và Score, mỗi class trả về list các giá trị cần thiết để insert vào bảng cùng tên
# Lớp Score kế thừa lớp Student, lớp Student kế thừa lớp School
class School:
    # Constructor khai báo số lượng trường, id trường, tên trường và địa chỉ trường
    def __init__(self, size):
        self.size = size
        self.school_id = []
        self.school_name = []
        self.school_address = []

    def gen_school_data(self):
        # Random id trường (3 chữ số)
        self.school_id = random.sample(range(100, 999), self.size)
        # Random tên trường từ schoolname.py (không trùng)
        self.school_name = random.sample(data_schools.school_lst, k=self.size)

        # Random tên đường từ streetname.py (không trùng)
        street_lst = random.sample(data_street.street_lst, self.size)
        # Lấy list n địa chỉ từ address.py
        address_lst = gen_add.get_school_address(self.size)

        # Random số đường và gộp với tên đường
        self.school_address = [
            f"{random.randint(1, 300)} {street}, {address}"
            for street, address in zip(street_lst, address_lst)
        ]

        # Trả về list id trường, tên trường, địa chỉ trường với n phần tử
        return self.school_id, self.school_name, self.school_address


class Student(School):
    # Constructor khai báo số lượng học sinh, họ, tên, ntns, cccd và địa chỉ học sinh
    def __init__(self, size):
        super().__init__(size)
        self.student_id = []
        self.student_first = []
        self.student_last = []
        self.student_date = []
        self.cccd = []
        self.student_address = []

    def gen_student(self, school_ids): # Truyền vào id trường
        # Quy ước id học sinh: 3 chữ số đầu là id trường + 5 chữ số sau random ngẫu nhiên
        for head_id in school_ids:
            # Random 5 chữ số
            tail_id = random.sample(range(10000, 100000), self.size)
            for i in range(self.size):
                # Ghép với id trường để tạo thành id học sinh
                self.student_id.append(str(head_id) + str(tail_id[i]))
        # Lấy list tên, họ từ hàm gen_name()
        first, last = gen_name.gen_name()
        # Lấy ngẫu nhiên họ, tên từ trong list
        self.student_first = random.choices(first, k=self.size * len(school_ids))
        self.student_last = random.choices(last, k=self.size * len(school_ids))
        # Lấy n số cccd từ hàm ran_cccd (Không trùng)
        self.cccd = list(gen_cccd.rand_cccd(self.size * len(school_ids)))
        # Lấy n ntns từ rand_year
        self.student_date = gen_date.rand_year(self.size * len(school_ids))
        # Lấy n địa chỉ từ get_student_address
        self.student_address = gen_add.get_student_address(self.size * len(school_ids))

        # Trả về list id học sinh, họ, tên, cccd, ntns và địa chỉ
        return self.student_id, self.student_last, self.student_first, self.cccd, self.student_date, self.student_address

class Score(Student):
    # Constructor khai báo id trường, id học sinh, năm học, điểm tb, xếp loại và kết quả
    def __init__(self):
        self.school_id = []
        self.student_id = []
        self.school_year = []
        self.scores = []
        self.grades = []
        self.results = []

    def get_school_year(self, num_results):
        # Các giá trị năm học
        year = ['2023', '2022', '2021']
        # Lấy số lượng năm học dựa trên năm sinh của học sinh
        school_years = year[:num_results]
        return school_years

    def check_result(self, score):
        grade_lst = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
        result_lst = ["Hoàn thành", "Chưa hoàn thành"]

        # Điều kiện để đạt được xếp loại a và kết quả b
        if score >= 9:
            # Xuất sắc
            grade = grade_lst[0]
        elif score >= 8:
            # Giỏi
            grade = grade_lst[1]
        elif score >= 6.5:
            # Khá
            grade = grade_lst[2]
        elif score >= 5:
            # Trung bình
            grade = grade_lst[3]
        else:
            # Yếu
            grade = grade_lst[-1]

        if score >= 5:
            # Hoàn thành
            result = result_lst[0]
        else:
            # Chưa hoàn thành
            result = result_lst[-1]

        return grade, result

    def gen_score(self, stud_id, dob): # Truyền vào id học sinh và ntns
        # Lấy năm sinh từ chuỗi dob
        years = [int(birthday[:4]) for birthday in dob]
        cnt = 0

        # Lặp trong list years, nếu hs là 2k5 (lớp 12) thì sẽ có 3 kết quả học tập, 2k6 là 2 và 2k7 là 1
        for year in years:
            if year == 2005:
                num_results = 3
            elif year == 2006:
                num_results = 2
            elif year == 2007:
                num_results = 1
            else:
                num_results = 0
            # Lấy điểm được random từ hàm score.py
            num_results_lst = gen_score.get_score(num_results)
            # Với mỗi học sinh có n bảng điểm, thì cần thêm n id học sinh vào list
            # VD: Có 5 trường, mỗi trường 10 hs, mỗi hs 2 bảng điểm
            # Số lượng id trường A xuất hiện: 10 * 2 = 20 lần mỗi trường
            # Số lượng id học sinh X xuất hiện: 2 lần mỗi học sinh
            # Ta cần lặp num_results lần để ghi thêm id học sinh vào list
            for i in range(num_results):
                self.student_id.append(stud_id[cnt])
                # Cắt 3 chữ số đầu trong id học sinh để ghi vào list id trường
                self.school_id.append(stud_id[cnt][:3])
            cnt += 1

            self.scores.extend(num_results_lst)
            self.school_year.extend(self.get_school_year(num_results))

        # Truyền vào điểm số để đưa ra xếp loại và kết quả của học sinh
        for score in self.scores:
            # Sử dụng hàm check_result ở trên để đánh giá
            grade, result = self.check_result(score)
            self.grades.append(grade)
            self.results.append(result)

        # Trả về list id trường, id học sinh, năm học, điểm tb, xếp loại và kết quả
        return self.school_id, self.student_id, self.school_year, self.scores, self.grades, self.results

