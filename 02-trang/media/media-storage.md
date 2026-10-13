# Media Storage — duyệt ổ cứng

Vùng trên trái. Đây là trình duyệt file của Resolve, để bạn **xem trước khi nạp**.

Chia làm hai phần: **Volume List** (cột trái) và **Media Browser** (vùng phải).

Ẩn/hiện cột Volume List: nút ở **góc trên trái** Media Storage. Ẩn cả Media Storage: nút **Media Storage** trên Interface Toolbar.

## Volume List — cột ổ đĩa

`★★★ Hằng ngày`

Liệt kê mọi ổ đang gắn vào máy. Ba nhóm:

### Scratch volumes
Nằm trên cùng, có **thanh số % dung lượng đã dùng** bên phải tên ổ. Đây là các ổ bạn đã khai báo ở **Preferences → System → Media Storage**.

> **Ổ trên cùng trong danh sách scratch là nơi Resolve lưu Gallery stills và cache files.** Nếu máy lag khi chỉnh màu, kiểm tra xem ổ này có phải SSD không.

### Available volumes
Có icon hình đĩa. Mọi ổ cố định, ổ rời và ổ mạng đang gắn.

Bấm tam giác bên trái tên ổ để mở ra cây thư mục con, đi sâu bao nhiêu cấp cũng được.

**Ổ không hiện ra?** Chuột phải vào vùng trống của Volume List → **Add New Location**, rồi trỏ tới ổ đó.

Bật hiện tự động: **Preferences → System → Media Storage → Automatically display attached local and network storage locations**.

> Nếu bạn cài Resolve từ **Mac App Store**, tính năng tự gắn ổ **mặc định tắt**. Phải bật tay ở chỗ trên.

### Favorites
Nằm dưới cùng. Dành cho thư mục bạn hay vào, khỏi phải lần mò cây thư mục mỗi lần.

| Việc | Cách |
|---|---|
| Thêm | Chuột phải thư mục trong Volume List → **Add folder to favorites** |
| Mở | Bấm vào favorite đó |
| Bỏ | Chuột phải favorite → **Remove folder from favorites** |

**Ví dụ:** bạn luôn đổ footage vào `/Volumes/SSD/Footage`. Thêm thư mục này vào Favorites. Lần sau chỉ một cú bấm.

> **Lối tắt từ Finder:** kéo một thư mục trong Finder thả vào Media Storage. Media Storage nhảy thẳng tới đúng thư mục đó.

---

## Media Browser — vùng xem nội dung

Ba kiểu hiển thị, chọn bằng ba icon ở góc trên vùng này: **Thumbnail · List · Metadata**.

| Kiểu | Hợp khi | Mức |
|---|---|---|
| **Thumbnail** | Nhìn hình để chọn cảnh | ★★★ |
| **List** | Lọc theo thông số kỹ thuật: fps, độ phân giải, codec | ★★☆ |
| **Metadata** | Thumbnail kèm vài dòng thông tin | ★☆☆ |

### Thumbnail view

`★★★ Hằng ngày`

- **Rê chuột ngang thumbnail** là xem nhanh nội dung clip.
- **Mũi tên Clip Info** ở góc dưới phải thumbnail: bấm để xem nhanh tên file, timecode vào/ra, độ dài, độ phân giải, fps, tỉ lệ điểm ảnh, codec, ngày tạo, cờ (flag).
- **Menu sắp xếp** (nằm giữa ô tìm kiếm và menu ⋯): sắp thumbnail theo File Name, Reel Name, Start TC, FPS, Audio Ch… tăng hoặc giảm.

### List view — các cột

Kiểu này mạnh nhất vì bạn **lọc footage trước khi nạp**. Các cột có sẵn:

| Cột | Nội dung |
|---|---|
| **File name** | Tên file |
| **Reel name** | Tên cuộn, lấy theo Conform Options trong Project Settings |
| **Start TC** | Timecode đầu |
| **Start / End** | Khung đầu / khung cuối |
| **Frames** | Độ dài tính bằng khung |
| **Resolution** | Kích thước khung hình |
| **Bit Depth** | Độ sâu màu |
| **Video Codec** | Codec hình |
| **Audio Codec** | Codec tiếng |
| **FPS** | Frame rate |
| **Audio Ch** | Số kênh tiếng |
| **Date Created / Modified** | Ngày tạo / sửa |
| **Shot / Scene / Take / Angle** | Metadata từ máy quay nếu có |
| **Good Take** | Đánh dấu take dùng được |

Thao tác với cột:

| Việc | Cách |
|---|---|
| Hiện/ẩn cột | Chuột phải vào **tiêu đề cột bất kỳ** → tick/bỏ tick |
| Đổi thứ tự cột | Kéo tiêu đề cột sang trái/phải |
| Đổi độ rộng | Kéo đường viền giữa hai cột |
| Sắp xếp | Bấm tiêu đề cột. Bấm lần nữa để đảo chiều tăng/giảm |

Sắp cột xong rồi **lưu lại layout** để lần sau gọi ra dùng luôn:

| Việc | Cách |
|---|---|
| Lưu | Chuột phải tiêu đề cột → **Create Column Layout** → đặt tên → **OK** |
| Gọi lại | Chuột phải tiêu đề cột → chọn tên layout (nằm đầu danh sách) |
| Xoá | Chuột phải tiêu đề cột → **Delete Column Layout** → chọn tên |

> **Dùng List view để tìm nhanh clip hỏng:** sắp theo cột **FPS** là thấy ngay clip nào lệch frame rate so với phần còn lại. Sắp theo **Resolution** thấy clip nào quay nhầm độ phân giải.

### Chuỗi ảnh — Frame Display Mode

`★☆☆ Tình huống cụ thể`

Ảnh đánh số liên tiếp (`IMG_0001.jpg`, `IMG_0002.jpg`…) có thể bị gom thành **một clip**. Đổi cách hiện ở **menu ⋯ của Media Storage → Frame Display Mode**:

| Chế độ | Hiện thế nào |
|---|---|
| **Auto** | Resolve tự quyết theo loại file. DPX, EXR thành clip; JPG thành ảnh lẻ |
| **Individual** | Mỗi ảnh một file riêng |
| **Sequence** | Gom mọi ảnh đánh số liên tiếp thành clip, bất kể loại file |

---

## Menu chuột phải trong Media Storage

Phần lớn việc nạp media nằm ở đây. Chuột phải vào **file** hoặc **thư mục**:

| Lệnh | Làm gì | Mức |
|---|---|---|
| **Add into Media Pool** | Nạp file đang chọn vào bin đang mở | ★★★ |
| **Add Folder into Media Pool** | Nạp file trong thư mục. **Bỏ qua** thư mục con | ★★☆ |
| **Add Folder and SubFolders into Media Pool** | Nạp cả thư mục con, dồn hết vào **một** bin | ★★☆ |
| **Add Folder and SubFolders into Media Pool (Create Bins)** | Nạp cả cây, **mỗi thư mục thành một bin** | ★★★ |
| **Extract Audio** | Tách tiếng của clip ra file `.wav` riêng | ★☆☆ |
| **Scene Cut Detection** | Cắt một file video đã dựng sẵn thành từng cảnh | ★☆☆ |
| **Set As Clone Source / Set As Clone Destination** | Đưa thư mục vào [Clone Tool](clone-tool.md) | ★★☆ |
| **Add As Offline Clip** | Nạp làm video tham chiếu để so với bản dựng | ★☆☆ |
| **Add to Media Pool as a Matte** | Gắn file matte cho clip, dùng ở trang Color | ★☆☆ |
| **Add folder to favorites** | Thêm vào Favorites | ★★☆ |
| **Add New Location** | (vùng trống Volume List) thêm ổ không tự hiện | ★☆☆ |

Các lệnh nâng cao hơn (Add Folder Based on EDLs, Split and add into Media Pool, Add Folder with Source Offset) dành cho quy trình conform EDL, người mới không cần.

Cách dùng từng lệnh nạp: [Nạp media](nap-media.md).

---

## Xem clip mà không cần nạp

`★★★ Hằng ngày`

Chọn clip trong Media Storage là **phát luôn trong Viewer**, chưa cần nạp vào Media Pool. Miễn là Resolve đọc được định dạng đó.

Dùng để: xem trước footage đang cân nhắc, hoặc kiểm tra lại file vừa xuất ra.

Resolve cũng mở được **gói DCP và IMF** theo cách này — chọn gói, phát trong Viewer như clip thường.

> **Kiểm tra file vừa xuất:** mở thư mục xuất trong Media Storage, chọn file, phát. Bật **Workspace → Dual Screen → On** nếu có màn phụ — màn phụ hiện cả bộ scope để soi.

---

## Live Media Preview

`★★★ Hằng ngày`

Mặc định **bật**. Khi bạn rê chuột ngang qua thumbnail trong Media Storage hoặc Media Pool, Viewer hiện luôn khung hình đang rê tới.

Tắt/bật ở: **menu ba chấm góc trên phải Viewer → Live Media Preview**.

Kết hợp với `I` và `O`: rê chuột trên thumbnail, bấm `I` và `O` ngay trên đó là đặt được điểm vào/ra mà không cần mở clip. Thumbnail sẽ hiện vạch đánh dấu khoảng đã chọn ở đáy.

Xoá điểm vào/ra: `⌥X`.

> **Thấy rối mắt?** Tắt Live Media Preview. Khi đó Viewer chỉ đổi khi bạn bấm chọn clip.

---

## Xuất một khung hình từ Viewer

`★★☆ Thường dùng`

**Dùng khi:** cần ảnh thumbnail YouTube, ảnh minh hoạ, hoặc gửi khách xem một khung.

1. Tua tới khung cần lấy.
2. **File → Export → Current Frame as Still**.
3. Đặt tên, chọn định dạng, bấm **Export**.

Làm được ở cả trang Media, Cut và Edit.

---

## Xem toàn màn hình

**Workspace → Viewer Mode → Cinema Viewer** (`⌘F`). Bấm lại để thoát.
