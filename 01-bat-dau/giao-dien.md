# Tám trang và vai trò

DaVinci Resolve không có một giao diện duy nhất. Nó chia thành **tám trang** (page), mỗi trang là một phòng ban riêng với bộ công cụ riêng.

> Từ bản 21, Resolve có thêm trang **Photo** chuyên cho ảnh tĩnh. Nhiều tài liệu cũ trên mạng — và cả vài đoạn trong manual chính thức — vẫn ghi "bảy trang".

![Tám trang](../assets/diagrams/pages.svg)

## Dãy icon đổi trang

Nằm ở **đáy cửa sổ**. Icon đang sáng là trang hiện tại.

![Dãy icon đổi trang ở đáy cửa sổ Resolve](../assets/img/page-cut.png)

*Ảnh chụp Resolve 21 trên macOS, đang ở trang Cut (icon thứ 3, gạch đỏ bên dưới).*

| # | Icon | Trang |
|---|---|---|
| 1 | Chồng ảnh | **Media** |
| 2 | Máy ảnh | **Photo** |
| 3 | Dải phim có tia tốc độ | **Cut** |
| 4 | Các thanh xếp ngang | **Edit** |
| 5 | Đũa phép | **Fusion** |
| 6 | Vòng tròn chấm | **Color** |
| 7 | Nốt nhạc | **Fairlight** |
| 8 | Tên lửa | **Deliver** |

Muốn thấy cả chữ bên cạnh icon: chuột phải vào dãy icon → **Show Icons and Labels**.

## Phím tắt đổi trang

| Phím | Đi tới | Chắc chắn? |
|---|---|---|
| `⇧1` | Project Manager | Có — theo manual |
| `⇧9` | Project Settings | Có — theo manual |
| `⇧2` … `⇧8` | Các trang | Xem lưu ý dưới |

Manual ghi `⇧2` tới `⇧8` dành cho các trang — nhưng câu đó viết từ khi Resolve còn bảy trang. Với tám trang ở bản 21, cách gán phím có thể đã đổi.

**Cách kiểm tra chắc chắn trên máy bạn:** mở menu **Workspace → Switch to Page**. Phím tắt của từng trang hiện ngay bên phải tên trang.

Nếu thứ tự không đổi so với bản cũ thì là: `⇧2` Media · `⇧3` Cut · `⇧4` Edit · `⇧5` Fusion · `⇧6` Color · `⇧7` Fairlight · `⇧8` Deliver.

## Mỗi trang làm gì

| Trang | Làm gì | Bạn sẽ dùng |
|---|---|---|
| [**Media**](../02-trang/media/README.md) | Nạp file, sắp xếp bin, gõ metadata, backup thẻ nhớ | Đầu mỗi dự án |
| **Photo** | Quản lý và chỉnh ảnh tĩnh: album, chấm sao, chụp tethered, xuất ảnh | Nếu bạn làm ảnh |
| [**Cut**](../02-trang/cut/README.md) | Dựng nhanh, ít nút, nhiều tự động | Video ngắn, deadline gấp |
| [**Edit**](../02-trang/edit/README.md) | Dựng chi tiết, nhiều track, keyframe | Phần lớn thời gian |
| [**Fusion**](../02-trang/fusion/README.md) | VFX dạng node: phông xanh, tracking, chữ động phức tạp | Khi cần hiệu ứng |
| [**Color**](../02-trang/color/README.md) | Chỉnh màu bằng node | Mọi video |
| [**Fairlight**](../02-trang/fairlight/README.md) | Mix âm thanh: EQ, nén, hiệu ứng | Mọi video có lời |
| [**Deliver**](../02-trang/deliver/README.md) | Xuất file | Cuối mỗi dự án |

**Cut và Edit dùng chung một timeline.** Dựng ở Cut rồi sang Edit sửa tiếp được, và ngược lại.

**Photo là luồng riêng.** Ảnh trong album của trang Photo đưa sang được các trang Cut, Edit, Color, Fusion để dùng trong video.

## Ẩn bớt trang không dùng

Không làm ảnh thì trang Photo chỉ tổ chật mắt. Vào **Workspace → Show Page** rồi bỏ tick những trang không cần.

Hiệu ứng đã áp ở trang bị ẩn **vẫn hoạt động bình thường**, chỉ là nút bấm biến mất. Vẫn vào được bằng phím tắt hoặc **Workspace → Switch to Page**.

Gọn hơn nữa:
- Chuột phải dãy icon → **Show Icons Only** — chỉ hiện icon, không chữ.
- **Workspace → Show Page Navigation** bỏ tick — ẩn hẳn dãy icon, chỉ đổi trang bằng phím tắt.

## Ba panel xuất hiện ở nhiều trang

| Panel | Là gì |
|---|---|
| **Media Pool** | Kho clip của project — cùng một kho ở mọi trang |
| **Inspector** | Thông số của thứ đang chọn |
| **Mixer** | Các kênh âm thanh |

Panel nào cũng kéo tách ra thành cửa sổ rời được — tiện khi dùng hai màn hình.

## Nút ở góc dưới phải

| Nút | Làm gì |
|---|---|
| **Ngôi nhà** | Mở Project Manager |
| **Bánh răng** | Mở Project Settings |
