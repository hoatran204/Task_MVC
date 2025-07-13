from model.base_model import BaseModel

class AssetModel:
    def status():
        status = [
            ["Broken", "Đã hỏng", "#e6f0ff", "#3399ff"],
            ["In Use", "Đang sử dụng", "#fff3cd", "#ff9800"],
            ["Under Maintenance","Đang bảo dưỡng", "#f3e8ff","#6f42c1"]
            ]
        return status
        
    def select():
        
        rows = BaseModel.Select("a.assignment_id,a.status, a.assign_date, a.reason AS ten_tai_san, a.created_at,u.full_name, u.avatar_url, t.type_name",
        "asset_assignments a JOIN users u ON a.user_id = u.user_id join asset_types t on a.type_id = t.type_id ORDER BY assign_date ASC")
        status = AssetModel.status()
        assets = []
        try:
            for row in rows:
                asset_status, choose_status = BaseModel.choose(row["status"], status)
                print(status, choose_status)
                assets.append([
                    row['assignment_id'],
                    row['ten_tai_san'],
                    row['type_name'],
                    [asset_status,choose_status],
                    row['full_name']
                ])
            print(assets)
            return assets
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            return []
    def update_status(new_status, id):
        where=f"assignment_id={id}"
        status = {"status": new_status}
        BaseModel.update("asset_assignments", status, where)
    def user_ar():
        user_arr = []
        users = BaseModel.Select("user_id, full_name", "users")
        for user in users:
            user_arr.append([
                user["user_id"],
                user["full_name"]
            ])     
        return user_arr
    def assets_alocation():
        user_arr = AssetModel.user_ar()   
        data = [
            [["select",  "45%", "Nhân viên sử dụng", "employee", "Chọn nhân viên","require", user_arr]],
            [["text",  "40%", "Người cấp phát", "dispenser", "Thêm tên","require"],
            ["date", "40%", "Ngày cấp phát", "date", "Ngày cấp phát","require"]],
            [["text","98%","Lý do", "reason","Lý do"]],
            [["text","98%","Địa điểm bàn giao","place","Địa điểm bàn giao"]]
        ]
        return data
    def insert_asset():
        
        data = AssetModel.add_asset_data()
        html = ""
        for row in data:
            html += f"""<td class='form-td'> {BaseModel.render_input(row)}</td>"""
        return html
    
    def add_asset_data():
        status_ar = AssetModel.status()
        return [["text","10px","", "asset_id[]","Điền mã tài sản","require"],
                ["text", "auto", "", "asset_name[]", "Điền tên tài sản", "require"],
                ["text", "auto", "", "asset_place[]", "Vị trí tài sản"],
                ["select", "auto", "", "asset_status[]", "Chọn trạng thái", "", status_ar],
                ['number',"auto", "", "asset_number[]", "Số lượng cấp phát","require"]]
    def add_data(data):
        table_and_columns = "asset_assignments(user_id, assigner, assign_date, reason, location, assignment_id, assignment_name, place, status, quantity)"
        

        for row in data:
            if len(row) == 10:
                # Gọi đúng format: truyền tuple(row)
                a = ""
                for cell in row:
                    if cell == row[9]:
                        a += f"'{cell}'"
                    else:
                        a += f"'{cell}',"
                BaseModel.Insert(table_and_columns, a)
            else:
                print("❌ Bỏ qua dòng không hợp lệ:", row)


