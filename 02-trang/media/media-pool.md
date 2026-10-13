# Media Pool — kho clip

Vùng dưới trang Media. Chứa **mọi clip bạn đã nạp** và **mọi timeline bạn tạo**.

Media Pool xuất hiện ở cả trang Cut, Edit, Fusion, Color và Fairlight — cùng một kho, chỉ là hiển thị nhỏ hơn. Ở trang Media nó được dành nhiều chỗ nhất nên đây là nơi để sắp xếp.

> Resolve tách bạch **media nguồn** và **timeline**. Cả hai đều nằm trong Media Pool nhưng được quản lý riêng. Nhờ vậy bạn thay thế, nối lại, chuyển đổi offline/online media mà không đụng tới bản dựng.

Bản đồ từng nút trên Media Pool: [Giao diện → Media Pool](giao-dien.md#media-pool).

## Nút Bin List

`★★★ Hằng ngày`

Nằm ở **góc trên trái Media Pool**. Bật/tắt cột danh sách bin bên trái.

- **Mở** — thấy toàn bộ cây bin, dễ kéo clip từ bin này sang bin kia.
- **Đóng** — không thấy bin, chỉ thấy nội dung bin đang chọn. Rộng chỗ hơn.

Ngay bên phải nút này là menu **Color Tag Filter** — chỉ hiện các bin cùng màu nhãn.

Chi tiết về bin: [Bin, Power Bin, Smart Bin](bin.md).

---

## Chọn clip

`★★★ Hằng ngày`

Gần như mọi lệnh đều bắt đầu bằng việc chọn clip.

| Muốn chọn | Cách |
|---|---|
| Một clip | Bấm vào clip |
| Một dải liền nhau | Bấm clip đầu, giữ `⇧` bấm clip cuối |
| Rải rác | Giữ `⌘` bấm từng clip. `⌘` bấm lại để bỏ chọn |
| Một nhóm gần nhau | Kéo khung chữ nhật quanh chúng |
| Mở rộng bằng phím | Đã chọn một clip, giữ `⇧` hoặc `⌘` rồi bấm phím mũi tên |

---

## Ba kiểu hiển thị

Ba icon ở góc trên phải Media Pool:

### Thumbnail view

`★★★ Hằng ngày`

Hiện ảnh đại diện. Rê chuột ngang thumbnail là xem nhanh (skim) toàn bộ clip.

Kéo thả để sắp xếp thủ công theo ý mình.

| Nút / thao tác | Làm gì |
|---|---|
| **Thanh trượt cỡ thumbnail** | To ra để dễ nhìn, nhỏ lại để thấy nhiều clip |
| **Clip Info** (mũi tên góc dưới phải thumbnail) | Xem nhanh thông tin clip |
| **Menu sắp xếp** (Sort Order) | Sắp theo File Name, Reel Name, Clip Name, Start TC, Duration, Type, FPS, Audio Ch, Flags, Date Modified, Date Created, Shot, Scene, Take |
| **Sort Order → Custom** | Kéo thumbnail đi đâu cũng được. Tick **Snap to Grid** để xếp thẳng hàng, bỏ tick để đặt tự do |

Vị trí bạn kéo ở chế độ **Custom** được giữ ở mọi trang, kể cả khi bạn chuyển sang kiểu sắp khác rồi quay lại.

**Đổi ảnh đại diện (poster frame):** mặc định thumbnail là khung đầu tiên — hay bị đen hoặc mờ. Rê chuột tới khung đẹp → chuột phải → **Set Poster Frame** (`⌘P`). Bỏ: **Clear Poster Frame** (`⌥P`).

**Vạch dùng clip:** khi một timeline đang mở, đáy thumbnail hiện **vạch màu** đánh dấu phần nào của clip đã nằm trên timeline. Chuột phải → **Usage** để xem danh sách và nhảy tới từng chỗ dùng.

> **Mẹo cho người làm vlog:** sắp theo **Date Created** là clip xếp đúng thứ tự quay. Đỡ phải nhớ cảnh nào trước cảnh nào.

### List view

`★★☆ Thường dùng`

Dạng bảng nhiều cột, giống List view của Media Storage nhưng thêm các cột **sửa được trực tiếp**: **Name, Description, Keyword, Comments**.

Gõ thẳng vào ô là xong, không cần mở Metadata Editor. Cách bấm: **bấm một lần, chờ một nhịp, bấm lần nữa** để ô thành ô gõ.

**Customize Columns — chọn cột:** chuột phải tiêu đề cột bất kỳ → cửa sổ **Customize Columns** mở ra.

| Việc | Cách |
|---|---|
| Hiện/ẩn cột | Tick/bỏ tick trong **Column Fields** → **Save** |
| Đổi thứ tự | Kéo tiêu đề cột, hoặc kéo tên cột trong **Selected Fields** |
| Lưu thành preset | Trong Customize Columns → menu tuỳ chọn → **Save as New Preset** |
| Gọi preset | Chuột phải tiêu đề cột → **Load Custom Layout** |
| Sửa / xoá preset | Menu tuỳ chọn trong Customize Columns → **Update** / **Delete Preset** |

**Cột đáng bật:**

| Cột | Cho biết |
|---|---|
| **Usage** | Clip đang được dùng mấy lần trên timeline đang mở |
| **Synced Audio** | Tên file tiếng đã đồng bộ với clip hình |
| **Proxy**, **Proxy Media Path** | Clip đã có proxy chưa, proxy nằm đâu |

Muốn cột Usage đếm cho **mọi** timeline: menu ⋯ → **Update Usage for Entire Project**.

### Metadata view

`★☆☆ Tình huống cụ thể`

Hiện thumbnail kèm một khối metadata bên cạnh mỗi clip. Hợp khi soát lại ghi chú của cả bin.

Mỗi thẻ có bốn dòng: dòng chính (đổi theo kiểu sắp) · Start TC, Date Created, Camera # · Scene, Shot, Take · Clip Name, Comment.

Sức mạnh nằm ở **menu sắp xếp** góc trên phải — clip tự **gom nhóm**:

| Kiểu sắp | Gom theo |
|---|---|
| **Bin** | Bin chứa clip |
| **Timecode** | Ngày tạo, xếp theo timecode |
| **Camera** | Số máy quay |
| **Date Time** | Từng ngày quay |
| **Clip Name** | Chữ cái đầu tên clip |
| **Scene, Shot** | Cảnh, rồi cú máy, rồi take |
| **Clip Color** | Màu clip |
| **Date Modified** / **Date Imported** | Ngày sửa file / ngày nạp vào project |

**Ví dụ:** quay hai máy A và B. Chọn **Camera** là clip tự chia hai cụm, máy nào ra máy đó.

> Kiểu hiển thị **đặt riêng cho từng bin được**. Bin footage để Thumbnail, bin audio để List — Resolve nhớ cho từng bin.

Cách đặt: chọn kiểu hiển thị muốn dùng → chuột phải bin → **Always Open in … View**. Cài đặt này lưu trên máy bạn, không ảnh hưởng người khác mở cùng project.

---

## Hiện dạng sóng cho clip audio

`★★☆ Thường dùng`

Mặc định clip audio chỉ là ô trống, khó phân biệt. Menu ⋯ của Media Pool → **Show Audio Waveforms**. Mỗi clip audio hiện dạng sóng.

Bật thêm Live Media Preview là rê chuột trên dạng sóng **nghe được** luôn. Rất tiện khi chọn nhạc nền trong một bin 50 bài.

---

## Media Pool Tabs

`★★☆ Thường dùng`

Mở nhiều bin thành các tab cạnh nhau trong cùng một Media Pool, giống tab trình duyệt. Đỡ phải nhảy qua lại.

Tạo tab: chuột phải bin → **Open as New Tab**. Dùng được cho bin thường, Power Bin và Smart Bin. Tab hiện ở Media Pool của mọi trang.

Chuột phải vào tab:

| Lệnh | Làm gì |
|---|---|
| **New Tab** | Tab mới (`⌘T`) |
| **Previous / Next Tab** | Sang tab trước/sau |
| **Close Tab** | Đóng tab đang mở (`⌘W`) |
| **Close All Other Tabs** | Chỉ giữ tab đang mở |

Mũi tên ở **cuối dải tab** mở danh sách tab kèm ô tìm. Ô này chỉ tìm **tên tab**, không tìm clip.

**Ví dụ:** dựng vlog, mở ba tab **Footage**, **Nhạc**, **Đồ hoạ**. Cần gì bấm tab đó, khỏi lần cây bin.

---

## Mở bin ra cửa sổ riêng

`★☆☆ Tình huống cụ thể`

Chuột phải bin trong Bin List → **Open As New Window**.

Cửa sổ mới là một Media Pool đầy đủ, có Bin list, Power Bins, Smart Bins riêng. Mở bao nhiêu cửa sổ cũng được.

Rất hợp khi dùng hai màn hình: kéo cửa sổ bin sang màn phụ trong lúc Resolve vẫn ở chế độ một màn hình.

Cửa sổ bin bị khuất: **Workspace → Media Pool Windows** → chọn cửa sổ cần đưa lên.

---

## Tìm clip

`★★★ Hằng ngày`

Icon kính lúp ở góc trên Media Pool. Tìm theo tên, theo metadata, hoặc lọc riêng clip / timeline.

1. Bấm **kính lúp** để hiện ô tìm.
2. (Tuỳ chọn) Menu cạnh kính lúp: tìm ở **All Bins** (mọi bin) hay **Selected Bins** (chỉ bin đang chọn).
3. (Tuỳ chọn) Menu **Filter By**: **All Fields** để tìm mọi cột, hoặc chọn một trường cụ thể.
4. Gõ từ khoá. Clip không khớp tạm ẩn đi. Bấm nút huỷ cuối ô tìm để hiện lại hết.

Một số lệnh tìm hữu ích trong menu chuột phải:

| Lệnh | Làm gì |
|---|---|
| **Find in Media Pool** | Từ clip trên timeline, nhảy về đúng clip gốc trong pool |
| **Reveal in Finder** | Mở thư mục chứa file trên máy |
| **Reveal in Media Storage** | Nhảy tới đúng vị trí trong Media Storage |
| **Reveal Media Pool Bin** | Từ kết quả tìm, nhảy tới bin chứa clip |
| **Reveal synced audio in Media Pool** | Từ clip hình, tìm clip tiếng đã đồng bộ |

Tìm timeline đang mở nằm ở bin nào: **Timeline → Find Current Timeline in Media Pool**.

> **IntelliSearch** — tìm bằng AI theo vật thể, khuôn mặt, câu thoại — là `Studio`. Bản free tìm theo tên và metadata.

---

## Đổi tên clip mà không đổi tên file

`★★☆ Thường dùng`

File máy quay tên `C0042.MP4` rất khó nhớ. Đặt **Clip Name** dễ đọc hơn — file trên ổ vẫn giữ tên cũ.

| Cách | Làm thế nào |
|---|---|
| Thumbnail view | Bấm tên clip, chờ một nhịp, bấm lần nữa, gõ tên mới, `Return` |
| List view | Gõ vào cột **Clip Name** |
| Nhiều clip một lúc | Chọn các clip → chuột phải → **Clip Attributes** → tab **Name** |

Đổi qua lại giữa tên file và tên clip: **View → Show File Names**.

---

## Nhân bản clip và timeline

`★☆☆ Tình huống cụ thể`

**Nhân bản clip** — bản sao là một clip **hoàn toàn riêng**, có metadata và marker riêng.

- **Edit → Duplicate Clip**
- Chuột phải clip → **Duplicate Clip**
- Giữ `⌥` kéo clip sang bin khác

**Nhân bản timeline** — chọn timeline → **Edit → Duplicate Timeline**.

**Dùng khi:** trước khi sửa lớn một bản dựng, nhân bản timeline để giữ bản cũ. Đặt tên `Vlog - v1`, `Vlog - v2`.

---

## Tạo timeline thẳng từ clip

`★★☆ Thường dùng`

Không cần kéo từng clip xuống timeline.

1. (Tuỳ chọn) Đặt `I` `O` cho từng clip. Sắp clip theo đúng thứ tự muốn ghép.
2. Chọn các clip → chuột phải → **Create Timeline Using Selected Clips**.
   Hoặc chuột phải **bin** → **Create Timeline Using Bin** để lấy cả bin.
3. Đặt tên. Tick **Use Selected Mark In/Out** nếu muốn dùng điểm `I` `O` đã đặt.
4. Bấm **Create New Timeline**.

> **Ví dụ:** sắp bin theo **Date Created**, chọn hết, tạo timeline. Bạn có ngay bản nháp xếp đúng thứ tự quay để bắt đầu cắt.

---

## Menu chuột phải của clip

Chuột phải một clip (hoặc nhóm clip đã chọn) trong Media Pool. Những lệnh người mới hay cần:

| Lệnh | Làm gì | Mức |
|---|---|---|
| **Clip Attributes** | Sửa fps, tiếng, timecode, tên — xem [Clip Attributes](clip-attributes.md) | ★★☆ |
| **Create Timeline Using Selected Clips** | Ghép clip đã chọn thành timeline mới | ★★☆ |
| **Generate Optimized Media** | Tạo bản nhẹ để dựng mượt — xem [Proxy và Optimized](nap-media.md#proxy-và-optimized-media) | ★★☆ |
| **Generate Proxy Media** | Tạo proxy | ★★☆ |
| **Relink Selected Clips** | Nối lại clip bị offline | ★★☆ |
| **Change Source Folder** | Nối lại khi cả thư mục bị dời đi | ★☆☆ |
| **Set Poster Frame** | Đổi ảnh đại diện (`⌘P`) | ★☆☆ |
| **Duplicate Clip** | Nhân bản clip | ★☆☆ |
| **Create Bin With Selected Clips** | Gom clip đã chọn vào bin mới | ★★☆ |
| **Remove Selected Clips** | Bỏ clip khỏi project (không xoá file) | ★★☆ |
| **Reveal in Finder** | Mở thư mục chứa file | ★★☆ |
| **AI Tools** | Transcription, Audio Classification, Slate, phân tích người | `Studio` |

---

## Khôi phục timeline đã xoá

`★★☆ Thường dùng`

**Menu tuỳ chọn Media Pool** (ba chấm) → **Deleted Timeline Backups**.

Xem các timeline đã xoá và các bản backup của từng timeline, chọn bản để khôi phục hoặc xoá hẳn.

Đây là cứu cánh khi bạn lỡ xoá nhầm một timeline đã dựng xong.

---

## Xoá media khỏi project

`★★☆ Thường dùng`

| Việc | Cách |
|---|---|
| Xoá clip khỏi Media Pool | Chọn clip → `Delete` (không xoá file trên ổ) |
| Xoá clip qua menu | Chuột phải → **Remove Selected Clips** |
| Xoá mọi clip trong bin đang mở | Chuột phải vùng trống → **Remove All Clips in Bin** |
| Xoá mọi clip không dùng tới | Menu tuỳ chọn Media Pool → **Remove Unused Clips** |

**Remove Unused Clips** rất hữu ích trước khi giao project: nó bỏ hết footage bạn nạp vào nhưng cuối cùng không dùng.

Cách chạy: menu ⋯ → **Remove Unused Clips** → bấm **Load All Timelines**. Resolve mở mọi timeline, compound clip, Fusion comp để kiểm tra, rồi bỏ clip không ai dùng. Project lớn có thể mất vài phút. Undo được.

> **Không file nào trên ổ bị xoá.** Cả hai cách chỉ bỏ clip khỏi project.

---

## Xuất bin thành PDF

`★☆☆ Tình huống cụ thể`

Mở bin → menu ⋯ → **Export as PDF** → chọn chỗ lưu. Ra một tờ "contact sheet" gồm mọi thumbnail trong bin, theo cỡ thumbnail đang đặt.

**Dùng khi:** gửi khách hoặc đạo diễn xem có những cảnh nào, không cần mở Resolve.
