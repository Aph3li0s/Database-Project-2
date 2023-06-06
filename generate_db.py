import source.create_data as gen_data
import source.sql_preprocess.sql_to_database as sql_db
import source.generator.score as visualize
def run():
    print("Nhập số lượng trường (100-120): ")
    num_schools = int(input())
    print("Nhập số lượng học sinh mỗi trường (10k-11k): ")
    num_students = int(input())
    visualize.visualize_score(num_schools, num_students)
    # Tạo data
    gen_data.create_data(num_schools, num_students)
    # Input vào database
    input("Nhấn enter để chọn database")
    while True:
        print("Nhập database(truonghoc1, truonghoc2). Nhấn 0 để thoát ")
        database_name = str(input())
        if database_name == '0':
            break
        if database_name != "truonghoc1" and database_name != "truonghoc2":
            print("Tên database không hợp lệ!")
        sql_db.gen_db(database_name)


run()