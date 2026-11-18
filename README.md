# Đồ Án Cơ Sở Ngành: Sửa lỗi chính tả tiếng Việt bằng khoảng cách chỉnh sửa

- **Sinh viên thực hiện:** Nguyễn Tuấn Thanh – MSSV: 66133391
- **Giảng viên hướng dẫn:** ThS. Ngô Nguyễn Tường Nghi
- **Ngôn ngữ & Môi trường:** Python 3 (Google Colab)

## 1. Cấu trúc thư mục
- `edit_distance.py`: Cài đặt lõi thuật toán Levenshtein chuẩn và Weighted Damerau-Levenshtein bằng Quy hoạch động (không dùng thư viện ngoài).
- `test_edit_distance.py`: Bộ Unit Test kiểm chứng độ chính xác với các cặp từ tính tay.
- `data/tudien_amtiet.txt`: Từ điển âm tiết tiếng Việt chuẩn (8.875 âm tiết).
- `data/corpus_mau.txt`: Kho ngữ liệu văn bản tiếng Việt phục vụ đếm tần suất N-gram (64.668 dòng, 158.507 tokens).

## 2. Hướng dẫn chạy kiểm thử (Unit Test)
```bash
python -m unittest -v test_edit_distance.py
