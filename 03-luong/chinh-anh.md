# Chỉnh ảnh tĩnh và ảnh RAW

> **Từ bản 21, Resolve có hẳn trang [Photo](../02-trang/photo/README.md) chuyên chỉnh ảnh** — album, chấm sao, tab RAW với cân bằng trắng và phơi sáng, xuất JPEG/PNG/HEIC/TIFF. **Với ảnh, hãy dùng trang Photo trước.**
>
> Trang này mô tả cách chỉnh ảnh bằng trang **Color** — dùng khi bạn cần công cụ chỉnh từng vùng (Qualifier, Power Window), hoặc khi ảnh nằm chung timeline với video.

Resolve không phải Lightroom, nhưng trang Color của nó mạnh hơn phần lớn phần mềm chỉnh ảnh. Dùng được cho ảnh tĩnh, nhất là khi bạn muốn ảnh và video trong cùng dự án có tông màu giống nhau.

## Nạp ảnh

Kéo file ảnh vào Media Pool như clip video. Resolve đọc được JPEG, PNG, TIFF, DPX, EXR và **RAW của nhiều máy** (CR2/CR3 của Canon, NEF của Nikon, ARW của Sony, DNG).

Độ dài mặc định của ảnh trên timeline đặt ở **Preferences → User → Editing → Standard still duration**.

## Ảnh RAW — bảng Camera Raw

Đây là lợi thế lớn nhất khi chỉnh ảnh RAW trong Resolve.

Sang trang Color, mở palette **Camera Raw** (icon hình máy ảnh ở hàng palette). Đổi **Decode Using** từ *Clip* sang **Project** hoặc *Clip* để mở khoá các thanh chỉnh.

Các thanh ở đây tác động lên **dữ liệu RAW gốc trước khi khử bayer**, nghĩa là chất lượng cao hơn hẳn so với chỉnh sau đó:

| Thanh | Làm gì |
|---|---|
| **Color Temp** | Nhiệt độ màu, chỉnh ở đây tốt hơn chỉnh bằng bánh xe |
| **Tint** | Ngả xanh lá / hồng tím |
| **Exposure** | Phơi sáng, tính theo stop |
| **Highlights / Shadows** | Kéo lại vùng cháy và vùng tối |
| **Color Boost** | Tăng độ sặc ở những chỗ còn nhạt |
| **Midtone Detail** | Độ nét ở vùng trung gian |

**Làm hết mọi chỉnh sửa về phơi sáng và cân bằng trắng ở đây trước**, rồi mới sang các node.

## Chuỗi node cho ảnh

Ảnh cần ít node hơn video:

```
01 Balance      cân bằng trắng, điểm đen/trắng
02 Contrast     đường cong chữ S
03 Color        hue vs hue, hue vs sat
04 Local        power window cho vùng cần sáng/tối riêng
05 Look         tông màu
06 Sharpen      blur radius < 0.5
```

## Những công cụ hợp với ảnh

### Power Window + Tracker không cần
Ảnh tĩnh nên không cần tracking. Vẽ window là xong.

### Curves
Mạnh hơn Lightroom ở **Hue vs Hue** và **Hue vs Sat** — đổi riêng một màu mà không đụng màu khác, mịn hơn công cụ HSL thông thường.

### Qualifier
Tách vùng theo màu chính xác hơn công cụ chọn màu của phần mềm ảnh, vì có cả vùng lõi và vùng mềm cho từng kênh H, S, L.

### Color Warper
Rất hợp để chỉnh tông da. Chế độ **Chroma–Luminance** cho phép kéo riêng độ sặc của vùng sáng hoặc tối.

### Sizing
**Output Sizing** để crop và xoay. Có cả **Flip**.

## Xuất ảnh

Ba cách:

**Cách 1 — Grab Still rồi export** (nhanh, dùng cho xem nhanh):
Ở trang Color bấm `⌥⌘G`, rồi trong Gallery chuột phải still → **Export**. Chọn PNG, TIFF hoặc JPEG.

**Cách 2 — Deliver, định dạng ảnh chuỗi** (chất lượng cao nhất):
Sang Deliver, ở **Format** chọn **TIFF** / **PNG** / **JPEG**, đặt **Render → Individual clips**, rồi đặt điểm `I`/`O` quanh đúng khung cần xuất.

**Cách 3 — Export Frame từ viewer:**
Chuột phải vào Viewer → **Grab Still** rồi export, hoặc **File → Export → Export Current Frame as Still**.

Muốn giữ nguyên độ phân giải gốc của ảnh, nhớ đặt **Timeline resolution** bằng đúng kích thước ảnh, nếu không Resolve sẽ thu ảnh về cỡ timeline.

## Khi nào đừng dùng Resolve cho ảnh

- Cần xử lý hàng loạt vài trăm ảnh → Lightroom nhanh hơn nhiều.
- Cần retouch, xoá vật thể, ghép ảnh → Photoshop hoặc Affinity.
- Cần quản lý thư viện ảnh → Resolve không có chức năng này.

Dùng Resolve cho ảnh khi: bạn cần tông màu khớp với video trong cùng dự án, hoặc cần các công cụ tách màu mà phần mềm ảnh không có.
