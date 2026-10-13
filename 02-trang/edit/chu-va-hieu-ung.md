# Chữ, chuyển cảnh, keyframe

Mọi thứ ở trang này lấy từ panel **Effects** (góc trên trái) → **Toolbox**.

## Chữ — Text, Text+

`★★★ Hằng ngày`

**Effects → Toolbox → Titles**. Kéo mẫu chữ lên **track hình phía trên** clip.

### Chọn loại nào

| Loại | Mạnh ở | Hạn chế | Dùng cho |
|---|---|---|---|
| **Text** | Nhanh, nhẹ. **Nhiều kiểu chữ trong một tiêu đề** (một chữ đậm, một chữ màu khác) | Ít hiệu ứng | Đoạn chữ thông tin, chú thích |
| **Text+** | Viền, bóng, gradient, **chữ chạy từng ký tự**, Write On | **Cả tiêu đề chỉ một kiểu chữ** | Tiêu đề lớn, chữ có animation |
| **L / M / R Lower 3rd** | Tự đặt hai dòng chữ ở góc dưới trái / giữa / phải | — | Tên + chức danh người phỏng vấn |
| **Scroll** | Chữ tự cuộn từ dưới lên | — | Danh sách cảm ơn cuối video |
| **Fusion Titles** | Mẫu có sẵn animation | Chỉnh được ít | Muốn đẹp nhanh, không tự làm |

**Scroll chạy nhanh hay chậm** tuỳ độ dài clip chữ trên timeline — kéo dài ra là chạy chậm lại.

### Chỉnh Text+

Chọn clip Text+ → Inspector. Bốn nhóm:

| Nhóm | Chỉnh gì |
|---|---|
| **Text** | Nội dung, font, cỡ, màu, giãn chữ, căn lề, **Write On** (chữ hiện dần) |
| **Layout** | Vị trí, xếp chữ theo khung, vòng tròn, đường cong |
| **Transform** | Xoay, phóng từng ký tự, từng chữ, từng dòng |
| **Shading** | Viền, bóng đổ, nền sau chữ — xếp chồng nhiều lớp |

**Chữ luôn đọc được trên mọi nền:** **Shading** → bật thêm một lớp **viền** đen mỏng, hoặc một lớp **nền** mờ phía sau chữ.

**Sửa chữ ngay trên hình:** menu **overlay** góc dưới trái Viewer Timeline → **Fusion Overlay**. Bấm vào chữ trên Viewer là sửa và kéo được.

**Chọn font dễ hơn:** bấm icon cạnh ô font để mở **Font Browser** — xem trước mặt chữ của từng font.

**Lưu chữ để dùng lại:** kéo clip chữ đã chỉnh từ timeline vào Media Pool. Bỏ vào [Power Bin](../media/bin.md#2-power-bin) để mọi project đều dùng được.

## Chuyển cảnh

`★★★ Hằng ngày`

| Việc | Cách |
|---|---|
| Thêm chuyển cảnh mặc định (Cross Dissolve) | Chọn điểm cắt → `⌘T` |
| Thêm kiểu khác | **Effects → Toolbox → Video Transitions**, kéo thả lên điểm cắt |
| Dài/ngắn hơn | Kéo mép chuyển cảnh trên timeline |
| Đổi chuyển cảnh mặc định | Chuột phải chuyển cảnh trong Effects → **Set as Standard Transition** |
| Xoá | Chọn chuyển cảnh → `Delete` |

**Nguyên tắc:** phần lớn chỗ nối nên **cắt thẳng**. Chỉ dùng chuyển cảnh mờ khi đổi chủ đề, đổi địa điểm, hoặc thời gian trôi qua.

**Muốn chuyển cảnh, clip phải dư footage** ở hai đầu (phần đã bị cắt bỏ). Nếu `⌘T` báo không đủ media, trim ngắn hai clip vào một chút rồi thử lại.

## Keyframe — cho mọi thứ chuyển động

`★★☆ Thường dùng`

**Là gì:** đánh dấu giá trị của một thông số tại hai thời điểm, Resolve tự tạo chuyển động ở giữa.

**Cách làm trong Inspector:**
1. Đặt con trỏ chỗ bắt đầu → bấm **kim cương** cạnh thông số → nó chuyển **cam**.
2. Dời con trỏ → đổi giá trị → keyframe thứ hai tự tạo.

| Việc | Cách |
|---|---|
| Nhảy giữa các keyframe | Mũi tên nhỏ hai bên viên kim cương |
| Chuyển động mềm | Chuột phải kim cương cam → **Ease In and Out** |
| Xoá một keyframe | Đứng tại đó, bấm viên kim cương cam |
| Xem và kéo keyframe trên timeline | Nút **Keyframe Editor** trên thanh công cụ timeline |

**Ví dụ thực tế:**
- Chữ trượt vào từ trái → keyframe **Position X**.
- Logo hiện dần → keyframe **Opacity** từ 0 lên 100.
- Zoom chậm vào khuôn mặt → keyframe **Zoom** từ 1.0 lên 1.15.

## Adjustment Clip

`★★☆ Thường dùng`

**Effects → Toolbox → Effects → Adjustment Clip**. Kéo lên track **trên cùng**, kéo dài phủ những clip muốn tác động.

Mọi hiệu ứng, Transform, chỉnh màu áp lên Adjustment Clip sẽ **tác động lên toàn bộ clip phía dưới**.

**Dùng khi:**
- Áp một tông màu cho cả đoạn — chỉnh màu Adjustment Clip ở trang Color.
- Zoom nhẹ cả đoạn để giấu rìa.
- Làm bản dọc từ bản ngang mà không đụng clip gốc.
