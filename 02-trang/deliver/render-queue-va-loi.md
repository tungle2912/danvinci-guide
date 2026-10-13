# Render Queue, Quick Export và lỗi khi xuất

Render Queue là **hàng đợi**: bạn xếp nhiều job vào rồi render một lượt. Mỗi job có thông số, khoảng xuất, thậm chí timeline riêng.

---

## Đưa một job vào hàng đợi

`★★★ Hằng ngày`

**Cách làm:**
1. Ở đầu Viewer, chọn **timeline** cần xuất.
2. Chọn preset hoặc chỉnh thông số ở Render Settings.
3. Chọn khoảng xuất ở timeline — mặc định **Entire Timeline**.
4. Bấm **Add to Render Queue** (đáy panel Render Settings).
5. Chưa chọn thư mục thì Resolve hỏi lúc này.

Job hiện ở panel phải với tên **Job 1**, kèm tên project, tên timeline và đường dẫn file.

**Hai cảnh báo có thể hiện ra:**

| Cảnh báo | Nghĩa | Làm gì |
|---|---|---|
| *This render may overwrite existing clips in this folder* | Thư mục đích đã có file trùng tên | **No**, đổi tên file. Chỉ **Yes** khi cố ý ghi đè bản cũ |
| **Media Offline** | Timeline còn clip mất file gốc | Thường nên huỷ, quay lại trang Edit tìm clip đỏ và relink. Add anyway thì đoạn đó ra khung báo lỗi |

---

## Xuất một đoạn

`★★☆ Thường dùng`

**Dùng khi:** chỉ cần xuất đoạn teaser 30 giây, hoặc xuất lại một đoạn vừa sửa để gửi khách xem.

**Cách làm:**
1. Trên timeline trang Deliver, đặt con trỏ ở đầu đoạn, bấm `I`.
2. Đặt con trỏ ở cuối đoạn, bấm `O`.
3. Menu **Render** trên timeline chuyển thành **In/Out Range**. Thanh màu cam trên thước thời gian cho thấy khoảng sẽ xuất.
4. Kiểm tra ô **DURATION** ở đầu Viewer.
5. **Add to Render Queue**.

Muốn quay về xuất cả timeline: chọn **Entire Timeline** ở menu **Render**.

**Cách khác:** chuột phải một ô ở Thumbnail timeline → **Render This Clip** — chọn đúng clip đó.

> **Ở chế độ Individual clips,** `I` và `O` tự bắt vào mép clip gần nhất. Không xuất được nửa clip. Cần nửa clip thì dùng **Single clip**.

### Bỏ một track khỏi bản xuất

Bấm nút **tắt track** ở đầu track video hoặc tiếng trên timeline Deliver.

**Ví dụ:** cần bản không chữ để gửi đơn vị dịch phụ đề. Chữ nằm ở V3 → tắt V3 → Add to Render Queue. Bật lại V3 trước khi tạo job tiếp theo.

---

## Nhiều job, một lượt render

`★★★ Hằng ngày`

**Là gì:** mỗi lần bấm Add to Render Queue là một job mới. Đổi thông số, đổi timeline, đổi khoảng xuất giữa các lần bấm.

**Dùng khi:** cần nhiều phiên bản — bản YouTube, bản dọc, bản duyệt, bản master.

**Cách làm:**
1. Tạo job đầu như bình thường.
2. Đổi preset hoặc thông số → **Add to Render Queue** lần nữa.
3. Lặp lại cho đủ phiên bản.
4. Không chọn job nào → bấm **Render All**.

Render chạy từ job **trên cùng** xuống.

### Chỉ render vài job

Bấm chọn một job, `⌘`-bấm để chọn thêm job rời, `⇧`-bấm để chọn cả dãy. Nút đổi thành **Render** kèm số job đang chọn (ví dụ **Render 1**) — chỉ render những job đó.

### Sắp xếp, đặt tên, xem chi tiết

| Muốn | Làm |
|---|---|
| Đổi thứ tự | Kéo job lên xuống. Số Job giữ nguyên thứ tự, chỉ thông số đổi chỗ |
| Đặt tên dễ nhớ | Bấm vào chữ **Job 1**, gõ tên mới (ví dụ *YouTube*, *Doc*) |
| Xem thông số từng job | Menu ba chấm của Render Queue → **Show Job Details**. Mỗi job hiện thêm kích thước, định dạng, frame rate, kênh tiếng, độ dài |

### Sửa một job

1. Bấm **biểu tượng bút chì** trên job. Thông số và khoảng xuất của job được nạp lại vào Render Settings.
2. Sửa những gì cần.
3. Bấm **Update Job** để ghi đè job đó, hoặc **Add New Job** để tạo job mới và giữ job cũ.

Bấm bút chì lần nữa mà chưa Update Job thì Resolve hỏi **Save**, **Cancel** hay **Don't Save**.

### Render lại job đã xong

Job đã render **vẫn nằm trong hàng đợi**. Bấm render lần nữa thì Resolve hỏi *"Selected items contain already rendered items. Do you want to re-render them?"*:

| Chọn | Kết quả |
|---|---|
| **Yes** | Render lại tất cả |
| **No** | Chỉ render job chưa render |
| **Cancel** | Huỷ |

Hoặc chuột phải job → **Clear Render Status** để đánh dấu lại là chưa render.

### Dọn hàng đợi

| Muốn xoá | Làm |
|---|---|
| Một job | Dấu **X** góc trên phải job |
| Mọi job đã render xong | Menu ba chấm → **Clear Rendered** |
| Tất cả | Menu ba chấm → **Clear All** |

### Tìm file vừa render

Chuột phải job đã render:

- **Reveal in Finder** — mở thư mục chứa file.
- **Reveal in Media Storage** — hiện file trong Media Storage của Resolve.
- **Reveal in Browser** — với job đã tải lên YouTube, Vimeo…, mở video trên trình duyệt.

### Đang render

- Nút đổi thành **Stop Render** — bấm để dừng.
- Icon Resolve trên Dock có thanh tiến độ nhỏ.
- Muốn render nhanh hơn trên máy yếu: menu ba chấm của **Viewer** → **Updates During Renders** → tắt hoặc giảm cập nhật hình.

---

## Một job, nhiều đầu ra

`★☆☆ Tình huống cụ thể`

**Là gì:** một job ghi ra **nhiều bộ file** với định dạng khác nhau — ví dụ bản ProRes 422 HQ và bản DNxHD, hoặc một bản có timecode đè và một bản sạch.

**Cách làm:** menu ba chấm của Render Settings → **Create Additional Output**. Một hàng số hiện dưới File Name và Location — bấm từng số để chỉnh đầu ra đó. Xoá: mở đầu ra cần xoá, bấm **Delete** ở đáy.

Với bản ngang + bản dọc thì **không** dùng cách này — hai bản đến từ hai timeline khác nhau, nên tạo hai job. Xem [ví dụ ở trang tổng quan](README.md#một-lượt-xuất-youtube-và-bản-dọc).

---

## Render job từ nhiều project

`★☆☆ Tình huống cụ thể`

**Dùng khi:** chia một phim dài thành nhiều project (mỗi tập một project) và muốn render tất cả qua đêm.

1. Mở từng project, tạo job, **lưu project mà không render**.
2. Ở project cuối, menu ba chấm của Render Queue → **Show All Projects**. Job của mọi project trong cùng Project Library hiện ra.
3. Bấm **Render All**.
4. Xong thì tắt **Show All Projects**.

---

## Render cache và "Use render cached images"

`★☆☆ Tình huống cụ thể`

Khi dựng, bạn có thể bật **Render Cache** để phát mượt clip nặng — xem [Tối ưu hiệu năng](../../04-tham-khao/hieu-nang.md). Cache là những file Resolve render sẵn ở chất lượng thường **thấp hơn** bản xuất.

Ở Advanced Settings của tab Video có ô **Use render cached images**:

| Bật | Tắt |
|---|---|
| Render nhanh hơn — Resolve lấy hình từ cache | Resolve xử lý lại mọi thứ từ footage gốc |
| Chỉ nên bật khi định dạng cache **bằng hoặc tốt hơn** định dạng xuất | Chọn cho **bản cuối** để chắc chắn chất lượng tốt nhất |

Tương tự với **Use optimized media** và **Use proxy media**.

---

## Quick Export

`★★☆ Thường dùng`

**Là gì:** xuất bằng preset trong một bước, **không cần sang Deliver**. Dùng được ở mọi trang.

**Cách làm:**
1. (Tuỳ chọn) Ở trang Cut, Edit, Fusion hoặc Color, đặt `I` `O` trên timeline nếu chỉ xuất một đoạn. Không đặt thì xuất cả timeline.
2. **File → Quick Export**. Trang Cut có thêm nút **Quick Export** góc trên phải.
3. Chọn preset ở **hàng icon trên cùng** của cửa sổ Quick Export.
4. **Export** → chọn thư mục, đặt tên → **Save**.

Thanh tiến trình cho biết còn bao lâu. Muốn xem preset dạng danh sách thay vì icon: bấm icon **List View**.

**Thêm preset của mình vào Quick Export:** khi lưu preset ở Deliver, tick **Add to quick export** — xem [Tự tạo preset](preset-theo-nen-tang.md#tự-tạo-preset).

| Dùng **Quick Export** | Dùng **trang Deliver** |
|---|---|
| Bản nháp, video ngắn đăng ngay | Bản cuối cần kiểm soát bitrate |
| Một phiên bản | Nhiều phiên bản một lượt |
| Preset có sẵn là đủ | Cần burn phụ đề, đổi codec, Individual clips |

Thêm về Quick Export ở trang Cut: [Boring Detector và Quick Export](../cut/kiem-tra-va-xuat.md#quick-export).

---

## Remote Rendering

`Studio`

Gửi job sang **một máy Resolve khác trong mạng** để render, máy của bạn làm việc tiếp. Cả hai máy phải cài **DaVinci Resolve Studio**, dùng chung Project Library dạng PostgreSQL và cùng truy cập được file gốc. Bản free không dùng được.

---

## Render xong mà file lỗi

| Hiện tượng | Nguyên nhân hay gặp | Cách sửa |
|---|---|---|
| **Hình đứng, tiếng vẫn chạy** | Bộ mã hoá phần cứng | Bỏ tick **Use hardware acceleration if available** rồi render lại |
| **File không mở được trên máy khác** | H.265 — máy, phần mềm cũ không đọc được | Xuất lại bằng **H.264** |
| **Màu xuất ra nhạt hơn lúc xem trong Resolve** | Vấn đề color management | Xem [LOG sang Rec.709](../../03-luong/log-sang-rec709.md). Advanced Settings: để **Data Levels** ở **Auto**, **Color Space Tag** và **Gamma Tag** ở **Same as Project** |
| **Không có tiếng** | Chưa tick **Export Audio**, hoặc Output Track chọn nhầm bus | Tab Audio: tick Export Audio, Output Track chọn bus chính |
| **Hình giật** | Frame rate xuất khác timeline | Tab Video: **Frame rate** về **Timeline Frame Rate** |
| **Video dọc bị viền đen hai bên** | Xuất từ timeline ngang, hoặc quên **Use vertical resolution** | Chọn đúng timeline dọc ở đầu Viewer, tick Use vertical resolution |
| **Có timecode, tên clip đè lên hình** | **Data burn-in** còn bật | Advanced Settings → **Data burn-in** → **None** |
| **Bản xuất mờ, kém nét hơn lúc xem** | Render từ proxy, optimized media hoặc cache | Tắt **Use proxy media**, **Use optimized media**, **Use render cached images** |
| **Thiếu phụ đề trên TikTok, Reels** | Xuất phụ đề dạng file rời | **Subtitle Settings** → **Burn into video** |
| **Có khung báo lỗi đỏ giữa video** | Clip offline lúc render | Relink clip ở trang Edit, render lại |
| **Bản cũ bị mất** | File mới trùng tên đã ghi đè | Đặt tên khác nhau cho mỗi phiên bản (`_v1`, `_v2`) |
| **Thiếu chữ hoặc một lớp hình** | Track đang bị tắt ở timeline Deliver | Bật lại track, render lại |

Lỗi tổng hợp ở mọi trang: [Lỗi thường gặp](../../04-tham-khao/loi-thuong-gap.md).
