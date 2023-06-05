import xml.etree.ElementTree as etr
import xml.sax.saxutils as saxutils
from sqlalchemy import create_engine
import xml.dom.minidom as minidom
import os
import time

def clean_file(sql_file):
    if os.stat(sql_file).st_size != 0:
        with open(sql_file, "w", encoding="utf-8") as f:
            f.write("")

def xml_convert(db, school_name, year, score_grade):
    # Kết nối với database
    engine = create_engine('mysql+mysqlconnector://root:22942294tram@localhost:3306/'+ str(db))
    with engine.connect() as conn:
        # Lệnh dùng để truy vấn (truyền các giá trị được nhập vào lệnh)
        query = f"""
            SELECT hs.ho, hs.ten, hs.ntns, hc.diemtb, hc.xeploai, hc.kqua
            FROM hs hs, hoc hc, truong tr
            WHERE tr.matr = hc.matr
                AND hs.mahs = hc.mahs
                AND tr.tentr = '{school_name}'
                AND hc.namhoc = '{year}'
                AND hc.xeploai = '{score_grade}';
        """
        result = conn.execute(query) # Execute lệnh
        rows = result.fetchall()
        # Đặt tên thẻ là <data> (gốc của cây)
        root = etr.Element("data")

        # Lặp qua các dòng đã được query
        for row in rows:
            # Đặt tên thẻ là <record> (tạo node trên cây)
            record = etr.SubElement(root, "record")

            # Lặp qua các keys trong result
            for i, column in enumerate(result.keys()):
                field_value = str(row[i]) # Lấy giá trị tại hàng thứ i
                field_value = saxutils.escape(field_value) # Loại bỏ các kí tự đặc biệt
                field = etr.SubElement(record, column) # Tạo node con trong node record
                field.text = field_value # Insert giá trị vào nội dung của xml

        # Chuyển thành chuỗi xml
        xml_string = etr.tostring(root, encoding="utf-8", method="xml")
        # Chuyển thành đối tượng DOM
        parsed_dom = minidom.parseString(xml_string)
        # Định dạng khoảng trắng để format xml đẹp hơn
        formatted_xml = parsed_dom.toprettyxml(indent="    ")

        # Thay thế các khoảng trắng bằng các gạch dưới để mở file xml
        school_name = school_name.replace(" ", "")
        score_grade = score_grade.replace(" ", "")

        with open("XML/'{}'.xml".format(db + "_" + school_name+ "_" + str(year) + "_" + score_grade), "w",
                  encoding="utf-8") as xml_file:
            # Ghi vào file xml tương ứng
            xml_file.write(formatted_xml)


def get_input():
    print("Hãy xem data trong folder source/csv_table để lấy info truy vấn")
    print("Nhập số lượng lệnh cần truy vấn: ")
    num = int(input())
    command_lst = [] # List để lưu các lệnh vừa được nhập
    print("Định dạng input: truonghoc1, FPT, 2022, Xuất sắc")
    for i in range(num):
        print("Nhập lệnh thứ " + str(i + 1))
        cmd = str(input())
        # Lưu các lệnh vào list
        command_lst.append(cmd)

    # File txt lưu links của các file vừa được tạo
    store_xml = "xml_links.txt"
    clean_file(store_xml)
    cnt = 0
    # Xử lí input
    with open(store_xml, 'w', encoding="utf-8") as xml:
        for i in command_lst:
            start_time = time.time()
            values = [value.strip() for value in i.split(",")] # Tách các giá trị cách bởi dấu phẩy vào lưu vào list
            # Truyền vào hàm các giá trị vừa tách (tương ứng tên database, tên trường, năm học, xếp loại
            xml_convert(values[0], values[1], int(values[2]), values[3])
            # Thay thế các khoảng trắng bằng các gạch dưới để ghi tên file xml
            values[1] = values[1].replace(" ", "")
            values[3] = values[3].replace(" ", "")
            # In tên file xml đúng định dạng
            xml.write("XML/'{}'.xml".format(values[0] + "_" + values[1] + "_" + values[2] + "_" + values[3]) + "\n")

            end_time = time.time()
            print("Thời gian để truy vấn lệnh thứ " + str(cnt + 1) + ": ")
            cnt += 1
            print(end_time - start_time)

get_input()