import xml.etree.ElementTree as ET

def query_xml(path, min_value, max_value):
    tree = ET.parse(path)
    root = tree.getroot()

    records = root.findall("./record")
    filtered_records = [record for record in records if float(min_value) < float(record.findtext("diemtb")) < float(max_value)]

    for i, record in enumerate(filtered_records, start=1):
        name = record.findtext("ho") + " " + record.findtext("ten")
        ntns = record.findtext("ntns")
        diemtb = record.findtext("diemtb")
        xeploai = record.findtext("xeploai")
        kqua = record.findtext("kqua")

        output = f"{i}. {name}, {ntns}, {diemtb}, {xeploai}, {kqua}"
        print(output)


def input_xml():
    print("Nhập đường dẫn file .xml (trong file xml_links.txt)")
    path = input()
    print("Nhập ngưỡng điểm tối thiểu: ")
    min = input()
    print("Nhập ngưỡng điểm tối đa: ")
    max = input()
    query_xml(path, min, max)

input_xml()