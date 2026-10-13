# Media — nạp và tổ chức

![Trang Media trong Resolve 21, project demo](../../assets/img/page-media.png)


Trang đầu tiên. Nơi footage đi vào project.

Khác với phần mềm khác dùng hộp thoại Import, Resolve dành hẳn một trang cho việc này — vì ở dự án lớn, nạp và sắp xếp media là cả một công đoạn.

## Năm vùng của trang Media

Mặc định trang chia làm năm vùng:

| Vùng | Vị trí | Dùng để |
|---|---|---|
| **Media Storage** | Trên trái | Duyệt ổ cứng, xem clip **trước khi** nạp |
| **Viewer** | Trên phải | Xem clip, đặt điểm vào/ra |
| **Audio Panel** | Dưới Viewer | Đồng hồ đo tiếng, hoặc dạng sóng để đồng bộ |
| **Metadata Editor** | Phải | Thông tin clip, nơi gõ ghi chú |
| **Media Pool** | Dưới | Kho clip của project |

## Thanh Interface Toolbar

Nằm **trên cùng trang Media**. Tám nút, kể từ trái sang phải — đây là thứ bạn bấm để bật tắt từng vùng:

| # | Nút | Làm gì |
|---|---|---|
| 1 | **Media Storage full/half height** | Cho Media Storage chiếm hết chiều cao màn hình, đổi lại Media Pool bị thu nhỏ |
| 2 | **Media Storage** | Ẩn/hiện Media Storage. Ẩn đi thì Viewer rộng ra |
| 3 | **Clone Tool** | Ẩn/hiện công cụ copy thẻ nhớ |
| 4 | **Audio Panel** | Ẩn/hiện panel âm thanh |
| 5 | **Metadata** | Ẩn/hiện Metadata Editor |
| 6 | **Inspector** | Ẩn/hiện Inspector |
| 7 | **Capture** | Chuyển Viewer sang chế độ thu từ đầu băng (hiếm dùng) |
| 8 | **Audio/Metadata full/half height** | Cho Audio Panel hoặc Metadata chiếm hết chiều cao |

Đổi kích thước vùng: kéo đường viền giữa hai panel bất kỳ.

## Mẹo: bật chỉ báo focus

Mặc định **tắt**. Khi bật, panel đang nhận phím tắt sẽ có viền cam ở cạnh trên — rất hữu ích khi bạn bấm phím mà không hiểu sao nó tác động nhầm chỗ.

Bật ở: **DaVinci Resolve → Preferences → User → UI Settings → Show focus indicators in the user interface**.

## Dùng hai màn hình

**Workspace → Dual Screen → On**.

Màn chính giữ Media Storage và Media Pool. Màn phụ hiện Viewer to, Audio Panel, Metadata Editor và **bộ scope đầy đủ** — tiện để soi chất lượng footage ngay lúc nạp.

Đổi chiều: **Workspace → Primary Display → Display 1 / Display 2**.

Màn hình siêu rộng một cái cũng dùng được chế độ này, Resolve tự chia đôi.

## Các trang con

* [Media Storage — duyệt ổ cứng](media-storage.md)
* [Media Pool — kho clip](media-pool.md)
* [Bin, Power Bin, Smart Bin](bin.md)
* [Nạp media vào project](nap-media.md)
* [Metadata Editor](metadata.md)
* [Clip Attributes — sửa thông số clip](clip-attributes.md)
* [Clone Tool — backup thẻ nhớ](clone-tool.md)
