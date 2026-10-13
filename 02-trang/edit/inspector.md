# Inspector — phóng to, crop, tốc độ

Chọn clip trên timeline → bấm **Inspector** góc trên phải (hoặc `⌘9` để đưa focus vào nó). Tab **Video** chứa gần hết những gì bạn cần.

Các mục **Transform, Cropping, Dynamic Zoom, Composite, Stabilization** ở trang Edit **giống hệt** trang Cut — xem giải thích đầy đủ từng thanh ở [Tools trang Cut](../cut/tools.md). Trang này nói cách dùng hay gặp nhất, và những gì **chỉ trang Edit có**.

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

---

## Sáu tab của Inspector

`★★★ Hằng ngày`

Trên cùng Inspector là hàng tab. Tab nào **không áp dụng** cho thứ đang chọn thì **mờ đi**, không bấm được.

| Tab | Hiện khi chọn | Dùng để | Mức |
|---|---|---|---|
| **Video** | Clip hình, chữ, generator | Phóng, dời, crop, trộn lớp, tốc độ, chống rung | ★★★ |
| **Audio** | Clip tiếng, đầu track tiếng | Âm lượng, pan, cao độ, EQ | ★★★ |
| **Effects** | Clip đã gắn hiệu ứng | Chỉnh Open FX, Fusion FX, Audio FX đã kéo vào clip | ★★☆ |
| **Transition** | Chuyển cảnh (bấm đúp nó trên timeline) | Độ dài, vị trí, kiểu chuyển | ★★☆ |
| **Image** | Clip RAW (BRAW, R3D…) | Chỉnh thông số RAW của máy quay | ★☆☆ |
| **File** | Mọi clip | Thông tin file, metadata, cấu hình kênh tiếng, timecode | ★☆☆ |

### Ba nút trên mỗi nhóm thông số

Mỗi nhóm (Transform, Cropping…) có một **thanh tiêu đề**:

| Nút / thao tác | Ở đâu | Làm gì |
|---|---|---|
| **Công tắc** | Bên trái tên nhóm | Tắt/bật cả nhóm **mà không mất số đã chỉnh**. Cam = bật, xám = tắt |
| **Bấm đúp tên nhóm** | Tên nhóm | Mở/gập nhóm |
| `⌥` + bấm đúp tên nhóm | Tên nhóm | Mở/gập **mọi** nhóm cùng lúc |
| **Reset** | Bên phải tên nhóm | Đưa cả nhóm về mặc định, xoá luôn keyframe của nhóm |

**So trước/sau nhanh nhất:** bấm công tắc của nhóm Transform — hình về như gốc. Bấm lại là các số cũ quay về.

### Inspector hiện clip nào?

| Tình huống | Inspector hiện |
|---|---|
| Có chọn clip | Clip đang chọn |
| Không chọn gì | Clip ở **track cao nhất** dưới con trỏ |
| Chọn nhiều clip | Tiêu đề ghi **Multiple Clips** — chỉnh một lần cho tất cả. Xem [Chỉnh nhiều clip cùng lúc](#chỉnh-nhiều-clip-cùng-lúc) |
| Bật **Timeline → Selection Follows Playhead** | Luôn là clip dưới con trỏ — tiện khi đi qua từng clip để chỉnh |

---

## Tab Video

Thứ tự các nhóm từ trên xuống: Transform · Smart Reframe · Cropping · Dynamic Zoom · Composite · Speed Change · Stabilization · Lens Correction · Retime and Scaling · Super Scale.

### Transform

`★★★ Hằng ngày` — giải thích từng thanh: [Transform trang Cut](../cut/tools.md#transform--phóng-to-dời-xoay)

**Zoom**, **Position**, **Rotation Angle**, **Anchor Point**, **Pitch**, **Yaw**, **Flip** (hai nút lật ngang, lật dọc).

**Mẹo:** nút **xích** giữa Zoom X và Y. Bật = giữ tỉ lệ. Tắt = kéo giãn một chiều — dùng để nắn file bị méo tỉ lệ.

### Smart Reframe

`Studio`

AI tự dò chủ thể và dời khung theo khi đổi tỉ lệ (ngang 16:9 sang dọc 9:16). Có **Object of Interest** (Auto / Reference Point), **Mode** (Auto / Pan Only / Tilt Only), nút **Reframe**.

**Bản free thay bằng:** keyframe **Position X** — xem [Keyframe trong Inspector](#keyframe-trong-inspector) và [Video dọc](../../03-luong/video-doc.md).

### Cropping

`★★☆ Thường dùng` — chi tiết: [Crop trang Cut](../cut/tools.md#crop--cắt-rìa)

**Crop Left / Right / Top / Bottom**, **Softness**, **Retain Image Position**. Phần bị crop thành **trong suốt** — thấy track bên dưới, hoặc đen nếu không có gì.

### Dynamic Zoom

`★★☆ Thường dùng` — cách kéo khung: [Dynamic Zoom trang Cut](../cut/tools.md#dynamic-zoom--zoom-chậm-tự-động)

Tắt sẵn. Bật công tắc mới có tác dụng. Trong Inspector chỉ có hai thứ: **Dynamic Zoom Ease** (Linear, Ease In, Ease Out, Ease In and Out) và nút **Swap** đảo chiều.

### Composite

`★☆☆ Tình huống cụ thể` — bảng các kiểu trộn: [Composite trang Cut](../cut/tools.md#composite--trộn-hai-lớp-hình)

**Composite Mode** và **Opacity**. Chỉ có tác dụng khi clip nằm **trên** clip khác.

### Speed Change

`★★☆ Thường dùng`

| Thông số | Làm gì |
|---|---|
| **Direction** | Tiến, lùi, hoặc đứng hình |
| **Speed %** | Tốc độ theo %. Đặt keyframe được |
| **Frames Per Second** | Tốc độ theo số khung/giây. Đặt keyframe được |
| **Duration** | Gõ độ dài mong muốn, Resolve tự tính tốc độ |
| **Ripple Sequence** | Phần sau timeline dồn theo độ dài mới |
| **Pitch Correction** | Giữ cao độ tiếng tự nhiên khi đổi tốc độ |

Cách dùng thực tế ở mục [Tốc độ — Retime](#tốc-độ--retime) bên dưới.

### Stabilization

`★★☆ Thường dùng` — bảng thông số: [Stabilization trang Cut](../cut/tools.md#stabilization--chống-rung)

Chọn **Perspective / Similarity / Translation** **trước**, rồi bấm **Stabilize**. Đổi phương pháp, **Cropping Ratio** hoặc **Smooth** thì phải bấm Stabilize lại.

> Kết quả chống rung cũng hiện ở palette **Tracker** của trang Color (chế độ Stabilizer) — có thêm biểu đồ để xem.

### Lens Correction

`Studio` — xem [Lens Correction trang Cut](../cut/tools.md#lens-correction--sửa-méo-góc-rộng).

### Retime and Scaling

`★★☆ Thường dùng` — **chỉ trang Edit mới thấy đủ**

Bốn thông số quyết định **chất lượng** khi đổi tốc độ và khi clip khác cỡ timeline. Mặc định đều là **Project Settings** — theo cài đặt chung của project.

| Thông số | Lựa chọn | Dùng khi |
|---|---|---|
| **Retime Process** | **Nearest** (lặp/bỏ khung, nhanh nhất) · **Frame Blend** (trộn hai khung kề) · **Optical Flow** (tính khung mới) | Slow motion bị giật → **Optical Flow** |
| **Motion Estimation** | **Standard Faster**, **Standard Better**, **Enhanced Faster**, **Enhanced Better**. **Speed Warp** là `Studio` | Chỉ hiện khi chọn Optical Flow. Hình nhoè quanh vật nhanh → **Enhanced Better** |
| **Scaling** | **Crop**, **Fit**, **Fill**, **Stretch** | Clip khác tỉ lệ timeline: Fit = vừa khung, có viền đen · Fill = lấp đầy, mất rìa · Crop = giữ đúng pixel · Stretch = kéo giãn |
| **Resize Filter** | **Sharper** · **Smoother** · **Bicubic** · **Bilinear** | Phóng to clip 1080 lên timeline 4K → **Sharper**. Máy yếu khi dựng → Bilinear, đổi lại trước khi xuất |

Clip quay xen kẽ (interlaced, như máy quay cũ) có thêm **Deinterlace Quality**: Normal / High. Tuỳ chọn DaVinci Neural Engine là AI.

**Ví dụ — ảnh dọc điện thoại trên timeline ngang:** chọn ảnh → **Scaling** → **Fit**. Ảnh nằm giữa, hai bên đen. Muốn nền mờ hai bên: đặt bản sao ảnh ở track dưới, Scaling **Fill**, thêm Gaussian Blur — xem [Open FX](chu-va-hieu-ung.md#open-fx--hiệu-ứng-có-sẵn).

### Super Scale

`Studio` — phóng độ phân giải nguồn lên 2×, 3×, 4× chất lượng cao. Bản free dùng **Resize Filter → Sharper** thay thế.

### Cinematic

`★☆☆` — chỉ hiện với clip iPhone quay chế độ **Cinematic**, trên macOS. Thanh **F-Stop** chỉnh độ mờ hậu cảnh. Bật overlay **Cinematic** trong menu overlay của Viewer để chỉnh trên hình.

### Khi chọn chữ hoặc generator

Tab Video chia thành hai bảng con:

| Bảng | Có gì |
|---|---|
| **Title** (Text, Lower 3rd, Scroll) hoặc **Text / Layout / Transform / Shading** (Text+) | Nội dung, font, màu, viền, bóng — xem [Chữ](chu-va-hieu-ung.md#chữ--text-text) |
| **Settings** | Composite, Transform, Cropping như mọi clip — để trộn và cho chữ bay |

Generator (Solid Color, Grey Scale…) có thêm ô **Display Name** — đặt tên hiện trên timeline.

---

## Tốc độ — Retime

`★★☆ Thường dùng`

| Cách | Mở bằng | Hợp với |
|---|---|---|
| **Inspector → Speed Change** | Chọn clip, mở Inspector | Đổi đều cả clip, gõ số chính xác |
| **Change Clip Speed** | Chuột phải clip → **Change Clip Speed** | Như trên, có thêm **Reverse Speed**, **Freeze Frame** |
| **Retime Controls** | `⌘R` | Speed ramp, dừng hình giữa clip, tua ngược một đoạn |
| **Retime Curve** | Bảng **Keyframes** → biểu đồ → chọn **Retime Speed** / **Retime Frame** | Chỉnh độ mượt khi chuyển tốc độ |

### Đổi tốc độ cả clip

Inspector → **Speed Change** → **Speed %**. `200` là nhanh gấp đôi, `50` là chậm một nửa.

Tick **Ripple Sequence** để phần sau timeline tự xê dịch theo độ dài mới.

**Kéo cho nhanh:** bấm `⌘R` → rê chuột lên **mép trái/phải thanh tốc độ** trên đầu clip cho tới khi con trỏ đổi hình → kéo dãn ra (chậm lại) hoặc bóp vào (nhanh lên).

> Ở chế độ **Selection** `A`, kéo đổi tốc độ **không** dồn timeline. Ở chế độ **Trim** `T` thì **dồn**.

**Đọc mũi tên trên thanh tốc độ:**

| Thấy | Nghĩa |
|---|---|
| Mũi tên xanh dương, đều nhau | 100% |
| Mũi tên **vàng**, thưa | Chậm hơn 100% |
| Mũi tên xanh dương, **dày** | Nhanh hơn 100% |
| Mũi tên **quay sang trái** | Đang tua ngược |

### Speed ramp — nhanh chậm trong cùng một clip

1. Chọn clip → `⌘R`. Thanh tốc độ hiện ngay trên clip.
2. Đặt con trỏ chỗ muốn đổi tốc độ, bấm **mũi tên nhỏ** trên thanh tốc độ → **Add Speed Point**.
3. Thêm điểm thứ hai. Clip chia thành nhiều đoạn.
4. Bấm mũi tên trên từng đoạn → chọn tốc độ (ví dụ 25% cho đoạn giữa).

**Ví dụ:** cảnh nhảy xuống nước — bình thường lúc chạy, chậm 25% lúc bay trên không, bình thường lại khi chạm nước.

**Menu mũi tên (Clip Speed) có gì:**

| Lệnh | Làm gì |
|---|---|
| **Change Speed** | Chọn nhanh một mức % cho đoạn đó |
| **Reverse Segment** | Đoạn đó chạy ngược |
| **Freeze Frame** | Dừng hình tại con trỏ — thêm sẵn hai điểm, kéo điểm sau để chỉnh dừng bao lâu. Xem [Freeze Frame](timeline-nang-cao.md#dừng-ở-giữa-clip-rồi-chạy-tiếp) |
| **Add Speed Point** / **Clear Speed Point** | Thêm / bỏ điểm đổi tốc độ |
| **Rewind** | Hiệu ứng tua ngược rồi phát lại — chọn mức % |
| **Speed Ramp** | Tự tạo năm đoạn tăng dần 10% → 30% → 50% → 70% → 90% |
| **Reset to 100%** | Về tốc độ gốc |

**Kéo điểm tốc độ:** tay nắm **trên** đổi tốc độ đoạn đó. Tay nắm **dưới** nới rộng vùng chạy ở tốc độ đó.

**Đóng thanh tốc độ:** `Esc`, hoặc `⌘R` lần nữa. Tốc độ vẫn giữ — clip có **huy hiệu retime** cạnh tên.

> Tiếng đi kèm một clip **speed ramp** (nhiều tốc độ) sẽ bị **tắt**. Muốn có tiếng, tách tiếng ra để ở tốc độ gốc.

### Retime Curve — chuyển tốc độ mượt hơn

`★☆☆ Tình huống cụ thể`

Chọn clip → bảng **Keyframes** (góc trên trái) → icon **Curve** → chọn **Retime Speed** hoặc **Retime Frame** trong danh sách thông số.

| Đường | Đọc thế nào | Lưu ý |
|---|---|---|
| **Retime Speed** | Đường phẳng = 100%. **Kéo đoạn** giữa hai điểm lên = nhanh, xuống = chậm | Kéo **đoạn**, không kéo điểm. Không tạo được tua ngược |
| **Retime Frame** | Đường chéo. Dốc thoải = chậm, dốc đứng = nhanh, dốc xuống = ngược | Kiểu quen thuộc ở phần mềm khác |

Điểm trên đường cong **trùng** với điểm tốc độ của `⌘R` — sửa bên nào bên kia đổi theo.

### Slow motion mượt

Quay 50fps hoặc 60fps rồi làm chậm thì luôn mượt. Quay 25fps mà làm chậm thì vào Inspector → **Retime and Scaling** → **Retime Process** → **Optical Flow**.

Muốn đặt Optical Flow cho **mọi** clip: **Project Settings → Master Settings → Frame Interpolation → Retime Process**.

---

## Tab Audio

`★★★ Hằng ngày`

**Hai chế độ**, đổi bằng icon góc trên trái tab: **Clip** (chỉnh clip đang chọn) và **Track** (chỉnh cả track). Bấm clip tiếng là tự sang Clip. Bấm đầu track tiếng là tự sang Track.

| Nhóm | Làm gì | Bản free? | Mức |
|---|---|---|---|
| **Volume** | Âm lượng clip — trùng với đường ngang trên clip tiếng | Có | ★★★ |
| **Pan** | Lệch tiếng sang trái/phải | Có | ★☆☆ |
| **Pitch** | Đổi cao độ, **không đổi tốc độ**. Hai thanh: **Semi Tones** (nửa cung) và **Cents** (1/100 nửa cung) | Có | ★☆☆ |
| **Equalizer** | EQ 6 băng tần cho riêng clip | Có | ★★☆ |
| **Dialogue Leveler** | Giọng đều, chỗ to hạ xuống, chỗ nhỏ nâng lên | Có | ★★☆ |
| **Voice Isolation** | Lọc tạp âm nền, giữ giọng | `Studio` | — |
| **Music Remixer** | Tách nhạc thành giọng, trống, bass, guitar… | `Studio` | — |
| **Music Editor** | Kéo dài/rút ngắn bài nhạc cho vừa video | `Studio` | — |
| **Dialogue Separator** (chỉ Track) | Tách giọng, nền, tiếng vang phòng | `Studio` | — |
| **Ducker** (chỉ Track) | Track này tự nhỏ khi track khác có tiếng | Có | ★★☆ |

Cách dùng Dialogue Leveler và Ducker: [Dialogue Leveler](../fairlight/mixer-va-track-fx.md#dialogue-leveler--giọng-đều-không-cần-chỉnh-tay), [Ducker](../fairlight/mixer-va-track-fx.md#ducker--nhạc-tự-nhỏ-khi-có-lời).

### Equalizer của clip

**Là gì:** EQ 6 băng tần, chạy **trước** EQ của Mixer. Có biểu đồ — kéo các chấm số 1–6.

| Băng | Kiểu lọc chọn được |
|---|---|
| **1** (thấp nhất) | Lo-Shelf, Bell, Notch, Hi-Shelf, **Hi-Pass** |
| **2–5** | Lo-Shelf, Bell, Notch, Hi-Shelf |
| **6** (cao nhất) | **Lo-Pass**, Lo-Shelf, Bell, Notch, Hi-Shelf |

Mỗi băng có **Freq**, **Gain**, và **Q** (độ rộng — chỉ khi chọn Bell).

**Ví dụ — giọng ù vì tiếng gió, tiếng xe:** bật băng **1** → **Hi-Pass** → Freq khoảng 80–100 Hz. Cách chỉnh EQ cho giọng nói kỹ hơn: [EQ — 3 thao tác](../fairlight/lam-sach-giong.md#eq--3-thao-tác-cho-giọng-nói).

> EQ của clip copy dán được sang clip khác, và giữa EQ clip với EQ track.

> Hiệu ứng tiếng kéo từ **Audio FX** không nằm ở đây mà ở tab **Effects**.

---

## Tab Effects

`★★☆ Thường dùng`

Mọi hiệu ứng bạn kéo từ [Effects Library](chu-va-hieu-ung.md#thư-viện-effects--cây-thư-mục) vào clip đều hiện ở đây, chia nhóm **Fusion**, **Open FX**, **Audio**. Clip chưa có hiệu ứng thì tab này mờ.

Thanh tiêu đề mỗi hiệu ứng:

| Nút | Làm gì |
|---|---|
| **Công tắc** (trái) | Tắt/bật hiệu ứng, giữ nguyên thông số |
| **Kim cương + hai mũi tên** | Đặt keyframe cho **mọi** thông số của hiệu ứng cùng lúc, nhảy giữa các keyframe |
| **Mũi tên lên/xuống** | Đổi thứ tự khi có nhiều hiệu ứng — hiệu ứng trên chạy trước |
| **Thùng rác** | Xoá hiệu ứng |
| **Reset** (phải) | Về mặc định |

Mọi Resolve FX có thanh **Blend** ở cuối — kéo xuống để giảm độ mạnh hiệu ứng, trộn với hình gốc.

**Kéo điều khiển trên hình:** menu góc dưới trái Viewer Timeline → **Open FX Overlay** (hoặc **Fusion Overlay** cho hiệu ứng Fusion).

---

## Tab Transition

`★★☆ Thường dùng`

Mở bằng cách **bấm đúp** chuyển cảnh trên timeline. Giải thích từng thông số: [Chuyển cảnh trong Inspector](chu-va-hieu-ung.md#chỉnh-chuyển-cảnh-trong-inspector).

---

## Tab Image

`★☆☆ Tình huống cụ thể` — chỉ có tác dụng với **file RAW** (Blackmagic RAW, RED, ARRI…).

Thay thông số máy đã ghi lúc quay (ISO, nhiệt độ màu, độ phơi sáng…). Video điện thoại, máy ảnh quay MP4/MOV thì tab này mờ.

---

## Tab File

`★☆☆ Tình huống cụ thể`

| Nhóm | Có gì | Dùng khi |
|---|---|---|
| **Clip Details** | Codec, độ phân giải, frame rate… | Kiểm tra nhanh file đang dùng |
| **Metadata** | Timecode, Date Created, Camera, Reel, Scene, Shot, Take, Good Take, **Clip Color**, **Name**, **Comments** | Đổi tên clip **chỉ trên timeline này**, ghi chú |
| **Audio Configuration** | Dạng sóng từng kênh của file, tắt/mute từng kênh, thanh **Level** chỉnh mức kênh | File có nhiều kênh tiếng (mic cài áo kênh 1, mic máy kênh 2) |
| **Timecode** | Current Frame, Slate, Offset Source | Sửa timecode sai |

**Audio Configuration dùng thế nào:** rê chuột trên dạng sóng là nghe riêng kênh đó. Bỏ tick một kênh thì lần sau kéo clip xuống timeline **không** mang kênh đó theo. Chỉ áp cho clip trong **Media Pool** — clip đã ở timeline thì các ô này mờ. Cách khác: [Clip Attributes](../media/clip-attributes.md#tab-audio).

---

## Chỉnh nhiều clip cùng lúc

`★★☆ Thường dùng`

Chọn nhiều clip → Inspector ghi **Multiple Clips**. Ô nào giá trị khác nhau giữa các clip thì hiện **hai gạch**.

| Muốn | Cách |
|---|---|
| **Cộng thêm** cùng một lượng, giữ chênh lệch giữa các clip | **Kéo** trên ô số. Ô hiện `+` hoặc `−` |
| Đặt **cùng một giá trị** cho mọi clip | **Bấm đúp** ô số → gõ số → `Return` |

**Ví dụ:** 12 clip quay hơi nghiêng — chọn cả 12, bấm đúp ô **Zoom**, gõ `1.05`.

### Copy thông số sang clip khác — Paste Attributes

1. Chọn clip đã chỉnh → `⌘C`.
2. Chọn một hoặc nhiều clip đích.
3. `⌥V` (**Edit → Paste Attributes**).
4. Tick những nhóm muốn dán (Transform, Cropping, Composite, Speed, Audio…) → **Apply**.

Có tuỳ chọn keyframe **Maintain Timing** / **Stretch to Fit**, và **Ripple Sequence** khi dán tốc độ.

**Bỏ hết chỉnh sửa:** chọn clip → **Edit → Remove Attributes** → tick nhóm muốn xoá → **Apply**.

> Clip có hiệu ứng (Inspector, tốc độ, plugin) hiện **màu đậm hơn** trên timeline. Remove Attributes hết thì về màu thường.

---

## Keyframe trong Inspector

`★★☆ Thường dùng`

Mỗi thông số có **viên kim cương** bên phải.

1. Đặt con trỏ ở điểm bắt đầu → bấm kim cương (chuyển **cam**) → đặt giá trị.
2. Dời con trỏ → đổi giá trị → keyframe mới tự tạo.
3. Phát thử.

**Cho chuyển động mềm:** chuột phải viên kim cương cam → **Ease In and Out**.

| Việc | Cách |
|---|---|
| Nhảy keyframe trước / sau | Mũi tên nhỏ hai bên kim cương, hoặc `[` `]` |
| Xoá một keyframe | Đứng tại keyframe, bấm kim cương cam |
| Xoá mọi keyframe của **một** thông số | Nút **reset** bên phải kim cương |
| Xoá mọi keyframe của **cả nhóm** | Nút **reset** trên thanh tiêu đề nhóm |
| Về chuyển động đều | Chuột phải kim cương cam → **Linear** |

Clip có keyframe hiện **icon keyframe** ở đầu thanh tên trên timeline.

Chi tiết hơn: [Keyframe](chu-va-hieu-ung.md#keyframe--cho-mọi-thứ-chuyển-động).
