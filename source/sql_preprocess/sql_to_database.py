from sqlalchemy import create_engine, text
import time
import source.sql_preprocess.create_sql as create

def execute_data(db):
    # Kết nối với mysql với quyền truy cập admin root
    engine = create_engine('mysql+mysqlconnector://root:22942294tram@localhost:3306/' + str(db))
    # Bắt đầu thời gian đếm
    start_time = time.time()
    # Bắt đầu kết nối với database
    with engine.connect() as connection:
        print("Importing data... (Average time: 3 minutes)")
        # Set buffer size = 64 mb (chia batch để tránh quá tải trong việc insert data)
        connection.execute("SET bulk_insert_buffer_size = 64 * 1024 * 1024;")
        # Set packet = 256 mb (lượng dữ liệu thường trên 150 mb nên cần phải mở rộng giới hạn)
        connection.execute("SET GLOBAL max_allowed_packet = 256 * 1024 * 1024;")

        # Insert data vào database
        with open("source/sql_preprocess/sql_insert_data/truong.sql", encoding="utf-8") as file:
            query = text(file.read())
            connection.execute(query)
        with open("source/sql_preprocess/sql_insert_data/hs.sql", encoding="utf-8") as file:
            query = text(file.read())
            connection.execute(query)
        with open("source/sql_preprocess/sql_insert_data/hoc.sql", encoding="utf-8") as file:
            query = text(file.read())
            connection.execute(query)

    # Kết thúc đếm thời gian
    end_time = time.time()
    # Thời gian chạy trung bình mỗi database: 150-160s (tùy vào lượng dữ liệu và CPU)
    print("Thời gian để insert dữ liệu vào database: ")
    print(end_time - start_time)

def gen_db():
    # Gọi các hàm bên file create_sql.py
    create.delete_files()
    create.data_truong()
    create.data_hs()
    create.data_hoc()
    # Lần lượt import vào database truonghoc1 và truonghoc2
    execute_data("truonghoc1")
    execute_data("truonghoc2")