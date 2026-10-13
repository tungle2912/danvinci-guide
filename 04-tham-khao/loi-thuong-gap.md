# Lỗi thường gặp

## Clip hiện màu đỏ "Media Offline"

Resolve không tìm thấy file gốc. Nó **không nhúng media vào project**, chỉ lưu đường dẫn.

Nguyên nhân: bạn đổi tên file, chuyển thư mục, hoặc rút ổ cứng ngoài.

Cách sửa: chuột phải vào clip trong Media Pool → **Relink Selected Clips** → trỏ tới thư mục mới. Resolve tự nối lại các clip còn lại cùng thư mục.

Phòng tránh: sắp xếp thư mục footage **trước khi** nạp vào Resolve, và đừng đổi tên file sau đó.

## Video xuất ra bị giật

Gần như luôn là do frame rate lệch.

Kiểm tra ba chỗ phải khớp nhau:
1. Frame rate của footage (xem ở trang Media, panel Metadata)
2. **Project Settings → Timeline frame rate**
3. Trang Deliver → tab Video → **Frame rate**

Nếu timeline sai frame rate thì không sửa được — phải tạo timeline mới đúng rồi copy toàn bộ clip sang.

## Tiếng lệch hình

**Nếu lệch dần theo thời gian** — frame rate lệch. Xem mục trên.

**Nếu lệch một khoảng cố định** — thường do lỡ kéo hình và tiếng lệch nhau khi tắt Linked Selection. Clip lệch sẽ hiện **số đỏ** ở đầu tên clip (số khung bị lệch). Chuột phải vào số đỏ đó:

- **Slip into place** — trượt nội dung clip cho khớp, clip không xê dịch
- **Move into place** — dời cả clip về đúng chỗ khớp

## Màu trong Resolve đẹp, xuất ra nhạt

Vấn đề color management, hay gặp trên Mac.

Màn hình Mac dùng profile Display P3 rộng hơn Rec.709, nên Resolve hiển thị sặc hơn thực tế.

Kiểm tra:
- **Project Settings → Color Management → Output color space** phải là **Rec.709 Gamma 2.4**
- Mở file xuất ra bằng **VLC** thay vì QuickTime — QuickTime có cách xử lý màu riêng làm sai lệch

## Chỉ nghe được một bên tai nghe

Mic thu mono nhưng Resolve gán vào một kênh của stereo.

Sửa: chuột phải clip trong Media Pool → **Clip Attributes** → tab **Audio** → đổi **Format** từ Stereo sang **Mono**, hoặc gán cả hai kênh output về cùng một source.

## Không kéo được clip xuống timeline

Thường do track bị khoá. Nhìn icon ổ khoá ở đầu track, bấm để mở (`⌥⇧1` cho V1).

Hoặc do destination control chưa chọn track nào — bấm `⌥1` để chọn V1.

## Export bị kẹt ở 0% hoặc báo lỗi

- Thư mục đích hết chỗ, hoặc không có quyền ghi.
- Bật/tắt ô **Use hardware acceleration if available** rồi thử lại.
- Có clip offline trong timeline — sửa trước khi render.
- Tên file có ký tự đặc biệt — đổi tên đơn giản hơn.

## Resolve không mở được file MP4 từ điện thoại

Một số điện thoại quay bằng codec Resolve không đọc được ở bản free (ví dụ HEVC 10-bit).

Chuyển đổi trước bằng **Shutter Encoder** hoặc **HandBrake** sang H.264 hoặc ProRes.

## Project biến mất

Resolve lưu project trong **database** nội bộ chứ không phải file rời.

Tìm lại: mở **Project Manager** (`⇧1`), kiểm tra xem bạn có đang ở đúng database không — nút hình ổ cứng góc trên trái liệt kê các database.

Khôi phục bản cũ: chuột phải project → **Project Backups**.

Mang sang máy khác: **File → Export Project** ra `.drp`.

## Fusion làm Resolve chậm hẳn

Mỗi clip có Fusion composition đều phải render lại liên tục. Bật **Render Cache Smart**, hoặc chuột phải clip → **Render in Place** để "nướng" kết quả thành một clip tĩnh.

## Text+ không hiện chữ

Thường do màu chữ trùng màu nền, hoặc **Size** quá nhỏ/quá lớn khiến chữ nằm ngoài khung.

Kiểm tra trong Inspector: **Color** ở tab Shading, và **Size** cùng **Center** ở tab Layout.

## Tài liệu chính thống

Khi tài liệu này không đủ, tra ở nguồn gốc:

- **DaVinci Resolve Manual** — bản PDF đầy đủ nhất, đã có sẵn trong máy bạn tại `/Applications/DaVinci Resolve/DaVinci Resolve Manual.pdf`. Hơn 4000 trang, tra bằng tìm kiếm.
- **Sáu cuốn hướng dẫn miễn phí của Blackmagic** cho Resolve 20 — xem [Nguồn tham khảo](nguon.md).
- **Diễn đàn Blackmagic** — [forum.blackmagicdesign.com](https://forum.blackmagicdesign.com), nơi hỏi đáp chính thức.
