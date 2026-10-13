# Bảng phím tắt

Chỉ gồm **phím hay dùng**. Mọi phím đều đối chiếu với **DaVinci Resolve Manual** bản gốc.

Phím theo macOS. Windows/Linux: đổi `⌘` → `Ctrl`, `⌥` → `Alt`.

> Tự đổi phím: `⌘⌥K`. Có preset cho người quen Premiere Pro, Final Cut Pro 7, Avid.

## Toàn cục

| Phím | Làm gì |
|---|---|
| `⇧1` | Project Manager |
| `⇧9` | Project Settings |
| `⇧D` | Tắt/bật toàn bộ chỉnh màu và Fusion — so sánh trước/sau, phát mượt hơn |
| `⌘Z` / `⌘⇧Z` | Hoàn tác / làm lại |
| `⌘S` | Lưu |
| `⌘I` | Import Media |
| `⌘F` | Viewer toàn màn hình |

**Đổi trang:** manual ghi `⇧2`…`⇧8`, nhưng câu đó viết từ khi Resolve còn 7 trang. Bản 21 có 8 trang (thêm Photo), nên xem phím chính xác ở **Workspace → Switch to Page**, hoặc bấm icon ở đáy cửa sổ.

## Phát và điều hướng

| Phím | Làm gì |
|---|---|
| `Space` | Phát / dừng |
| `J` `K` `L` | Lùi / dừng / tiến — bấm nhiều lần để nhanh hơn |
| `←` `→` | Từng khung |
| `⇧←` `⇧→` | Từng giây |
| `↑` `↓` | Điểm cắt trước / sau |
| `I` `O` | Điểm vào / ra |
| `⌥X` | Xoá điểm vào và ra |
| `M` | Marker. Bấm lần nữa để ghi chú |

## Edit và Cut

| Phím | Làm gì |
|---|---|
| `A` / `T` / `B` | Chế độ Selection / Trim / Blade |
| `W` | Dynamic Trim — trim bằng `J` `K` `L` |
| `N` | Nam châm |
| `F9` / `F10` / `F11` / `F12` | Insert / Overwrite / Replace / Place On Top |
| `⇧F10` | Ripple Overwrite — thay cảnh, độ dài timeline tự đổi theo |
| `⇧F11` | Fit to Fill — co giãn tốc độ cho vừa khoảng `I` `O` |
| `⇧F12` | Append — nối vào cuối |
| `⌘B` | Cắt tại con trỏ (Razor) |
| `⌘\` | Cắt tại con trỏ (Split Clip) |
| `Delete` | Xoá, **để lại khoảng trống** |
| `Fn` + `Delete` | Xoá, **phần sau dồn lên** |
| `⌘T` | Chuyển cảnh mặc định |
| `⌘R` | Bảng tốc độ (Retime) |
| `⇧R` | Freeze Frame — dừng hình tại con trỏ |
| `G` | Gắn flag cho clip |
| `,` `.` | Dịch clip/mép đang chọn một khung |
| `⌘⇧L` | Bật/tắt Linked Selection |
| `⌥⌘L` | Tách hẳn hình và tiếng của clip |
| `⇧Z` | Thu timeline vừa khung |
| `⌘=` `⌘−` | Phóng to / thu nhỏ timeline |
| `⌥1`…`⌥8` | Chọn track hình đích |

Giữ `⌥` khi bấm clip: tạm chọn riêng hình hoặc riêng tiếng.

## Color

| Phím | Làm gì |
|---|---|
| `⌥S` | Thêm node sau |
| `⇧S` | Thêm node trước |
| `⌥O` | Node Outside — vùng ngược lại |
| `⌥C` | Node có sẵn khung tròn |
| `⌘D` | Tắt/bật node đang chọn |
| `⌥D` | Tắt/bật mọi node của clip |
| `⇧Home` | Reset node |
| `⌥⌘G` | Grab Still — lưu grade |
| `⌘W` | Bật/tắt wipe so sánh với still |
| `=` | Copy grade từ clip ngay trước |
| `−` | Copy grade từ clip cách hai clip trước |
| `⇧H` | Xem vùng Qualifier đã chọn |
| `⌥⇧H` | Xem vùng chọn dạng đen trắng |
| Click chuột giữa | Copy grade từ clip đó sang clip đang chọn |

## Photo

| Phím | Làm gì |
|---|---|
| `1`–`5`, `0` | Chấm sao, xoá sao |
| `S` / `X` | Tag tốt / loại |
| `⌘[` `⌘]` | Xoay trái / phải |
| `⌘R` | Reset tab Photo *(Inspector đang chọn)* |
| `⌘⇧R` | Reset tất cả *(Inspector đang chọn)* |
| Giữ `H` | Kéo ảnh trong Viewer |

## Fusion

Phím Fusion **phụ thuộc panel đang chọn** — bấm vào Viewer hay Node Editor trước rồi mới bấm phím. Xem [Giao diện Fusion](../02-trang/fusion/giao-dien.md).

**Node** — xem [Node cơ bản](../02-trang/fusion/node-co-ban.md#xoá-tắt-tạm-khoá-node):

| Phím | Làm gì |
|---|---|
| `⇧Space` | Thêm node — gõ tên, `Return` |
| `1` / `2` | Đưa node đang chọn lên Viewer trái / phải. Bấm lại để gỡ |
| `Delete` | Xoá node, hai node hai bên tự nối lại |
| `⌘P` | Tắt tạm node (Pass Through) |
| `⌘L` | Khoá node |
| `⌘U` | Ngừng cập nhật node |
| `⌘T` | Đảo Background và Foreground của Merge |
| `F2` | Đổi tên node (bấm vào thanh tên ở đầu Inspector trước) |
| `⌘C` / `⌘V` / `⌘X` | Copy / dán / cắt node |
| `⌘A` | Chọn mọi node |
| `V` | Bật/tắt bản đồ thu nhỏ Node Editor |
| Giữ `⇧` khi kéo node | Chèn vào đường nối, hoặc tách khỏi chuỗi |

**Viewer và phát:**

| Phím | Làm gì |
|---|---|
| `F` | Vừa khít khung |
| `⌘1` / `⌘2` | Zoom 100% / 200% (Node Editor: `⌘1` về cỡ mặc định) |
| `=` / `-` | Phóng to / thu nhỏ Viewer |
| `A` | Xem kênh alpha |
| `C` | Đổi qua lại giữa màu và alpha |
| `Space`, `J` `K` `L` | Phát / dừng, phát lùi, phát tới |
| `⇧←` `⇧→` | Về khung đầu / cuối của clip |
| `⌘←` `⌘→` | Về đầu / cuối vùng render |
| `⌥[` `⌥]` | Keyframe trước / sau |

**Mask Polygon, Tracker** — xem [Polygon](../02-trang/fusion/mask-tracker-keyer.md#polygon), [Tracker](../02-trang/fusion/mask-tracker-keyer.md#bước-2--track):

| Phím | Làm gì |
|---|---|
| `⇧C` / `⇧I` / `⇧D` | Click Append / Insert and Modify / Draw Append |
| `⇧M` / `⇧N` | Modify Only / Done |
| `⇧O` | Khép / mở hình |
| `Tab` / `⇧Tab` | Chuyển giữa các hình |
| `Esc` | Dừng Tracker đang track |

**Spline Editor** — xem [Keyframe và Spline](../02-trang/fusion/keyframe-va-spline.md#thao-tác-cơ-bản):

| Phím | Làm gì |
|---|---|
| `⌘K` | Thêm keyframe tại con trỏ |
| `⇧S` | Smooth — chậm dần, mượt |
| `T` | Ease In/Out bằng số |
| `⌘F` | Vừa khít mọi đường |

## Fairlight

Xem [Sửa clip trên timeline Fairlight](../02-trang/fairlight/thu-am-va-chinh-clip.md#sửa-clip-trên-timeline-fairlight).

| Phím | Làm gì |
|---|---|
| `⌘B` / `⌘\` | Cắt tại con trỏ (Razor / Split Clip) |
| `⇧[` / `⇧]` | Trim Start / Trim End về con trỏ |
| `⇧⌘T` | Trim to Selection |
| `⌘⌥E` | Smart Zoom — phóng to track đang chọn. Bấm lại để trở về |
| Giữ `⌘⌥` + lăn chuột | Phóng to sóng âm (chỉ để nhìn) |
| `F4` | Đổi giữa xem clip và xem automation |
| Giữ `⌥` + bấm đường gain | Thêm keyframe gain / automation |
| Giữ `⌘⌥` + bấm keyframe | Xoá keyframe |
| Giữ `⇧` khi kéo fader | Chỉnh mịn từng 0,1 dB |
| `⌘F` | Cinema Viewer — soát tiếng khớp môi |

## Deliver

| Phím | Làm gì |
|---|---|
| `I` / `O` | Chỉ xuất một đoạn — xem [Xuất một đoạn](../02-trang/deliver/render-queue-va-loi.md#xuất-một-đoạn) |
| `⇧Z` | Thu timeline vừa khung |
| Giữ `C` + rê chuột | Tua lướt trên Viewer |
| `⌘`-bấm / `⇧`-bấm job | Chọn vài job rời / cả dãy trong Render Queue |
