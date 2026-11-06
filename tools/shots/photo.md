# Danh sách ảnh cần chụp — trang Photo (`02-trang/photo/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-photo.png` (toàn cửa sổ, chưa có album — đã nhúng ở README). `photo-layout.svg`, `photo-white-balance.svg`, `photo-where-adjust.svg`, `photo-album-flow.svg`, `photo-export-options.svg` là sơ đồ vẽ, không cần chụp.

**Chuẩn bị chung — cần nạp ảnh tĩnh (demo hiện chỉ có video):**

Không dùng ảnh cá nhân của chủ máy. Mọi ảnh trong danh sách này là ảnh stock miễn phí.

1. Tải về một thư mục riêng (ví dụ `~/Downloads/demo-anh/`):
   - 10–12 ảnh **JPG** stock miễn phí, giấy phép cho dùng lại (Unsplash, Pexels): nên có 1 ảnh trong nhà ám vàng, 1 ảnh phong cảnh có đường chân trời, 1 ảnh chân dung, 1 ảnh đồ ăn. Không có người nổi tiếng, không có logo thương hiệu.
   - 1 ảnh **RAW Canon `.CR3`** mẫu miễn phí (trang mẫu ảnh của các trang review máy ảnh có file CR3 tải tự do). Nên chọn ảnh chụp ngoài trời, hơi tối, có trời sáng — để ví dụ tab RAW (Daylight, Exposure, Highlights) có tác dụng rõ. Trong danh sách gọi là **ảnh mẫu CR3 trong album Demo - Anh**.
   - Tuỳ chọn: 1 ảnh **PNG** có nền trong suốt (cho mục xuất PNG / Include Alpha Channel).
2. Mở project "So tay DaVinci - Demo", sang trang **Photo** (icon máy ảnh trên dãy icon trang).
3. Trong Media Pool: **Bin List** → **+ Add Bin**, đặt tên **06 Anh**. Mở bin đó, bấm icon **Import Media** → **Import Media Folder** → chọn thư mục vừa tải.
4. Chọn mọi ảnh vừa nạp → chuột phải → **Create New Photo Album Using Selected Clips...**, đặt tên **Demo - Anh** → **Create**. (Ảnh nạp thêm sau: chuột phải → **Add Photo(s) to Album**.)
5. Mở dải album bằng nút **Photo Album** trên toolbar.

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
- **Chuẩn bị:** chọn ảnh mẫu CR3 trong album Demo - Anh, Viewer ở **Photo Album** + **Single View**.
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
- **Chuẩn bị:** chọn ảnh mẫu CR3 trong album Demo - Anh, bấm **EXIF Data**.
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
- **Chuẩn bị:** chọn ảnh mẫu CR3 trong album Demo - Anh (hơi tối), Histogram đang hiện mặc định.
- **Khung chụp:** chỉ một vùng — panel Histogram, kèm icon mở rộng góc trên phải.
- **Cần thấy rõ trong ảnh:** biểu đồ dồn về bên trái (ảnh tối), icon mở rộng.
- **Alt + chú thích:** `![Histogram trang Photo](../../assets/img/photo-histogram.png)` — *Histogram dồn trái: ảnh đang tối.*

### PHO-09 — `photo-media-pool-buttons.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Nạp ảnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** Media Pool đang mở bin 06 Anh.
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
- **Chuẩn bị:** chọn ảnh mẫu CR3 trong album Demo - Anh, Inspector → tab **File**.
- **Khung chụp:** chỉ một vùng — panel Inspector từ hàng tab tới hết phần Metadata, gồm ô **Auto Select Next Photo**.
- **Cần thấy rõ trong ảnh:** File Data (ISO, tốc độ, khẩu độ…), các ô Metadata sửa được, ô Auto Select Next Photo.
- **Alt + chú thích:** `![Tab File trong Inspector trang Photo](../../assets/img/photo-inspector-file-tab.png)` — *File Data chỉ xem; phần Metadata gõ được.*

### PHO-15 — `photo-inspector-tabs.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `# Chỉnh ảnh — tab RAW, tab Photo, Tools` (đặt dưới bảng bốn tab, trước dấu `---`)
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn một ảnh JPG, mở Inspector. Chụp ảnh A. Chọn ảnh mẫu CR3 trong album Demo - Anh, chụp ảnh B.
- **Khung chụp:** chỉ một vùng — hàng tab đầu Inspector; ghép hai ảnh A và B cạnh nhau.
- **Cần thấy rõ trong ảnh:** RAW · Photo · Effects · File; tab RAW xám với JPG (A) và sáng với CR3 (B).
- **Alt + chú thích:** `![Tab RAW xám với JPG, sáng với CR3](../../assets/img/photo-inspector-tabs.png)` — *Tab RAW chỉ sáng khi ảnh là file RAW.*

### PHO-16 — `photo-raw-white-balance.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Nhóm 2 — Cân bằng trắng`
- **Trang Resolve:** Photo
- **Chuẩn bị:** ảnh mẫu CR3 trong album Demo - Anh, Inspector → tab **RAW**, mở menu **White Balance** cho xổ danh sách preset.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector từ Decode Quality tới Tint + menu.
- **Cần thấy rõ trong ảnh:** As Shot, Daylight, Cloudy, Shade, Tungsten, Fluorescent, Flash; thanh Color Temp và Tint.
- **Alt + chú thích:** `![Preset White Balance trong tab RAW](../../assets/img/photo-raw-white-balance.png)` — *Chọn preset gần đúng, rồi tinh chỉnh Color Temp và Tint.*

### PHO-17 — `photo-raw-exposure-color.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Thứ tự kéo các thanh trong tab RAW`
- **Trang Resolve:** Photo
- **Chuẩn bị:** ảnh mẫu CR3 trong album Demo - Anh, tab RAW, đặt đúng giá trị ví dụ ở README: White Balance Daylight, Exposure +0.7, Highlights −40, Shadows +25, Color Boost +15, Midtone Detail +10.
- **Khung chụp:** chỉ một vùng — Inspector tab RAW từ White Balance tới Sharpness/Noise Reduction (cuộn nếu cần, ghép hai nửa).
- **Cần thấy rõ trong ảnh:** các thanh với đúng giá trị trên.
- **Alt + chú thích:** `![Tab RAW sau khi chỉnh ảnh ví dụ](../../assets/img/photo-raw-exposure-color.png)` — *Đủ bước cân bằng trắng, phơi sáng, màu, độ nét trong một tab.*
- **Ghi chú:** giữ nguyên chỉnh sửa này cho PHO-18.

### PHO-18 — `photo-before-after.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/README.md` — ngay sau heading `## Ví dụ: chỉnh một ảnh RAW Canon từ đầu đến cuối` (cuối danh sách bước)
- **Trang Resolve:** Photo
- **Chuẩn bị:** ảnh mẫu CR3 trong album Demo - Anh đã chỉnh theo PHO-17. Chụp Viewer một lần, bấm `⇧D` (Bypass), chụp lần nữa.
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
- **Chuẩn bị:** ảnh mẫu CR3 trong album Demo - Anh (hoặc ảnh JPG ngang), bấm **Tools** góc dưới trái Viewer → **Crop**, mở menu **Aspect Ratio** chọn `4:5`, ổ khoá Lock Aspect Ratio đang khoá. Giữ Tools mở.
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
- **Chuẩn bị:** ảnh mẫu CR3 trong album Demo - Anh đã chỉnh; bấm menu **ba chấm** góc trên phải Inspector.
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
- **Chuẩn bị:** không chọn ảnh nào trong album, bấm **Quick Export** trên toolbar; đặt đúng ví dụ "gửi khách qua Zalo" trong trang: **JPEG** ở cột trái · **Export** cả album · **File Name** `Demo_` · **Scale** `50%` · **Resolution** `72` · **Quality** khoảng 85% · bỏ tick **Include Metadata**. Không bấm Export.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Quick Export.
- **Cần thấy rõ trong ảnh:** cột định dạng JPEG/PNG/HEIC/TIFF (JPEG đang chọn); cột thông số Export, File Name = Demo_, Scale = 50%, Resolution = 72, Quality ≈ 85%, Bit Depth, Include Metadata bỏ tick; nút Export.
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
- **Chuẩn bị:** album Demo - Anh đang mở, ảnh mẫu CR3 đã chỉnh ở tab RAW/Photo; chuyển sang trang **Color**, chọn ảnh đó trong dải thumbnail.
- **Khung chụp:** chỉ một vùng — dải thumbnail (album thành timeline) + Node Editor.
- **Cần thấy rõ trong ảnh:** mỗi ảnh là một clip trong dải thumbnail; node đầu tiên chứa chỉnh sửa từ trang Photo.
- **Alt + chú thích:** `![Album ảnh mở ở trang Color](../../assets/img/photo-album-in-color.png)` — *Chỉnh sửa ở trang Photo thành node đầu tiên; thêm node sau nó.*

### PHO-31 — `photo-import-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `### Cách nạp`
- **Trang Resolve:** Photo
- **Chuẩn bị:** Media Pool đang mở bin 06 Anh. Bấm icon **Import Media** trên đầu Media Pool cho xổ menu.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt thanh nút Media Pool + menu.
- **Cần thấy rõ trong ảnh:** bốn mục Import Media, Import Media Folder, Import from Photos, Import Blackmagic Cloud Folder.
- **Alt + chú thích:** `![Menu Import Media trang Photo](../../assets/img/photo-import-menu.png)` — *Import Media Folder nạp cả một buổi chụp một lần.*

### PHO-32 — `photo-smart-bin-dialog.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `### Bin và Smart Bin`
- **Trang Resolve:** hộp thoại Smart Bin (trang Photo)
- **Chuẩn bị:** **Bin List** → **+ Add Smart Bin**. Đặt tên `Anh Canon`, luật **Camera** chứa `Canon`. Không bấm Create.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Smart Bin.
- **Cần thấy rõ trong ảnh:** ô tên, dòng luật Camera / contains / Canon, nút Create Smart Bin.
- **Alt + chú thích:** `![Tạo Smart Bin lọc ảnh máy Canon](../../assets/img/photo-smart-bin-dialog.png)` — *Ảnh Canon nạp sau cũng tự vào bin này.*
- **Ghi chú:** ảnh mẫu CR3 phải nằm trong project để luật có kết quả. Bấm Cancel sau khi chụp.

### PHO-33 — `photo-lightroom-import.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `### Nạp catalog Lightroom`
- **Trang Resolve:** Photo (menu File)
- **Chuẩn bị:** mở **File → Import**, rê tới menu con cho hiện **Lightroom Catalog**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt menu File + menu con Import.
- **Cần thấy rõ trong ảnh:** mục Lightroom Catalog đang được rê chuột.
- **Alt + chú thích:** `![Menu File → Import → Lightroom Catalog](../../assets/img/photo-lightroom-import.png)` — *Ảnh vào ở trạng thái gốc, chỉnh sửa Lightroom không đi theo.*

### PHO-34 — `photo-advanced-filter-menu.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `### Lọc nâng cao`
- **Trang Resolve:** Photo
- **Chuẩn bị:** dải album đang mở. Bấm mũi tên thả xuống cạnh tên **Demo - Anh** cho xổ menu; rê tới **Modified Photos** cho hiện menu con mốc giờ.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt đầu dải album + menu.
- **Cần thấy rõ trong ảnh:** All Photos, Selected Photos, Graded / Ungraded Photos, Modified Photos (menu con last hour…), Open FX, Source Sizing, Create Smart Filter.
- **Alt + chú thích:** `![Menu lọc nâng cao của Photo Album](../../assets/img/photo-advanced-filter-menu.png)` — *Ungraded Photos chỉ hiện ảnh chưa chỉnh.*

### PHO-35 — `photo-metadata-panel.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/nap-va-album.md` — ngay sau heading `## Metadata ảnh`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn ảnh mẫu CR3, bấm nút **Metadata** trên toolbar. Mở menu **Metadata Groups** (bên phải) cho xổ, rê tới **Camera**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt đầu bảng Metadata + menu.
- **Cần thấy rõ trong ảnh:** menu Metadata Presets (Default) bên trái, menu Metadata Groups bên phải với nhóm Camera.
- **Alt + chú thích:** `![Bảng Metadata với hai menu Presets và Groups](../../assets/img/photo-metadata-panel.png)` — *Nhóm Camera sửa được ISO, tốc độ, ống kính.*
- **Ghi chú:** đặt sau PHO-14.

### PHO-36 — `photo-effects-overlay.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/chinh-anh.md` — ngay sau heading `### Effects Overlay`
- **Trang Resolve:** Photo
- **Chuẩn bị:** áp **Vignette** lên một ảnh JPG. Bấm **Tools** → icon **Effects Overlay**, chọn **Open FX Overlay** để hiện điều khiển trên Viewer.
- **Khung chụp:** chỉ một vùng — Viewer với điều khiển của hiệu ứng + hàng Tools bên dưới.
- **Cần thấy rõ trong ảnh:** điểm tâm / khung điều khiển hiệu ứng trên ảnh, icon Effects Overlay đang sáng.
- **Alt + chú thích:** `![Điều khiển hiệu ứng trên Viewer qua Effects Overlay](../../assets/img/photo-effects-overlay.png)` — *Kéo trực tiếp trên ảnh; ⇧` để ẩn tạm.*

### PHO-37 — `photo-effect-toggle-trash.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/photo/hieu-ung.md` — ngay sau heading `### Gỡ hiệu ứng`
- **Trang Resolve:** Photo
- **Chuẩn bị:** giữ ảnh có Sharpen + Vignette từ PHO-27. Tắt công tắc cam của **Vignette**.
- **Khung chụp:** chỉ một vùng — hai dòng tiêu đề hiệu ứng trong Inspector tab Effects.
- **Cần thấy rõ trong ảnh:** công tắc cam (Sharpen bật, Vignette tắt), icon thùng rác bên phải, mũi tên lên/xuống.
- **Alt + chú thích:** `![Công tắc bật tắt và thùng rác của hiệu ứng](../../assets/img/photo-effect-toggle-trash.png)` — *Công tắc tắt tạm giữ thông số; thùng rác xoá hẳn.*

### PHO-38 — `photo-deliver-photo-section.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/photo/xuat-anh.md` — ngay sau heading `### Mục Photo`
- **Trang Resolve:** Deliver (chế độ ảnh tĩnh)
- **Chuẩn bị:** album Demo - Anh đang mở ở trang Photo, chuyển sang **Deliver**. Mục **Photo**: **Format** `JPEG`, **Bit Depth** 8-bit, **Size** `Long Side` `2048`, **Resolution** `72` ppi, **Quality** `90`, bỏ tick **Include Metadata**.
- **Khung chụp:** chỉ một vùng — panel Render Settings, riêng mục Photo từ Format tới Include Metadata.
- **Cần thấy rõ trong ảnh:** đúng các giá trị trên, menu Format (HEIF/JPEG/PNG/TIFF) nếu chụp được lúc xổ.
- **Alt + chú thích:** `![Mục Photo trong Render Settings](../../assets/img/photo-deliver-photo-section.png)` — *JPEG 90%, cạnh dài 2048: bộ ảnh gửi khách qua mạng.*
- **Ghi chú:** PHO-29 chụp phần File Name/Export/Size tổng quát; ảnh này chỉ cắt mục Photo.

### PHO-39 — `photo-deliver-file-section.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/xuat-anh.md` — ngay sau heading `### Đặt tên file tự động`
- **Trang Resolve:** Deliver (chế độ ảnh tĩnh)
- **Chuẩn bị:** như PHO-38. Mở mục **File**: **File Name Uses** `Custom Name`, **Custom Name** `Demo_` rồi gõ `%` cho xổ danh sách trường metadata; **File Suffix** `_web`; `3` digits.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt mục File + danh sách trường.
- **Cần thấy rõ trong ảnh:** File Name Uses, Custom Name với danh sách trường metadata, File Suffix, số chữ số.
- **Alt + chú thích:** `![Mục File đặt tên ảnh tự động](../../assets/img/photo-deliver-file-section.png)` — *Gõ % để chèn trường metadata vào tên file.*

### PHO-40 — `photo-safe-area-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/photo/giao-dien.md` — ngay sau heading `### Safe Area`
- **Trang Resolve:** Photo
- **Chuẩn bị:** chọn ảnh JPG ngang. Bấm **Viewer Guides** trên thanh trên Viewer cho xổ menu tỉ lệ.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt thanh trên Viewer + menu.
- **Cần thấy rõ trong ảnh:** danh sách tỉ lệ khung an toàn, icon Safe Area.
- **Alt + chú thích:** `![Menu Viewer Guides chọn khung an toàn](../../assets/img/photo-safe-area-menu.png)` — *Bật khung tỉ lệ nơi đăng trước khi crop.*
- **Ghi chú:** nếu menu có `4:5` thì chọn và chụp thêm Viewer có khung 4:5; nếu không có, ghi lại để sửa trang.
