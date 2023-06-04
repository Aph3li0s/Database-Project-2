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
    engine = create_engine('mysql+mysqlconnector://root:22942294tram@localhost:3306/'+ str(db))
    with engine.connect() as conn:
        query = f"""
            SELECT hs.ho, hs.ten, hs.ntns, hc.diemtb, hc.xeploai, hc.kqua
            FROM hs hs, hoc hc, truong tr
            WHERE tr.matr = hc.matr
                AND hs.mahs = hc.mahs
                AND tr.tentr = '{school_name}'
                AND hc.namhoc = '{year}'
                AND hc.xeploai = '{score_grade}';
        """
        result = conn.execute(query)
        rows = result.fetchall()
        root = etr.Element("data")

        for row in rows:
            record = etr.SubElement(root, "record")

            for i, column in enumerate(result.keys()):
                field_value = str(row[i])
                field_value = saxutils.escape(field_value)  # Escape special characters
                field = etr.SubElement(record, column)
                field.text = field_value

        xml_string = etr.tostring(root, encoding="utf-8", method="xml")
        parsed_dom = minidom.parseString(xml_string)
        formatted_xml = parsed_dom.toprettyxml(indent="    ")

        school_name = school_name.replace(" ", "")
        score_grade = score_grade.replace(" ", "")

        with open("XML/'{}'.xml".format(db + "_" + school_name+ "_" + str(year) + "_" + score_grade), "w",
                  encoding="utf-8") as xml_file:
            xml_file.write(formatted_xml)


def get_input():
    print("Hãy xem data trong folder source/csv_table để lấy info truy vấn")
    print("Nhập số lượng lệnh cần truy vấn: ")
    num = int(input())
    command_lst = []
    print("Định dạng input: truonghoc1, FPT, 2022, Xuất sắc")
    for i in range(num):
        print("Nhập lệnh thứ " + str(i + 1))
        cmd = str(input())
        command_lst.append(cmd)

    store_xml = "xml_links.txt"
    clean_file(store_xml)
    cnt = 0
    with open(store_xml, 'w', encoding="utf-8") as xml:
        for i in command_lst:
            start_time = time.time()
            values = [value.strip() for value in i.split(",")]
            xml_convert(values[0], values[1], int(values[2]), values[3])
            values[1] = values[1].replace(" ", "")
            values[3] = values[3].replace(" ", "")
            xml.write("XML/'{}'.xml".format(values[0] + "_" + values[1] + "_" + values[2] + "_" + values[3]) + "\n")

            end_time = time.time()
            print("Thời gian để truy vấn lệnh thứ " + str(cnt) + ": ")
            cnt += 1
            print(end_time - start_time)

get_input()