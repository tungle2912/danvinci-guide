# Video dọc cho TikTok, Reels, Shorts

Có hai tình huống khác hẳn nhau. Chọn đúng tình huống trước khi làm.

## Tình huống A — quay dọc sẵn

Đơn giản nhất.

1. **Project Settings** (`⇧9`) → **Timeline resolution** → **1080×1920**.
2. Frame rate khớp footage.
3. Dựng như bình thường.

## Tình huống B — có sẵn bản ngang, muốn cắt ra bản dọc

Đây mới là tình huống thường gặp, và có một cái bẫy.

> **Đừng dựng trực tiếp trên timeline 9:16 nếu bạn quay ngang.** Khung dọc che mất hai bên nên bạn không thấy được chủ thể đang ở đâu, dựng rất khổ.

Cách đúng: **dựng xong bản ngang trước**, rồi mới tạo bản dọc từ nó.

### Các bước

1. Dựng và hoàn thiện bản ngang 1920×1080.
2. Trong Media Pool, chuột phải timeline → **Duplicate Timeline**. Đặt tên kiểu `… – dọc`.
3. Mở timeline mới, vào **Timeline Settings** (chuột phải timeline trong Media Pool → **Timelines → Timeline Settings**), bỏ tick **Use Project Settings**, đổi resolution thành **1080×1920**.
4. Mỗi clip giờ có viền đen trên dưới. Với từng clip, vào **Inspector → Transform**, tăng **Zoom** cho đến khi lấp đầy khung, rồi chỉnh **Position X** để chủ thể vào giữa.

Bản ngang gốc vẫn nguyên vẹn vì bạn làm trên bản sao.

### Cách nhanh hơn cho cả timeline

Thay vì chỉnh từng clip, đặt chế độ xử lý chung:

**Timeline Settings → Mismatched resolution files** → chọn:

- **Scale full frame with crop** — lấp đầy khung, cắt bớt hai bên. Dùng cho video dọc.
- **Scale entire image to fit** — giữ toàn bộ hình, có viền đen.
- **Center crop with no resizing** — cắt giữa, không phóng to.

Đặt **Scale full frame with crop** rồi chỉ chỉnh tay những clip có chủ thể lệch khỏi giữa.

### Cách dùng Adjustment Clip

Nếu muốn giữ một timeline duy nhất:

1. Ở timeline ngang, thêm **Adjustment Clip** lên track trên cùng, kéo dài hết timeline.
2. Chỉnh Transform trên adjustment clip đó.
3. Khi xuất bản dọc thì bật nó, xuất bản ngang thì tắt.

Cách này gọn nhưng khó chỉnh riêng từng cảnh.

> **Smart Reframe** — tính năng tự bám chủ thể khi đổi tỉ lệ — là `Studio`. Bản free phải chỉnh tay.

## Bố cục khung dọc

Đừng đặt nội dung quan trọng ở sát mép:

- **Trên khoảng 15%** — bị tên tài khoản và caption che.
- **Dưới khoảng 20%** — bị nút tương tác và mô tả che.
- **Phải khoảng 15%** — bị cột nút like, share che.

Bật **View → Safe Area** để thấy khung an toàn.

## Chữ cho video dọc

Chữ phải **to hơn nhiều** so với video ngang vì người ta xem trên điện thoại. Cỡ chữ tối thiểu nên chiếm khoảng 1/20 chiều cao khung.

Luôn có **nền mờ hoặc viền** sau chữ — nền video thay đổi liên tục, chữ trắng trơn sẽ có lúc chìm.

## Xuất

| Mục | Đặt |
|---|---|
| Resolution | 1080×1920 |
| Format | MP4 |
| Codec | H.264 |
| Frame rate | 30 fps (hoặc 60 nếu quay 60) |
| Bitrate | Restrict to 15.000 Kb/s |
| Audio | AAC 320 Kb/s |

Nếu có phụ đề: cuối tab **Video** → **Subtitle Settings** → tick **Export Subtitle** → chọn **Burn into video**. Xem [Subtitle Settings](../02-trang/deliver/cai-dat-xuat.md#subtitle-settings). TikTok và Reels không đọc file phụ đề rời.
