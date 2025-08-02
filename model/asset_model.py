from model.base_model import BaseModel

class AssetModel:
    def contentTabs_ar(type):
        data = AssetModel.contentTable_all(type)
        collumn = data["collumn"]
        status = AssetModel.status()
        maintab1 = [["all", "Tất cả"]]
        for row in status:
            maintab1.append([
                row[0],
                row[1]
            ])
        maintab = BaseModel.count(maintab1, "asset_assignments", "status")
        ar = {
            "maintab": maintab,
            "setting": [
                ["Cài đặt tab", "main", {
                    "ShowAndHide": maintab
                    },"tab"],
                ["Cài đặt cột", "main", {
                    "ShowAndHide": collumn
                },"collumn"],
                ["Nhóm theo", "main", {
                    "setting": [
                        ["Loại tài sản", "none",4],
                        ["Trạng thái", "none",5],
                        ["Mức độ mật", "none"],
                        ["Đơn vị quản lý", "none"],
                        ["Vị trí tài sản", "none"]
                    ]}, "groupby"
                ]
            ]
        }


        return ar

    def contentTable_all(type):
        data = AssetModel.select(type)
        detail_data = []
        for row in data:
            detail_data.append({
                "id": row[2],
                "header": [row[3], row[2], row[5][0][1]],
                "information": [
                    ["ĐƠN VỊ QUẢN LÝ", row[8]],
                    ["VỊ TRÍ TÀI SẢN", row[7]],
                    ["NHÀ CUNG CẤP", "-"],
                    ["GIÁ MUA", "20000"]
                ],
                "description": ["Mô tả", row[9]]
            })
        ar = {
            "class": "content-table",
            "collumn": [ ["-hidden", ""],
                ["--checkbox",""],
                ["-normal","Mã tài sản"],
                ["-normal","Tên tài sản"],
                ["-normal","Loại tài sản"],
                ["-normal","Trạng thái"],
                ["-normal","Nhân viên sử dụng"],
                ["-normal","Vị trí tài sản"],
                ["-normal", "Đơn vị quản lý"]],
            "data": data,
            "style": ["-hidden", "--checkbox", "id","name","","option", "","", "", "-hidden"],
            "detail_data": detail_data
        }
        return ar
    def sort_contentTable(ar,i):
        return BaseModel.sort_ar(ar, i)
    
    def status():
        status = [                
            ["warehourse", "Lưu kho", "#f1f2f6", "#2f3542"],        
            ["inuse", "Đang sử dụng", "#fff3cd", "#ff9800"],
            ["broke", "Hỏng", "#e6f0ff", "#3399ff"],
            ["fix", "Đang sửa chữa/bảo dưỡng", "#f3e8ff", "#6f42c1"]
        ]
        return status
    @staticmethod
    def select(type):
        
        rows = BaseModel.Select("a.assignment_id,a.status,a.location, a.assign_date,a.place, a.assignment_name AS ten_tai_san ,a.reason, a.created_at,e.full_name,  t.type_name as loai_tai_san",
        "asset_assignments a JOIN employee e ON a.user_id = e.employee_id join asset_types t on a.type_id = t.type_id ORDER BY assign_date ASC")
        status = AssetModel.status()
        assets = []
        try:
            index = 1
            for row in rows:
                asset_status, choose_status = BaseModel.choose(row["status"], status)
                assets.append([
                    index,
                    "",
                    row['assignment_id'],
                    row['ten_tai_san'],
                    row['loai_tai_san'],
                    [asset_status,choose_status],
                    row['full_name'],
                    row['location'],
                    row['place'],
                    row["reason"]
                ])
                index += 1
            if type == "all":
                return assets
            else:
                print(assets)
                filtered_assets = [
                    item for item in assets 
                    if item[5][0] is not None and item[5][0][0] == type
                ]
                return filtered_assets
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            return []
    def update_status(new_status, id):
        where=f"assignment_id={id}"
        status = {"status": new_status}
        BaseModel.update("asset_assignments", status, where)
    