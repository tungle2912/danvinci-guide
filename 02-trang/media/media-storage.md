# Media Storage — duyệt ổ cứng

Vùng trên trái. Đây là trình duyệt file của Resolve, để bạn **xem trước khi nạp**.

Chia làm hai phần: **Volume List** (cột trái) và **Media Browser** (vùng phải).

## Volume List — cột ổ đĩa

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

## Media Browser — vùng xem nội dung

Ba kiểu hiển thị, chọn bằng ba icon ở góc trên vùng này: **Thumbnail · List · Metadata**.

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

Sắp cột xong rồi **lưu lại layout** để lần sau gọi ra dùng luôn.

> **Dùng List view để tìm nhanh clip hỏng:** sắp theo cột **FPS** là thấy ngay clip nào lệch frame rate so với phần còn lại. Sắp theo **Resolution** thấy clip nào quay nhầm độ phân giải.

## Xem clip mà không cần nạp

Chọn clip trong Media Storage là **phát luôn trong Viewer**, chưa cần nạp vào Media Pool. Miễn là Resolve đọc được định dạng đó.

Dùng để: xem trước footage đang cân nhắc, hoặc kiểm tra lại file vừa xuất ra.

Resolve cũng mở được **gói DCP và IMF** theo cách này — chọn gói, phát trong Viewer như clip thường.

## Live Media Preview

Mặc định **bật**. Khi bạn rê chuột ngang qua thumbnail trong Media Storage hoặc Media Pool, Viewer hiện luôn khung hình đang rê tới.

Tắt/bật ở: **menu ba chấm góc trên phải Viewer → Live Media Preview**.

Kết hợp với `I` và `O`: rê chuột trên thumbnail, bấm `I` và `O` ngay trên đó là đặt được điểm vào/ra mà không cần mở clip. Thumbnail sẽ hiện vạch đánh dấu khoảng đã chọn ở đáy.

Xoá điểm vào/ra: `⌥X`.

## Xuất một khung hình từ Viewer

1. Tua tới khung cần lấy.
2. **File → Export → Current Frame as Still**.
3. Đặt tên, chọn định dạng, bấm **Export**.

Làm được ở cả trang Media, Cut và Edit.

## Xem toàn màn hình

**Workspace → Viewer Mode → Cinema Viewer** (`⌘F`). Bấm lại để thoát.
