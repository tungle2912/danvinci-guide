# Scope — đọc Parade, Waveform

Mắt người **tự thích nghi** với màu ám — nhìn lâu là quen. Màn hình cũng mỗi cái một khác. Scope là thước đo **không nói dối**.

**Mở:** icon **Scopes** ở **ngoài cùng bên phải** hàng palette. Đổi loại bằng menu thả xuống góc trên phải khung scope (đang ghi **Parade** trong ảnh chụp ở trang trước). Vị trí nút: [Góc dưới phải — Keyframes · Scopes · Info](giao-dien.md#góc-dưới-phải--keyframes--scopes--info).

## Năm loại scope — chọn cái nào

`★★★ Hằng ngày`

| Scope | Đo gì | Dùng khi | Mức |
|---|---|---|---|
| **Waveform** | Độ sáng, trái → phải theo khung hình | Đặt điểm đen, điểm trắng, bắt cháy sáng | ★★★ |
| **Parade** | Đỏ, xanh lá, xanh dương **tách ba cột** | Cân bằng trắng, bắt ám màu | ★★★ |
| **Vectorscope** | Loại màu (hướng) và độ đậm (xa tâm) | Kiểm tra màu da, màu quá rực | ★★☆ |
| **Histogram** | Bao nhiêu điểm ảnh ở mỗi mức sáng | Quen đọc biểu đồ máy ảnh | ★☆☆ |
| **CIE Chromaticity** | Màu ảnh so với tam giác gam màu | Kiểm tra vượt gam màu khi giao HDR, P3 | ★☆☆ |

> Trục dọc Waveform và Parade mặc định là **0–1023** (10-bit), bất kể cài đặt Video/Data Level của project.

---

## Mở scope to hơn — cửa sổ Scopes

`★★☆ Thường dùng`

Ô scope ở góc dưới phải chỉ hiện **một** scope, và khá nhỏ.

| Cách | Làm gì |
|---|---|
| Nút **Expand** góc trên phải ô scope | Tách scope ra **cửa sổ nổi** |
| **Workspace → Video Scopes → On** (`⇧⌘W`) | Mở cửa sổ nổi. Dùng được ở trang **Media, Color, Deliver** |
| **Workspace → Dual Screen → On** | Scope nằm sẵn trên màn hình thứ hai |
| Kéo góc dưới phải cửa sổ | Đổi cỡ cửa sổ |

### 1-up, 2-up, 4-up

Nút ở **góc trên phải cửa sổ Scopes** chọn hiện **1, 2, 4 hoặc 9** scope cùng lúc. Hoặc **Workspace → Video Scopes → 1-Up / 2-Up / 4-Up**.

**Đổi scope trong từng ô:** menu tên scope ở **góc trên trái** mỗi ô. Một loại có thể mở **nhiều lần** với cài đặt khác nhau.

**Ví dụ — bố trí 4-up hay dùng:** Waveform · Parade · Vectorscope · Histogram. Chỉnh một clip mà không cần đổi qua lại.

**Ví dụ — ba Vectorscope:** đặt một cái **Low**, một cái **Mid**, một cái **High** — xem riêng màu vùng tối, vùng giữa, vùng sáng.

### Phóng to, dời trong scope

| Việc | Cách |
|---|---|
| Phóng to biểu đồ | Giữ `⌥` + lăn chuột |
| Dời vùng nhìn | Kéo bằng **nút giữa** chuột |

---

## Menu cài đặt scope

`★☆☆ Tình huống cụ thể`

Có hai chỗ:

- **Menu ⋯** (option menu) của scope — cài đặt **chung** cho mọi scope.
- **Nút Option** bên phải menu tên scope — cài đặt **riêng** scope đó. Bấm ra ngoài để đóng.

### Cài đặt chung — menu ⋯

| Mục | Làm gì |
|---|---|
| **Waveform Scale Style** | Thang số bên trái Waveform, Parade: **10-bit** (mặc định), **12-bit**, **Percentage** (0–100), **mV**. **HDR (ST.2084/HLG)** là `Studio` |
| **Video Level Scopes** (trong Waveform Scale Style) | Hiện theo Video Levels thay vì Data Levels. **Chỉ đổi cách hiện**, không đổi file xuất |
| **Vectorscope Scale Style** | Lưới Vectorscope: **Off**, **Standard** (mặc định), **Simplified**, **Hue Vectors**. Chọn ô mục tiêu 75%, 100% hay cả hai, có hiện tên màu hay không |
| **Quality** | **High / Medium / Low / Auto**. Máy yếu, phát giật → hạ xuống |
| **Low Pass Filter** | Lọc nhiễu, biểu đồ gọn dễ đọc. Đỉnh, đáy trông **thấp hơn thật** — bật kèm **Extents** |
| **Display Qualifier Focus** | Rê ống hút trên Viewer (chế độ Qualifier) → scope **khoanh tròn** đúng chỗ của điểm ảnh đó |
| **Reset All** | Đưa mọi scope về mặc định |

> Scope cũng tốn sức GPU. Máy yếu mà không cần nhìn thì **đóng scope** cho phát mượt hơn.

### Cài đặt riêng — nút Option

| Thông số | Có ở | Làm gì |
|---|---|---|
| Chế độ kênh | Waveform: **Y / CbCr / RGB** (RGB bật tắt riêng R, G, B). Parade: **RGB / YRGB / YCbCr**. Histogram: **RGB / YRGB** | Xem kênh nào |
| **Colorize** | Waveform, Parade, Vectorscope | Tô biểu đồ bằng màu — dễ thấy phần nào của hình nằm đâu trên scope |
| **Extents** | Waveform, Parade, Vectorscope | Vẽ viền quanh **mọi điểm vượt ra** — thấy chính xác đỉnh và đáy |
| Thanh **độ sáng biểu đồ** | Mọi scope (Histogram gọi là **Gain**) | Biểu đồ sáng hơn để thấy chi tiết |
| **Graticule** | Mọi scope | Vạch thang đo sáng hơn hoặc mờ đi |
| **Show Reference Levels** | Waveform, Parade, Histogram | Hai vạch **Low** và **High** tự đặt — đánh dấu giới hạn cần giữ |
| **ALL / Low / Mid / High** | Vectorscope | Xem màu cả hình, hay chỉ vùng tối / giữa / sáng. **Combine** chồng cả ba viền lên nhau |
| **Low Range / High Range** | Vectorscope | Ranh giới vùng tối, vùng sáng. Mặc định 0.30 và 0.70 |
| **Show 2X Zoom** | Vectorscope, CIE | Phóng biểu đồ 200% |
| **Show Skin Tone Indicator** | Vectorscope | Bật **vạch màu da** |
| **Show Graticule** | Vectorscope, CIE | Ẩn/hiện vòng chia độ và dấu tâm |

---

## Parade

`★★★ Hằng ngày` — dùng để cân bằng trắng

Ba cột **đỏ, xanh lá, xanh dương** đặt cạnh nhau. Trục dọc là độ sáng, từ 0 (đáy) tới 1023 (đỉnh).

| Thấy gì | Nghĩa | Sửa |
|---|---|---|
| Ba cột **chân ngang nhau, đỉnh ngang nhau** | Cân bằng trắng **đúng** | — |
| Cột xanh dương cao hơn hai cột kia | Ảnh **ám xanh** | Temp lên |
| Cột đỏ cao hơn | Ảnh **ám cam/đỏ** | Temp xuống |
| Cột xanh lá cao hơn | Ảnh **ám xanh lá** | Tint lên |

> Chỉ so ở những vùng **đáng lẽ trung tính** (trắng, xám, đen). Cảnh hoàng hôn thì cột đỏ cao hơn là đúng.

**Đọc từng tầng:** so **chân** ba cột = màu vùng tối. So **giữa** = vùng trung. So **đỉnh** = vùng sáng. Ám màu có thể chỉ ở một tầng — ví dụ bóng tối ám xanh nhưng vùng sáng vẫn trung tính → chỉnh **Lift**, không đụng Gain.

**Độ cao cả cột** = độ tương phản. Cột **cao** (chân sát 0, đỉnh gần 1023) = tương phản mạnh. Cột **lùn** = ảnh bẹt.

**Chế độ YRGB** thêm cột độ sáng (Y) cạnh ba cột màu.

**Ví dụ — quay trong nhà dưới đèn sợi đốt:** cột đỏ cao hơn hẳn ở đỉnh. Kéo **Temp** xuống tới khi đỉnh ba cột ngang nhau ở chỗ tường trắng.

## Waveform

`★★★ Hằng ngày` — dùng để đặt độ sáng

Một khối duy nhất cho độ sáng. Trái sang phải tương ứng trái sang phải trong khung hình.

| Thấy gì | Nghĩa |
|---|---|
| Đáy chạm khoảng **0** | Có điểm đen thật — tốt |
| Đáy lơ lửng ở 100–200 | Ảnh bị **xám, bạc** — kéo Lift xuống |
| Đỉnh khoảng **900–1000** | Đủ sáng, chưa cháy — tốt |
| Đỉnh **dẹt phẳng ở 1023** | **Cháy** — mất chi tiết, kéo Gain hoặc Highlights xuống |
| Dồn cục ở giữa | Ảnh **thiếu tương phản** — điển hình của footage LOG |

**Nên để chế độ Y** (độ sáng thuần). Chế độ **RGB** chồng ba màu lên nhau — chỗ ba màu trùng nhau hiện **trắng**.

### Đọc cháy sáng và chết đen

| Thấy trên Waveform | Nghĩa | Làm gì |
|---|---|---|
| Một **đường thẳng ngang** dày ở 1023 | Cháy sáng — trời, cửa sổ thành mảng trắng | Gain hoặc Highlights xuống tới khi đường đó tách ra thành vệt |
| Một **đường thẳng ngang** dày ở 0 | Chết đen — tóc, áo đen mất chi tiết | Lift hoặc Shadows lên một chút |
| Đường ngang có sẵn **từ lúc quay** | Đã cháy trong file gốc | Kéo xuống chỉ ra mảng xám. Không cứu được chi tiết |

> Bật **Extents** để thấy chính xác điểm cao nhất, thấp nhất — nhất là khi đang bật Low Pass Filter.

**Ví dụ — người đứng trước cửa sổ:** bên phải Waveform dẹt ở 1023 (cửa sổ), khối giữa ở 300–500 (mặt). Hạ **Highlights** cho cửa sổ xuống dưới 1000, rồi nâng **Gamma** cho mặt sáng lên.

## Vectorscope

`★★☆ Thường dùng` — dùng cho màu da

Một vòng tròn. **Càng xa tâm càng đậm màu**, hướng chỉ loại màu.

**Đường skin tone line:** vạch chéo hướng khoảng **11 giờ**. Da người, **bất kể màu da gì**, nằm trên hoặc rất gần vạch này.

**Bật vạch:** nút Option của Vectorscope → **Show Skin Tone Indicator**.

**Cách kiểm tra da:** dùng Window khoanh riêng khuôn mặt — Vectorscope chỉ hiện màu của vùng đó. Lệch khỏi vạch thì chỉnh ở node Secondary.

| Thấy gì | Nghĩa |
|---|---|
| Đám biểu đồ **nằm giữa tâm** | Ảnh không ám màu |
| Cả đám **lệch về một phía** | Ảnh ám màu theo hướng đó |
| Vệt dài **chạm hoặc vượt ô mục tiêu** | Màu đó rất rực — dễ bị chói khi xem trên TV |
| Vệt da lệch về phía **vàng/xanh lá** | Da trông bệnh |
| Vệt da lệch về phía **đỏ/hồng** | Da đỏ quá |

Mỗi **ô nhỏ** quanh vòng là mục tiêu của một màu: đỏ, hồng tím, xanh dương, xanh ngọc, xanh lá, vàng.

**Ví dụ — mặt bị ám xanh lá do đèn huỳnh quang:** khoanh mặt bằng Window → vệt nằm bên phải vạch da, ngả về phía G. Kéo bánh xe **Gamma** ngược hướng cho vệt quay về vạch.

## Histogram

`★☆☆` — giống biểu đồ của máy ảnh. Quen với chụp ảnh thì dễ đọc, nhưng Parade và Waveform chính xác hơn để chỉnh video.

| Thấy gì | Nghĩa |
|---|---|
| Trái = đen, phải = trắng | Trục ngang là độ sáng |
| Đồi **dồn sát mép phải**, có cột dựng đứng | Cháy sáng |
| Đồi **dồn sát mép trái** | Chết đen |
| Đồi **hẹp**, nằm giữa | Thiếu tương phản |
| Đồi đỏ, xanh lá, xanh dương **lệch nhau** | Ám màu |

## CIE Chromaticity

`★☆☆ Tình huống cụ thể`

**Là gì:** hình **móng ngựa** là mọi màu mắt người thấy được. **Tam giác** bên trong là gam màu đang dùng (ví dụ Rec.709). Biểu đồ màu của ảnh vẽ đè lên.

| Thông số | Làm gì |
|---|---|
| **CIE 1931 xy** / **CIE 1976 uv** | Hai kiểu vẽ. Không cái nào "đúng hơn" — chọn cái dễ nhìn |
| **Additional Gamut** | Thêm tam giác thứ hai để so, ví dụ P3 với Rec.709 |

**Đọc:** biểu đồ **vượt ra ngoài** tam giác → chắc chắn vượt gam màu. Nằm trong tam giác thì **chưa chắc** an toàn — vùng sáng, vùng tối vẫn có thể vượt.

> Video thường đăng mạng xã hội, chỉnh Rec.709 thì gần như không cần scope này.

## Thứ tự nhìn scope khi chỉnh một clip

1. **Waveform** → đặt điểm đen, điểm trắng (node 01)
2. **Parade** → cân bằng trắng (node 01)
3. **Vectorscope** → kiểm tra da người (node 04)
