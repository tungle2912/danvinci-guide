# Tạo project đúng ngay từ đầu

Phần lớn rắc rối về sau (video giật, tiếng lệch hình, xuất ra mờ) bắt nguồn từ năm phút đầu tiên. Làm đúng ở đây thì về sau không phải sửa.

## Bước 1 — Frame rate, thứ không sửa được về sau

Mở **Project Settings** (`⇧9`) → **Master Settings** → **Timeline frame rate**.

Đặt đúng bằng frame rate bạn quay. Quay 24 thì để 24, quay 30 thì để 30.

> **Đây là thiết lập quan trọng nhất và là thứ duy nhất không đổi được sau khi timeline đã có clip.** Nếu sai, bạn phải tạo timeline mới và dựng lại.

Khi bạn kéo clip đầu tiên vào timeline, Resolve sẽ hỏi có đổi frame rate project cho khớp không. **Luôn chọn Change.**

Cách an toàn hơn: tạo project, nạp clip vào Media Pool trước, chuột phải vào clip → **Create Timeline Using Selected Clips**. Resolve tự lấy đúng mọi thông số từ clip.

## Bước 2 — Độ phân giải

Cùng chỗ đó, **Timeline resolution**:

| Làm gì | Đặt |
|---|---|
| Video ngang thông thường | 1920×1080 |
| Video 4K | 3840×2160 |
| TikTok, Reels, Shorts | 1080×1920 |

Timeline resolution và resolution lúc xuất là **hai thứ khác nhau**. Bạn hoàn toàn có thể dựng ở 1080 cho nhẹ máy rồi xuất ra 4K — xem [Tối ưu hiệu năng](../04-tham-khao/hieu-nang.md).

## Bước 3 — Chọn cách quản lý màu

Vào **Project Settings → Color Management → Color science**. Có hai hướng, **chọn một, đừng dùng cả hai**:

### DaVinci YRGB (mặc định)
Resolve không tự chuyển đổi gì cả. Bạn tự xử lý bằng node **Color Space Transform** trong trang Color.

Chọn cái này nếu: bạn quay toàn bộ ở một máy, muốn nhìn rõ từng bước chuyển đổi, hoặc muốn chỉnh sáng tối *trước* khi chuyển đổi màu.

### DaVinci YRGB Color Managed
Resolve tự nhận diện footage và tự chuyển đổi. Bạn khai báo ba thứ: clip quay ở không gian màu nào, muốn chỉnh ở không gian nào, xuất ra không gian nào.

Chọn cái này nếu: bạn trộn footage từ nhiều máy khác nhau, hoặc quay LOG/RAW và muốn ít thao tác nhất.

Thiết lập thường dùng cho bản free:

- Color processing mode: **DaVinci YRGB Color Managed**
- Output color space: **Rec.709 Gamma 2.4**

Rồi với từng clip LOG, chuột phải trong Media Pool → **Input Color Space** → chọn đúng profile máy quay.

> Đánh đổi của Color Managed là phép chuyển đổi **không hiện trong node graph**, nên khó soi khi có gì sai.

## Bước 4 — Nơi lưu cache

**Project Settings → Master Settings → Working Folders**. Trỏ **Cache files location** vào một ổ SSD nhanh, đừng để chung ổ với footage nếu có thể.

## Bước 5 — Tự động lưu

**DaVinci Resolve → Preferences → User → Project Save and Load** → bật **Live Save** (lưu liên tục) và **Project Backups** (giữ các bản cũ để quay về khi cần). Đây là thiết lập của máy, áp cho mọi project.

## Nhắc về cách Resolve lưu project

Resolve **không lưu ra file .drp** như Premiere lưu .prproj. Project nằm trong một **database** nội bộ. Muốn mang project sang máy khác:

- **File → Export Project** ra file `.drp` (chỉ project, không kèm media).
- Hoặc **File → Media Management** để gom cả media.

Chỉ copy thư mục footage là không đủ.
