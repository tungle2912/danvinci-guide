# Tools trong Viewer — phóng to, crop, tốc độ

Bấm nút **Tools** ở **góc dưới trái Viewer**. Một hàng công cụ hiện ra ngay dưới hình — chỉnh trực tiếp trên Viewer, **không cần mở Inspector**.

Chọn clip trên timeline trước, rồi chọn một nhóm công cụ.

## Hai nút chung của mọi nhóm

| Vị trí | Nút | Làm gì |
|---|---|---|
| **Ngoài cùng bên trái** | Toggle | Tắt/bật hiệu ứng **mà không mất** những gì đã chỉnh — để so sánh trước/sau |
| **Ngoài cùng bên phải** | Reset | Đưa mọi thông số của nhóm đó về mặc định |

> Muốn chỉnh con số chính xác thì mở **Inspector** (góc trên phải). Mọi thứ chỉnh ở Tools đều hiện bên Inspector và ngược lại — cùng một dữ liệu.

---

## Transform — phóng to, dời, xoay

`★★★ Hằng ngày`

Khi chọn Transform, **khung điều khiển** hiện lên trên hình trong Viewer:

| Kéo vào | Làm gì |
|---|---|
| **Bất kỳ đâu trong khung** | Dời hình |
| **Góc chéo** | Phóng to/thu nhỏ, giữ tỉ lệ |
| **Cạnh trên/dưới/trái/phải** | Kéo giãn hoặc bóp méo một chiều |
| **Tay nắm giữa** | Xoay |

Giữ `⇧` khi dời → chỉ dời ngang hoặc chỉ dời dọc.

**Các thông số tương ứng (trong Inspector):**

| Thông số | Làm gì | Mức |
|---|---|---|
| **Zoom** X/Y | Phóng to. Khoá X và Y với nhau để giữ tỉ lệ | ★★★ |
| **Position** X/Y | X dời ngang, Y dời dọc | ★★★ |
| **Rotation Angle** | Xoay quanh điểm neo | ★★☆ |
| **Anchor Point** | Điểm làm tâm cho mọi phép xoay, phóng to | ★☆☆ |
| **Pitch** | Nghiêng hình về trước/sau theo trục ngang — hiệu ứng 3D | ★☆☆ |
| **Yaw** | Nghiêng hình sang trái/phải theo trục dọc | ★☆☆ |
| **Flip** | Lật ngang hoặc lật dọc | ★★☆ |

**Dùng khi:**
- Cắt bớt khung để bỏ vật thừa ở rìa → tăng **Zoom** lên 110–120%.
- Video dọc từ footage ngang → tăng Zoom, chỉnh **Position X** đưa người vào giữa.
- Hình người quay lệch hướng, muốn nhìn sang phải → **Flip** ngang.
- Đường chân trời bị nghiêng → **Rotation** khoảng ±1–3 độ, rồi tăng Zoom nhẹ để giấu góc đen.

---

## Crop — cắt rìa

`★★☆ Thường dùng`

Mỗi cạnh hình có **tay nắm riêng** trên Viewer, kéo vào để cắt cạnh đó.

| Thông số | Làm gì |
|---|---|
| **Crop Left / Right / Top / Bottom** | Cắt bao nhiêu pixel ở mỗi cạnh |
| **Softness** | Làm mờ mép cắt. Số âm làm mờ vào trong, số dương làm mờ ra ngoài |
| **Retain Image Position** | Tick vào thì phóng to bằng Transform không làm xê dịch khung crop |

**Khác Transform ở đâu:** Crop **cắt bỏ** phần rìa và để lộ thứ bên dưới (track thấp hơn, hoặc đen). Transform Zoom thì **phóng to** để lấp đầy khung.

**Dùng khi:**
- Làm hiệu ứng **khung phim điện ảnh** (dải đen trên dưới) → Crop Top và Bottom bằng nhau.
- Đặt hai video **cạnh nhau** (split screen) → crop nửa trái clip này, nửa phải clip kia, đặt chồng lên nhau.
- Làm khung hình nhỏ trong góc (picture-in-picture) với mép mềm → Crop + Softness dương.

---

## Dynamic Zoom — zoom chậm tự động

`★★☆ Thường dùng`

Hiệu ứng **Ken Burns**: hình từ từ phóng to hoặc dời trong suốt clip. Không cần keyframe.

**Cách làm:**
1. Chọn **Dynamic Zoom** trong Tools.
2. Trên Viewer hiện hai khung:
   - **Khung xanh lá** = khung hình lúc **bắt đầu**
   - **Khung đỏ** = khung hình lúc **kết thúc**
3. Kéo vào trong khung để dời, kéo góc để đổi cỡ. Một đường hiện ra cho thấy chuyển động.
4. Phát thử.

| Nút | Làm gì |
|---|---|
| **Swap** | Đảo chiều — zoom vào thành zoom ra |
| **Ease** | Kiểu tăng tốc: **Linear** (đều), **Ease In** (chậm lúc đầu), **Ease Out** (chậm lúc cuối), **Ease In and Out** (chậm hai đầu — tự nhiên nhất) |

**Dùng khi:**
- Ảnh tĩnh trong video (ảnh cũ, ảnh chụp sản phẩm) → làm sống động hơn.
- Cảnh quay tĩnh dài, muốn có chút chuyển động.
- Dẫn mắt người xem tới chi tiết quan trọng.

> Đặt **Ease In and Out** gần như mọi lúc. Linear trông máy móc.

---

## Composite — trộn hai lớp hình

`★☆☆ Tình huống cụ thể`

Chỉ có tác dụng khi clip nằm **trên** một clip khác.

| Thông số | Làm gì |
|---|---|
| **Composite Mode** | Kiểu trộn. **Normal** là không trộn |
| **Opacity** | Độ trong suốt, 0 (vô hình) đến 100 (đặc) |

Năm kiểu trộn hay dùng:

| Mode | Kết quả | Dùng khi |
|---|---|---|
| **Screen** | Chỉ giữ phần sáng, phần đen biến mất | Light leak, lửa, bokeh, bụi quay trên nền đen |
| **Multiply** | Chỉ giữ phần tối, phần trắng biến mất | Texture giấy, vết bẩn, bóng đổ |
| **Overlay** | Tăng tương phản, giữ cả sáng lẫn tối | Phủ texture lên hình |
| **Add** | Cộng sáng, mạnh hơn Screen | Hiệu ứng ánh sáng gắt |
| **Normal** + Opacity thấp | Hai hình chồng mờ lên nhau | Hồi tưởng, chuyển cảnh mơ màng |

> Clip **không có gì bên dưới** mà giảm Opacity thì nó trộn với **màu đen** — tương đương fade ra đen.

> File PNG hoặc video có **kênh alpha** (nền trong suốt) tự động trong suốt khi đặt lên track trên. Không cần chỉnh gì.

---

## Speed — nhanh, chậm, tua ngược

`★★☆ Thường dùng`

| Thông số | Làm gì |
|---|---|
| **Speed** | Hệ số tốc độ. `2` là nhanh gấp đôi, `0.5` là chậm một nửa, **số âm là tua ngược** |
| **Duration** | Xem độ dài mới sau khi đổi tốc độ |
| **Add Speed Point** | Thêm điểm đổi tốc độ tại con trỏ — để làm **speed ramp** |

**Tiếng tự động được giữ đúng cao độ** khi đổi tốc độ ở trang Cut — không bị giọng chuột chít khi tua nhanh.

**Speed ramp** — nhanh rồi chậm rồi nhanh trong cùng một clip:
1. Đặt con trỏ ở chỗ muốn bắt đầu chậm, bấm **Add Speed Point**.
2. Đặt con trỏ ở chỗ muốn hết chậm, bấm **Add Speed Point** lần nữa.
3. Clip giờ chia làm 3 đoạn, chọn từng đoạn đặt Speed riêng.

**Dùng khi:**
- Timelapse từ cảnh quay thường → Speed `4`–`10`.
- Khoảnh khắc ấn tượng (nhảy, ném, té nước) → slow motion `0.25`–`0.5`.
- Cảnh hành động kiểu điện ảnh → speed ramp: bình thường → chậm đúng khoảnh khắc → nhanh lại.

### Slow motion mượt cần đúng footage

**Slow motion đẹp cần quay ở frame rate cao.** Quay 60fps dựng timeline 30fps thì chậm `0.5` mượt hoàn hảo. Quay 30fps mà chậm `0.5` thì Resolve phải **bịa ra** khung hình còn thiếu.

Muốn Resolve bịa khung hình mượt hơn: **Inspector → Retime and Scaling → Retime Process → Optical Flow**.
Nếu thấy hình bị méo nhoè quanh vật chuyển động nhanh, đổi **Motion Estimation** sang **Enhanced Better**.

> Các chế độ **Speed Warp** dùng DaVinci Neural Engine, thuộc `Studio`.

### Thêm trong Inspector

Inspector → **Speed Change** có thêm:

| Thông số | Làm gì |
|---|---|
| **Direction** | Tiến, lùi, hoặc **đứng hình** (freeze frame) |
| **Frames Per Second** | Đặt tốc độ theo số khung/giây |
| **Duration** | Gõ độ dài mong muốn, Resolve tự tính tốc độ — **ép clip vừa khít một khoảng** |
| **Ripple Sequence** | Tick để phần sau timeline tự xê dịch theo độ dài mới |
| **Pitch Correction** | Giữ đúng cao độ tiếng |

**Freeze frame dùng khi:** dừng hình đúng khoảnh khắc để chèn chữ giới thiệu nhân vật.

---

## Stabilization — chống rung

`★★☆ Thường dùng`

**Cách làm:**
1. Chọn **phương pháp** trong menu thả xuống **trước** — đổi phương pháp sau thì phải phân tích lại.
2. Bấm **Stabilize**. Resolve phân tích và làm mượt.
3. Chỉnh thêm các thông số, **mỗi lần chỉnh xong bấm Stabilize lại**.

| Phương pháp | Sửa gì | Dùng khi |
|---|---|---|
| **Perspective** | Phối cảnh, dời, nghiêng, phóng, xoay | Mặc định, mạnh nhất |
| **Similarity** | Dời, nghiêng, phóng, xoay | Perspective làm hình bị **méo sóng** |
| **Translation** | Chỉ dời ngang dọc | Hai cái trên đều méo. An toàn nhất |

Thông số tinh chỉnh (trong Inspector):

| Thông số | Làm gì |
|---|---|
| **Camera Lock** | Khoá cứng như quay chân máy, loại bỏ **mọi** chuyển động |
| **Zoom** | Tự phóng to để giấu viền đen sinh ra do chống rung |
| **Cropping Ratio** | `1.0` là không chống rung. Càng thấp càng chống mạnh nhưng càng cắt nhiều |
| **Smooth** | Càng cao càng mượt, càng mất chất chuyển động gốc |
| **Strength** | `1` là chống tối đa, `0.5` giữ lại một nửa rung gốc cho tự nhiên |

**Dùng khi:**
- Quay cầm tay đi bộ → **Similarity**, Smooth trung bình.
- Muốn cảnh như quay chân máy → **Camera Lock**.
- Muốn giữ cảm giác cầm tay nhưng bớt giật → **Strength** khoảng `0.6`.

> Chống rung **không cứu được** cảnh bị nhoè do rung (motion blur). Nó chỉ làm khung hình đứng yên hơn, còn hình mờ vẫn mờ.

---

## Lens Correction — sửa méo góc rộng

`Studio`

Sửa méo cong ở mép hình do ống kính góc rộng (GoPro, điện thoại góc 0.5×). Nút **Analyze** tự dò, thanh **Distortion** chỉnh tay.

Bản free không có. Thay thế: tăng nhẹ Zoom để cắt bớt phần mép bị cong nhiều nhất.

---

## Color — Auto Color

`★★☆ Thường dùng`

Chỉ một nút: **Auto Color**. Tự cân bằng điểm đen, điểm trắng và màu dựa trên khung hình tại con trỏ.

**Dùng khi:** cần sửa nhanh clip ám màu mà không muốn sang trang Color. Đặt con trỏ ở khung hình đại diện nhất của clip rồi bấm.

Đây là cùng thuật toán với nút **A** trong trang Color. Muốn chỉnh màu kỹ hơn thì sang [Color](../color/README.md).

---

## Audio — volume clip

`★★★ Hằng ngày`

Một thanh trượt chỉnh to nhỏ tiếng của clip đang chọn. Giống hệt volume của clip ở trang Edit và Fairlight.

---

## Effects Overlay

Bật **Open FX** hoặc **Fusion** overlay để hiện **điều khiển trên màn hình** của các hiệu ứng có hỗ trợ (ví dụ kéo tâm của hiệu ứng làm mờ).

---

## Voiceover — thu giọng thẳng vào timeline

`★★☆ Thường dùng` — nếu bạn làm video có lời bình

Bấm nút **Voiceover** (icon đỏ) ở thanh dưới đáy Viewer. Bảng Voiceover mở ra ngay dưới hình.

**Dùng khi:** thu lời bình cho video hướng dẫn, review sản phẩm, du lịch — vừa xem hình vừa nói, khớp ngay từ đầu.

### Cách làm

1. Đặt con trỏ ở chỗ muốn bắt đầu nói.
2. Bấm **Record**. Nói. Bấm **Stop**.
3. Tiếng nằm ngay trên một track mới tên **VO**.

Thu hỏng thì bấm **Cue** — con trỏ nhảy về đúng điểm bắt đầu để thu lại.

### Thiết lập (menu tuỳ chọn của bảng Voiceover)

| Mục | Đặt gì |
|---|---|
| **Audio Input** | Chọn micro |
| **Record Track** | Track đích. Mặc định tạo track mới tên VO |
| **Monitoring** | Nghe gì khi thu: cả timeline lẫn giọng mình · chỉ timeline · chỉ giọng mình |
| **Mute Monitoring When Recording** | Tắt hết tiếng khi thu — dùng khi **không đeo tai nghe**, tránh loa lọt vào mic |
| **Countdown** | Không đếm · đếm 3 giây · đếm 5 giây trước khi thu |
| **Recording File Location** | Nơi lưu file tiếng |

> **Đặt đếm ngược 3 giây** — đủ để hít một hơi trước khi nói.

### Máy nhắc chữ (Prompter) — tính năng ít người biết

Resolve có sẵn **teleprompter**: chữ kịch bản chạy chồng lên Viewer trong lúc bạn thu.

1. Viết kịch bản ra file `.txt`.
2. Trong thiết lập Voiceover → **Load Script File** → chọn file đó.
3. Bật **Enable Prompter Overlay**.
4. Chỉnh **Font Size**, **Line Spacing**, **Side Margin**, **Background Opacity** cho dễ đọc.

**Dùng khi:** lời bình dài, có số liệu, tên riêng — đọc theo kịch bản thay vì nói tự do để khỏi vấp.

### Hai nút xử lý tiếng lúc thu

| Nút | Làm gì | |
|---|---|---|
| **Dialog Leveler** | Giữ âm lượng giọng đều, không lúc to lúc nhỏ | Bản free |
| **Voice Isolation** | Lọc tiếng ồn nền | `Studio` |

### Mức tiếng mic

Đồng hồ nhỏ trong bảng cho thấy mức mic. Giữ ở vùng **xanh**, chỗ to nhất chạm **vàng** là vừa. Chạm đỏ là quá to — lùi xa mic hoặc giảm gain.
