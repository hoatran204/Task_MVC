class InsertController:
    def InsertForm():
        html = f"""<div class="insert-form">
                        <div class="insert-form-modal-overlay">
                            <div class="insert-form-modal-container">
                                <div class="insert-form-modal-header">
                                    <h2 class="insert-form-modal-title">Thêm mới tài sản</h2>
                                    <button class="insert-form-close-button" onclick="hiddenInsertForm('.insert-form')">
                                        <i class="fas fa-times"></i>
                                    </button>
                                </div>
                                
                                <div class="insert-form-modal-content">
                                    <div class="insert-form-sidebar">
                                        <div class="insert-form-upload-area">
                                            <i class="fas fa-plus insert-form-upload-icon"></i>
                                            <div class="insert-form-upload-text">Tải lên ảnh</div>
                                        </div>
                                        <button class="insert-form-sidebar-item insert-form-active">
                                            <i class="fas fa-info-circle"></i>
                                            Thông tin chung
                                        </button>
                                        <button class="insert-form-sidebar-item">
                                            <i class="fas fa-shield-alt"></i>
                                            Bảo hành
                                        </button>
                                        <button class="insert-form-sidebar-item">
                                            <i class="fas fa-paperclip"></i>
                                            Tệp đính kèm
                                        </button>
                                    </div>

                                    <div class="insert-form-content">
                                        <div class="insert-form-section">
                                            <div class="insert-form-checkbox-group">
                                                <input type="checkbox" id="nhapHangLoat" class="insert-form-checkbox">
                                                <label for="nhapHangLoat" class="insert-form-checkbox-label">Nhập hàng loạt</label>
                                            </div>

                                            <div class="insert-form-row">
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Mã tài sản</label>
                                                    <input type="text" class="insert-form-input" placeholder="">
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Cỡ số mã</label>
                                                    <select class="insert-form-select">
                                                        <option>1</option>
                                                    </select>
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Số lượng</label>
                                                    <select class="insert-form-select">
                                                        <option>1</option>
                                                    </select>
                                                </div>
                                            </div>

                                            <div class="insert-form-grid">
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label insert-form-required">Tên tài sản</label>
                                                    <input type="text" class="insert-form-input" placeholder="">
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Giá mua</label>
                                                    <div class="insert-form-price-group">
                                                        <input type="text" class="insert-form-input insert-form-price-input">
                                                        <select class="insert-form-select insert-form-currency-select">
                                                            <option>VND</option>
                                                        </select>
                                                    </div>
                                                </div>

                                                <div class="insert-form-group">
                                                    <label class="insert-form-label insert-form-required">Loại tài sản</label>
                                                    <select class="insert-form-select">
                                                        <option value="">Chọn loại tài sản</option>
                                                    </select>
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Ngày mua</label>
                                                    <div class="insert-form-date-input">
                                                        <input type="date" class="insert-form-input">
                                                        <i class="fas fa-calendar-alt insert-form-date-icon"></i>
                                                    </div>
                                                </div>

                                                <div class="insert-form-group">
                                                    <label class="insert-form-label insert-form-required">Đơn vị quản lý</label>
                                                    <select class="insert-form-select">
                                                        <option value="">Chọn đơn vị</option>
                                                    </select>
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Series</label>
                                                    <input type="text" class="insert-form-input" placeholder="">
                                                </div>

                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Vị trí tài sản</label>
                                                    <select class="insert-form-select">
                                                        <option value="">Chọn vị trí</option>
                                                    </select>
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Mô tả</label>
                                                    <textarea class="insert-form-input insert-form-textarea" placeholder=""></textarea>
                                                </div>

                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Nhà cung cấp</label>
                                                    <select class="insert-form-select">
                                                        <option value="">Chọn nhà cung cấp</option>
                                                    </select>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="insert-form-section">
                                            <div class="insert-form-section-title">
                                                Bảo hành
                                                <i class="fas fa-chevron-down"></i>
                                            </div>
                                            
                                            <div class="insert-form-grid">
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Thời hạn bảo hành</label>
                                                    <input type="text" class="insert-form-input" placeholder="">
                                                </div>
                                                <div class="insert-form-group">
                                                    <label class="insert-form-label">Đơn vị</label>
                                                    <select class="insert-form-select">
                                                        <option value="">Chọn đơn vị</option>
                                                    </select>
                                                </div>
                                                <div class="insert-form-group insert-form-full-width">
                                                    <label class="insert-form-label">Điều kiện bảo hành</label>
                                                    <input type="text" class="insert-form-input" placeholder="">
                                                </div>
                                                <div class="insert-form-group insert-form-full-width">
                                                    <label class="insert-form-label">Hạn bảo hành</label>
                                                    <div class="insert-form-date-input">
                                                        <input type="date" class="insert-form-input">
                                                        <i class="fas fa-calendar-alt insert-form-date-icon"></i>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>

                                        <div class="insert-form-section">
                                            <div class="insert-form-section-title">
                                                Tệp đính kèm
                                                <i class="fas fa-chevron-down"></i>
                                            </div>
                                            <a href="#" class="insert-form-add-attachment">
                                                <i class="fas fa-plus"></i>
                                                Thêm tệp đính kèm
                                            </a>
                                        </div>
                                    </div>
                                </div>

                                <div class="insert-form-modal-footer">
                                    <button class="insert-form-btn insert-form-btn-secondary">Hủy</button>
                                    <button class="insert-form-btn insert-form-btn-primary">Lưu</button>
                                </div>
                            </div>
                        </div>
                    </div>
                """
        return html
