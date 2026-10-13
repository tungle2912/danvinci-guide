# Giao diện trang Media — từng nút nằm ở đâu

Trang Media có năm vùng: **Media Storage** (trên trái), **Viewer** (trên giữa), **Audio Panel** và **Metadata Editor** (bên phải), **Media Pool** (dưới). Inspector và Clone Tool là hai panel bật thêm khi cần.

Phần lớn lệnh của trang này **không nằm trên nút**, mà nằm trong **menu chuột phải**. Gặp clip hay thư mục, cứ chuột phải trước.

Đổi kích thước: kéo **đường viền** giữa hai panel bất kỳ. Lỡ kéo lộn xộn: **Workspace → Reset UI Layout** để về bố cục gốc.

---

## Interface Toolbar — dải nút trên cùng

Tám nút, từ trái sang phải. Mỗi nút bật/tắt một vùng.

| # | Nút | Làm gì | Mức |
|---|---|---|---|
| 1 | **Media Storage full/half height** | Media Storage cao hết màn hình. Media Pool bị thu nhỏ lại | ★☆☆ |
| 2 | **Media Storage** | Ẩn/hiện Media Storage. Ẩn đi thì Viewer rộng ra | ★★☆ |
| 3 | **Clone Tool** | Ẩn/hiện công cụ copy thẻ nhớ — xem [Clone Tool](clone-tool.md) | ★★☆ |
| 4 | **Audio Panel** | Ẩn/hiện panel âm thanh | ★★☆ |
| 5 | **Metadata** | Ẩn/hiện Metadata Editor | ★★☆ |
| 6 | **Inspector** | Ẩn/hiện Inspector | ★★☆ |
| 7 | **Capture** | Chuyển Viewer và Audio Panel sang chế độ thu từ đầu băng. Cần đầu băng điều khiển được | ★☆☆ |
| 8 | **Audio/Metadata full/half height** | Audio Panel hoặc Metadata Editor cao hết màn hình | ★☆☆ |

> **Màn hình laptop chật?** Tắt Media Storage (nút 2) sau khi nạp xong. Viewer rộng gấp rưỡi.

---

## Media Storage — trình duyệt ổ đĩa

Chi tiết cách dùng: [Media Storage](media-storage.md). Ở đây chỉ liệt kê nút.

| Nút / vùng | Ở đâu | Làm gì | Mức |
|---|---|---|---|
| **Nút ẩn/hiện danh sách thư mục** | Góc trên trái | Ẩn cột ổ đĩa bên trái để vùng xem file rộng ra | ★☆☆ |
| **Cột ổ đĩa** (Volume List) | Bên trái | Scratch volumes, các ổ đang gắn, Favorites | ★★★ |
| **Ba nút kiểu xem** | Phía trên vùng file | **List**, **Thumbnail**, **Metadata** | ★★☆ |
| **Ô tìm kiếm** | Phía trên | Tìm file trong thư mục đang mở | ★★☆ |
| **Menu sắp xếp** (Thumbnail Sort) | Giữa ô tìm và menu ⋯, chỉ hiện ở Thumbnail view | Sắp thumbnail theo File Name, Reel Name, Start TC, FPS… tăng hoặc giảm | ★☆☆ |
| **Menu ⋯** | Góc trên phải | Có **Frame Display Mode** — cách hiện chuỗi ảnh | ★☆☆ |
| **Clip Info** (mũi tên nhỏ) | Góc dưới phải mỗi thumbnail | Xem nhanh tên, timecode, độ dài, độ phân giải, fps, codec, ngày tạo | ★★☆ |

**Mẹo mở nhanh một thư mục:** kéo thư mục từ Finder thả vào Media Storage. Media Storage nhảy thẳng tới đúng chỗ đó.

---

## Viewer

Bấm vào clip ở **bất kỳ đâu** trong trang Media (Media Storage hay Media Pool) là clip hiện trong Viewer.

### Góc trên phải

| Nút | Làm gì | Mức |
|---|---|---|
| **Ô timecode** | Vị trí con trỏ trong clip | ★★☆ |
| **Menu ⋯** | Tuỳ chọn Viewer — bảng dưới | ★★☆ |

**Menu ⋯ của Viewer:**

| Mục | Làm gì | Mức |
|---|---|---|
| **Live Media Preview** | Bật sẵn. Rê chuột trên thumbnail là Viewer hiện theo | ★★★ |
| **Show All Video Frames** | Máy yếu: bật thì đủ khung hình nhưng tiếng méo; tắt thì giữ tiếng, bỏ bớt khung | ★☆☆ |
| **Show Timecode Toolbar** | Thanh nhỏ hiện timecode `I`, `O` và độ dài đoạn đã chọn | ★★☆ |
| **Show Audio Waveforms in Source Clip** | Dạng sóng tiếng của cả clip đè lên đáy hình | ★★☆ |
| **Show Audio Waveforms Zoomed In** | Dạng sóng phóng to quanh con trỏ | ★☆☆ |
| **Previous Clip / Next Clip** | Nhảy sang clip trước/sau trong Media Pool | ★★☆ |
| **Clear Recently Viewed Clips** | Xoá danh sách clip xem gần đây | ★☆☆ |
| **Show Marker Overlays** | Bật sẵn. Dừng đúng marker thì ghi chú marker hiện trên hình | ★☆☆ |
| **Markers** | Danh sách marker của clip. Chọn một cái là nhảy tới đó | ★☆☆ |

> **Show Timecode Toolbar** rất đáng bật khi cắt subclip: bạn thấy ngay đoạn `I`→`O` dài bao nhiêu giây.

### Dưới đáy Viewer — từ trái sang phải

| Nút | Làm gì | Mức |
|---|---|---|
| **Thanh jog** (ngay dưới hình) | Kéo con trỏ. Cả chiều ngang = cả clip | ★★★ |
| **Jog** (núm nhỏ bên trái) | Kéo trái/phải để dò từng khung | ★★☆ |
| **Về khung đầu · Phát lùi · Dừng · Phát · Về khung cuối** | Nút phát. `Space` để phát/dừng | ★★★ |
| **In / Out** | Đặt điểm vào/ra (`I` / `O`) | ★★★ |
| **Biểu tượng loa** | Bấm: tắt/bật tiếng. **Chuột phải** rồi kéo: chỉnh âm lượng nghe | ★★☆ |

**Mẹo xem lướt:** giữ phím `C` rồi rê chuột trên Viewer là tua theo chuột.

**Chuột phải thanh jog → Make Subclip:** cắt đoạn `I`→`O` thành subclip. Xem [Nạp một đoạn](nap-media.md#nạp-một-đoạn-thay-vì-cả-clip-subclip).

**Toàn màn hình:** **Workspace → Viewer Mode → Cinema Viewer** (`⌘F`). Bấm lại để thoát.

---

## Audio Panel

Ẩn/hiện bằng nút **Audio Panel** trên Interface Toolbar. Có **hai chế độ**, đổi bằng hai nút phía trên panel:

| Chế độ | Hiện gì | Dùng khi | Mức |
|---|---|---|---|
| **Meters** (mặc định) | Đồng hồ đo mức tiếng từng track khi phát clip | Kiểm tra clip có tiếng không, tiếng có quá nhỏ hay vỡ không | ★★★ |
| **Waveform** | Dạng sóng tiếng của một clip audio, đặt cạnh clip hình trong Viewer | Đồng bộ tay tiếng thu rời với hình | ★☆☆ |

**Ở chế độ Waveform có thêm:**

| Nút | Ở đâu | Làm gì |
|---|---|---|
| **Link/Unlink Audio** | Góc dưới phải panel | Khoá tiếng vào hình sau khi đã căn khớp |
| **Menu ⋯** | Góc trên | **Retain embedded audio** (giữ tiếng gốc của máy quay), **Retain video metadata** (giữ metadata của clip hình) |

Cách đồng bộ: xem [Đồng bộ tiếng thu rời](nap-media.md#đồng-bộ-tiếng-thu-rời-với-hình).

---

## Metadata Editor

Chi tiết cách gõ: [Metadata Editor](metadata.md).

| Nút | Ở đâu | Làm gì | Mức |
|---|---|---|---|
| **Header** | Trên cùng | Tên file, thư mục, độ dài, codec, fps, độ phân giải, tiếng. Chỉ xem | ★★☆ |
| **Metadata Presets** | Menu bên trái | Bộ trường tự tạo. Mặc định `Default` | ★☆☆ |
| **Metadata Groups** | Menu bên phải | Đổi nhóm trường: Clip Details, Shot & Scene, Camera… hoặc **All Groups** | ★★☆ |
| **Menu ⋯** | Góc trên | **Create Custom Metadata**, **Manage Custom Metadata** | ★☆☆ |
| **Save** | Đáy panel | Lưu khi sửa cho **nhiều clip** một lúc | ★★☆ |
| **Slate ID** | Trên cùng panel | Đọc chữ trên bảng clapper | `Studio` |

---

## Media Pool

Chi tiết: [Media Pool](media-pool.md) và [Bin](bin.md).

### Góc trên trái

| Nút | Làm gì | Mức |
|---|---|---|
| **Bin List** | Ẩn/hiện cột danh sách bin | ★★★ |
| **Color Tag Filter** (menu ngay bên phải Bin List) | Chỉ hiện bin có cùng màu nhãn. **Show All** để hiện lại hết | ★☆☆ |

### Dải tab

Mỗi tab là một lối tắt tới một bin. Tạo: chuột phải bin → **Open as New Tab**. Chi tiết: [Media Pool Tabs](media-pool.md#media-pool-tabs).

### Phía trên, bên phải

| Nút | Làm gì | Mức |
|---|---|---|
| **Thanh trượt cỡ thumbnail** (Icon Size) | Phóng to/thu nhỏ thumbnail | ★★☆ |
| **Menu sắp xếp** (Sort Order) | Sắp clip theo tên, timecode, độ dài, fps, ngày tạo… hoặc **Custom** để kéo tay | ★★☆ |
| **Ba nút kiểu xem** | **Thumbnail**, **List**, **Metadata** | ★★★ |
| **Kính lúp** | Mở ô tìm. Menu bên cạnh chọn tìm ở **All Bins** hay **Selected Bins**; menu **Filter By** chọn tìm theo trường nào | ★★★ |
| **Menu ⋯** | Tuỳ chọn Media Pool — bảng dưới | ★★☆ |
| **Import Blackmagic Cloud Folder** | Nối thư mục Blackmagic Cloud vào Media Pool. Cần đăng nhập Blackmagic Cloud | ★☆☆ |
| **AI Clip Analysis** | Chạy phân tích AI: IntelliSearch, Slate, Transcription, Audio Classification | `Studio` |
| **Transcribe Audio** | Chép lời thoại thành chữ | `Studio` |

**Menu ⋯ của Media Pool:**

| Mục | Làm gì | Mức |
|---|---|---|
| **Show Power Bins** | Hiện khu Power Bin (bin dùng chung mọi project) | ★★☆ |
| **Show Smart Bins** | Hiện khu Smart Bin (bin tự lọc) | ★★☆ |
| **Show Audio Waveforms** | Clip audio hiện dạng sóng thay cho ô trống | ★★☆ |
| **Deleted Timeline Backups** | Khôi phục timeline đã xoá | ★★☆ |
| **Remove Unused Clips** | Bỏ khỏi project mọi clip không nằm trên timeline nào | ★★☆ |
| **Update Usage for Entire Project** | Đếm clip được dùng bao nhiêu lần trên **mọi** timeline | ★☆☆ |
| **Export as PDF** | Xuất thumbnail của bin thành một tờ PDF | ★☆☆ |
| **IntelliSearch Mode** | Chọn Faster/Better cho tìm kiếm AI | `Studio` |

---

## Inspector

Bật bằng nút **Inspector** trên Interface Toolbar. Chọn clip trong Media Pool rồi chỉnh — thông số đi theo clip đó khi bạn đưa xuống timeline.

| Tab | Có gì | Mức |
|---|---|---|
| **Video** | Transform (Zoom, Position, Rotation, Flip), Cropping, Dynamic Zoom, Composite, Retime and Scaling. Lens Correction và Super Scale là `Studio` | ★☆☆ |
| **Audio** | Clip Volume, Clip Pan, Clip Pitch, Equalizer 6 dải | ★★☆ |
| **Image** | Thông số camera RAW (chỉ sáng khi clip là RAW) | ★☆☆ |
| **File** | Thông tin file, ô metadata gõ nhanh, **Audio Configuration**, **Timecode** | ★★☆ |

Tab nào không áp dụng cho clip đang chọn thì bị mờ.

> **Tab File là lối tắt rất tiện.** Phần **Audio Configuration** cho xem dạng sóng từng track, tắt track thừa, chọn Mono/Stereo — làm được phần lớn việc của [Clip Attributes → Audio](clip-attributes.md#tab-audio) mà trực quan hơn.

---

## Menu chuột phải — nơi chứa phần lớn lệnh

Không cần nhớ hết. Biết ba menu này có những gì là đủ.

| Chuột phải vào | Lệnh hay dùng | Xem |
|---|---|---|
| **File/thư mục trong Media Storage** | Add into Media Pool, Add Folder and SubFolders into Media Pool (Create Bins), Extract Audio, Scene Cut Detection, Set As Clone Source/Destination, Add folder to favorites | [Media Storage](media-storage.md#menu-chuột-phải-trong-media-storage) |
| **Clip trong Media Pool** | Clip Attributes, Generate Optimized/Proxy Media, Relink Selected Clips, Create Timeline Using Selected Clips, Duplicate Clip, Reveal in Finder | [Media Pool](media-pool.md#menu-chuột-phải-của-clip) |
| **Bin trong Bin List** | Add Bin, Rename Bin, Delete Bin, Color Tag, Open As New Window, Open as New Tab, Export Bin, Auto Sync Audio | [Bin](bin.md#1-bin-thường) |

---

## Undo — lùi lại

| Việc | Cách |
|---|---|
| Lùi một bước | `⌘Z` |
| Làm lại | `⇧⌘Z` |
| Lùi nhiều bước một lúc | **Edit → History** → chọn bước muốn quay về |
| Xem toàn bộ lịch sử | **Edit → History → Open History Window** |

Trang Media, Cut, Edit và Fairlight **dùng chung** một chuỗi undo. Đóng project là mất lịch sử undo.
