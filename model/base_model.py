class BaseModel:
    @staticmethod
    def render_table(columns, data, column_styles=None):
        # Bắt đầu table
        html = "<table>\n"
        html += "<thead>"

        # Header
        html += "  <tr>\n"
        for i, col in enumerate(columns):
            html += f"    <th>{col}</th>\n"
        html += "  </tr>\n"
        html += "</thead>\n"
        html += "<tbody>\n"
        
        # Data rows
        for row in data:
            html += "  <tr>"
            for i, cell in enumerate(row):
                html += f"<td"
                if column_styles and i <len(column_styles):
                    html += f" {BaseModel.style(column_styles[i], cell)}</td>"
                else:
                    html += f">{cell}"
            html += "  </tr>\n"
        html += "</tbody>\n"
        html += "</table>\n"
        return html
    @staticmethod
    def nav(data):
        html = "<div class='tabs-list'>"

        for i, row in enumerate(data):
            html += "<div class='tab-item'>"
            for j, cell in enumerate(row):
                if i < 1:
                    # kiểu A
                    if j == 0:
                        html += f"<strong>{cell}</strong>"
                    else:
                        html += f" ({cell})"
                else:
                    # kiểu B
                    html += f"<div class='dropdown-container'>"
                    html += f"<button class='dropdown-btn'>Khác<span class='dropdown-arrow'></span>"
                    html += f" </button></div>"
                    break
            html += "</div>"
        html += "</div>"
        return html
    @staticmethod
    def style(style, cell):
        if style == "user":
            return f" style='color:blue' ><img src={cell[0]}>{cell[1]}"
        else:
            return f">{cell}"
        
         
    