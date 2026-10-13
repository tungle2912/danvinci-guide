# Khuôn mỗi mục ảnh (dùng chung cho mọi file tools/shots/*.md)

Mỗi ảnh là một mục, viết tiếng Việt, đúng khuôn:

### <ID> — `<ten-file>.png`
- **Ưu tiên:** P1 (thiếu là khó hiểu) · P2 (giúp rõ hơn nhiều) · P3 (có thì tốt)
- **Chèn vào:** `<đường dẫn md>` — ngay sau heading `## ...` (ghi đúng heading đang có trong file)
- **Trang Resolve:** Media / Cut / Edit / Fusion / Color / Fairlight / Deliver / Photo / hộp thoại ...
- **Chuẩn bị:** các bước đưa giao diện về đúng trạng thái (clip nào chọn, panel nào mở, menu nào xổ, giá trị nào đặt). Dùng project demo "So tay DaVinci - Demo", timeline "Demo - Vlog".
- **Khung chụp:** toàn cửa sổ / chỉ một vùng (mô tả vùng: ví dụ "panel Inspector bên phải, từ tiêu đề Transform tới hết Crop") / menu xổ.
- **Cần thấy rõ trong ảnh:** những nút, giá trị người đọc phải nhìn thấy.
- **Alt + chú thích:** `![alt](../../assets/img/<ten-file>.png)` và một câu chú thích in nghiêng ngắn.

Quy tắc:
- ID dạng `<khu>-<số>`, ví dụ `MED-01`, `EDT-07`.
- Tên file: chữ thường, gạch nối, tiền tố theo trang (`media-`, `cut-`, `edit-`, `fusion-`, `color-`, `fairlight-`, `deliver-`, `photo-`, `start-`, `flow-`).
- KHÔNG liệt kê ảnh đã có. Ảnh đã có nằm ở `assets/img/` (liệt kê bằng `ls assets/img`); kiểm tra xem trang đã nhúng chưa. Nếu một ảnh đã có nhưng chưa được nhúng vào trang phù hợp, ghi mục "Dùng lại" thay vì chụp mới.
- Ưu tiên ảnh cắt vùng (một panel, một menu) hơn ảnh toàn cửa sổ — trang tổng quan đã có ảnh toàn cửa sổ.
- Menu xổ và hộp thoại là cửa sổ riêng: ghi rõ "menu xổ — cần chụp toàn màn hình rồi cắt".
- Chỉ đề xuất ảnh cho thứ có thật trong Resolve 21 bản free (nếu là Studio, ghi rõ là không chụp được ở bản free và bỏ qua).
