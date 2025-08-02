from model.base_model import BaseModel
class ContentModel:
    @staticmethod
    def render_contentTabs(data, type, url):
        html = ''
        if data != None:
            maintab = data["maintab"]
            html = f"""
                <div class="content-tabs">
                <div style='position:relative'><button onclick ="ShowAndHide('.content-tab-menu-section')" class = "content-tab"><i class="fa-solid fa-gear"></i></button>
                """
            for i, row in enumerate(maintab):
                html += f"""<button class = "content-tab" id = "maintab-{row[0]}" """
                
                if row[0] == type:
                    html += f"""--active'><strong>{row[1]}</strong>({row[2]})"""
                else:
                    html += f"""'><a style="all: unset;cursor: pointer;" href='/assignments?type={row[0]}'<strong>{row[1]}</strong>({row[2]})</a>"""
                html += "</button>"
            
            menusection, html1= ContentModel.menu_section(data, url, a=0, i=0)
            html += menusection
            html += f"""
            </div> </div>
                """
            html += html1
        
        return html
    @staticmethod
    def menu_section(data, url, a, i):
        print(url)
        html, html1 = "", ""
        setting = data["setting"]
        html += f"""<div class="content-tab-menu-section" id='content-tab-menu-section{a}{i}'"""
        if a != 0:
            html += " style='margin-left:130px;margin-top:-40px'"
        html += ">"

        for idx, cell in enumerate(setting):
            label, cell_type = cell[0], cell[1]

            # Trường hợp là menu chính
            if cell_type == "main":
                extra = cell[2] if len(cell) > 2 else {}
                html += "<div>"

                # Nếu có ShowAndHide
                if "ShowAndHide" in extra:
                    html += f"""
                        <div class="content-tab-menu-item" onclick="ShowAndHide('#content-showandhide-container{cell[3]}')">
                            <span>{label}</span>
                            <i class="fa-solid fa-chevron-right content-tab-chevron"></i>
                        </div>
                        {ContentModel.ShowAndHide(extra["ShowAndHide"], cell)}
                    """

                # Nếu là dạng nhóm (có lồng menu bên trong)
                elif "setting" in extra:
                    html += f"""
                        <div class="content-tab-menu-item" onclick="ShowAndHide('#content-tab-menu-section{a+1}{idx}')">
                            <span>{label}</span>
                            <i class="fa-solid fa-chevron-right content-tab-chevron"></i>
                        </div>
                    """
                    section, html1 = ContentModel.menu_section(extra, url, a + 1, idx)
                    html += section

                    # Nếu có nhóm GroupBy
                    if len(cell) > 3 and cell[3] == "groupby":
                        groupBy_ar = [[s[0], s[2]] for s in extra["setting"] if len(s) > 2]
                        if "sort" in url:
                            sort_index = BaseModel.extract_sort_manual(url, "sort")
                            html1 = ContentModel.GroupBy(sort_index, groupBy_ar, url)

                else:
                    # Không có cấu trúc con
                    html += f"""
                        <div class="content-tab-menu-item">
                            <span>{label}</span>
                            <i class="fa-solid fa-chevron-right content-tab-chevron"></i>
                        </div>
                    """

                html += "</div>"

            # Trường hợp là nút cuối (none)
            elif cell_type == "none":
                onclick = ""
                if len(cell) > 2:
                    param = f"&sort={cell[2]}"
                    base = BaseModel.replace(url, "sort") if "sort" in url else url
                    onclick = f"""onclick="window.location.href='{base}{param}'" """
                html += f"""
                    <div class="content-tab-menu-item" {onclick}>
                        <span>{label}</span>
                    </div>
                """

        html += "</div>"
        return html, html1

    @staticmethod
    def GroupBy(sort, ar, url):
        html =  f"""<div class="content-groupby-container" >
                <!-- Header dropdown -->
                <div class="content-groupby-header">
                    <select class = "content-groupby-select" onchange="changeAssignment(this)"> """
        for cell in ar:
            new_url = BaseModel.replace(url, "sort")
            if str(cell[1]) == sort:
                html += f"""<option value = "" disabled selected> Nhóm theo: {cell[0]} </option > """
            else:
                html += f"""<option value="{new_url}&sort={cell[1]}">{cell[0]}</option>"""
        html += f"""    
                    </select>
                    <div class="content-groupby-arrow"></div>
                    
                </div>

                <!-- Group by rows -->
                <div class="content-groupby-row">
                    <button class="content-groupby-delete" onclick="window.location.href='{BaseModel.replace(url, 'sort')}'"></button>
                </div>
            </div > """
        return html
    @staticmethod
    def ShowAndHide(data, cell):
        html = f"""<div class="content-showandhide-container" id ="content-showandhide-container{cell[3]}">

                <div class="content-showandhide-main">
                    <div class="content-showandhide-header">
                        <svg class="content-showandhide-gear" viewBox="0 0 24 24">
                            <path d="M12,8A4,4 0 0,0 8,12A4,4 0 0,0 12,16A4,4 0 0,0 16,12A4,4 0 0,0 12,8M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4Z"/>
                        </svg>
                        <h2 class="content-showandhide-title">{cell[0]}</h2>
                    </div>

                    <div class="content-showandhide-search">
                        <input 
                            type="text" 
                            class="content-showandhide-search-input" 
                            placeholder="Tìm kiếm..."
                        >
                    </div>

                    <div class="content-showandhide-options">"""
        for row in data:
            if row[1] != "":
                html += f"""
                            <div class="content-showandhide-option">

                                <input type = "checkbox" """
                if cell[3] == "tab":                 
                    html += f"""id ="id-maintab-{row[0]}" onclick="toggleContent(this)" """
                elif cell[3] == "collumn":
                    index = next((i for i, col in enumerate(data) if col[1] == row[1]), -1)
                    print(index)
                    print(cell[1])
                    html += f"""onclick ="toggleColumn({index}, this.checked)" """
                html +=            f""" class="content-showandhide-checkbox" checked>
                                <label for="{row[0]}" class="content-showandhide-label">{row[1]}</label>
                            </div>"""
        html += f"""
                    </div>

                    <button class="content-showandhide-default-btn">
                        Mặc định
                    </button>
                </div>
            </div > """
        return html   
    @staticmethod
    def collumn(TableData):
        TableClass = TableData["class"]
        html = "<tr>"
        for cls, text in TableData["collumn"]:
            if cls == "--checkbox":
                html += f"""<th class="{TableClass}-cell--checkbox">
                            <input type="checkbox" class="content-checkbox">
                        </th> """
            else:
                html += f"""<th class="{TableClass}{cls}">{text}</th>"""

        html += "</tr></thead>"
        return html
    @staticmethod
    def data(TableData):
        TableClass = TableData["class"]
        html = ""
        data = TableData["data"]
        for row in data:
            html += f"""<tr class="{TableClass}-row" >"""
            for i, cell1 in enumerate(row):
                style = TableData["style"][i]
                if style == "--checkbox":
                    html += f"""<td class="{TableClass}-cell content-table-cell--checkbox">
                        <input type="checkbox" class="content-checkbox">
                    </td>"""
                elif style == "-hidden":
                    html += f"""<td class="{TableClass}-cell-hidden">
                        {cell1}
                    </td > """
                elif style == "name":
                    html += f"""<td class = "{TableClass}-cell" onclick ="ShowAndHide('#content-information-card{row[2]}')" style="cursor: pointer;">
                    {cell1}</td>
                    """
                elif style == "option":
                    if cell1 and isinstance(cell1, list) and len(cell1) > 0 and isinstance(cell1[0], list):
                        html += f"""
                            <td class="{TableClass}-cell">
                            <form method="post" action="/update_status">
                                <select class="{TableClass}-cell-no-arrow" name="status" onchange="updateStatus(this)" data-id="{row[2]}" style='
                                background-color: {cell1[0][2]};
                                color: {cell1[0][3]};
                                border: 1px solid {cell1[0][3]};
                                padding: 4px 12px;
                                border-radius: 999px;
                                font-size: 11px;
                                font-weight: 500;
                                display: inline-block;
                                '>
                                <option value="{cell1[0][0]}" selected hidden>{cell1[0][1]}</option>
                            """

                        for option in cell1[1]:  # các lựa chọn còn lại
                            
                            html += f"""<option style='background-color: {option[2]};
                            color: {option[3]};
                            border: 1px solid {option[3]};' value='{option[0]}'>{option[1]}</option>"""

                        html += """
                            </select>
                        </form>
                        </td>
                        """
                    else:
                        html += f"<td></td>"
                else:
                    html += f"""<td class="{TableClass}-cell">
                        {cell1}
                    </td> """
            html += "</tr>"
        return html
    def content_information(tabledata):
        html = ""
        if "detail_data" in tabledata:
            data = tabledata["detail_data"]
            
            for row in data:
                html += f"""<div class="content-information-card" id="content-information-card{row["id"]}">
                        <div class="content-information-tabs">
                            <div class="content-information-tab active">Thông tin</div>
                            <div class="content-information-tab">Nhật ký</div>
                        </div>
                        <button class="content-information-close">×</button>
                        
                        <div class="content-information-body">
                            <div class="content-information-product">
                                <img src="https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=300&h=200&fit=crop&crop=center" alt="ThinkPad t14" class="content-information-image">
                                
                                <div class="content-information-details">
                                    <h3 class="content-information-title">{row["header"][0]}</h3>
                                    <div class="content-information-model">({row["header"][1]})</div>
                                    <span class="content-information-status">{row["header"][2]}</span>
                                </div>
                            </div>

                            <div class="content-information-actions">
                                <button class="content-information-action-btn">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
                                        <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                                        <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                                    </svg>
                                </button>
                                <button class="content-information-action-btn">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
                                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
                                        <rect x="9" y="9" width="6" height="6"/>
                                    </svg>
                                </button>
                                <button class="content-information-action-btn">
                                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2">
                                        <circle cx="12" cy="12" r="1"/>
                                        <circle cx="19" cy="12" r="1"/>
                                        <circle cx="5" cy="12" r="1"/>
                                    </svg>
                                </button>
                            </div>

                            <div class = "content-information-specs" > """
                for cell in row["information"]:
                    html += f"""
                                <div class="content-information-spec-group">
                                    <div class="content-information-spec-label">{cell[0]}</div>
                                    <div class="content-information-spec-value">{cell[1]}</div>
                                </div > """
                html += f"""
                                <div class="content-information-description">
                                    <div class="content-information-spec-label">{row["description"][0]}</div>
                                    <div class="content-information-description-text">
                                        {row["description"][1]}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div > """
        return html