import xml.etree.ElementTree as ET

def query_xml(path, min_value, max_value):
    tree = ET.parse(path) # Thực hiện truy vấn trên cây
    root = tree.getroot() # Lấy gốc của cây

    records = root.findall("./record") # Tìm tất cả data có trong node record
    # Sử dụng xpath để thực hiện điều kiện: tìm info học sinh có ngưỡng điểm trong giá trị đã cho
    filtered_records = [record for record in records if float(min_value) < float(record.findtext("diemtb")) < float(max_value)]

    # Tìm tất cả info học sinh và xuất ra màn hình
    for i, record in enumerate(filtered_records, start=1):
        name = record.findtext("ho") + " " + record.findtext("ten")
        ntns = record.findtext("ntns")
        diemtb = record.findtext("diemtb")
        xeploai = record.findtext("xeploai")
        kqua = record.findtext("kqua")
        # Định dạng output cho dễ nhìn hơn
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