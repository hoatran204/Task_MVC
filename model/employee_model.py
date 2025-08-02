from model.base_model import BaseModel
class EmployeeModel:
    def select_data():
        rows = BaseModel.Select("employee.*, COUNT(a.assignment_id) AS tong_tai_san",
        f"""employee
            LEFT JOIN 
                asset_assignments a ON employee.employee_id = a.user_id
            GROUP BY 
                employee.employee_id""")
        employees = []
        for row in rows:
            employees.append([
                row['employee_id'],
                "",
                row['full_name'],
                row["department"],
                row["tong_tai_san"],
                row["email"],
                row["phone_number"],
                row["status"],
                row["position"]
            ])
        return employees
    def contentTable_all():
        data = EmployeeModel.select_data()
        ar = {
            "class": "content-table",
            "collumn": [ ["-hidden", ""],
                ["--checkbox",""],
                ["-normal","Tên nhân viên"],
                ["-normal","Thuộc đơn vị"],
                ["-normal","Số TS đang sử dụng"],
                ["-normal","Email"],
                ["-normal","Số điện thoại"],
                ["-normal","Tình trạng"],
                ["-normal", "Chức vụ"]],
            "data": data,
            "style": ["-hidden", "--checkbox", '',"", "", "", "", "",""]
        }
        return ar