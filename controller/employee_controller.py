from model.employee_model import EmployeeModel
from flask import url_for
from controller.base_controller import BaseController

class EmployeeController:
    def add_content(type, sort_type, url, current_path):
        main_table = EmployeeModel.contentTable_all()
        Tabdata = None
        return_url = None
        html = BaseController.add_content(type, sort_type,url, current_path, Tabdata, main_table, return_url, "Nhân viên", "Danh sách nhân viên")
        return html