# Nạp media vào project

## Bốn cách cơ bản

| Cách | Thao tác | Khi nào dùng |
|---|---|---|
| **Kéo từ Media Storage** | Kéo file hoặc thư mục từ Media Storage xuống Media Pool | Thường dùng nhất |
| **Kéo từ Finder** | Kéo thẳng từ Finder vào Media Pool | Nhanh, vài file lẻ |
| **Import Media** | `⌘I` hoặc **File → Import → Media** | Khi biết chính xác file cần |
| **Import Folder** | **File → Import → Media Folder** | Giữ nguyên cấu trúc thư mục thành các bin |

**Import Folder** là cách tốt nhất khi thẻ nhớ đã có sẵn cấu trúc thư mục hợp lý — Resolve tạo bin tương ứng với từng thư mục.

Chuột phải trong Media Storage cũng có các lệnh:

- **Add Into Media Pool** — nạp vào bin đang chọn
- **Add Folder Into Media Pool** — nạp cả thư mục
- **Add Folder and SubFolders Into Media Pool (Create Bins)** — nạp cả cây thư mục, tự tạo bin

## Nạp một đoạn thay vì cả clip (subclip)

Không cần nạp cả file dài 40 phút nếu chỉ dùng 2 phút.

1. Chọn clip trong Media Storage.
2. Đặt `I` và `O` trong Viewer quanh đoạn cần.
3. Chuột phải clip → **Add Subclip to Media Pool**.

Subclip vẫn trỏ về file gốc, không nhân bản dữ liệu.

## Nạp một khung từ chuỗi ảnh

Resolve mặc định gom chuỗi ảnh (image sequence) thành một clip video. Muốn lấy một khung riêng lẻ: chuột phải → bỏ tick **Frame Sequence**, rồi nạp.

## Nạp ảnh tĩnh

Kéo vào như clip bình thường. Độ dài mặc định đặt ở **Preferences → User → Editing → Standard still duration**.

## Hộp thoại đổi frame rate

Khi bạn kéo clip đầu tiên vào **timeline** (không phải Media Pool), Resolve hỏi có đổi frame rate project cho khớp không.

> **Luôn chọn Change.** Đây là thứ duy nhất không sửa được sau khi timeline đã có clip.

Cách tránh hộp thoại này hoàn toàn: nạp clip vào Media Pool trước, rồi chuột phải clip → **Create Timeline Using Selected Clips**. Resolve lấy đúng mọi thông số từ clip.

## Media offline — khi clip hiện đỏ

Resolve **không nhúng media vào project**, chỉ lưu đường dẫn. Đổi tên file, chuyển thư mục hay rút ổ là clip thành offline.

Nối lại: chuột phải clip trong Media Pool → **Relink Selected Clips** → trỏ tới thư mục mới. Resolve tự nối lại các clip khác cùng thư mục.

Chủ động ngắt: **Unlink Selected Clips** — dùng khi muốn chuyển sang bản proxy hay bản online khác.

## Tách tiếng ra khỏi file hình

Chuột phải clip trong Media Storage → **Extract Audio**. Tạo ra file tiếng riêng.

## Đổi media gốc của một clip

Chuột phải clip → **Replace Selected Clip**. Mọi chỗ clip đó xuất hiện trên timeline đều đổi theo, giữ nguyên điểm cắt.

Dùng khi: đạo diễn đổi ý về một cảnh, hoặc bạn có bản footage chất lượng cao hơn.

## Proxy và Optimized Media

Hai thứ khác nhau, hay bị nhầm.

### Optimized Media
Bản nhẹ do Resolve tạo và **tự quản lý**. Không xuất ra ngoài, không mang sang máy khác được.

1. Chọn clip → chuột phải → **Generate Optimized Media**
2. Bật dùng: **Playback → Use Optimized Media If Available**

Chọn codec và độ phân giải ở **Project Settings → Master Settings → Optimized Media Format / Optimized Media Resolution**.

### Proxy Media
File thật nằm trên ổ, **mang sang máy khác được**.

1. Chọn clip → chuột phải → **Generate Proxy Media**
2. Bật dùng: **Playback → Proxy Handling → Prefer Proxies**

Dùng Proxy khi làm việc nhóm hoặc dựng trên laptop rồi chuyển sang máy bàn. Dùng Optimized Media khi chỉ làm một mình trên một máy.

Chi tiết cách chọn codec: [Tối ưu hiệu năng](../../04-tham-khao/hieu-nang.md).
