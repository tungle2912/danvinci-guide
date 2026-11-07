# Danh sách ảnh cần chụp — trang Deliver (`02-trang/deliver/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-deliver.png` (toàn cửa sổ với preset YouTube 1080p dạng gọn và hai job trong Render Queue, nhúng ở README và ở `giao-dien.md` mục Render Queue). Các hình `assets/diagrams/deliver-*.svg` là sơ đồ vẽ (bố cục trang, chọn preset/codec theo mục đích, luồng Render Queue) — các mục dưới đây bổ sung ảnh thật bên cạnh sơ đồ, không thay sơ đồ. Bỏ qua Remote Rendering và IMF vì là tính năng `Studio`.

**Chuẩn bị chung:** mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps; V1 có 6 clip LOG 4K; A1 "Giong noi", A2 "Nhac nen"). Sang trang **Deliver** (icon tên lửa, ngoài cùng bên phải hàng icon trang dưới đáy; bản 21 không dùng ⇧8 để chuyển trang). Cửa sổ Resolve phóng toàn màn hình. Render Queue giữ sẵn hai job: Job 1 YouTube 1080p, Job 2 TikTok 1080p. Không bấm Render trừ khi mục ghi rõ; sau mỗi ảnh chọn lại preset **YouTube → 1080p** để về trạng thái gốc.

---

### DEL-01 — `deliver-preset-menu.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/deliver/giao-dien.md` — ngay sau heading `### 1. Preset`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** bấm ô **Preset** ở đầu panel Render Settings cho xổ danh sách, rê chuột lên **YouTube** cho hiện menu con 720p/1080p/1440p/2160p.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh panel Render Settings và menu.
- **Cần thấy rõ trong ảnh:** Custom Export trên cùng, nhóm mạng xã hội (YouTube, Vimeo, TikTok, Dropbox), H.264 Master, H.265 Master, ProRes, Audio Only, menu con độ phân giải của YouTube.
- **Alt + chú thích:** `![Menu Preset của Render Settings](../../assets/img/deliver-preset-menu.png)` — *Bản 21 gom preset vào một menu thả xuống thay cho hàng icon.*

### DEL-02 — `deliver-video-tab.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/deliver/cai-dat-xuat.md` — ngay sau heading `## Tab Video`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** ô Preset → **Custom Export**. Chọn tab **Video**, Format **MP4**, Codec **H.264**. Cuộn lên đầu tab.
- **Khung chụp:** chỉ một vùng — panel Render Settings từ nút Single clip/Individual clips tới hết phần nhìn thấy của tab Video.
- **Cần thấy rõ trong ảnh:** nút Render Single clip / Individual clips, ba tab Video · Audio · File, Export Video, Format, Codec, Encoder, Use hardware acceleration if available, Resolution, Frame rate, Quality.
- **Alt + chú thích:** `![Tab Video của Custom Export](../../assets/img/deliver-video-tab.png)` — *Chọn Custom Export thì mọi ô trong ba tab mới mở khoá.*

### DEL-03 — `deliver-advanced-settings.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/cai-dat-xuat.md` — ngay sau heading `### Advanced Settings — những ô đáng biết`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** như DEL-02, cuộn xuống và bấm mở **Advanced Settings**.
- **Khung chụp:** chỉ một vùng — phần Advanced Settings trong panel; ảnh dài thì cắt làm hai nửa ghép dọc.
- **Cần thấy rõ trong ảnh:** Data Levels, Retain sub-black and super-white data, Data burn-in, Force sizing to highest quality, Use render cached images, Render All Video Tracks, Enable flat pass.
- **Alt + chú thích:** `![Advanced Settings trong tab Video](../../assets/img/deliver-advanced-settings.png)` — *Phần lớn để mặc định; chỉ đổi khi biết rõ vì sao.*

### DEL-04 — `deliver-subtitle-settings.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/cai-dat-xuat.md` — ngay sau heading `### Subtitle Settings`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** như DEL-02, cuộn xuống cuối tab Video, tick **Export Subtitle**, mở menu **Format** cho thấy các kiểu xuất. Nếu demo chưa có track phụ đề thì thêm một track phụ đề trống ở trang Edit trước, chụp xong xoá đi.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh mục Subtitle Settings.
- **Cần thấy rõ trong ảnh:** ô Export Subtitle đã tick, các kiểu Burn into video, As a separate file, As embedded captions.
- **Alt + chú thích:** `![Subtitle Settings ở cuối tab Video](../../assets/img/deliver-subtitle-settings.png)` — *TikTok cần Burn into video; YouTube dùng file rời.*

### DEL-05 — `deliver-audio-tab.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/cai-dat-xuat.md` — ngay sau heading `## Tab Audio`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** Custom Export, Format **MP4**. Chọn tab **Audio**, mở menu **Codec** cho thấy danh sách codec tiếng.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh tab Audio.
- **Cần thấy rõ trong ảnh:** Export Audio, Codec với AAC trong danh sách, Sample Rate 48000, Bit Rate, Output Track (Bus 1), mục Audio Normalization.
- **Alt + chú thích:** `![Tab Audio của Custom Export](../../assets/img/deliver-audio-tab.png)` — *Codec tiếng đổi theo Format; MP4 trên Mac thì chọn AAC.*

### DEL-06 — `deliver-file-tab.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/deliver/cai-dat-xuat.md` — ngay sau heading `## Tab File`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** Custom Export, chọn tab **File**, chọn **Use Custom Filename**.
- **Khung chụp:** chỉ một vùng — tab File trong panel Render Settings.
- **Cần thấy rõ trong ảnh:** ba lựa chọn Use Custom Filename / Use Timeline Name / Use Source Filename, Use unique filenames, các ô đánh số file.
- **Alt + chú thích:** `![Tab File của Custom Export](../../assets/img/deliver-file-tab.png)` — *Chọn cách đặt tên file trước khi thêm job.*

### DEL-07 — `deliver-tiktok-vertical.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/deliver/preset-theo-nen-tang.md` — ngay sau heading `## TikTok, Reels, Shorts — video dọc`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** ô Preset → **TikTok** → **1080p**. Tick **Use vertical resolution** để Resolution đổi thành 1080 x 1920. Ảnh chỉ lấy panel nên timeline demo đang ngang cũng được; chụp xong bỏ tick.
- **Khung chụp:** chỉ một vùng — panel Render Settings dạng gọn của TikTok.
- **Cần thấy rõ trong ảnh:** tiêu đề panel có chữ TikTok, ô Use vertical resolution đã tick, Resolution 1080 x 1920, mục Upload directly to TikTok.
- **Alt + chú thích:** `![Preset TikTok với Use vertical resolution đã tick](../../assets/img/deliver-tiktok-vertical.png)` — *Preset mặc định không tick ô này — đây là bước hay quên nhất.*

### DEL-08 — `deliver-save-preset.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/preset-theo-nen-tang.md` — ngay sau heading `## Tự tạo preset`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** Custom Export → menu ba chấm của Render Settings → **Save as New Preset**. Gõ tên "Vlog 1080p", tick **Add to quick export**. Chụp xong bấm **Cancel**.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát hộp thoại.
- **Cần thấy rõ trong ảnh:** ô tên preset, dãy icon để chọn, ô Add to quick export đã tick, nút Save.
- **Alt + chú thích:** `![Hộp thoại lưu preset mới](../../assets/img/deliver-save-preset.png)` — *Tick Add to quick export để preset hiện ở mọi trang.*

### DEL-09 — `deliver-overwrite-warning.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `## Đưa một job vào hàng đợi`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** cần một file đã render sẵn trong thư mục đích. Chọn preset YouTube 1080p với đúng tên file và thư mục của Job 1, bấm **Add to Render Queue** cho hiện cảnh báo. Chụp xong bấm **No**.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát hộp thoại.
- **Cần thấy rõ trong ảnh:** dòng "This render may overwrite existing clips in this folder", hai nút Yes / No.
- **Alt + chú thích:** `![Cảnh báo ghi đè file khi thêm job](../../assets/img/deliver-overwrite-warning.png)` — *Bấm No rồi đổi tên file, trừ khi cố ý ghi đè.*

### DEL-10 — `deliver-render-range.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `## Xuất một đoạn`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** trên timeline Deliver, đặt `I` ở clip thứ 2 và `O` ở clip thứ 3. Bấm menu **Render** trên thanh timeline cho xổ danh sách.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh thanh trên timeline và thước thời gian.
- **Cần thấy rõ trong ảnh:** menu với Entire Timeline, In/Out Range, All Filtered Clips; thanh cam In/Out trên thước thời gian.
- **Alt + chú thích:** `![Menu Render và khoảng In/Out trên timeline Deliver](../../assets/img/deliver-render-range.png)` — *Đặt I và O thì Render tự chuyển thành In/Out Range.*

### DEL-11 — `deliver-timeline-filter.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `### Chỉ render lại clip đã sửa`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** bấm mũi tên cạnh nút **Clips** trên toolbar để mở menu **Timeline Filter**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh nút Clips và menu.
- **Cần thấy rõ trong ảnh:** All Clips, nhóm Modified Clips, nhóm Unrendered Clips.
- **Alt + chú thích:** `![Menu Timeline Filter](../../assets/img/deliver-timeline-filter.png)` — *Lọc chỉ còn clip đã sửa hoặc chưa render, rồi render riêng chúng.*

### DEL-12 — `deliver-job-details.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `### Sắp xếp, đặt tên, xem chi tiết`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** menu ba chấm của Render Queue → bật **Show Job Details**. Đổi tên Job 1 thành "YouTube", Job 2 thành "TikTok"; chụp xong trả tên cũ nếu cần.
- **Khung chụp:** chỉ một vùng — cột Render Queue bên phải.
- **Cần thấy rõ trong ảnh:** hai job có tên dễ nhớ, mỗi job hiện kích thước, định dạng, frame rate, kênh tiếng, độ dài; biểu tượng bút chì.
- **Alt + chú thích:** `![Render Queue khi bật Show Job Details](../../assets/img/deliver-job-details.png)` — *Đặt tên job theo nền tảng để khỏi nhầm khi hàng đợi dài.*

### DEL-13 — `deliver-rendering.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `### Đang render`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** chọn Job 1, bấm **Render 1**. Chụp khi thanh tiến độ khoảng giữa, rồi bấm **Stop Render** nếu không cần file.
- **Khung chụp:** chỉ một vùng — cột Render Queue cùng nút Stop Render ở đáy.
- **Cần thấy rõ trong ảnh:** thanh tiến độ trên job, thời gian còn lại, nút Stop Render.
- **Alt + chú thích:** `![Job đang render trong Render Queue](../../assets/img/deliver-rendering.png)` — *Nút Render đổi thành Stop Render trong lúc chạy.*

### DEL-14 — `deliver-quick-export.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/deliver/render-queue-va-loi.md` — ngay sau heading `## Quick Export`
- **Trang Resolve:** Edit (hoặc Cut)
- **Chuẩn bị:** sang trang **Edit**, menu **File → Quick Export**. Chọn preset H.264. Chụp xong đóng cửa sổ, không bấm Export.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát cửa sổ Quick Export.
- **Cần thấy rõ trong ảnh:** dãy icon preset trên cùng, preset H.264 đang chọn, thông số tóm tắt, nút Export.
- **Alt + chú thích:** `![Cửa sổ Quick Export](../../assets/img/deliver-quick-export.png)` — *Xuất bằng preset ngay từ trang đang làm, không cần sang Deliver.*
