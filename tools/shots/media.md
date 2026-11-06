# Danh sách ảnh cần chụp — trang Media (`02-trang/media/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-media.png` (toàn cửa sổ, đã nhúng ở README). Các hình `assets/diagrams/media-*.svg` là sơ đồ vẽ, không phải ảnh chụp — các mục dưới đây bổ sung ảnh thật bên cạnh sơ đồ, không thay sơ đồ.

**Chuẩn bị chung:** mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps; V1 có 6 clip từ hai clip LOG 4K — đĩa phô mai/rau củ và cô gái ở trại cừu Kazakhstan; A1 "Giong noi", A2 "Nhac nen"). Media Pool có các bin 01 Footage, 02 Audio, 03 Nhac, 04 Do hoa, 05 Timelines. Sang trang **Media** bằng icon **Media** dưới đáy cửa sổ (Resolve 21 không dùng `⇧2` để đổi trang). Cửa sổ Resolve phóng toàn màn hình. Mặc định chọn bin `01 Footage`, kiểu xem **Thumbnail**. Sau mỗi ảnh có thay đổi project thì `⌘Z` hoàn tác về trạng thái gốc.

**Chuẩn bị thêm media** (chép vào một thư mục trên ổ, ví dụ `~/So tay DaVinci/Them/`):

- Một file `.wav` thu rời khớp một clip cô gái ở trại cừu (dùng cho MED-17). Có thể xuất tiếng của clip đó ra `.wav` bằng **Extract Audio** rồi đổi tên.
- Một thư mục giả làm thẻ nhớ, tên `A001`, có vài clip bên trong (dùng cho MED-15, MED-16).
- Một file video đã dựng sẵn có nhiều điểm cắt — render timeline "Demo - Vlog" ra một file `.mov` (dùng cho MED-18).
- Một thư mục `Footage` có hai thư mục con `Bep` và `Trang-trai` (dùng cho MED-03).

---

### MED-01 — `media-interface-toolbar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/giao-dien.md` — ngay sau heading `## Interface Toolbar — dải nút trên cùng`
- **Trang Resolve:** Media
- **Chuẩn bị:** bật đủ Media Storage, Audio Panel, Metadata; tắt Clone Tool và Inspector. Chuột phải lên dải toolbar → bật **Show Icon Labels** (nếu có) để chữ hiện dưới icon.
- **Khung chụp:** chỉ một vùng — dải Interface Toolbar trên cùng, từ nút đầu trái tới nút cuối phải.
- **Cần thấy rõ trong ảnh:** tám nút theo đúng thứ tự, nút đang bật được tô sáng, nhãn từng nút.
- **Alt + chú thích:** `![Tám nút Interface Toolbar trang Media](../../assets/img/media-interface-toolbar.png)` — *Mỗi nút bật/tắt một vùng; số trong bảng đếm từ trái sang.*

### MED-02 — `media-storage-volumes.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/media-storage.md` — ngay sau heading `## Volume List — cột ổ đĩa`
- **Trang Resolve:** Media
- **Chuẩn bị:** cắm một ổ ngoài (hoặc thẻ nhớ). Thêm thư mục `~/So tay DaVinci` vào Favorites (chuột phải → **Add Folder to Favorites**).
- **Khung chụp:** chỉ một vùng — cột ổ đĩa bên trái Media Storage, từ đầu danh sách tới hết Favorites.
- **Cần thấy rõ trong ảnh:** ba nhóm scratch volume, ổ đang gắn, Favorites có thư mục vừa thêm.
- **Alt + chú thích:** `![Cột ổ đĩa của Media Storage](../../assets/img/media-storage-volumes.png)` — *Ổ đang gắn ở giữa, thư mục hay dùng ghim ở Favorites.*

### MED-03 — `media-storage-right-click.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/media-storage.md` — ngay sau heading `### Chuột phải thư mục`
- **Trang Resolve:** Media
- **Chuẩn bị:** trên ổ có `~/davinci/So tay DaVinci/Footage/` với hai thư mục con `Bep`, `Trang-trai` (file là hard link của hai clip demo). Trong Media Storage mở tới `Footage`, chuột phải `Footage`.
- **Khung chụp:** cây thư mục từ `/Users/mac/davinci` tới hết menu. Che các thư mục khác của người dùng bên dưới bằng màu nền panel.
- **Cần thấy rõ trong ảnh:** **Refresh**, ba lệnh **Add Folder...**, **Add Folder to Favorites**, **Set as Clone Source**, **Add as Clone Destination**, **Delete Folder Permanently...**.
- **Alt + chú thích:** `![Menu chuột phải thư mục trong Media Storage](../../assets/img/media-storage-right-click.png)` — *Create Bins nạp cả thư mục con và dựng sẵn cây bin.*

### MED-04 — `media-viewer-options.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/giao-dien.md` — ngay sau heading `### Góc trên phải`
- **Trang Resolve:** Media
- **Chuẩn bị:** bấm một clip đĩa phô mai trong Media Pool cho hiện ở Viewer. Bấm menu **⋯** góc trên phải Viewer cho xổ.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng góc trên phải Viewer và cả menu.
- **Cần thấy rõ trong ảnh:** **Live Media Preview** có dấu tick, **Show Timecode Toolbar**, **Show Audio Waveforms in Source Clip**, **Previous Clip / Next Clip**.
- **Alt + chú thích:** `![Menu tuỳ chọn Viewer trang Media](../../assets/img/media-viewer-options.png)` — *Bật Show Timecode Toolbar để thấy độ dài đoạn In–Out.*

### MED-05 — `media-audio-panel-waveform.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/giao-dien.md` — ngay sau heading `## Audio Panel`
- **Trang Resolve:** Media
- **Chuẩn bị:** nạp file `.wav` thu rời vào bin `02 Audio`. Bấm nút **Waveform** trên đầu Audio Panel. Chọn clip cô gái ở trại cừu, rồi chọn file `.wav` cho dạng sóng hiện ra.
- **Khung chụp:** chỉ một vùng — Audio Panel bên phải Viewer, từ hai nút Meters/Waveform tới đáy panel.
- **Cần thấy rõ trong ảnh:** nút **Waveform** đang sáng, dạng sóng, nút **Link/Unlink Audio** góc dưới phải.
- **Alt + chú thích:** `![Audio Panel ở chế độ Waveform](../../assets/img/media-audio-panel-waveform.png)` — *Căn đỉnh sóng tiếng vỗ tay rồi bấm Link để khoá tiếng vào hình.*

### MED-06 — `media-pool-toolbar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/giao-dien.md` — ngay sau heading `### Phía trên, bên phải`
- **Trang Resolve:** Media
- **Chuẩn bị:** bin `01 Footage`, kiểu xem Thumbnail. Không bấm gì thêm.
- **Khung chụp:** chỉ một vùng — dải trên cùng của Media Pool, từ nút Bin List tới nút ⋯ ngoài cùng phải.
- **Cần thấy rõ trong ảnh:** nút Bin List, nút AI Clip Analysis và Transcribe (mờ ở bản free), menu kiểu xem (icon lưới ▾), kính lúp, Sort Order, nút ⋯.
- **Alt + chú thích:** `![Thanh công cụ phía trên Media Pool](../../assets/img/media-pool-toolbar.png)` — *Đổi kiểu xem, sắp xếp và tìm clip đều ở dải này.*

### MED-07 — `media-pool-options-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/bin.md` — ngay sau heading `## 2. Power Bin`
- **Trang Resolve:** Media
- **Chuẩn bị:** bấm nút **⋯** góc trên phải Media Pool cho xổ menu.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng gồm nút ⋯ và cả menu.
- **Cần thấy rõ trong ảnh:** **Show Power Bins**, **Show Smart Bins**, **Show Audio Waveforms**, **Remove Unused Clips**, **Update Usage for Entire Project**.
- **Alt + chú thích:** `![Menu tuỳ chọn Media Pool](../../assets/img/media-pool-options-menu.png)` — *Power Bin và Smart Bin mặc định ẩn, bật ở đây.*

### MED-08 — `media-bin-list-three-areas.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/bin.md` — ngay sau heading `## 1. Bin thường`
- **Trang Resolve:** Media
- **Chuẩn bị:** bật **Show Power Bins** và **Show Smart Bins**. Tạo một Power Bin tên `Logo` và một Smart Bin tên `Trai cuu` (Keywords contains `trai cuu`). Mở nhóm Smart Bin tự tạo **Timelines** bằng tam giác.
- **Khung chụp:** chỉ một vùng — cột Bin List bên trái Media Pool, từ Master tới hết khu Smart Bins.
- **Cần thấy rõ trong ảnh:** cây bin 01 Footage…05 Timelines dưới Master, khu Power Bins có `Logo`, khu Smart Bins có `Trai cuu` và nhóm Timelines.
- **Alt + chú thích:** `![Ba khu bin trong Bin List](../../assets/img/media-bin-list-three-areas.png)` — *Bin thường, Power Bin và Smart Bin nằm ở ba khu riêng.*

### MED-09 — `media-bin-right-click.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/giao-dien.md` — ngay sau heading `## Menu chuột phải — nơi chứa phần lớn lệnh`
- **Trang Resolve:** Media
- **Chuẩn bị:** chuột phải bin `01 Footage` cho xổ menu.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng gồm bin và cả menu.
- **Cần thấy rõ trong ảnh:** **Add Bin**, **Rename Bin**, **Color Tag**, **Open as New Tab**, **Export Bin**, **Auto Sync Audio**.
- **Alt + chú thích:** `![Menu chuột phải của bin](../../assets/img/media-bin-right-click.png)` — *Auto Sync Audio và Export Bin đều chạy trên cả bin.*

### MED-10 — `media-create-smart-bin.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/bin.md` — ngay sau heading `### Hộp thoại tạo Smart Bin`
- **Trang Resolve:** hộp thoại Create Smart Bin
- **Chuẩn bị:** chuột phải vùng trống khu Smart Bins → **Add Smart Bin...**. Tên `B-roll 4K`, Match **All**, dòng 1: MediaPool Properties → File Name → contains → `Artlist`. Bấm **+** thêm dòng 2: MediaPool Properties → Resolution → is → `3840` X `2160`.
- **Khung chụp:** đúng hộp thoại (tìm vị trí bằng System Events).
- **Cần thấy rõ trong ảnh:** ô **Name**, **Show in all projects**, **Match All**, hai dòng điều kiện với ba menu và ô giá trị, nút **−** **+**, nút **Create**.
- **Alt + chú thích:** `![Hộp thoại Create Smart Bin](../../assets/img/media-create-smart-bin.png)` — *Hai điều kiện ghép bằng Match All: tên file có "Artlist" và đúng 3840 × 2160.*

### MED-11 — `media-pool-list-view.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/media-pool.md` — ngay sau heading `### List view`
- **Trang Resolve:** Media
- **Chuẩn bị:** bin `01 Footage`, bấm nút **List**. Chuột phải tiêu đề cột → bật cột **Usage**. Bấm menu ⋯ → **Update Usage for Entire Project**. Bấm tiêu đề **Usage** để sắp xếp.
- **Khung chụp:** chỉ một vùng — vùng clip của Media Pool ở List view, đủ thấy các cột Clip Name, Duration, FPS, Usage.
- **Cần thấy rõ trong ảnh:** các cột, cột Usage có số (có clip số 0), mũi tên sắp xếp trên tiêu đề Usage.
- **Alt + chú thích:** `![Media Pool ở List view, sắp theo Usage](../../assets/img/media-pool-list-view.png)` — *Usage bằng 0 là clip chưa dùng trên timeline nào.*

### MED-12 — `media-pool-metadata-view.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/media/media-pool.md` — ngay sau heading `### Metadata view`
- **Trang Resolve:** Media
- **Chuẩn bị:** bin `01 Footage`, bấm nút **Metadata**. Gõ sẵn Scene/Shot/Take cho vài clip.
- **Khung chụp:** chỉ một vùng — vùng clip của Media Pool, đủ thấy 3–4 thẻ clip.
- **Cần thấy rõ trong ảnh:** thumbnail kèm các dòng metadata bên cạnh mỗi clip.
- **Alt + chú thích:** `![Media Pool ở Metadata view](../../assets/img/media-pool-metadata-view.png)` — *Mỗi clip hiện kèm thông tin để duyệt nhanh như thẻ.*

### MED-13 — `media-pool-clip-right-click.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/media-pool.md` — ngay sau heading `## Menu chuột phải của clip`
- **Trang Resolve:** Media
- **Chuẩn bị:** chọn một clip đĩa phô mai, chuột phải cho xổ menu.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng gồm clip và cả menu (menu dài, cắt đủ từ đầu tới cuối).
- **Cần thấy rõ trong ảnh:** **Clip Attributes**, **Generate Optimized Media**, **Generate Proxy Media**, **Relink Selected Clips**, **Create New Timeline Using Selected Clips…**, **Reveal in Finder**, mục **AI Tools**.
- **Alt + chú thích:** `![Menu chuột phải của clip trong Media Pool](../../assets/img/media-pool-clip-right-click.png)` — *Phần lớn lệnh với clip nằm ở menu này.*

### MED-14 — `media-frame-rate-dialog.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `## Hộp thoại đổi frame rate`
- **Trang Resolve:** hộp thoại thay đổi frame rate khi nạp
- **Chuẩn bị:** tạo một project trống mới (đừng dùng project demo). Kéo một clip 4K đầu tiên từ Media Storage vào Media Pool cho hộp thoại hiện ra. Chụp xong bấm **Don't Change** và đóng project trống không lưu.
- **Khung chụp:** hộp thoại — cần chụp toàn màn hình rồi cắt đúng hộp thoại.
- **Cần thấy rõ trong ảnh:** câu hỏi về frame rate, hai nút **Change** và **Don't Change**.
- **Alt + chú thích:** `![Hộp thoại hỏi đổi frame rate khi nạp clip đầu tiên](../../assets/img/media-frame-rate-dialog.png)` — *Chọn Change nếu muốn timeline theo fps của clip; sau khi nạp xong thì khó đổi.*

### MED-15 — `media-clone-tool-job.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/clone-tool.md` — ngay sau heading `## Các nút của panel Clone Tool`
- **Trang Resolve:** Media
- **Chuẩn bị:** bấm nút **Clone Tool** trên Interface Toolbar. Bấm **Add Job**. Chuột phải thư mục `A001` → **Set as Clone Source**; chuột phải hai thư mục đích → **Add as Clone Destination**. Không bấm **Clone**.
- **Khung chụp:** chỉ một vùng — panel Clone Tool, đủ thấy job, nút **Add Job** và nút **Clone**.
- **Cần thấy rõ trong ảnh:** ô source có `A001`, hai đích, **Add Job** góc dưới trái, nút **Clone**.
- **Alt + chú thích:** `![Một job Clone Tool với một nguồn và hai đích](../../assets/img/media-clone-tool-job.png)` — *Một job copy ra nhiều ổ, mỗi ổ được kiểm tra riêng.*

### MED-16 — `media-clone-checksum-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/clone-tool.md` — ngay sau heading `### Chọn kiểu checksum`
- **Trang Resolve:** Media
- **Chuẩn bị:** như MED-15. Bấm **⋯** góc trên phải panel Clone Tool → **Checksum Type** cho xổ menu con.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng gồm menu tuỳ chọn và menu con.
- **Cần thấy rõ trong ảnh:** **Preserve Folder Name**, bảy kiểu checksum, dấu tick ở **MD5**.
- **Alt + chú thích:** `![Menu Checksum của Clone Tool](../../assets/img/media-clone-checksum-menu.png)` — *MD5 là mặc định; XXHASH 64 nhanh nhất mà vẫn kiểm tra tốt.*

### MED-17 — `media-auto-sync-audio.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `### Tự động — Auto Sync Audio`
- **Trang Resolve:** hộp thoại Automatically Sync Audio
- **Chuẩn bị:** tạm chuyển `giong-noi.wav` vào bin `01 Footage`. Chuột phải bin → **Auto Sync Audio...**. Chụp menu **Synchronize Using** đang mở, rồi chọn **Waveform**, tick **Retain embedded audio**, chụp lần hai. Ghép hai ảnh cạnh nhau. Bấm Cancel, trả file wav về `02 Audio`.
- **Khung chụp:** đúng hộp thoại (tìm vị trí bằng System Events).
- **Cần thấy rõ trong ảnh:** **Synchronize Using** = Waveform, **Use channel number**, **Retain embedded audio** đã tick, **Retain video metadata**, nút **Sync**; bên phải là danh sách Waveform / Timecode / In / Out / Marker.
- **Alt + chú thích:** `![Hộp thoại Automatically Sync Audio và menu Synchronize Using](../../assets/img/media-auto-sync-audio.png)` — *Waveform hợp nhất khi máy quay có thu tiếng mic trên máy. Mặc định là Timecode.*

### MED-18 — `media-scene-detect.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `## Cắt video đã dựng thành từng cảnh`
- **Trang Resolve:** cửa sổ Scene Cut Detection
- **Chuẩn bị:** trong Media Storage, chuột phải file `.mov` đã render từ "Demo - Vlog" → **Scene Cut Detection** → bấm **Auto Scene Detect**, chờ xong.
- **Khung chụp:** toàn cửa sổ Scene Cut Detection — cần chụp toàn màn hình rồi cắt đúng cửa sổ.
- **Cần thấy rõ trong ảnh:** ba viewer PiP phía trên, Scene Detect Graph có vạch điểm cắt, thanh ngang màu hồng (magenta), Cut List, nút **Add Cuts to Media Pool**.
- **Alt + chú thích:** `![Cửa sổ Scene Cut Detection](../../assets/img/media-scene-detect.png)` — *Kéo thanh hồng lên để bỏ các điểm cắt ít chắc chắn.*

### MED-19 — `media-optimized-proxy-settings.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `### Optimized Media`
- **Trang Resolve:** hộp thoại Project Settings
- **Chuẩn bị:** mở **Project Settings** (bánh răng góc dưới phải) → **Master Settings** → cuộn tới **Optimized Media and Render Cache**.
- **Khung chụp:** chỉ một vùng — mục Optimized Media and Render Cache trong Project Settings, từ tiêu đề tới hết **Render Cache Format**.
- **Cần thấy rõ trong ảnh:** **Proxy media resolution**, **Proxy media format**, **Optimized media resolution**, **Optimized media format**, **Render Cache Format**.
- **Alt + chú thích:** `![Cài đặt proxy, optimized media và render cache trong Project Settings](../../assets/img/media-optimized-proxy-settings.png)` — *Ba thứ cùng nằm trong một mục của Master Settings.*

### MED-20 — `media-proxy-handling-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `### Proxy Media`
- **Trang Resolve:** Media (menu Playback)
- **Chuẩn bị:** tạo proxy cho một clip cô gái (chuột phải → **Generate Proxy Media**). Mở menu **Playback** → rê tới **Proxy Handling** cho xổ menu con.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng menu Playback và menu con.
- **Cần thấy rõ trong ảnh:** **Disable All Proxies**, **Prefer Proxies**, **Prefer Camera Originals**, và **Use Optimized Media If Available**, **Render Cache** trong cùng menu Playback.
- **Alt + chú thích:** `![Menu Playback → Proxy Handling](../../assets/img/media-proxy-handling-menu.png)` — *Proxy Handling áp cho cả project, không theo từng clip.*

### MED-21 — `media-relink-change-source.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/nap-media.md` — ngay sau heading `## Media offline — khi clip hiện đỏ`
- **Trang Resolve:** hộp thoại Change Source Folder
- **Chuẩn bị:** đổi tên tạm thư mục chứa footage demo trong Finder cho clip hiện đỏ. Chọn mọi clip `01 Footage` → chuột phải → **Change Source Folder**. Chụp xong đổi tên thư mục lại như cũ.
- **Khung chụp:** hộp thoại — cần chụp toàn màn hình rồi cắt vùng gồm vài thumbnail đỏ phía sau và hộp thoại.
- **Cần thấy rõ trong ảnh:** thumbnail clip offline màu đỏ, đường dẫn cũ, nút **Browse** và **Change**.
- **Alt + chú thích:** `![Clip offline và hộp thoại Change Source Folder](../../assets/img/media-relink-change-source.png)` — *Trỏ sang thư mục mới, mọi clip nối lại cùng lúc.*

### MED-22 — `media-clip-attributes-video.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/clip-attributes.md` — ngay sau heading `## Tab Video`
- **Trang Resolve:** hộp thoại Clip Attributes
- **Chuẩn bị:** chọn một clip cô gái → chuột phải → **Clip Attributes** → tab **Video**. Không đổi gì.
- **Khung chụp:** hộp thoại — cần chụp toàn màn hình rồi cắt đúng hộp thoại.
- **Cần thấy rõ trong ảnh:** dãy tab Video/Audio/Timecode/Name, **Video Frame Rate**, **Data Levels**, **Pixel Aspect Ratio**, **Image Orientation**, **Field Dominance**, **Super Scale** (mờ ở bản free).
- **Alt + chú thích:** `![Tab Video của Clip Attributes](../../assets/img/media-clip-attributes-video.png)` — *Sửa cách Resolve hiểu clip, file trên ổ không đổi.*

### MED-23 — `media-clip-attributes-audio.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/media/clip-attributes.md` — ngay sau heading `### Danh sách track bên dưới`
- **Trang Resolve:** hộp thoại Clip Attributes
- **Chuẩn bị:** mở Clip Attributes của `nhac-nen.wav` (bin 03 Nhac, clip có tiếng stereo) → tab **Audio**. Ở hàng trên chọn **Format** = Mono, **Tracks** = 1 → **Add**. Chụp xong bấm Cancel.
- **Khung chụp:** hộp thoại — cần chụp toàn màn hình rồi cắt đúng hộp thoại.
- **Cần thấy rõ trong ảnh:** hàng **Format / Tracks / Add**, track Stereo gốc và track Mono mới, cột **Source Channel**, icon thùng rác.
- **Alt + chú thích:** `![Tab Audio của Clip Attributes](../../assets/img/media-clip-attributes-audio.png)` — *Thêm track Mono rồi xoá track Stereo để giọng ra đều hai tai.*

### MED-24 — `media-clip-attributes-name.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/media/clip-attributes.md` — ngay sau heading `## Tab Name`
- **Trang Resolve:** hộp thoại Clip Attributes
- **Chuẩn bị:** gõ Scene/Shot/Take cho ba clip. Chọn ba clip → **Clip Attributes** → tab **Name**. Trong ô **Clip Name** gõ `%`, chèn biến Scene, `_`, Shot, `_`, Take. Gõ `%` lần nữa cho danh sách biến hiện ra.
- **Khung chụp:** hộp thoại — cần chụp toàn màn hình rồi cắt đúng hộp thoại.
- **Cần thấy rõ trong ảnh:** ô Clip Name có các biến dạng ô có nền, danh sách biến đang xổ.
- **Alt + chú thích:** `![Đặt tên clip bằng biến metadata](../../assets/img/media-clip-attributes-name.png)` — *Gõ % để chèn biến; clip trống trường nào thì biến đó trống.*

### MED-25 — `media-metadata-shot-scene.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/media/metadata.md` — ngay sau heading `## Những trường đáng gõ`
- **Trang Resolve:** Media
- **Chuẩn bị:** chọn một clip cô gái. Ở Metadata Editor, menu nhóm bên phải → **Shot & Scene**. Gõ Scene `2`, Shot `A`, Take `1`, Keywords `trai cuu`, `cuu`, cho 4 sao, tick **Good Take**.
- **Khung chụp:** chỉ một vùng — panel Metadata Editor, từ header tới hết trường Keywords.
- **Cần thấy rõ trong ảnh:** hai menu đầu panel, các trường Scene/Shot/Take, sao, Good Take, keyword dạng thẻ.
- **Alt + chú thích:** `![Nhóm Shot & Scene của Metadata Editor](../../assets/img/media-metadata-shot-scene.png)` — *Keyword dạng thẻ là thứ Smart Bin lọc nhiều nhất.*

### MED-26 — `media-inspector-file-tab.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/media/metadata.md` — ngay sau heading `### Nhập liệu nhanh bằng Inspector — tab File`
- **Trang Resolve:** Media
- **Chuẩn bị:** bật nút **Inspector** trên Interface Toolbar. Chọn một clip cô gái → tab **File**. Tick **Auto Select Next Unsorted Clip**.
- **Khung chụp:** chỉ một vùng — panel Inspector, từ dãy tab tới hết phần **Audio Configuration**.
- **Cần thấy rõ trong ảnh:** tab **File** đang chọn, các ô Scene/Shot/Take, ô tick **Auto Select Next Unsorted Clip**, nút **Next Clip**, Audio Configuration với nút Mute từng track.
- **Alt + chú thích:** `![Tab File của Inspector trang Media](../../assets/img/media-inspector-file-tab.png)` — *Gõ xong bấm Return là nhảy sang clip kế.*

### MED-27 — `media-pool-tabs.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/media/media-pool.md` — ngay sau heading `## Media Pool Tabs`
- **Trang Resolve:** Media
- **Chuẩn bị:** chuột phải bin `01 Footage` → **Open as New Tab**. Làm tương tự với `03 Nhac`. Chọn tab `01 Footage`.
- **Khung chụp:** chỉ một vùng — phần trên Media Pool, đủ thấy dải tab và vài thumbnail bên dưới.
- **Cần thấy rõ trong ảnh:** hai tab `01 Footage` và `03 Nhac`, tab đang chọn được tô sáng.
- **Alt + chú thích:** `![Dải tab Media Pool](../../assets/img/media-pool-tabs.png)` — *Mỗi tab là lối tắt tới một bin, bấm là chuyển ngay.*
