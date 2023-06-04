import source.create_data as gen_data
import source.sql_preprocess.sql_to_database as sql_db

def run():
    print("Nhập số lượng trường (100-120): ")
    num_school = int(input())
    print("Nhập số lượng học sinh mỗi trường (10k-11k): ")
    num_students = int(input())
    gen_data.create_data(num_school, num_students)
    sql_db.gen_db()


run()