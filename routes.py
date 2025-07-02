from flask import Blueprint, render_template, request, redirect, url_for
from controller.base_controller import BaseController
from flask_babel import _
import json

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    result = BaseController.bindingdata()
    html = BaseController.nav()
    return render_template(
        "task.html",
        result=result,
        title="Công việc",
        header="Danh sách công việc",
        nav = html
    )
