# Danh sách ảnh cần chụp — trang Photo (`02-trang/photo/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-photo.png` (toàn cửa sổ, chưa có album — đã nhúng ở README). `photo-layout.svg`, `photo-white-balance.svg` là sơ đồ vẽ.

**Chuẩn bị chung — cần nạp ảnh tĩnh (demo hiện chỉ có video):**
1. Mở project "So tay DaVinci - Demo", sang trang **Photo** (icon máy ảnh, thứ 2 trên dãy icon).
2. Trong Media Pool tạo bin **Anh demo**. Bấm **Import Media**, nạp:
   - `/Users/mac/davinci/IMG_7912.CR3` — ảnh RAW Canon (đúng file ví dụ ở README, dùng cho mọi ảnh tab RAW).
   - Khoảng 8–12 file JPG từ `/Users/mac/davinci/uyen/` (ví dụ `IMG_7488.JPG` … `IMG_7497.JPG`) — dùng cho Lightbox, chấm sao, lọc, Paste Attributes. Đây là ảnh riêng của người dùng: chọn những ảnh phù hợp để đăng công khai.
   - Tuỳ chọn: `/Users/mac/davinci/IMG_6389.PNG` để có một ảnh PNG.
   - Nếu không muốn dùng ảnh cá nhân: ở trang Edit, đặt con trỏ trên clip phô mai và clip trại cừu → **File → Export → Current Frame as Still** ra vài file PNG/JPG rồi nạp lại.
3. Chuột phải trong Media Pool → **New Photo Album**, đặt tên **Demo - Anh**. Chọn mọi ảnh vừa nạp → chuột phải → **Add Photo(s) to Album**.
4. Mở dải album bằng nút **Photo Album** trên toolbar.

Sau mỗi ảnh có chỉnh sửa, reset ảnh về gốc (menu ba chấm Inspector → **Remove and Reset All**) trừ khi mục sau cần giữ.

---

### PHO-01 — `photo-toolbar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Thanh toolbar trên cùng`
- **Trang Resolve:** Photo
- **Chuẩn bị:** album Demo - Anh đang mở. Chuột phải toolbar → bật hiện nhãn chữ dưới icon (nếu có tuỳ chọn).
- **Khung chụp:** chỉ một vùng — toàn bộ dải toolbar trên cùng (có thể cắt làm hai nửa ghép dọc nếu quá dài).
- **Cần thấy rõ trong ảnh:** bảy nút Media Pool, Effects Library, Photo Album, Quick Export, Metadata, Capture (Studio, có thể xám), Inspector.
- **Alt + chú thích:** `![Toolbar trang Photo](../../assets/img/photo-toolbar.png)` — *Bảy nút từ trái sang phải; Capture chỉ có ở Studio.*

### PHO-02 — `photo-viewer-top-bar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Thanh trên của Viewer`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn ảnh IMG_7912.CR3 trong album, Viewer ở **Photo Album** + **Single View**.
- **Khung chụp:** chỉ một vùng — thanh trên của Viewer, toàn chiều ngang.
- **Cần thấy rõ trong ảnh:** Source, Photo Album, Zoom %, Album List, Single View, Lightbox, Viewer Guides, Photo Preview Resolution, Bypass Color and Fusion.
- **Alt + chú thích:** `![Thanh trên Viewer trang Photo](../../assets/img/photo-viewer-top-bar.png)` — *Chọn nguồn xem, mức zoom, Single View hay Lightbox.*

### PHO-03 — `photo-preview-resolution-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `### Photo Preview Resolution — cho máy chạy mượt`
- **Trang Resolve:** Photo
- **Chuẩn bị:** bấm nút **Photo Preview Resolution** cho xổ menu.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt vùng nút + menu.
- **Cần thấy rõ trong ảnh:** Auto (đang chọn), Full, Half, Quarter.
- **Alt + chú thích:** `![Menu Photo Preview Resolution](../../assets/img/photo-preview-resolution-menu.png)` — *Auto thu ảnh lớn về 4K khi xem; xuất luôn dùng kích thước gốc.*

### PHO-04 — `photo-lightbox.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Lightbox — xem cả album cùng lúc`
- **Trang Resolve:** Photo
- **Chuẩn bị:** bấm **Lightbox**. Kéo thanh trượt cỡ thumbnail cho thấy khoảng 3 hàng ảnh. Chọn một ảnh JPG.
- **Khung chụp:** chỉ một vùng — toàn bộ Viewer đang ở Lightbox.
- **Cần thấy rõ trong ảnh:** lưới thumbnail, ảnh đang chọn có viền, thanh trượt cỡ thumbnail góc trên trái, nút Lightbox sáng.
- **Alt + chú thích:** `![Lightbox trang Photo](../../assets/img/photo-lightbox.png)` — *Chỉnh một ảnh, cả lưới cập nhật trực tiếp.*

### PHO-05 — `photo-viewer-bottom-bar.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Thanh dưới của Viewer`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn một ảnh JPG, bấm `4` để chấm 4 sao, bấm `S` để gắn tag tốt.
- **Khung chụp:** chỉ một vùng — thanh dưới Viewer, toàn chiều ngang.
- **Cần thấy rõ trong ảnh:** Tools, EXIF Data, Favorite (tim, đang sáng), Untag, Reject (x), Version Selector, Star Rating (4 sao), Color, Flag.
- **Alt + chú thích:** `![Thanh dưới Viewer trang Photo](../../assets/img/photo-viewer-bottom-bar.png)` — *Ảnh đang được gắn tim và 4 sao.*

### PHO-06 — `photo-exif-overlay.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Thanh dưới của Viewer` (đặt sau PHO-05)
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn IMG_7912.CR3, bấm **EXIF Data**.
- **Khung chụp:** chỉ một vùng — Viewer với lớp EXIF hiện trên ảnh.
- **Cần thấy rõ trong ảnh:** tên máy ảnh, ISO, tốc độ, khẩu độ, ống kính.
- **Alt + chú thích:** `![Thông tin EXIF trên Viewer](../../assets/img/photo-exif-overlay.png)` — *Nút EXIF Data hiện thông số chụp ngay trên ảnh.*

### PHO-07 — `photo-viewer-guides.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Đường gióng và thước đo`
- **Trang Resolve:** Photo
- **Chuẩn bị:** bấm **Viewer Guides**, bật **Rulers**; **View → Guides → Add Guide** thêm một đường dọc ở 1/3 chiều ngang.
- **Khung chụp:** chỉ một vùng — Viewer có thước và đường gióng.
- **Cần thấy rõ trong ảnh:** thước pixel cạnh khung, đường gióng, icon ổ khoá góc trên trái thước.
- **Alt + chú thích:** `![Thước và đường gióng trên Viewer](../../assets/img/photo-viewer-guides.png)` — *Dùng để căn đường chân trời hay sản phẩm theo một phần ba.*

### PHO-08 — `photo-histogram.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `## Histogram`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn IMG_7912.CR3 (hơi tối), Histogram đang hiện mặc định.
- **Khung chụp:** chỉ một vùng — panel Histogram, kèm icon mở rộng góc trên phải.
- **Cần thấy rõ trong ảnh:** biểu đồ dồn về bên trái (ảnh tối), icon mở rộng.
- **Alt + chú thích:** `![Histogram trang Photo](../../assets/img/photo-histogram.png)` — *Histogram dồn trái: ảnh đang tối.*

### PHO-09 — `photo-media-pool-buttons.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Nạp ảnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** Media Pool đang mở bin Anh demo.
- **Khung chụp:** chỉ một vùng — thanh nút trên đầu Media Pool.
- **Cần thấy rõ trong ảnh:** Bin List, Back/Forward, Import Media, Import Media Folder, Import From Photos, Import Blackmagic Cloud Folder, Relink Media, AI Clip Analysis (Studio), Media Pool View, Search.
- **Alt + chú thích:** `![Thanh nút đầu Media Pool trang Photo](../../assets/img/photo-media-pool-buttons.png)` — *Import Media nạp từng ảnh, Import Media Folder nạp cả thư mục.*

### PHO-10 — `photo-new-album-menu.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Photo Album`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn 3 ảnh JPG trong Media Pool, chuột phải cho hiện menu ngữ cảnh.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Media Pool + menu.
- **Cần thấy rõ trong ảnh:** mục **New Photo Album** và **Add Photo(s) to Album**.
- **Alt + chú thích:** `![Menu chuột phải tạo album và thêm ảnh](../../assets/img/photo-new-album-menu.png)` — *Tạo album rồi thêm ảnh vào album mới chỉnh được.*

### PHO-11 — `photo-album-strip.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `### Icon nhỏ dưới thumbnail`
- **Trang Resolve:** Photo
- **Chuẩn bị:** trong album: áp **Vignette** cho ảnh 1 (để có icon FX), crop ảnh 2 (Tools → Crop 4:5, đóng Tools), Transform ảnh 3 (Zoom 1.1). Mở dải Photo Album.
- **Khung chụp:** chỉ một vùng — dải Photo Album ở đáy màn hình, gồm các icon lọc phía trên.
- **Cần thấy rõ trong ảnh:** thumbnail có icon FX, icon Transform, icon Crop; tên album.
- **Alt + chú thích:** `![Dải Photo Album với icon dưới thumbnail](../../assets/img/photo-album-strip.png)` — *FX là có hiệu ứng, hình chữ nhật là đã Transform, hai góc chồng là đã Crop.*

### PHO-12 — `photo-album-filters.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Lọc album`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chấm sao một vài ảnh (2, 3, 4, 5 sao), gắn `X` cho một ảnh. Chuột phải icon **Rating** trên dải album cho xổ menu điều kiện; chọn ≥ 4.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt hàng icon lọc + menu.
- **Cần thấy rõ trong ảnh:** icon Filters, Tags, Rating, Flags, Color, Keywords, Sort Photos; menu Rating với lựa chọn bằng/≤/≥ và số sao.
- **Alt + chú thích:** `![Icon lọc album và menu Rating](../../assets/img/photo-album-filters.png)` — *Bấm để bật lọc, chuột phải để chọn điều kiện.*

### PHO-13 — `photo-new-version.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Versions — nhiều phiên bản của một ảnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn một ảnh JPG, chỉnh Temp ấm lên; chuột phải ảnh trong album → **New Version**, gõ tên "Mau am" (để hộp thoại mở).
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt hộp đặt tên version, kèm Version Selector ở thanh dưới Viewer nếu lọt khung.
- **Cần thấy rõ trong ảnh:** ô tên version, nút OK.
- **Alt + chú thích:** `![Tạo phiên bản mới cho ảnh](../../assets/img/photo-new-version.png)` — *Lưu kiểu chỉnh hiện tại thành một version rồi thử kiểu khác.*

### PHO-14 — `photo-inspector-file-tab.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Metadata ảnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn IMG_7912.CR3, Inspector → tab **File**.
- **Khung chụp:** chỉ một vùng — panel Inspector từ hàng tab tới hết phần Metadata, gồm ô **Auto Select Next Photo**.
- **Cần thấy rõ trong ảnh:** File Data (ISO, tốc độ, khẩu độ…), các ô Metadata sửa được, ô Auto Select Next Photo.
- **Alt + chú thích:** `![Tab File trong Inspector trang Photo](../../assets/img/photo-inspector-file-tab.png)` — *File Data chỉ xem; phần Metadata gõ được.*

### PHO-15 — `photo-inspector-tabs.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `# Chỉnh ảnh — tab RAW, tab Photo, Tools` (đặt dưới bảng bốn tab, trước dấu `---`)
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn một ảnh JPG, mở Inspector. Chụp ảnh A. Chọn IMG_7912.CR3, chụp ảnh B.
- **Khung chụp:** chỉ một vùng — hàng tab đầu Inspector; ghép hai ảnh A và B cạnh nhau.
- **Cần thấy rõ trong ảnh:** RAW · Photo · Effects · File; tab RAW xám với JPG (A) và sáng với CR3 (B).
- **Alt + chú thích:** `![Tab RAW xám với JPG, sáng với CR3](../../assets/img/photo-inspector-tabs.png)` — *Tab RAW chỉ sáng khi ảnh là file RAW.*

### PHO-16 — `photo-raw-white-balance.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Nhóm 2 — Cân bằng trắng`
- **Trang Resolve:** Photo
- **Chuẩn bị:** IMG_7912.CR3, Inspector → tab **RAW**, mở menu **White Balance** cho xổ danh sách preset.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector từ Decode Quality tới Tint + menu.
- **Cần thấy rõ trong ảnh:** As Shot, Daylight, Cloudy, Shade, Tungsten, Fluorescent, Flash; thanh Color Temp và Tint.
- **Alt + chú thích:** `![Preset White Balance trong tab RAW](../../assets/img/photo-raw-white-balance.png)` — *Chọn preset gần đúng, rồi tinh chỉnh Color Temp và Tint.*

### PHO-17 — `photo-raw-exposure-color.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Thứ tự kéo các thanh trong tab RAW`
- **Trang Resolve:** Photo
- **Chuẩn bị:** IMG_7912.CR3, tab RAW, đặt đúng giá trị ví dụ ở README: White Balance Daylight, Exposure +0.7, Highlights −40, Shadows +25, Color Boost +15, Midtone Detail +10.
- **Khung chụp:** chỉ một vùng — Inspector tab RAW từ White Balance tới Sharpness/Noise Reduction (cuộn nếu cần, ghép hai nửa).
- **Cần thấy rõ trong ảnh:** các thanh với đúng giá trị trên.
- **Alt + chú thích:** `![Tab RAW sau khi chỉnh ảnh ví dụ](../../assets/img/photo-raw-exposure-color.png)` — *Đủ bước cân bằng trắng, phơi sáng, màu, độ nét trong một tab.*
- **Ghi chú:** giữ nguyên chỉnh sửa này cho PHO-18.

### PHO-18 — `photo-before-after.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/README.md` — ngay sau heading `## Ví dụ: chỉnh một ảnh RAW Canon từ đầu đến cuối` (cuối danh sách bước)
- **Trang Resolve:** Photo
- **Chuẩn bị:** IMG_7912.CR3 đã chỉnh theo PHO-17. Chụp Viewer một lần, bấm `⇧D` (Bypass), chụp lần nữa.
- **Khung chụp:** chỉ một vùng — riêng ảnh trong Viewer; ghép trước/sau cạnh nhau.
- **Cần thấy rõ trong ảnh:** ảnh gốc tối ám xanh (trái) và ảnh đã chỉnh (phải).
- **Alt + chú thích:** `![Ảnh RAW trước và sau khi chỉnh](../../assets/img/photo-before-after.png)` — *Bên trái là gốc, bên phải sau các bước 3–7.*

### PHO-19 — `photo-tab-photo-adjustments.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Các thanh trong Adjustments`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn một ảnh JPG, Inspector → tab **Photo**, thu gọn Source Transform/Source Cropping/Looks, mở **Adjustments**. Không đổi giá trị (để thấy Saturation 50, Hue 50 mặc định).
- **Khung chụp:** chỉ một vùng — Inspector từ tiêu đề Adjustments tới hết Hue, gồm nút Auto Balance.
- **Cần thấy rõ trong ảnh:** Auto Balance, Temp, Tint, Lift, Gamma, Gain, Contrast, Pivot, Midtone Details, Shadows, Highlights, Saturation = 50, Hue = 50.
- **Alt + chú thích:** `![Nhóm Adjustments trong tab Photo](../../assets/img/photo-tab-photo-adjustments.png)` — *Lưu ý Saturation mặc định là 50, không phải 0.*

### PHO-20 — `photo-looks-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Looks — tông màu có sẵn`
- **Trang Resolve:** Photo
- **Chuẩn bị:** ảnh JPG, tab Photo → Looks → mở menu **Type**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector + menu.
- **Cần thấy rõ trong ảnh:** Default (Original) và danh sách look có sẵn.
- **Alt + chú thích:** `![Menu Looks trong tab Photo](../../assets/img/photo-looks-menu.png)` — *Chọn một tông có sẵn rồi chỉnh tiếp bằng Adjustments.*

### PHO-21 — `photo-tools-crop.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Crop`
- **Trang Resolve:** Photo
- **Chuẩn bị:** IMG_7912.CR3 (hoặc ảnh JPG ngang), bấm **Tools** góc dưới trái Viewer → **Crop**, mở menu **Aspect Ratio** chọn `4:5`, ổ khoá Lock Aspect Ratio đang khoá. Giữ Tools mở.
- **Khung chụp:** chỉ một vùng — Viewer có khung crop + hàng Tools bên dưới.
- **Cần thấy rõ trong ảnh:** khung crop 4:5 với tay nắm cạnh, khung ảnh gốc mờ bên dưới, Aspect Ratio = 4:5, ổ khoá, nút Toggle/Reset hai đầu.
- **Alt + chú thích:** `![Crop 4:5 bằng Tools trên Viewer](../../assets/img/photo-tools-crop.png)` — *Crop chỉ áp vào ảnh khi đóng thanh Tools.*

### PHO-22 — `photo-tools-transform.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Transform`
- **Trang Resolve:** Photo
- **Chuẩn bị:** ảnh JPG, Tools → **Transform**, xoay nhẹ khoảng 3° bằng tay nắm giữa.
- **Khung chụp:** chỉ một vùng — Viewer + hàng Transform.
- **Cần thấy rõ trong ảnh:** khung điều khiển, tay nắm xoay, nút Zoom Link (ổ khoá).
- **Alt + chú thích:** `![Transform trên Viewer trang Photo](../../assets/img/photo-tools-transform.png)` — *Kéo tay nắm giữa để xoay thẳng đường chân trời.*

### PHO-23 — `photo-paste-attributes.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Cách 2 — Paste Attributes (chọn được copy gì)`
- **Trang Resolve:** hộp thoại Paste Attributes (trang Photo)
- **Chuẩn bị:** chỉnh một ảnh JPG (Temp, Contrast, thêm Vignette), `⌘C`. Chọn 3 ảnh JPG khác, `⌥V`.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Paste Attributes.
- **Cần thấy rõ trong ảnh:** các ô tick Photo Attributes, ô **Plugins**, nút Apply.
- **Alt + chú thích:** `![Hộp Paste Attributes](../../assets/img/photo-paste-attributes.png)` — *Tick Plugins nếu muốn dán cả hiệu ứng.*

### PHO-24 — `photo-generate-lut.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `## Lưu tông màu thành LUT`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chuột phải một ảnh đã chỉnh trong album → rê tới **Generate LUT** cho hiện menu con.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt dải album + menu.
- **Cần thấy rõ trong ảnh:** Generate LUT → 33 Point Cube (và các lựa chọn khác).
- **Alt + chú thích:** `![Generate LUT từ ảnh đã chỉnh](../../assets/img/photo-generate-lut.png)` — *Chỉ thiết lập tab Photo được lưu vào LUT.*
- **Ghi chú:** không cần lưu file LUT thật — Esc sau khi chụp.

### PHO-25 — `photo-inspector-reset-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `## Reset`
- **Trang Resolve:** Photo
- **Chuẩn bị:** IMG_7912.CR3 đã chỉnh; bấm menu **ba chấm** góc trên phải Inspector.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt đầu Inspector + menu.
- **Cần thấy rõ trong ảnh:** Reset Photo (⌘R), Remove All Photo Effects (⇧R), Reset Camera Raw, Remove and Reset All (⌘⇧R).
- **Alt + chú thích:** `![Menu reset của Inspector trang Photo](../../assets/img/photo-inspector-reset-menu.png)` — *Reset riêng từng tab hoặc đưa ảnh về nguyên gốc.*

### PHO-26 — `photo-effects-library.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/hieu-ung.md` — ngay sau heading `## Xem trước, áp, chỉnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** bấm **Effects Library**; chọn một ảnh JPG; rê chuột lên thumbnail **Vignette** để Viewer xem trước.
- **Khung chụp:** chỉ một vùng — Effects Library + Viewer (ảnh có vignette xem trước).
- **Cần thấy rõ trong ảnh:** các nhóm hiệu ứng, ô tìm kiếm, tab Favorites, thumbnail Vignette đang được rê chuột.
- **Alt + chú thích:** `![Effects Library trang Photo, xem trước Vignette](../../assets/img/photo-effects-library.png)` — *Rê chuột qua thumbnail là thấy kết quả trên ảnh, chưa cần áp thật.*

### PHO-27 — `photo-effects-inspector-stack.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/hieu-ung.md` — ngay sau heading `### Chỉnh thông số`
- **Trang Resolve:** Photo
- **Chuẩn bị:** áp lần lượt **Sharpen** rồi **Vignette** lên một ảnh JPG; Inspector → tab **Effects**.
- **Khung chụp:** chỉ một vùng — Inspector tab Effects, thấy hai hiệu ứng xếp chồng và mũi tên lên/xuống cạnh tên.
- **Cần thấy rõ trong ảnh:** Sharpen ở trên, Vignette ở dưới, mũi tên đổi thứ tự.
- **Alt + chú thích:** `![Hai hiệu ứng xếp chồng trong tab Effects](../../assets/img/photo-effects-inspector-stack.png)` — *Hiệu ứng chạy từ trên xuống; sửa ảnh trên, tạo không khí dưới.*

### PHO-28 — `photo-quick-export.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/xuat-anh.md` — ngay sau heading `## Quick Export`
- **Trang Resolve:** hộp thoại Quick Export (trang Photo)
- **Chuẩn bị:** chọn một ảnh trong album, bấm **Quick Export** trên toolbar; chọn **JPEG** ở cột trái; Quality khoảng 90%, Resolution 72. Không bấm Export.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Quick Export.
- **Cần thấy rõ trong ảnh:** cột định dạng JPEG/PNG/HEIC/TIFF; cột thông số Export, File Name, Scale, Resolution, Quality, Bit Depth, Include Metadata; nút Export.
- **Alt + chú thích:** `![Quick Export riêng cho ảnh tĩnh](../../assets/img/photo-quick-export.png)` — *Chọn định dạng bên trái, đặt thông số bên phải, rồi Export.*

### PHO-29 — `photo-deliver-still-mode.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/xuat-anh.md` — ngay sau heading `## Xuất từ trang Deliver`
- **Trang Resolve:** Deliver (chế độ ảnh tĩnh)
- **Chuẩn bị:** album Demo - Anh đang mở ở trang Photo, chuyển sang trang **Deliver**. Mở mục **Size** chọn **Long Side**, 2048.
- **Khung chụp:** chỉ một vùng — panel Render Settings chế độ ảnh, từ File Name tới hết Size, gồm nút Add to Render Queue.
- **Cần thấy rõ trong ảnh:** Entire Album / Selected Photos, nút `+` cạnh File Name, định dạng, Size = Long Side 2048, Include Alpha Channel.
- **Alt + chú thích:** `![Trang Deliver ở chế độ xuất ảnh](../../assets/img/photo-deliver-still-mode.png)` — *Đang mở album thì Deliver tự đổi sang giao diện xuất ảnh.*

### PHO-30 — `photo-album-in-color.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/xuat-anh.md` — ngay sau heading `## Đưa album sang trang Color`
- **Trang Resolve:** Color
- **Chuẩn bị:** album Demo - Anh đang mở, IMG_7912.CR3 đã chỉnh ở tab RAW/Photo; chuyển sang trang **Color**, chọn ảnh đó trong dải thumbnail.
- **Khung chụp:** chỉ một vùng — dải thumbnail (album thành timeline) + Node Editor.
- **Cần thấy rõ trong ảnh:** mỗi ảnh là một clip trong dải thumbnail; node đầu tiên chứa chỉnh sửa từ trang Photo.
- **Alt + chú thích:** `![Album ảnh mở ở trang Color](../../assets/img/photo-album-in-color.png)` — *Chỉnh sửa ở trang Photo thành node đầu tiên; thêm node sau nó.*
