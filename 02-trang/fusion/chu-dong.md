# Chữ động với Text+

**Text+** là node tạo chữ của Fusion. Nó vẽ chữ trên **nền trong suốt**, nên bạn ghép lên video bằng [Merge](node-co-ban.md#merge--ghép-hai-lớp).

Text+ dùng được mọi font cài trên máy (TrueType, OpenType, PostScript), gõ được tiếng Việt có dấu.

---

## Text+ ở trang Edit hay trang Fusion

Cùng một công cụ. Text+ ở trang Edit (**Effects → Titles → Text+**) chính là node Text+ của Fusion, chỉ khác chỗ chỉnh.

| | Text+ ở trang Edit | Text+ ở trang Fusion |
|---|---|---|
| Bốn tab Text, Layout, Transform, Shading | Có | Có |
| Keyframe | Có | Có, thêm Spline Editor để chỉnh độ mượt |
| Ghép thêm lớp: nền, mask, hình khác | Không | Có |
| Chữ bám theo vật chuyển động | Không | Có (Tracker) |
| Tốc độ làm | Nhanh | Chậm hơn |

**Mẹo:** tạo Text+ ở trang Edit, đặt con trỏ lên nó rồi sang trang Fusion — bạn thấy nó đã là một node Text+ thật, tiếp tục thêm lớp từ đó.

> Chỉ cần chữ tĩnh, tiêu đề, phụ đề tay → làm ở [trang Edit](../edit/chu-va-hieu-ung.md). Sang Fusion khi cần nhiều lớp hoặc hiệu ứng chạy theo từng ký tự.

---

## Thêm Text+ và ghép lên video

`★★★ Hằng ngày`

1. Bấm khoảng trống trong Node Editor để **bỏ chọn** mọi node.
2. Bấm icon **Text** trên thanh công cụ, hoặc `⇧Space` gõ `text+`, `Return`. Node **Text1** đứng riêng.
3. Kéo **đầu ra** Text1 thả lên **đầu ra** MediaIn1. Fusion tự tạo Merge, chữ ở lớp trên.
4. Chọn MediaOut1, bấm `2` để xem kết quả. Chọn Text1 để chỉnh ở Inspector.

Text+ có sáu tab trong Inspector: **Text**, **Layout**, **Transform**, **Shading**, **Image**, **Settings**. Bốn tab đầu là thứ bạn dùng.

---

## Gõ chữ ngay trên Viewer

Khi chọn Text+, một **thanh công cụ chữ** hiện ra trên Viewer. Bấm đúp vào Viewer để vào chế độ gõ chữ trực tiếp, dùng `←` `→` di chuyển con trỏ, `↑` `↓` đổi dòng.

| Nút | Làm gì |
|---|---|
| **Allow Typing in Viewer** | Gõ, sửa chữ ngay trên hình |
| **Allow Manual Kerning** | Kéo từng ký tự xích lại gần hoặc ra xa. Chọn ký tự, giữ `⌥` + `←` `→` để nhích; thêm `⇧` để nhích nhiều |
| **No Text Outline / Outside Frame Only / Show Always** | Hiện khung viền quanh chữ để dễ tìm. **Outside Frame Only** giúp thấy chữ đang nằm ngoài khung hình |

---

## Tab Text

`★★★ Hằng ngày`

**Là gì:** nội dung chữ và định dạng cơ bản — giống trình soạn thảo văn bản.

| Thông số | Làm gì | Mức |
|---|---|---|
| **Ô chữ** (Styled Text) | Gõ nội dung. Có kiểm tra chính tả — từ sai gạch đỏ, chuột phải để xem gợi ý | ★★★ |
| **Font** | Hai menu: họ font và kiểu (Regular, Bold, Italic…) | ★★★ |
| **Color** | Màu chữ | ★★★ |
| **Size** | Cỡ chữ. Tính theo **bề ngang khung hình**, không phải point như Word | ★★★ |
| **Tracking** | Khoảng cách đều giữa các ký tự | ★★☆ |
| **Line Spacing** | Khoảng cách giữa các dòng | ★★☆ |
| **V Anchor / H Anchor** | Căn trên–giữa–dưới, trái–giữa–phải. Cũng là **tâm xoay** của chữ | ★★☆ |
| **V Justify / H Justify** | Dàn đều chữ, dùng khi Layout là **Frame** | ★☆☆ |
| **Emphasis** | Gạch chân, gạch ngang | ★☆☆ |
| **Write On** | Thanh hai đầu **Start** và **End** — hiện dần hoặc ẩn dần chữ | ★★★ |
| **Advanced Controls** | Kerning theo font, ligature | ★☆☆ |

**Chèn emoji:** `⌃⌘Space` trong ô chữ.

### Write On — chữ hiện dần như đang gõ

`★★★ Hằng ngày`

**Là gì:** thanh **Write On** có hai đầu. Mặc định **Start** `0`, **End** `1` — hiện đủ chữ. Kéo End xuống thì phần cuối chữ biến mất.

**Cách làm hiệu ứng gõ chữ:**
1. Đặt con trỏ ở khung bắt đầu. Kéo **End** về `0`, bấm nút keyframe bên phải Write On.
2. Đi tới khung kết thúc (ví dụ 1 giây sau). Kéo **End** về `1`. Keyframe tự tạo.

Ngược lại, **chữ biến mất dần:** keyframe **Start** từ `0` lên `1`.

---

## Tab Layout

`★★★ Hằng ngày`

**Là gì:** vị trí và **kiểu sắp xếp** cả khối chữ. Đây là tab bạn keyframe để **chữ trượt, xoay, phóng** cả khối.

**Type — bốn kiểu sắp chữ:**

| Type | Chữ nằm thế nào | Dùng khi |
|---|---|---|
| **Point** (mặc định) | Quanh một điểm tâm | Tiêu đề, chữ thường |
| **Frame** | Trong một khung chữ nhật, có căn lề | Đoạn văn nhiều dòng |
| **Circle** | Dọc theo vòng tròn hoặc ellipse | Chữ vòng quanh logo |
| **Path** | Dọc theo một đường bạn vẽ | Chữ chạy theo đường cong. Keyframe **Position on Path** để chữ trượt dọc đường |

**Thông số khác:**

| Thông số | Làm gì | Mức |
|---|---|---|
| **Center X / Y** | Vị trí khối chữ. Cũng kéo được trực tiếp trên Viewer | ★★★ |
| **Size** | Phóng cả khối chữ | ★★☆ |
| **Rotation** + **Angle X / Y / Z** | Xoay khối chữ, kể cả xoay 3D | ★★☆ |
| **Perspective** | Tăng giảm hiệu ứng phối cảnh khi xoay X, Y | ★☆☆ |
| **Width / Height** | Kích thước khung (Frame) hoặc vòng (Circle) | ★☆☆ |
| **Background Color** | Màu nền sau chữ — mặc định trong suốt | ★☆☆ |

---

## Tab Transform

`★★☆ Thường dùng`

**Là gì:** biến đổi **từng ký tự, từng từ, hoặc từng dòng** riêng rẽ — mỗi phần quay quanh tâm của chính nó. Khác tab Layout (biến đổi cả khối).

**Menu Transform** chọn đơn vị: **Characters**, **Words**, hoặc **Lines**. Ba mức áp được cùng lúc; menu này chỉ để đổi bộ thông số đang hiện.

| Thông số | Làm gì |
|---|---|
| **Spacing** | Giãn cách giữa các ký tự/từ/dòng. Nhỏ hơn 1 thì chồng lên nhau |
| **Pivot X / Y / Z** | Dời tâm xoay của từng phần |
| **X, Y, Z** (Rotation) | Xoay từng phần quanh trục |
| **Shear X / Y** | Nghiêng từng phần |
| **Size X / Y** | Co giãn từng phần |

**Ví dụ:** chọn **Characters**, keyframe **Y** (rotation) từ `90` về `0` — mỗi ký tự lật như tấm bảng từ cạnh ra mặt. Kết hợp với [Follower](#follower--chữ-hiện-lần-lượt) để các ký tự lật lần lượt thay vì cùng lúc.

---

## Tab Shading

`★★☆ Thường dùng`

**Là gì:** **tối đa tám lớp hiệu ứng** chồng lên cùng một dòng chữ: lớp màu chữ, viền, bóng đổ, khung nền… Đây là thứ làm Text+ mạnh hơn hẳn chữ thường.

**Cách làm:** chọn số lớp **1–8** ở hàng số trên cùng → tích **Enabled** → chỉnh. Lớp 1 là màu chữ, bật sẵn.

**Appearance — lớp này vẽ cái gì:**

| Appearance | Vẽ |
|---|---|
| **Text Fill** | Tô đầy chữ (mặc định) |
| **Text Outline** | Viền quanh chữ |
| **Border Fill** | Khối nền quanh chữ — theo cả đoạn, từng dòng, từng từ hoặc từng ký tự (mục **Level**) |
| **Border Outline** | Viền quanh khối nền |

**Thông số hay dùng:**

| Thông số | Làm gì | Mức |
|---|---|---|
| **Opacity** | Độ đậm lớp này | ★★★ |
| **Color Type** | **Solid** (một màu), **Gradient**, hoặc **Image** (lấy hình từ node khác tô vào chữ) | ★★☆ |
| **Thickness** | Độ dày viền (chỉ Outline) | ★★☆ |
| **Outside Only** | Viền chỉ nằm ngoài, không ăn vào chữ | ★★☆ |
| **Join Style** | Góc viền: nhọn, tròn, vát | ★☆☆ |
| **Round** | Bo góc khối nền (Border) | ★★☆ |
| **Extend Horizontal / Vertical** | Nới khối nền rộng ra | ★★☆ |
| **Softness X / Y** | Làm mềm, nhoè lớp này | ★★☆ |
| **Offset X / Y** | Dời lớp này lệch khỏi chữ | ★★☆ |
| **Priority Back / Front** | Lớp nào nằm trên, lớp nào nằm dưới | ★☆☆ |

**Ví dụ — chữ trắng viền đen có bóng đổ:**

| Lớp | Appearance | Chỉnh |
|---|---|---|
| 1 | Text Fill | Màu trắng |
| 2 | Text Outline | Màu đen, **Thickness** nhỏ, **Outside Only** |
| 3 | Text Fill | Màu đen, **Opacity** `0.6`, **Softness** khoảng `5`, **Offset** `0.005, -0.005` |

Mặc định lớp số nhỏ nằm trên, lớp số lớn nằm dưới — nên bóng đổ đặt ở lớp số lớn.

**Ví dụ — nhãn tên có khối nền bo góc:** lớp 2 chọn **Border Fill**, **Level** = Text, màu đen, Opacity `0.7`, **Round** cho bo góc, **Extend** cho khối rộng hơn chữ.

---

## Làm chữ chuyển động bằng keyframe

`★★★ Hằng ngày`

Mọi thông số có **hình thoi nhỏ** bên phải đều keyframe được. Cách làm chung — chi tiết ở [Keyframe và Spline](keyframe-va-spline.md):

1. Đặt con trỏ ở thời điểm thứ nhất. Chỉnh giá trị. Bấm hình thoi → chuyển cam.
2. Đặt con trỏ ở thời điểm thứ hai. Chỉnh giá trị. Keyframe **tự tạo**.

**Các kiểu chuyển động hay dùng và keyframe ở đâu:**

| Hiệu ứng | Tab | Keyframe thông số |
|---|---|---|
| Trượt vào từ mép | Layout | **Center X** (hoặc Y) |
| Phóng to dần | Layout | **Size** |
| Hiện dần, mờ dần | Shading (lớp 1) | **Opacity** |
| Gõ chữ | Text | **Write On** (End) |
| Giãn chữ rộng dần | Text | **Tracking** |
| Lật 3D cả khối | Layout | **Angle Y** |
| Từng ký tự bay vào | Transform + Follower | Xem bên dưới |

> **Chữ chạy mượt hơn:** keyframe tạo chuyển động đều, dừng cái cụp. Mở **Spline**, chọn các keyframe, bấm `⇧S` để chậm dần ở cuối. Xem [Làm chuyển động mượt](keyframe-va-spline.md#làm-chuyển-động-mượt).

---

## Follower — chữ hiện lần lượt

`★☆☆ Tình huống cụ thể`

**Là gì:** modifier làm **một hiệu ứng chạy lần lượt qua từng ký tự**, thay vì mọi ký tự cùng lúc. Kiểu "chữ rơi xuống từng chữ một".

**Dùng khi:** intro, tiêu đề có nhịp. Cảm giác chuyên nghiệp hơn hẳn chữ trượt cả khối.

**Cách làm:**
1. Chuột phải vào **ô chữ** (Styled Text) ở tab Text → **Follower**.
2. Mở trang **Modifiers** ở đầu Inspector. Follower có các tab **Text**, **Alignment**, **Transform**, **Shading** (giống Text+) và tab **Timing**.
3. Trong các tab đó, **keyframe** thông số bạn muốn chạy. Ví dụ: ở tab Shading, khung 0 kéo **Opacity** về `0`; khung 15 kéo về `1`.
4. Sang tab **Timing**, chọn **Order** và **Delay**.

> **Quan trọng:** trong Follower, chỉ đổi giá trị mà **không keyframe** thì không có tác dụng gì. Phải có ít nhất hai keyframe.

**Timing — Order (chạy theo hướng nào):**

| Order | Chạy |
|---|---|
| **Left to right** | Trái sang phải |
| **Right to left** | Phải sang trái |
| **Inside out** | Từ giữa ra hai bên |
| **Outside in** | Từ hai bên vào giữa |
| **Random but one by one** | Ngẫu nhiên, từng ký tự một |
| **Completely random** | Ngẫu nhiên, nhiều ký tự cùng lúc |
| **Manual curve** | Tự chỉnh bằng thanh trượt |

Dấu cách cũng tính là một ký tự.

**Timing — Delay Type:**

| Delay Type | Nghĩa |
|---|---|
| **Between Each Character** | Ký tự sau bắt đầu trễ hơn ký tự trước N khung. Chữ càng dài, hiệu ứng càng lâu |
| **Between First and Last Character** | Tổng thời gian cố định, dù chữ dài hay ngắn |

**Range:** chạy cho mọi ký tự, hoặc chỉ một đoạn — quét chọn ký tự ngay trên Viewer.

---

## Các modifier khác của Text+

Chuột phải ô chữ để gắn. Thông số nằm ở trang **Modifiers** của Inspector.

| Modifier | Làm gì | Mức |
|---|---|---|
| **Character Level Styling** | Đổi font, màu, cỡ cho **riêng vài ký tự**. Chọn ký tự trên Viewer rồi chỉnh | ★★☆ |
| **Text Scramble** | Đổi ký tự ngẫu nhiên. Keyframe **Randomness** từ `1` về `0` → chữ "giải mã" dần ra chữ thật | ★☆☆ |
| **Text Timer** | Đồng hồ đếm ngược, bấm giờ, hoặc giờ hệ thống | ★☆☆ |
| **Time Code** | Hiện timecode của khung đang phát | ★☆☆ |
| **Comp Name** | Hiện tên comp — dùng làm slate | ★☆☆ |

---

## Lưu thành Fusion Title dùng lại ở trang Edit

`★☆☆ Tình huống cụ thể`

**Là gì:** biến comp chữ bạn làm thành **một mẫu title** hiện trong **Effects → Titles → Fusion Titles** ở trang Edit. Lần sau chỉ cần kéo vào timeline, sửa chữ ở Inspector — không cần mở Fusion.

**Dùng khi:** kênh YouTube có intro, lower third dùng lặp lại ở mọi video.

**Cách làm:**
1. Làm xong comp chữ (Text+, Background, Merge…).
2. Chọn **mọi node trong mẫu, trừ MediaIn và MediaOut**. Mẹo: `⌘`-click từng node theo thứ tự bạn muốn các thông số hiện ra sau này.
3. Chuột phải một node đã chọn → **Macro → Create Macro**.
4. Cửa sổ **Macro Editor** mở ra. Gõ tên ở ô **Macro Name**.
5. Mở từng node trong danh sách, tích cột **Export** cho thông số muốn sửa được từ trang Edit — thường là **Styled Text** và **Color**. Đừng tích hết.
6. Bấm **Close**, chọn lưu. Muốn mẫu hiện trong Titles của trang Edit, lưu vào:
   `Macintosh HD/Users/<tên bạn>/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Templates/Edit/Titles`
7. **Thoát và mở lại** Resolve. Mẫu hiện trong **Effects → Titles → Fusion Titles**.

Trong Macro Editor, menu ba chấm có **Save to Edit Template** — chọn loại **Title**, **Generator**, **Effect** hoặc **Transition** để lưu thẳng thành mẫu cho trang Edit và Cut.

> **Mẫu có sẵn:** Resolve kèm sẵn nhiều Fusion Titles. Mở một cái trong Fusion (kéo vào timeline, đặt con trỏ lên, sang trang Fusion) để xem nó được dựng bằng node gì — cách học nhanh nhất.
