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
- **Create Subtitles from Audio** — tự tạo phụ đề từ lời nói
- **Audio Assistant** — tự mix tiếng
- **Voice Convert** — đổi giọng người nói
- **Speed Warp** — slow motion chất lượng cao bằng AI (Optical Flow thường vẫn dùng được ở bản free)

## Chống nhiễu

- **Hình:** palette **Motion Effects** ở trang Color (Noise Reduction, Motion Blur) là `Studio`. Ở bản free, xử lý nhiễu hình từ khâu quay: đủ sáng, hạ ISO.
- **Tiếng:** **Noise Reduction** trong FairlightFX **dùng được ở bản free**. Chỉ **Voice Isolation** (tách giọng bằng AI) là `Studio`.

## Trang Color — dùng gì thay công cụ AI

- **Magic Mask** — tách người, vật bằng AI → bản free dùng Qualifier + Window
- **IntelliTrack** — tracker AI → bản free dùng Tracker thường

## Âm thanh — bản free có gì đáng chú ý

Ba công cụ "tự mix" hữu ích nhất đều **có ở bản free**: **Dialogue Leveler**, **Ducker**, **Normalize Audio Levels**. Xem [Fairlight](../02-trang/fairlight/README.md).

## Sửa hình

- **Lens Correction** — sửa méo ống kính góc rộng. Bản free không có, kể cả ở trang Cut và Edit.

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
