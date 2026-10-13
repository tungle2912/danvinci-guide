# Nạp media vào project

Resolve **không copy** file khi nạp. Clip trong Media Pool chỉ trỏ tới file gốc trên ổ. Vì vậy:

- Copy footage về **ổ nhanh** (SSD) trước khi nạp.
- Đặt file ở chỗ **cố định**. Dời hay đổi tên sau khi nạp là clip bị offline.

> **Trước khi nạp clip đầu tiên:** mở **File → Project Settings → Master Settings** và đặt **Timeline frame rate** đúng frame rate bạn sẽ xuất (25, 30…). Sau khi Media Pool có clip, ô này **không đổi được nữa**.

## Bốn cách cơ bản

`★★★ Hằng ngày`

| Cách | Thao tác | Khi nào dùng |
|---|---|---|
| **Kéo từ Media Storage** | Kéo file hoặc thư mục từ Media Storage xuống Media Pool | Thường dùng nhất |
| **Kéo từ Finder** | Kéo thẳng từ Finder vào Media Pool | Nhanh, vài file lẻ |
| **Import Media** | `⌘I`, hoặc chuột phải Media Pool → **Import Media**, hoặc **File → Import → Media** | Khi biết chính xác file cần |
| **Import Folder** | Chuột phải thư mục trong Media Storage → **Add Folder and SubFolders into Media Pool (Create Bins)**. Ở trang Cut: nút **Import Media Folder** | Giữ nguyên cấu trúc thư mục thành các bin |

**Import Folder** là cách tốt nhất khi thẻ nhớ đã có sẵn cấu trúc thư mục hợp lý — Resolve tạo bin tương ứng với từng thư mục.

**Muốn clip vào đúng bin nào:** bấm chọn bin đó trong Bin List **trước**, rồi mới nạp.

Chuột phải trong Media Storage cũng có các lệnh:

- **Add Into Media Pool** — nạp vào bin đang chọn
- **Add Folder Into Media Pool** — nạp file trong thư mục, bỏ qua thư mục con
- **Add Folder and SubFolders Into Media Pool** — nạp cả thư mục con, dồn hết vào một bin
- **Add Folder and SubFolders Into Media Pool (Create Bins)** — nạp cả cây thư mục, tự tạo bin

**Kéo thư mục thả vào đâu cũng có nghĩa:**

| Thả vào | Kết quả |
|---|---|
| **Vùng clip** của Media Pool | Mọi clip (kể cả thư mục con) dồn vào bin đang chọn |
| **Bin List** | Thư mục thành bin mới, thư mục con thành bin con |

> **Thẻ máy quay nhiều tầng thư mục** (Sony, Canon hay có `PRIVATE/M4ROOT/CLIP`…): dùng **Add Folder and SubFolders into Media Pool** để lấy hết clip vào một bin, khỏi lần từng tầng.

---

## Nạp một đoạn thay vì cả clip (subclip)

`★★☆ Thường dùng`

Không cần nạp cả file dài 40 phút nếu chỉ dùng 2 phút.

1. Chọn clip trong Media Storage — clip mở trong Viewer.
2. Đặt `I` và `O` trong Viewer quanh đoạn cần.
3. Chuột phải **thanh jog** dưới hình → **Make Subclip**. Hoặc kéo hình từ Viewer thả xuống Media Pool.
4. Hộp thoại **New Subclip** hiện ra: đặt tên. Tick ô dùng toàn bộ độ dài nếu muốn subclip vẫn mở rộng được ra cả clip.

Subclip vẫn trỏ về file gốc, không nhân bản dữ liệu.

Làm được cả với clip đã nằm trong Media Pool — rất tiện để chia một clip "quay liền nhiều take" thành từng take.

**Sửa subclip sau này:** chuột phải subclip → **Edit Subclip** → đổi timecode đầu/cuối hoặc tick dùng toàn bộ độ dài → **Update**.

---

## Nạp một khung từ chuỗi ảnh

`★☆☆ Tình huống cụ thể`

Resolve có thể gom chuỗi ảnh đánh số liên tiếp (image sequence) thành một clip video. Muốn lấy từng ảnh riêng lẻ:

1. Menu ⋯ của Media Storage → **Frame Display Mode** → **Individual**.
2. Chọn ảnh cần lấy, nạp như bình thường.

Chế độ **Auto** để Resolve tự quyết: DPX, EXR thành clip; JPG thành ảnh lẻ. **Sequence** thì gom hết thành clip.

---

## Nạp ảnh tĩnh

`★★☆ Thường dùng`

Kéo vào như clip bình thường. Độ dài mặc định khi đưa xuống timeline đặt ở **Preferences → User → Editing → Standard still duration** (mặc định 5 giây).

**Đồ hoạ động:** file **Lottie** (`.lottie`) và **OGraf** (`.json`) kéo vào Media Pool như clip thường. Nền trong suốt được giữ — đặt lên track trên là thấy hình bên dưới.

---

## Hộp thoại đổi frame rate

`★★★ Hằng ngày`

Khi bạn nạp clip vào một **project còn trống** và frame rate của clip **khác** frame rate project, Resolve hỏi có đổi project cho khớp không.

| Nút | Kết quả |
|---|---|
| **Change** | Project đổi theo frame rate (và thông số) của clip đang nạp |
| **Don't Change** | Project giữ frame rate cũ, clip vẫn được nạp |

> **Chọn cẩn thận.** Sau khi Media Pool đã có clip, frame rate project **không đổi được nữa**.

**Chọn thế nào:**

- Clip đầu tiên là footage chính (quay 25p hay 30p như phần lớn video): chọn **Change**.
- Clip đầu tiên là slow motion 50p/60p, hoặc một bài nhạc, ảnh: chọn **Don't Change**, rồi đặt frame rate bằng tay trong Project Settings.

Cách chắc ăn nhất: đặt **Timeline frame rate** trong **Project Settings → Master Settings** **trước** khi nạp gì cả.

---

## Media offline — khi clip hiện đỏ

`★★☆ Thường dùng`

Resolve **không nhúng media vào project**, chỉ lưu đường dẫn. Đổi tên file, chuyển thư mục hay rút ổ là clip thành offline.

Nối lại: chuột phải clip trong Media Pool → **Relink Selected Clips** → trỏ tới thư mục mới. Resolve tự nối lại các clip khác cùng thư mục.

Chủ động ngắt: **Unlink Selected Clips** — dùng khi muốn chuyển sang bản proxy hay bản online khác.

**Ba cách nối lại, chọn theo tình huống:**

| Cách | Ở đâu | Dùng khi |
|---|---|---|
| **Nút Relink Media** | Media Pool trang Cut và Edit — icon **sáng cam** khi có clip mất | Cách nhanh nhất. Hộp thoại cho biết clip mất vốn nằm ở **ổ nào**. Bấm **Locate** để chỉ chỗ mới; tìm không ra thì **Disk Search** để quét sâu |
| **Relink Selected Clips** | Chuột phải clip. Cả bin: chuột phải bin → **Relink Clips for Selected Bin** | File đã bị sắp xếp lại lung tung. Resolve dò theo **tên file và timecode** |
| **Change Source Folder** | Chuột phải clip | Cả thư mục chỉ bị **dời chỗ**, cấu trúc bên trong giữ nguyên. Bấm **Browse** cạnh ô **Change To** → chọn chỗ mới → **Change** |

**Relink Selected Clips chạy thế nào:**

1. Chọn thư mục để tìm → **OK**. Resolve tìm file trùng tên trong thư mục đó.
2. Còn clip chưa tìm thấy: hỏi có **tìm sâu** (deep search) mọi thư mục con không. Bấm **Yes** — lâu hơn nhưng chắc.
3. Vẫn còn thiếu: chọn thư mục khác để tìm tiếp, hoặc thoát.

> **Ví dụ:** bạn chép cả thư mục dự án từ ổ ngoài sang SSD mới. Mọi clip đỏ. Chọn hết clip → **Change Source Folder** → trỏ sang thư mục trên SSD. Xong trong vài giây.

---

## Tách tiếng ra khỏi file hình

`★☆☆ Tình huống cụ thể`

Chuột phải clip trong Media Storage → **Extract Audio**.

1. Bấm **Browse** để chọn chỗ lưu.
2. Bấm **Extract**. Resolve ghi ra một file `.wav`.
3. Nạp file `.wav` đó vào Media Pool nếu muốn dùng.

**Dùng khi:** chỉ cần tiếng của một video — ví dụ một bản ghi phỏng vấn dài.

---

## Đổi media gốc của một clip

`★☆☆ Tình huống cụ thể`

**Dùng khi:** bạn có bản file mới thay cho bản cũ — bản quay lại, bản đã sửa màu ở phần mềm khác, bản chất lượng cao hơn — mà không muốn dựng lại.

Cách đơn giản nhất: **đặt file mới cùng tên** với file cũ, vào một thư mục khác.

1. Chọn clip trong Media Pool → chuột phải → **Unlink Selected Clips**.
2. Chuột phải clip → **Relink Selected Clips** → trỏ tới thư mục chứa file mới.

Mọi chỗ clip đó xuất hiện trên timeline đều đổi theo, giữ nguyên điểm cắt.

Nếu bạn chỉ dời cả thư mục sang chỗ mới mà giữ nguyên cấu trúc bên trong, dùng **Change Source Folder** cho nhanh.

> File mới phải có **cùng độ dài và timecode** với file cũ, nếu không điểm cắt sẽ lệch.

---

## Đồng bộ tiếng thu rời với hình

`★☆☆ Tình huống cụ thể`

**Là gì:** ghép tiếng thu bằng máy ghi âm riêng (Zoom, Tascam, mic không dây ghi trong) vào clip hình, để khi kéo xuống timeline thì hình và tiếng tốt đi liền nhau.

### Tự động — Auto Sync Audio

1. Bỏ clip hình và clip tiếng cần ghép vào **cùng một bin** (hoặc `⌘` chọn hai bin).
2. Chuột phải bin → **Auto Sync Audio**.
3. Ở **Synchronize Using**, chọn cách so:

| Cách | Dùng khi |
|---|---|
| **Timecode** | Máy quay và máy ghi âm chạy chung timecode |
| **Waveform** | Không có timecode chung, nhưng máy quay **có thu tiếng** (mic trên máy). Phổ biến nhất với người làm vlog |
| **In / Out / Marker** | Không có cả hai. Phải tự đặt `I`, `O` hoặc marker ở cùng một khoảnh khắc (tiếng vỗ tay) trên clip hình và clip tiếng. Chỉ ghép **từng cặp** một |

4. Tuỳ chọn:
   - **Retain embedded audio** — giữ cả tiếng máy quay. Trên timeline clip có thêm một track tiếng.
   - **Retain Video Metadata** — giữ metadata của clip hình thay vì lấy của file tiếng.
   - Với Waveform: **Use channel number** chọn kênh để so. **Auto** để Resolve tự chọn.
5. Bấm **Sync**.

Clip đã ghép có **icon âm thanh** ở góc dưới trái thumbnail.

> **Chia nhỏ để nhanh:** quay nhiều ngày thì ghép từng ngày một. Resolve so ít file hơn, chạy nhanh hơn và ít ghép nhầm.

### Bằng tay — trong Audio Panel

1. Bấm nút **Waveform** trên đầu Audio Panel.
2. Chọn clip hình, tua tới khoảnh khắc vỗ tay hoặc đập clapper.
3. Chọn clip tiếng tương ứng — dạng sóng hiện trong Audio Panel. Tua tới đỉnh sóng của tiếng vỗ.
4. Bấm nút **Link/Unlink Audio** ở góc dưới phải Audio Panel để khoá lại.

Lệch vài khung sau khi ghép: chọn clip, mở Waveform, tắt nút link, chỉnh lại điểm khớp, bật link lại.

Tìm clip tiếng đã ghép: chuột phải clip hình → **Audio Sync → Reveal synced audio in Media Pool**.

---

## Cắt video đã dựng thành từng cảnh

`★☆☆ Tình huống cụ thể`

**Là gì:** Scene Cut Detection tìm các điểm cắt trong **một file video đã dựng sẵn** (không có EDL đi kèm), rồi chia thành từng clip.

**Dùng khi:** khách gửi một file video thành phẩm, nhờ bạn chỉnh màu lại từng cảnh.

1. Trong **Media Storage**, chuột phải file → **Scene Cut Detection**. Làm **trước** khi nạp file vào Media Pool.
2. Bấm **Auto Scene Detect** (góc dưới trái cửa sổ).
3. Điểm cắt hiện thành vạch xanh trên biểu đồ. Kéo **thanh ngang màu hồng** lên để bỏ vạch thấp (ít chắc chắn).
4. Soát từng điểm trong **Cut List**: ba khung hình phía trên — khung trái khác hẳn hai khung kia là cắt đúng. Sai thì **Delete**, thiếu thì **Add**.
5. Bấm **Add Cuts to Media Pool**.

> Bản tự cắt cảnh **ngay trên timeline** (**Timeline → Detect Scene Cuts**) là `Studio`.

---

## Proxy và Optimized Media

`★★☆ Thường dùng`

Hai thứ khác nhau, hay bị nhầm.

| | Optimized Media | Proxy Media |
|---|---|---|
| Ai quản lý | Resolve, cất trong thư mục cache | File `.mov` thật nằm trên ổ |
| Mang sang máy khác | Không | Được |
| Bật dùng | **Playback → Use Optimized Media If Available** | **Playback → Proxy Handling → Prefer Proxies** |
| Hợp khi | Làm một mình trên một máy | Làm nhóm, dựng trên laptop rồi chuyển máy |

**Dùng khi:** footage 4K, H.265, 10-bit hoặc RAW phát bị giật khi dựng. Máy mạnh, footage nhẹ thì không cần.

### Optimized Media
Bản nhẹ do Resolve tạo và **tự quản lý**. Không xuất ra ngoài, không mang sang máy khác được.

1. Chọn clip → chuột phải → **Generate Optimized Media**
2. Bật dùng: **Playback → Use Optimized Media If Available**

Chọn codec và độ phân giải ở **Project Settings → Master Settings → Optimized Media and Render Cache → Optimized media format / Optimized media resolution**.

| Cài đặt | Chọn gì |
|---|---|
| **Optimized media resolution** | **Choose automatically** — chỉ thu nhỏ clip lớn hơn timeline. Hoặc Original, Half, Quarter… |
| **Optimized media format** | ProRes 422 hoặc DNxHR cho dựng. Định chỉnh màu HDR trên optimized media thì cần ProRes 4444 hoặc 16-bit float để không bị cắt vùng sáng |

File optimized nằm cùng chỗ với cache — mặc định là ổ scratch đầu tiên trong **Preferences → System → Media Storage**.

Đổi thông số RAW của clip thì optimized media cũ **bị bỏ**, phải tạo lại.

### Proxy Media
File thật nằm trên ổ, **mang sang máy khác được**.

1. Chọn clip → chuột phải → **Generate Proxy Media**
2. Bật dùng: **Playback → Proxy Handling → Prefer Proxies**

Chọn độ phân giải và codec ở **Project Settings → Master Settings → Optimized Media and Render Cache → Proxy media resolution / Proxy media format**. Proxy được ghi vào **Proxy generation location** (mục **Working Folders** của Master Settings).

**Ba chế độ Proxy Handling** (menu **Playback**, hoặc nút trên Viewer trang Cut):

| Chế độ | Làm gì |
|---|---|
| **Disable All Proxies** | Chỉ dùng file gốc |
| **Prefer Proxies** | Dùng proxy nếu có, không có thì dùng file gốc |
| **Prefer Camera Originals** | Dùng file gốc nếu có, không có thì dùng proxy |

Đoạn nào trên timeline mất file gốc sẽ có **vạch tím**.

**Nhận biết clip đang dùng gì** — icon nhỏ ở góc dưới trái thumbnail:

| Icon | Nghĩa |
|---|---|
| **PXY** tím | Chỉ có proxy, mất file gốc |
| **PXY** tím trên nền trắng | Có cả hai, đang dùng proxy |
| **HQ** trắng trên nền tím | Có cả hai, đang dùng file gốc |
| Không icon | Không dùng proxy |

**Proxy làm ở chỗ khác** (hoặc bạn đã dời proxy đi): chọn clip → chuột phải → **Link Proxy Media** → chỉ tới file/thư mục proxy. Bỏ liên kết: **Unlink Proxy Media** — file proxy vẫn nằm trên ổ, phải xoá tay.

> **Khi xuất ở trang Deliver,** Resolve tự quay về file gốc để có chất lượng cao nhất. Không cần tắt proxy trước khi xuất.

Chi tiết cách chọn codec: [Tối ưu hiệu năng](../../04-tham-khao/hieu-nang.md).

---

## Chép lời thoại

`Studio`

Chuột phải clip → **AI Tools → Audio Transcription → Transcribe**, hoặc nút **Transcribe Audio** trên Media Pool. Clip đã chép lời có icon bong bóng thoại ở góc thumbnail.

Bản free không có. Muốn phụ đề ở bản free: gõ tay theo [Phụ đề](../edit/phu-de.md).
