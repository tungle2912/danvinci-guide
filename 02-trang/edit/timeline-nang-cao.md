# Timeline nâng cao — phiên bản, compound, multicam

Những công cụ này không dùng mỗi ngày. Nhưng khi cần thì chúng tiết kiệm hàng giờ.

---

## Tạo timeline và Timeline Settings

`★★★ Hằng ngày`

### Tạo timeline mới

| Cách | Kết quả |
|---|---|
| **File → New Timeline** (`⌘N`) | Hộp thoại đầy đủ |
| Chuột phải Media Pool → **Timelines → Create New Timeline** | Như trên |
| Chọn clip → chuột phải → **Create Timeline Using Selected Clips** | Timeline có sẵn các clip, theo thứ tự sắp xếp của Media Pool |
| Chuột phải một bin → **Create Timeline Using Bin** | Timeline chứa mọi clip trong bin |
| Kéo một clip thả vào vùng timeline trống (project chưa có timeline) | Tự tạo timeline |

Timeline mới nằm trong **bin đang chọn**. Nên có một bin riêng tên `Timelines`.

**Trong hộp thoại New Timeline:**

| Mục | Ý nghĩa |
|---|---|
| **Start Timecode** | Timecode bắt đầu. Mặc định `01:00:00:00` |
| **Timeline Name** | Đặt tên ngay, đừng để `Timeline 1` |
| **No. of Video Tracks / Audio Tracks** | Số track ban đầu |
| **Audio Track Type** | Mono, Stereo… |
| **Empty Timeline** | Bỏ tick = đưa **mọi** clip trong Media Pool vào |
| **Use Selected Mark In/Out** | Dùng đoạn `I` `O` đã đặt sẵn trên từng clip |
| **Use Custom Settings** | Mở thêm tab Format, Monitor, Output — cho timeline này **khác** project |

### Timeline Settings — mỗi timeline một cỡ khung

`★★☆ Thường dùng`

**Là gì:** mỗi timeline có thể có độ phân giải, frame rate riêng, khác cài đặt chung của project.

**Mở:** chuột phải timeline trong Media Pool → **Timelines → Timeline Settings** → bỏ tick **Use Project Settings**.

**Làm timeline dọc 9:16:** trong tab Format, chọn độ phân giải rồi tick **Use vertical resolution** — Resolve đảo chiều ngang và dọc. Hoặc gõ thẳng `1080 × 1920`.

**Dùng khi:** cùng một project cần bản ngang cho YouTube và bản dọc cho Reels. Cách làm đầy đủ: [Video dọc](../../03-luong/video-doc.md).

> Frame rate của timeline **không đổi được** sau khi đã có clip. Chọn đúng từ đầu — xem [Tạo project](../../01-bat-dau/tao-du-an.md).

**Đổi timecode bắt đầu cho nhiều timeline:** chọn các timeline → chuột phải → **Timelines → Starting Timecode**.

---

## Nhân bản timeline — giữ phiên bản

`★★★ Hằng ngày`

**Là gì:** tạo bản sao y hệt của timeline. Sửa bản sao, bản gốc nguyên vẹn.

**Cách làm** (một trong):
- Chọn timeline trong Media Pool → **Edit → Duplicate Timeline**.
- Chuột phải timeline → **Duplicate Timeline**.
- Chuột phải **tab** timeline (khi bật tab) → **Duplicate Timeline** — bản sao mở luôn trong tab mới.

Bản sao có chữ `copy` ở cuối tên. Đổi tên ngay cho dễ nhớ.

**Dùng khi:**
- Trước khi sửa lớn theo góp ý khách hàng — giữ lại bản đã gửi.
- Làm bản 60 giây từ bản 3 phút.
- Làm bản dọc từ bản ngang.

**Cách đặt tên gợi ý:**

| Tên | Là gì |
|---|---|
| `Vlog_v1_gui-khach` | Bản đã gửi, không đụng nữa |
| `Vlog_v2` | Bản đang sửa |
| `Vlog_v2_60s` | Bản rút gọn |
| `Vlog_v2_doc` | Bản dọc |

> Mỗi timeline có **màu riêng** (grade riêng) cho từng clip, kể cả bản sao. Chỉnh màu ở bản sao không ảnh hưởng bản gốc.

### Tắt timeline cũ cho project nhẹ

`★☆☆ Tình huống cụ thể`

Chuột phải timeline → **Disable Timeline**. Timeline vẫn nằm trong Media Pool (có icon con mắt gạch chéo) nhưng **không được nạp vào RAM** — project mở và lưu nhanh hơn. Không mở được cho tới khi **Enable Timeline** lại.

**Dùng khi:** đã có hàng chục bản v1, v2, v3… làm project chậm đi.

### Timeline Backup — điểm khôi phục

`★★☆ Thường dùng`

| Việc | Cách |
|---|---|
| Bật tự sao lưu timeline | **Preferences → User → Project Save and Load** → tick **Timeline Backups** |
| Tạo điểm sao lưu bằng tay | **File → Create Timeline Backup** (`⌥⌘S`) |
| Khôi phục | Chuột phải timeline → **Restore Timeline Backup** → chọn mốc giờ |
| So sánh với bản cũ | Chuột phải timeline → **Compare with Timeline Backup** |

Khôi phục **không ghi đè** timeline hiện tại — bản khôi phục hiện ra thành timeline mới có chữ `Backup`.

### Mở nhiều timeline cùng lúc

`★☆☆ Tình huống cụ thể`

**Timeline View Options** → bật **Stacked Timelines**. Timeline hiện dạng **tab**. Nút **Add Timeline** ở cuối thanh tab cho **xếp chồng** hai timeline trên dưới — kéo clip từ timeline này sang timeline kia.

**Dùng khi:** gom cảnh đẹp từ timeline "selects" sang timeline dựng chính.

---

## Compound Clip — gộp nhiều clip thành một

`★★☆ Thường dùng`

**Là gì:** gộp một nhóm clip (nối tiếp hoặc chồng nhiều track) thành **một clip duy nhất** trên timeline. Bên trong vẫn còn đủ các clip gốc.

**Vì sao hữu ích:**
- Áp **một** hiệu ứng, một Transform, một chuyển cảnh cho cả nhóm.
- Ở trang Color, nhóm hiện như **một clip** — chỉnh màu một lần.
- Timeline gọn hơn.

### Cách tạo

| Cách | Làm |
|---|---|
| Từ các clip đang chọn | Chọn clip → chuột phải → **New Compound Clip** → đặt tên → **Create** |
| Từ một đoạn `I` `O` | Đặt `I` `O` trên timeline → chuột phải vùng `I`→`O` trên thước → **Convert In and Out to Compound Clip** |

Cách `I` `O` lấy được **một phần** clip ở hai đầu, và lấy **mọi track** trong khoảng đó.

Một bản sao của compound clip cũng xuất hiện trong Media Pool — kéo xuống timeline khác dùng lại được.

### Sửa bên trong

1. Chuột phải compound clip → **Open in Timeline**.
2. Sửa như timeline bình thường.
3. Quay ra: bấm đúp **tên timeline chính** trên **thanh đường dẫn** ở góc dưới trái timeline.

### Tách ra lại

Chuột phải → **Decompose in Place**. Compound clip biến mất, các clip gốc trở lại đúng chỗ.

**Ví dụ:** logo + chữ + nền màu chồng trên ba track. Gộp thành compound clip → thêm Cross Dissolve một lần ở đầu và cuối, thay vì ba lần. Dùng lại ở intro mọi video.

### Timeline lồng trong timeline (nested)

Kéo **một timeline** từ Media Pool vào timeline khác → nó thành một clip, giống compound clip. Sửa: chuột phải → **Open in Timeline**.

**Muốn lấy clip gốc chứ không lấy cả khối:** bật **Edit → Decompose Compound Clips on Edit** trước khi edit. Hoặc mở timeline đó ở Viewer Source, đặt con trỏ vào clip cần lấy, bấm `X` để đặt `I` `O` ôm đúng clip đó, rồi `F10`.

**Dùng khi:** có timeline "selects" gom câu hay nhất của mỗi buổi phỏng vấn, muốn dựng tiếp từ đó.

---

## Freeze Frame — dừng hình

`★★☆ Thường dùng`

### Dừng cả clip

1. Đặt con trỏ ở **khung muốn dừng**.
2. Chọn clip → **Clip → Freeze Frame** (`⇧R`).

**Cả clip** thành ảnh tĩnh của khung đó, độ dài giữ nguyên.

Bỏ freeze: chuột phải clip → **Change Clip Speed** → bỏ tick **Freeze Frame**.

### Dừng ở giữa clip rồi chạy tiếp

1. Chọn clip → `⌘R` để hiện thanh tốc độ.
2. Đặt con trỏ ở khung muốn dừng.
3. Bấm **mũi tên nhỏ** cạnh số % ở đáy clip → **Freeze Frame**.
4. Hai điểm tốc độ hiện ra. Kéo điểm thứ hai để chỉnh **dừng bao lâu**.

**Kết quả:** chạy bình thường → dừng hình → chạy tiếp từ khung kế.

**Ví dụ:** vlog giới thiệu bạn đồng hành — dừng hình đúng lúc bạn ấy quay lại cười, thêm chữ tên bằng Text+ phía trên, rồi chạy tiếp.

> Tốc độ, speed ramp: xem [Retime](inspector.md#tốc-độ--retime).

---

## Multicam — dựng nhiều góc máy

`★☆☆ Tình huống cụ thể`

**Là gì:** gộp các clip quay **cùng lúc** từ nhiều máy thành **một multicam clip**. Khi phát, bạn bấm chọn góc máy như đạo diễn truyền hình — Resolve tự cắt trên timeline.

**Dùng khi:** phỏng vấn hai máy, podcast ba máy, sân khấu, đám cưới.

### Bước 1 — tạo multicam clip

1. Chọn mọi clip của các góc máy trong Media Pool.
2. Chuột phải → **Create Multicam Clip Using Selected Clips**.
3. Chọn **Angle Sync** — cách khớp các góc:

| Angle Sync | Khi nào chọn |
|---|---|
| **Sound** | Mỗi máy đều thu tiếng — **hay dùng nhất** với máy ảnh, điện thoại |
| **Timecode** | Các máy được đồng bộ timecode |
| **In** / **Out** | Bạn đã tự đặt `I` (hoặc `O`) ở cùng một khoảnh khắc trên mỗi clip — ví dụ tiếng vỗ tay |
| **Marker** | Bạn đã tự đặt marker ở cùng một khoảnh khắc |

4. **Create**. Multicam clip có badge riêng ở góc thumbnail.

> **Mẹo quay:** vỗ tay một cái thật rõ trước mặt mọi máy khi bắt đầu. Sync bằng Sound gần như luôn khớp.

### Bước 2 — đưa vào timeline

Kéo multicam clip xuống timeline như clip thường.

### Bước 3 — cắt chọn góc

1. Menu **Source Viewer Mode** (dưới Viewer Source) → **Multicam**. Viewer Source chia lưới, mỗi ô một góc.
2. Menu ở góc dưới phải Viewer: chọn lưới **2×2**, **3×3**… Máy yếu thì chọn ít góc.
3. Chọn đổi **cả hình và tiếng**, **chỉ hình**, hay **chỉ tiếng** bằng nút ở giữa đáy Viewer. Thường chọn **chỉ hình** để tiếng giữ một nguồn tốt nhất.
4. Phát timeline. Bấm vào góc nào là **cắt và chuyển** sang góc đó.

| Thao tác | Kết quả |
|---|---|
| Bấm một góc | Cắt tại con trỏ và chuyển góc |
| `⌥`-bấm một góc | **Đổi góc** đoạn hiện tại, **không** thêm vết cắt |
| Phím `1`…`9` | Cắt sang góc số đó |
| `⌘⇧←` / `⌘⇧→` | Đổi sang góc trước / sau |

5. Dừng phát là xong. Chọn lại **Source** ở Source Viewer Mode để trim như clip thường.

**Sửa một góc đã chọn sai:** đặt con trỏ trong đoạn đó, `⌥`-bấm góc đúng.

**Chỉnh multicam clip** (dời lệch sync, xoá góc thừa, đổi tên góc): chuột phải multicam clip trong Media Pool → **Open in Timeline**.

> **Multicam SmartSwitch** — tự chọn góc theo người đang nói — là `Studio`.

---

## Edit Index — danh sách mọi điểm cắt

`★☆☆ Tình huống cụ thể`

**Mở:** nút **Index** ở góc trên trái → tab **Edit Index**.

**Là gì:** bảng liệt kê mọi clip và chuyển cảnh trên timeline, kiểu danh sách EDL: số thứ tự, tên, timecode nguồn, timecode trên timeline, codec, độ phân giải, màu, ghi chú marker…

**Bấm một dòng** là con trỏ nhảy tới clip đó.

### Lọc — menu ⋯ của Edit Index

| Lọc | Dùng khi |
|---|---|
| **Show Through Edits** | Tìm các vết cắt thừa (hai nửa cùng một clip liền nhau) |
| **Show Offline Clips** | Tìm clip mất file gốc |
| **Show Markers** / **Show Flags** | Đi qua mọi ghi chú cần sửa |
| **Show Clips With Speed Effects** | Kiểm tra clip đã đổi tốc độ |
| **Show Clips With Transform Effects** | Clip đã zoom, dời |
| **Show Stills and Freeze Frames** | Ảnh tĩnh, clip dừng hình |
| **Show Compound Clips and Nested Timelines** | Tìm các khối gộp |
| **Show Video / Audio Track Items** | Chỉ xem hình hoặc chỉ xem tiếng |
| **Show All** | Bỏ lọc |

**Xuất danh sách:** menu ⋯ → **Export Edit Index** → `.csv` hoặc `.txt`. Gửi cho người khác tìm lại file thiếu.

**Đổi cột:** chuột phải tên cột để ẩn/hiện. Kéo tên cột để đổi thứ tự.

### Hai tab còn lại

| Tab | Làm gì |
|---|---|
| **Tracks** | Danh sách mọi track: đổi tên, màu, khoá, tắt, ẩn track. Kéo cột `#` để đổi thứ tự |
| **Markers** | Danh sách mọi marker. Sửa tên, ghi chú ngay trong bảng. Bấm đúp để nhảy tới |

---

## Flag, màu clip, màu track

`★☆☆ Tình huống cụ thể`

Ba cách tô màu, mỗi cách một ý nghĩa:

| | Flag | Màu clip | Màu track |
|---|---|---|---|
| Gắn vào | **File gốc** — mọi lần dùng file đó đều có cờ | **Riêng lần dùng đó** trên timeline | Cả track |
| Hiện ra | Badge cờ trên clip | Clip đổi màu | Dải màu đầu track, clip trên track đổi màu theo |
| Cách thêm | Chọn clip → `G`, hoặc nút **Flag** | Chuột phải clip → **Clip Color** | Chuột phải đầu track → **Change Track Color** |
| Bỏ | Mũi tên cạnh nút Flag → xoá | **Clip Color → Default Color** | Đổi màu khác |

Màu clip **đè lên** màu track.

**Cách dùng gợi ý:**
- **Flag đỏ:** file có vấn đề (mất nét, cháy sáng) — mọi chỗ dùng file đó đều hiện cờ, khỏi sót.
- **Màu clip cam:** cảnh tạm, sẽ thay.
- **Màu track:** xanh lá cho lời, tím cho nhạc, vàng cho SFX — nhìn timeline là biết.

Lọc theo màu: [Edit Index](#edit-index--danh-sách-mọi-điểm-cắt) → **Show Flags** / **Show Clip Colors**.

---

## Tìm nhanh

| Muốn | Cách |
|---|---|
| Timeline đang mở nằm ở bin nào | **Timeline → Find Current Timeline in Media Pool** |
| Gom mọi timeline vào một chỗ | **Preferences → User → Editing** → tick **Smart Bin for Timelines** |
| Khoảng trống tiếp theo | `⌥⌘'` (sau) / `⌥⌘;` (trước) |
| Marker tiếp theo | `⇧↓` / `⇧↑` |
