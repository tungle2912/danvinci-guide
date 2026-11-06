# Danh sách ảnh cần chụp — trang Color (`02-trang/color/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có, không chụp lại:

- `page-color.png` (toàn cửa sổ, nhúng ở giao-dien) và `color-6-nodes.png` (nhúng ở README).
- 15 ảnh palette `color-pal-*.png`, đã nhúng hết:
  - Primaries ở chế độ **Color Bars**.
  - Curves, Qualifier, Window, Tracker, Warper, Blur, Key, Sizing, HDR, RGB Mixer, ColorSlice, Color Match, Motion Effects, Camera Raw.

Sơ đồ vẽ (không chụp):

- `color-layout.svg`, `node-chain.svg`, `node-types.svg`.
- `color-lgg-vung-tac-dong.svg`, `color-node-kieu-noi.svg`, `color-qualifier-window-tracker.svg`.
- `color-doc-parade.svg`, `color-doc-vectorscope.svg`, `color-rcm-pipeline.svg`, `color-lut-vi-tri.svg`.

**Chuẩn bị chung:**
1. Mở project "So tay DaVinci - Demo", timeline "Demo - Vlog", sang trang **Color**.
2. Mỗi clip trên V1 đã có grade 6 node: 01 Balance … 06 Finishing. Giữ nguyên grade, trừ khi mục ghi khác.
3. Mặc định chọn **clip có cô gái ở trại cừu** (có da người, áo, trời). Mục nào cần clip món ăn thì ghi rõ.
4. Trong Gallery có sẵn ít nhất 2 still: chọn clip món ăn, chuột phải Viewer → **Grab Still**; làm lại với clip trại cừu.
5. Sau mỗi mục có chỉnh thử, bấm `⌘Z` hoặc xoá node thêm để trả grade về như cũ.

---

### COL-01 — `color-pal-primaries-wheels.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/can-bang.md` — ngay sau heading `## Sáng tối — 4 bánh xe`, sau sơ đồ vùng tác động
- **Trang Resolve:** Color
- **Chuẩn bị:** chọn node 01 Balance. Mở palette **Primaries** (icon thứ 3). Bấm icon chế độ **Color Wheels** ở góc trên phải palette (ảnh đã có đang ở Color Bars).
- **Khung chụp:** chỉ một vùng — toàn bộ palette Primaries, từ tiêu đề tới hàng thanh dưới cùng.
- **Cần thấy rõ trong ảnh:**
  - Bốn bánh xe Lift, Gamma, Gain, Offset, mỗi cái có vòng xoay bên dưới.
  - Hàng thanh trên: Temp, Tint, Contrast, Pivot, Mid/Detail.
  - Hàng thanh dưới: Color Boost, Shadows, Highlights, Saturation, Hue, Lum Mix.
  - Nút **A** và ống hút White Balance.
  - Ba icon chế độ góc trên phải.
- **Alt + chú thích:** `![Palette Primaries ở chế độ Color Wheels: bốn bánh xe Lift Gamma Gain Offset và hai hàng thanh](../../assets/img/color-pal-primaries-wheels.png)` — *Chế độ hay dùng nhất: kéo tâm bánh xe để đổi màu, xoay vòng dưới để đổi độ sáng.*

### COL-02 — `color-wb-eyedropper.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/can-bang.md` — ngay sau heading `### Cách 2 — Ống hút White Balance`
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Chọn clip món ăn, node 01. Primaries ở **Color Wheels**.
  - Bấm ống hút **White Balance**, rê con trỏ lên vùng đĩa trắng trên Viewer (chưa bấm), để tooltip RGB hiện ra (nếu có).
- **Khung chụp:** chỉ một vùng — cắt hai mảnh ghép ngang:
  - (1) góc trên trái palette Primaries, thấy nút A và ống hút đang sáng;
  - (2) vùng Viewer quanh con trỏ ống hút.
- **Cần thấy rõ trong ảnh:** vị trí thật của nút **A** và ống hút (trên trái hay dưới trái — sách đang ghi trên trái), con trỏ ống hút trên vùng trắng.
- **Alt + chú thích:** `![Ống hút White Balance trong palette Primaries và con trỏ trên vùng trắng của Viewer](../../assets/img/color-wb-eyedropper.png)` — *Bấm ống hút rồi bấm vào chỗ đáng lẽ trắng hoặc xám.*

### COL-03 — `color-node-add-menu.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/node.md` — ngay sau heading `## Thêm node`
- **Trang Resolve:** Color
- **Chuẩn bị:** chuột phải node 03 trong Node Editor → rê tới **Add Node** cho submenu xổ ra.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng node + menu chính + submenu.
- **Cần thấy rõ trong ảnh:**
  - Submenu Add Node đủ các kiểu node (Serial, Serial trước node, Parallel, Layer, Outside…), phím tắt in bên phải từng mục.
  - Trong menu chính: các mục **Change Label**, **LUT**, **Reset Node Grade**.
- **Alt + chú thích:** `![Menu chuột phải node, submenu Add Node mở](../../assets/img/color-node-add-menu.png)` — *Mọi kiểu node mới đều ở Add Node; phím tắt in sẵn bên phải.*

### COL-04 — `color-qualifier-highlight.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/curves-va-vung.md` — ngay sau heading `### Qualifier — hút màu`, sau ảnh palette Qualifier
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Clip trại cừu, chọn node 04 Secondary. Qualifier chế độ **3D**, kéo một nét qua áo khoác cô gái.
  - Bấm `⇧H`.
- **Khung chụp:** chỉ một vùng — toàn bộ Viewer.
- **Cần thấy rõ trong ảnh:** vùng áo giữ màu, phần còn lại xám phẳng; nét vẽ 3D trên áo; nút **Highlight** sáng trên thanh công cụ Viewer.
- **Alt + chú thích:** `![Viewer ở chế độ Highlight: chỉ áo cô gái giữ màu, nền chuyển xám](../../assets/img/color-qualifier-highlight.png)` — *`⇧H`: phần được chọn giữ màu, phần còn lại xám — thấy ngay chọn thừa hay thiếu.*

### COL-05 — `color-window-viewer.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/curves-va-vung.md` — ngay sau heading `### Window — khoanh vùng`, sau ảnh palette Window
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Clip trại cừu, `⌥S` thêm node sau node 04.
  - Palette Window → **Circle**. Kéo khung quanh mặt cô gái, kéo vòng mềm ra rộng.
  - Menu onscreen control để **Power Window**.
- **Khung chụp:** chỉ một vùng — Viewer, cắt quanh khuôn mặt và khung tròn.
- **Cần thấy rõ trong ảnh:** viền trong (đỏ/trắng), viền mềm ngoài, điểm tâm, các điểm kéo trên viền.
- **Alt + chú thích:** `![Khung Circle Window quanh mặt cô gái trên Viewer, có viền mềm bên ngoài](../../assets/img/color-window-viewer.png)` — *Kéo tâm để dời, kéo điểm trên viền để đổi cỡ, kéo vòng ngoài để làm mềm.*

### COL-06 — `color-scope-parade.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `## Parade`, sau sơ đồ Parade
- **Trang Resolve:** Color
- **Chuẩn bị:** clip món ăn, đã có grade. Scope góc dưới phải → chọn **Parade**. Nút Option của scope: tắt Low Pass Filter.
- **Khung chụp:** chỉ một vùng — ô scope góc dưới phải, kèm thanh tiêu đề có menu chọn loại scope.
- **Cần thấy rõ trong ảnh:** ba cột R, G, B; thang 0–1023 bên trái; chân ba cột gần ngang nhau.
- **Alt + chú thích:** `![Scope Parade thật của clip món ăn: ba cột R G B](../../assets/img/color-scope-parade.png)` — *Clip đã cân bằng: chân và đỉnh ba cột gần ngang nhau.*

### COL-07 — `color-scope-waveform.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `## Waveform`
- **Trang Resolve:** Color
- **Chuẩn bị:** clip trại cừu (có trời sáng). Scope → **Waveform**, nút Option → chế độ **Y**.
- **Khung chụp:** chỉ một vùng — ô scope góc dưới phải.
- **Cần thấy rõ trong ảnh:** khối độ sáng trải từ gần 0 tới gần 1000; vùng trời ở phần trên; thang 0–1023.
- **Alt + chú thích:** `![Scope Waveform chế độ Y của clip trại cừu](../../assets/img/color-scope-waveform.png)` — *Trái sang phải trên scope là trái sang phải trong khung hình; trời nằm ở phần cao.*

### COL-08 — `color-scope-vectorscope.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `## Vectorscope`, sau sơ đồ Vectorscope
- **Trang Resolve:** Color
- **Chuẩn bị:** clip trại cừu. Scope → **Vectorscope**. Nút Option → bật **Show Skin Tone Indicator**.
- **Khung chụp:** chỉ một vùng — ô scope góc dưới phải.
- **Cần thấy rõ trong ảnh:** vạch skin tone hướng 11 giờ, các ô mục tiêu màu, đám màu da gần vạch.
- **Alt + chú thích:** `![Vectorscope thật có vạch màu da](../../assets/img/color-scope-vectorscope.png)` — *Vạch chéo hướng 11 giờ là vạch màu da; da người nằm dọc theo nó.*

### COL-09 — `color-viewer-title-bar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `### Thanh tiêu đề — trên cùng Viewer`
- **Trang Resolve:** Color
- **Chuẩn bị:** Viewer cỡ thường. Bấm nút **Image Wipe** cho các tuỳ chọn wipe hiện bên phải hàng dưới.
- **Khung chụp:** chỉ một vùng — toàn chiều ngang Viewer, từ thanh tiêu đề tới hết thanh công cụ Image Wipe · Split Screen · Highlight.
- **Cần thấy rõ trong ảnh:**
  - Thanh tiêu đề: Zoom, tên timeline, timecode, Viewer Guides, Proxy, độ phân giải, Bypass, Expand, nút ba chấm.
  - Thanh dưới: ba nút so sánh và các kiểu wipe.
- **Alt + chú thích:** `![Thanh tiêu đề và thanh công cụ Viewer trang Color](../../assets/img/color-viewer-title-bar.png)` — *Hàng trên: hiển thị và Bypass. Hàng dưới: Wipe, Split Screen, Highlight.*

### COL-10 — `color-lut-browser.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/lut-va-quan-ly-mau.md` — ngay sau heading `## LUT Browser`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm nút **LUTs** trên toolbar. Chọn nhóm **Blackmagic Design** ở cột trái, chế độ xem **Thumbnail**. Gắn sao một LUT.
- **Khung chụp:** chỉ một vùng — toàn bộ khung LUT Browser.
- **Cần thấy rõ trong ảnh:** cột nhóm bên trái (có **Favorites**), lưới LUT có ảnh xem trước, ngôi sao trên LUT đã gắn, nút Column/Thumbnail và kính lúp.
- **Alt + chú thích:** `![LUT Browser: cột nhóm bên trái, lưới LUT có ảnh xem trước](../../assets/img/color-lut-browser.png)` — *Rê chuột qua LUT để xem trước; kéo thả lên node để áp.*

### COL-11 — `color-project-color-management.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/lut-va-quan-ly-mau.md` — ngay sau heading `### Bật Color Managed — cách đơn giản`
- **Trang Resolve:** hộp thoại Project Settings
- **Chuẩn bị:**
  - **Project Settings** → **Color Management**. Tạm đổi **Color science** sang **DaVinci YRGB Color Managed**, tick **Automatic Color Management**.
  - Chụp xong bấm **Cancel**, không lưu, để grade demo không lệch.
- **Khung chụp:** hộp thoại — cắt phần nội dung bên phải, từ **Color Space & Transforms** tới hết **Output color space**.
- **Cần thấy rõ trong ảnh:** Color science, ô tick Automatic Color Management, Color processing mode, Output color space.
- **Alt + chú thích:** `![Project Settings, mục Color Management, chế độ Color Managed tự động](../../assets/img/color-project-color-management.png)` — *Bốn ô cần đặt: Color science, Automatic, SDR, Output Rec.709.*

### COL-12 — `color-gallery.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `## Gallery`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm **Gallery** trên toolbar. Bấm nút album ở góc trên trái Gallery cho cột album hiện ra. Bật nút **Memories**.
- **Khung chụp:** chỉ một vùng — toàn bộ Gallery.
- **Cần thấy rõ trong ảnh:** cột album (Stills, PowerGrade), 2 still đã chụp, hàng Memories A–H.
- **Alt + chú thích:** `![Gallery trang Color: cột album, hai still và hàng Memories](../../assets/img/color-gallery.png)` — *Bấm đúp still để wipe; chuột phải still để áp grade.*

### COL-13 — `color-image-wipe.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `#### Image Wipe — so với still`
- **Trang Resolve:** Color
- **Chuẩn bị:** chọn clip món ăn khác clip của still. Bấm đúp still món ăn trong Gallery. Kiểu wipe **Horizontal**, kéo đường chia ra giữa.
- **Khung chụp:** chỉ một vùng — toàn bộ Viewer.
- **Cần thấy rõ trong ảnh:** đường chia dọc giữa ảnh, nửa trái là clip hiện tại, nửa phải là still; nút Image Wipe sáng.
- **Alt + chú thích:** `![Viewer chia đôi so clip hiện tại với still](../../assets/img/color-image-wipe.png)` — *Kéo đường chia để so từng vùng; `⌥W` đảo hai bên.*

### COL-14 — `color-split-screen.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `#### Split Screen — xem nhiều ảnh một lúc`
- **Trang Resolve:** Color
- **Chuẩn bị:** `⌘`+bấm chọn 4 clip trên dải clip. Bấm **Split Screen** → chọn **Selected Clips**.
- **Khung chụp:** chỉ một vùng — Viewer kèm thanh công cụ có menu chế độ bên phải.
- **Cần thấy rõ trong ảnh:** lưới 4 ô, viền xám ở ô hiện tại, menu chế độ ghi Selected Clips.
- **Alt + chú thích:** `![Split Screen chế độ Selected Clips: bốn clip trong một Viewer](../../assets/img/color-split-screen.png)` — *So cả cảnh một lúc để bắt clip lệch tông.*

### COL-15 — `color-scopes-4up.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `### 1-up, 2-up, 4-up`
- **Trang Resolve:** cửa sổ Video Scopes
- **Chuẩn bị:**
  - Clip trại cừu, mở **Workspace → Video Scopes → On** (`⇧⌘W`), chọn **4-up**.
  - Đặt bốn ô: Waveform, Parade, Vectorscope, Histogram.
- **Khung chụp:** cửa sổ riêng — chụp toàn màn hình rồi cắt đúng cửa sổ Scopes.
- **Cần thấy rõ trong ảnh:** nút chọn 1/2/4/9-up góc trên phải, tên scope ở góc trên trái mỗi ô.
- **Alt + chú thích:** `![Cửa sổ Scopes 4-up: Waveform, Parade, Vectorscope, Histogram](../../assets/img/color-scopes-4up.png)` — *Bố trí 4-up hay dùng: chỉnh một clip không cần đổi scope qua lại.*

### COL-16 — `color-scope-settings-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `### Cài đặt chung — menu ⋯`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm menu **⋯** ở góc trên phải ô scope.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt ô scope + menu.
- **Cần thấy rõ trong ảnh:** các mục trong menu, có **Display Qualifier Focus**.
- **Alt + chú thích:** `![Menu cài đặt chung của scope](../../assets/img/color-scope-settings-menu.png)` — *Cài đặt áp cho mọi scope.*

### COL-17 — `color-curve-hue-vs-sat.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/curves-chi-tiet.md` — ngay sau heading `## Hue vs Sat — đậm/nhạt một màu`
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Clip trại cừu, `⌥S` thêm node. Curves → **Hue vs Sat**.
  - Bấm ô màu **xanh dương** ở thanh dưới để có ba điểm, kéo điểm giữa lên khoảng 1.30.
- **Khung chụp:** chỉ một vùng — palette Curves.
- **Cần thấy rõ trong ảnh:** ba điểm, điểm giữa nhô lên ở vùng xanh dương, ô Input/Output, 6 ô màu.
- **Alt + chú thích:** `![Curve Hue vs Sat: điểm ở vùng xanh dương kéo lên](../../assets/img/color-curve-hue-vs-sat.png)` — *Trời đậm hơn, da không đổi vì điểm hai bên khoá phạm vi.*

### COL-18 — `color-cst-settings.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/lut-va-quan-ly-mau.md` — ngay sau heading `### Thông số`
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Thêm node trước 01 (`⇧S`), kéo **Color Space Transform** từ Effects thả lên.
  - Đặt Input theo profile LOG của footage demo (hỏi người quay; nếu không rõ thì để Sony S-Gamut3.Cine / S-Log3 cho ảnh minh hoạ).
  - Đặt Output Rec.709 / Gamma 2.4, Tone Mapping **DaVinci**.
  - Chụp xong xoá node.
- **Khung chụp:** chỉ một vùng — bảng Effects, tab **Settings**, toàn bộ thông số CST.
- **Cần thấy rõ trong ảnh:** Input/Output Color Space, Input/Output Gamma, Tone Mapping Method, Gamut Mapping Method.
- **Alt + chú thích:** `![Thông số Color Space Transform trong tab Settings của Effects](../../assets/img/color-cst-settings.png)` — *Vào: profile máy quay. Ra: Rec.709 Gamma 2.4.*

### COL-19 — `color-qualifier-3d-strokes.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/curves-va-vung.md` — ngay sau heading `### Qualifier — hút màu`, sau đoạn "Mỗi nét bạn vẽ là một dòng…"
- **Trang Resolve:** Color
- **Chuẩn bị:** như COL-04 nhưng thêm một nét `⌥`-kéo (nét trừ, màu đỏ). Tắt `⇧H`.
- **Khung chụp:** chỉ một vùng — palette Qualifier ở chế độ 3D.
- **Cần thấy rõ trong ảnh:** danh sách nét (một nét thêm, một nét trừ), ô màu, thùng rác, icon chế độ 3D đang chọn.
- **Alt + chú thích:** `![Qualifier chế độ 3D với danh sách nét thêm và nét trừ](../../assets/img/color-qualifier-3d-strokes.png)` — *Mỗi nét một dòng: bấm ô màu để tắt tạm, bấm thùng rác để xoá.*

### COL-20 — `color-thumbnail-strip.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `### Dải clip (Thumbnail timeline)`
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Cắm cờ màu cho clip 02 (chuột phải → **Flags**).
  - Bấm đúp dòng chữ dưới ảnh để hiện tên clip.
- **Khung chụp:** chỉ một vùng — 3 thumbnail đầu, phóng to.
- **Cần thấy rõ trong ảnh:** số clip có vòng cầu vồng, timecode nguồn, số track V1, cờ, tên clip, viền cam ở clip đang chọn.
- **Alt + chú thích:** `![Cận cảnh ba thumbnail trên dải clip trang Color](../../assets/img/color-thumbnail-strip.png)` — *Vòng cầu vồng quanh số clip nghĩa là clip đã chỉnh.*

### COL-21 — `color-node-group-modes.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/node.md` — ngay sau heading `### Group — nhóm các clip cùng bối cảnh`
- **Trang Resolve:** Color
- **Chuẩn bị:**
  - Chọn 3 clip trại cừu → chuột phải → **Add Into New Group**, đặt tên "Trai cuu".
  - Bấm chấm **Pre-Clip** ở đầu Node Editor, thêm một node.
- **Khung chụp:** chỉ một vùng — phần trên Node Editor, thấy hàng chấm và vài node.
- **Cần thấy rõ trong ảnh:** bốn chấm Pre-Clip / Clip / Post-Clip / Timeline, tên chế độ đang chọn.
- **Alt + chú thích:** `![Node Editor với bốn chấm chế độ khi clip thuộc group](../../assets/img/color-node-group-modes.png)` — *Clip trong group có bốn tầng grade; chấm sáng là tầng đang sửa.*

### COL-22 — `color-palette-icons.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `## Hàng icon palette`
- **Trang Resolve:** Color
- **Chuẩn bị:** chọn node 04 Secondary (có Qualifier, Window) để chấm cam hiện trên icon. Màn hình ≥ 1920 px.
- **Khung chụp:** chỉ một vùng — hàng icon trên khu palette, toàn chiều ngang (cắt hai nửa ghép dọc nếu quá dài).
- **Cần thấy rõ trong ảnh:** 6 icon cụm trái, 10 icon cụm giữa, 3 icon Keyframes · Scopes · Info bên phải, chấm cam trên icon Qualifier/Window.
- **Alt + chú thích:** `![Hàng icon palette trang Color, hai cụm trái và giữa](../../assets/img/color-palette-icons.png)` — *Chấm cam nhỏ: node đang chọn có chỉnh ở palette đó.*

### COL-23 — `color-scope-histogram.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `## Histogram`
- **Trang Resolve:** Color
- **Chuẩn bị:** clip món ăn. Scope → **Histogram**.
- **Khung chụp:** chỉ một vùng — ô scope góc dưới phải.
- **Cần thấy rõ trong ảnh:** ba đường R, G, B chồng nhau, trục ngang 0–1023.
- **Alt + chú thích:** `![Scope Histogram của clip món ăn](../../assets/img/color-scope-histogram.png)` — *Trái là vùng tối, phải là vùng sáng; chiều cao là số điểm ảnh.*

### COL-24 — `color-tracker-tracked.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/curves-va-vung.md` — ngay sau heading `### Tracker`, sau ảnh palette Tracker
- **Trang Resolve:** Color
- **Chuẩn bị:** dùng window tròn ở COL-05. Mở Tracker, tick Pan, Tilt, Zoom, bấm **Track Forward** tới cuối clip.
- **Khung chụp:** chỉ một vùng — palette Tracker.
- **Cần thấy rõ trong ảnh:** đồ thị có đường cong nhiều màu (mỗi màu một chuyển động), playhead, ô tick đã chọn.
- **Alt + chú thích:** `![Palette Tracker sau khi track xong, đồ thị có đường cong](../../assets/img/color-tracker-tracked.png)` — *Đường cong mượt là bám tốt; gãy đột ngột là khung bị trượt.*

### COL-25 — `color-clip-filter-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `### Lọc clip — menu ▾ cạnh nút Clips`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm mũi tên **▾** cạnh nút **Clips** trên toolbar.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt nút + menu.
- **Cần thấy rõ trong ảnh:** All Clips, Ungraded Clips, Graded Clips, Flagged Clips, Marked Clips…
- **Alt + chú thích:** `![Menu lọc clip cạnh nút Clips](../../assets/img/color-clip-filter-menu.png)` — *Chọn Ungraded Clips để soát clip còn sót.*

### COL-26 — `color-keyframes.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `### Keyframes`
- **Trang Resolve:** Color
- **Chuẩn bị:** clip trại cừu, node 02. Mở **Keyframes**. Đặt 2 keyframe Dynamic (`⌘[`) cách nhau 2 giây, đổi Gain ở keyframe thứ hai. Chụp xong xoá keyframe.
- **Khung chụp:** chỉ một vùng — toàn bộ khung Keyframes.
- **Cần thấy rõ trong ảnh:** track từng node, hai keyframe hình thoi, nút Auto Keyframe và nút khoá ở đầu track.
- **Alt + chú thích:** `![Khung Keyframes với hai keyframe Dynamic trên track node 02](../../assets/img/color-keyframes.png)` — *Hình thoi là Dynamic (chuyển dần); hình tròn là Static.*

### COL-27 — `color-lightbox.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `## Lightbox`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm **Lightbox** trên toolbar, kéo thanh Zoom cho 6 clip vừa một màn hình.
- **Khung chụp:** toàn cửa sổ.
- **Cần thấy rõ trong ảnh:** lưới 6 clip, thanh Zoom góc trên phải, nút sidebar góc trên trái.
- **Alt + chú thích:** `![Lightbox: sáu clip của timeline dạng lưới](../../assets/img/color-lightbox.png)` — *Nhìn cả video một lúc để bắt clip lệch tông.*

### COL-28 — `color-osc-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/giao-dien.md` — ngay sau heading `### Menu onscreen control — góc dưới trái Viewer`
- **Trang Resolve:** Color
- **Chuẩn bị:** bấm menu onscreen control góc dưới trái Viewer.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt góc Viewer + menu.
- **Cần thấy rõ trong ảnh:** Off, Qualifier, Power Window, Image Wipe, Open FX Overlay, Color Chart, Annotations.
- **Alt + chú thích:** `![Menu onscreen control ở góc dưới trái Viewer](../../assets/img/color-osc-menu.png)` — *Chọn thứ được vẽ đè lên ảnh.*

### COL-29 — `color-generate-lut-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/lut-va-quan-ly-mau.md` — ngay sau heading `### Xuất grade thành LUT`
- **Trang Resolve:** Color
- **Chuẩn bị:** chuột phải thumbnail clip món ăn trên dải clip → rê tới **Generate LUT**.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt thumbnail + menu + submenu.
- **Cần thấy rõ trong ảnh:** bốn mục 17 / 33 / 65 Point Cube và Panasonic VLUT.
- **Alt + chú thích:** `![Submenu Generate LUT với bốn định dạng](../../assets/img/color-generate-lut-menu.png)` — *33 Point Cube là lựa chọn an toàn.*

### COL-30 — `color-node-parallel.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/node.md` — ngay sau heading `### Serial, Parallel, Layer khác nhau thế nào`, sau sơ đồ
- **Trang Resolve:** Color
- **Chuẩn bị:** chọn node 03, bấm `⌥P` hai lần để có ba nhánh song song vào **Parallel Mixer**. Chụp xong `⌘Z`.
- **Khung chụp:** chỉ một vùng — Node Editor.
- **Cần thấy rõ trong ảnh:** ba node song song, Parallel Mixer với ba ngõ vào, đường nối xanh lá.
- **Alt + chú thích:** `![Node Editor với ba node song song nối vào Parallel Mixer](../../assets/img/color-node-parallel.png)` — *Các nhánh cùng nhận một ảnh vào và được trộn đều.*

### COL-31 — `color-powergrade-album.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/node.md` — ngay sau heading `## PowerGrade — khung node dùng cho mọi project`
- **Trang Resolve:** Color
- **Chuẩn bị:** trong Gallery, cột album → chuột phải vùng PowerGrade → **Add PowerGrade Album**. Kéo still clip món ăn vào album mới.
- **Khung chụp:** chỉ một vùng — Gallery có cột album.
- **Cần thấy rõ trong ảnh:** nhóm **PowerGrade** trong cột album, album mới chứa một still.
- **Alt + chú thích:** `![Album PowerGrade trong Gallery chứa một still](../../assets/img/color-powergrade-album.png)` — *Still trong album PowerGrade dùng được ở mọi project.*

### COL-32 — `color-scope-cie.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/color/scopes.md` — ngay sau heading `## CIE Chromaticity`
- **Trang Resolve:** Color
- **Chuẩn bị:** clip trại cừu. Scope → **CIE Chromaticity**.
- **Khung chụp:** chỉ một vùng — ô scope góc dưới phải.
- **Cần thấy rõ trong ảnh:** hình móng ngựa CIE, tam giác gam màu, đám điểm ảnh bên trong.
- **Alt + chú thích:** `![Scope CIE Chromaticity với tam giác gam màu Rec.709](../../assets/img/color-scope-cie.png)` — *Điểm nằm ngoài tam giác là màu vượt gam màu giao hàng.*
