# Keyframe và Spline — làm chuyển động

**Keyframe** là mốc ghi lại giá trị của một thông số tại một khung hình. Có hai keyframe với hai giá trị khác nhau, Fusion tự tính phần ở giữa — thế là thành chuyển động.

Ở Fusion có ba chỗ làm việc với keyframe:

| Chỗ | Dùng để | Mức |
|---|---|---|
| **Inspector** | Tạo keyframe | ★★★ |
| **Keyframes Editor** | Dời keyframe sớm hơn, muộn hơn; chỉnh độ dài clip và hiệu ứng | ★★☆ |
| **Spline Editor** | Chỉnh **cách** chuyển động: đều, chậm dần, nhanh dần, nảy | ★★☆ |

---

## Keyframe trong Inspector

`★★★ Hằng ngày`

**Là gì:** mỗi thông số keyframe được có một **nút hình thoi** nhỏ bên phải.

| Nút | Nghĩa |
|---|---|
| Hình thoi **xám** | Chưa có keyframe ở khung này. Bấm để tạo |
| Hình thoi **cam** | Đang đứng đúng trên một keyframe. Bấm để **xoá** keyframe đó |
| Mũi tên nhỏ hai bên | Còn keyframe ở phía trước/sau. Bấm để nhảy tới |

**Cách làm:**
1. Đặt con trỏ ở khung bắt đầu. Chỉnh thông số về giá trị đầu. Bấm hình thoi → chuyển cam.
2. Đặt con trỏ ở khung kết thúc. Chỉnh thông số về giá trị cuối. **Keyframe tự tạo** — không cần bấm hình thoi nữa.
3. Bấm `Space` xem thử.

> **Quan trọng:** sau keyframe đầu tiên, **mọi lần đổi giá trị** thông số đó đều tạo keyframe mới ở khung hiện tại. Muốn chỉnh giá trị chung mà không tạo keyframe thì phải xoá hoạt ảnh trước.

**Cách khác:** chuột phải vào thông số → **Animate**. Thông số được gắn đường hoạt ảnh ngay, chưa cần keyframe.

**Xoá toàn bộ hoạt ảnh của một thông số:** chuột phải vào nút hình thoi → **Remove `<tên thông số>`**.

**Node đã có keyframe** hiện một huy hiệu nhỏ trên thân trong Node Editor (khi bật chuột phải node → **Show → Show Modes/Options**).

### Nhảy giữa các keyframe

Chọn node có keyframe: Time Ruler dưới Viewer hiện **vạch trắng nhỏ** ở vị trí từng keyframe.

| Phím | Làm gì |
|---|---|
| `⌥[` | Nhảy tới keyframe **trước** |
| `⌥]` | Nhảy tới keyframe **sau** |

### Hai thông số cùng một chuyển động

Chuột phải thông số thứ hai → **Connect To** → chọn thông số đã keyframe. Hai thông số dùng chung một đường hoạt ảnh — sửa một, cả hai đổi.

**Ví dụ:** keyframe **Size** của Text+, rồi nối **Opacity** của lớp bóng vào cùng đường đó.

### Keyframe vị trí tạo ra đường đi

Keyframe **Center** (của Transform, Merge, Text+ Layout…) thì Viewer hiện một **đường đi** (motion path). Kéo điểm trên đường để sửa quỹ đạo ngay trên hình. Muốn đường cong thay vì thẳng, kéo tay nắm ở các điểm đó.

---

## Keyframes Editor

`★★☆ Thường dùng`

**Là gì:** một **timeline thu nhỏ**, mỗi node là một thanh. Mở bằng nút **Keyframes** trên thanh trên cùng.

Thứ tự các thanh **không** ảnh hưởng thứ tự xếp lớp — cái đó do Node Editor quyết định. Ở đây chỉ chỉnh **thời gian**.

### Chỉnh thời gian clip và hiệu ứng

| Thao tác | Kết quả |
|---|---|
| Kéo **mép** thanh MediaIn | Trim điểm đầu/cuối của clip trong comp |
| Kéo **cả** thanh MediaIn | Dời clip sớm hơn, muộn hơn so với lớp khác |
| Kéo **mép** thanh của một node hiệu ứng | Hiệu ứng chỉ có tác dụng trong khoảng đó, bật tắt đột ngột ở hai đầu |

**Ví dụ:** comp có hai lớp chữ. Kéo thanh của chữ thứ hai lùi sau 1 giây — chữ thứ hai xuất hiện muộn hơn, không cần sửa keyframe.

### Chỉnh keyframe

Mặc định mọi keyframe của một node **gộp chung một hàng** trên thanh của node đó. Bấm **tam giác** bên trái tên node để mở ra mỗi thông số một hàng.

| Thao tác | Cách |
|---|---|
| Chọn | Bấm keyframe, hoặc kéo khung chọn nhiều cái |
| Dời | Kéo sang trái, phải |
| Nhân bản | Giữ `⌘` rồi kéo |
| Đổi kiểu, copy, dán | Chuột phải keyframe đã chọn |
| Đặt chính xác khung | Chọn keyframe, gõ số khung vào ô **Time** ở góc dưới phải |

**Time Stretch** (nút ở góc dưới trái): chọn một dãy keyframe, bật Time Stretch → hiện một khung. Kéo khung co giãn để **cả chuyển động nhanh hơn hoặc chậm hơn** mà giữ nguyên nhịp giữa các keyframe.

**Spreadsheet** (cạnh Time Stretch): hiện keyframe dạng bảng số — gõ trực tiếp khung và giá trị.

Dạng sóng âm thanh của timeline cũng hiện ở đây — tiện để đặt keyframe khớp nhịp nhạc.

---

## Spline Editor

`★★☆ Thường dùng`

**Là gì:** xem chuyển động dạng **đồ thị**. Trục ngang là thời gian, trục dọc là giá trị. Mỗi keyframe là một điểm, đường nối giữa các điểm (spline) cho biết giá trị thay đổi **thế nào**.

Mở bằng nút **Spline** trên thanh trên cùng.

**Bốn vùng:**

| Vùng | Có gì |
|---|---|
| Trên cùng | Zoom ngang, dọc; **Zoom to Fit**; thước thời gian |
| Bên trái | **Danh sách thông số** — tích ô để hiện đường của thông số đó. Đổi màu đường cho dễ phân biệt |
| Giữa | **Đồ thị** |
| Dưới cùng | Thanh công cụ: kiểu nội suy, lặp, công cụ chỉnh |

**Đọc đồ thị:**
- Đường **thẳng xiên** = chuyển động đều.
- Đường **cong thoải dần về ngang** ở cuối = chậm dần rồi dừng.
- Đường **nằm ngang** = đứng yên.
- Đường **bậc thang** = nhảy cóc, không chuyển tiếp.

### Thao tác cơ bản

| Thao tác | Cách |
|---|---|
| Vừa khít mọi đường | `⌘F` |
| Chỉ hiện node đang chọn | Menu Option → **Show Only Selected Tool** |
| Hiện mọi thông số | Menu Option → **Expose All Controls** |
| Chọn điểm | Bấm, `⌘`-click thêm điểm, hoặc kéo khung chọn |
| Thêm keyframe tại con trỏ | `⌘K`, hoặc chuột phải → **Set Key** |
| Thêm điểm bất kỳ | Bấm lên đường |
| Dời điểm | Kéo. Giữ `⇧` để chỉ dời ngang hoặc chỉ dời dọc |
| Xoá điểm | `Delete` |
| Giữ nguyên giá trị một quãng | Chuột phải → **Set Key Equal To** → bằng keyframe trước/sau |

> **Mẹo:** kéo **thanh tên node** trong Inspector thả vào Spline Editor — mọi đường hoạt ảnh của node đó hiện ra ngay.

---

## Làm chuyển động mượt

`★★☆ Thường dùng`

**Là gì:** đổi **kiểu nội suy** giữa các keyframe — chuyển động đều cứng nhắc thành chậm dần, nhanh dần tự nhiên. Trong ngành gọi là *easing*.

**Dùng khi:** gần như mọi chuyển động chữ, logo. Vật thật không bao giờ đang chạy rồi dừng cái cụp.

**Sáu nút đầu trên thanh công cụ Spline Editor:**

| Nút | Phím | Kết quả | Mức |
|---|---|---|---|
| **Smooth** | `⇧S` | Cong mượt — chậm lại khi qua keyframe | ★★★ |
| **Linear** | `⇧L` | Thẳng — chuyển động đều | ★★☆ |
| **Invert** | — | Chỉ dùng cho đường LUT, không dùng cho hoạt ảnh | — |
| **Step In** | — | Giữ giá trị, tới keyframe sau thì nhảy cóc | ★☆☆ |
| **Step Out** | — | Nhảy cóc ngay tại keyframe | ★☆☆ |
| **Reverse** | — | Đảo ngược thứ tự keyframe theo thời gian | ★☆☆ |

**Cách làm nhanh:** chọn mọi điểm (kéo khung chọn), bấm `⇧S`. Xong.

### Chỉnh độ cong bằng tay nắm

Chọn một điểm → hiện **hai tay nắm** (Bézier). Kéo tay nắm:
- **Dài và nằm ngang** = chậm hẳn khi tới gần điểm đó.
- **Ngắn** = chuyển hướng gấp.

Hai tay nắm mặc định khoá với nhau. Giữ `⌘` khi kéo để kéo riêng một bên — tạo chuyển động gãy đột ngột.

### Ease In/Out bằng số

Chọn keyframe, bấm `T` (hoặc chuột phải → **Edit → Ease In/Out**). Hai ô số hiện trên đồ thị cho độ dài tay nắm vào và ra. Bấm **Lock In/Out** để chỉnh hai bên cùng lúc.

**Ví dụ — logo bay vào, chậm dần, dừng nhẹ nhàng:**
1. Keyframe **Center X** của Merge: khung 0 = `-0.3`, khung 20 = `0.5`.
2. Mở Spline, chọn điểm ở khung 20, bấm `T`.
3. Đặt **Ease In** lớn (tay nắm dài) để logo phanh từ từ. Điểm ở khung 0 để Linear để logo **lao vào** với tốc độ đầy đủ ngay từ đầu.

---

## Lặp chuyển động

`★☆☆ Tình huống cụ thể`

**Là gì:** lặp lại một đoạn keyframe mãi sau keyframe cuối, không cần tạo hàng trăm keyframe.

**Cách làm:** chọn các điểm cần lặp, bấm một trong ba nút lặp trên thanh công cụ Spline Editor:

| Nút | Lặp kiểu |
|---|---|
| **Set Loop** | Lặp y hệt: A→B, A→B, A→B |
| **Set Ping Pong** | Đi rồi về: A→B→A→B — liền mạch, không giật |
| **Set Relative** | Lặp nhưng cộng dồn: mỗi vòng cao hơn vòng trước |

**Ví dụ:**
- Mũi tên nhấp nháy chỉ vào nút Subscribe: keyframe **Size** 1 → 1.2 trong 10 khung, **Set Ping Pong**.
- Bánh xe quay mãi: keyframe **Angle** 0 → 360 trong 1 giây, **Set Relative**.

---

## Các công cụ khác trên thanh Spline Editor

| Nút | Làm gì |
|---|---|
| **Select All** | Chọn mọi keyframe đang hiện |
| **Click Append** | Bấm lên đồ thị để thêm keyframe |
| **Time Stretch** | Co giãn thời gian một dãy keyframe, giữ nguyên nhịp |
| **Shape Box** | Khung quanh nhóm điểm: kéo để co giãn, bẻ góc, dời cả nhóm |
| **Show Key Markers** | Hiện vị trí keyframe trên thước trên cùng |
