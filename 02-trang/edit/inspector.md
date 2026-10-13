# Inspector — phóng to, crop, tốc độ

Chọn clip trên timeline → bấm **Inspector** góc trên phải. Tab **Video** chứa gần hết những gì bạn cần.

Các mục **Transform, Crop, Dynamic Zoom, Composite, Stabilization** ở trang Edit **giống hệt** trang Cut — xem giải thích đầy đủ từng thanh ở [Tools trang Cut](../cut/tools.md). Trang này chỉ nói cách dùng hay gặp nhất.

## Những việc làm hằng ngày

| Muốn | Mục | Chỉnh |
|---|---|---|
| Cắt bớt vật thừa ở rìa | **Transform** | **Zoom** lên 1.1–1.2 |
| Đưa người vào giữa khung | **Transform** | **Position X** |
| Chỉnh đường chân trời nghiêng | **Transform** | **Rotation Angle** ±1–3, rồi tăng Zoom nhẹ |
| Dải đen trên dưới kiểu điện ảnh | **Crop** | **Crop Top** và **Crop Bottom** bằng nhau |
| Zoom chậm vào ảnh tĩnh | **Dynamic Zoom** | Bật, kéo khung xanh (đầu) và đỏ (cuối) trong Viewer |
| Mờ dần một lớp hình | **Composite** | **Opacity** |
| Bớt rung tay | **Stabilization** | Chọn **Similarity** → **Stabilize** |

> **Lens Correction** ở cuối tab Video là tính năng `Studio`.

Kéo trực tiếp trên Viewer thay vì gõ số: bấm menu nhỏ **góc dưới trái Viewer Timeline** → chọn **Transform**. Khung điều khiển hiện lên hình, kéo như ở trang Cut.

## Tốc độ — Retime

`★★☆ Thường dùng`

### Đổi tốc độ cả clip

Inspector → **Speed Change** → **Speed %**. `200` là nhanh gấp đôi, `50` là chậm một nửa.

Tick **Ripple Sequence** để phần sau timeline tự xê dịch theo độ dài mới.

### Speed ramp — nhanh chậm trong cùng một clip

1. Chọn clip → `⌘R`. Thanh tốc độ hiện ngay trên clip.
2. Đặt con trỏ chỗ muốn đổi tốc độ, bấm **mũi tên nhỏ** trên thanh tốc độ → **Add Speed Point**.
3. Thêm điểm thứ hai. Clip chia thành nhiều đoạn.
4. Bấm mũi tên trên từng đoạn → chọn tốc độ (ví dụ 25% cho đoạn giữa).

**Ví dụ:** cảnh nhảy xuống nước — bình thường lúc chạy, chậm 25% lúc bay trên không, bình thường lại khi chạm nước.

### Slow motion mượt

Quay 50fps hoặc 60fps rồi làm chậm thì luôn mượt. Quay 25fps mà làm chậm thì vào Inspector → **Retime and Scaling** → **Retime Process** → **Optical Flow**.

## Keyframe trong Inspector

`★★☆ Thường dùng`

Mỗi thông số có **viên kim cương** bên phải.

1. Đặt con trỏ ở điểm bắt đầu → bấm kim cương (chuyển **cam**) → đặt giá trị.
2. Dời con trỏ → đổi giá trị → keyframe mới tự tạo.
3. Phát thử.

**Cho chuyển động mềm:** chuột phải viên kim cương cam → **Ease In and Out**.

Chi tiết hơn: [Keyframe](chu-va-hieu-ung.md#keyframe--cho-mọi-thứ-chuyển-động).
