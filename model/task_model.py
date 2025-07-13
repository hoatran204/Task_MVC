from model.base_model import BaseModel
from datetime import datetime

class TaskModel:
    @staticmethod
    def column_style():
        styles = ["hidden", "", "user", "datetime", "percent", "choose", "", "", "subs"]
        return styles

    @staticmethod
    def compare_time(progress,thoi_gian_kiem_tra:str, dinh_dang='%Y-%m-%d'):
        # Lấy thời gian hiện tại
        now = datetime.now().date()
        # Chuyển đổi chuỗi kiểm tra thành time
        check_time = datetime.strptime(thoi_gian_kiem_tra, dinh_dang).date()
        if progress == 100:
            return "Hoàn thành"
        elif now < check_time:
            return f"Chưa đến thời hạn"
        elif now > check_time:
            return f"Trễ hạn {abs((now - check_time).days)} ngày"
        else:
            return f"Đã đến hạn"


    @staticmethod
    def get_all_task():
        rows = BaseModel.Select(
            """
            mt.main_task_id, mt.task_name, u.full_name, u.avatar_url,
            mt.due_date, mt.progress, mt.status, mt.priority
            """,
            "main_tasks mt JOIN users u ON mt.assigner_id = u.user_id ORDER BY mt.main_task_id ASC;"
        )
        status = [
            ["Pending", "Chưa bắt đầu", "#e6f0ff", "#3399ff"],
            ["In Progress", "Đang thực hiện", "#fff3cd", "#ff9800"],
            ["Done","Hoàn thành", "#f3e8ff","#6f42c1"]
            ]
        tasks = []
        for row in rows:
            main_id = row['main_task_id']
            avatar_file = row["avatar_url"] or "default.png"
            avatar_url = f"/static/images/{avatar_file}"
            user_info = [avatar_url, row["full_name"]]
            
            # Thời gian gợi ý
            main_due_date = str(row["due_date"])
            main_progress = float(row["progress"])
            main_time = TaskModel.compare_time(main_progress, main_due_date)
            main_status,choose_main_status =  BaseModel.choose(row["status"],status)
            print(main_status)
            # load sub tasks
            subsets = BaseModel.Select(
                """
                st.sub_task_id, st.task_name, st.due_date,
                st.progress, st.status, st.priority
                """,
                f"sub_task st WHERE st.main_task_id={main_id}"
            )

            subs = []
            for sub in subsets:
                sub_id = f"sub-{main_id}-{sub['sub_task_id']}"
                sub_due_date = str(sub["due_date"])
                sub_progress = float(sub["progress"])
                sub_time = TaskModel.compare_time(sub_progress, sub_due_date)
                sub_status, choose_sub_status = BaseModel.choose(sub["status"],status)
                subs.append([
                    sub_id,
                    sub["task_name"],
                    user_info,
                    sub_due_date,
                    sub_progress,
                    [sub_status,choose_sub_status ],
                    sub["priority"],
                    sub_time
                ])

            tasks.append([
                f"main-{main_id}",
                row["task_name"],
                user_info,
                main_due_date,
                main_progress,
                [main_status,choose_main_status],
                row["priority"],
                main_time,
                subs
            ])

        return tasks
    def update_status(new_status, table, id):
        where=""
        if table == "main_tasks":
            where = "main_task_id="+id
        elif table == "sub_task":
            where = "sub_task_id="+id

        status = {"status": new_status}
        BaseModel.update(table, status, where)

