import os
import pandas as pd

truong = pd.read_csv("source/csv_table/truong.csv")
hs = pd.read_csv("source/csv_table/hocsinh.csv")
hoc = pd.read_csv("source/csv_table/hoctap.csv")

def delete_files():
    for file_name in os.listdir("source/sql_preprocess/sql_insert_data"):
        file_path = os.path.join("source/sql_preprocess/sql_insert_data", file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def clean_file(sql_file):
    if os.stat(sql_file).st_size != 0:
        with open(sql_file, "w", encoding="utf-8") as f:
            f.write("")

def data_truong():
    sql_file = "source/sql_preprocess/sql_insert_data/truong.sql"
    with open(sql_file, 'w'):
        clean_file(sql_file)
        a = "INSERT INTO truong (matr, tentr, dchitr) VALUES \n"
        with open(sql_file, "a", encoding="utf-8") as f:
            f.write(a)
            for i, row in enumerate(truong.itertuples(index=False)):
                string = "('{}', '{}', '{}')".format(*row)
                f.write(string)
                if i < len(truong) - 1:
                    f.write(",\n")
            f.write(";")

def data_hs():
    sql_file = "source/sql_preprocess/sql_insert_data/hs.sql"
    with open(sql_file, 'w'):
        clean_file(sql_file)
        a = "INSERT INTO hs (mahs, ho, ten, cccd, ntns, dchi_hs) VALUES \n"
        with open(sql_file, "a", encoding="utf-8") as f:
            f.write(a)
            for i, row in enumerate(hs.itertuples(index=False)):
                string = "('{}', '{}', '{}', '{}', '{}', '{}')".format(*row)
                f.write(string)
                if i < len(hs) - 1:
                    f.write(",\n")
            f.write(";")

def data_hoc():
    sql_file = "source/sql_preprocess/sql_insert_data/hoc.sql"
    with open(sql_file, 'w'):
        clean_file(sql_file)
        a = "INSERT INTO hoc (matr, mahs, namhoc, diemtb, xeploai, kqua) VALUES \n"
        with open(sql_file, "a", encoding="utf-8") as f:
            f.write(a)
            for i, row in enumerate(hoc.itertuples(index=False)):
                string = "('{}', '{}', '{}', '{}', '{}', '{}')".format(*row)
                f.write(string)
                if i < len(hoc) - 1:
                    f.write(",\n")
            f.write(";")




