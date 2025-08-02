from config import get_connection
import json
from collections import defaultdict
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from mysql.connector import Error
from datetime import datetime, date
from flask import url_for
import copy


class BaseModel:
    @staticmethod
    def Select(columns, table):
        conn = None  
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)

            query = f"SELECT {columns} FROM {table}"
            cursor.execute(query)

            lists = cursor.fetchall()
            return lists

        except Error as e:
            print("Lỗi khi kết nối hoặc truy vấn MySQL:", e)
            return []

        finally:
            if conn and conn.is_connected():  # ✅ Kiểm tra conn tồn tại
                cursor.close()
    @staticmethod
    def update(table, data, condition):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Tạo câu lệnh UPDATE
            set_clause = ", ".join([f"{key} = %s" for key in data])
            values = list(data.values())
            query = f"UPDATE {table} SET {set_clause} WHERE {condition}"

            cursor.execute(query, values)
            conn.commit()
            return True

        except Error as e:
            print("Lỗi khi cập nhật dữ liệu:", e)
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    @staticmethod
    def Delete(table, condition):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = f"DELETE FROM {table} WHERE {condition}"
            cursor.execute(query)
            conn.commit()
            return True

        except Error as e:
            print("Lỗi khi xoá dữ liệu:", e)
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    @staticmethod
    def Insert(table, condition):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = f"INSERT INTO {table} values ({condition})"
            cursor.execute(query)
            conn.commit()
            return True

        except Error as e:
            print("Lỗi khi xoá dữ liệu:", e)
            return False

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    @staticmethod
    def sort_ar(ar, i):
        
        # Kiểm tra điều kiện đầu vào
        if not isinstance(ar, dict):
            raise TypeError("Input 'ar' must be a dictionary")
        if "data" not in ar:
            raise KeyError("Dictionary 'ar' must contain 'data' key")
        if not isinstance(ar["data"], list):
            raise TypeError("'ar[\"data\"]' must be a list")
        
        # Tạo bản sao sâu
        new_ar = copy.deepcopy(ar)
        data = new_ar["data"]
        
        # Kiểm tra độ dài và cấu trúc của từng phần tử
        for item in data:
            if not isinstance(item, list) or len(item) <= i:
                raise ValueError("Each item in 'ar[\"data\"]' must be a list with at least {} elements".format(i + 1))
        
        # Xác định logic sắp xếp
        def get_sort_key(x):
            value = x[i]
            if isinstance(value, str):
                return (value == "", value.lower() if value else "")
            elif isinstance(value, list):
                if value[0] is None and len(value) > 1:
                    # Lấy trạng thái đầu tiên trong danh sách lồng nhau
                    states = value[1]
                    if states and isinstance(states, list):
                        return (True, states[0][1].lower() if states[0][1] else "")
                else:
                    # Lấy trạng thái đầu tiên nếu có
                    return (False, value[0][1].lower() if value and value[0] and value[0][1] else "")
            return (True, "")  # Giá trị mặc định nếu không khớp

        # Sắp xếp dữ liệu
        sorted_data = sorted(data, key=get_sort_key)
        
        # Cập nhật dữ liệu đã sắp xếp
        new_ar["data"] = sorted_data
        return new_ar
    @staticmethod
    def choose(a, ar1):
        ar2 = None
        ar3 = []
        for ar in ar1:
            if a == ar[0]:
                ar2 = ar
            else:
                ar3.append(ar)
        return ar2, ar3
    @staticmethod
    def extract_sort_manual(url, split_value):
        if '?' not in url:
            return None
        query_str = url.split('?', 1)[1]
        print(f"[DEBUG] query_str: {query_str}")
        pairs = query_str.split('&')
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                print(f"[DEBUG] key: {key}, value: {value}")
                if key.strip() == split_value.strip():
                    print(f"[FOUND] {split_value} = {value}")
                    return value
        return None
    @staticmethod
    def replace(url, split_value):
        index = BaseModel.extract_sort_manual(url, split_value)
        content= f"&{split_value}={index}"
        new_url = url.replace(content, "")
        return new_url
    def main_leftbar_ar():
        ar = [
            ["Thống kê", "statistic", "fas fa-chart-bar"],
            ["Tài sản", "assignments", "fas fa-briefcase"],
            ["Nhân viên", "employees", "fas fa-users"],
            ["Kiểm kê", "inventory", "fas fa-clipboard-list"],
            ["Cài đặt", "main", "fas fa-cog", [
                ["Thông tin công ty", "company_information"],
                ["Cơ cấu tổ chức", "organizational_structure"],
                ["Loại tài sản", "asignment_type"],
                ["Nhà cung cấp","supplier"]
            ]]
        ]
        return ar
    def count(data, table, column):
        new_data = []
        for row in data:
            if row[0] == "all":
                result = BaseModel.Select("count(*)", table)
            else:
                value = f"'{row[0]}'" if isinstance(row[0], str) else row[0]
                result = BaseModel.Select("count(*)", f"{table} WHERE {column} = {value}")
            
            # Lấy giá trị số thay vì dict
            count_number = result[0]['count(*)'] if result else 0

            new_data.append([
                row[0],   # Giá trị điều kiện
                row[1],   # Nhãn
                count_number  # Số lượng
            ])

        print(new_data)
        return new_data



    
    

    