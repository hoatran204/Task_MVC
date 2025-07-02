from model.base_model import BaseModel
class BaseController:
    def bindingdata():
        # Ví dụ sử dụng
        columns = [
            "TÊN CÔNG VIỆC",
            "NGƯỜI GIAO VIỆC",
            "HẠN HOÀN THÀNH",
            "TIẾN ĐỘ",
            "TRẠNG THÁI",
            "ƯU TIÊN",
            "TÌNH TRẠNG"
        ]

        data = [
            [["Thiết kế UI"], ["url_for('static',filename='images/user_test.png')","Lan"], ["2025-07-01"], "60%", "Đang làm", "Cao", "Chưa hoàn thành"],
            ["Viết Backend", "Tùng", "2025-07-05", "30%", "Chưa làm", "Trung bình", "Chưa hoàn thành"],
            ["Test chức năng", "Hải", "2025-07-10", "80%", "Đang làm", "Cao", "Đang kiểm tra"],
            ["Triển khai Production", "Minh", "2025-07-15", "0%", "Chưa làm", "Cao", "Chưa triển khai"],
            ["Cập nhật tài liệu", "An", "2025-07-03", "100%", "Hoàn thành", "Thấp", "Đã xong"]
        ]
        styles = ["","user"]
        result = BaseModel.render_table(columns, data, styles)

        return result
    def nav():
        data = [
            ["Việc của bạn"],
            ["Việc bạn giao", 27]
        ]
        html = BaseModel.nav(data)
        return html

