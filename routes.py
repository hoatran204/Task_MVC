from flask import Blueprint, render_template, request, redirect, url_for
from controller.base_controller import BaseController
from controller.task_controller import TaskController
from controller.asset_controller import AssetController
from flask_babel import _
import json
from flask import jsonify


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    result = AssetController.get_asset()
    html = BaseController.nav()
    return render_template(
        "base.html",
        result=result,
        title="Tài sản",
        header="Danh sách Tài sản",
        nav = html
    )
@routes.route('/task')
def index1():
    
    result = TaskController.get_tasks()
    html = BaseController.nav()
    return render_template(
        "base.html",
        result=result,
        nav = html
    )
@routes.route('/asset_allocation')
def index2():
    result = AssetController.add_asset()
    return render_template(
        "base.html",
        result=result,
        title="Cấp phát tài sản",
        header="Cấp phát tài sản"
    )
@routes.route("/update-status", methods=["POST"])
def update_status():
    data = request.get_json()
    task_id = data.get("id")
    new_status = data.get("status")
    referer = request.headers.get("Referer", "")
    print(referer)
    BaseController.update_status(task_id,new_status,referer)

    # Trả về JSON để JS xử lý
    return jsonify({"message": "Đã cập nhật", "from": referer})
@routes.route("/add_asset", methods=["POST"])
def add_asset():
    last_data = BaseController.last_data(
        AssetController.assets_alocation(),
        AssetController.return_asset_data()
    )

    print("🔥 Dữ liệu cuối cùng gửi vào DB:")
    for row in last_data:
        print(row)

    AssetController.add_data(last_data)
    return render_template("base.html")
