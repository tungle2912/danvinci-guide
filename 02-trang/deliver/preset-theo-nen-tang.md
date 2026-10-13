# Preset theo nền tảng — công thức xuất có sẵn

Mỗi mục dưới đây là một **công thức**: chọn preset nào, đổi ô nào, để yên ô nào. Tên preset ghi đúng như trong menu **Preset** của Resolve 21.

| Bạn cần | Công thức |
|---|---|
| Đăng YouTube | [YouTube](#youtube) |
| Đăng TikTok, Reels, Shorts | [Video dọc](#tiktok-reels-shorts--video-dọc) |
| Gửi khách xem nhanh | [Bản duyệt nhẹ](#gửi-khách-duyệt--bản-nhẹ) |
| Lưu bản gốc chất lượng cao | [Master lưu trữ](#master-lưu-trữ--prores-hoặc-dnxhr) |
| Chỉ cần tiếng | [Chỉ xuất tiếng](#chỉ-xuất-tiếng) |
| Một khung hình hoặc chuỗi ảnh | [Ảnh tĩnh, chuỗi ảnh](#ảnh-tĩnh-và-chuỗi-ảnh) |
| Dùng lại thiết lập của mình | [Tự tạo preset](#tự-tạo-preset) |

---

## YouTube

`★★★ Hằng ngày`

**Là gì:** preset **YouTube** chọn sẵn MP4 + H.264, profile High, tiếng AAC, xuất một file theo frame rate timeline.

**Dùng khi:** đăng YouTube, Facebook, hay bất kỳ nơi nào nhận MP4.

**Cách làm:**
1. Ô **Preset** → **YouTube**, chọn độ phân giải ở menu con: **720p**, **1080p**, **1440p** hoặc **2160p**. Chọn khớp với timeline.
2. Gõ **File Name**, chọn **Location**.
3. Tick **Normalize Audio** nếu chưa tự chỉnh độ to lúc mix. Standard để **YouTube**.
4. **Add to Render Queue** → **Render All**.

**Tuỳ chọn trong preset:**

| Ô | Làm gì | Mức |
|---|---|---|
| **Normalize Audio** | Đưa độ to về chuẩn YouTube (-14 LKFS) | ★★☆ |
| **Use Proxy Media** | Render từ proxy cho nhanh — **chất lượng kém hơn**. Bản đăng thật thì để tắt | ★☆☆ |
| **Render without timecode** | Bỏ timecode trong file — cho vài app dựng trên điện thoại bị lỗi với timecode | ★☆☆ |
| **Upload directly to YouTube** | Render xong tự tải lên kênh | ★☆☆ |

### Tải thẳng lên YouTube

Cần đăng nhập trước ở **Preferences → System → Internet Accounts**.

Tick **Upload directly to YouTube** thì hiện thêm: **Title**, **Description**, **Visibility** (ai được xem), **Category**, **Upload Thumbnail** (chọn ảnh bìa), **Chapters from Markers** (biến marker thành chương). Có nhiều kênh thì chọn kênh cần đăng.

Việc tải lên chạy ngầm — vẫn làm việc khác trong Resolve được. Xem tiến độ: **Workspace → Background Activity**.

> **Muốn xem lại trước khi đăng:** menu ba chấm của Render Queue → **Review Before Upload**. Render xong job dừng ở trạng thái *Waiting for Upload*. Chuột phải job → **Reveal in Finder** để xem file, rồi chuột phải lần nữa chọn **Upload to YouTube** hoặc **Cancel Upload**.

**Cần bitrate cụ thể?** Preset YouTube không có ô bitrate. Chọn **Custom Export**, đặt MP4 + H.264 và **Restrict to** theo [bảng bitrate](cai-dat-xuat.md#quality--chọn-bitrate).

---

## TikTok, Reels, Shorts — video dọc

`★★★ Hằng ngày`

**Là gì:** preset **TikTok** chọn sẵn MP4 + H.264, tiếng AAC, độ phân giải **720p** hoặc **1080p**.

**Dùng khi:** đăng TikTok, Instagram Reels, YouTube Shorts — mọi nền tảng video dọc 9:16.

**Điều kiện:** timeline phải là timeline **dọc** sẵn (1080×1920). Có bản ngang thì làm bản dọc trước theo [Luồng: video dọc](../../03-luong/video-doc.md).

**Cách làm:**
1. Ở đầu Viewer, chọn đúng **timeline dọc**.
2. Ô **Preset** → **TikTok** → **1080p**.
3. Tick **Use vertical resolution** — 1920×1080 đổi thành **1080×1920**. Preset mặc định **không** tick, nên đây là bước hay quên nhất.
4. Đặt **File Name** có chữ `doc` để khỏi lẫn với bản ngang.
5. **Add to Render Queue**.

**Có phụ đề:** preset TikTok không có mục phụ đề. Chọn **Custom Export** để bật **Subtitle Settings → Burn into video** — xem [Subtitle Settings](cai-dat-xuat.md#subtitle-settings). TikTok và Reels không đọc file phụ đề rời.

**Tải thẳng lên TikTok:** tick **Upload directly to TikTok**, điền **Title**, chọn **Visible To** (Private, Public, Friends), và tuỳ chọn **Allow comments**, **Allow Duet**, **Allow Stitch**.

> **Kiểm tra trước khi render:** nhìn Viewer — hình phải đứng dọc, không có viền đen hai bên. Có viền đen là timeline vẫn đang ngang.

---

## Gửi khách duyệt — bản nhẹ

`★★☆ Thường dùng`

**Là gì:** bản nhỏ, nhẹ để gửi qua Zalo, email, Drive cho khách xem và góp ý. Không dùng để đăng.

**Cách làm:**
1. Ô **Preset** → **Custom Export**.
2. Tab Video: **Format** MP4, **Codec** H.264.
3. **Resolution** 1280×720 hoặc 1920×1080.
4. **Quality** → **Restrict to** 5.000 Kb/s.
5. (Tuỳ chọn) Advanced Settings → **Data burn-in** để có **timecode đè lên hình** — khách ghi chú "sửa ở 00:01:12" là bạn tìm được ngay. Bật timecode ở **Workspace → Data Burn-In** trước.
6. Tab Audio: AAC, 128–192 Kb/s là đủ.
7. Đặt tên có `_duyet_v1`.

**Ví dụ:** video 5 phút 1080p, bản đăng YouTube khoảng 560 MB. Bản duyệt 720p ở 5.000 Kb/s còn khoảng 190 MB — gửi Zalo thoải mái.

> **Nhớ tắt Data burn-in** khi xuất bản cuối. Hoặc tốt hơn: lưu bản duyệt thành preset riêng để không đụng vào thiết lập bản cuối — xem [Tự tạo preset](#tự-tạo-preset).

---

## Master lưu trữ — ProRes hoặc DNxHR

`★★☆ Thường dùng`

**Là gì:** bản chất lượng cao gần như không mất gì. Dùng làm **bản gốc** để lưu, hoặc gửi cho người khác làm tiếp (chỉnh màu, làm tiếng, làm phụ đề).

**Dùng khi:** xong dự án quan trọng, muốn có một file để sau này xuất lại bản khác mà không cần mở project.

### Cách 1 — preset ProRes 422 HQ

Ô **Preset** → **ProRes 422 HQ** (manual gọi là *ProRes Master*). Resolve đặt sẵn:

| Ô | Giá trị |
|---|---|
| Render | Single clip |
| Format | QuickTime |
| Codec | Apple ProRes |
| Type | Apple ProRes 422 HQ |
| Audio Codec | Linear PCM, 16-bit |

### Cách 2 — DNxHR

Chọn **Custom Export** → **Format** QuickTime hoặc MXF OP1A → **Codec** DNxHR, chọn loại ở **Type**. Hợp khi người nhận dùng Windows hoặc Avid.

| Lưu ý | |
|---|---|
| **Dung lượng** | Rất lớn — video 5 phút 1080p ProRes 422 HQ đã vài GB. Kiểm tra ô **Disk space** ở tab File |
| **Mở trên máy khác** | ProRes mở tốt trên Mac. DNxHR hợp Windows hơn |
| **Advanced Settings** | Tắt **Use optimized media**, **Use proxy media**, **Use render cached images** để chắc chắn render từ gốc |

---

## Chỉ xuất tiếng

`★★☆ Thường dùng`

**Dùng khi:** gửi bản mix cho người làm podcast, xuất nhạc nền đã dựng, gửi tiếng cho người khác làm hậu kỳ âm thanh.

### Cách 1 — preset Audio Only

Ô **Preset** → **Audio Only**. Mặc định Resolve xuất bus **Main 1** dạng **MXF OP-Atom**, **Linear PCM 16-bit** — định dạng dành cho dân hậu kỳ. Đổi cho dễ dùng hơn:

| Ô | Đổi thành |
|---|---|
| **Format** | **WAVE** (cũng có QuickTime, MP4) |
| **Bit Depth** | 24 nếu gửi người làm tiếng |
| **Output Track** | Bus chính, hoặc chọn một submix, một track cụ thể |

### Cách 2 — Custom Export bỏ hình

Chọn **Custom Export**, bỏ tick **Export Video**. Tab Audio hiện thêm menu **Format** — chọn **WAVE**, **MP3** hoặc **FLAC**.

**Ví dụ:** podcast quay video, muốn đăng thêm bản nghe trên Spotify. Bỏ tick Export Video, Format MP3, xuất một file tiếng từ chính timeline đã dựng.

> **Gửi sang Pro Tools** thì dùng preset **Pro Tools** riêng — nó xuất kèm file AAF và video tham chiếu. Lưu ý: hiệu ứng tiếng (FairlightFX, EQ, Compressor…) **không** được xuất theo.

---

## Ảnh tĩnh và chuỗi ảnh

`★☆☆ Tình huống cụ thể`

### Một khung hình — không cần sang Deliver

Ở trang Media, Cut hoặc Edit: đặt con trỏ đúng khung → **File → Export → Current Frame as Still** → gõ tên, chọn định dạng → **Export**.

Nhanh nhất để lấy ảnh bìa video.

### Một khung hình chất lượng cao từ Deliver

1. **Custom Export** → **Format** **TIFF**, **PNG** hoặc **JPEG**.
2. Trên timeline, đặt `I` và `O` **cùng một khung**.
3. **Add to Render Queue** → render.

Cách này lấy ảnh qua đầy đủ bộ xử lý xuất, hợp khi cần ảnh để in. Xem thêm [Luồng chỉnh ảnh](../../03-luong/chinh-anh.md).

### Chuỗi ảnh — mỗi khung một file

**Dùng khi:** gửi cảnh cho người làm VFX, làm hoạt hình từng khung.

1. **Custom Export** → **Format** **DPX**, **EXR**, **TIFF** hoặc **PNG**.
2. Đặt `I` `O` quanh đoạn cần xuất.
3. Tab File → **Use filename digits** — số chữ số đánh số khung. Mặc định 8.
4. Nên chọn thư mục trống riêng cho mỗi lần xuất, vì một đoạn 10 giây là hàng trăm file.

| Định dạng | Hợp với |
|---|---|
| **PNG** | Cần nền trong suốt, nhẹ |
| **TIFF** | In ấn, đưa sang Photoshop |
| **DPX** | Phim điện ảnh, trao đổi với hãng hậu kỳ |
| **EXR** | VFX, HDR |

### Ảnh động

**Format** **GIF** (tối đa 256 màu) hoặc **WebP**. Dùng cho ảnh động trên web, meme.

### Ảnh từ trang Photo

Album ảnh của trang Photo xuất ở giao diện riêng — xem [Photo → Xuất ảnh](../photo/xuat-anh.md).

---

## Tự tạo preset

`★★☆ Thường dùng`

**Là gì:** lưu một bộ thông số bạn hay dùng thành preset, chọn một lần là xong.

**Cách làm:**
1. Ô **Preset** → **Custom Export** để mở khoá mọi ô.
2. Chỉnh tab Video, Audio, File theo ý.
3. **Menu ba chấm** của Render Settings → **Save as New Preset**.
4. Đặt tên, chọn **icon** đại diện.
5. Tick **Add to quick export** nếu muốn preset hiện trong Quick Export ở mọi trang.
6. **Save**.

> Chỉ thiết lập **Single clip** mới lưu được thành preset cho Quick Export, **Individual clips** thì không.

**Quản lý preset** — cùng ở menu ba chấm, chọn tên preset rồi:

| Mục | Làm gì |
|---|---|
| **Update Preset** | Ghi thiết lập hiện tại đè lên preset. **Không hoàn tác được** |
| **Delete Preset** | Xoá preset. **Không hoàn tác được** |
| **Export Preset** | Lưu ra file `.xml` — gửi cho đồng nghiệp hoặc mang sang máy khác |
| **Import Preset** | Nạp file `.xml` preset |

### Dùng preset mà không cần mở Deliver

Preset tự tạo xuất hiện ở hai chỗ khác:

- **Quick Export** (**File → Quick Export**) ở mọi trang — nếu đã tick Add to quick export. Xem [Quick Export](render-queue-va-loi.md#quick-export).
- **Chuột phải một timeline trong Media Pool → Add to Render Queue Using** → chọn preset. Timeline vào thẳng Render Queue, bấm **Render All** ở Deliver khi sẵn sàng.

**Ba preset nên tạo sẵn:**

| Tên | Thông số chính |
|---|---|
| *YouTube 1080p 15M* | MP4, H.264, 1920×1080, Restrict to 15.000 Kb/s, AAC 320 |
| *TikTok doc* | MP4, H.264, 1080×1920, Restrict to 15.000 Kb/s, phụ đề Burn into video |
| *Ban duyet nhe* | MP4, H.264, 1280×720, Restrict to 5.000 Kb/s, Data burn-in timecode |
