# Video dọc cho TikTok, Reels, Shorts

Có hai tình huống khác hẳn nhau. Chọn đúng tình huống trước khi làm.

| Tình huống | Làm theo |
|---|---|
| Quay dọc sẵn bằng điện thoại | [Tình huống A](#tình-huống-a--quay-dọc-sẵn) |
| Có bản ngang, cần thêm bản dọc | [Tình huống B](#tình-huống-b--có-sẵn-bản-ngang-muốn-cắt-ra-bản-dọc) |

## Tình huống A — quay dọc sẵn

Đơn giản nhất.

1. **Project Settings** (`⇧9`) → **Master Settings** → **Timeline resolution** 1920×1080 → tick **Use vertical resolution**. Khung thành **1080×1920**.
2. **Timeline frame rate** khớp footage — đặt trước khi nạp clip. Xem [Tạo project](../01-bat-dau/tao-du-an.md#bước-2--frame-rate-thứ-không-sửa-được-về-sau).
3. Dựng như bình thường. Trang Cut tự đổi giao diện khi timeline dọc — xem [Cut → giao diện video dọc](../02-trang/cut/giao-dien.md#giao-diện-tự-đổi-khi-làm-video-dọc).
4. Sang [Bố cục khung dọc](#bố-cục-khung-dọc) và [Xuất](#xuất).

## Tình huống B — có sẵn bản ngang, muốn cắt ra bản dọc

Đây mới là tình huống thường gặp, và có một cái bẫy.

> **Đừng dựng trực tiếp trên timeline 9:16 nếu bạn quay ngang.** Khung dọc che mất hai bên nên bạn không thấy được chủ thể đang ở đâu, dựng rất khổ.

Cách đúng: **dựng xong bản ngang trước**, rồi mới tạo bản dọc từ nó.

### Các bước

1. Dựng và hoàn thiện bản ngang 1920×1080.
2. Trong Media Pool, chọn timeline → **Edit → Duplicate Timeline**. Đặt tên kiểu `… doc`. Xem [Nhân bản timeline](../02-trang/edit/timeline-nang-cao.md#nhân-bản-timeline--giữ-phiên-bản).
3. Chuột phải timeline mới trong Media Pool → **Timelines → Timeline Settings** → bỏ tick **Use Project Settings**.
4. Tab **Format**: tick **Use vertical resolution** (hoặc gõ thẳng 1080 × 1920). Xem [Timeline Settings](../02-trang/edit/timeline-nang-cao.md#timeline-settings--mỗi-timeline-một-cỡ-khung).
5. Mỗi clip giờ có viền đen trên dưới. Đặt chế độ xử lý chung — xem [mục dưới](#cách-nhanh-hơn-cho-cả-timeline) — rồi chỉ chỉnh tay clip lệch: **Inspector → Transform**, tăng **Zoom** cho lấp khung, chỉnh **Position X** để chủ thể vào giữa. Xem [Inspector](../02-trang/edit/inspector.md#những-việc-làm-hằng-ngày).

Bản ngang gốc vẫn nguyên vẹn vì bạn làm trên bản sao.

### Cách nhanh hơn cho cả timeline

Thay vì chỉnh từng clip, đặt chế độ xử lý chung cho clip khác cỡ khung. Ở Timeline Settings của timeline dọc (hoặc **Project Settings → Image Scaling → Input Scaling**), ô **Mismatched resolution files**:

| Chọn | Kết quả | Dùng khi |
|---|---|---|
| **Scale full frame with crop** | Lấp đầy khung, cắt bớt hai bên | **Video dọc** |
| **Scale entire image to fit** | Giữ toàn bộ hình, có viền đen. Mặc định | Không muốn mất phần nào |
| **Center crop with no resizing** | Cắt giữa, không phóng to | Footage rất lớn (4K vào khung 1080) |

Đặt **Scale full frame with crop** rồi chỉ chỉnh tay những clip có chủ thể lệch khỏi giữa.

### Cách dùng Adjustment Clip

Nếu muốn giữ một timeline duy nhất:

1. Ở timeline ngang, thêm **Adjustment Clip** lên track trên cùng, kéo dài hết timeline. Xem [Adjustment Clip](../02-trang/edit/chu-va-hieu-ung.md#adjustment-clip).
2. Chỉnh Transform trên adjustment clip đó.
3. Khi xuất bản dọc thì bật nó, xuất bản ngang thì tắt.

Cách này gọn nhưng khó chỉnh riêng từng cảnh.

> **Smart Reframe** — tính năng tự bám chủ thể khi đổi tỉ lệ — là `Studio`. Bản free phải chỉnh tay. Xem [Free và Studio](../01-bat-dau/free-vs-studio.md).

## Bố cục khung dọc

Đừng đặt nội dung quan trọng ở sát mép:

- **Trên khoảng 15%** — bị tên tài khoản và caption che.
- **Dưới khoảng 20%** — bị nút tương tác và mô tả che.
- **Phải khoảng 15%** — bị cột nút like, share che.

Bật **View → Safe Area** để thấy khung an toàn.

Đây là con số tham khảo từ thói quen dựng, không phải thông số của Resolve. Mỗi nền tảng đổi giao diện thường xuyên.

## Chữ và phụ đề cho video dọc

Chữ phải **to hơn nhiều** so với video ngang vì người ta xem trên điện thoại. Cỡ chữ tối thiểu nên chiếm khoảng 1/20 chiều cao khung.

Luôn có **nền mờ hoặc viền** sau chữ — nền video thay đổi liên tục, chữ trắng trơn sẽ có lúc chìm.

| Muốn | Làm ở |
|---|---|
| Vài dòng chữ to, tiêu đề | Text+ — xem [Chữ](../02-trang/edit/chu-va-hieu-ung.md#chữ--text-text) |
| Chữ chạy từng ký tự, viền nhiều lớp | Fusion — xem [Chữ động với Text+](../02-trang/fusion/chu-dong.md) |
| Phụ đề cả video | Track phụ đề — xem [Phụ đề](../02-trang/edit/phu-de.md) |

**Phụ đề cho video dọc:** tab **Track** của Inspector phụ đề → **Position** đẩy phụ đề lên khỏi 20% dưới cùng; **Stroke** hoặc **Background** cho dễ đọc. Xem [Kiểu chữ phụ đề](../02-trang/edit/phu-de.md#kiểu-chữ-phụ-đề).

## Xuất

Sang trang **Deliver**. Ở đầu Viewer, chọn đúng **timeline dọc**.

### Không có phụ đề — preset TikTok

1. Ô **Preset** → **TikTok** → **1080p**. Panel hiện **dạng gọn**: một danh sách, không có tab.
2. Tick **Use vertical resolution** — Resolution đổi từ 1920×1080 thành **1080×1920**. Preset mặc định **không** tick, đây là bước hay quên nhất.
3. **File Name** có chữ `doc` để khỏi lẫn bản ngang. Chọn **Location**.
4. Để **Frame rate** là Timeline Frame Rate, **Format** MP4, **Video Codec** H.264, **Audio Codec** AAC.
5. Tick **Normalize Audio** nếu chưa đo loudness ở Fairlight.
6. Nhìn Viewer: hình đứng dọc, **không** có viền đen hai bên. Liếc **Estimated File Size**.
7. **Add to Render Queue** → **Render All**.

Chi tiết: [Preset TikTok, Reels, Shorts](../02-trang/deliver/preset-theo-nen-tang.md#tiktok-reels-shorts--video-dọc).

### Có phụ đề — Custom Export

TikTok và Reels **không đọc file phụ đề rời**, nên phải in phụ đề vào hình. Dạng gọn của preset TikTok không có mục phụ đề.

1. Ô **Preset** → **Custom Export**. Panel hiện ba tab **Video · Audio · File**.
2. Tab Video: **Format** MP4, **Codec** H.264, **Resolution** 1080×1920 (hoặc tick **Use vertical resolution**), **Frame rate** Timeline Frame Rate.
3. **Quality** → **Restrict to** 15.000 Kb/s (cùng mức 1080p).
4. Cuối tab Video → **Subtitle Settings** → tick **Export Subtitle** → **Format: Burn into video**. Xem [Subtitle Settings](../02-trang/deliver/cai-dat-xuat.md#subtitle-settings).
5. Tab Audio: **Codec** AAC, **Data Rate** 320 Kb/s.
6. **Add to Render Queue** → **Render All**.

> **Burn into video chỉ in track phụ đề đang bật.** Có nhiều track phụ đề thì kiểm tra track nào đang bật ở timeline trước khi render.

Dùng lại lần sau: menu ba chấm của Render Settings → **Save as New Preset**, đặt tên *TikTok doc*. Xem [Tự tạo preset](../02-trang/deliver/preset-theo-nen-tang.md#tự-tạo-preset).

### Xuất cả bản ngang và bản dọc một lượt

Thêm job bản ngang (preset YouTube) và job bản dọc vào Render Queue, rồi **Render All**. Xem [Một lượt xuất YouTube và bản dọc](../02-trang/deliver/README.md#một-lượt-xuất-youtube-và-bản-dọc).

### Lỗi hay gặp

| Hiện tượng | Sửa |
|---|---|
| Viền đen hai bên | Đang xuất timeline ngang, hoặc quên **Use vertical resolution** |
| Không thấy phụ đề trên TikTok | Xuất phụ đề dạng file rời. Đổi sang **Burn into video** |
| Chủ thể bị cắt mất | Chỉnh **Position X** của clip đó ở Inspector |

Thêm: [Render xong mà file lỗi](../02-trang/deliver/render-queue-va-loi.md#render-xong-mà-file-lỗi).
