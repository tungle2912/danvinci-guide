# Bin, Power Bin, Smart Bin

Có **ba loại bin** trong Media Pool, mỗi loại nằm ở một khu riêng trong Bin List. Chúng hoạt động khác hẳn nhau.

Hiện/ẩn khu Power Bins và Smart Bins: **menu tuỳ chọn Media Pool** (ba chấm) → tick **Show Power Bins** / **Show Smart Bins**.

## 1. Bin thường

Thư mục thủ công. Kéo gì vào thì nó nằm đó.

- Tạo: chuột phải trong Bin List → **Add Bin**, hoặc `⇧⌘N`
- Lồng nhau bao nhiêu cấp cũng được

Mọi thứ nạp vào project mặc định nằm ở bin **Master** trên cùng.

### Cách chia bin cho một dự án vừa

```
Master
├── 01 Footage
│   ├── A-cam
│   └── B-roll
├── 02 Audio
├── 03 Nhạc
├── 04 Đồ hoạ
└── 05 Timelines
```

Đánh số ở đầu tên để bin luôn sắp đúng thứ tự.

## 2. Power Bin

**Mặc định ẩn.** Đây là bin **dùng chung cho mọi project trong cùng database**.

Dùng để chứa những thứ bạn cần ở mọi dự án:

- Mẫu chữ, lower third đã làm sẵn
- Logo, watermark
- Thư viện tiếng động
- Nhạc nền hay dùng
- LUT dưới dạng clip tham chiếu

Tạo: hiện khu Power Bins → chuột phải trong đó → **Add Bin**.

> Đây là tính năng tiết kiệm thời gian nhất mà ít người biết. Làm xong một bộ lower third đẹp, bỏ vào Power Bin, dự án sau mở ra là có sẵn.

## 3. Smart Bin

Không chứa clip. Nó là **bộ lọc tự chạy** — bạn đặt điều kiện, clip nào thoả thì tự xuất hiện.

Tạo: hiện khu Smart Bins → chuột phải → **Add Smart Bin** → đặt tên và điều kiện → **Create Smart Bin**.

### Ví dụ điều kiện hữu ích

| Muốn lọc | Đặt điều kiện |
|---|---|
| Mọi cảnh phỏng vấn | Keywords **contains** `phỏng vấn` |
| Mọi take tốt | Good Take **is** `true` |
| Footage quay 4K | Resolution **is** `3840x2160` |
| Clip dài trên 1 phút | Duration **greater than** `00:01:00:00` |
| Clip quay hôm nay | Date Created **is** hôm nay |

Ghép nhiều điều kiện bằng **All** (và) hoặc **Any** (hoặc).

### Smart Bin chỉ tốt bằng metadata của bạn

Smart Bin lọc dựa trên metadata. Nếu bạn không gõ metadata thì nó chỉ lọc được theo thông tin kỹ thuật (độ phân giải, fps, ngày tạo).

Muốn dùng Smart Bin hiệu quả, phải đầu tư vào [Metadata Editor](metadata.md) trước.

Nội dung Smart Bin **cập nhật tự động** — gắn thêm keyword cho một clip là nó xuất hiện ngay trong Smart Bin tương ứng.

## Gắn nhãn màu cho bin

Dự án nhiều bin thì gắn màu để nhận ra nhanh. Có **tám màu**.

Chuột phải bin → **Color Tag** → chọn màu.

Sau đó lọc theo màu để chỉ hiện các bin cùng nhãn.

Cách dùng thường thấy: đỏ cho footage chưa xem, vàng cho đang dựng, xanh cho đã xong.

## Xuất nhập bin và timeline

| Định dạng | Chứa gì | Lệnh |
|---|---|---|
| `.drb` | Một bin (DaVinci Resolve Bin) | Chuột phải bin → **Export Bin** |
| `.drt` | Một timeline (DaVinci Resolve Timeline) | Chuột phải timeline → **Timelines → Export → Timeline** |
| `.drp` | Cả project | **File → Export Project** |

`.drb` tiện khi muốn chuyển một bộ đồ hoạ sang dự án khác mà không mang cả project.

## Đồng bộ bin với thư mục trên ổ

Chuột phải bin → **Sync Bin with Folder**. Từ đó, file mới bỏ vào thư mục đó trên ổ sẽ **tự xuất hiện** trong bin.

Hữu ích khi làm việc nhóm: người quay đổ thẻ vào thư mục chung, bin của bạn tự cập nhật.
