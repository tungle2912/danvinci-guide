# Danh sách ảnh cần chụp — Bắt đầu (`01-bat-dau/`) và Tra cứu (`04-tham-khao/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-cut.png` (đã nhúng ở `01-bat-dau/giao-dien.md`, mục Dãy icon đổi trang). Các ảnh `page-*.png` còn lại đã nhúng ở README từng trang, không cần nhúng lại ở đây. Các hình `assets/diagrams/start-*.svg`, `ref-*.svg` và `pages.svg` là sơ đồ vẽ. Các mục dưới đây là ảnh chụp thật để đặt cạnh sơ đồ, không thay sơ đồ. Ảnh cho phần Bắt đầu dùng tiền tố `start-`. Ảnh cho phần Tra cứu dùng `ref-`, cùng tiền tố với sơ đồ của khu này.

**Chuẩn bị chung:** mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps; V1 có 6 clip từ hai clip LOG 4K; A1 "Giong noi", A2 "Nhac nen"). Cửa sổ Resolve phóng toàn màn hình. Hầu hết mục ở đây là hộp thoại hoặc menu xổ: chụp toàn màn hình rồi cắt. Không đổi giá trị nào trong Preferences hay Project Settings khi chụp. Chỉ mở ra, chụp, rồi bấm **Cancel**.

---

### STA-01 — `start-project-manager.png`
- **Ưu tiên:** P1
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 1 — Tạo project trong Project Manager`
- **Trang Resolve:** cửa sổ Project Manager
- **Chuẩn bị:** bấm `⇧1` hoặc icon nhà ở góc dưới phải để mở Project Manager. Bật sidebar **Project Libraries** (icon bên trái thanh tiêu đề) để thấy project library "Local Database". Xem dạng lưới (thumbnail). Project "So tay DaVinci - Demo" đang mở, nằm trong lưới.
- **Khung chụp:** toàn cửa sổ Project Manager (là cửa sổ riêng — chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** sidebar Project Libraries, thumbnail project demo, nút **New Project**, **Import**, ô tìm kiếm.
- **Alt + chú thích:** `![Project Manager với sidebar Project Libraries và project demo](../assets/img/start-project-manager.png)` — *Project Manager: mỗi thumbnail là một project. Bên trái là các project library.*

### STA-02 — `start-new-project-dialog.png`
- **Ưu tiên:** P2
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 1 — Tạo project trong Project Manager`
- **Trang Resolve:** hộp thoại Create New Project
- **Chuẩn bị:** trong Project Manager bấm **New Project**. Gõ tên "Thu nghiem" vào ô tên nhưng **không** bấm Create.
- **Khung chụp:** chỉ hộp thoại (chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** ô tên project, nút **Create**, **Cancel**.
- **Alt + chú thích:** `![Hộp thoại tạo project mới](../assets/img/start-new-project-dialog.png)` — *Đặt tên rồi bấm Create. Mọi thiết lập khác chỉnh sau trong Project Settings.*

### STA-03 — `start-project-context-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Sau khi tạo xong`
- **Trang Resolve:** Project Manager, menu chuột phải
- **Chuẩn bị:** chuột phải thumbnail project demo.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt, giữ một phần thumbnail bên cạnh.
- **Cần thấy rõ trong ảnh:** **Export Project**, **Export Project Archive** (hoặc **Archive**, tuỳ nhãn thật của bản 21), **Project Backups**, **Delete**, **Rename**.
- **Alt + chú thích:** `![Menu chuột phải của một project](../assets/img/start-project-context-menu.png)` — *Chuột phải project để xuất, nén kèm media, mở bản sao lưu hoặc xoá.*

### STA-04 — `start-project-settings-timeline-format.png`
- **Ưu tiên:** P1
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 2 — Frame rate, thứ không sửa được về sau`
- **Trang Resolve:** hộp thoại Project Settings → Master Settings
- **Chuẩn bị:** bấm `⇧9` (hoặc bánh răng góc dưới phải). Chọn **Master Settings**, cuộn lên đầu, tới mục **Timeline Format**.
- **Khung chụp:** chỉ hộp thoại Project Settings, từ danh sách mục bên trái tới hết khối Timeline Format.
- **Cần thấy rõ trong ảnh:** **Timeline resolution** 3840×2160 (hoặc giá trị của demo), **Timeline frame rate** 25, **Playback frame rate**, ô **Use vertical resolution**.
- **Alt + chú thích:** `![Project Settings, mục Timeline Format](../assets/img/start-project-settings-timeline-format.png)` — *Timeline frame rate bị khoá ngay khi timeline đầu tiên có clip. Hãy đặt trước khi dựng.*

### STA-05 — `start-project-settings-image-scaling.png`
- **Ưu tiên:** P3
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 3 — Độ phân giải`
- **Trang Resolve:** hộp thoại Project Settings → Image Scaling
- **Chuẩn bị:** `⇧9` → chọn **Image Scaling** ở cột trái.
- **Khung chụp:** chỉ phần bên phải của hộp thoại, khối **Input Scaling**.
- **Cần thấy rõ trong ảnh:** dropdown **Mismatched resolution files** với giá trị đang chọn.
- **Alt + chú thích:** `![Image Scaling, mục Mismatched resolution files](../assets/img/start-project-settings-image-scaling.png)` — *Quyết định clip khác khung hình được co, phóng hay cắt khi đặt vào timeline.*

### STA-06 — `start-project-settings-color-management.png`
- **Ưu tiên:** P1
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 4 — Chọn cách quản lý màu`
- **Trang Resolve:** hộp thoại Project Settings → Color Management
- **Chuẩn bị:** `⇧9` → **Color Management**. Giữ nguyên thiết lập của demo.
- **Khung chụp:** chỉ phần bên phải, khối **Color Space & Transforms**.
- **Cần thấy rõ trong ảnh:** dropdown **Color science**, **Timeline color space**, **Output color space**, đúng nhãn của bản 21.
- **Alt + chú thích:** `![Project Settings, mục Color Management](../assets/img/start-project-settings-color-management.png)` — *Color science quyết định Resolve tự quản lý màu hay để bạn tự làm bằng node.*

### STA-07 — `start-project-settings-working-folders.png`
- **Ưu tiên:** P2
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 5 — Nơi lưu cache và file tạo ra`
- **Trang Resolve:** hộp thoại Project Settings → Master Settings
- **Chuẩn bị:** `⇧9` → **Master Settings**, cuộn xuống mục **Working Folders**.
- **Khung chụp:** chỉ khối Working Folders.
- **Cần thấy rõ trong ảnh:** **Proxy generation location**, **Cache files location**, **Gallery stills location** và đường dẫn đang đặt.
- **Alt + chú thích:** `![Working Folders trong Project Settings](../assets/img/start-project-settings-working-folders.png)` — *Ba thư mục chứa file Resolve tự tạo ra. Nên trỏ cache vào SSD nhanh.*

### STA-08 — `start-preferences-project-save-load.png`
- **Ưu tiên:** P1
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 6 — Tự động lưu và bản sao lưu`
- **Trang Resolve:** hộp thoại Preferences → User → Project Save and Load
- **Chuẩn bị:** **DaVinci Resolve → Preferences** (`⌘,`) → tab **User** → **Project Save and Load**. Không đổi gì.
- **Khung chụp:** chỉ phần bên phải của hộp thoại, từ **Load Settings** tới hết **Save Settings**.
- **Cần thấy rõ trong ảnh:** ô **Live save**, **Project backups**, các ô **Perform backups every … minutes**, **Hourly backups for … hours**, **Daily backups for … days**, **Project backup location**. Ảnh này dùng để chốt số mặc định thật (10/2/2 hay 10/8/5), nên chụp trên máy chưa từng đổi các ô này.
- **Alt + chú thích:** `![Preferences, mục Project Save and Load](../assets/img/start-preferences-project-save-load.png)` — *Live Save và ba ô sao lưu định kỳ. Ba ô này dùng chung cho cả Project Backups lẫn Timeline Backups.*

### STA-09 — `start-project-backups-dialog.png`
- **Ưu tiên:** P2
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 6 — Tự động lưu và bản sao lưu`
- **Trang Resolve:** hộp thoại Project Backups
- **Chuẩn bị:** cần có ít nhất một bản backup: bật **Project backups** (STA-08), làm việc trên demo hơn 10 phút. Rồi ở Project Manager chuột phải project demo → **Project Backups**.
- **Khung chụp:** chỉ hộp thoại.
- **Cần thấy rõ trong ảnh:** danh sách bản backup có ngày giờ, nút **Load**.
- **Alt + chú thích:** `![Hộp thoại Project Backups](../assets/img/start-project-backups-dialog.png)` — *Chọn một mốc giờ rồi bấm Load để mở lại bản sao lưu.*

### STA-10 — `start-menu-switch-to-page.png`
- **Ưu tiên:** P1
- **Chèn vào:** `01-bat-dau/giao-dien.md` — ngay sau heading `## Phím tắt đổi trang`
- **Trang Resolve:** Edit, menu Workspace
- **Chuẩn bị:** ở trang Edit, mở **Workspace → Switch to Page**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt, gồm menu Workspace và submenu Switch to Page.
- **Cần thấy rõ trong ảnh:** tên tám trang và phím tắt in bên phải từng dòng, nếu có. Ảnh này dùng để chốt phím đổi trang thật của bản 21.
- **Alt + chú thích:** `![Menu Workspace → Switch to Page](../assets/img/start-menu-switch-to-page.png)` — *Menu Switch to Page liệt kê các trang kèm phím tắt mà bản đang chạy thực sự dùng.*

### STA-11 — `start-page-bar-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `01-bat-dau/giao-dien.md` — ngay sau heading `## Ẩn bớt trang không dùng`
- **Trang Resolve:** bất kỳ trang nào, dãy icon trang dưới đáy
- **Chuẩn bị:** chuột phải vào khoảng trống trên dãy icon trang dưới đáy cửa sổ. Nếu không có menu, dùng **Workspace → Show Page**.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt, giữ một đoạn dãy icon bên dưới.
- **Cần thấy rõ trong ảnh:** **Show Icons and Labels** / **Show Icons Only**, danh sách trang có dấu tick.
- **Alt + chú thích:** `![Menu ẩn hiện trang](../assets/img/start-page-bar-menu.png)` — *Bỏ tick trang không dùng để dãy icon gọn hơn.*

### STA-12 — `start-preferences-media-storage.png`
- **Ưu tiên:** P3
- **Chèn vào:** `01-bat-dau/tao-du-an.md` — ngay sau heading `## Bước 5 — Nơi lưu cache và file tạo ra`
- **Trang Resolve:** Preferences → System → Media Storage
- **Chuẩn bị:** `⌘,` → tab **System** → **Media Storage**.
- **Khung chụp:** chỉ phần bên phải.
- **Cần thấy rõ trong ảnh:** danh sách **Media Storage Locations**, ổ đứng đầu (ổ cache mặc định).
- **Alt + chú thích:** `![Preferences, mục Media Storage](../assets/img/start-preferences-media-storage.png)` — *Ổ đứng đầu danh sách là nơi Resolve lưu cache cho project mới.*

---

### REF-01 — `ref-keyboard-customization.png`
- **Ưu tiên:** P1
- **Chèn vào:** `04-tham-khao/phim-tat.md` — ngay sau heading `## Toàn cục`
- **Trang Resolve:** cửa sổ Keyboard Customization
- **Chuẩn bị:** **DaVinci Resolve → Keyboard Customization**. Gõ "Switch to" vào ô tìm kiếm bên phải để lọc các lệnh đổi trang. Không đổi phím nào.
- **Khung chụp:** toàn cửa sổ Keyboard Customization (cửa sổ riêng — chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** bàn phím ảo, dropdown preset (**DaVinci Resolve**), ô tìm kiếm, danh sách lệnh kèm phím. Ghi lại phím tắt của menu Keyboard Customization để chốt.
- **Alt + chú thích:** `![Cửa sổ Keyboard Customization lọc lệnh đổi trang](../assets/img/ref-keyboard-customization.png)` — *Tìm lệnh theo tên để xem hoặc gán phím. Phím đã gán hiện màu trên bàn phím ảo.*

### REF-02 — `ref-menu-timeline-proxy-resolution.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Bước 1 — Hạ độ phân giải khi xem (miễn phí, tức thì)`
- **Trang Resolve:** Edit, menu Playback
- **Chuẩn bị:** ở trang Edit, mở **Playback → Timeline Proxy Resolution**.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt, gồm menu Playback và submenu.
- **Cần thấy rõ trong ảnh:** **None**, **Half**, **Quarter** và dấu tick ở giá trị hiện tại.
- **Alt + chú thích:** `![Menu Playback → Timeline Proxy Resolution](../assets/img/ref-menu-timeline-proxy-resolution.png)` — *Half hoặc Quarter làm Viewer nhẹ ngay, không tạo file nào.*

### REF-03 — `ref-render-cache-bar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Bước 2 — Render Cache`
- **Trang Resolve:** Edit
- **Chuẩn bị:** bật **Playback → Render Cache → Smart**. Thêm tạm một ResolveFX nặng (ví dụ Gaussian Blur) vào clip 2 để có đoạn cần cache. Chụp lúc vạch còn **đỏ**, đợi vài phút rồi chụp lại lúc vạch thành **xanh lam**. Xong thì `⌘Z` gỡ hiệu ứng và đặt Render Cache về như cũ.
- **Khung chụp:** chỉ vùng thước timeline và hai clip đầu của V1. Ghép hai ảnh đỏ và xanh cạnh nhau nếu được.
- **Cần thấy rõ trong ảnh:** vạch mỏng ở mép dưới thước timeline, màu đỏ và xanh lam.
- **Alt + chú thích:** `![Vạch render cache đỏ rồi xanh trên thước timeline](../assets/img/ref-render-cache-bar.png)` — *Đỏ là đoạn đang chờ cache, xanh lam là đã cache xong và sẽ phát mượt.*

### REF-04 — `ref-project-settings-optimized-cache.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Bước 4 — Optimized Media`
- **Trang Resolve:** Project Settings → Master Settings
- **Chuẩn bị:** `⇧9` → **Master Settings**, cuộn tới khối **Optimized Media and Render Cache**.
- **Khung chụp:** chỉ khối đó.
- **Cần thấy rõ trong ảnh:** **Proxy media resolution**, **Proxy media format**, **Optimized media resolution**, **Optimized media format**, **Render cache format**, ô **Enable background caching after … seconds**.
- **Alt + chú thích:** `![Khối Optimized Media and Render Cache](../assets/img/ref-project-settings-optimized-cache.png)` — *Một khối cài đặt cho cả ba loại file nhẹ: proxy, optimized media và render cache.*

### REF-05 — `ref-menu-generate-optimized-proxy.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Bước 5 — Proxy Media`
- **Trang Resolve:** Media hoặc Edit, Media Pool
- **Chuẩn bị:** chọn hai clip gốc trong Media Pool, chuột phải.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt.
- **Cần thấy rõ trong ảnh:** hai dòng **Generate Optimized Media** và **Generate Proxy Media** gần nhau.
- **Alt + chú thích:** `![Menu chuột phải clip với Generate Optimized Media và Generate Proxy Media](../assets/img/ref-menu-generate-optimized-proxy.png)` — *Hai lệnh tạo bản nhẹ nằm cạnh nhau trong menu chuột phải của Media Pool.*

### REF-06 — `ref-menu-proxy-handling.png`
- **Ưu tiên:** P3
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Bước 5 — Proxy Media`
- **Trang Resolve:** Edit, menu Playback
- **Chuẩn bị:** **Playback → Proxy Handling**.
- **Khung chụp:** menu xổ — chụp toàn màn hình rồi cắt.
- **Cần thấy rõ trong ảnh:** **Prefer Proxies**, **Prefer Camera Originals**, **Disable All Proxies**, dấu tick.
- **Alt + chú thích:** `![Menu Playback → Proxy Handling](../assets/img/ref-menu-proxy-handling.png)` — *Prefer Proxies phát bằng proxy, clip nào chưa có proxy thì dùng file gốc.*

### REF-07 — `ref-preferences-memory-gpu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Thiết lập khác đáng chỉnh`
- **Trang Resolve:** Preferences → System → Memory and GPU
- **Chuẩn bị:** `⌘,` → **System** → **Memory and GPU**. Không đổi gì.
- **Khung chụp:** chỉ phần bên phải.
- **Cần thấy rõ trong ảnh:** **Limit Resolve memory usage to**, **Fusion memory cache**, **GPU processing mode** (Metal/Auto).
- **Alt + chú thích:** `![Preferences, mục Memory and GPU](../assets/img/ref-preferences-memory-gpu.png)` — *Giới hạn RAM và chế độ GPU. Trên Mac để Auto hoặc Metal.*

### REF-08 — `ref-preferences-decode-options.png`
- **Ưu tiên:** P3
- **Chèn vào:** `04-tham-khao/hieu-nang.md` — ngay sau heading `## Vấn đề gốc — codec của footage`
- **Trang Resolve:** Preferences → System → Decode Options
- **Chuẩn bị:** `⌘,` → **System** → **Decode Options**.
- **Khung chụp:** chỉ phần bên phải.
- **Cần thấy rõ trong ảnh:** các ô **Use hardware acceleration** cho H.264/HEVC, ghi chú nếu ô nào bị mờ ở bản free.
- **Alt + chú thích:** `![Preferences, mục Decode Options](../assets/img/ref-preferences-decode-options.png)` — *Bật giải mã phần cứng giúp H.264, H.265 từ điện thoại phát nhẹ hơn.*

### REF-09 — `ref-relink-media.png`
- **Ưu tiên:** P1
- **Chèn vào:** `04-tham-khao/loi-thuong-gap.md` — ngay sau heading `## Clip hiện màu đỏ "Media Offline"`
- **Trang Resolve:** Media
- **Chuẩn bị:** làm một bản sao của project demo (Project Manager → chuột phải → Duplicate), mở bản sao. Trong Finder đổi tạm tên thư mục chứa footage demo để clip thành offline. Ở trang Media, Media Pool hiện clip đỏ và icon **Relink Media** màu cam trên thanh Media Pool. Bấm icon đó để mở hộp thoại. Chụp xong đổi tên thư mục lại như cũ, xoá bản sao.
- **Khung chụp:** Media Pool kèm hộp thoại Relink Media (chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** clip có thumbnail đỏ "Media Offline", icon Relink màu cam, nút **Locate** và **Disk Search**.
- **Alt + chú thích:** `![Relink Media cho clip offline](../assets/img/ref-relink-media.png)` — *Locate để trỏ tới thư mục mới, Disk Search để Resolve tự tìm theo tên file.*

### REF-10 — `ref-out-of-sync-indicator.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/loi-thuong-gap.md` — ngay sau heading `## Tiếng lệch hình`
- **Trang Resolve:** Edit
- **Chuẩn bị:** dùng một clip có tiếng liền hình (nếu demo không có, chọn clip có tiếng trong Media Pool và kéo lên một timeline tạm). Tắt **Linked Selection**, kéo riêng phần tiếng lệch vài frame rồi bật lại. Chuột phải con số đỏ ở đầu clip.
- **Khung chụp:** chỉ vùng clip trên timeline và menu chuột phải (menu xổ — chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** số đỏ ở đầu clip (ví dụ `+5`), menu có **Slip into place** và **Move into place**.
- **Alt + chú thích:** `![Số đỏ báo lệch tiếng và menu sửa](../assets/img/ref-out-of-sync-indicator.png)` — *Số đỏ là số frame tiếng đang lệch so với hình. Chuột phải để kéo về đúng chỗ.*

### REF-11 — `ref-new-timeline-project-settings.png`
- **Ưu tiên:** P2
- **Chèn vào:** `04-tham-khao/loi-thuong-gap.md` — ngay sau heading `## Video xuất ra bị giật`
- **Trang Resolve:** hộp thoại New Timeline
- **Chuẩn bị:** **File → New Timeline** (`⌘N`). Bỏ tick **Use Project Settings**, chọn tab **Format**. Không bấm Create.
- **Khung chụp:** chỉ hộp thoại.
- **Cần thấy rõ trong ảnh:** ô **Use Project Settings** đã bỏ tick, tab **Format** với **Timeline Frame Rate**.
- **Alt + chú thích:** `![Hộp thoại New Timeline với Use Project Settings bỏ tick](../assets/img/ref-new-timeline-project-settings.png)` — *Bỏ tick Use Project Settings để đặt frame rate riêng cho timeline mới.*

### REF-12 — `ref-render-media-offline-warning.png`
- **Ưu tiên:** P3
- **Chèn vào:** `04-tham-khao/loi-thuong-gap.md` — ngay sau heading `## Export bị kẹt ở 0% hoặc báo lỗi`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** làm tiếp trên bản sao project của REF-09, lúc clip đang offline. Sang Deliver, **Add to Render Queue**, bấm **Render All**. Chụp hộp cảnh báo, rồi bấm Cancel. Xong thì trả thư mục footage và xoá bản sao như REF-09.
- **Khung chụp:** chỉ hộp cảnh báo (chụp toàn màn hình rồi cắt).
- **Cần thấy rõ trong ảnh:** nội dung cảnh báo Media Offline và các nút lựa chọn.
- **Alt + chú thích:** `![Cảnh báo Media Offline khi render](../assets/img/ref-render-media-offline-warning.png)` — *Resolve dừng lại báo clip offline trước khi render. Relink xong mới render lại.*

---

**Tổng:** 24 ảnh — P1: 8 (STA-01, 04, 06, 08, 10; REF-01, 03, 09) · P2: 10 · P3: 6.
