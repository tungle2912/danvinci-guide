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

| Trang | Làm gì | Bạn sẽ dùng | Giao diện chi tiết | Đọc tiếp |
|---|---|---|---|---|
| [**Media**](../02-trang/media/README.md) | Nạp file, sắp xếp bin, gõ metadata, backup thẻ nhớ | Đầu mỗi dự án | [Năm vùng của trang Media](../02-trang/media/README.md#năm-vùng-của-trang-media) | [Nạp media](../02-trang/media/nap-media.md), [Bin](../02-trang/media/bin.md), [Clone Tool](../02-trang/media/clone-tool.md) |
| [**Photo**](../02-trang/photo/README.md) | Quản lý và chỉnh ảnh tĩnh: album, chấm sao, chụp tethered, xuất ảnh | Nếu bạn làm ảnh | [Giao diện Photo](../02-trang/photo/giao-dien.md) | [Chỉnh ảnh](../02-trang/photo/chinh-anh.md), [Xuất ảnh](../02-trang/photo/xuat-anh.md) |
| [**Cut**](../02-trang/cut/README.md) | Dựng nhanh, ít nút, nhiều tự động | Video ngắn, deadline gấp | [Giao diện Cut](../02-trang/cut/giao-dien.md) | [6 nút edit](../02-trang/cut/dung-clip.md), [Trim](../02-trang/cut/trim.md), [Quick Export](../02-trang/cut/kiem-tra-va-xuat.md#quick-export) |
| [**Edit**](../02-trang/edit/README.md) | Dựng chi tiết, nhiều track, keyframe, phụ đề | Phần lớn thời gian | [Giao diện Edit](../02-trang/edit/giao-dien.md) | [Cắt, trim](../02-trang/edit/dung-va-cat.md), [Inspector](../02-trang/edit/inspector.md), [Phụ đề](../02-trang/edit/phu-de.md) |
| [**Fusion**](../02-trang/fusion/README.md) | Hiệu ứng dạng node: chữ động, ghép lớp, phông xanh, tracking | Khi trang Edit không làm được | [Giao diện Fusion](../02-trang/fusion/giao-dien.md) | [Node cơ bản](../02-trang/fusion/node-co-ban.md), [Chữ động](../02-trang/fusion/chu-dong.md), [Mask, Tracker, Keyer](../02-trang/fusion/mask-tracker-keyer.md) |
| [**Color**](../02-trang/color/README.md) | Chỉnh màu bằng node | Mọi video | [Giao diện Color](../02-trang/color/giao-dien.md) | [Cân bằng](../02-trang/color/can-bang.md), [Node](../02-trang/color/node.md), [LUT, quản lý màu](../02-trang/color/lut-va-quan-ly-mau.md) |
| [**Fairlight**](../02-trang/fairlight/README.md) | Mix âm thanh: làm sạch giọng, cân to nhỏ, đo loudness | Mọi video có lời | [Giao diện Fairlight](../02-trang/fairlight/giao-dien.md) | [Làm sạch giọng](../02-trang/fairlight/lam-sach-giong.md), [Mixer, Ducker](../02-trang/fairlight/mixer-va-track-fx.md), [Loudness](../02-trang/fairlight/loudness-va-xuat.md) |
| [**Deliver**](../02-trang/deliver/README.md) | Xuất file, xếp hàng đợi render | Cuối mỗi dự án | [Giao diện Deliver](../02-trang/deliver/giao-dien.md) | [Preset theo nền tảng](../02-trang/deliver/preset-theo-nen-tang.md), [Cài đặt xuất](../02-trang/deliver/cai-dat-xuat.md), [Lỗi khi xuất](../02-trang/deliver/render-queue-va-loi.md#render-xong-mà-file-lỗi) |

**Cut và Edit dùng chung một timeline.** Dựng ở Cut rồi sang Edit sửa tiếp được, và ngược lại.

**Fusion, Color, Fairlight cũng làm trên chính timeline đó.** Comp Fusion và grade màu dính theo từng clip; chỉnh tiếng ở Fairlight thì quay về Edit vẫn thấy.

**Thứ tự xử lý hình:** Edit → Fusion → Color. Vì vậy Viewer trang Fusion hiện hình **chưa chỉnh màu** — xem [Fusion làm việc thế nào](../02-trang/fusion/README.md#fusion-làm-việc-thế-nào).

**Photo là luồng riêng.** Album của trang Photo đưa sang trang Color, Fusion để chỉnh tiếp; muốn dùng ảnh trong video thì xuất ra file rồi nạp lại. Xem [Photo → Đưa album sang trang Color](../02-trang/photo/xuat-anh.md#đưa-album-sang-trang-color).

## Một video đi qua các trang thế nào

| Bước | Trang | Đọc |
|---|---|---|
| 1. Tạo project, nạp footage | Media | [Tạo project](tao-du-an.md), [Nạp media](../02-trang/media/nap-media.md) |
| 2. Dựng | Cut hoặc Edit | [Đưa clip xuống, cắt, trim](../02-trang/edit/dung-va-cat.md) |
| 3. Chữ, phụ đề | Edit, Fusion | [Phụ đề](../02-trang/edit/phu-de.md), [Chữ động Text+](../02-trang/fusion/chu-dong.md) |
| 4. Màu | Color | [Chuỗi 6 node](../02-trang/color/node.md#chuỗi-6-node-cơ-bản) |
| 5. Tiếng | Fairlight | [Một lượt cân tiếng vlog](../02-trang/fairlight/README.md#một-lượt-cân-tiếng-vlog) |
| 6. Xuất | Deliver | [Preset theo nền tảng](../02-trang/deliver/preset-theo-nen-tang.md) |

Bước 2 đến 5 không bắt buộc đúng thứ tự — quay lại trang trước bất cứ lúc nào. Luồng đầy đủ: [Vlog YouTube](../03-luong/vlog-youtube.md).

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
| **Inspector** | Thông số của thứ đang chọn. Xem [Inspector trang Edit](../02-trang/edit/inspector.md) |
| **Mixer** | Các kênh âm thanh — ở Fairlight có thêm EQ, Dynamics, Track FX. Xem [Cột kênh trong Mixer](../02-trang/fairlight/mixer-va-track-fx.md#cột-kênh-trong-mixer) |

Panel nào cũng kéo tách ra thành cửa sổ rời được — tiện khi dùng hai màn hình.

## Nút ở góc dưới phải

| Nút | Làm gì |
|---|---|
| **Ngôi nhà** | Mở Project Manager |
| **Bánh răng** | Mở Project Settings |

Thiết lập nên làm ngay khi tạo project: [Tạo project đúng ngay từ đầu](tao-du-an.md).
