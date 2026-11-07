# Danh sách ảnh cần chụp — luồng làm việc (`03-luong/`)

Khuôn mục: xem `FORMAT.md`. Trang luồng đi qua nhiều trang Resolve, nên phần lớn ảnh panel đã có trong danh sách của từng trang. File này chỉ liệt kê ảnh **riêng cho luồng**: ảnh cho thấy kết quả của cả một bước, hoặc giá trị cụ thể mà trang luồng dùng.

Ảnh đã có và đã nhúng: `color-6-nodes.png` (vlog-youtube bước 8, log-sang-rec709), `media-pool-clip-right-click.png` (vlog-youtube bước 1), `color-pal-warper.png` (chinh-anh bước 7). Sơ đồ vẽ, không cần chụp: `flow-vlog-youtube.svg`, `flow-video-doc.svg`, `flow-log-rec709.svg`, `flow-chinh-anh.svg`.

**Chuẩn bị chung:**
1. Mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps, V1 có 6 clip LOG 4K, A1 `Giong noi`, A2 `Nhac nen`).
2. Ảnh cho `chinh-anh.md`: dùng album **Demo - Anh** đã dựng theo phần "Chuẩn bị chung" của `photo.md` (ảnh JPG stock và ảnh mẫu CR3). Không dùng ảnh cá nhân.
3. Mọi thay đổi chỉ để chụp (node CST tạm, timeline dọc, marker) làm trên bản sao timeline hoặc xoá đi sau khi chụp, trừ khi mục ghi giữ lại.

---

### FLO-01 — `flow-vlog-chapter-markers.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/vlog-youtube.md` — ngay sau heading `## 3. Dựng thô`
- **Trang Resolve:** Edit
- **Chuẩn bị:** timeline "Demo - Vlog". Đặt 3 marker **cùng màu Blue** trên thước timeline (bấm `M` khi không chọn clip) ở đầu clip 1, clip 3, clip 5. Bấm đúp từng marker, đặt **Name** `Mo dau`, `Trai cuu`, `Ket`. Zoom timeline cho thấy cả 6 clip.
- **Khung chụp:** chỉ một vùng — thước timeline và track V1, A1, A2, toàn chiều ngang timeline.
- **Cần thấy rõ trong ảnh:** 3 marker cùng màu trên thước, 6 clip V1, tên track A1 `Giong noi`, A2 `Nhac nen`.
- **Alt + chú thích:** `![Ba marker cùng màu trên thước timeline làm chapter](../assets/img/flow-vlog-chapter-markers.png)` — *Marker cùng một màu sẽ thành chapter YouTube khi xuất.*
- **Ghi chú:** giữ các marker cho FLO-04.

### FLO-02 — `flow-vlog-mixer-chain.png`
- **Ưu tiên:** P1
- **Chèn vào:** `03-luong/vlog-youtube.md` — ngay sau heading `## 9. Âm thanh tinh`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** bấm **Mixer**. Cột A1: bật **Dialogue Leveler** ở ô **Dial Lev**, bật **EQ** và **Dynamics** (Compressor Ratio 3:1). Cột A2: bật **Ducker**, Source = A1. Cột **Bus 1**: thêm **Limiter** vào mục **Effects**, Ceiling −1 dB. Thiếu ô Ducker: menu ba chấm Mixer → **Visible Track FX** → tick Ducker.
- **Khung chụp:** chỉ một vùng — Mixer, ba cột A1, A2, Bus 1, từ hàng Effects tới fader.
- **Cần thấy rõ trong ảnh:** ô Dial Lev sáng ở A1, ô EQ và Dynamics có đường cong nhỏ ở A1, ô Ducker sáng ở A2, Limiter trong Effects của Bus 1.
- **Alt + chú thích:** `![Mixer Fairlight với chuỗi xử lý giọng, Ducker và Limiter](../assets/img/flow-vlog-mixer-chain.png)` — *Giọng xử lý ở A1, nhạc tự nhỏ ở A2, chặn trần ở Bus 1.*

### FLO-03 — `flow-vlog-loudness-result.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/vlog-youtube.md` — ngay sau heading `## 9. Âm thanh tinh` (đặt sau FLO-02, cạnh dòng 7 của bảng)
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** giữ chuỗi xử lý của FLO-02. **Meters** → menu ba chấm của Loudness meter → **YouTube**. Đưa con trỏ về đầu, bấm **Reset**, phát hết timeline.
- **Khung chụp:** chỉ một vùng — Loudness meter.
- **Cần thấy rõ trong ảnh:** chuẩn YouTube đang chọn, **Integrated** quanh −14 LUFS, **TP** dưới −1.
- **Alt + chú thích:** `![Loudness meter sau khi phát hết video, Integrated quanh −14 LUFS](../assets/img/flow-vlog-loudness-result.png)` — *Đo cả bài: Integrated quanh −14, TP dưới −1 là đạt.*
- **Ghi chú:** nếu số đo khác xa −14, ghi lại số thật vào chú thích, không sửa ảnh.

### FLO-04 — `flow-vlog-youtube-upload.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/vlog-youtube.md` — ngay sau heading `## 10. Xuất`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** ô **Preset** → **YouTube** → **1080p**. **File Name** `Demo - Vlog`. Tick **Upload directly to YouTube**: phần Title, Description, Chapters from Markers, Upload Thumbnail, Visibility, Category hiện ra. **Chapters from Markers** chọn màu Blue (marker của FLO-01). **Visibility** Private. Không bấm Render.
- **Khung chụp:** chỉ một vùng — panel Render Settings dạng gọn, từ tiêu đề preset tới hết mục upload. Dài quá thì ghép hai nửa.
- **Cần thấy rõ trong ảnh:** File Name, Format MP4, Video Codec H.264, Normalize Audio, ô Upload directly to YouTube đã tick, Chapters from Markers màu Blue, Visibility.
- **Alt + chú thích:** `![Preset YouTube với Upload directly to YouTube và Chapters from Markers](../assets/img/flow-vlog-youtube-upload.png)` — *Tick Upload là có ô tiêu đề, chapter, thumbnail ngay trong Resolve.*
- **Ghi chú:** ô upload có thể yêu cầu đăng nhập tài khoản YouTube ở **Preferences → System → Internet Accounts**. Không đăng nhập tài khoản thật để chụp; nếu ô bị khoá khi chưa đăng nhập, chụp trạng thái khoá và ghi lại để sửa trang.

### FLO-05 — `flow-vlog-export-still-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `03-luong/vlog-youtube.md` — ngay sau heading `## 11. Thumbnail`
- **Trang Resolve:** Edit (menu File)
- **Chuẩn bị:** con trỏ trên clip trại cừu, khung mặt cô gái rõ. Mở **File → Export** cho hiện menu con.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt menu File + menu con Export.
- **Cần thấy rõ trong ảnh:** mục **Current Frame as Still** đang được rê chuột.
- **Alt + chú thích:** `![Menu File → Export → Current Frame as Still](../assets/img/flow-vlog-export-still-menu.png)` — *Lấy đúng khung đang đứng làm ảnh bìa.*

### FLO-06 — `flow-doc-vertical-resolution.png`
- **Ưu tiên:** P1
- **Chèn vào:** `03-luong/video-doc.md` — ngay sau heading `## Tình huống A — quay dọc sẵn`
- **Trang Resolve:** hộp thoại Project Settings
- **Chuẩn bị:** `⇧9` → **Master Settings**. **Timeline resolution** `1920 x 1080 HD`, tick **Use vertical resolution**. Không bấm Save — bấm **Cancel** sau khi chụp để project demo giữ khung ngang.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt mục Timeline Format.
- **Cần thấy rõ trong ảnh:** Timeline resolution, ô Use vertical resolution đã tick, cỡ khung hiện 1080 x 1920, Timeline frame rate.
- **Alt + chú thích:** `![Project Settings với Use vertical resolution đã tick](../assets/img/flow-doc-vertical-resolution.png)` — *Một ô tick đảo 1920×1080 thành 1080×1920.*

### FLO-07 — `flow-doc-timeline-settings.png`
- **Ưu tiên:** P1
- **Chèn vào:** `03-luong/video-doc.md` — ngay sau heading `### Các bước`
- **Trang Resolve:** hộp thoại Timeline Settings
- **Chuẩn bị:** Media Pool → chọn "Demo - Vlog" → **Edit → Duplicate Timeline**, đổi tên `Demo - Vlog doc`. Chuột phải timeline mới → **Timelines → Timeline Settings** → bỏ tick **Use Project Settings**. Tab **Format**: tick **Use vertical resolution**. **Mismatched resolution files** → **Scale full frame with crop**.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Timeline Settings.
- **Cần thấy rõ trong ảnh:** ô Use Project Settings bỏ tick, bốn tab Format/Monitor/Output/Color, 1080 x 1920, Mismatched resolution files = Scale full frame with crop.
- **Alt + chú thích:** `![Timeline Settings của bản dọc](../assets/img/flow-doc-timeline-settings.png)` — *Bỏ tick Use project settings, tick Use vertical resolution, Mismatched resolution = Scale full frame with crop. Frame rate mờ vì timeline đã có clip.*
- **Ghi chú:** nếu ô Mismatched resolution files không nằm ở tab Format, ghi lại tab thật để sửa bước 5 của trang. Giữ timeline `Demo - Vlog doc` cho FLO-08, FLO-09.

### FLO-08 — `flow-doc-reframe.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/video-doc.md` — ngay sau heading `### Các bước` (đặt sau FLO-07, cạnh bước 6)
- **Trang Resolve:** Edit
- **Chuẩn bị:** timeline `Demo - Vlog doc`. Chọn clip trại cừu (cô gái lệch một bên). **Inspector → Transform**: **Zoom** `1.15`, kéo **Position X** cho cô gái vào giữa khung.
- **Khung chụp:** chỉ một vùng — Timeline Viewer khung dọc + Inspector phần Transform.
- **Cần thấy rõ trong ảnh:** khung dọc 9:16, chủ thể ở giữa, Zoom X/Y = 1.150, Position X khác 0.
- **Alt + chú thích:** `![Chỉnh Position X và Zoom cho clip trong timeline dọc](../assets/img/flow-doc-reframe.png)` — *Clip nào chủ thể lệch thì kéo Position X; cần cận hơn thì tăng Zoom.*

### FLO-09 — `flow-doc-safe-area.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/video-doc.md` — ngay sau heading `## Bố cục khung dọc`
- **Trang Resolve:** Cut
- **Chuẩn bị:** mở timeline `Demo - Vlog doc` ở trang Cut, con trỏ ở clip 1 (có chữ "PHO MAI & RAU CU"). Nút **Safe Area** góc phải Viewer → **Title** và **Action**.
- **Khung chụp:** chỉ một vùng — Viewer trang Cut với khung an toàn.
- **Cần thấy rõ trong ảnh:** hai khung Title và Action, chữ tiêu đề nằm trong khung Title.
- **Alt + chú thích:** `![Khung an toàn Title và Action trên Viewer khung dọc](../assets/img/flow-doc-safe-area.png)` — *Chữ nằm trong khung Title thì không bị giao diện app che.*
- **Ghi chú:** chụp thêm menu Safe Area mở xổ (nhóm **Social Media** → **9:16**) nếu được, đặt tên `flow-doc-safe-area-menu.png` — menu xổ, cần chụp toàn màn hình rồi cắt.

### FLO-10 — `flow-doc-adjustment-clip.png`
- **Ưu tiên:** P3
- **Chèn vào:** `03-luong/video-doc.md` — ngay sau heading `### Cách dùng Adjustment Clip`
- **Trang Resolve:** Edit
- **Chuẩn bị:** trên bản sao của "Demo - Vlog" (không phải bản doc). Kéo **Adjustment Clip** từ Effects → Toolbox → Effects lên V2, kéo dài hết 6 clip.
- **Khung chụp:** chỉ một vùng — timeline, V1 và V2, toàn chiều ngang.
- **Cần thấy rõ trong ảnh:** Adjustment Clip trên V2 phủ hết các clip V1, nút bật/tắt track V2.
- **Alt + chú thích:** `![Adjustment Clip phủ cả timeline trên track V2](../assets/img/flow-doc-adjustment-clip.png)` — *Bật V2 khi xuất bản dọc, tắt khi xuất bản ngang.*

### FLO-11 — `flow-log-before-after.png`
- **Ưu tiên:** P1
- **Chèn vào:** `03-luong/log-sang-rec709.md` — ngay sau heading `## Kiểm tra đã đúng chưa`
- **Trang Resolve:** Color
- **Chuẩn bị:** clip trại cừu. Bấm `⇧D` tắt grade, **Grab Still** (`⌥⌘G`) để có bản LOG gốc. Bấm `⇧D` bật lại grade. Bấm đúp still trong Gallery để bật **Image Wipe**, kéo đường chia vào giữa. Mở scope **Waveform** (`⇧⌘W` hoặc nút scope).
- **Khung chụp:** chỉ một vùng — Viewer chia đôi + Waveform. Hai vùng cách xa thì chụp riêng rồi ghép dọc.
- **Cần thấy rõ trong ảnh:** nửa trái LOG xám nhạt, nửa phải đã chuyển; Waveform trải gần 0–1023.
- **Alt + chú thích:** `![Footage LOG trước và sau khi chuyển sang Rec.709, kèm Waveform](../assets/img/flow-log-before-after.png)` — *Trái: LOG gốc, dồn ở giữa Waveform. Phải: đã chuyển, trải gần hết thang.*

### FLO-12 — `flow-log-cst-input-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/log-sang-rec709.md` — ngay sau heading `## Profile của các máy phổ biến`
- **Trang Resolve:** Color
- **Chuẩn bị:** thêm node tạm, thả **Color Space Transform** lên. Bảng Effects → tab **Settings** → mở menu **Input Color Space** cho xổ. Chụp lần hai với menu **Input Gamma** xổ. Xong xoá node tạm.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt bảng Effects + menu (danh sách dài thì cuộn, ghép hai nửa).
- **Cần thấy rõ trong ảnh:** tên các mục theo hãng: Sony, Canon, Panasonic, Fujifilm, DJI, GoPro, Blackmagic Design, DaVinci Wide Gamut.
- **Alt + chú thích:** `![Menu Input Color Space của Color Space Transform](../assets/img/flow-log-cst-input-menu.png)` — *Tìm theo tên hãng máy trước, rồi chọn đúng gamut.*
- **Ghi chú:** chép lại đúng tên Fujifilm, DJI, GoPro, Canon trong hai menu này để sửa bảng profile của trang (manual không liệt kê).

### FLO-13 — `flow-log-input-color-space-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/log-sang-rec709.md` — ngay sau heading `### Cách 2 — Color Management toàn project`
- **Trang Resolve:** Media (hoặc Media Pool ở trang Edit)
- **Chuẩn bị:** **Lưu project trước.** `⇧9` → **Color Management** → **Color science** `DaVinci YRGB Color Managed`, tick **Automatic Color Management**, **Output color space** Rec.709 → **Save**. Chọn 2 clip LOG trong bin `01 Footage` → chuột phải → rê tới **Input Color Space** cho hiện menu con. Chụp xong đổi Color science về **DaVinci YRGB** (hoặc mở lại bản lưu) để grade demo không lệch.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Media Pool + menu + menu con.
- **Cần thấy rõ trong ảnh:** mục Input Color Space và danh sách profile trong menu con.
- **Alt + chú thích:** `![Chọn Input Color Space cho clip LOG trong Media Pool](../assets/img/flow-log-input-color-space-menu.png)` — *Chỉ có mục này khi project đang ở chế độ Color Managed.*

### FLO-14 — `flow-log-shared-node.png`
- **Ưu tiên:** P2
- **Chèn vào:** `03-luong/log-sang-rec709.md` — ngay sau heading `## Áp cho mọi clip cùng máy`
- **Trang Resolve:** Color
- **Chuẩn bị:** ở clip 1, thêm node CST tạm, đặt nhãn `CST`, chuột phải → **Save as Shared Node**. Chọn clip 2, chuột phải vùng trống Node Editor → **Add Node** cho hiện menu con.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Node Editor + menu.
- **Cần thấy rõ trong ảnh:** Shared Node `CST` ở cuối menu con Add Node.
- **Alt + chú thích:** `![Shared Node CST ở cuối menu Add Node](../assets/img/flow-log-shared-node.png)` — *Lưu một lần, thêm vào clip khác từ cuối menu Add Node.*
- **Ghi chú:** xoá node tạm ở cả hai clip sau khi chụp. Chuột phải Shared Node xem có mục **Lock Node** không, ghi lại.

### FLO-15 — `flow-log-mac-display-pref.png`
- **Ưu tiên:** P3
- **Chèn vào:** `03-luong/log-sang-rec709.md` — ngay sau heading `## Lỗi hay gặp`
- **Trang Resolve:** hộp thoại Preferences
- **Chuẩn bị:** **DaVinci Resolve → Preferences** → **System** → **General**. Không đổi gì.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt nhóm ô có Use Mac Display Color Profile for viewers và Automatically Tag Rec.709 Scene Clips as Rec.709-A.
- **Cần thấy rõ trong ảnh:** hai ô trên và trạng thái tick hiện tại.
- **Alt + chú thích:** `![Preferences System General với ô Use Mac Display Color Profile](../assets/img/flow-log-mac-display-pref.png)` — *Viewer dùng profile màn hình Mac để gần với file xuất ra.*
- **Ghi chú:** nếu hai ô không nằm ở System → General, ghi lại đúng chỗ để sửa trang.

### FLO-16 — `flow-photo-color-warper.png`
- **Ưu tiên:** P3
- **Chèn vào:** `03-luong/chinh-anh.md` — ngay sau heading `## 7. Chỉnh từng vùng — sang trang Color`
- **Trang Resolve:** Color
- **Chuẩn bị:** cần một ảnh JPG stock có người mặc áo màu rõ (đỏ hoặc xanh) trong album **Demo - Anh**. Mở album ở trang Photo, chuyển sang **Color**, chọn ảnh đó. `⌥S` thêm node 02, mở **Color Warper**, kéo điểm lưới ở màu áo sang màu khác.
- **Khung chụp:** chỉ một vùng — Viewer + Node Editor (node 01 là phần chỉnh từ trang Photo, node 02 mới). Ảnh Color Warper đã có riêng, không cần chụp lại palette.
- **Cần thấy rõ trong ảnh:** áo đã đổi màu, phần còn lại giữ nguyên; hai node.
- **Alt + chú thích:** `![Ảnh ở trang Color, node 02 đổi màu áo bằng Color Warper](../assets/img/flow-photo-color-warper.png)` — *Node 01 là chỉnh sửa từ trang Photo; node 02 chỉ đổi màu áo.*

---

## Ảnh của khu khác dùng lại được (khi đã chụp)

Không chụp lại. Khi các ảnh này có, nhúng thêm vào trang luồng:

| Ảnh | Nhúng vào | Ngay sau heading |
|---|---|---|
| `start-project-settings-timeline-format.png` (STA-04) | `03-luong/vlog-youtube.md` | `## 1. Chuẩn bị project` |
| `fairlight-normalize-dialog.png` (FAI-04) | `03-luong/vlog-youtube.md` | `## 5. Nhạc nền` |
| `edit-subtitle-track.png` (EDT-16) | `03-luong/vlog-youtube.md` | `## 7. Phụ đề` |
| `deliver-tiktok-vertical.png` (DEL-07) | `03-luong/video-doc.md` | `### Không có phụ đề — preset TikTok` |
| `deliver-subtitle-settings.png` (DEL-04) | `03-luong/video-doc.md` | `### Có phụ đề — Custom Export` |
| `color-cst-settings.png` (COL-18) | `03-luong/log-sang-rec709.md` | `### Cách 1 — Color Space Transform (khuyên dùng)` |
| `color-project-color-management.png` (COL-11) | `03-luong/log-sang-rec709.md` | `### Cách 2 — Color Management toàn project` |
| `deliver-advanced-settings.png` (DEL-03) | `03-luong/log-sang-rec709.md` | `## Xuất và soát màu` |
| `photo-raw-exposure-color.png` (PHO-17) | `03-luong/chinh-anh.md` | `## 3. Chỉnh RAW — cân bằng trắng và phơi sáng` |
| `photo-tools-crop.png` (PHO-21) | `03-luong/chinh-anh.md` | `## 5. Crop và thẳng khung` |
| `photo-paste-attributes.png` (PHO-23) | `03-luong/chinh-anh.md` | `## 6. Áp cho cả loạt` |
| `photo-quick-export.png` (PHO-28) | `03-luong/chinh-anh.md` | `## 8. Xuất` |
