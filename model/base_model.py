from config import get_connection
import json
from collections import defaultdict
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from mysql.connector import Error
from datetime import datetime, date
from flask import url_for


class BaseModel:
    @staticmethod
    def render_column(columns, column_styles=None, class_table = None):
        # Bắt đầu table

        html = f"<table id='{class_table}' class='{class_table}'>\n"
        html += "<thead>"

        # Header
        html += "  <tr>\n"
        for i, col in enumerate(columns):
            if column_styles and i < len(column_styles) and column_styles[i] == "hidden":
                html += f"<th style='display:none'>{col}</th>"
            else:
                html += f"    <th>{col}</th>\n"

        html += "  </tr>\n"
        html += "</thead>\n"
        return html
    @staticmethod
    def render_data(data, column_styles=None):
        html = ""
        for row in data:
            html += f"  <tr"
            if str(row[0]).startswith("sub"):
                html += f" style='display:none'"
            html += f" id={row[0]}>"
            
            for i, cell in enumerate(row):
                
                if column_styles and i < len(column_styles):
                    id = row[0]
                    html += f" {BaseModel.style(column_styles[i],i, cell,column_styles,row)}"
                else:
                    html += f"<td>{cell}</td>"
            html += "  </tr>\n"
        
        return html
    @staticmethod
    def render_table(columns, data, column_styles=None, class_table=None):
        html = BaseModel.render_column(columns, column_styles, class_table)
        html += "<tbody>"
        html += BaseModel.render_data(data, column_styles)
        html += "</tbody>\n"
        html += "</table>\n"
        return html
    @staticmethod
    def nav(data):
        html = "<div class='tabs-list'>"

        for i, row in enumerate(data):
            html += "<div class='tab-item'>"
            for j, cell in enumerate(row):
                if i < 1:
                    # kiểu A
                    if j == 0:
                        html += f"<strong>{cell}</strong>"
                    else:
                        html += f" ({cell})"
                else:
                    # kiểu B
                    html += f"<div class='dropdown-container'>"
                    html += f"<button class='dropdown-btn'>Khác<span class='dropdown-arrow'></span>"
                    html += f" </button></div>"
                    break
            html += "</div>"
        html += "</div>"
        return html
    @staticmethod
    def render_form(data):
        html = ""
        for row in data:
            result = BaseModel.render(row)
            if result:
                html += result
        return html
    @staticmethod
    def render(row):
        html = ""
        if len(row) == 1:
            for cell in row:

                html = f"""
                
                <div class="form-group" style="width:{cell[1]}">
                {BaseModel.render_input(cell)}
                </div> """
        else:
            html = f"<div class='form-row'>"
            for cell in row:
                html += f"""
                
                <div class="form-item" >
                {BaseModel.render_input(cell)}
                </div>"""
            html +="</div>"
            
        return html
    @staticmethod 
    def render_input(ar):
        require = ["",""]
        if len(ar) > 5:
            if ar[5] == "require":
                require = ["*", "required"]
        if ar[0] == "select":
            options_html = ""
            for cell in ar[6]:  # Bỏ 2 phần đầu
                options_html += f"""<option value="{cell[0]}">{cell[1]}</option>"""
            
            return f"""
                <label class='label_form'>{ar[2]}
                {require[0]}
                </label>
                <select class='select_form' name="{ar[3]}" {require[1]}>
                    <option value="">-- {ar[4]} --</option>
                    {options_html}
                </select>"""
        if ar[0] == "text":
            return f"""
                <label class='label_form' >{ar[2]} {require[0]}</label>
                <input  type='text' name='{ar[3]}' {require[1]}>
            """
        if ar[0] == "date":
            return f"""
                <label class='label_form'>{ar[2]}{require[0]}</label>
                <input  type='date' name='{ar[3]}' {require[1]}>
            """
        if ar[0] == "number":
            return f"""
                <label class='label_form'>{ar[2]}{require[0]}</label>
                <input  type='number' name='{ar[3]}' {require[1]}>
            """
            
    @staticmethod
    def isMain(i,row):
        html = ""
        if i == 1 and str(row[0]).startswith("main"):
            html = f"<span class='expand-icon' id ='open{row[0]}'>▶</span>"
        return html
    @staticmethod
    def style(style,i, cell, columns_styles, row):
        if style == "user":
            return f"""<td style='display:flex;align-items: center;' >
            {BaseModel.isMain(i,row)}
            <img style='border-radius:50%; height:40px;margin-right:10px;' src={cell[0]}> {cell[1]}</td>"""
        elif style == "percent":
            html = f"""<td>{BaseModel.isMain(i,row)}<div style='font-weight:bold; margin-bottom: 4px;'>{cell}%</div>
                            <div style='width: 100%; background-color: #eee; border-radius: 4px; overflow: hidden;'>
                            <div style='width: {cell}%; background-color: #28a745; height: 10px;'></div>
                            </div></td>
                            """
            return html
        elif style == "choose":
            html = f"""
            <td>
                <select class="no-arrow" name="status" onchange="updateStatus(this)" data-id="{row[0]}" style='
                background-color: {cell[0][2]};
                color: {cell[0][3]};
                border: 1px solid {cell[0][3]};
                padding: 4px 12px;
                border-radius: 999px;
                font-size: 14px;
                font-weight: 500;
                display: inline-block;
                '>
                <option value="{cell[0][0]}" selected hidden>{cell[0][1]}</option>
            """

            for option in cell[1]:  # các lựa chọn còn lại
                html += f"""<option style='background-color: {option[2]};
                color: {option[3]};
                border: 1px solid {option[3]};' value='{option[0]}'>{option[1]}</option>"""

            html += """
                </select>
            </form>
            </td>
            """
            return html
        elif style == "hidden":
            return f"<td style='display:none'>{BaseModel.isMain(i,row)}{cell}</td>"
        elif style == "subs":
            html = BaseModel.render_data(cell,columns_styles)
            
            return html
        else:
            return f"<td>{BaseModel.isMain(i,row)}{cell}</td>"
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
            print(query)
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
    def button(data):
        html = f"""<div class="form-actions" style='background:white'>"""
        for row in data:
            html += f"""<button type="{row[0]}" class="{row[1]}" onclick="{row[2]}">{row[3]}</button>"""
        html += f"""</div>"""
        return html
    