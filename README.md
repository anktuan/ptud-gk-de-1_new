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
cd blog-flask
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
python main.py
```
Mặc định server sẽ chạy tại: **http://127.0.0.1:5000/**

---

## Hướng Dẫn Sử Dụng
### 1. Đăng ký & Đăng nhập
- Truy cập trang **/register** để tạo tài khoản.
- Sau khi đăng ký, truy cập **/login** để đăng nhập.

### 2. Viết Bài
- Truy cập trang **/new_post** để tạo bài viết mới.

### 3. Bình Luận Bài Viết
- Dưới mỗi bài viết, nhập bình luận và nhấn "Gửi".

### 4. Theo Dõi Bài Viết
- Nhấn nút "Theo dõi" để lưu bài viết vào danh sách theo dõi.

---

## Công Nghệ Sử Dụng
- **Backend**: Flask, Flask-SQLAlchemy, Flask-Login
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap, Jinja2
- **Hình ảnh ngẫu nhiên**: [Picsum Photos](https://picsum.photos/)

---

## Liên Hệ
Nếu bạn có thắc mắc hoặc góp ý, vui lòng liên hệ:
- Email: anhtuan59gz@gmail.com


