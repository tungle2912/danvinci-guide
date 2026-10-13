# Clip Attributes — sửa thông số clip

Chuột phải clip trong Media Pool → **Clip Attributes**.

Đây là nơi sửa những thông số Resolve đọc sai từ file, hoặc những thông số file không ghi. Sửa ở đây tác động lên **mọi chỗ clip đó xuất hiện**.

## Tab Video

| Mục | Khi nào cần sửa |
|---|---|
| **Frame Rate** | Resolve đọc nhầm fps. Hay gặp với file quay slow motion hoặc file đã qua phần mềm khác |
| **Data Levels** | Ảnh bị bệt đen hoặc cháy trắng bất thường. Đổi giữa **Video** (16–235) và **Full** (0–255) |
| **Pixel Aspect Ratio** | Hình bị méo ngang hoặc dọc. Thường để **Square** |
| **Resolution** | Khi file ghi sai kích thước |

### Data Levels — lỗi hay gặp nhất

Nếu footage mở ra thấy **vùng đen bị bệt mất chi tiết** hoặc **vùng sáng cháy sớm**, gần như chắc chắn là Data Levels sai.

Đổi từ **Auto** sang **Full** hoặc **Video** rồi xem Waveform. Đúng là khi dải sáng trải đều, không bị cắt cụt ở đầu hoặc đuôi.

## Tab Audio

Đây là nơi sửa lỗi "chỉ nghe được một bên tai nghe".

| Mục | Làm gì |
|---|---|
| **Format** | Mono, Stereo, 5.1, 7.1, Adaptive |
| **Track** | Số track tiếng trong file |
| **Channels trong mỗi track** | Gán kênh nguồn nào vào kênh đích nào |

### Sửa mic mono thu vào một kênh

Triệu chứng: giọng chỉ ra ở tai trái hoặc tai phải.

1. Clip Attributes → tab **Audio**
2. Đổi **Format** từ `Stereo` sang `Mono`
3. Hoặc giữ Stereo nhưng gán **cả hai kênh output** về cùng một **source channel**

### Mic ngoài thu vào track 2

Máy ảnh thường ghi mic trong ở track 1, mic ngoài ở track 2. Vào tab Audio, bỏ track 1, giữ track 2.

## Tab Timecode

Sửa timecode bắt đầu. Cần khi đồng bộ nhiều máy quay theo timecode mà một máy bị lệch.

## Tab Name

Đổi tên hiển thị trong Media Pool mà **không đổi tên file trên ổ**.

Hữu ích: file từ máy ảnh tên là `C0042.MP4`, đổi hiển thị thành `Phỏng vấn anh An - take 3`.

## Áp cho nhiều clip

Chọn nhiều clip rồi mở Clip Attributes — sửa một lần áp cho cả nhóm. Rất tiện khi cả thẻ nhớ đều bị đọc sai frame rate.
