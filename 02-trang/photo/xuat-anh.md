# Xuất ảnh, đưa sang trang Color

Hai cách xuất: **Quick Export** (nhanh, đủ dùng) và **trang Deliver** (đầy đủ tuỳ chọn).

> **Chỉ phiên bản đang chọn của mỗi ảnh mới được xuất.** Nếu ảnh có nhiều [Versions](nap-va-album.md#versions--nhiều-phiên-bản-của-một-ảnh), kiểm tra Version Selector trước.

---

## Quick Export

`★★★ Hằng ngày`

Nút **Quick Export** trên toolbar trang Photo. Cửa sổ này **dành riêng cho ảnh tĩnh**, khác với Quick Export của video.

**Cách dùng:** chọn định dạng ở **cột trái** → đặt thông số ở **cột phải** → **Export**.

### Định dạng

| Định dạng | Dùng khi |
|---|---|
| **JPEG** | Đăng mạng, gửi khách. Phổ thông nhất |
| **PNG** | Cần nền trong suốt, hoặc đồ hoạ có chữ |
| **HEIC** | Dung lượng nhỏ hơn JPEG cùng chất lượng — hợp với thiết bị Apple |
| **TIFF** | In ấn, lưu trữ, gửi sang Photoshop |

### Thông số

| Thông số | Làm gì | Đặt gì |
|---|---|---|
| **Export** | Xuất **cả album** hay **chỉ ảnh đang chọn** | |
| **File Name** | Tiền tố tên file | Ví dụ `Cuoi_An_Binh_` |
| **Scale** | Kích thước gốc hoặc thu nhỏ theo % | Gốc cho in, thu nhỏ cho web |
| **Resolution** | Mật độ điểm ảnh, đơn vị ppi | **72** cho web và màn hình · **300** cho in |
| **Quality** | Chất lượng nén | Web: khoảng 85–90%. Lưu trữ: 100% |
| **Compression** | Kiểu nén (tuỳ định dạng) | |
| **Bit Depth** | Độ sâu màu | 8-bit cho JPEG. 16-bit cho TIFF nếu còn chỉnh tiếp |
| **Include Metadata** | Giữ thông tin máy ảnh, ngày chụp | Bỏ tick nếu không muốn lộ vị trí GPS |

---

## Xuất từ trang Deliver

`★★☆ Thường dùng` — khi cần nhiều kích thước hoặc nhiều định dạng cùng lúc

Đang mở một album mà sang trang **Deliver**, Resolve tự chuyển sang **chế độ xuất ảnh** riêng.

### Cách làm

1. **Render Settings**: đặt tên file, nơi lưu, định dạng.
2. Chọn xuất **Entire Album** hay **Selected Photos**.
3. **Add to Render Queue**.
4. Muốn thêm định dạng khác: đổi thiết lập, **Add to Render Queue** lần nữa.
5. **Render All**.

### Đặt tên file tự động

Ô **File Name** có nút **+**. Bấm vào để chèn **thông tin metadata** vào tên file — tự điền theo từng ảnh. Ví dụ: tên + ngày chụp + số sao.

Resolve tự thêm số thứ tự ở cuối để không trùng tên.

### Định cỡ ảnh — mục Size

| Chế độ | Làm gì | Dùng khi |
|---|---|---|
| **Original** | Đúng kích thước gốc | In, lưu trữ |
| **Width and Height** | Đặt chính xác rộng × cao | Khung thiết kế có sẵn |
| **Short Side** | Đặt cạnh ngắn, cạnh dài tự tính | |
| **Long Side** | Đặt cạnh dài, cạnh ngắn tự tính | **Đăng web** — ví dụ cạnh dài 2048px |
| **Percentage** | Thu nhỏ 25–100% | |
| **Megapixels** | Đặt theo số megapixel | Nền tảng giới hạn dung lượng |

Thêm: **Include Alpha Channel** cho PNG và TIFF có nền trong suốt.

### Ví dụ: một lần render ra ba bộ ảnh

Cùng một album, ba lần Add to Render Queue với ba thiết lập:

| Job | Định dạng | Size | Dùng cho |
|---|---|---|---|
| 1 | TIFF 16-bit | Original | Lưu trữ, in |
| 2 | JPEG 90% | Long Side 2048 | Gửi khách qua mạng |
| 3 | JPEG 85% | Long Side 1080 | Instagram |

Bấm **Render All** một lần, ra đủ ba thư mục.

---

## Đưa album sang trang Color

`★★☆ Thường dùng` — khi tab RAW và tab Photo không đủ

**Dùng khi:** cần chỉnh **riêng một vùng** — làm sáng riêng khuôn mặt, đổi riêng màu trời, đổi màu tóc. Đó là việc của Qualifier, Power Window, Color Warper — chỉ có ở trang Color.

**Cách làm:** mở album ở trang Photo, rồi chuyển sang trang **Color**. Album tự biến thành một **timeline** bình thường, mỗi ảnh là một clip.

**Chỉnh sửa ở trang Photo không mất** — chúng tự trở thành **node đầu tiên** của mỗi ảnh. Bạn thêm node tiếp theo sau nó.

Chỉnh xong quay lại trang Photo, kết quả đã nằm trong album. Xuất như bình thường, **vẫn ở độ phân giải gốc**.

> Ở các trang khác, mỗi ảnh được gán một độ dài mặc định để hiển thị như clip. Đổi độ dài này ở **Preferences → User → Editing → General Settings → Standard still duration**. Quay lại trang Photo thì độ dài tự biến mất.

Chi tiết các công cụ trang Color: [Color](../color/README.md).

### Đưa sang trang Fusion

Tương tự, album đưa sang trang **Fusion** để ghép ảnh, thêm chữ, mặt nạ, đặt vào không gian 3D. Xong quay về Photo xuất ở độ phân giải gốc.

### Trang Cut, Edit, Fairlight

Album chỉ **hiển thị như timeline** ở các trang này, không làm được gì nhiều. Muốn dùng ảnh đã chỉnh trong video: **xuất ra file** ở trang Photo rồi **nạp lại** như ảnh tĩnh bình thường.
