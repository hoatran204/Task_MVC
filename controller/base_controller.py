from model.base_model import BaseModel
from controller.base.content_controller import ContentController
from controller.base.insert_controller import InsertController
from flask import url_for,request, redirect

class BaseController:
    def header1(title):
        
        html = f"""
        <header class="header-container">
            <div class="header-wrapper">
                <div class="header-content">
                    <div class="header-left">
                        <h1 class="header-title">{title}</h1>
                    </div>

                    <div class="header-right">
                        <!-- Message Icon -->
                        <div class="header-icon header-message-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M8 10H16M8 14H13M6 20L4 21V5C4 3.89543 4.89543 3 6 3H18C19.1046 3 20 3.89543 20 5V17C20 18.1046 19.1046 19 18 19H6Z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>

                        <!-- Notification Icon with Badge -->
                        <div class="header-icon header-notification-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <path d="M15 17H20L18.5951 15.5951C18.2141 15.2141 18 14.6973 18 14.1585V11C18 8.38757 16.3304 6.16509 14 5.34142V5C14 3.89543 13.1046 3 12 3C10.8954 3 10 3.89543 10 5V5.34142C7.66962 6.16509 6 8.38757 6 11V14.1585C6 14.6973 5.78595 15.2141 5.40493 15.5951L4 17H9M15 17V18C15 19.6569 13.6569 21 12 21C10.3431 21 9 19.6569 9 18V17M15 17H9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                            <div class="header-notification-badge">1</div>
                        </div>

                        <!-- Profile Avatar -->
                        <div class="header-profile">
                            <div class="header-avatar">A</div>
                        </div>
                    </div>
                </div>
            </div>
        </header>"""
        return html
    def content(title, tabdata, tabledata,type, url, return_url):
        all_data=tabledata["data"]
        page = int(request.args.get('page', 1))
        items_per_page = 10

        start = (page - 1) * items_per_page
        end = start + items_per_page
        paged_data = all_data[start:end]
        new_table_data = {
            "class": tabledata["class"],
            "collumn": tabledata["collumn"],
            "data": paged_data,
            "style": tabledata["style"]
        }
        contentHeader = ContentController.contentHeader(title)
        contentTabs = ContentController.contentTabs(tabdata, type, return_url)
        contentTable = ContentController.contentTable(new_table_data)
        contentPagination = ContentController.contentPagination(tabledata,url,current_page=page,
                                                items_per_page=items_per_page)
        contentInfor = ContentController.in4(tabledata)
        html = f"""<div style="display:flex; align-items: flex-start;">
        <div class="content-wrapper" style="flex:1">
        {contentHeader}
        {contentTabs}
        {contentTable}
        {contentPagination}
        

        
        </div>{contentInfor}</div>
        """
        return html

    def bindingdata(columns,data,styles, class_table):

        
        result = BaseModel.render_table(columns, data, styles, class_table)

        return result
    
    def action():
        html = f"""
        <div class="action-container">

        <!-- Compact version -->
        <div class="action-action-bar action-action-bar--compact">
            <button class="action-close-btn"><i class="fas fa-times"></i></button>
            <span class="action-title">Đã chọn: 2</span>
            <button class="action-action-btn action-check-btn"><i class="fas fa-check"></i></button>
            <button class="action-action-btn action-delete-btn"><i class="fas fa-trash"></i></button>
            <button class="action-action-btn action-menu-btn"><i class="fas fa-ellipsis-v"></i></button>
        </div>
     </div>"""
        return html
    def update_status(id, new_status, referer):
        from controller.task_controller import TaskController
        from controller.asset_controller import AssetController
        if referer == "http://127.0.0.1:5000/task":
            TaskController.update_status(id, new_status)
        elif "assignments" in referer:
            AssetController.update_status(id, new_status)
    def InsertForm():
        html = InsertController.InsertForm()
        return html

    def leftbar(page):
        ar = BaseModel.main_leftbar_ar()
        html = f"""
        <div class="leftbar-container">
            <div class="leftbar-header">
                <div class="leftbar-logo">J</div>
                <div class="leftbar-brand">Jiffy</div>
            </div>
            
            <nav class="leftbar-nav">
                <ul class = "leftbar-menu"> """
        for row in ar:
            if len(row) < 4:
                html += f"""<li class="leftbar-menu-item"
                """
                if str(row[1]) == page:
                    html += " style = 'background-color:#3b82f6', color:white"
                html += f"""
                            >
                        <a href="{row[1]}" class="leftbar-menu-link" """
                if str(row[1]) == page:
                    html += " style = 'color:white '"
                html += f""">
                            <div class="leftbar-menu-icon">
                                <i class="{row[2]}"></i>
                            </div>
                            <span class = 'leftbar-menu-text'>{row[0]}</span>
                        </a>
                    </li> """
            else:
                html += f"""<li class="leftbar-menu-item leftbar-expanded">
                        <a href="#" class="leftbar-menu-link
                        """
                if str(row[1]) == page:
                    html += "-active"
                html += f"""
                " onclick="toggleSubmenu(this)">
                            <div class="leftbar-menu-icon">
                                <i class="fas fa-cog"></i>
                            </div>
                            <span class="leftbar-menu-text">Cài đặt</span>
                            <div class="leftbar-dropdown-arrow">
                                <i class="fas fa-chevron-right"></i>
                            </div>
                        </a>
                        <ul class = "leftbar-submenu" > """
                for cell in row[3]:
                    html += f"""        
                        
                            <li class="leftbar-submenu-item">
                                <a href="#" class="leftbar-submenu-link">
                                    <div class="leftbar-submenu-bullet"></div>
                                    <span onclick="window.location.href='/{cell[1]}'">{cell[0]}</span>
                                </a>
                            </li > """
                html += "</ul></li>"       
        html += f"""
                        
                </ul>
            </nav>
        </div>
        """
       
        return html
    
    def add_content(type, sort_type,url, current_path, Tabdata, main_table, return_url,a,b):
        html = BaseController.header1(a)
        html += BaseController.leftbar(current_path)
        html += BaseController.content(b, Tabdata, main_table, type, url,return_url)
        html += BaseController.InsertForm()
        return html
