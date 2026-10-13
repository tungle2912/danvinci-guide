# Cân bằng trắng và sáng tối

Tất cả nằm trong **một palette**: **Color Wheels** — icon thứ 3 trên hàng palette, hình vòng tròn có chấm giữa. Manual gọi nó là **Primaries palette**.

> Làm trên **node 01** của [chuỗi 6 node](node.md#chuỗi-6-node-cơ-bản). Chọn node trước rồi mới kéo.

---

## Cân bằng trắng chỉnh ở đâu?

Có **4 cách**, từ nhanh đến chính xác:

### Cách 1 — Nút A (Auto Color)

`★★★` · Nhanh nhất

**Ở đâu:** **góc dưới trái** palette Color Wheels, nút chữ **A**.

**Làm gì:** tự cân lại điểm đen, điểm trắng và màu dựa trên **khung hình tại con trỏ**.

**Dùng khi:** muốn có điểm khởi đầu nhanh. Bấm A rồi chỉnh tiếp bằng tay. Đặt con trỏ ở khung hình **đại diện nhất** của clip trước khi bấm.

### Cách 2 — Ống hút White Balance

`★★★` · Nhanh và chính xác khi có vật màu trắng

**Ở đâu:** **góc dưới trái** palette, **ngay cạnh nút A**.

**Cách làm:**
1. Bấm ống hút — con trỏ chuột đổi thành ống hút.
2. Bấm vào một vật **đáng lẽ màu trắng** trong Viewer: tường trắng, áo trắng, khung cửa trắng.

**Lưu ý từ manual:**
- Chọn vật **trắng thật**, không phải trắng ngà.
- Chọn chỗ **không bị cháy sáng** — chỗ cháy trông trắng nhưng không phản ánh đúng màu.
- Điều chỉnh này **không hiện lên thanh nào** — nó là một chỉnh sửa ẩn. Muốn bỏ thì reset node.

### Cách 3 — Thanh Temp và Tint

`★★★` · Chỉnh bằng mắt, dễ kiểm soát nhất

**Ở đâu:** **hàng thanh phía trên** các bánh xe màu.

| Thanh | Kéo lên | Kéo xuống | Dải giá trị |
|---|---|---|---|
| **Temp** | Ấm hơn, ngả **cam** | Lạnh hơn, ngả **xanh dương** | −4000 tới +4000, mặc định 0 |
| **Tint** | Ngả **hồng tím** — sửa ánh đèn huỳnh quang | Ngả **xanh lá** | −100 tới +100, mặc định 0 |

**Cách chỉnh trên thanh:**
- **Kéo chữ hoặc con số** sang trái/phải để đổi giá trị.
- **Bấm đúp con số** để gõ trực tiếp.
- **Bấm đúp tên thanh** để reset về mặc định.

**Ảnh ám màu gì thì kéo thế nào:**

| Ảnh bị | Kéo |
|---|---|
| Ám xanh dương (quay ngoài trời râm, buổi tối) | **Temp** lên |
| Ám cam vàng (đèn sợi đốt, đèn trong nhà) | **Temp** xuống |
| Ám xanh lá (đèn tuýp, đèn huỳnh quang) | **Tint** lên |
| Ám hồng tím | **Tint** xuống |

### Cách 4 — Bánh xe màu + Parade

`★★☆` · Chính xác nhất, cần nhìn scope

Mở **Scopes** → chọn **Parade** (xem [Scope](scopes.md)). Kéo **vòng tròn màu** của bánh xe **Offset** về phía ngược với màu đang dư, đến khi **chân ba cột R G B ngang nhau** và **đỉnh ba cột ngang nhau**.

---

## Sáng tối — 4 bánh xe

`★★★ Hằng ngày`

| Bánh xe | Tác động lên | Kéo **thanh dưới** bánh xe sang phải |
|---|---|---|
| **Lift** | Vùng tối | Vùng tối sáng lên, ảnh bớt đậm |
| **Gamma** | Vùng trung gian | Cả ảnh sáng lên, vùng tối và sáng gần như giữ nguyên |
| **Gain** | Vùng sáng | Vùng sáng sáng hơn — dễ cháy |
| **Offset** | **Toàn bộ** ảnh | Cả ảnh sáng lên đều |

Mỗi bánh xe có hai phần:
- **Vòng tròn màu** — kéo **dấu chấm ở giữa** về một màu để đổi màu cho vùng đó.
- **Thanh trượt bên dưới** — kéo sang trái/phải để đổi sáng tối.

Reset một bánh xe: nút **reset** nhỏ ở góc trên phải bánh xe đó.

### Ống hút điểm đen, điểm trắng

**Ở đâu:** **góc trên trái** của bánh xe **Lift** (điểm đen) và **Gain** (điểm trắng).

| Ống hút | Bấm vào | Kết quả |
|---|---|---|
| **Pick Black Point** | Chỗ **đen nhất** đáng lẽ phải đen: bóng tối sâu, vải đen | Vùng tối đậm hơn, hết ám màu ở vùng tối |
| **Pick White Point** | Chỗ **trắng nhất** đáng lẽ phải trắng | Vùng sáng sáng hơn, hết ám màu ở vùng sáng |

Khác ống hút White Balance: hai ống hút này **có hiện kết quả** trên bánh xe Lift và Gain, nên chỉnh tiếp được.

> Manual cảnh báo: rất dễ kéo quá tay làm **cháy vùng sáng** hoặc **bệt vùng tối**. Luôn nhìn Waveform sau khi dùng.

### Thứ tự chỉnh chuẩn

1. **Offset** — cân màu tổng thể
2. **Lift** — đặt điểm đen chạm 0 trên Waveform
3. **Gain** — đặt điểm trắng gần đỉnh nhưng không chạm trần
4. **Gamma** — chỉnh độ sáng chung theo cảm nhận

---

## Hàng thanh điều chỉnh

Hai hàng thanh nằm **trên và dưới** các bánh xe. Dùng được ở cả ba chế độ của palette.

### Hàng trên

| Thanh | Làm gì | Dải giá trị | Mức |
|---|---|---|---|
| **Temp** | Ấm ↔ lạnh | −4000 … +4000 | ★★★ |
| **Tint** | Hồng ↔ xanh lá | −100 … +100 | ★★★ |
| **Contrast** | Tương phản quanh điểm Pivot | mặc định 1.0 | ★★★ |
| **Pivot** | Tâm của tương phản | — | ★★☆ |
| **Mid/Detail** | Độ nét cảm nhận. Số âm làm mịn da | −100 … +100 | ★★☆ |

**Contrast + Pivot:** ảnh tối mà tăng Contrast thì vùng tối bị bệt — hạ **Pivot** xuống trước. Ảnh sáng thì nâng Pivot lên.

### Hàng dưới

| Thanh | Làm gì | Dải giá trị | Mức |
|---|---|---|---|
| **Color Boost** | Tăng độ tươi ở **chỗ còn nhạt**, không đụng chỗ đã đậm | −100 … +100, mặc định 0 | ★★★ |
| **Shadows** | Lấy lại chi tiết vùng tối | −100 … +100 | ★★★ |
| **Highlights** | Kéo **xuống** để cứu vùng cháy (trời, cửa sổ) | −100 … +100 | ★★★ |
| **Saturation** | Độ đậm của **mọi** màu | 0 … 100, **mặc định 50** | ★★☆ |
| **Hue** | Xoay toàn bộ màu | mặc định 50 | ★☆☆ |
| **Lum Mix** | Cân giữa chỉnh tương phản kiểu YRGB và kiểu chỉ độ sáng | mặc định 100 | ★☆☆ |

> **Bẫy hay gặp:** **Saturation mặc định là 50**, không phải 0. Kéo về 0 là ảnh đen trắng. Muốn tăng màu cho da người tự nhiên, dùng **Color Boost** thay vì Saturation.

---

## Ba chế độ của palette

Đổi bằng menu thả xuống ở góc trên palette:

| Chế độ | Giao diện | Dùng khi |
|---|---|---|
| **Wheels** | 4 bánh xe | Mặc định, trực quan nhất |
| **Bars** | Thanh dọc R, G, B, Y riêng cho Lift/Gamma/Gain/Offset | Cân bằng trắng chính xác bằng cách nhìn Parade, kéo **từng kênh** |
| **Log** | Bánh xe Shadow / Midtone / Highlight + Offset | Footage LOG, chỉnh trước khi chuyển đổi màu |

Người mới: ở nguyên **Wheels**.

---

## Những gì làm ở palette này **không** làm được

- Chỉnh **riêng một vùng** (chỉ khuôn mặt, chỉ bầu trời) → [Qualifier và Window](curves-va-vung.md#chỉnh-riêng-một-vùng)
- Đổi **riêng một màu** (lá vàng thành lá xanh) → [Curves Hue vs Hue](curves-va-vung.md#curves)
- Chuyển footage **LOG sang Rec.709** đúng chuẩn → [LOG sang Rec.709](../../03-luong/log-sang-rec709.md)
