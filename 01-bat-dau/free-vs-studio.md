# Free và Studio khác gì nhau

Bản free của Resolve rộng rãi một cách bất thường — gần như toàn bộ công cụ chỉnh màu, dựng và âm thanh đều có. Studio là mua đứt một lần (khoảng 299 USD), không thuê bao.

Tài liệu này viết cho **bản free**. Dưới đây là những gì bạn *không* có, để khỏi mất công đi tìm.

Trong manual, công cụ nào chỉ có ở Studio đều có câu ghi chú kiểu *"…is only available in DaVinci Resolve Studio"* ngay đầu mục. Số trang `tr.` dưới đây là trang PDF của manual 21 nơi có câu đó. Trong tài liệu này, nhãn `Studio` đánh dấu những công cụ như vậy.

> **Mẹo:** Không chắc một công cụ có ở bản free không? Tra tên nó trong manual và tìm chữ *Studio* ở đầu mục, hoặc thử thêm nó vào clip. Với nhiều hiệu ứng `Studio`, bản free vẫn cho thêm nhưng sẽ hiện watermark trên Viewer hoặc báo cần nâng cấp. Manual không mô tả hành vi này, nên hãy coi đó là dấu hiệu, không phải quy tắc.

## Giới hạn xuất file

`★★★ Hằng ngày`

| | Free | Studio |
|---|---|---|
| Độ phân giải xuất tối đa | 4K UHD (3840×2160) | tới 32K |
| Frame rate xuất tối đa | 60 fps | 120 fps |
| Độ sâu màu | 8-bit | 10-bit |
| Tăng tốc phần cứng khi encode | Hạn chế | Đầy đủ H.264/H.265 |
| Số GPU dùng được | 1 | Nhiều |

> **Lưu ý:** Manual **không có** bảng này. Các con số lấy từ trang so sánh của Blackmagic và các bài tổng hợp ở cuối trang, nên có thể đổi theo phiên bản. Nhất là dòng 10-bit và tăng tốc phần cứng: nên tự thử xuất ở Deliver trước khi tin.

Bản free vẫn **nạp, dựng và chỉnh màu** được footage lớn hơn 4K bình thường. Chỉ là không xuất ra lớn hơn 4K.

Ở trang Deliver, preset **IMF** (tr.4191) và **Remote Rendering** (tr.4215, render trên máy khác trong mạng) cũng là `Studio`. Xem [Deliver → Giới hạn bản free](../02-trang/deliver/README.md#giới-hạn-bản-free).

## Tính năng AI thuộc Studio

`Studio`

Đây là nhóm bị khoá nhiều nhất. Những thứ dưới đây **không có** ở bản free. Một số công cụ tự động vẫn free: nút **Auto Color** (tr.791), **Dialogue Leveler**.

**Dựng và phụ đề (trang Cut, Edit)**

| Công cụ | Làm gì | Tr. |
|---|---|---|
| **Smart Reframe** | Tự cắt khung sang tỉ lệ khác, bám chủ thể | 756 |
| **Scene Cut Detection** | Tự cắt clip tại các điểm chuyển cảnh | 709 |
| **IntelliSearch** | Tìm clip trong Media Pool theo nội dung hình | 409 |
| **Text-Based Editing** | Dựng bằng cách sửa transcript | 734, 1018 |
| **Detect Speakers** | Nhận ra ai đang nói trong transcript | 1024 |
| **Create Subtitles from Audio** | Tự tạo phụ đề từ lời nói. Bản free gõ tay hoặc nhập `.srt`, xem [Phụ đề](../02-trang/edit/phu-de.md#create-subtitles-from-audio--ai-tự-tạo) | 723 |
| **AI Animated Subtitles** | Chữ phụ đề sáng lên theo từng từ | 1281 |
| **Multicam SmartSwitch** | Tự chọn góc máy theo người đang nói | 1070 |

**Hình (trang Color và Inspector)**

| Công cụ | Làm gì | Tr. |
|---|---|---|
| **Magic Mask** | Tách người, vật bằng AI | 3339 |
| **IntelliTrack** | Tracker AI | 3375 |
| **Face Refinement** | Làm mịn da, chỉnh khuôn mặt | 3686 |
| **Object Removal** | Xoá vật thể | 3719 |
| **Depth Map** | Tạo bản đồ chiều sâu | 3680 |
| **Relight** | Thêm nguồn sáng ảo | 3696 |
| **Super Scale** | Phóng to bằng AI | 297 |
| **Motion DeBlur** | Giảm nhoè do chuyển động | 471 |

**Âm thanh (trang Fairlight và Edit)**

| Công cụ | Làm gì | Tr. |
|---|---|---|
| **Voice Isolation** | Tách giọng khỏi tiếng ồn | 794, 3837 |
| **Audio Assistant** | Tự mix tiếng | 802, 4045 |
| **Dialogue Separator** | Tách giọng, nền, tiếng vang | 4093 |
| **Music Remixer** | Tách nhạc thành từng phần (giọng, trống, bass…) | 796 |
| **Music Editor** | Tự kéo dài hoặc rút ngắn bản nhạc cho vừa đoạn video | 797 |
| **Beat Detector** | Đánh dấu nhịp nhạc | 801 |
| **Dialogue Matcher** | Khớp âm sắc giọng giữa các clip | 801 |
| **Voice Convert** | Đổi giọng người nói | 803 |
| **Speech Generator** | Tạo giọng đọc từ văn bản | 807 |
| **Remove Silence** | Tự cắt khoảng lặng | 3945 |
| **AI Checkerboard**, **AI Create ADR Cues** | Tách thoại chồng nhau ra hai track, tự tạo danh sách thu lại thoại | 3946, 3919 |

> **Lưu ý:** **Speed Warp** (slow motion chất lượng cao bằng DaVinci Neural Engine, tr.149, 444) thường được liệt vào nhóm `Studio`, nhưng manual 21 **không ghi** điều đó ở mục Retime Process. Bản free chắc chắn có **Optical Flow** loại Standard và Enhanced. Muốn biết Speed Warp có dùng được không, mở **Retime Process** của một clip và xem có lựa chọn này không, hoặc có watermark khi chọn không.

## Chống nhiễu

`★★☆ Thường dùng`

- **Hình:** palette **Motion Effects** ở trang Color (Noise Reduction, Motion Blur) là `Studio` (tr.3583). ResolveFX **Noise Reduction** cũng thế (tr.3715). Ở bản free, xử lý nhiễu hình từ khâu quay: đủ sáng, hạ ISO.
- **Tiếng:** **Noise Reduction** trong FairlightFX **dùng được ở bản free**. Chỉ **Voice Isolation** (tách giọng bằng AI) là `Studio`.

> **Lỗi hay gặp:** Chỉnh palette Motion Effects ở bản free rồi thấy watermark trên Viewer, hoặc chỉnh mà không thấy tác dụng. Đó không phải lỗi, mà là dấu hiệu công cụ này thuộc `Studio`. Reset palette (hoặc tắt node) để trả hình về như cũ.

## Trang Color — dùng gì thay công cụ AI

`★★☆ Thường dùng`

| Công cụ `Studio` | Bản free dùng thay |
|---|---|
| **Magic Mask**, tách người hoặc vật | **Qualifier** + **Window** |
| **IntelliTrack**, tracker AI | **Tracker** thường |
| **Motion Effects** (khử nhiễu) | Quay đủ sáng, hạ ISO |
| ResolveFX **Sharpen** | Palette **Blur**, chế độ **Sharpen** (tr.3591–3592) |

## Âm thanh — bản free có gì đáng chú ý

`★★★ Hằng ngày`

Ba công cụ "tự mix" hữu ích nhất đều **có ở bản free**: **Normalize Audio Levels**, **Dialogue Leveler**, **Ducker**. Xem [Track FX — ba công cụ "tự mix"](../02-trang/fairlight/mixer-va-track-fx.md#track-fx--ba-công-cụ-tự-mix).

Bộ **Fairlight FX** làm sạch giọng (Noise Reduction, EQ, De-Esser, De-Hummer, Dialogue Processor, Limiter) cũng có ở bản free — xem [Làm sạch giọng](../02-trang/fairlight/lam-sach-giong.md). Loudness meter chuẩn YouTube và **Normalize Audio** lúc xuất đều dùng được.

## Fusion — node nào bị khoá

`★☆☆ Tình huống cụ thể`

Đã thử trên Resolve 21.0.4 **bản free** (thêm node bằng script):

| Node | Bản free |
|---|---|
| **Tracker** | Có |
| **Delta Keyer** | Có |
| **Planar Tracker** | Không — `Studio` |
| **Planar Transform** | Không — `Studio` |
| **Camera Tracker** | Không — `Studio` |
| **Surface Tracker** | Không — `Studio` |

**Magic Mask** trong Fusion cũng là `Studio` — bản free dùng mask Polygon kèm keyframe. Manual còn ghi `Studio` cho **Cryptomatte** (tr.2563) và các node **VR180** (tr.2999).

Thay biển hiệu, màn hình điện thoại ở bản free: dùng **Tracker** chế độ Corner Position. Xem [Planar Tracker](../02-trang/fusion/mask-tracker-keyer.md#planar-tracker--bám-mặt-phẳng) và [Tracker](../02-trang/fusion/mask-tracker-keyer.md#tracker--bám-một-điểm).

Text+, Merge, Transform, mask, keyframe, Spline — mọi thứ dùng để [làm chữ động](../02-trang/fusion/chu-dong.md) — đều có ở bản free.

## Sửa hình

`★★☆ Thường dùng`

- **Lens Correction** — sửa méo ống kính góc rộng, là `Studio` (tr.443, 760, 947). Bản free không có, kể cả ở trang Cut và Edit. Thay thế: tăng nhẹ Zoom để cắt bớt mép cong — xem [Cut → Lens Correction](../02-trang/cut/tools.md#lens-correction--sửa-méo-góc-rộng).

## Hiệu ứng

`★★☆ Thường dùng`

Studio có thêm vài chục ResolveFX. Vài cái hay được tìm, kèm trang manual ghi `Studio`:

| ResolveFX `Studio` | Tr. | Bản free dùng thay |
|---|---|---|
| **Film Grain** | 3629 | Phủ một clip grain có sẵn lên track trên, chế độ Overlay |
| **Lens Blur** | 3606 | Palette **Blur** ở trang Color |
| **Lens Flare** | 3661 | Text+ hoặc ảnh flare có sẵn trong Fusion |
| **Motion Blur** | 3751 | Quay với shutter 1/50 cho video 25 fps |
| **Sharpen** | 3724 | Palette **Blur**, chế độ **Sharpen** (tr.3591–3592) |

Bản free vẫn có đủ các hiệu ứng cơ bản: blur, glow, các transition. Manual không ghi `Studio` cho **Glow**.

> **Mẹo:** Palette **Blur** ở trang Color có ba chế độ **Blur**, **Sharpen** và **Mist** (tr.3591). Kéo Radius xuống dưới 0.50 là làm nét, lên trên là làm mờ. Đây là cách làm nét chuẩn của bản free.

## Màu

`★★☆ Thường dùng`

Bản free có **gần như toàn bộ** công cụ chỉnh màu: node, curves, qualifier, power window, tracker, color warper, LUT, palette **HDR** (manual giới thiệu nó là công cụ chỉnh màu chính cho cả SDR lẫn HDR, tr.3214). Studio thêm:

- **Làm phim HDR** — mọi tính năng HDR trong chương *HDR Grading* đều là `Studio` (tr.261), kể cả tuỳ chọn gắn HDR metadata khi xuất (tr.147). Palette HDR thì vẫn dùng được cho video SDR thường.
- **Dolby Vision** — manual ghi grading và finishing Dolby Vision có ở cả hai bản (tr.154). Riêng ô **Enable Dolby Vision** để xem trước trên màn ngoài là `Studio` (tr.270). Với vlog SDR, bạn không cần cái này.
- **DCTL** (transform màu tự viết) — `Studio` (tr.3617).
- **Remote Monitor** — xem màu từ xa qua mạng, `Studio` (tr.4345). **Remote Grading**, tức điều khiển grading giữa hai máy, nằm cùng chương 198 (tr.4343), nhưng manual không ghi rõ nó là `Studio` hay không.

## Việc gì thì nên mua Studio

`★☆☆ Tình huống cụ thể`

Mua nếu bạn:
- xuất 4K liên tục và muốn encode nhanh bằng phần cứng;
- làm nội dung dọc từ footage ngang, vì **Smart Reframe** tiết kiệm rất nhiều thời gian;
- quay ở môi trường thiếu sáng nên cần **Noise Reduction**;
- thu tiếng ở nơi ồn, cần **Voice Isolation**;
- làm phụ đề thường xuyên, cần **Create Subtitles from Audio**.

Không cần mua nếu bạn làm vlog, video ngắn hoặc phim ngắn ở 1080p hay 4K 30fps, và quay ở nơi đủ sáng.

**Ví dụ:** Bạn làm vlog 1080p 25 fps, quay ngoài trời và thu micro cài áo. Mọi khâu đều làm được ở bản free: Dialogue Leveler cân tiếng, làm nét bằng palette Blur, xuất H.264. Nếu chuyển sang quay trong quán cà phê tối và ồn, Noise Reduction (hình) và Voice Isolation (tiếng) là hai lý do chính đáng để mua.

---

**Nguồn:** danh sách AI, hiệu ứng và màu ở trên đối chiếu với manual *DaVinci Resolve 21 Reference Manual*, kèm số trang. Bảng giới hạn xuất file thì không có trong manual. Bảng đó lấy từ trang so sánh chính thức trên [trang Blackmagic Design](https://www.blackmagicdesign.com/products/davinciresolve), là nơi tra chuẩn nhất cho phiên bản hiện tại, và đối chiếu thêm với [Toolfarm](https://www.toolfarm.com/tutorial/in-depth-davinci-resolve-studio-vs-the-free-version/) và [CineD](https://www.cined.com/davinci-resolve-an-in-depth-comparison-between-the-free-and-studio-version/).
