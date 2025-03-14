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

## Hướng dẫn cài đặt

1. Clone repository:
```bash
git clone https://github.com/anktuan/ptud-gk-de-1_new.git
cd ptud-gk-de-1_new
```

2. Tạo môi trường ảo:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

4. Chạy ứng dụng:
```bash
python main.py
```

5. Truy cập ứng dụng:
- Mở trình duyệt và truy cập: http://localhost:5000

## Cấu trúc thư mục

flask-tiny-app/
├── website/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── auth.py
│   ├── posts.py
│   ├── admin.py
│   ├── static/
│   └── templates/
├── instance/
├── venv/
├── main.py
├── requirements.txt
└── README.md

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


