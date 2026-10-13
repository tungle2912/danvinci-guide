# Boring Detector và Quick Export

Hai công cụ cho bước cuối: **soát lại** bản dựng và **xuất nhanh**.

---

## Boring Detector

`★☆☆ Tình huống cụ thể` — nhưng nên chạy một lần trước khi xuất

**Là gì:** quét timeline và **tô màu** những clip quá dài (dễ gây chán) hoặc quá ngắn (dễ là lỗi).

**Mở:** icon **Timeline Options** (góc trên trái timeline) → **Boring Detector**.

Cửa sổ **Analyze Timeline Edits** hiện ra với hai thanh trượt:

| Thanh | Đặt gì | Clip bị tô |
|---|---|---|
| **Boring Clips** | Số **giây** tối đa một clip được phép dài | Dài hơn → tô **xám nhạt** trên timeline trên |
| **Jump Cuts** | Số **khung** tối thiểu một clip phải có | Ngắn hơn → tô **đỏ** trên timeline trên |

Bấm **Analyze**.

Boring Detector **chạy liên tục** — bạn sửa tới đâu nó cập nhật tới đó. Tắt bằng cách bấm lại icon.

### Hai cách dùng thực tế

**Tìm flash frame** — dùng nhiều nhất:
Đặt **Jump Cuts = 2 khung**. Mọi clip chỉ dài 1–2 khung sẽ đỏ lên. Đó gần như luôn là **mẩu thừa** sót lại khi cắt — mắt thường xem không thấy nhưng người xem sẽ thấy hình nháy.

**Soát nhịp cho video ngắn:**
Đặt **Boring Clips** theo loại video:

| Loại | Ngưỡng gợi ý |
|---|---|
| TikTok, Reels | 3–4 giây |
| Vlog YouTube | 8–10 giây |
| Phim tài liệu | 15–20 giây |

Không phải cứ xám là phải cắt. Cảnh phong cảnh đẹp dài 12 giây có thể là chủ ý. Nó chỉ nhắc bạn **xem lại**.

---

## Quick Export

`★★☆ Thường dùng`

**Là gì:** xuất file bằng **preset có sẵn** trong một bước, không phải sang trang Deliver chỉnh thông số.

**Mở:** nút **Quick Export** góc trên phải trang Cut. Hoặc **File → Quick Export** — dùng được ở **mọi trang**.

### Cách làm

1. (Tuỳ chọn) Đặt `I` `O` trên timeline nếu chỉ muốn xuất một đoạn. Không đặt thì xuất cả timeline.
2. Mở Quick Export.
3. Chọn preset ở **hàng icon trên cùng**.
4. Bấm **Export** → chọn thư mục, đặt tên → **Save**.

Thanh tiến trình cho biết còn bao lâu.

### Đăng thẳng lên mạng

Quick Export **tải lên trực tiếp** được **YouTube**, **Vimeo**, **Dropbox** sau khi xuất. Cần đăng nhập tài khoản trong **Preferences → Internet Accounts** trước.

### Tự tạo preset riêng

Preset có sẵn không đúng ý (ví dụ bạn muốn bitrate cụ thể cho TikTok)? Tạo một lần, dùng mãi:

1. Sang trang **Deliver**, chọn **Custom Export**.
2. Chỉnh Video, Audio, File theo ý.
3. Menu **ba chấm** của Render Settings → **Save as New Preset**.
4. Đặt tên, chọn icon.
5. Tick **Add to quick export** → **Save**.

Preset đó giờ xuất hiện trong Quick Export ở mọi trang.

> Chỉ thiết lập **Single Clip** mới lưu thành preset được, **Individual Clips** thì không.

### Khi nào dùng Quick Export, khi nào sang Deliver

| Dùng **Quick Export** | Sang **[Deliver](../deliver/README.md)** |
|---|---|
| Bản nháp gửi khách xem | Bản cuối, cần kiểm soát bitrate chính xác |
| Video ngắn đăng mạng xã hội | Cần xuất nhiều phiên bản cùng lúc |
| Preset có sẵn là đủ | Cần burn phụ đề, đổi codec đặc biệt |
| Xuất xong là đăng luôn | Cần xuất từng clip riêng |

> **Mẹo:** tạo sẵn ba preset tuỳ chỉnh — *TikTok 1080×1920*, *YouTube 1080p*, *Bản nháp nhẹ* — và tick Add to quick export cho cả ba. Từ đó gần như không phải mở trang Deliver.
