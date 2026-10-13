# Giao diện trang Photo — từng nút nằm ở đâu

![Bố cục trang Photo](../../assets/diagrams/photo-layout.svg)

---

## Thanh toolbar trên cùng

Bảy nút, từ trái sang phải:

| # | Nút | Làm gì | Mức |
|---|---|---|---|
| 1 | **Media Pool** | Ẩn/hiện kho ảnh. Ở trang này **chỉ hiện ảnh tĩnh** — video, tiếng, timeline đều bị ẩn | ★★★ |
| 2 | **Effects Library** | Ẩn/hiện kho hiệu ứng ảnh | ★★☆ |
| 3 | **Photo Album** | Mở dải album ở đáy màn hình | ★★★ |
| 4 | **Quick Export** | Xuất ảnh nhanh — xem [Xuất ảnh](xuat-anh.md) | ★★★ |
| 5 | **Metadata** | Thông tin và ghi chú của ảnh. Mở **ở cùng chỗ với Inspector** | ★☆☆ |
| 6 | **Capture** | Chụp cắm máy trực tiếp | `Studio` |
| 7 | **Inspector** | Toàn bộ thanh chỉnh ảnh — xem [Chỉnh ảnh](chinh-anh.md) | ★★★ |

---

## Thanh trên của Viewer

Từ trái sang phải:

| Nút | Làm gì | Mức |
|---|---|---|
| **Source** | Xem ảnh đang chọn trong Media Pool | ★★☆ |
| **Photo Album** | Xem ảnh đang chọn trong album | ★★★ |
| **Zoom %** | Mức phóng to. `⌘Z` vừa khung, `⌥⇧Z` đúng 100% | ★★★ |
| **Album List** | Album đang mở. Bấm mũi tên để mở nhanh album gần đây | ★★☆ |
| **Single View** | Một ảnh to | ★★★ |
| **Lightbox** | Lưới thumbnail cả album — xem [Lightbox](#lightbox--xem-cả-album-cùng-lúc) | ★★☆ |
| **Viewer Guides** | Khung an toàn, thước đo, đường gióng | ★☆☆ |
| **Photo Preview Resolution** | Giảm độ phân giải xem trước cho máy chạy nhanh | ★☆☆ |
| **Bypass Color and Fusion** | Tắt tạm mọi chỉnh sửa để so với ảnh gốc (`⇧D`) | ★★★ |
| **Capture Live View** | Màn hình chụp cắm máy | `Studio` |

> **`⇧D` là phím so sánh trước/sau nhanh nhất.** Bấm một lần thấy ảnh gốc, bấm lần nữa thấy ảnh đã chỉnh.

> **Lưu ý phím `⌘Z`:** ở các trang khác `⌘Z` là hoàn tác. Trong Viewer trang Photo, manual ghi `⌘Z` là **vừa khung ảnh**. Nếu bạn bấm `⌘Z` để hoàn tác mà ảnh chỉ co lại vừa khung, hãy bấm vào chỗ khác ngoài Viewer trước.

### Photo Preview Resolution — cho máy chạy mượt

Ảnh 40–60 megapixel rất nặng. Resolve mặc định **thu nhỏ khi xem**:

| Chế độ | Xem trước ở |
|---|---|
| **Auto** (mặc định) | Ảnh trên 4K thu về 4K |
| **Full** | Kích thước thật — chậm |
| **Half** | Một nửa |
| **Quarter** | Một phần tư |

Đổi ở đây hoặc **Playback → Photo Album Preview Resolution**.

**Lúc xuất luôn dùng kích thước gốc**, dù bạn đặt xem trước ở mức nào.

---

## Di chuyển trong ảnh

| Thao tác | Làm gì |
|---|---|
| Giữ `H` rồi kéo | Chế độ bàn tay — kéo ảnh đi |
| Bấm đúp vào một vùng | Phóng tới **100%** tại vùng đó — để soi độ nét |
| Bấm đúp lần nữa | Thu về vừa khung |

**Dùng khi:** kiểm tra mắt có nét không, soi nhiễu ở vùng tối.

---

## Lightbox — xem cả album cùng lúc

`★★☆ Thường dùng`

Bấm **Lightbox** trên thanh trên Viewer. Ảnh to biến thành **lưới thumbnail** của cả album. Kéo thanh trượt góc trên trái để đổi cỡ thumbnail.

**Điểm hay nhất:** chọn một ảnh và chỉnh — **cả lưới cập nhật trực tiếp**. Bạn thấy ngay ảnh đó có hợp tông với cả bộ hay không.

**Dùng khi:** chỉnh một bộ ảnh cùng buổi chụp (đám cưới, sản phẩm, du lịch) và muốn cả bộ đồng đều.

---

## Thanh dưới của Viewer

| Nút | Làm gì | Phím | Mức |
|---|---|---|---|
| **Tools** | Mở các công cụ Transform, Crop, Looks — xem [Tools](chinh-anh.md#tools--chỉnh-trực-tiếp-trên-viewer) | | ★★★ |
| **EXIF Data** | Hiện máy ảnh, ISO, tốc độ, khẩu độ, ống kính | | ★★☆ |
| **Favorite** (tim) | Đánh dấu ảnh yêu thích | | ★★★ |
| **Untag** | Bỏ dấu yêu thích hoặc loại | | ★★☆ |
| **Reject** (x) | Đánh dấu loại | | ★★★ |
| **Version Selector** | Đổi giữa các phiên bản đã lưu | | ★★☆ |
| **Star Rating** | Chấm 1–5 sao | `1`–`5`, `0` xoá | ★★★ |
| **Color** | Gắn nhãn màu | | ★☆☆ |
| **Flag** | Gắn cờ màu | | ★☆☆ |

Chi tiết cách lọc ảnh theo các dấu này: [Chấm sao, gắn tag](nap-va-album.md#chấm-sao-gắn-tag-gắn-cờ).

---

## Đường gióng và thước đo

`★☆☆ Tình huống cụ thể`

Bấm **Viewer Guides** trên thanh trên Viewer.

| Mục | Làm gì |
|---|---|
| **Safe Area** | Khung cho các tỉ lệ khác nhau — thấy ngay phần nào bị cắt nếu đổi tỉ lệ |
| **Rulers** | Thước đo cạnh khung, đơn vị pixel hoặc % |
| **Guides** | Đường gióng ngang/dọc tự đặt |

**Thêm đường gióng:** **View → Guides → Add Guide** → chọn vị trí, hướng, màu → **Add**. Hoặc chuột phải lên thước → **Add Guides**.

**Hít vào đường gióng:** khi dời ảnh bằng Transform, mép ảnh tự hít vào đường gióng, đường đổi **tím** là đã khớp. Giữ `⌥` để tạm tắt hít.

**Khoá đường gióng:** bấm icon ổ khoá nhỏ ở góc trên trái thước.

**Dùng khi:** căn sản phẩm vào đúng giữa, căn đường chân trời theo quy tắc một phần ba, chuẩn bị ảnh cho một khung thiết kế có sẵn.

---

## Histogram

Trang Photo mặc định hiện **Histogram** — loại biểu đồ quen thuộc với người chụp ảnh. Có thể đổi sang các scope khác của Resolve.

Bấm icon **mở rộng** góc trên phải histogram để tách ra cửa sổ to hơn.

| Histogram trông thế nào | Nghĩa |
|---|---|
| Dồn sát mép trái | Ảnh tối, có thể mất chi tiết vùng tối |
| Dồn sát mép phải | Ảnh sáng, có thể cháy |
| Trải đều từ trái sang phải | Phơi sáng tốt |
| Cột cao dựng đứng ở sát mép | Vùng đó đã **mất hẳn chi tiết** |

---

## Phím tắt trang Photo

| Việc | Phím |
|---|---|
| Chấm sao | `1`–`5`. `0` xoá sao |
| Gắn tag tốt / loại | `S` = tốt · `X` = loại. Bấm lại để bỏ |
| Xoay trái / phải | `⌘[` / `⌘]` |
| Lật ngang / dọc | `⇧[` / `⇧]` |
| Chuyển sang ảnh khác trong album | Các phím mũi tên |
| Reset tab Photo | `⌘R` *(Inspector phải đang được chọn)* |
| Bỏ mọi hiệu ứng | `⇧R` *(Inspector phải đang được chọn)* |
| Reset tất cả | `⌘⇧R` *(Inspector phải đang được chọn)* |
| So sánh với gốc | `⇧D` |
| Chế độ bàn tay | Giữ `H` |
| Mở tìm hiệu ứng | `⇧Space` |
