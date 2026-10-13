# Hiệu ứng ảnh

Mở bằng nút **Effects Library** trên toolbar. Kho hiệu ứng chia theo nhóm.

Trang Photo chỉ hiện **một nhóm hiệu ứng đã chọn lọc** cho ảnh tĩnh. Muốn dùng toàn bộ kho ResolveFX thì [đưa album sang trang Color](xuat-anh.md#đưa-album-sang-trang-color).

---

## Xem trước, áp, chỉnh

### Xem trước

Rê chuột ngang qua thumbnail hiệu ứng — Viewer hiện ngay kết quả trên ảnh đang chọn với thông số mặc định. Không cần áp thật.

Nếu không thấy xem trước: menu ba chấm của Effects → tick **Hover Scrub Preview**.

### Tìm hiệu ứng

Gõ vào ô tìm kiếm trên đầu Effects Library. Hoặc bấm `⇧Space` để mở hộp tìm nhanh — bấm đúp kết quả là áp luôn vào ảnh đang chọn.

Tìm được cả theo **tên nhóm**: gõ `Stylize` ra mọi hiệu ứng trong nhóm Stylize.

### Áp hiệu ứng

| Cho | Cách |
|---|---|
| Một ảnh | Kéo thumbnail hiệu ứng thả lên ảnh trong album. Hoặc chọn ảnh rồi bấm đúp hiệu ứng |
| Nhiều ảnh | Chọn các ảnh (`⌘`+click từng ảnh, `⇧`+click một dãy, `⌘A` tất cả) rồi bấm đúp hiệu ứng |

Áp bao nhiêu hiệu ứng lên một ảnh cũng được.

### Chỉnh thông số

**Inspector → tab Effects**. Mọi hiệu ứng đã áp **xếp chồng từ trên xuống dưới** và chạy theo đúng thứ tự đó.

Đổi thứ tự: bấm **mũi tên lên/xuống** cạnh tên hiệu ứng.

> **Thứ tự quan trọng.** Làm nét rồi mới làm mờ viền khác với làm mờ viền rồi mới làm nét. Nguyên tắc chung: hiệu ứng sửa ảnh (sharpen, giảm nhiễu) đặt **trên**, hiệu ứng tạo không khí (vignette, glow) đặt **dưới**.

### Gỡ hiệu ứng

| Gỡ | Cách |
|---|---|
| Một vài hiệu ứng | Chuột phải ảnh → **Remove Attributes** → tick hiệu ứng cần gỡ → **Apply** |
| Mọi hiệu ứng | `⇧R` (Inspector đang được chọn) |

### Hiệu ứng yêu thích

Bấm **ngôi sao nhỏ** trên thumbnail, hoặc chuột phải → **Add to Favorites**. Hiệu ứng hiện ở tab **Favorites** của Effects Library.

> Favorite chỉ lưu **hiệu ứng**, không lưu thông số bạn đã chỉnh. Áp lại sẽ về mặc định.

---

## Hiệu ứng nào dùng được ở bản free

Danh sách dưới đối chiếu với nhãn trong manual cho toàn bộ ResolveFX. Không phải hiệu ứng nào cũng có mặt trong kho đã chọn lọc của trang Photo.

### Dùng được ở bản free

| Hiệu ứng | Dùng để | Mức |
|---|---|---|
| **Vignette** | Tối viền, dồn mắt vào giữa ảnh | ★★★ |
| **Sharpen** | Làm nét | ★★★ |
| **Glow** | Vùng sáng toả sáng mềm — ảnh mơ màng, ánh đèn đêm | ★★☆ |
| **Gaussian Blur** | Làm mờ — thường kết hợp mặt nạ | ★★☆ |
| **Light Rays** | Tia sáng xuyên qua cửa sổ, tán cây | ★☆☆ |
| **Film Damage** | Vết xước, bụi, viền phim cũ | ★☆☆ |
| **Mosaic Blur** | Che mặt, che biển số | ★☆☆ |
| **Prism Blur** | Tách màu kiểu lăng kính | ★☆☆ |
| **Blanking Fill** | Lấp viền trống bằng phiên bản mờ của ảnh | ★☆☆ |

### Chỉ có ở `Studio`

| Hiệu ứng | Là gì |
|---|---|
| **Film Grain** | Hạt phim |
| **Film Look Creator** | Bộ giả phim nhựa trọn gói: hạt, halation, bloom, vignette, split tone |
| **CineFocus** | Xoá phông giả bằng AI — tạo độ sâu trường ảnh như ống kính khẩu lớn |
| **Lens Blur** | Xoá phông kiểu ống kính |
| **Tilt-Shift Blur** | Hiệu ứng mô hình thu nhỏ |
| **Lens Flare**, **Lens Reflections**, **Aperture Diffraction** | Hiệu ứng ống kính, loé sáng |
| **Beauty**, **Face Refinement** | Làm đẹp da, chỉnh khuôn mặt |
| **Dehaze** | Xoá sương mù |
| **Contrast Pop** | Tăng tương phản cục bộ |
| **Color Compressor** | Gom màu về một tông |
| **Analog Damage** | Lỗi băng từ, VHS |
| **Depth Map** | Bản đồ độ sâu |
| **Super Scale** | Phóng to ảnh bằng AI |

### Thay thế ở bản free

| Muốn hiệu ứng `Studio` | Làm gần giống ở bản free |
|---|---|
| **Film Grain** | Không có thay thế trực tiếp. Đưa album sang trang Fusion, phủ một ảnh hạt grain tải về bằng node **Merge** chế độ **Overlay** |
| **Dehaze** | Tab Photo: hạ **Lift**, tăng **Contrast**, tăng **Saturation** nhẹ |
| **Contrast Pop** | Tab RAW hoặc Photo: tăng **Midtone Detail** |
| **Beauty** | Tab Photo: **Midtone Details** về số âm nhẹ (khoảng −15) |
| **CineFocus**, **Lens Blur** | Sang trang Color: vẽ Power Window quanh chủ thể, đảo ngược, áp Blur |

---

## Công thức hiệu ứng thường dùng

### Ảnh chân dung mềm mại
1. **Midtone Details** (tab Photo) khoảng −10
2. **Glow** — cường độ thấp
3. **Vignette** — nhẹ

### Ảnh phong cảnh có chiều sâu
1. **Midtone Detail** (tab RAW) khoảng +15
2. **Sharpen** — nhẹ
3. **Vignette** — vừa

### Ảnh hoài cổ
1. Tab Photo: **Saturation** khoảng 35, **Temp** ấm lên
2. **Film Damage** — nhẹ
3. **Vignette** — mạnh
