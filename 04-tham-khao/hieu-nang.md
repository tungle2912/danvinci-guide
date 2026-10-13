# Tối ưu hiệu năng

Resolve lag không có nghĩa là máy bạn yếu. Phần lớn trường hợp là do codec của footage, không phải do phần cứng.

Làm theo thứ tự dưới đây, dừng lại ngay khi đã đủ mượt. Đừng làm hết từ đầu.

| Bước | Tốn gì |
|---|---|
| [1. Hạ độ phân giải khi xem](#bước-1--hạ-độ-phân-giải-khi-xem-miễn-phí-tức-thì) | Không tốn gì |
| [2. Render Cache](#bước-2--render-cache) | Ổ cache |
| [3. Hạ timeline resolution](#bước-3--hạ-timeline-resolution) | Không tốn gì |
| [4. Optimized Media](#bước-4--optimized-media) | Ổ, thời gian tạo |
| [5. Proxy Media](#bước-5--proxy-media) | Ổ, thời gian tạo |
| [Riêng trang Fusion](#riêng-trang-fusion) | — |

## Bước 1 — Hạ độ phân giải khi xem (miễn phí, tức thì)

**Playback → Timeline Proxy Resolution → Half Resolution** (hoặc Quarter Resolution). Chọn **None** để tắt.

Resolve phát ở độ phân giải thấp hơn nhưng **không đụng gì đến file gốc**. Lúc xuất vẫn full chất lượng.

Đây là thứ nên thử đầu tiên, mất 2 giây.

## Bước 2 — Render Cache

**Playback → Render Cache**. Ba chế độ:

| Chế độ | Làm gì |
|---|---|
| **Off** | Tắt |
| **Smart** | Resolve tự render trước những clip quá nặng cho GPU |
| **User** | Chỉ render những clip bạn tự đánh dấu |

**Smart là lựa chọn tốt cho hầu hết trường hợp.** Bật lên rồi để máy nghỉ vài phút, vạch màu trên timeline chuyển từ đỏ sang xanh là xong.

Chế độ **User**: chuột phải clip → **Render Cache Color Output** cho những clip có nhiều hiệu ứng.

Đặt nơi lưu cache: **Project Settings → Master Settings → Working Folders → Cache files location**. Trỏ vào SSD nhanh. Xem [Tạo project → Nơi lưu cache](../01-bat-dau/tao-du-an.md#bước-5--nơi-lưu-cache-và-file-tạo-ra).

Lúc xuất, cache dùng lại được nhờ ô **Use render cached images** — xem [Render cache khi xuất](../02-trang/deliver/render-queue-va-loi.md#render-cache-và-use-render-cached-images).

## Bước 3 — Hạ timeline resolution

**Project Settings → Master Settings → Timeline resolution** → hạ xuống 1920×1080 dù footage là 4K.

Lúc xuất, ở trang Deliver đặt lại Resolution thành 3840×2160. Resolve render từ footage gốc nên **không mất chất lượng**.

Cách này hiệu quả rõ rệt và hay bị bỏ qua.

## Bước 4 — Optimized Media

Chọn toàn bộ clip trong Media Pool → chuột phải → **Generate Optimized Media**. Rồi bật **Playback → Use Optimized Media If Available**.

Resolve tạo bản nhẹ bằng codec dễ giải mã và tự chuyển qua lại.

Chọn codec ở **Project Settings → Master Settings → Optimized Media Format**:

| Máy | Codec nên chọn |
|---|---|
| Mac | ProRes 422 LT, hoặc ProRes 422 Proxy nếu máy yếu |
| Windows | DNxHR SQ, hoặc DNxHR LB nếu máy yếu |

Đặt **Optimized Media Resolution** là Half hoặc Quarter.

Nhược điểm: tốn dung lượng ổ, và mất thời gian tạo.

## Bước 5 — Proxy Media

Giống Optimized Media nhưng tạo ra **file thật** nằm trên ổ, mang sang máy khác được.

Chuột phải clip → **Generate Proxy Media**. Dùng khi làm việc nhóm hoặc dựng trên laptop rồi chuyển sang máy bàn.

So sánh Proxy và Optimized Media chi tiết: [Proxy và Optimized Media](../02-trang/media/nap-media.md#proxy-và-optimized-media).

> Lúc xuất, để **tắt** **Use Proxy Media** — render từ proxy sẽ kém nét. Xem [Render xong mà file lỗi](../02-trang/deliver/render-queue-va-loi.md#render-xong-mà-file-lỗi).

## Riêng trang Fusion

Fusion nặng hơn trang Edit nhiều và không đảm bảo phát đúng tốc độ thực.

- Chuột phải vùng nút phát → bật **Proxy** hoặc **Auto Proxy**. Xem [Time Ruler và nút phát](../02-trang/fusion/giao-dien.md#time-ruler-và-nút-phát).
- Giữ `⌘` kéo trên Time Ruler để thu hẹp vùng render khi xem thử.
- Node quá nặng: chọn node, `⌘U` để ngừng cập nhật. Xem [Xoá, tắt tạm, khoá node](../02-trang/fusion/node-co-ban.md#xoá-tắt-tạm-khoá-node).
- Việc làm được ở trang Edit thì đừng mở Fusion. Xem [Khi nào cần Fusion](../02-trang/fusion/README.md#khi-nào-cần-fusion-khi-nào-không).

## Vấn đề gốc — codec của footage

Nếu footage là **H.264 hoặc H.265** quay từ điện thoại hay máy ảnh, đó chính là nguyên nhân. Hai codec này nén rất chặt, mỗi khung hình phải giải mã dựa vào các khung lân cận, nên tua ngược hay nhảy cóc đều rất nặng.

ProRes và DNxHR nén từng khung độc lập nên nhẹ hơn nhiều khi dựng, đổi lại file to gấp nhiều lần.

Nếu bạn làm dự án dài với footage H.265, chuyển đổi toàn bộ sang ProRes trước bằng **Shutter Encoder** (miễn phí) hoặc **HandBrake** sẽ tiết kiệm nhiều thời gian hơn là vật lộn với proxy.

## Thiết lập khác đáng chỉnh

**Project Settings → Master Settings:**
- **Optimized Media Resolution** → Half

**Preferences → System → Memory and GPU:**
- **GPU processing mode** → Metal (trên Mac)
- **Limit Resolve Memory Usage to** → để Resolve dùng khoảng 70–75% RAM máy

**Preferences → System → Decode Options:**
- Bật **Decode H.264/HEVC using hardware acceleration** nếu máy hỗ trợ

## Cấu hình máy tham khảo

| Làm gì | RAM | Ghi chú |
|---|---|---|
| 1080p | 16 GB | Đủ dùng |
| 4K | 32 GB | Nên có |
| 4K nhiều lớp, nhiều hiệu ứng | 64 GB | |

Ổ lưu footage nên là SSD. Ổ cứng cơ 5400 vòng là nút thắt lớn hơn cả CPU yếu.

## Thói quen giúp máy nhẹ

- Đóng Chrome khi dựng. Mỗi tab là một tiến trình ăn RAM.
- Tắt **Fusion** và các hiệu ứng nặng khi chưa cần xem.
- Dọn cache định kỳ: **Playback → Delete Render Cache → All**.
- Chia dự án dài thành nhiều timeline ngắn rồi ghép ở timeline tổng.

---

**Nguồn tham khảo thêm:** [Miracamp](https://www.miracamp.com/learn/davinci-resolve/how-to-fix-laggy-playback-in-davinci-resolve-optimize-timeline-performance) và [Elements.tv](https://elements.tv/blog/davinci-resolve-5-ways-to-achieve-better-playback-performance/).
