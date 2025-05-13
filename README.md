# Fshare2GDrive (Python Edition)

Tải file từ Fshare.vn và upload trực tiếp lên Google Drive qua Rclone.

## Tính năng:
- Đăng nhập Fshare và lưu token
- Duyệt Google Drive bằng rclone và chọn thư mục đích
- Tải file từ Fshare (API)
- Kiểm tra trùng lặp và upload qua `rclone rcat`

## Cách sử dụng:
```bash
bash login.sh
python3 f_dl.py
```

## Yêu cầu:
- Python 3
- rclone (`curl https://rclone.org/install.sh | sudo bash`)
- Đã cấu hình remote tên `gdrive` bằng `rclone config`
