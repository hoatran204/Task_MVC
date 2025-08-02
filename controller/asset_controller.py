from model.asset_model import AssetModel
from flask import url_for
from controller.base_controller import BaseController

class AssetController:
    def add_content(type, sort_type, url, current_path):
        Tabdata = AssetModel.contentTabs_ar(type)
        main_table = AssetModel.contentTable_all(type)
        if sort_type:
            main_table = AssetModel.sort_contentTable(main_table, int(sort_type))
        return_url = f"?type={type}"
        if sort_type != None:
            return_url += f"&sort={sort_type}"
        html = BaseController.add_content(type, sort_type,url, current_path, Tabdata, main_table, return_url, "Tài sản", "Danh sách tài sản")
        return html
    def update_status(id, new_status):
        return AssetModel.update_status(new_status, id)