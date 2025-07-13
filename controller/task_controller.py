from model.task_model import TaskModel
from flask import url_for
from controller.base_controller import BaseController

class TaskController:
    
    def get_tasks():
        data = TaskModel.get_all_task()
        header= BaseController.header("Công việc","Quản lý Công việc")

        columns = [
            "ID",
            "TÊN CÔNG VIỆC",
            "NGƯỜI GIAO VIỆC",
            "HẠN HOÀN THÀNH",       
            "TIẾN ĐỘ",
            "TRẠNG THÁI",
            "ƯU TIÊN",
            "TÌNH TRẠNG"
        ]
        styles = TaskModel.column_style()
        html = header
        html += BaseController.bindingdata(columns, data, styles,"")
        return html
    def update_status(id, new_status):
        if id.startswith("main-"):
            table = "main_tasks"
            id_number = id.split("-")[1]
        elif id.startswith("sub-"):
            table = "sub_task"
            id_number = id.split("-")[1]
        else:
            print("ID không hợp lệ")
            return

        TaskModel.update_status(new_status, table, id_number)



