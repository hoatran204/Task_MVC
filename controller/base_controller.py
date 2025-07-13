from model.base_model import BaseModel

from flask import url_for,request, redirect

class BaseController:
    def header(header, title):
        html = f"""
        <!DOCTYPE html>
        <html lang="vi">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{header}</title>
            <link rel="stylesheet" href="{{{{ url_for('static', filename='base/base.css') }}}}">
        </head>
        <body>
            <header class="header">
                <div class="header-left">
                    <span class="logo-text">{title}</span>
                </div>
                
                <div class="header-right">
                    <span class="ai-assistant-text">AI Assistant</span>
                    <div class="header-icons">
                        <button class="header-btn dots-btn" title="More options"></button>
                        <button class="header-btn notification-btn" title="Notifications"></button>
                        <button class="header-btn settings-btn" title="Settings"></button>
                        <button class="header-btn fullscreen-btn" title="Fullscreen"></button>
                        <div class="user-avatar" title="User account">U</div>
                    </div>
                </div>
            </header>
        </body>
        </html>"""
        return html

    def bindingdata(columns,data,styles, class_table):

        
        result = BaseModel.render_table(columns, data, styles, class_table)

        return result
    def nav():
        html = f"""<div class="tabs-container">"""
        data = [
            ["Việc của bạn"],
            ["Việc bạn giao", 27]
        ]
        html += BaseModel.nav(data)
        html += f"""    <div class="tabs-right">
                <button class="action-btn">+</button>
                <button class="more-btn"></button>
            </div>
        </div>
        <div class="toolbar">
            <div class="toolbar-group">
                <button class="toolbar-btn">
                    <span class="icon">☰</span>
                    Danh sách
                    <span class="dropdown-arrow"></span>
                </button>
                
                <button class="toolbar-btn">
                    <span class="icon">📊</span>
                    Tuần này
                    <span class="dropdown-arrow"></span>
                </button>
            </div>
            </div>"""
        return html
    def update_status(id, new_status, referer):
        from controller.task_controller import TaskController
        from controller.asset_controller import AssetController
        if referer == "http://127.0.0.1:5000/task":
            TaskController.update_status(id, new_status)
        elif referer.rstrip("/") == "http://127.0.0.1:5000":
            AssetController.update_status(id, new_status)
    def form(data):
        return BaseModel.render_form(data)
    def button(data):
        return BaseModel.button(data)
    def check_list_asset(data):
        arr = []
        for row in data:
            arr.append(row[3])
        return arr
    def check_list(data):
        arr = []
        for row in data:
            for cell in row:
                if isinstance(cell, list) and len(cell) > 3:
                    arr.append(cell[3])  # lấy 'employee', 'dispenser', ...
                else:
                    print(f"Bỏ qua cell vì không hợp lệ: {cell}")
        return arr

    def last_data(main,detail):
        data = BaseController.check_list(main)
        ar_data = [request.form.get(field) for field in data]
        data_asset = BaseController.check_list_asset(detail)
        ar_data_asset = [request.form.getlist(field) for field in data_asset]
        last_data = []
        for i in range(len(ar_data_asset[1])):
            row = ar_data + [ar_data_asset[j][i] for j in range(len(ar_data_asset))]
            last_data.append(row)
        
        return last_data
        

