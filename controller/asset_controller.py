from model.asset_model import AssetModel
from flask import url_for
from controller.base_controller import BaseController

class AssetController:
    def add_asset():

        data = []
        columns = [
            "Mã tài sản",
            "Tên tài sản",
            "Vị trí tài sản",
            "Trạng thái",
            "SL cấp phát"
        ]
        ar = [[]]
        styles = ["edit","edit","edit","status","edit"]
        class_table = "assigntable"
        html = f"""<form action = "/add_asset" method=post>"""
        html += "<div style='width:800px; margin:-10px; background:white; padding: 0'>"
        html += "<h3>Cấp phát tài sản</h3>"
        html += f"""{AssetController.get_assets_alocation()}"""
        
        html+="<h5 style='margin: 10 20px'>Tài sản được cấp phát (0)</h5>"
        html+= f"""<button style='margin:0 30px' type='button' id="addRowBtn" class="btn-add">➕ Thêm mới</button>"""
        html += f"""{BaseController.bindingdata(columns, data, styles, class_table)}"""
        html += f"""{AssetController.button()}"""
        html += "</div></form>"
        html += f"""<script>
            document.getElementById("addRowBtn").addEventListener("click", function (event) {{
            event.preventDefault(); // Prevents form submission
            const tableBody = document.getElementById("assigntable").querySelector("tbody");
                if (!tableBody) {{
                console.error("Table or tbody not found!");
                return;
            }}
            const newRow = document.createElement("tr");
            newRow.innerHTML = `
                """
        html += AssetModel.insert_asset()
        html += f"""
            `;

            tableBody.appendChild(newRow);
            }});
            </script>"""

        print(html)
        return html
    def get_asset():
        header= BaseController.header("Tài sản","Quản lý tài sản")
        data = AssetModel.select()
        columns = [
            "Mã tài sản",
            "Tên tài sản",
            "Loại tài sản",
            "Trạng thái",
            "Nhân viên sử dụng",
            "Vị trí tài sản",
            "Đơn vị quản lý"
        ]
        styles = ["","","","choose","","",""]
        html = f"{header}"
        html += BaseController.nav()
        html += f""" {BaseController.bindingdata(columns, data, styles,"")}"""
        return html
    def update_status(id, new_status):
        return AssetModel.update_status(new_status, id)
    def get_assets_alocation():

        data = AssetModel.assets_alocation()
        return BaseController.form(data)
    def button():
        data = [["button","btn btn-secondary","reloadPage() ","Hủy"],
                ["submit","btn btn-primary","submitForm()","Cấp phát"]]
        return BaseController.button(data)
    def return_asset_data():
        return AssetModel.add_asset_data()
    def assets_alocation():
        return AssetModel.assets_alocation()
    def add_data(data):
        return AssetModel.add_data(data)