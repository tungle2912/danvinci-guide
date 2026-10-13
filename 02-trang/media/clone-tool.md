# Clone Tool — backup thẻ nhớ

`★★☆ Thường dùng`

**Là gì:** công cụ copy thẻ nhớ, SSD hay ổ cứng ra **một hoặc nhiều ổ đích**, rồi **kiểm tra lại** từng file bằng checksum.

**Dùng khi:** mỗi lần đổ thẻ sau buổi quay, **trước khi** nạp vào project.

**Mở:** bấm nút **Clone Tool** (nút thứ ba) trên Interface Toolbar ở đầu trang Media. Bấm lần nữa để ẩn.

Đây là công cụ ít người biết nhưng nên dùng mỗi lần đổ thẻ.

---

## Vì sao không copy bằng Finder

Kéo thả trong Finder **không kiểm tra** dữ liệu sau khi copy. Một bit lỗi trong file 4K thì bạn chỉ phát hiện lúc dựng, khi thẻ đã bị format.

Clone Tool tính **checksum** — một "dấu vân tay" — cho file gốc và file copy, rồi so hai cái. Khớp nghĩa là bản copy giống hệt bản gốc.

| | Finder | Clone Tool |
|---|---|---|
| Copy ra nhiều ổ một lần | Phải kéo nhiều lần | Một job, nhiều đích |
| Kiểm tra file sau khi copy | Không | Có, theo checksum |
| Ghi báo cáo | Không | Có, ở mỗi ổ đích |
| Giữ cấu trúc thư mục | Tuỳ cách kéo | Luôn giữ |

---

## Các nút của panel Clone Tool

| Nút / vùng | Vị trí | Làm gì | Mức |
|---|---|---|---|
| **Add Job** | Góc dưới trái panel | Tạo một job copy mới | ★★★ |
| **Drop source here** | Trong job | Ô thả nguồn — thẻ nhớ hoặc thư mục gốc | ★★★ |
| **Drop destination here** | Trong job | Ô thả đích. Thả được nhiều đích | ★★★ |
| **Clone** | Trong panel | Bắt đầu copy | ★★★ |
| **Menu tuỳ chọn** | Option menu của panel | **Preserve Folder Name** và menu con **Checksum** | ★★☆ |

---

## Cách dùng

`★★★ Hằng ngày` với người quay nhiều.

**Cách kéo thả:**

1. Bấm nút **Clone Tool** trên Interface Toolbar.
2. Bấm **Add Job**. Một job mới hiện ra, có chữ hướng dẫn.
3. Từ [Media Storage](media-storage.md), kéo **thẻ nhớ** (hoặc thư mục gốc) vào ô **Drop source here**.
4. Kéo **thư mục đích** vào ô **Drop destination here**.
5. Muốn nhiều bản: kéo thêm ổ đích khác vào.
6. Bấm **Clone**.

**Cách nhanh bằng chuột phải:**

1. Trong Media Storage, chuột phải thẻ nhớ → **Set As Clone Source**. Job tự được tạo.
2. Chuột phải thư mục đích → **Set As Clone Destination**. Lặp lại cho mỗi ổ đích.
3. Bấm **Clone**.

**Ví dụ — đổ thẻ sau buổi quay:** tạo trước thư mục `2026-10-13_quay-cafe/A001` trên ổ làm việc và ổ backup. Đặt thẻ làm source, hai thư mục `A001` làm destination. Bấm **Clone**, chờ xong rồi mới rút thẻ.

### Preserve Folder Name

**Là gì:** giữ lại **tên thư mục ngoài cùng** của nguồn khi copy.

**Bật khi:** muốn ổ đích có thêm một lớp thư mục mang tên thẻ (ví dụ `A001`), thay vì nội dung thẻ đổ thẳng vào thư mục đích.

**Bật ở:** menu tuỳ chọn của panel → **Preserve Folder Name**.

> Cấu trúc thư mục **bên trong** luôn được giữ nguyên, dù bật hay tắt mục này.

### Chọn kiểu checksum

Menu tuỳ chọn → **Checksum**. Kiểm tra càng chặt thì copy càng chậm.

| Kiểu | Tốc độ | Độ chắc | Khi nào chọn |
|---|---|---|---|
| **None** | Nhanh nhất | Không kiểm tra | Không nên dùng cho footage gốc |
| **File Size** | Rất nhanh | Thấp, chỉ so dung lượng | Copy tạm, không quan trọng |
| **CRC 32** | Nhanh hơn MD5 | Kém MD5 | Ít khi cần |
| **MD5** | Vừa | Khá | **Mặc định**. Đủ cho hầu hết dự án |
| **SHA 256** / **SHA 512** | Chậm | Cao nhất | Hợp đồng yêu cầu chuẩn này |
| **XXHASH64** | Nhanh nhất trong các kiểu có kiểm tra thật | Tốt | Đổ hàng terabyte mỗi ngày |

> **Không chắc thì để MD5.** Đổ nhiều thẻ dung lượng lớn mà thấy chậm thì đổi sang **XXHASH64**.

---

## Copy ra nhiều ổ một lúc

Thêm nhiều Destination cho cùng một job. Resolve copy ra tất cả và kiểm tra từng bản.

Quy tắc an toàn cho footage: **ba bản, trên hai loại thiết bị, một bản để nơi khác**. Clone Tool lo được hai bản đầu trong một lần chạy. Bản thứ ba nên để ở nơi khác — ổ mang về nhà, hoặc lưu trữ đám mây.

**Ví dụ:** destination 1 là SSD làm việc, destination 2 là ổ HDD backup. Xong cắm ổ HDD về nhà, chép thêm một bản nữa.

---

## File MHL

Sau khi clone, Resolve ghi một **báo cáo checksum** vào **thư mục gốc của mỗi ổ đích**. Báo cáo ghi checksum của từng file, xác nhận bản copy khớp với bản gốc. Dân DIT hay gọi chung loại file này là file MHL (Media Hash List).

**Dùng để làm gì:**

- Bằng chứng cho khách hoặc đạo diễn rằng footage đã được backup đủ.
- Về sau nghi ổ hỏng, so lại checksum để biết file nào bị lỗi.

> Giữ báo cáo này cùng footage. Đừng xoá khi dọn ổ.

---

## Lưu ý

- Clone **toàn bộ thẻ**, giữ nguyên cấu trúc. Đừng copy lẻ từng file video — nhiều máy quay (nhất là máy chuyên nghiệp) cần nguyên cấu trúc thư mục để đọc đúng metadata.
- Clone xong mới format thẻ. Nên mở thử vài file trên ổ đích trước khi format.
- Copy về **ổ nhanh** trước khi nạp. Resolve không copy file vào project mà chỉ nhớ đường dẫn — xem [Nạp media](nap-media.md).
- Nạp media từ **ổ đích**, không nạp thẳng từ thẻ. Rút thẻ ra là clip sẽ bị offline.
