from flask import Blueprint, render_template, request, redirect, url_for
from controller.base_controller import BaseController
from controller.task_controller import TaskController
from controller.asset_controller import AssetController
from controller.base.content_controller import ContentController
from controller.employee_controller import EmployeeController

from flask_babel import _
import json
from flask import jsonify


routes = Blueprint('routes', __name__)
    
@routes.route("/update-status", methods=["POST"])
def update_status():
    data = request.get_json()            
    task_id = data.get("id")             
    new_status = data.get("status")
    referer = request.headers.get("Referer", "")
    BaseController.update_status(task_id, new_status, referer)
    return jsonify({"message": "Đã cập nhật", "from": referer})


@routes.route("/assignments")
def assignments():
    url = request.url
    current_path = url.strip("/")
    action_type = request.args.get("type", "all")
    sort_type = request.args.get("sort", None)
    html = AssetController.add_content(action_type, sort_type, request.url, current_path)
    return render_template("base.html",
                        result=html,
                        headTitle="Tài sản")
@routes.route("/employees")
def employees():
    current_path = request.path.strip("/")
    action_type = request.args.get("type", "all")
    sort_type = request.args.get("sort", None)
    html = EmployeeController.add_content(action_type, sort_type, request.url, current_path)
    return render_template("base.html",
                        result=html,
                        headTitle="Nhân viên")
@routes.route("/test")
def assignments1():
    url = "?type=allsort=4"
    sort = BaseController.test(url, "sort")
    print("Kết quả:", sort)
    return render_template("base.html")


