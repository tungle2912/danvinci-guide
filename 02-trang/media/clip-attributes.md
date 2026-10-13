# Clip Attributes — sửa thông số clip

`★★☆ Thường dùng`

**Là gì:** cửa sổ sửa cách Resolve **hiểu** một clip — frame rate, mức sáng, kênh tiếng, timecode, tên.

**Dùng khi:** Resolve đọc sai file, hoặc file không ghi đủ thông tin. Ví dụ: clip slow motion chạy nhanh bất thường, giọng chỉ ra một bên tai, ảnh bệt đen.

**Cách mở:**

| Ở đâu | Làm gì |
|---|---|
| **Media Pool** (trang nào cũng được) | Chọn một hoặc nhiều clip → chuột phải → **Clip Attributes** |
| **Timeline** trang Cut, Edit, Color | Chọn clip trên timeline → chuột phải → **Clip Attributes** |

Cửa sổ có nhiều tab: **Video**, **Audio**, **Timecode**, **Name**, **Reel Name**. Bấm tab cần sửa → sửa → bấm **OK**.

> **Sửa ở đây không đụng tới file trên ổ.** Resolve chỉ ghi lại cách hiểu mới trong project. Muốn quay về: mở lại Clip Attributes, đặt lại giá trị cũ.

---

## Tab Video

Sửa frame rate, tỉ lệ điểm ảnh, mức sáng, hướng hình.

| Mục | Làm gì | Khi nào cần | Mức |
|---|---|---|---|
| **Video Frame Rate** | Đổi fps Resolve coi clip là gì. Chọn từ 1 tới 120, hoặc **Custom** gõ số | Resolve đọc nhầm fps, hay gặp với file slow motion hoặc file đã qua phần mềm khác | ★★☆ |
| **Data Levels** | Chọn **Auto**, **Video** hoặc **Full** | Ảnh bệt đen hoặc cháy trắng bất thường — xem mục dưới | ★★☆ |
| **Pixel Aspect Ratio** | Tỉ lệ một điểm ảnh. **Custom** để gõ số | Hình bị méo ngang hoặc dọc. Footage thường để **Square** | ★☆☆ |
| **Image Orientation** | Xoay 0°, 90° phải, 180°, 90° trái | File có ghi hướng xoay nhưng mở ra bị nằm ngang | ★☆☆ |
| **Horizontal / Vertical Image Flip** | Lật hình ngang/dọc | Chỉ cho file **R3D** (máy RED) | ★☆☆ |
| **Input Sizing Preset** | Gán preset co giãn hình | Nhiều clip SD cần cùng một cách co giãn | ★☆☆ |
| **Field Dominance** | Auto / Upper / Lower | Footage xen kẽ (interlaced) bị rung răng cưa | ★☆☆ |
| **Enable Deinterlacing** | Khử xen kẽ | Footage interlaced cũ | `Studio` |
| **Alpha Mode** | Bật/tắt kênh trong suốt, chọn Premultiplied hay Straight, đảo alpha | File có nền trong suốt (ProRes 4444, chuỗi ảnh PNG/TIFF, EXR) bị viền đen hoặc nền không trong | ★☆☆ |
| **Super Scale** | Phóng to bằng thuật toán, tăng độ phân giải gốc của clip | Đưa footage SD vào timeline 4K | `Studio` |
| **Remove 3:2 Pulldown** | Lấy lại 24 khung gốc từ video 29.97 interlaced | Phim nhựa đã telecine sang NTSC | ★☆☆ |

**Ví dụ — clip slow motion chạy nhanh:** máy quay ghi 120 fps nhưng file ghi là 30 fps. Chọn clip → **Clip Attributes** → **Video Frame Rate** → `120` → **OK**.

> **Đổi Video Frame Rate thì độ dài và tốc độ phát của hình đổi theo, nhưng tiếng thì không.** Clip có tiếng thoại sẽ lệch tiếng. Chỉ dùng cho clip hình, hoặc clip mà bạn sẽ tắt tiếng.

### Data Levels — lỗi hay gặp nhất

**Là gì:** cách Resolve đọc dải sáng của file. **Video** là dải hẹp (16–235), **Full** là dải đầy (0–255). **Auto** để Resolve tự đoán.

**Triệu chứng đoán sai:**

| Hiện tượng | Thường do |
|---|---|
| Vùng đen bệt mất chi tiết, vùng sáng cháy sớm, ảnh quá gắt | File dải hẹp bị đọc như dải đầy |
| Ảnh xám, nhạt, đen không đen hẳn | File dải đầy bị đọc như dải hẹp |

**Cách sửa:**

1. Chọn clip → chuột phải → **Clip Attributes** → tab **Video**.
2. Đổi **Data Levels** từ **Auto** sang **Video** hoặc **Full**.
3. Bấm **OK**, mở Waveform ở trang Color xem lại.

Đúng là khi dải sáng trải đều, không bị cắt cụt ở đầu hoặc đuôi.

> Chỉ đổi khi thấy rõ lỗi. Phần lớn file từ máy ảnh và điện thoại để **Auto** là đúng.

---

## Tab Audio

`★★★ Hằng ngày` với ai quay phỏng vấn bằng máy ảnh.

**Là gì:** nơi quyết định clip mang **mấy track tiếng**, mỗi track **định dạng gì**, và **kênh nào trong file** đi vào đâu.

**Dùng khi:** giọng chỉ ra một bên tai. Mic ngoài và mic trong máy lẫn vào nhau. File có 4 kênh mic muốn tách riêng từng mic.

> Sửa ở đây tác động tới clip **khi kéo xuống timeline sau đó**. Clip đã nằm trên timeline thì không đổi theo — xoá đi và kéo lại.

### Hàng nút trên cùng — thêm track

| Nút | Làm gì |
|---|---|
| **Format** | Chọn định dạng cho track sắp thêm: **Mono**, **Stereo**, **5.1**, **7.1**, **Adaptive** |
| **Tracks** | Số track muốn thêm |
| **Add** | Thêm các track đó vào clip |
| **Reset** (icon) | Trả phần tiếng của clip về như lúc mới nạp |

Bảng chọn định dạng:

| Format | Dùng cho |
|---|---|
| **Mono** | Một kênh. Một mic |
| **Stereo** | Hai kênh trái/phải. Nhạc, mic stereo |
| **5.1** / **7.1** | Âm thanh vòm |
| **Adaptive** | Nhiều kênh mono gom lại: mic boom + hai mic cài áo + track mix |

### Danh sách track bên dưới

Mỗi dòng là một track, các kênh của nó nằm thụt vào bên dưới.

| Cột | Làm gì |
|---|---|
| **Format** | Định dạng của track đó |
| **Source Channel** | Kênh nào trong file đi vào đây. Chọn `<none>` để bỏ kênh |
| **Track** | Tên track |
| **Channel in Track** | Tên kênh trong track |
| **Thùng rác** | Rê chuột lên một track mới hiện. Bấm để xoá track đó |

### Sửa mic mono thu vào một kênh

**Triệu chứng:** giọng chỉ ra ở tai trái hoặc tai phải.

**Cách 1 — giữ Stereo, chép kênh có tiếng sang cả hai bên:**

1. Clip Attributes → tab **Audio**.
2. Ở track Stereo, đặt **Source Channel** của **cả hai kênh** về cùng kênh có tiếng (thường là kênh 1).
3. Bấm **OK**.

**Cách 2 — đổi sang Mono:**

1. Ở hàng trên cùng, đặt **Format** = `Mono`, **Tracks** = `1` → **Add**.
2. Gán **Source Channel** của track mới về kênh có tiếng.
3. Rê chuột lên track Stereo cũ → bấm **thùng rác**.
4. Bấm **OK**.

> Track Mono đặt lên timeline sẽ ra đều hai tai. Đây là cách sạch nhất cho giọng nói.

### Mic ngoài thu vào track 2

Máy ảnh hay ghi mic trong máy vào kênh 1, mic ngoài vào kênh 2.

**Cách làm:** tab Audio → ở kênh mic trong máy, đặt **Source Channel** = `<none>`. Hoặc xoá hẳn track đó bằng thùng rác. Chỉ giữ kênh mic ngoài.

**Ví dụ — file 4 mic:** máy thu ghi 4 kênh, mỗi kênh một người. Thêm `4` track **Mono** → gán mỗi track một **Source Channel** → xoá track gốc. Kéo xuống timeline sẽ thành 4 clip tiếng riêng, chỉnh từng người được.

---

## Tab Timecode

`★☆☆ Tình huống cụ thể`

**Là gì:** sửa timecode của clip **trong project**. File gốc không đổi.

**Dùng khi:** đồng bộ nhiều máy quay theo timecode mà một máy bị lệch.

| Mục | Làm gì |
|---|---|
| **Current Frame Timecode** | Gõ timecode mới cho **khung đang xem**. Cả clip dời theo |
| **Slate Timecode** | Gõ timecode đọc được trên bảng clapper. Thành timecode thứ hai, không thay timecode chính |
| **Offset Source Timecode** | Cả loạt clip lệch đều một khoảng → dời cùng lúc |

**Ví dụ — cả thẻ nhớ lệch đúng 1 giờ:** chọn mọi clip của thẻ → **Clip Attributes** → **Timecode** → **Offset Source Timecode** → gõ khoảng lệch → **OK**.

> **Máy quay thu timecode vào kênh tiếng (LTC)?** Chọn clip → chuột phải → **Update timecode from audio - LTC**. Resolve đọc LTC và sửa timecode ngay, không cần mở Clip Attributes.

---

## Tab Name

`★★☆ Thường dùng`

**Là gì:** đổi **Clip Name** — tên hiển thị trong Resolve — mà **không đổi tên file trên ổ**.

**Ví dụ:** file từ máy ảnh tên `C0042.MP4`. Đặt tên hiển thị là `Phỏng vấn anh An - take 3`.

Tên mới hiện ở Media Pool, trên clip ở timeline và thanh tiêu đề Viewer.

**Đặt tên tự động theo metadata:**

1. Chọn nhiều clip → **Clip Attributes** → tab **Name**.
2. Trong ô **Clip Name**, gõ `%` → danh sách biến hiện ra.
3. Chọn biến (bấm `↑` `↓` rồi `Return`), xen chữ thường vào giữa. Ví dụ: biến **Scene**, gõ `_`, biến **Shot**, gõ `_`, biến **Take**. Biến hiện thành ô có nền.
4. Bấm **OK**.

Clip có Scene `12`, Shot `A`, Take `3` sẽ tên là `12_A_3`. Trường metadata nào trống thì biến đó không hiện gì.

> Cần gõ metadata trước — xem [Metadata Editor](metadata.md). Đổi qua lại tên file và tên clip: **View → Show File Names**.

---

## Tab Reel Name

`★☆☆ Tình huống cụ thể`

Dùng khi trao đổi project với phần mềm khác qua EDL. Tab này **chỉ sửa được** khi đã bật **Assist using Reel Names** trong **Project Settings → General Options**.

Các cách lấy reel name: từ đường dẫn file (kèm **Pattern**), từ tên bin, từ dữ liệu nhúng trong file, từ tên file, hoặc **User Defined** để gõ tay.

> Dựng vlog, YouTube thì bỏ qua tab này.

---

## Áp cho nhiều clip

`★★★ Hằng ngày`

1. Chọn nhiều clip: `⇧`-click, `⌘`-click, hoặc kéo khung chọn.
2. Chuột phải một clip đã chọn → **Clip Attributes**.
3. Sửa mục cần. Mục nào bạn sửa sẽ **tự được tick** — chỉ các mục có tick mới áp cho cả nhóm.
4. Bấm **OK**.

**Ví dụ:** cả thẻ nhớ bị đọc sai frame rate, hoặc mọi clip phỏng vấn cùng bị tiếng một bên. Sửa một lần cho cả nhóm.

> Mẹo: dùng [Smart Bin](bin.md#3-smart-bin) lọc ra đúng nhóm clip cần sửa (ví dụ cùng camera, cùng fps), chọn hết rồi mở Clip Attributes.
