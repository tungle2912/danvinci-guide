# Chỉnh ảnh — tab RAW, tab Photo, Tools

![Tab RAW xám với JPG, sáng với CR3](../../assets/img/photo-inspector-tabs.png)
*Trái: ảnh JPG, tab RAW xám. Phải: ảnh CR3, tab RAW sáng.*

Mọi thanh chỉnh ảnh nằm ở **hai chỗ**:

- **Inspector** (nút góc trên phải) — các thanh trượt, chỉnh bằng số
- **Tools** (nút góc dưới trái Viewer) — kéo trực tiếp trên ảnh

Inspector có **bốn tab** ở trên cùng: **RAW · Photo · Effects · File**.

| Tab | Chứa gì | Khi nào sáng |
|---|---|---|
| **RAW** | Chỉnh từ dữ liệu cảm biến gốc | Chỉ khi ảnh là file RAW. JPG/PNG thì tab này xám |
| **Photo** | Xoay, crop, màu, tương phản | Mọi ảnh |
| **Effects** | Thông số hiệu ứng đã áp | Chỉ khi ảnh có hiệu ứng |
| **File** | Thông tin, metadata | Mọi ảnh |

![Mỗi loại chỉnh nằm ở đâu: tab RAW, tab Photo, Tools](../../assets/diagrams/photo-where-adjust.svg)

*Cùng một việc có thể có ở hai chỗ. Ảnh RAW: sáng và màu ở tab RAW trước. Crop, xoay: tab Photo bằng số hoặc Tools bằng tay.*

---

## Cân bằng trắng chỉnh ở đâu?

![Chọn tab để chỉnh cân bằng trắng](../../assets/diagrams/photo-white-balance.svg)

**Ảnh RAW** → **Inspector → tab RAW** → mục **White Balance**, **Temperature**, **Tint**.
**Ảnh JPG, PNG, HEIC** → **Inspector → tab Photo** → mục **Adjustments** → **Auto Balance**, **Temp**, **Tint**.

Ảnh RAW thì **luôn chỉnh ở tab RAW trước**. Lý do: tab RAW chỉnh trên dữ liệu cảm biến **trước khi** thành ảnh màu, nên giữ được nhiều thông tin hơn hẳn. Tab Photo chỉnh **sau khi** ảnh đã thành hình, dư địa ít hơn.

---

## Tab RAW — chỉnh từ dữ liệu gốc

`★★★ Hằng ngày` với ảnh RAW

> Manual khuyên: với ảnh RAW, đây là **cách được ưu tiên** để chỉnh phơi sáng và màu, vì nó dùng dữ liệu cảm biến thuần và được tinh chỉnh riêng cho từng hãng máy.

### Nhóm 1 — Giải mã

| Thanh | Làm gì | Đặt gì |
|---|---|---|
| **Decode Quality** | Giải mã ảnh ở độ phân giải **Full**, **Half**, **Quarter**, hoặc **Use project setting** (mặc định, theo cài đặt chung của project) | Máy yếu thì để **Half** khi chỉnh, đổi về **Full** trước khi xuất |
| **Color Space** | Không gian màu để chỉnh và xuất | Manual khuyên chọn không gian màu của hãng máy, hoặc một chuẩn video như Rec.709 nếu ảnh sẽ vào video |
| **Gamma** | Đường cong gamma | Của hãng máy, hoặc chuẩn video — chọn cùng nhóm với Color Space |

### Nhóm 2 — Cân bằng trắng

![Preset White Balance trong tab RAW](../../assets/img/photo-raw-white-balance.png)
*Chọn preset gần đúng, rồi tinh chỉnh Temperature và Tint.*

| Thanh | Làm gì | Kéo thế nào |
|---|---|---|
| **White Balance** | Chọn **preset** theo ánh sáng lúc chụp. Chọn xong, Temp và Tint tự nhảy theo | Xem bảng preset bên dưới |
| **Temperature** | Nhiệt độ màu, đơn vị **Kelvin** | Ảnh **ám xanh** (lạnh) → kéo **lên**. Ảnh **ám cam** (nóng) → kéo **xuống** |
| **Tint** | Trục **xanh lá ↔ hồng tím** | Ảnh **ám xanh lá** (đèn huỳnh quang) → kéo **lên**. Ảnh **ám hồng** → kéo **xuống** |

**Preset White Balance:**

| Preset | Chọn khi chụp dưới |
|---|---|
| **As Shot** | Giữ đúng cài đặt máy lúc chụp — mặc định |
| **Daylight** | Nắng trực tiếp ban ngày |
| **Cloudy** | Trời âm u |
| **Shade** | Bóng râm |
| **Tungsten** | Đèn sợi đốt vàng, đèn trong nhà |
| **Fluorescent** | Đèn huỳnh quang, đèn tuýp |
| **Flash** | Đèn flash |

**Cách làm nhanh nhất:** chọn preset gần đúng nhất trước, rồi tinh chỉnh **Temperature** và **Tint** bằng mắt.

**Cách làm chính xác nhất:** tìm trong ảnh một vật **đáng lẽ màu trắng hoặc xám** (tường trắng, áo trắng, bê tông), chỉnh Temp và Tint đến khi vật đó trông trung tính — không ngả màu nào.

### Nhóm 3 — Sáng tối

| Thanh | Làm gì | Dải giá trị | Mặc định |
|---|---|---|---|
| **Exposure** | Phơi sáng, tính theo **stop** | −5 tới +5 | 0 |
| **Highlights** | Kéo **xuống** để cứu vùng sáng bị cháy | −100 tới +100 | 0 |
| **Shadows** | Kéo **lên** để lấy lại chi tiết vùng tối | −100 tới +100 | 0 |
| **Lift** | Điểm đen. Kéo lên làm vùng tối xám đi, kéo xuống làm đen sâu hơn | −100 tới +100 | — |
| **Gain** | Điểm trắng. Kéo lên làm vùng sáng sáng hơn | −100 tới +100 | 0 |
| **Contrast** | Tương phản. Kéo lên thì tối tối hơn, sáng sáng hơn, trung gian giữ nguyên | −100 tới +100 | 0 |

> **Không sợ kéo quá tay.** Manual ghi rõ: kéo Exposure làm ảnh vượt mức trắng thì dữ liệu **vẫn được giữ nguyên**, kéo lại là lấy lại được.

### Nhóm 4 — Màu và chi tiết

| Thanh | Làm gì | Dải giá trị | Mặc định |
|---|---|---|---|
| **Color Boost** | Tăng độ tươi ở **những chỗ còn nhạt màu**, không đụng chỗ đã đậm — giống **Vibrance** của Lightroom | −100 tới +100 | 0 |
| **Saturation** | Tăng/giảm độ đậm của **mọi màu** đều nhau | −100 tới +100 | 0 |
| **Midtone Detail** | Độ nét cảm nhận ở vùng nhiều chi tiết — giống **Clarity**. Số âm làm mềm da | −100 tới +100 | 0 |
| **Sharpness** | Làm nét lúc giải mã | 0 tới 100 | **10** |
| **Noise Reduction** | Giảm nhiễu. Ảnh ISO cao hoặc chụp tối cần | — | — |

**Color Boost hay Saturation?** Gần như luôn chọn **Color Boost**. Saturation làm da người bị cam đỏ trước khi phần còn lại đủ tươi. Color Boost tránh được chuyện đó vì nó chừa những màu đã đậm.

### Thứ tự kéo các thanh trong tab RAW

![Tab RAW sau khi chỉnh ảnh ví dụ](../../assets/img/photo-raw-exposure-color.png)
*Đủ bước cân bằng trắng, phơi sáng, màu, độ nét trong một tab.*

1. **White Balance** — chọn preset
2. **Temperature**, **Tint** — tinh chỉnh
3. **Exposure** — cho tổng thể đủ sáng
4. **Highlights** — cứu trời, cứu vùng cháy
5. **Shadows** — lấy lại vùng tối
6. **Contrast** — tạo chiều sâu
7. **Color Boost** — cho màu tươi
8. **Midtone Detail** — độ nét

Cân bằng trắng **trước** phơi sáng, vì ảnh ám màu sẽ đánh lừa mắt khi đánh giá độ sáng.

**Ví dụ — ảnh CR3 chụp ngược sáng, mặt người tối, trời cháy:**

| Thanh | Đặt |
|---|---|
| **White Balance** | `Daylight` |
| **Exposure** | `+0.5` |
| **Highlights** | `−60` |
| **Shadows** | `+35` |
| **Contrast** | `+10` |
| **Color Boost** | `+15` |
| **Midtone Detail** | `+8` |

Bấm `⇧D` để so với ảnh gốc. Thấy da bị xám thì giảm **Shadows** lại một chút.

### Reset riêng tab RAW

Menu **ba chấm** góc trên phải Inspector → **Reset Camera Raw**.

---

## Tab Photo — Adjustments

`★★★ Hằng ngày` — với mọi ảnh

Tab này có bốn nhóm: **Source Transform · Source Cropping · Looks · Adjustments**. Phần chỉnh màu nằm ở **Adjustments**.

### Auto Balance — bắt đầu từ đây

`★★☆ Thường dùng`

**Một nút**, tự cân lại dải sáng và cân bằng trắng bằng machine learning.

**Dùng khi:** không biết bắt đầu từ đâu. Bấm Auto Balance, xem kết quả, rồi chỉnh tiếp bằng tay. Thường là điểm khởi đầu tốt hơn ảnh gốc.

**Cách làm:**
1. Chọn ảnh trong album. **Inspector → tab Photo**.
2. Cuộn xuống mục **Adjustments** → bấm **Auto Balance**.
3. Bấm `⇧D` vài lần để so với ảnh gốc. Không ưng thì `⌘R` để bỏ (Inspector đang được chọn).

### Các thanh trong Adjustments

![Nhóm Adjustments trong tab Photo](../../assets/img/photo-tab-photo-adjustments.png)
*Lưu ý Saturation mặc định là 50, không phải 0.*

| Thanh | Kéo sang phải | Kéo sang trái | Mặc định |
|---|---|---|---|
| **Temp** | Ấm hơn, ngả cam | Lạnh hơn, ngả xanh dương | 0 |
| **Tint** | Ngả hồng tím — sửa ánh đèn huỳnh quang | Ngả xanh lá | 0 |
| **Lift** | Vùng tối sáng lên, tương phản giảm | Vùng tối đen sâu hơn | — |
| **Gamma** | Cả ảnh sáng hơn | Cả ảnh tối hơn | — |
| **Gain** | Vùng sáng sáng hơn, dễ cháy | Vùng sáng tối đi | — |
| **Contrast** | Tương phản tăng quanh điểm Pivot | Tương phản giảm | — |
| **Pivot** | Dời tâm tương phản lên vùng sáng | Dời tâm xuống vùng tối | — |
| **Midtone Details** | Nét hơn ở vùng nhiều chi tiết | Mềm vùng ít chi tiết — mịn da | 0 |
| **Shadows** | Lấy lại chi tiết vùng tối | Vùng tối tối hơn | — |
| **Highlights** | Vùng sáng sáng hơn | Cứu vùng cháy | — |
| **Saturation** | Đậm hơn (100 = gấp đôi) | Nhạt hơn (0 = đen trắng) | **50** |
| **Hue** | Xoay mọi màu theo vòng màu | Xoay ngược | **50** |

> **Bẫy hay gặp:** **Saturation** ở tab Photo **mặc định là 50**, không phải 0. Muốn ảnh đen trắng thì kéo về **0**. Còn Saturation ở tab RAW mặc định là 0 và chạy từ −100. Hai thanh cùng tên nhưng thang khác nhau.

**Ví dụ — ảnh JPG chụp trong nhà, ám vàng, hơi bệt:**

1. **Auto Balance**.
2. **Temp** kéo sang trái (âm) đến khi tường trắng hết vàng.
3. **Contrast** kéo nhẹ sang phải. Ảnh tối thì hạ **Pivot** trước.
4. **Saturation** từ `50` lên `55` — tăng nhẹ, không quá tay.
5. `⇧D` so với gốc.

### Pivot dùng khi nào

Ảnh **tối** mà tăng Contrast → vùng tối bị bệt đen. Hạ **Pivot** xuống trước rồi mới tăng Contrast.
Ảnh **sáng** mà tăng Contrast → vùng tối không đủ đậm. Nâng **Pivot** lên.

### Looks — tông màu có sẵn

Mục **Looks → Type**: chọn một tông màu preset từ danh sách. Để **Default (Original)** là không dùng.

Chọn look xong vẫn chỉnh tiếp được bằng các thanh Adjustments. Muốn dùng tông màu **của riêng bạn**, áp một LUT thay vì Look — xem [Lưu tông màu thành LUT](#lưu-tông-màu-thành-lut).

### Source Transform

**Zoom X/Y**, **Position X/Y**, **Rotation Angle**, **Pitch**, **Yaw**, **Flip** — cùng các thông số với [Transform trên Viewer](#transform) bên dưới, chỉ khác là gõ số.

**Dùng nhiều nhất:** **Rotation Angle** để chỉnh đường chân trời bị nghiêng, ví dụ `−1.5`. Phím tắt xoay 90°: `⌘[` / `⌘]`.

> **Mẹo:** xoay xong mép ảnh lộ góc trống. Tăng **Zoom** một chút (ví dụ `1.03`) hoặc crop lại để che.

### Source Cropping

| Thanh | Làm gì |
|---|---|
| **Ratio** | Tỉ lệ khung. **As Shot** là giữ tỉ lệ máy |
| **Lock Aspect Ratio** | Tick để crop vẫn giữ đúng tỉ lệ đã chọn |
| **Crop Left / Right / Top / Bottom** | Cắt bao nhiêu pixel mỗi cạnh |

Crop bằng số ở đây, hoặc kéo trực tiếp bằng [Tools → Crop](#crop).

### Reset tab Photo

`⌘R` (Inspector phải đang được chọn), hoặc menu ba chấm → **Reset Photo**.

---

## Tools — chỉnh trực tiếp trên Viewer

`★★★ Hằng ngày`

Bấm **Tools** ở **góc dưới trái Viewer**. Ba nhóm hiện ra: **Transform · Crop · Looks**, cộng **Effects Overlay**.

Mỗi nhóm có nút **Toggle** ngoài cùng trái (bật/tắt không mất chỉnh sửa) và **Reset** ngoài cùng phải.

> **Quan trọng:** khi đang mở Tools, Viewer vẫn hiện **khung ảnh gốc** bên dưới lưới để bạn căn. Transform và Crop chỉ **áp vào ảnh khi bạn đóng thanh Tools lại**.

### Transform

`★★☆ Thường dùng`

| Kéo | Làm gì |
|---|---|
| Trong khung | Dời ảnh |
| Góc chéo | Phóng to giữ tỉ lệ |
| Cạnh | Kéo giãn một chiều |
| Tay nắm giữa | Xoay |

Các ô số trên thanh Transform:

| Ô | Làm gì |
|---|---|
| **Zoom Width / Height** | Phóng to, thu nhỏ theo chiều ngang / dọc |
| **Zoom Link** (ổ khoá) | Bật để phóng to giữ đúng tỉ lệ ảnh. Tắt để kéo giãn một chiều |
| **Position X / Y** | Dời ảnh sang ngang / lên xuống |
| **Rotation Angle** | Xoay quanh tâm |
| **Pitch** | Nghiêng ảnh ra sau hoặc tới trước theo trục ngang — số dương đẩy mép trên ra xa |
| **Yaw** | Xoay ảnh theo trục dọc — số dương kéo mép trái lại gần |
| **Flip** | Hai nút: lật ngang, lật dọc |

**Ví dụ:** ảnh tòa nhà chụp ngửa lên, cạnh tường chụm vào nhau. Kéo **Pitch** từng chút một và quan sát đến khi cạnh tường thẳng lại. Bật [đường gióng](giao-dien.md#đường-gióng-và-thước-đo) dọc để so.

### Crop

![Crop 4:5 bằng Tools trên Viewer](../../assets/img/photo-tools-crop.png)
*Crop chỉ áp vào ảnh khi đóng thanh Tools.*

`★★★ Hằng ngày`

| Điều khiển | Làm gì |
|---|---|
| **Aspect Ratio** | Chọn tỉ lệ có sẵn hoặc tự đặt. Mặc định **As Shot** |
| **Lock Aspect Ratio** (ổ khoá) | Khoá tỉ lệ khi kéo crop. Mở khoá để crop tự do |
| **Crop Left / Right / Top / Bottom** | Số pixel cắt mỗi cạnh |
| Tay nắm mỗi cạnh trên Viewer | Kéo để cắt cạnh đó |

**Cách làm — crop 4:5 cho Instagram:**
1. Bấm **Tools** → **Crop**.
2. **Aspect Ratio** → `4:5`. Bật ổ khoá **Lock Aspect Ratio**.
3. Kéo góc khung để chọn vùng, kéo trong khung để dời.
4. Đóng thanh **Tools** — crop mới áp vào ảnh.

**Tỉ lệ hay dùng:**

| Tỉ lệ | Dùng cho |
|---|---|
| **1:1** | Ảnh đại diện, lưới Instagram cũ |
| **4:5** | Bài đăng Instagram dọc — chiếm nhiều diện tích màn hình nhất |
| **9:16** | Story, Reels, TikTok |
| **3:2** | In ảnh, tỉ lệ gốc máy ảnh full-frame |
| **16:9** | Thumbnail YouTube, hình nền |

### Looks

| Điều khiển | Làm gì |
|---|---|
| **Auto Balance** | Tự cân bằng — giống nút trong tab Photo |
| **Look Selector** | Chọn tông màu preset |

Look chọn ở đây và ở **tab Photo → Looks** là một. Muốn tông màu riêng của bạn thì áp LUT.

### Effects Overlay

`★☆☆ Tình huống cụ thể`

Hiệu ứng nào có điều khiển kéo trên Viewer (như điểm tâm, vùng tác động) thì điều khiển đó nằm ở đây.

1. Áp hiệu ứng — xem [Hiệu ứng ảnh](hieu-ung.md). Thường hiệu ứng tự bật chế độ này.
2. Nếu chưa thấy điều khiển: bấm **Tools** → icon **Effects Overlay** → **Open FX Overlay** (hiệu ứng Resolve FX) hoặc **Fusion Overlay** (hiệu ứng Fusion).
3. Kéo điều khiển trên Viewer. Bấm ``⇧` `` để tạm ẩn/hiện điều khiển khi muốn nhìn ảnh sạch.

---

## Áp cùng chỉnh sửa cho nhiều ảnh

`★★☆ Thường dùng` — chỉnh một ảnh, áp cho cả loạt cùng buổi chụp

### Cách 1 — Click chuột giữa (nhanh nhất)

1. Trong album, **chọn những ảnh muốn nhận chỉnh sửa**.
2. **Click chuột giữa** vào ảnh đã chỉnh xong.

Xong. Lưu ý:
- **Không** copy hiệu ứng.
- **Có** copy thiết lập RAW, nhưng chỉ khi các ảnh **cùng loại RAW** (cùng là CR3 với nhau chẳng hạn).

### Cách 2 — Paste Attributes (chọn được copy gì)

1. Chọn ảnh đã chỉnh → `⌘C`.
2. Chọn các ảnh muốn nhận.
3. **Edit → Paste Attributes** (`⌥V`), hoặc chuột phải một ảnh đã chọn → **Paste Attributes**.
4. Trên đầu cửa sổ ghi tên ảnh nguồn và các ảnh nhận — kiểm tra lại. Tick những thứ muốn dán → **Apply**.

Muốn dán cả **hiệu ứng**: tick ô **Plugins** trong mục **Photo Attributes**.

**Ví dụ:** 40 ảnh chụp cùng ánh sáng. Chỉnh xong ảnh đầu, `⌘C`. Lọc album **Rating ≥ 4**, chọn hết (`⌘A`), `⌥V` → tick mọi mục trừ phần crop → **Apply**. Mỗi ảnh vẫn giữ crop riêng.

> **Lỗi hay gặp:** click chuột giữa sang ảnh JPG từ ảnh CR3 — phần tab RAW không đi theo vì khác loại file. Ảnh JPG chỉ nhận phần tab Photo.

### Gỡ bớt chỉnh sửa

1. Chọn một hoặc nhiều ảnh.
2. **Edit → Remove Attributes**, hoặc chuột phải → **Remove Attributes**.
3. Chỉ các ô có thứ để gỡ mới bật. Tick thứ muốn gỡ → **Apply**.

---

## Lưu tông màu thành LUT

`★☆☆ Tình huống cụ thể`

**Dùng khi:** chỉnh được một tông ảnh ưng ý, muốn áp đúng tông đó cho **video** hoặc cho project khác.

**LUT là gì:** một file bảng tra màu (đuôi `.cube`), mang tông màu từ ảnh này sang ảnh, video khác.

**Tạo LUT:**
1. Chuột phải ảnh trong album → **Generate LUT**.
2. Chọn **33 Point Cube** — loại tương thích rộng nhất. Các lựa chọn khác: **17 Point Cube** (nhẹ, thô hơn), **65 Point Cube** (mịn hơn, file to), **Panasonic VLUT** (cho máy Panasonic VariCam).
3. Đặt tên, lưu vào thư mục mặc định `Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/` → **Save**.
4. Nạp lại LUT vào Resolve: **Project Settings → Color Management → Lookup Tables → Update Lists**. Xem [Cài LUT mua/tải về](../color/lut-va-quan-ly-mau.md#cài-lut-muatải-về).

> Chỉ thiết lập ở **tab Photo** được lưu vào LUT. Thiết lập **tab RAW** và **hiệu ứng** thì **không**.

**Áp LUT có sẵn cho ảnh:** chuột phải thumbnail ảnh → **LUT** → chọn.

---

## Reset

Menu **ba chấm** góc trên phải Inspector:

| Lệnh | Phím | Làm gì |
|---|---|---|
| **Reset Photo** | `⌘R` | Bỏ mọi chỉnh sửa ở tab Photo |
| **Remove All Photo Effects** | `⇧R` | Gỡ mọi hiệu ứng |
| **Reset Camera Raw** | — | Bỏ mọi chỉnh sửa ở tab RAW |
| **Remove and Reset All** | `⌘⇧R` | Đưa ảnh về nguyên gốc hoàn toàn |

Các phím tắt chỉ chạy khi **Inspector đang được chọn** — bấm vào Inspector trước.

---

## Cần nhiều công cụ hơn?

Tab RAW và tab Photo đủ cho phần lớn ảnh. Khi cần chỉnh **riêng một vùng** (chỉ làm sáng mặt, chỉ đổi màu trời), đưa album sang trang **Color** để dùng node, Qualifier, Power Window — xem [Đưa album sang trang Color](xuat-anh.md#đưa-album-sang-trang-color).
