# Free và Studio khác gì nhau

Bản free của Resolve rộng rãi một cách bất thường — gần như toàn bộ công cụ chỉnh màu, dựng và âm thanh đều có. Studio là mua đứt một lần (khoảng 299 USD), không thuê bao.

Tài liệu này viết cho **bản free**. Dưới đây là những gì bạn *không* có, để khỏi mất công đi tìm.

## Giới hạn xuất file

| | Free | Studio |
|---|---|---|
| Độ phân giải xuất tối đa | 4K UHD (3840×2160) | tới 32K |
| Frame rate xuất tối đa | 60 fps | 120 fps |
| Độ sâu màu | 8-bit | 10-bit |
| Tăng tốc phần cứng khi encode | Hạn chế | Đầy đủ H.264/H.265 |
| Số GPU dùng được | 1 | Nhiều |

Bản free vẫn **nạp, dựng và chỉnh màu** được footage lớn hơn 4K bình thường. Chỉ là không xuất ra lớn hơn 4K.

Ở trang Deliver, preset **IMF** và **Remote Rendering** (render trên máy khác trong mạng) cũng là `Studio`. Xem [Deliver → Giới hạn bản free](../02-trang/deliver/README.md#giới-hạn-bản-free).

## Tính năng AI thuộc Studio

Đây là nhóm bị khoá nhiều nhất. Những thứ dưới đây **không có** ở bản free. (Một số công cụ AI vẫn free: nút **Auto Color**, **Dialogue Leveler**.)

- **Magic Mask** — tách người/vật bằng AI
- **Smart Reframe** — tự cắt khung sang tỉ lệ khác, bám chủ thể
- **Voice Isolation** — tách giọng khỏi tiếng ồn
- **Face Refinement** — làm mịn da, chỉnh khuôn mặt
- **Object Removal** — xoá vật thể
- **Depth Map** — tạo bản đồ chiều sâu
- **Super Scale** — phóng to bằng AI
- **Scene Cut Detection** — tự cắt clip tại các điểm chuyển cảnh
- **Text-Based Editing** — dựng bằng cách sửa transcript
- **Create Subtitles from Audio** — tự tạo phụ đề từ lời nói. Bản free gõ tay hoặc nhập file `.srt` — xem [Phụ đề](../02-trang/edit/phu-de.md#create-subtitles-from-audio--ai-tự-tạo)
- **AI Animated Subtitles** — chữ phụ đề sáng lên theo từng từ
- **Multicam SmartSwitch** — tự chọn góc máy theo người đang nói
- **Audio Assistant** — tự mix tiếng
- **Dialogue Separator**, **Music Remixer**, **Remove Silence** — tách giọng/nền/vang, tách nhạc thành từng phần, tự cắt khoảng lặng
- **Voice Convert** — đổi giọng người nói
- **Speed Warp** — slow motion chất lượng cao bằng AI (Optical Flow thường vẫn dùng được ở bản free)

## Chống nhiễu

- **Hình:** palette **Motion Effects** ở trang Color (Noise Reduction, Motion Blur) là `Studio`. Ở bản free, xử lý nhiễu hình từ khâu quay: đủ sáng, hạ ISO.
- **Tiếng:** **Noise Reduction** trong FairlightFX **dùng được ở bản free**. Chỉ **Voice Isolation** (tách giọng bằng AI) là `Studio`.

## Trang Color — dùng gì thay công cụ AI

- **Magic Mask** — tách người, vật bằng AI → bản free dùng Qualifier + Window
- **IntelliTrack** — tracker AI → bản free dùng Tracker thường

## Âm thanh — bản free có gì đáng chú ý

Ba công cụ "tự mix" hữu ích nhất đều **có ở bản free**: **Normalize Audio Levels**, **Dialogue Leveler**, **Ducker**. Xem [Track FX — ba công cụ "tự mix"](../02-trang/fairlight/mixer-va-track-fx.md#track-fx--ba-công-cụ-tự-mix).

Bộ **Fairlight FX** làm sạch giọng (Noise Reduction, EQ, De-Esser, De-Hummer, Dialogue Processor, Limiter) cũng có ở bản free — xem [Làm sạch giọng](../02-trang/fairlight/lam-sach-giong.md). Loudness meter chuẩn YouTube và **Normalize Audio** lúc xuất đều dùng được.

## Fusion — node nào bị khoá

Đã thử trên Resolve 21.0.4 **bản free** (thêm node bằng script):

| Node | Bản free |
|---|---|
| **Tracker** | Có |
| **Delta Keyer** | Có |
| **Planar Tracker** | Không — `Studio` |
| **Planar Transform** | Không — `Studio` |
| **Camera Tracker** | Không — `Studio` |
| **Surface Tracker** | Không — `Studio` |

**Magic Mask** trong Fusion cũng là `Studio` — bản free dùng mask Polygon kèm keyframe.

Thay biển hiệu, màn hình điện thoại ở bản free: dùng **Tracker** chế độ Corner Position. Xem [Planar Tracker](../02-trang/fusion/mask-tracker-keyer.md#planar-tracker--bám-mặt-phẳng) và [Tracker](../02-trang/fusion/mask-tracker-keyer.md#tracker--bám-một-điểm).

Text+, Merge, Transform, mask, keyframe, Spline — mọi thứ dùng để [làm chữ động](../02-trang/fusion/chu-dong.md) — đều có ở bản free.

## Sửa hình

- **Lens Correction** — sửa méo ống kính góc rộng. Bản free không có, kể cả ở trang Cut và Edit. Thay thế: tăng nhẹ Zoom để cắt bớt mép cong — xem [Cut → Lens Correction](../02-trang/cut/tools.md#lens-correction--sửa-méo-góc-rộng).

## Hiệu ứng

Studio có thêm vài chục ResolveFX: film grain, optical blur, motion blur, lens flare… Bản free vẫn có đủ các hiệu ứng cơ bản gồm blur, sharpen, glow, các transition.

## Màu

Bản free có **gần như toàn bộ** công cụ chỉnh màu: node, curves, qualifier, power window, tracker, color warper, LUT. Studio thêm:

- Xuất HDR và Dolby Vision (palette **HDR** để chỉnh màu thì bản free vẫn có)
- Scope cho HDR (ST.2084, HLG)
- DCTL (transform màu tự viết) — bản free chạy sẽ bị watermark
- Grading từ xa, đồng bộ nhiều máy

## Việc gì thì nên mua Studio

Mua nếu bạn: xuất 4K liên tục và muốn encode nhanh bằng phần cứng, làm nội dung dọc từ footage ngang (Smart Reframe đỡ rất nhiều thời gian), quay ở môi trường thiếu sáng nên cần Noise Reduction, hoặc thu tiếng ở nơi ồn.

Không cần mua nếu bạn: làm vlog, video ngắn, phim ngắn ở 1080p hoặc 4K 30fps, và quay ở nơi đủ sáng.

---

**Nguồn:** bảng so sánh chính thức trên [trang Blackmagic Design](https://www.blackmagicdesign.com/products/davinciresolve) là nơi tra chuẩn nhất cho phiên bản hiện tại; các con số ở trên đối chiếu thêm với [Toolfarm](https://www.toolfarm.com/tutorial/in-depth-davinci-resolve-studio-vs-the-free-version/) và [CineD](https://www.cined.com/davinci-resolve-an-in-depth-comparison-between-the-free-and-studio-version/).
