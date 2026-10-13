# Clone Tool — backup thẻ nhớ

Nút thứ ba trên Interface Toolbar (hoặc icon ở góc dưới trái). Panel hiện ra ở đáy trang Media.

Đây là công cụ ít người biết nhưng nên dùng mỗi lần đổ thẻ.

## Vì sao không copy bằng Finder

Kéo thả trong Finder **không kiểm tra** dữ liệu sau khi copy. Một bit lỗi trong file 4K thì bạn chỉ phát hiện lúc dựng, khi đã quá muộn.

Clone Tool copy kèm **kiểm tra checksum** từng file và xuất ra file log **MHL** (Media Hash List) xác nhận bản copy khớp hoàn toàn với bản gốc.

## Cách dùng

1. Bấm nút **Clone Tool** trên Interface Toolbar.
2. Bấm **Add Job**.
3. Kéo **thư mục gốc** (thẻ nhớ) vào ô **Source**.
4. Kéo **thư mục đích** vào ô **Destination**.
5. Thêm nhiều đích nếu muốn copy ra nhiều ổ cùng lúc.
6. Bấm **Clone**.

## Copy ra nhiều ổ một lúc

Thêm nhiều Destination cho cùng một job. Resolve copy song song ra tất cả.

Quy tắc an toàn cho footage: **ba bản, trên hai loại thiết bị, một bản để nơi khác**. Clone Tool lo được hai bản đầu trong một lần chạy.

## File MHL

Sau khi xong, Resolve ghi file `.mhl` vào thư mục đích. File này chứa checksum của từng file.

Giữ file đó lại. Về sau nghi ngờ ổ cứng hỏng, bạn kiểm tra lại được bằng công cụ đọc MHL.

## Lưu ý

- Clone **toàn bộ thư mục**, giữ nguyên cấu trúc thẻ. Đừng copy lẻ từng file video — nhiều máy quay (nhất là máy quay chuyên nghiệp) cần nguyên cấu trúc thư mục để đọc đúng metadata.
- Clone xong mới format thẻ, và nên kiểm tra mở thử vài file trước khi format.
