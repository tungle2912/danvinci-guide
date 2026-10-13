# Mask, Tracker, Delta Keyer

Ba nhóm công cụ cho ba việc người mới hay cần nhất: **khoanh một vùng**, **bám theo vật chuyển động**, **tách phông xanh**.

---

## Mask là gì

**Mask** là một hình đen trắng dùng để **chọn vùng**: trắng = chọn, đen = không chọn, xám = chọn một phần. Node mask chỉ tạo ra một kênh duy nhất, không có màu.

Mask tự nó không hiện gì trên video. Bạn **nối nó vào** một node khác để giới hạn node đó.

**Các node mask trên thanh công cụ:**

| Node | Hình | Dùng khi | Mức |
|---|---|---|---|
| **Rectangle** | Chữ nhật, bo góc được | Crop một phần hình, thanh nền chữ | ★★☆ |
| **Ellipse** | Tròn, bầu dục | Vignette, khoanh mặt người, làm mờ một vùng tròn | ★★☆ |
| **Polygon** | Tự vẽ bằng các điểm (Bézier) | Hình bất kỳ — che biển số, tách một vật | ★★☆ |
| **BSpline** | Tự vẽ, đường cong mềm hơn với ít điểm hơn | Hình tròn trịa như người, xe | ★☆☆ |

Trong Effects Library (nhóm **Mask**) còn có **Triangle**, **Wand** (chọn vùng cùng màu bằng một điểm), **Bitmap**, **Ranges**, **Mask Paint**.

| Node AI | |
|---|---|
| **Magic Mask** | Tách người, vật bằng AI — `Studio`. Bản free dùng Polygon và keyframe |

---

## Rectangle và Ellipse

`★★☆ Thường dùng`

**Cách làm:**
1. Chọn node cần giới hạn (ví dụ một **Blur**). Bấm icon **Rectangle** hoặc **Ellipse** trên thanh công cụ.
2. Mask **tự nối vào đầu vào xanh dương** (Effect Mask) của node đang chọn.
3. Trên Viewer: kéo **tâm** để dời, kéo **cạnh** để đổi kích thước.

**Thông số trong Inspector** (tab **Controls**):

| Thông số | Làm gì | Mức |
|---|---|---|
| **Soft Edge** | Làm mềm mép. `0` = mép sắc | ★★★ |
| **Invert** | Đảo vùng chọn — chọn **bên ngoài** hình | ★★★ |
| **Center X / Y** | Vị trí | ★★☆ |
| **Width / Height** | Kích thước | ★★☆ |
| **Angle** | Xoay | ★☆☆ |
| **Corner Radius** | Bo góc (chỉ Rectangle). `0` = góc vuông, `1` = bo tối đa | ★★☆ |
| **Level** | Độ đậm của mask. Thấp hơn 1 = chỉ chọn một phần | ★☆☆ |
| **Solid** | Bỏ tích → chỉ còn đường viền, độ dày theo **Border Width** | ★☆☆ |

**Ví dụ — làm mờ nền, giữ rõ mặt người:**
1. Chọn MediaIn1, thêm **Blur** (`⇧Space` → `blur`).
2. Chọn Blur, thêm **Ellipse**. Kéo ellipse quanh mặt người.
3. Tích **Invert** → chỉ phần **ngoài** ellipse bị mờ.
4. **Soft Edge** khoảng `0.1` để chuyển mờ êm.

---

## Polygon

`★★☆ Thường dùng`

**Là gì:** mask bạn **tự vẽ** bằng cách bấm từng điểm. Công cụ chính để rotoscope — vẽ lại vùng chọn qua từng khung khi vật chuyển động.

**Cách vẽ:**
1. Thêm Polygon. Một **thanh công cụ Polyline** hiện dọc cạnh Viewer.
2. Bấm từng điểm quanh vùng cần chọn. **Bấm và kéo** để tạo điểm cong.
3. **Bấm lại điểm đầu tiên** để khép hình (hoặc `⇧O`).
4. Khép xong, Polygon tự chuyển sang chế độ sửa: kéo điểm để chỉnh, bấm lên cạnh để thêm điểm.

**Chế độ vẽ trên thanh Polyline:**

| Chế độ | Phím | Làm gì |
|---|---|---|
| **Click Append** | `⇧C` | Bấm từng điểm — mặc định khi bắt đầu |
| **Insert and Modify** | `⇧I` | Thêm điểm vào cạnh, kéo điểm có sẵn |
| **Draw Append** | `⇧D` | Vẽ tự do như bút chì — hợp với bút tablet |
| **Modify Only** | `⇧M` | Chỉ sửa, không thêm điểm |
| **Done** | `⇧N` | Khoá, không sửa được nữa |
| **Close** | `⇧O` | Khép / mở hình |

**Mẹo khi vẽ:**
- Giữ `⇧` khi vẽ: điểm sau bám theo góc 45°.
- `⌘A`: chọn mọi điểm của hình đang sửa.
- `Tab` / `⇧Tab`: chuyển qua lại giữa các hình khi có nhiều mask.
- Chuột phải hình → **Convert Bézier Spline to B-Spline** và ngược lại.

> **Polygon tự bật keyframe.** Ngay khi thêm, mọi lần bạn sửa hình ở một khung mới đều tạo keyframe hình dạng. Vật chuyển động thì đi qua vài khung, chỉnh lại điểm — Fusion tự nội suy ở giữa. Vật đứng yên thì cứ vẽ một lần ở một khung là đủ.

Soft Edge, Invert, Solid, Border Width giống Rectangle.

### Ghép nhiều mask

Nối mask này vào **đầu vào** của mask kia. Mask sau có thêm menu **Paint Mode** để chọn cách ghép:

| Paint Mode | Kết quả |
|---|---|
| **Merge** (mặc định) | Cộng hai vùng lại |
| **Subtract** | Lấy vùng trước trừ vùng sau — khoét lỗ |
| **Minimum** | Chỉ phần giao nhau |
| **Invert** | Đảo phần bị mask sau phủ lên |

**Ví dụ:** Ellipse lớn + Ellipse nhỏ ở giữa với **Subtract** = một vành khuyên.

---

## Gắn mask vào đâu

`★★☆ Thường dùng`

| Gắn vào | Kết quả | Dùng khi |
|---|---|---|
| **Effect Mask** (xanh dương) của một node hiệu ứng | Hiệu ứng chỉ xảy ra **trong vùng mask** | Làm mờ, chỉnh màu một vùng |
| **Effect Mask** của Merge | Chỉ ghép lớp trên **trong vùng mask** | Lớp trên chỉ lộ ra ở một phần khung |
| **Đầu vào** của **MediaIn** | MediaIn có **alpha** theo hình mask — phần ngoài thành trong suốt | Cắt một vật ra khỏi clip để ghép chỗ khác |
| **Garbage Matte** (xám) của **MatteControl** hoặc keyer | Loại bỏ vùng đó khỏi alpha | Cắt bỏ chân đèn, mép phông khi tách phông xanh |

> **Hình đen kịt sau khi nối mask?** Nối mask **chưa có hình** vào MediaIn thì mask đó ra toàn trong suốt — hình biến mất. Cách đúng: để Polygon **đứng riêng**, đưa MediaIn lên Viewer, chọn Polygon để vẽ. Vẽ và khép hình xong rồi mới nối vào MediaIn.

> **Thêm mask cho keyer nhanh:** chuột phải thanh tên node keyer trong Inspector → chọn mask trong menu **Effect Mask**, **SolidMatte** hoặc **GarbageMatte**.

Mask nối vào Effect Mask được áp **sau** hiệu ứng: node xử lý cả hình rồi mới cắt theo mask. Node Saver, Resize, Scale, Crop không có Effect Mask.

---

## Tracker — bám một điểm

`★★☆ Thường dùng`

**Là gì:** node phân tích một **điểm nhỏ, rõ nét** trong hình (góc cửa sổ, mắt, logo trên áo) qua từng khung, tạo ra **đường chuyển động**. Rồi dùng đường đó để gắn thứ khác bám theo, hoặc để chống rung.

**Dùng khi:** gắn chữ, mũi tên, hình bám theo người hoặc vật đang chuyển động. Gắn chữ vào một toà nhà khi máy quay lia qua.

**Bốn chế độ** (tab **Operation**, menu **Operation**):

| Chế độ | Làm gì | Mức |
|---|---|---|
| **Match Move** | Áp chuyển động đã track lên một hình khác — **gắn chữ, hình bám theo** | ★★☆ |
| **Match Move** + Merge **BG Only** | Ngược lại: **khử** chuyển động — chống rung | ★☆☆ |
| **Corner Position** | Track bốn góc, ghép một hình vào bốn góc đó — thay màn hình, biển hiệu | ★☆☆ |
| **Perspective Position** | Track bốn góc rồi kéo thẳng phối cảnh | ★☆☆ |

Ở bản Studio, hai việc dùng bốn góc này làm bằng **Planar Tracker** dễ hơn — xem bên dưới. Bản free dùng Corner Position của Tracker thường.

### Bước 1 — Nối và đặt ô track

1. Thêm **Tracker** (`⇧Space` → `tracker`). Nối hình cần track vào **đầu vào Background** (vàng) của Tracker. Tracker chỉ phân tích hình ở đầu vào này.
2. Chọn Tracker, đưa nó lên Viewer. Một **ô xanh lá** hiện ra.
3. Rê chuột lên ô: hiện **hai khung**. Khung **liền** bên trong là **pattern** — chi tiết cần bám. Khung **nét đứt** bên ngoài là **vùng tìm**.
4. Kéo **tay nắm nhỏ ở góc trên trái** khung trong để đặt nó lên chi tiết cần bám. Một ô phóng to hiện ra giúp căn chính xác.
5. Kéo cạnh khung trong để vừa khít chi tiết. Kéo cạnh khung ngoài nếu vật di chuyển nhanh.

Ô đang chọn có màu **đỏ**, ô không chọn màu **xanh lá**.

**Chọn chi tiết tốt để bám:**
- **Tương phản cao**, rõ nét, có hình dạng riêng — góc, chấm, chữ. Tránh mảng trơn như bầu trời, bức tường trắng.
- **Thấy được suốt đoạn** — không bị che, không ra khỏi khung.
- **Không đổi hình dạng** nhiều.
- Vật chạy nhanh sang ngang → nới **vùng tìm** rộng theo chiều ngang. Vùng tìm nhỏ hơn quãng vật đi được trong một khung thì track sẽ trượt.

### Bước 2 — Track

Các nút track ở **đầu tab Tracker** trong Inspector:

| Nút | Track |
|---|---|
| **Track Forward** | Từ đầu vùng render tới cuối |
| **Track Forward from Current Frame** | Từ khung hiện tại tới cuối |
| **Track Reverse** | Từ cuối vùng render ngược về đầu |
| **Track Backward from Current Frame** | Từ khung hiện tại ngược về đầu |

Dừng: nút **Stop**, hoặc `Esc`. Đang track thì không dùng được Node Editor.

Xong, Viewer hiện **đường chuyển động** với các vạch nhỏ — mỗi vạch là một keyframe vị trí.

**Đổi tên tracker** cho dễ tìm: bấm đúp tên trong **Tracker List**, gõ tên mới (ví dụ `Toa nha`). Bấm **Add** để thêm tracker thứ hai, thứ ba trong cùng node.

### Bước 3 — Gắn thứ khác bám theo

**Cách A — Tracker kiêm luôn Merge** (đơn giản nhất):
1. Nối lớp cần gắn (ví dụ Text+) vào **đầu vào Foreground** của Tracker.
2. Tab **Operation** → **Operation: Match Move**.
3. Menu **Merge** → **FG Over BG**. Tracker giờ làm việc như một Merge: lớp chữ đặt lên video và đi theo chuyển động.
4. Nối đầu ra Tracker vào MediaOut.

**Cách B — nối dữ liệu track vào thông số của node khác** (linh hoạt hơn):
1. Để Tracker **rẽ nhánh** từ MediaIn, đầu ra không cần nối đi đâu — nó chỉ giữ dữ liệu.
2. Chọn node cần bám, ví dụ Text+. Sang tab **Layout**.
3. **Chuột phải** vào hàng **Center X / Y** → **Connect To** → **Tracker1** → **`<tên tracker>`: Offset position**.
4. Chữ nhảy tới đúng điểm đã track và đi theo nó.
5. Muốn chữ lệch lên trên điểm track một chút: chọn lại Tracker1, chỉnh **X Offset / Y Offset**. Đường đứt đỏ trên Viewer cho thấy độ lệch.

Cách B dùng được cho bất cứ thông số **Center**, **Pivot** nào — ví dụ cho một Ellipse bám theo để làm mờ mặt người đi lại.

> **Track bị giật ở vài khung?** Mở **Spline Editor**, tìm đường **Displacement** của tracker, sửa các điểm lệch bằng tay.

---

## Planar Tracker — bám mặt phẳng

`Studio`

> **Bản free không có node này.** Đã thử trên Resolve 21.0.4 bản free: Planar Tracker, Planar Transform, Camera Tracker và Surface Tracker đều không thêm được vào comp. Tracker thường và Delta Keyer thì có. Phần dưới để bạn biết nó làm gì khi lên bản Studio.

**Là gì:** track cả một **mặt phẳng** (biển số, biển hiệu, màn hình, bức tường) thay vì một điểm. Ra được cả **phối cảnh** — mặt phẳng nghiêng thế nào, hình gắn vào nghiêng theo thế đó. Chịu được khi một phần mặt phẳng bị che hoặc ra khỏi khung tốt hơn Tracker thường.

**Dùng khi:** thay chữ trên biển hiệu, dán poster lên tường trống, thay nội dung màn hình điện thoại, che biển số xe.

**Bốn chế độ (Operation Mode):**

| Chế độ | Làm gì |
|---|---|
| **Track** | Phân tích mặt phẳng — luôn làm bước này trước |
| **Steady** | Khử mọi chuyển động của mặt phẳng — để vẽ, sửa trên hình đứng yên |
| **Corner Pin** | Ghép một hình (nối vào Foreground) vào bốn góc trên mặt phẳng, kèm phối cảnh |
| **Stabilize** | Làm mượt rung lắc nhưng giữ chuyển động máy chủ ý |

**Cách làm — dán một hình lên tường:**
1. Thêm **Planar Tracker**, nối clip vào **đầu vào Background**. Đưa Planar Tracker lên Viewer.
2. **Operation Mode: Track**.
3. Tua tới khung mà mặt phẳng **to nhất, rõ nhất, không bị che**. Bấm nút **Set** trong Inspector để lấy khung này làm **khung tham chiếu**.
4. Ngay tại khung đó, **bấm từng điểm** vẽ một đa giác quanh vùng mặt phẳng cần track. Chọn vùng **không bị người, vật đi qua che**.
5. Về lại khung tham chiếu, bấm **Track To End**. Track ngược nếu khung tham chiếu ở giữa clip.
6. Phát lại kiểm tra. Mẹo: chuyển sang **Steady** rồi tua — mặt phẳng đứng yên tuyệt đối là track tốt, còn trôi là track kém.
7. Bấm **Create Planar Transform**. Fusion tạo node **Planar Transform** mang dữ liệu track.
8. Nối hình cần dán (ảnh poster, chữ…) vào Planar Transform, rồi Merge kết quả lên video gốc.

**Chọn vùng tốt để track:**
- Phải là **mặt phẳng thật**. Càng không phẳng, track càng trượt.
- **Càng to càng tốt**, càng nằm trọn trong khung càng tốt.
- Chọn khung mà mặt phẳng **nhìn thẳng**, không quá xiên.
- Ống kính góc rộng méo hình làm track trượt. Sửa méo trước (ở bản free, Lens Correction không có — xem [Free và Studio](../../01-bat-dau/free-vs-studio.md)).

> Vật đi ngang che mặt phẳng: vẽ một mask quanh vật đó, nối vào đầu vào **occlusion mask** (trắng) của Planar Tracker để nó bỏ qua vùng đó.

> **Biết khi nào bỏ cuộc:** có những cảnh không track được. Track rung hoặc trôi mãi không sửa được thì chuyển sang Tracker thường, hoặc keyframe tay.

---

## Delta Keyer — tách phông xanh

`★★☆ Thường dùng`

**Là gì:** node tách phông xanh lá hoặc xanh dương (thực ra tách được **mọi màu nền**), tạo ra alpha — người đứng trước phông thành lớp có nền trong suốt.

**Dùng khi:** quay trước phông xanh, muốn thay nền bằng cảnh khác.

### Cách làm cơ bản

1. Chọn MediaIn của clip phông xanh. `⇧Space` → `delta` → `Return`. **DeltaKeyer1** chèn ngay sau.
2. Nếu cần ghép nền mới: thêm clip nền từ Media Pool, rồi kéo đầu ra DeltaKeyer1 thả lên đầu ra clip nền → tự tạo Merge, người ở lớp trên. Đưa Merge lên Viewer 2.
3. Chọn DeltaKeyer1. Ở tab **Key**, kéo **ống nhỏ giọt** (cạnh ô **Background Color**) ra Viewer, thả lên **mảng phông xanh**. Khi kéo, một ô nhỏ cho biết màu đang hút. Chọn chỗ phông có độ sáng trung bình, đừng lấy chỗ sát người.
4. Thả chuột — Viewer 2 thấy ngay người trên nền mới.

### Kiểm tra alpha

Nhìn kết quả ghép thường **đánh lừa**. Luôn kiểm tra kênh alpha:

1. Đưa **DeltaKeyer1** lên Viewer 1.
2. Bấm vào Viewer, bấm `C` (hoặc nút **Color** trên thanh Viewer) để đổi sang xem **alpha**.
3. Đọc hình: **đen** = trong suốt, **trắng** = đặc, **xám** = nửa trong suốt.

Người phải **trắng tinh**, nền phải **đen kịt**. Chỉ tóc, mép áo mỏng được phép xám. Thấy lốm đốm xám trên người hoặc đốm trắng trên nền là cần tinh chỉnh.

### Tinh chỉnh

**Tab Key:**

| Thông số | Làm gì |
|---|---|
| **Gain** | Tăng để phông trong suốt hơn. Tăng quá thì người cũng bị thủng |
| **Balance** | Đẩy màu người lệch về đỏ hoặc xanh dương, đổi cách tính độ trong |

**Tab Matte** (tab thứ ba):

| Thông số | Làm gì |
|---|---|
| **Threshold** (Low / High) | Kéo Low lên để nền đen hơn, kéo High xuống để người trắng hơn |
| **Clean Background** | Lấp đốm trắng lốm đốm trên nền |
| **Clean Foreground** | Lấp lỗ xám trên người |
| **Replace Mode** | Cách xử lý ánh xanh hắt lên người (spill) |

> Chỉnh **Clean Foreground** và **Clean Background** thật nhẹ. Tăng nhiều thì mép người cứng và mất chi tiết tóc.

**Bảy tab của Delta Keyer:** **Key**, **Pre-Matte**, **Matte**, **Fringe**, **Tuning**, **Mask**, **Settings**. Người mới chỉ cần Key và Matte.

### Ánh xanh hắt lên người (spill)

Phông xanh phản sáng lên tóc, vai, mép áo — người bị viền xanh. Delta Keyer tự khử spill, nhưng đôi khi làm da người lệch màu.

Cách xử lý gọn hơn: tab **Matte** → **Replace Mode: Source** (tắt khử spill), rồi thêm một node chỉnh màu (ColorCorrector) sau Delta Keyer để giảm màu xanh lá.

### Chân đèn, mép phông lọt vào

Phông không đủ rộng, lộ chân đèn hoặc mép phòng: vẽ một **Polygon** quanh người (thoáng rộng), nối vào đầu vào **Garbage Matte** (xám) của Delta Keyer. Mọi thứ ngoài vùng đó bị loại.

### Không cần ghép trong Fusion

Chỉ cần **MediaIn → DeltaKeyer → MediaOut**. Alpha được đưa về timeline. Ở trang Edit, đặt clip nền ở **track dưới** — nó hiện ra qua chỗ trong suốt.

> **Quay phông xanh cho dễ key:** phông phẳng, chiếu sáng đều, không nhăn. Người đứng **cách phông** vài mét để ít spill. Không mặc đồ cùng màu phông. Tốc độ màn trập cao để tóc, tay ít nhoè chuyển động.
