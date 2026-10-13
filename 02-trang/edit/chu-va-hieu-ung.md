# Chữ, chuyển cảnh, keyframe

Mọi thứ ở trang này lấy từ panel **Effects** (góc trên trái) → **Toolbox**. Chỉnh thông số trong [Inspector](inspector.md).

---

## Thư viện Effects — cây thư mục

`★★★ Hằng ngày`

Bấm nút **Effects** ở góc trên trái. Bên trái là **cây thư mục**, bên phải là **ô xem trước** các mục trong thư mục đang chọn. Nút góc trên trái ẩn/hiện cây thư mục.

| Thư mục | Bên trong | Mức |
|---|---|---|
| **Toolbox** | Bấm vào là thấy **tất cả** bốn mục con dưới đây cùng lúc | ★★★ |
| ├ **Video Transitions** | Chuyển cảnh hình. Cuối danh sách có nhóm **User** — preset bạn tự lưu | ★★★ |
| ├ **Audio Transitions** | Chuyển cảnh tiếng: **Cross Fade +3 dB**, **Cross Fade −3 dB**, **Cross Fade 0 dB** | ★★☆ |
| ├ **Titles** | Text, Text+, MultiText, Lower 3rd, Scroll, Subtitle, Fusion Titles | ★★★ |
| ├ **Generators** | Nền màu, thanh màu chuẩn, dải xám, Fusion Generators | ★★☆ |
| └ **Effects** | **Adjustment Clip**, **Fusion Composition** — clip "giữ chỗ" để gắn hiệu ứng | ★★☆ |
| **Open FX** | **Filters** — các Resolve FX có sẵn và plugin bên thứ ba. **Transitions**, **Generators** của plugin bên thứ ba | ★★☆ |
| **Audio FX** | **Fairlight FX** có sẵn. Trên Mac còn có plugin **VST** và **AU** đã cài | ★☆☆ |
| **Favorites** | Những mục bạn đã đánh sao | ★★☆ |

### Tìm hiệu ứng nhanh

| Cách | Làm gì |
|---|---|
| **Kính lúp** đầu panel | Gõ tên. Menu bên cạnh chọn tìm **mọi thư mục** hay chỉ thư mục đang mở. Gõ tên nhóm (ví dụ `Stylize`) cũng ra |
| `⇧Space` | Mở hộp **Effects Search** ở giữa màn hình. Đang chọn clip thì bấm vào kết quả là **áp luôn** |
| **Rê chuột** qua ô xem trước | Viewer chạy thử hiệu ứng trên clip đang chọn (hoặc clip dưới con trỏ). Cần bật **Hover Scrub Preview** trong menu ⋯ của panel |
| Bấm **ngôi sao** ở mép phải một mục | Đưa vào **Favorites** |

### Gắn hiệu ứng vào clip — bốn cách

1. Kéo hiệu ứng thả lên clip trên timeline.
2. Chọn clip → **bấm đúp** hiệu ứng.
3. Kéo hiệu ứng thả vào **Inspector**.
4. Kéo hiệu ứng thả lên **Viewer** — áp cho clip đang hiện.

**Áp cho nhiều clip:** chọn các clip → kéo một hiệu ứng **Open FX** thả lên một clip bất kỳ trong nhóm đã chọn.

Chỉnh, sắp thứ tự, tắt, xoá hiệu ứng: [Tab Effects của Inspector](inspector.md#tab-effects).

---

## Chữ — Text, Text+

`★★★ Hằng ngày`

**Effects → Toolbox → Titles**. Kéo mẫu chữ lên **track hình phía trên** clip.

Clip chữ mặc định dài **5 giây**. Đổi mặc định ở **Preferences → User → Editing**.

### Chọn loại nào

| Loại | Mạnh ở | Hạn chế | Dùng cho |
|---|---|---|---|
| **Text** | Nhanh, nhẹ. **Nhiều kiểu chữ trong một tiêu đề** (một chữ đậm, một chữ màu khác) | Ít hiệu ứng | Đoạn chữ thông tin, chú thích |
| **Text+** | Viền, bóng, gradient, **chữ chạy từng ký tự**, Write On | **Cả tiêu đề chỉ một kiểu chữ** | Tiêu đề lớn, chữ có animation |
| **MultiText** | Nhiều lớp chữ, mỗi lớp một kiểu, trong **một** clip. Nhập được file `.csv` thành chữ chia cột | Mới, nhiều nút | Bảng tên, bảng giá, nhiều dòng khác kiểu |
| **L / M / R Lower 3rd** | Tự đặt hai dòng chữ ở góc dưới trái / giữa / phải | — | Tên + chức danh người phỏng vấn |
| **Scroll** | Chữ tự cuộn từ dưới lên | — | Danh sách cảm ơn cuối video |
| **Fusion Titles** | Mẫu có sẵn animation | Chỉnh được ít | Muốn đẹp nhanh, không tự làm |

**Scroll chạy nhanh hay chậm** tuỳ độ dài clip chữ trên timeline — kéo dài ra là chạy chậm lại.

**Subtitle** trong Titles là để thả vào **track phụ đề** — xem [Phụ đề](phu-de.md).

### Text, Text+ hay Fusion Titles — chọn nhanh

| Bạn cần | Chọn |
|---|---|
| Một dòng chữ tĩnh, một từ tô màu khác | **Text** |
| Chữ to có viền, bóng, hiện dần | **Text+** |
| Chữ có hiệu ứng đẹp ngay, không mất công | **Fusion Titles** |
| Chữ nhiều lớp phức tạp, chữ bám theo vật | Text+ rồi mở ở [trang Fusion](../fusion/chu-dong.md) |

> Text+ **chỉnh màu được** ở trang Color như clip thường. Text thường thì không.

### Chỉnh Text (loại thường)

Chọn clip Text → Inspector → tab **Video** → bảng **Title**.

| Nhóm | Chỉnh gì |
|---|---|
| **Rich Text** | Ô chữ, font, kiểu chữ, màu, cỡ, **Tracking** (giãn chữ), **Line Spacing**, gạch chân, chỉ số trên/dưới, **Font Case** (viết hoa hết, viết thường hết…), căn lề, **Anchor**, Position, Zoom, Rotation |
| **Drop Shadow** | Màu, độ lệch, độ mờ, độ trong của bóng đổ |
| **Stroke** | Màu và độ dày viền chữ |
| **Background** | Khung nền sau chữ: màu, viền, rộng, cao, **Corner Radius** (bo góc), độ trong |

**Nhiều kiểu trong một tiêu đề:** bôi đen vài chữ trong ô chữ rồi đổi màu, font — chỉ phần bôi đen đổi. Không bôi đen gì = đổi cả khối.

**Ví dụ — nhãn giá kiểu "sticker":** Text → gõ `120.000đ` → **Background** màu vàng, **Corner Radius** khoảng 20, chữ đen. Bôi đen `đ` → giảm cỡ.

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

Giải thích từng thanh của bốn nhóm: [Chữ động với Text+](../fusion/chu-dong.md#tab-text).

### Sửa chữ ngay trên Viewer

| Việc | Cách |
|---|---|
| Dời, phóng, xoay khối chữ (Text) | Chọn clip chữ → **bấm một lần** vào chữ trên Viewer → kéo khung |
| Gõ sửa chữ | **Bấm đúp** vào chữ trên Viewer |
| Dời tự do, không hít vào giữa khung | Giữ `⌥` khi kéo |
| Chỉ dời ngang hoặc dọc | Giữ `⇧` khi kéo |
| Text+ | Phải bật **Fusion Overlay** trước (xem trên) |

Khi kéo, chữ tự **hít** vào tâm khung và các đường một phần ba.

### Font Browser

| Nút | Làm gì |
|---|---|
| **All Fonts / Favorites** | Mọi font / font đã đánh sao |
| **Thumbnail View / List View** | Xem dạng ô vuông / dạng dòng |
| **Ô tìm** | Gõ một phần tên, ví dụ `Nova` |
| **Filter** | Lọc theo loại: có chân, đơn cách, đậm… |
| **Mũi tên trái/phải** trong một ô | Đổi giữa các kiểu (Regular, Bold…) của cùng họ font |
| Menu ⋯ → **Display User Custom Text** | Xem trước bằng câu tự gõ — gõ câu có dấu `ặ ỡ ữ` để kiểm tra font đủ dấu tiếng Việt |

### Kiểm tra chính tả, emoji

- Chữ sai chính tả bị **gạch đỏ** trên Viewer và Inspector. Chuột phải để xem gợi ý. Tắt gạch đỏ trên Viewer: **View → Show Spelling Errors on Viewer**.
- Chèn emoji vào Text+ và MultiText: `⌃⌘Space`.

### Khung an toàn cho chữ

Nút **Safe Area** góc trên phải Viewer Timeline. Menu bên cạnh có:

| Nhóm | Lựa chọn |
|---|---|
| **Social Media** | 1:1, 4:5, 9:16, 1.91:1, 16:9 — xem phần nào bị cắt khi đăng mạng xã hội |
| **Broadcast and Film** | 1.33, 1.66, 1.77, 1.85, 2.35 |
| **Safe Area Guides** | **Action** (hành động), **Title** (chữ nằm trong khung này), **Center** |

**Dùng khi:** làm bản ngang nhưng sẽ cắt thêm bản dọc → bật **9:16**, giữ chữ quan trọng trong khung đó.

---

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

**Muốn chuyển cảnh, clip phải dư footage** ở hai đầu (phần đã bị cắt bỏ). Nếu `⌘T` báo không đủ media, trim ngắn hai clip vào một chút rồi thử lại — hoặc để Resolve tự làm, xem [Khi không đủ footage](#khi-không-đủ-footage).

### Thêm chuyển cảnh — mọi cách

| Cách | Làm | Mức |
|---|---|---|
| `⌘T` | Chọn điểm nối (bấm, hoặc `V` chọn điểm gần con trỏ) → `⌘T`. Thêm cả hình lẫn tiếng | ★★★ |
| `⌥T` / `⇧T` | Chỉ chuyển cảnh **hình** / chỉ chuyển cảnh **tiếng** | ★★☆ |
| Kéo từ Effects | Thả **lệch trái, giữa, hoặc lệch phải** điểm nối → chuyển cảnh kết thúc ở, nằm giữa, hoặc bắt đầu ở điểm nối | ★★★ |
| Chuột phải điểm nối | Chọn nhanh độ dài: **¼ giây**, **½ giây**, **1 giây**, **2 giây** | ★★☆ |
| Bấm đúp chuyển cảnh trong Effects | Thêm vào **cuối clip** dưới con trỏ | ★☆☆ |
| Chọn nhiều điểm nối → chuột phải chuyển cảnh trong Effects → **Add to Selected Edit Points** | Thêm cùng lúc cho mọi điểm đã chọn | ★★☆ |
| `⇧Space` → gõ tên | Áp vào điểm nối gần con trỏ nhất | ★☆☆ |
| Giữ `⌥⇧` khi kéo mép clip, kéo clip, hoặc kéo clip từ Media Pool chồng lên clip khác | Phần chồng nhau tự thành chuyển cảnh | ★☆☆ |

**Chọn vị trí bằng phím:** chọn điểm nối → bấm `U` để đổi giữa **đầu / giữa / cuối** điểm nối → `⌘T`.

**Ví dụ — cả video 40 điểm cắt, muốn fade đen ở 6 chỗ đổi chương:** `⌘`-bấm chọn 6 điểm nối → chuột phải **Dip to Color Dissolve** trong Effects → **Add to Selected Edit Points**.

### Độ dài và vị trí

| Muốn | Cách |
|---|---|
| Dài/ngắn đều hai bên | Kéo mép chuyển cảnh |
| Chỉ dài/ngắn **một bên** | Giữ `⌘` khi kéo mép |
| Gõ số chính xác | Chọn chuyển cảnh → `⌘D` (**Change Transition Duration**) → gõ → **Change** |
| Đổi vị trí so với điểm nối | Chuột phải chuyển cảnh → chọn kiểu căn, hoặc Inspector → **Alignment** |
| Đổi kiểu chuyển cảnh | Kéo kiểu khác **thả đè** lên chuyển cảnh cũ |
| Dời sang điểm nối khác | Kéo chuyển cảnh sang đó |
| **Chép** sang điểm nối khác | Giữ `⌥` rồi kéo |
| Chép sang nhiều điểm nối | Chọn chuyển cảnh → `⌘C` → giữ `⌘` bấm các điểm nối (chuyển xanh lá) → chuột phải một điểm → **Paste** (`⌘V`) |
| Chọn mọi chuyển cảnh trên timeline | **Timeline → Select Transitions** |

**Độ dài mặc định** khi bấm `⌘T`: 1 giây. Đổi ở **Preferences → User → Editing → Standard transition duration**.

### Chỉnh chuyển cảnh trong Inspector

**Bấm đúp** chuyển cảnh trên timeline → Inspector mở tab **Transition**.

| Thông số | Làm gì |
|---|---|
| **Transition Type** | Đổi sang kiểu chuyển cảnh khác ngay tại chỗ |
| **Duration** | Độ dài, theo giây và theo khung |
| **Alignment** | **Start on Edit** · **Center on Edit** · **End on Edit** |
| **Style** (riêng nhóm Dissolve) | **Video** (đều) · **Film** (như máy in phim) · **Additive** (sáng lên ở giữa) · **Subtractive** (tối đi ở giữa) · **Highlights** · **Shadows** |
| **Start Ratio / End Ratio** | Chuyển cảnh bắt đầu/kết thúc ở bao nhiêu %. End Ratio khác 100 = không bao giờ chuyển hẳn |
| **Reverse** | Đảo chiều (wipe chạy ngược). Mờ với Dissolve |
| **Ease** | **None** · **In** · **Out** · **In & Out** · **Custom** (vẽ bằng **Transition Curve**) |

Các kiểu wipe, iris, shape có thêm **Color** và **Border** (viền màu ở mép), **Feather** (mép mềm), **Preset** (hướng).

**Ví dụ — fade đen giữa hai cảnh:** **Dip to Color Dissolve** → **Color** đen. Muốn fade trắng kiểu hồi tưởng: Color trắng.

### Các nhóm chuyển cảnh có sẵn

| Nhóm | Gồm | Dùng khi |
|---|---|---|
| **Dissolve** | **Cross Dissolve**, **Dip to Color Dissolve**, Additive, Non-Additive, **Blur Dissolve**, **Smooth Cut** | Hằng ngày. Thời gian trôi, đổi cảnh nhẹ nhàng |
| **Iris** | Arrow, Cross, Diamond, Eye, Hexagon, Oval, Pentagon, Square, Triangle | Kiểu phim xưa, video vui nhộn |
| **Motion** | **Barn Door**, **Push**, **Slide**, Split | Đẩy hình — vlog, video nhanh |
| **Shape** | Box, Heart, Star, Triangle Left/Right | Video vui, thiệp mời |
| **Wipe** | Band, Center, **Clock**, Edge, Radial, Spiral, Venetian Blind, X Wipe | Quét hình theo hướng chuyển động |
| **Fusion Transitions** | Brightness Flash, Camera Shake, Crash Zoom, Glitch, Zoom In, Slide, Tunnel of Light… | Hiệu ứng mạnh cho video ngắn mạng xã hội |
| **Resolve FX Transitions** | **Burn Away** — phim cháy | Kiểu retro |
| **User** | Preset bạn đã lưu | Kiểu riêng dùng lại |

> **Smooth Cut** làm mờ cú giật khi cắt bỏ "ờ, à" giữa câu phỏng vấn. Để thật ngắn: 2–6 khung. Nó dựa trên **AI Speed Warp**, vốn thuộc nhóm tính năng `Studio` — thử trên bản free của bạn trước khi tính dùng.

> **Glitch** đẹp nhất khi chỉ dài vài khung.

### Preset và chuyển cảnh mặc định

| Việc | Cách |
|---|---|
| Lưu chuyển cảnh đã chỉnh thành preset | Chuột phải chuyển cảnh trên timeline → **Create Transition Preset** → đặt tên. Hiện trong nhóm **User** |
| Xoá preset | Chuột phải preset → **Delete Transition Preset** |
| Đặt làm mặc định cho `⌘T` | Chuột phải chuyển cảnh trong Effects → **Set as Standard Transition**. Có **chấm cam** cạnh tên |
| Sửa sâu bằng node | Chuột phải chuyển cảnh → **Convert to Fusion Cross Dissolve** → chuột phải lần nữa → **Open in Fusion Page** |

**Ví dụ:** vlog dùng toàn **Dip to Color Dissolve** màu trắng dài 8 khung → chỉnh một cái → **Create Transition Preset** → **Set as Standard Transition**. Từ đó `⌘T` ra đúng kiểu đó.

### Khi không đủ footage

Bấm `⌘T` (hoặc chọn độ dài từ chuột phải) mà clip không dư đủ hai đầu → hộp thoại ba lựa chọn:

| Nút | Làm gì |
|---|---|
| **Trim Clips** | Tự cắt ngắn hai clip vừa đủ để thêm chuyển cảnh |
| **Skip Clips** | Bỏ qua điểm nối không đủ, chỉ thêm ở chỗ đủ |
| **Cancel** | Huỷ |

---

## Generators — nền màu, thanh màu

`★★☆ Thường dùng`

**Effects → Toolbox → Generators**. Kéo xuống timeline như clip thường. Mặc định dài 5 giây.

| Generator | Là gì | Dùng khi | Mức |
|---|---|---|---|
| **Solid Color** | Nền một màu. Đổi màu ở Inspector → **Color** | Nền cho chữ, khoảng đen giữa hai phần, nền tiêu đề | ★★★ |
| **Four Color Gradient** | Bốn màu ở bốn góc hoà vào nhau. Chỉnh **Center X/Y** và bốn màu | Nền chuyển màu cho intro, thumbnail | ★★☆ |
| **Window** | Hình chữ nhật trắng trên nền đen | Làm mask, đặt dưới chữ rồi trộn bằng Composite | ★☆☆ |
| **Grey Scale**, **10 Step**, **100mV Steps** | Dải xám từ đen tới trắng | Kiểm tra màn hình, kiểm tra LUT | ★☆☆ |
| **SMPTE Color Bar**, **EBU Color Bar** | Thanh màu chuẩn | Đầu file giao đài truyền hình | ★☆☆ |
| **BT.2111 Color Bar** (HLG, PQ) | Thanh màu chuẩn HDR | Chỉ khi làm HDR | ★☆☆ |
| **YCbCr Ramp** | Dải chuyển kiểm tra tín hiệu | Kỹ thuật | ★☆☆ |
| **Fusion Generators** | Generator làm bằng Fusion, ví dụ **Noise Gradient** | Nền động. Mở trang Fusion để sửa | ★☆☆ |

Generator (trừ Solid Color) **không có thông số riêng** — chỉ có Composite, Transform, Cropping, Dynamic Zoom như mọi clip, và ô **Display Name** để đặt tên.

**Ví dụ — thẻ chương giữa video:** Solid Color đen dài 2 giây → Text đặt lên track trên → Cross Dissolve ở hai đầu.

**Ví dụ — nền chữ chạy ngang dưới đáy:** Solid Color → Inspector → **Cropping** cắt chỉ còn một dải dưới đáy → **Opacity** 70.

### Ảnh tĩnh

Ảnh `.png`, `.tif`, `.exr`, `.tga` giữ được **nền trong suốt**. `.jpg`, `.psd` thì không. Ảnh tĩnh có đủ Composite, Transform, Cropping, Retime, Scaling như clip.

**File Photoshop:** chuột phải file `.psd` trên timeline → **Split PSD Layers in Place** → mỗi layer thành một track riêng.

**Sửa ảnh ở app khác:** mở ảnh trong Photoshop hoặc app chỉnh ảnh, lưu lại — Viewer của Resolve tự cập nhật.

---

## Open FX — hiệu ứng có sẵn

`★★☆ Thường dùng`

**Effects → Open FX → Filters**. Các hiệu ứng tên **Resolve FX**, chia nhóm Blur, Color, Light, Stylize, Transform… Kéo lên clip, chỉnh ở [tab Effects](inspector.md#tab-effects).

Những cái **dùng được ở bản free** (manual không đánh dấu Studio) và hay cần:

| Hiệu ứng | Làm gì | Dùng khi |
|---|---|---|
| **Gaussian Blur** | Làm mờ đều | Nền mờ hai bên video dọc, che thông tin |
| **Mosaic Blur** | Làm vỡ ô | Che mặt, biển số xe |
| **Zoom Blur**, **Radial Blur**, **Directional Blur** | Mờ theo hướng | Nhấn cảm giác tốc độ, chuyển cảnh tự chế |
| **Box Blur**, **Prism Blur** | Mờ hộp, mờ tách màu | Hiệu ứng nghệ thuật |
| **Glow** | Vùng sáng toả sáng | Cảnh đèn đêm, cảm giác mơ |
| **Light Rays** | Tia sáng toả ra từ vùng sáng | Nắng xuyên qua cây, logo intro |
| **Vignette** | Tối dần ra mép | Hướng mắt vào giữa — nhanh hơn làm ở trang Color |
| **Drop Shadow** | Bóng đổ cho lớp có nền trong suốt | Logo, ảnh PNG đặt lên video |
| **Mirrors** | Soi gương, lật đối xứng | Hiệu ứng vui, kaleidoscope |
| **Edge Detect** | Chỉ giữ đường viền | Hiệu ứng phác thảo |
| **Video Collage** | Chia khung thành lưới nhiều ô | Ghép nhiều cảnh trong một khung |
| **Transform**, **Picture in Picture** | Dời, phóng, khung hình nhỏ có viền và bóng | Hình trong hình |
| **Blanking Fill** | Lấp viền đen bằng hình mờ | Clip dọc trên timeline ngang |
| **Film Damage** | Vết xước, bụi phim cũ | Cảnh hồi tưởng |
| **Stop Motion** | Giật khung như phim tĩnh vật | Phong cách stop-motion |

**Hay gặp là `Studio`** (bản free không dùng được): **Film Grain**, **Lens Flare**, **Noise Reduction**, **Sharpen**, **Camera Shake**, **Lens Blur**, **Tilt-Shift Blur**, **Beauty**, **Face Refinement**, **Dehaze**, **Deflicker**, **Object Removal**, **Warper**.

**Mọi Resolve FX có thanh Blend** ở cuối — kéo xuống để hiệu ứng nhẹ đi.

**Ví dụ — video dọc điện thoại trên timeline ngang, hai bên mờ:**
1. Đặt clip dọc ở **V2**. Inspector → **Scaling** → **Fit**.
2. `⌥`-kéo bản sao xuống **V1**. Inspector → **Zoom** khoảng 3.2 cho lấp đầy khung.
3. Kéo **Gaussian Blur** lên clip ở V1, tăng độ mờ. Hạ **Opacity** hoặc kéo thanh sáng tối nếu nền rối.

> Hiệu ứng nặng làm phát giật: chuột phải clip → **Render in Place** — Resolve xuất thành file mới thay vào timeline. Muốn sửa lại: chuột phải → **Decompose to Original**.

---

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

### Thêm keyframe ngay khi đang phát

| Phím | Làm gì |
|---|---|
| `⌘[` | **Mark → Add Keyframe** tại con trỏ, kể cả khi đang phát |
| `⌥]` | **Mark → Delete Keyframe** đang chọn |

Resolve **tự đoán** thông số cần đặt, theo thứ tự: thanh tốc độ (nếu đang mở `⌘R`) → đường cong đang mở trong Keyframe Editor → thông số Inspector bạn vừa chỉnh → **âm lượng clip**. Clip chưa chỉnh gì thì `⌘[` đặt keyframe âm lượng.

### Keyframe Editor — xem mọi keyframe

Hai chỗ mở:

| Chỗ | Mở bằng | Hợp với |
|---|---|---|
| **Khay keyframe** dưới clip | Nút **Keyframe Editor** (Show Keyframe Tray) trên thanh công cụ timeline | Xem nhanh keyframe của clip đang chọn ngay trên timeline |
| **Bảng Keyframes** riêng | Nút **Keyframes** góc trên trái | Nhiều keyframe, cần chỗ rộng. Nút **Expand** mở thành cửa sổ riêng |

Mỗi thông số là **một hàng**, gom theo nhóm (Transform, Cropping, Speed…). Kéo keyframe trên **hàng nhóm** là dời mọi keyframe cùng chỗ trong nhóm.

| Việc | Cách |
|---|---|
| Chọn nhiều keyframe | `⌘`-bấm từng cái, hoặc kéo khung quanh |
| Dời keyframe | Kéo trái/phải |
| Copy, dán keyframe | Chọn → `⌘C` → đặt con trỏ → `⌘V` |
| Xoá | Chọn → `Delete` |
| Chỉ hiện hàng đã có keyframe | Menu ⋯ cột tên → **Display Parameters with Keyframes** |
| Gập/mở mọi nhóm | Menu ⋯ → **Collapse All Parameters** / **Expand All Parameters** |
| Khoá một hàng khỏi sửa nhầm | Icon **khoá** ở đầu hàng |

> Trim clip ngắn lại mà keyframe nằm ngoài clip → keyframe hiện thành **mũi tên**. Vẫn nhảy tới được bằng `[` `]`.

### Curve Editor — chỉnh độ mượt

`★☆☆ Tình huống cụ thể`

Bấm icon **Curve** góc trên trái Keyframe Editor. Mỗi thông số có keyframe là một **đường màu** — màu trùng chấm màu ở Keyframe Editor. Rê chuột lên đường để xem tên và giá trị.

**Thanh công cụ Curve Editor:**

| Nút | Làm gì |
|---|---|
| **Linear** | Đi thẳng, đều tốc từ keyframe này sang keyframe kia |
| **Ease In** / **Ease Out** / **Ease In and Out** | Chậm lúc đầu / chậm lúc cuối / chậm cả hai đầu |
| **Step In** / **Step Out** | Đổi giá trị **tức thì**, không chuyển dần |
| **Add Keyframes** | Bấm lên đường là thêm điểm |
| **Shape Box** | Kéo khung quanh nhiều điểm để co giãn cả cụm |
| **Hand** | Kéo để dời vùng nhìn khi đã phóng to |
| **Flat Handle** | Khoá tay nắm nằm ngang |

| Thao tác | Kết quả |
|---|---|
| `⌥`-bấm lên đường | Thêm điểm |
| Kéo điểm | Ngang = đổi thời điểm, dọc = đổi giá trị |
| `⇧`-kéo | Chỉ dời theo một chiều |
| Kéo **tay nắm Bezier** | Uốn cong — chỉnh độ tăng tốc |

Menu ⋯ có **Reverse Keyframes** (đảo thứ tự) và **Loop Type** (lặp lại chuyển động).

**Ví dụ — chữ bật vào rồi khựng lại:** keyframe **Position X** hai điểm → chọn điểm sau → **Ease Out**. Kéo tay nắm cho đoạn cuối thật thoải.

### Đường chuyển động trên Viewer

Keyframe **Position** tạo ra một **đường đi** trên Viewer (bật menu overlay góc dưới trái → **Transform**).

- Điểm trên đường mặc định là góc nhọn. Chuột phải điểm → **Smooth** để thành đường cong.
- Kéo tay nắm để uốn. `⌘`-kéo một tay nắm để bẻ góc riêng hai bên.
- **Chấm** dọc đường: chấm **dày** = chạy chậm, chấm **thưa** = chạy nhanh.
- Xoá điểm: chuột phải → **Delete Keyframe**.

---

## Adjustment Clip

`★★☆ Thường dùng`

**Effects → Toolbox → Effects → Adjustment Clip**. Kéo lên track **trên cùng**, kéo dài phủ những clip muốn tác động.

Mọi hiệu ứng, Transform, chỉnh màu áp lên Adjustment Clip sẽ **tác động lên toàn bộ clip phía dưới**.

**Dùng khi:**
- Áp một tông màu cho cả đoạn — chỉnh màu Adjustment Clip ở trang Color.
- Zoom nhẹ cả đoạn để giấu rìa.
- Làm bản dọc từ bản ngang mà không đụng clip gốc.

**Áp được gì:**

| Loại | Ví dụ |
|---|---|
| Resolve FX, Open FX | Gaussian Blur, Glow, Vignette |
| Thông số Inspector | Composite, Transform, Cropping, Dynamic Zoom |
| Hiệu ứng Fusion | Mở trang Fusion khi con trỏ nằm trên Adjustment Clip |
| Màu và Sizing trang Color | Một LUT, một tông cho cả cảnh |

**Mẹo:**
- **Đặt tên** Adjustment Clip ở Inspector — ví dụ `Tong am`, `Zoom 9x16`.
- **Lưu để dùng lại:** kéo Adjustment Clip từ timeline vào Media Pool.
- Muốn **tắt nhanh** để so: tắt track chứa nó, hoặc chọn rồi `D` (tắt clip).
- Xếp chồng hai Adjustment Clip: cái trên tác động lên cả cái dưới.

**Ví dụ — fade cả đoạn ra đen một lần:** Adjustment Clip phủ 3 giây cuối → keyframe **Opacity** 100 → 0. Mọi track bên dưới mờ cùng lúc.

> Muốn chỉ gom vài clip chồng nhiều track thành một khối để thêm chuyển cảnh: dùng [Compound Clip](timeline-nang-cao.md#compound-clip--gộp-nhiều-clip-thành-một) thay vì Adjustment Clip.
