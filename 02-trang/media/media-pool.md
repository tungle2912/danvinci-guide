# Media Pool — kho clip

Vùng dưới trang Media. Chứa **mọi clip bạn đã nạp** và **mọi timeline bạn tạo**.

Media Pool xuất hiện ở cả trang Cut, Edit, Fusion, Color và Fairlight — cùng một kho, chỉ là hiển thị nhỏ hơn. Ở trang Media nó được dành nhiều chỗ nhất nên đây là nơi để sắp xếp.

> Resolve tách bạch **media nguồn** và **timeline**. Cả hai đều nằm trong Media Pool nhưng được quản lý riêng. Nhờ vậy bạn thay thế, nối lại, chuyển đổi offline/online media mà không đụng tới bản dựng.

## Nút Bin List

Nằm ở **góc trên trái Media Pool**. Bật/tắt cột danh sách bin bên trái.

- **Mở** — thấy toàn bộ cây bin, dễ kéo clip từ bin này sang bin kia.
- **Đóng** — không thấy bin, chỉ thấy nội dung bin đang chọn. Rộng chỗ hơn.

Chi tiết về bin: [Bin, Power Bin, Smart Bin](bin.md).

## Ba kiểu hiển thị

Ba icon ở góc trên phải Media Pool:

### Thumbnail view
Hiện ảnh đại diện. Rê chuột ngang thumbnail là xem nhanh (skim) toàn bộ clip.

Kéo thả để sắp xếp thủ công theo ý mình.

### List view
Dạng bảng nhiều cột, giống List view của Media Storage nhưng thêm các cột **sửa được trực tiếp**: **Name, Description, Keyword, Comments**.

Gõ thẳng vào ô là xong, không cần mở Metadata Editor.

### Metadata view
Hiện thumbnail kèm một khối metadata bên cạnh mỗi clip. Hợp khi soát lại ghi chú của cả bin.

> Kiểu hiển thị **đặt riêng cho từng bin được**. Bin footage để Thumbnail, bin audio để List — Resolve nhớ cho từng bin.

## Media Pool Tabs

Mở nhiều bin thành các tab cạnh nhau trong cùng một Media Pool, giống tab trình duyệt. Đỡ phải nhảy qua lại.

## Mở bin ra cửa sổ riêng

Chuột phải bin trong Bin List → **Open As New Window**.

Cửa sổ mới là một Media Pool đầy đủ, có Bin list, Power Bins, Smart Bins riêng. Mở bao nhiêu cửa sổ cũng được.

Rất hợp khi dùng hai màn hình: kéo cửa sổ bin sang màn phụ trong lúc Resolve vẫn ở chế độ một màn hình.

## Tìm clip

Icon kính lúp ở góc trên Media Pool. Tìm theo tên, theo metadata, hoặc lọc riêng clip / timeline.

Một số lệnh tìm hữu ích trong menu chuột phải:

| Lệnh | Làm gì |
|---|---|
| **Find in Media Pool** | Từ clip trên timeline, nhảy về đúng clip gốc trong pool |
| **Reveal in Finder** | Mở thư mục chứa file trên máy |
| **Reveal in Media Storage** | Nhảy tới đúng vị trí trong Media Storage |

## Khôi phục timeline đã xoá

**Menu tuỳ chọn Media Pool** (ba chấm) → **Deleted Timeline Backups**.

Xem các timeline đã xoá và các bản backup của từng timeline, chọn bản để khôi phục hoặc xoá hẳn.

Đây là cứu cánh khi bạn lỡ xoá nhầm một timeline đã dựng xong.

## Xoá media khỏi project

| Việc | Cách |
|---|---|
| Xoá clip khỏi Media Pool | Chọn clip → `Delete` (không xoá file trên ổ) |
| Xoá mọi clip không dùng tới | Menu tuỳ chọn Media Pool → **Remove Unused Clips** |

**Remove Unused Clips** rất hữu ích trước khi giao project: nó bỏ hết footage bạn nạp vào nhưng cuối cùng không dùng.
