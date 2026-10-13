# Vlog YouTube từ đầu đến cuối

Luồng đầy đủ cho một video 10–15 phút, quay bằng một máy, có nhạc nền và chữ. Làm theo đúng thứ tự này thì không phải quay lại sửa.

## 1. Chuẩn bị project

1. Tạo project mới, đặt tên có ngày tháng.
2. Nạp toàn bộ footage vào Media Pool (`⌘I`).
3. Chuột phải clip đầu tiên → **Create Timeline Using Selected Clips**. Resolve lấy đúng frame rate và resolution.
4. Nếu máy lag: chọn hết clip → chuột phải → **Generate Optimized Media**, rồi bật **Playback → Use Optimized Media If Available**.

## 2. Lọc trước khi dựng

Đừng kéo hết mọi thứ xuống timeline rồi mới cắt.

Mở từng clip ở Source Viewer, xem một lượt, đặt `I` và `O` quanh đoạn dùng được, rồi `⇧F12` (Append) để nối vào cuối timeline.

Xong bước này bạn có một bản thô đã bỏ hết phần thừa.

## 3. Dựng thô

Sắp xếp lại thứ tự, cắt bớt. Chỉ quan tâm **nội dung và nhịp**, chưa quan tâm đẹp xấu.

Phím dùng nhiều: `⌘B` cắt, `Fn+Delete` xoá dồn, `A` và `T` đổi chế độ chuột.

Mẹo: xem lại bản thô với tốc độ 1.5× (**Playback → Speed**) để nhận ra chỗ nào lê thê.

## 4. B-roll và chữ

- **B-roll** đặt lên track V2 bằng `F12` (Place on Top).
- **Chữ** từ **Effects → Titles → Text+**, cũng đặt lên track trên.

Đặt destination control đúng track trước khi bấm `F12` (`⌥2` để chọn V2).

## 5. Nhạc nền

1. Kéo nhạc xuống track A2.
2. Chọn clip lời (A1), chuột phải → **Normalize Audio Levels** → ITU-R BS.1770, mục tiêu −14 LUFS.
3. Kéo volume nhạc xuống khoảng −20 dB.
4. Bật **Ducker** trên track nhạc, chọn track lời làm nguồn — nhạc tự nhỏ khi có người nói. Xem [Ducker](../02-trang/fairlight/mixer-va-track-fx.md#ducker--nhạc-tự-nhỏ-khi-có-lời).

## 6. Chuyển cảnh

Ít thôi. Phần lớn cắt thẳng là đẹp nhất.

Dùng `⌘T` (Cross Dissolve) ở chỗ chuyển chủ đề hoặc chuyển thời gian. Đừng dùng transition loè loẹt ở mọi điểm cắt.

## 7. Chỉnh màu

Sang trang **Color** (icon vòng tròn chấm ở đáy).

1. Clip đầu tiên: dựng [chuỗi 6 node](../02-trang/color/node.md#chuỗi-6-node-cơ-bản).
2. Cân bằng ở node 01 bằng **Parade** — chân và đỉnh ba cột R/G/B ngang nhau.
3. Tương phản ở node 02.
4. Look ở node 05.
5. Lưu thành **PowerGrade**.
6. Các clip còn lại: chọn hết → `⌥V` (Paste Attributes) từ clip đã chỉnh, rồi chỉnh tay từng clip chỗ nào lệch.

Nếu các cảnh quay cùng một chỗ cùng ánh sáng, dùng **Group** thay vì copy từng clip.

## 8. Âm thanh tinh

Sang trang **Fairlight** (icon nốt nhạc). Với clip lời:

1. EQ: cắt dưới 80 Hz, nâng nhẹ 3–5 kHz.
2. Compressor: Ratio 3:1, Threshold đặt sao cho chỉ nén chỗ to nhất.
3. Limiter ở −1 dB trên track tổng.

## 9. Xuất

Sang trang **Deliver** (icon tên lửa).

- Preset **YouTube 1080p** (hoặc 4K nếu quay 4K)
- Format MP4, Codec H.264
- Quality: **Restrict to 15.000 Kb/s** cho 1080p
- Tick **Use hardware acceleration if available**
- Audio: AAC 320 Kb/s
- **Add to Render Queue** → **Render All**

## 10. Thumbnail

Vào đúng khung hình muốn lấy, ở trang Color bấm `⌥⌘G` (Grab Still), rồi trong Gallery chuột phải still → **Export** ra PNG.

## Thời gian tham khảo

| Bước | Thời gian cho video 12 phút |
|---|---|
| Lọc + dựng thô | 1–2 giờ |
| B-roll, chữ | 45 phút |
| Âm thanh | 30 phút |
| Màu | 30–60 phút |
| Xuất | 10–20 phút |
