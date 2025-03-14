# ptud-gk-de-1_new
# Blog Flask Project

## Thông Tin Tác Giả
- **Tên**: Trần Anh Tuấn
- **Email**: anhtuan59gz@gmail.com
- **Mô tả**: Dự án blog cá nhân dùng Flask và SQLite, hỗ trợ chức năng viết bài, bình luận và theo dõi.

---

## Giới Thiệu
Dự án Blog này được xây dựng bằng **Flask (Python)** và **SQLite**, cho phép người dùng:
- Viết bài blog
- Bình luận bài viết
- Theo dõi bài viết
- Hiển thị danh sách bài viết dạng thẻ (**Card-Based UI**)

Hình ảnh trong bài viết được lấy ngẫu nhiên từ [Picsum Photos](https://picsum.photos/).

---

## Hướng Dẫn Cài Đặt
### Yêu Cầu
- **Python** ≥ 3.8
- **pip** và **virtualenv** (tùy chọn)

### 1. Clone Repository
```bash
git clone https://github.com/anktuan/ptud-gk-de-1_new.git
```

### 2. Tạo Virtual Environment (Không bắt buộc)
```bash
python -m venv venv
source venv/bin/activate  # Trên macOS/Linux
venv\Scripts\activate    # Trên Windows
```

### 3. Cài Đặt Thư Viện Cần Thiết
```bash
pip install -r requirements.txt
```

### 4. Chạy Server 
```bash
khởi tạo dữ liệu ban đầu gồm admin, user test
python .\generate_data.py
chạy server 
python main.py
```
Mặc định server sẽ chạy tại: **http://127.0.0.1:5000/**

---

## Hướng Dẫn Sử Dụng
### 1. Đăng ký & Đăng nhập
- Truy cập trang **/Đăng ký** để tạo tài khoản.
- Sau khi đăng ký, truy cập **/Đăng nhập** để đăng nhập.
- **/BLOG APP** để trở về trang chủ.

### 2. Viết Bài
- Truy cập trang **/Quản lý bài viết**
- Để tạo bài viết mới **/Thêm bài viết**
- Để xóa bài viết **/Xóa bài viết**

### 4. Theo Dõi Bài Viết
- Nhấn nút "Theo dõi" để lưu bài viết vào danh sách theo dõi.
- Nhấn nút "Bỏ theo dõi" để xóa viết vào danh sách theo dõi.
---

## Công Nghệ Sử Dụng
**Backend Framework:**
Flask (Python web framework)
Flask-Login (quản lý xác thực người dùng)
Flask-SQLAlchemy (ORM để tương tác với database)
**Database:**
SQLite (hệ quản trị cơ sở dữ liệu)
SQLAlchemy (ORM - Object Relational Mapping)
**Frontend:**
HTML5
CSS3
JavaScript (ES6+)
Bootstrap 5.3.3 (CSS framework)
Font Awesome 6.4.2 (icon library)
jQuery 3.6.0 (JavaScript library)
- **Hình ảnh ngẫu nhiên**: [Picsum Photos](https://picsum.photos/)

---

## Liên Hệ
Nếu bạn có thắc mắc hoặc góp ý, vui lòng liên hệ:
- Email: anhtuan59gz@gmail.com


