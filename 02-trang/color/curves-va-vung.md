# Curves và chỉnh vùng

## Curves

`★★★ Hằng ngày` · Palette thứ 7 (icon đường cong)

Chọn loại curve bằng các nút ở **đầu palette**.

| Loại | Dùng để | Ví dụ | Mức |
|---|---|---|---|
| **Custom** | Tương phản bằng đường chữ S | Kéo điểm vùng tối xuống, điểm vùng sáng lên | ★★★ |
| **Hue vs Hue** | Đổi **một màu** thành màu khác | Lá vàng → lá xanh, áo đỏ → áo cam | ★★★ |
| **Hue vs Sat** | Tăng/giảm độ đậm của **một màu** | Bớt sặc màu đỏ của da, làm trời xanh đậm hơn | ★★★ |
| **Hue vs Lum** | Sáng/tối **một màu** | Làm trời xanh tối lại cho có chiều sâu | ★★☆ |
| **Lum vs Sat** | Độ đậm theo vùng sáng tối | Bớt màu ở vùng tối để ảnh sạch hơn | ★★☆ |

Đủ 7 chế độ (thêm **Sat vs Sat**, **Sat vs Lum**) và ví dụ từng cái: [Curves chi tiết](curves-chi-tiet.md).

**Cách chọn đúng màu trên Hue curves:** bấm và kéo chuột **trên Viewer** vào vùng màu muốn chỉnh — Resolve tự thêm điểm đúng màu đó trên curve. Rồi kéo điểm lên/xuống.

## Chỉnh riêng một vùng

`★★★ Hằng ngày` — chỉ làm sáng mặt, chỉ đổi màu trời

Hai công cụ, thường dùng chung trong **một node**:

- **Qualifier** — chọn theo **màu**
- **Window** — chọn theo **hình**

### Qualifier — hút màu

Palette thứ 10 (icon ống hút).

Có 4 chế độ, đổi ở đầu palette:

| Chế độ | Chọn theo | Dùng khi |
|---|---|---|
| **3D** | Vẽ nét lên vùng màu muốn chọn | **Tách một màu** — da người, trời, áo. Nên thử đầu tiên |
| **HSL** | Hue, Saturation, Luminance riêng từng thanh | 3D không chọn sạch được |
| **LUM** | Chỉ độ sáng | Tách vùng sáng hoặc vùng tối |
| **RGB** | Kênh R, G, B | Ít dùng |

**Cách làm (chế độ 3D):**
1. Tạo node mới (`⌥S`), mở Qualifier, chọn **3D**.
2. **Kéo một nét** trên Viewer qua vùng muốn chọn (ví dụ má, trán).
3. Bấm `⇧H` để **xem vùng đã chọn** — phần không chọn chuyển xám.
4. Làm mượt bằng **Matte Finesse** ở cuối palette:

| Thanh | Làm gì |
|---|---|
| **Clean Black** | Xoá lấm tấm ở phần **không** được chọn |
| **Clean White** | Lấp lỗ thủng ở phần **được** chọn |
| **Blur Radius** | Làm mềm mép vùng chọn |

5. `⇧H` lần nữa để thoát xem vùng chọn, rồi chỉnh màu như bình thường — chỉ vùng đó đổi.

> `⌥⇧H` xem vùng chọn dạng **đen trắng** — dễ thấy mép răng cưa nhất.

### Window — khoanh vùng

Palette thứ 11.

| Hình | Dùng khi |
|---|---|
| **Linear** (chữ nhật) | Vùng vuông vức: màn hình, cửa sổ |
| **Circle** | Khuôn mặt, vignette |
| **Polygon** | Vùng nhiều góc |
| **Curve** | Vẽ tự do theo hình dạng |
| **Gradient** | Chuyển dần — làm tối dần bầu trời |

Kéo **mép mềm** (vòng ngoài) để vùng chuyển mượt. Nút **Invert** đảo vùng.

**Qualifier + Window cùng node:** Qualifier chọn màu da, Window khoanh quanh mặt → chỉ da trên mặt bị ảnh hưởng, không lan sang tay hay tường cùng màu.

### Tracker

`★★☆ Thường dùng` · Palette thứ 12

Window đứng yên, người thì di chuyển. Tracker cho window **bám theo**.

1. Tạo window quanh khuôn mặt.
2. Mở Tracker, bấm **Track Forward** (mũi tên sang phải). Resolve tự phân tích từng khung.
3. Đi ngược nếu cần: **Track Reverse**.

Bám bị trượt: bỏ tick các chuyển động không có (ví dụ **Rotate**, **3D**) rồi track lại.

> **Magic Mask** (tách người bằng AI) và **IntelliTrack** là `Studio`.

## Hoàn thiện

### Vignette

`★★☆ Thường dùng`

1. Node cuối: `⌥C` — node mới có sẵn **khung tròn**.
2. Kéo khung rộng ra quanh chủ thể, kéo mép mềm thật rộng.
3. Bấm **Invert** để chọn phần **bên ngoài**.
4. Mở Color Wheels, kéo **Gain** xuống nhẹ.

### Làm nét, làm mờ

`★★☆` · Palette **Blur** (thứ 13)

Thanh **Radius** mặc định **0.5**:
- **Trên 0.5** → làm mờ
- **Dưới 0.5** → làm nét. Video 1080p để khoảng 0.45–0.48 là vừa.

### Giảm cường độ một node

`★★☆` · Palette **Key** (thứ 14)

**Key Output Gain** về **0.5** → node đó chỉ tác động một nửa.

**Dùng khi:** một bước chỉnh, nhất là LUT, hơi quá tay. Giảm ở đây nhanh hơn chỉnh lại từ đầu.
