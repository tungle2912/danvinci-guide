# Vlog YouTube từ đầu đến cuối

Luồng đầy đủ cho một video 10–15 phút, quay bằng một máy, có nhạc nền, chữ và phụ đề. Làm theo đúng thứ tự này thì không phải quay lại sửa.

| Bước | Trang | Kết quả |
|---|---|---|
| [1. Chuẩn bị project](#1-chuẩn-bị-project) | Media | Timeline đúng frame rate |
| [2. Lọc trước khi dựng](#2-lọc-trước-khi-dựng) | Edit | Bản thô đã bỏ phần thừa |
| [3. Dựng thô](#3-dựng-thô) | Edit | Nội dung và nhịp xong |
| [4. B-roll và chữ](#4-b-roll-và-chữ) | Edit, Fusion | Lớp hình phụ, tiêu đề |
| [5. Nhạc nền](#5-nhạc-nền) | Edit | Nhạc nằm dưới lời |
| [6. Chuyển cảnh](#6-chuyển-cảnh) | Edit | Vài chỗ chuyển mềm |
| [7. Phụ đề](#7-phụ-đề) | Edit | Track phụ đề |
| [8. Chỉnh màu](#8-chỉnh-màu) | Color | Màu đều giữa các clip |
| [9. Âm thanh tinh](#9-âm-thanh-tinh) | Fairlight | Lời rõ, đủ to −14 LUFS |
| [10. Xuất](#10-xuất) | Deliver | File MP4 + file `.srt` |
| [11. Thumbnail](#11-thumbnail) | Edit | Ảnh bìa PNG |

## 1. Chuẩn bị project

1. Tạo project mới, đặt tên có ngày tháng. Đặt **Timeline frame rate** trước khi nạp clip — xem [Tạo project](../01-bat-dau/tao-du-an.md#bước-2--frame-rate-thứ-không-sửa-được-về-sau).
2. Nạp toàn bộ footage vào Media Pool (`⌘I`). Resolve hỏi đổi frame rate thì chọn **Change**. Xem [Nạp media](../02-trang/media/nap-media.md).
3. Chọn các clip → chuột phải → **Create Timeline Using Selected Clips**. Resolve lấy đúng frame rate và resolution.
4. Nếu máy lag: chọn hết clip → chuột phải → **Generate Optimized Media**, rồi bật **Playback → Use Optimized Media If Available**. Xem [Tối ưu hiệu năng](../04-tham-khao/hieu-nang.md).

## 2. Lọc trước khi dựng

Đừng kéo hết mọi thứ xuống timeline rồi mới cắt.

Mở từng clip ở Source Viewer, xem một lượt, đặt `I` và `O` quanh đoạn dùng được, rồi `⇧F12` (Append) để nối vào cuối timeline. Xem [Append](../02-trang/edit/dung-va-cat.md#append--f12).

Xong bước này bạn có một bản thô đã bỏ hết phần thừa.

## 3. Dựng thô

Sắp xếp lại thứ tự, cắt bớt. Chỉ quan tâm **nội dung và nhịp**, chưa quan tâm đẹp xấu.

Phím dùng nhiều: `⌘B` cắt, `Fn+Delete` xoá dồn, `A` và `T` đổi chế độ chuột. Xem [Cắt và xoá](../02-trang/edit/dung-va-cat.md#cắt-và-xoá).

Mẹo: xem lại bản thô với tốc độ 1.5× (**Playback → Speed**) để nhận ra chỗ nào lê thê.

## 4. B-roll và chữ

- **B-roll** đặt lên track V2 bằng `F12` (Place on Top). Đặt destination đúng track trước khi bấm (`⌥2` để chọn V2). Xem [Place On Top](../02-trang/edit/dung-va-cat.md#place-on-top--f12).
- **Chữ tĩnh, tiêu đề đơn giản:** **Effects → Toolbox → Titles** → kéo **Text+** lên track trên. Xem [Chữ — Text, Text+](../02-trang/edit/chu-va-hieu-ung.md#chữ--text-text).
- **Tiêu đề chạy, nhiều lớp viền bóng:** mở clip chữ ở trang Fusion. Xem [Ví dụ: tiêu đề trượt vào](../02-trang/fusion/README.md#ví-dụ-tiêu-đề-trượt-vào-trên-video) và [Chữ động với Text+](../02-trang/fusion/chu-dong.md).

> Việc gì làm được trong 30 giây ở trang Edit thì làm ở Edit. Fusion nặng máy hơn nhiều — xem [Khi nào cần Fusion](../02-trang/fusion/README.md#khi-nào-cần-fusion-khi-nào-không).

## 5. Nhạc nền

1. Kéo nhạc xuống track A2. Đặt tên track: A1 "Giọng", A2 "Nhạc".
2. Chọn hết clip lời ở A1 → chuột phải → **Normalize Audio Levels** → chọn một chuẩn đo loudness → **Set Level: Relative**. Xem [Normalize](../02-trang/fairlight/mixer-va-track-fx.md#normalize--cân-đều-các-clip).
3. Kéo volume nhạc xuống tạm khoảng −20 dB. Bước 9 sẽ cho nhạc tự nhỏ khi có lời.

## 6. Chuyển cảnh

Ít thôi. Phần lớn cắt thẳng là đẹp nhất.

Dùng `⌘T` (Cross Dissolve) ở chỗ chuyển chủ đề hoặc chuyển thời gian. Đừng dùng transition loè loẹt ở mọi điểm cắt. Xem [Chuyển cảnh](../02-trang/edit/chu-va-hieu-ung.md#chuyển-cảnh).

## 7. Phụ đề

Không bắt buộc, nhưng giúp người xem không bật tiếng.

1. Chuột phải đầu track bất kỳ → **Add Subtitle Track**. Bấm đúp tên track, đổi thành `Tieng Viet` — tên này thành tên file `.srt`.
2. Gõ từng câu ở Inspector → tab **Captions**, hoặc nhập file `.srt` làm sẵn.
3. Kiểu chữ cho cả track: chọn đầu track → Inspector → tab **Track**. Chọn font có đủ dấu tiếng Việt.

Chi tiết: [Phụ đề](../02-trang/edit/phu-de.md). Tự tạo phụ đề bằng AI là `Studio`.

## 8. Chỉnh màu

Sang trang **Color**.

1. Clip đầu tiên: dựng [chuỗi 6 node](../02-trang/color/node.md#chuỗi-6-node-cơ-bản) (`⌥S` năm lần).
2. Cân bằng ở node 01 bằng **Parade** — chân và đỉnh ba cột R/G/B ngang nhau. Xem [Cân bằng trắng](../02-trang/color/can-bang.md) và [Parade](../02-trang/color/scopes.md#parade).
3. Tương phản ở node 02.
4. Look ở node 05.
5. `⌥⌘G` (Grab Still) lưu grade. Lưu thành **PowerGrade** nếu muốn dùng cho project sau — xem [PowerGrade](../02-trang/color/node.md#powergrade--khung-node-dùng-cho-mọi-project).
6. Các clip còn lại: chọn clip đích → click chuột giữa vào clip đã chỉnh (hoặc chuột phải → **Apply Grade**). Chỉnh tay từng clip chỗ nào lệch. Xem [Áp grade cho nhiều clip](../02-trang/color/node.md#áp-grade-cho-nhiều-clip).
7. So trước/sau: `⇧D`.

Nếu các cảnh quay cùng một chỗ cùng ánh sáng, dùng [Group](../02-trang/color/node.md#group--nhóm-các-clip-cùng-bối-cảnh) thay vì copy từng clip.

Quay LOG thì làm [LOG sang Rec.709](log-sang-rec709.md) trước bước này.

## 9. Âm thanh tinh

Sang trang **Fairlight**. Bấm **Mixer** góc trên phải. Làm đúng thứ tự:

1. **Giọng đều:** cột A1 → mục **Track FX** → ô **Dial Lev** → bật **Dialogue Leveler**, tick **Lift Soft Dialogue**. Xem [Dialogue Leveler](../02-trang/fairlight/mixer-va-track-fx.md#dialogue-leveler--giọng-đều-không-cần-chỉnh-tay).
2. **Ồn nền (nếu có):** kéo **Noise Reduction** từ **Effects → Audio FX → Fairlight FX** thả lên đầu track A1, thử preset **De-Hiss**. Xem [Noise Reduction](../02-trang/fairlight/lam-sach-giong.md#noise-reduction--giảm-ồn-nền).
3. **EQ giọng:** bấm đúp ô **EQ** ở cột A1. Cắt dưới 80 Hz (**Hi-Pass**), hạ nhẹ 200–400 Hz, nâng nhẹ 3–5 kHz. Xem [EQ](../02-trang/fairlight/lam-sach-giong.md#eq--3-thao-tác-cho-giọng-nói).
4. **Nén nhẹ:** bấm đúp ô **Dynamics** → bật **Compressor**, Ratio 3:1, hạ Threshold tới khi chỉ chỗ to nhất bị nén. Xem [Compressor](../02-trang/fairlight/lam-sach-giong.md#compressor).
5. **Nhạc tự nhỏ khi có lời:** cột A2 → **Track FX** → bật **Ducker**, **Source** chọn A1, **Duck Amount** 2–5 dB. Không thấy Ducker: menu ba chấm của Mixer → **Visible Track FX** → tick Ducker. Xem [Ducker](../02-trang/fairlight/mixer-va-track-fx.md#ducker--nhạc-tự-nhỏ-khi-có-lời).
6. **Chặn trần:** cột **Bus 1** → **+** ở mục **Effects** → **Limiter**, **Ceiling** −1 dB. Xem [Limiter trên Bus](../02-trang/fairlight/loudness-va-xuat.md#limiter-trên-bus--chặn-trần).
7. **Đo độ to:** bấm **Meters**. Menu ba chấm của Loudness meter → chọn **YouTube**. Đưa con trỏ về đầu, bấm **Reset**, phát hết video. **Integrated** nên quanh −14 LUFS, **TP** dưới −1. Xem [Loudness meter](../02-trang/fairlight/loudness-va-xuat.md#loudness-meter--đo-độ-to-cảm-nhận).
8. Soát lần cuối: không track nào còn **Solo** hay **Mute** nhầm. Xem [Kiểm tra trước khi sang Deliver](../02-trang/fairlight/loudness-va-xuat.md#kiểm-tra-trước-khi-sang-deliver).

## 10. Xuất

Sang trang **Deliver**. Kiểm tra tên timeline ở đầu Viewer.

1. Ô **Preset** → **YouTube** → **1080p** (hoặc **2160p** nếu timeline 4K). Panel đổi sang **dạng gọn** — một danh sách, không có tab. Xem [Panel có hai dạng](../02-trang/deliver/giao-dien.md#panel-có-hai-dạng--tuỳ-preset).
2. Gõ **File Name**, chọn **Location**.
3. Để **Frame rate** là Timeline Frame Rate, **Format** MP4, **Video Codec** H.264, **Audio Codec** AAC như preset điền sẵn.
4. **Data burn-in:** mặc định Same as project. Nếu đã bật timecode ở **Workspace → Data Burn-In** để gửi duyệt thì đổi sang **None**, kẻo timecode dính vào bản đăng.
5. **Normalize Audio:** tick nếu ở bước 9 chưa đạt −14 LUFS. Standard để **YouTube** (−14 LKFS, đỉnh −1.0 dBTP).
6. Để tắt **Use Proxy Media** — render từ proxy sẽ kém nét.
7. Liếc **Estimated File Size**, rồi **Add to Render Queue** → **Render All**.

Chi tiết: [Preset YouTube](../02-trang/deliver/preset-theo-nen-tang.md#youtube).

**Cần bitrate cụ thể** (ví dụ 15.000 Kb/s cho 1080p)? Dạng gọn không có ô bitrate. Chọn **Custom Export** → tab Video → **Quality → Restrict to**. Xem [Quality — bitrate](../02-trang/deliver/cai-dat-xuat.md#quality--chọn-bitrate).

**File phụ đề cho YouTube:** từ trang Edit, **File → Export Subtitle** ra `.srt`, rồi tải lên YouTube cùng video. Hoặc dùng Custom Export → cuối tab Video → **Subtitle Settings** → **As a separate file**. Xem [Xuất phụ đề](../02-trang/edit/phu-de.md#xuất-phụ-đề).

**Render xong:** chuột phải job → **Reveal in Finder**, mở xem đầu, giữa, cuối. Lỗi gì thì tra [Render xong mà file lỗi](../02-trang/deliver/render-queue-va-loi.md#render-xong-mà-file-lỗi).

## 11. Thumbnail

Ở trang Edit, đặt con trỏ đúng khung muốn lấy → **File → Export → Current Frame as Still** → chọn PNG. Xem [Ảnh tĩnh](../02-trang/deliver/preset-theo-nen-tang.md#một-khung-hình--không-cần-sang-deliver).

## Thời gian tham khảo

| Bước | Thời gian cho video 12 phút |
|---|---|
| Lọc + dựng thô | 1–2 giờ |
| B-roll, chữ | 45 phút |
| Phụ đề gõ tay | 45–90 phút |
| Âm thanh | 30 phút |
| Màu | 30–60 phút |
| Xuất | 10–20 phút |
