from model.base.content_model import ContentModel
from urllib.parse import urlencode, parse_qs, urlparse
class ContentController:
    def contentHeader(title):
        html = f"""<div class="content-header">
            <h1 class="content-title">{title}</h1>
            <div class="content-search-container">
                <div class="content-search-wrapper">
                    <input type="text" class="content-search-input" placeholder="Tìm kiếm">
                    <span class="content-search-icon"><i class="fas fa-search"></i></span>
                </div>
                <button class="content-filter-btn" ><i class="fas fa-filter"></i></button>
                <button class="content-add-btn" onclick="showInsertForm('.insert-form')"><i class="fas fa-plus"></i> 
                </button><button class="content-filter-btn">
                <i class="fas fa-chevron-down"></i></button>
            </div>
        </div>
        """
        return html
    def contentTabs(data,type, url):

        html = ContentModel.render_contentTabs(data,type,url)
        return html
    
    @staticmethod
    def contentTable(TableData):
        TableClass = TableData["class"]
        collumn = ContentModel.collumn(TableData)
        data = TableData["data"]
        TableDT = ContentModel.data(TableData)
        # content-table
        html = f"""<div class="{TableClass}-container"> 
            <table class="{TableClass}" id="myTable">
                <thead class="{TableClass}-header">
                    {collumn}
                </thead>
                <tbody>
                    <tr>{TableDT}</tr>
                </tbody>
            </table>
        </div > """
        
        return html

    @staticmethod
    def contentPagination(TableData, request_url, current_page, items_per_page):
        data = TableData["data"]
        total_items = len(data)
        total_pages = (total_items + items_per_page - 1) // items_per_page

        start_item = (current_page - 1) * items_per_page + 1
        end_item = min(start_item + items_per_page - 1, total_items)

        # Lấy query string hiện tại từ request_url (nếu có)
        query_params = {}
        if request_url:
            parsed_url = urlparse(request_url)
            query_params = parse_qs(parsed_url.query)

        html = f"""
        <div class="content-pagination">
            <div class="content-pagination-info">
                Từ {start_item} - {end_item} trên tổng {total_items}
            </div>
            <div class="content-pagination-controls">
        """

        # Hàm phụ để tạo URL với query string được cập nhật
        def build_url(page_num):
            # Sao chép query_params và cập nhật tham số 'page'
            new_params = query_params.copy()
            new_params['page'] = [str(page_num)]  # Đảm bảo page là chuỗi
            return f"?{urlencode(new_params, doseq=True)}"

        # Nút về đầu
        if current_page > 1:
            html += f'<a href="{build_url(1)}" class="content-page-btn"><i class="fas fa-angle-double-left"></i></a>'
            html += f'<a href="{build_url(current_page-1)}" class="content-page-btn"><i class="fas fa-chevron-left"></i></a>'
        else:
            html += f'<button disabled class="content-page-btn"><i class="fas fa-angle-double-left"></i></button>'
            html += f'<button disabled class="content-page-btn"><i class="fas fa-chevron-left"></i></button>'

        # Các nút số trang
        for p in range(1, total_pages + 1):
            active = 'content-page-btn--active' if p == current_page else ''
            html += f'<a href="{build_url(p)}" class="content-page-btn {active}">{p}</a>'

        # Nút tiếp
        if current_page < total_pages:
            html += f'<a href="{build_url(current_page+1)}" class="content-page-btn"><i class="fas fa-chevron-right"></i></a>'
            html += f'<a href="{build_url(total_pages)}" class="content-page-btn"><i class="fas fa-angle-double-right"></i></a>'
        else:
            html += f'<button disabled class="content-page-btn"><i class="fas fa-chevron-right"></i></button>'
            html += f'<button disabled class="content-page-btn"><i class="fas fa-angle-double-right"></i></button>'

        html += "</div></div>"
        return html
    def in4(tabledata):
        return ContentModel.content_information(tabledata)
