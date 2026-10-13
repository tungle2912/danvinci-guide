# Chỉnh ảnh tĩnh và ảnh RAW

Từ bản 21, Resolve có hẳn trang [Photo](../02-trang/photo/README.md) chuyên chỉnh ảnh — album, chấm sao, tab RAW, xuất JPEG/PNG/HEIC/TIFF ở độ phân giải gốc. **Với ảnh, bắt đầu ở trang Photo.** Chỉ sang trang **Color** khi cần chỉnh từng vùng (Qualifier, Power Window, Color Warper).

| Bước | Trang | Đọc |
|---|---|---|
| [1. Nạp ảnh, tạo album](#1-nạp-ảnh-tạo-album) | Photo | [Nạp ảnh, album](../02-trang/photo/nap-va-album.md) |
| [2. Lọc ảnh đẹp](#2-lọc-ảnh-đẹp) | Photo | [Chấm sao, gắn cờ](../02-trang/photo/nap-va-album.md#chấm-sao-gắn-tag-gắn-cờ) |
| [3. Chỉnh RAW](#3-chỉnh-raw--cân-bằng-trắng-và-phơi-sáng) | Photo | [Tab RAW](../02-trang/photo/chinh-anh.md#tab-raw--chỉnh-từ-dữ-liệu-gốc) |
| [4. Chỉnh màu, tương phản](#4-chỉnh-màu-và-tương-phản) | Photo | [Tab Photo](../02-trang/photo/chinh-anh.md#tab-photo--adjustments) |
| [5. Crop](#5-crop-và-thẳng-khung) | Photo | [Crop](../02-trang/photo/chinh-anh.md#crop) |
| [6. Áp cho cả loạt](#6-áp-cho-cả-loạt) | Photo | [Áp cùng chỉnh sửa](../02-trang/photo/chinh-anh.md#áp-cùng-chỉnh-sửa-cho-nhiều-ảnh) |
| [7. Chỉnh từng vùng (nếu cần)](#7-chỉnh-từng-vùng--sang-trang-color) | Color | [Đưa album sang Color](../02-trang/photo/xuat-anh.md#đưa-album-sang-trang-color) |
| [8. Xuất](#8-xuất) | Photo, Deliver | [Xuất ảnh](../02-trang/photo/xuat-anh.md) |

## 1. Nạp ảnh, tạo album

1. Mở trang **Photo**. Nút **Import Media** trên đầu Media Pool → chọn file.
2. Chuột phải trong Media Pool → **New Photo Album**. Chuột phải ảnh → **Add Photo(s) to Album**.

RAW đọc được: Canon **CR3**, Fujifilm **RAF**, Apple **ProRAW**, Nikon **NEF**, Sony **ARW**, Panasonic **RW2**. Ảnh thường: JPEG, PNG, HEIC, TIFF. Xem [Định dạng RAW được hỗ trợ](../02-trang/photo/nap-va-album.md#định-dạng-raw-được-hỗ-trợ).

## 2. Lọc ảnh đẹp

Phím `1`–`5` chấm sao, `0` xoá sao. Lọc album theo số sao để chỉ còn ảnh cần chỉnh. Xem [Quy trình lọc ảnh trong 3 lượt](../02-trang/photo/nap-va-album.md#quy-trình-lọc-ảnh-trong-3-lượt).

## 3. Chỉnh RAW — cân bằng trắng và phơi sáng

Nút **Inspector** góc trên phải → tab **RAW** (chỉ sáng lên với file RAW). Các thanh ở đây tác động lên **dữ liệu cảm biến gốc**, nên chỉnh ở đây chất lượng hơn chỉnh về sau.

| Thanh | Làm gì |
|---|---|
| **White Balance** / **Color Temp** / **Tint** | Cân bằng trắng |
| **Exposure** | Phơi sáng |
| **Highlights** / **Shadows** | Kéo lại vùng cháy và vùng tối |
| **Color Boost** | Tăng độ tươi ở chỗ còn nhạt |
| **Midtone Detail** | Độ nét vùng trung gian |

Làm hết phơi sáng và cân bằng trắng ở đây trước. Thứ tự kéo: [Thứ tự kéo các thanh trong tab RAW](../02-trang/photo/chinh-anh.md#thứ-tự-kéo-các-thanh-trong-tab-raw). Ảnh JPEG thì cân bằng ở đâu: [Cân bằng trắng chỉnh ở đâu?](../02-trang/photo/chinh-anh.md#cân-bằng-trắng-chỉnh-ở-đâu)

## 4. Chỉnh màu và tương phản

Tab **Photo** của Inspector. Bấm **Auto Balance** để có điểm khởi đầu, rồi chỉnh các thanh trong **Adjustments**. Xem [Auto Balance](../02-trang/photo/chinh-anh.md#auto-balance--bắt-đầu-từ-đây) và [Các thanh trong Adjustments](../02-trang/photo/chinh-anh.md#các-thanh-trong-adjustments).

Muốn tông màu có sẵn: [Looks](../02-trang/photo/chinh-anh.md#looks--tông-màu-có-sẵn). Thêm grain, vignette, glow: [Hiệu ứng ảnh](../02-trang/photo/hieu-ung.md).

## 5. Crop và thẳng khung

Nút **Tools** dưới đáy Viewer → **Crop** → **Aspect Ratio** chọn tỉ lệ (ví dụ `4:5` cho Instagram). Xem [Crop](../02-trang/photo/chinh-anh.md#crop).

## 6. Áp cho cả loạt

Ảnh cùng buổi chụp, cùng ánh sáng: chỉnh một ảnh rồi áp cho cả loạt bằng **click chuột giữa** hoặc **Paste Attributes**. Xem [Áp cùng chỉnh sửa cho nhiều ảnh](../02-trang/photo/chinh-anh.md#áp-cùng-chỉnh-sửa-cho-nhiều-ảnh).

Thử nhiều kiểu trên một ảnh mà không mất bản cũ: [Versions](../02-trang/photo/nap-va-album.md#versions--nhiều-phiên-bản-của-một-ảnh).

## 7. Chỉnh từng vùng — sang trang Color

Cần làm sáng riêng khuôn mặt, đổi riêng màu trời, đổi màu áo — đó là việc của trang Color.

1. Mở album ở trang Photo, rồi chuyển sang trang **Color**. Album tự thành một timeline, mỗi ảnh là một clip.
2. Chỉnh sửa ở trang Photo không mất — chúng thành **node đầu tiên** của mỗi ảnh. Thêm node sau nó (`⌥S`).
3. Chỉnh xong quay lại trang Photo. Kết quả đã nằm trong album, xuất vẫn ở độ phân giải gốc.

Chuỗi node gợi ý cho ảnh (node 01 là phần chỉnh từ trang Photo):

```
01 Photo        chỉnh từ trang Photo (tự có)
02 Color        Hue vs Hue, Hue vs Sat
03 Local        Power Window cho vùng cần sáng/tối riêng
04 Look         tông màu
05 Sharpen      Blur palette, làm nét nhẹ
```

**Công cụ trang Color hợp với ảnh:**

| Công cụ | Dùng khi | Đọc |
|---|---|---|
| **Curves Hue vs Hue / Hue vs Sat** | Đổi riêng một màu mà không đụng màu khác | [Curves chi tiết](../02-trang/color/curves-chi-tiet.md#hue-vs-hue--đổi-màu-này-thành-màu-kia) |
| **Qualifier** | Tách vùng theo màu, có vùng lõi và vùng mềm cho H, S, L | [Qualifier](../02-trang/color/curves-va-vung.md#qualifier--hút-màu) |
| **Window** | Khoanh vùng. Ảnh tĩnh nên không cần Tracker | [Window](../02-trang/color/curves-va-vung.md#window--khoanh-vùng) |
| **Color Warper** | Kéo màu da, đổi màu áo | [Color Warper](../02-trang/color/palette-khac.md#color-warper--kéo-màu-này-sang-màu-kia) |
| **RGB Mixer** | Ảnh đen trắng có chủ ý | [RGB Mixer](../02-trang/color/palette-khac.md#rgb-mixer--đen-trắng-có-chủ-ý) |

Cần ghép ảnh, thêm chữ: album cũng đưa sang được trang Fusion — xem [Đưa sang trang Fusion](../02-trang/photo/xuat-anh.md#đưa-sang-trang-fusion).

## 8. Xuất

| Cách | Khi nào | Đọc |
|---|---|---|
| **Quick Export** trên toolbar trang Photo | Một định dạng, nhanh. JPEG, PNG, HEIC, TIFF | [Quick Export](../02-trang/photo/xuat-anh.md#quick-export) |
| **Trang Deliver** khi đang mở album | Nhiều kích thước, nhiều định dạng một lượt | [Xuất từ trang Deliver](../02-trang/photo/xuat-anh.md#xuất-từ-trang-deliver) |

Quick Export: chọn định dạng ở cột trái, đặt **Quality** khoảng 85–90% cho web, **Resolution** 72 ppi cho màn hình, 300 ppi cho in. Bỏ tick **Include Metadata** nếu không muốn lộ vị trí GPS.

Mang tông màu ảnh sang video: [Lưu tông màu thành LUT](../02-trang/photo/chinh-anh.md#lưu-tông-màu-thành-lut).

## Ảnh nằm trong timeline video

Ảnh dùng làm cảnh trong video (ảnh minh hoạ, ảnh bìa) thì nạp như clip thường ở trang Media hoặc Edit, chỉnh ở trang Color như mọi clip khác.

- Độ dài mặc định trên timeline: **Preferences → User → Editing → General Settings → Standard still duration**.
- Lấy một khung hình từ video làm ảnh: **File → Export → Current Frame as Still** ở trang Media, Cut hoặc Edit. Xem [Ảnh tĩnh và chuỗi ảnh](../02-trang/deliver/preset-theo-nen-tang.md#ảnh-tĩnh-và-chuỗi-ảnh).

## Khi nào đừng dùng Resolve cho ảnh

- Cần xử lý hàng loạt vài nghìn ảnh mỗi tuần → phần mềm chuyên ảnh như Lightroom quen tay hơn.
- Cần retouch, xoá vật thể, ghép ảnh phức tạp → Photoshop hoặc Affinity. Object Removal ở Resolve là `Studio`.

Dùng Resolve cho ảnh khi: bạn cần tông màu khớp với video trong cùng dự án, hoặc cần công cụ tách màu của trang Color.
