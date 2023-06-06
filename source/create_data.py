import source.generator.get_data as data
import pandas as pd
import random
import time
import os

# Hàm dùng để xóa các bảng đã tạo
def delete_files():
    for file_name in os.listdir("source/csv_table"):
        file_path = os.path.join("source/csv_table", file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def create_data(num_schools, num_students):
    # Thực hiện xóa file trước khi khởi tạo
    # delete_files()

    # Bắt đầu đếm thời gian
    start_time = time.time()
    # Gọi các objects school, student, score
    school_lst = data.School(num_schools)
    student_lst = data.Student(num_students)
    score_lst = data.Score()

    # Lưu giá trị trả về vào các list tương ứng
    school_id, school_name, school_address = school_lst.gen_school_data()
    student_id, student_last, student_first, student_cccd, student_date, student_address = student_lst.gen_student(school_id)
    sch_id, stud_id, student_year, student_score, student_grade, student_result = score_lst.gen_score(student_id, student_date)

    # Các dict chứa keys là tên bảng và values là các giá trị được trả về bên trên
    # Dict trường -> truong.csv
    truong= {"MATR": school_id,
            "TENTR": school_name,
            "DCHITR": school_address
            }

    # Dict học sinh -> hocsinh.csv
    hs = {"MAHS": student_id,
          "HO": student_last,
          "TEN": student_first,
          "CCCD": student_cccd,
          "NTNS": student_date,
          "DCHI_HS": student_address
          }

    # Dict học -> hoctap.csv
    hoc = {"MATR": sch_id,
           "MAHS" : stud_id,
           "NAMHOC" : student_year,
           "DIEMTB" : student_score,
           "XEPLOAI": student_grade,
           "KQUA": student_result
        }
    random.shuffle(truong["DCHITR"])

    print("Creating data...")

    # Đưa data vào file .csv
    school = pd.DataFrame(truong)
    school.to_csv("source/csv_table/truong.csv", index= False)

    student = pd.DataFrame(hs)
    student.to_csv("source/csv_table/hocsinh.csv", index= False)

    score = pd.DataFrame(hoc)
    score.to_csv("source/csv_table/hoctap.csv", index= False)

    # Kết thúc đếm thời gian
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\n")
    print("Tổng có " + str(len(school_id)) + " trường, " + str(len(student_id)) + " học sinh, " +
          str(len(student_score)) + " kết quả học tập")

    print("Thời gian sinh data: ")
    print(elapsed_time)
