# Footage LOG sang Rec.709

Quay LOG xong mở ra thấy xám xịt, nhạt toẹt, tưởng hỏng. Không hỏng — đó là đúng. LOG là định dạng **giữ thông tin**, không phải định dạng để xem.

Việc của bạn là chuyển nó về Rec.709, không gian màu mà màn hình và YouTube hiểu được.

## Ba cách, chọn một

### Cách 1 — Color Space Transform (khuyên dùng)

Linh hoạt nhất, nhìn rõ từng bước.

1. Sang trang Color, chọn clip.
2. Bấm nút **Effects** (góc trên phải trang Color) → nhóm **ResolveFX Color** → kéo **Color Space Transform** thả vào node đầu tiên.
3. Đặt:
   - **Input Color Space** / **Input Gamma** — đúng profile máy quay (ví dụ `Sony S-Gamut3.Cine` / `S-Log3`)
   - **Output Color Space** — `Rec.709`
   - **Output Gamma** — `Gamma 2.4`

Nếu vùng sáng bị cháy bệt, đặt **Tone Mapping Method → DaVinci** — manual mô tả đây là lựa chọn hợp nhất cho footage máy quay gamut rộng: vùng sáng và vùng tối được nén mềm thay vì cắt cụt.

### Cách 2 — Color Management toàn project

Ít thao tác nhất khi trộn nhiều máy quay.

1. **Project Settings** (`⇧9`) → **Color Management**.
2. **Color science** → **DaVinci YRGB Color Managed**.
3. **Output color space** → **Rec.709 Gamma 2.4**.
4. Với từng clip, chuột phải trong Media Pool → **Input Color Space** → chọn profile máy quay.

Resolve tự xử lý phần còn lại. Đánh đổi: phép chuyển đổi **không hiện trong node graph** nên khó soi khi có gì sai.

### Cách 3 — LUT chuyển đổi của hãng

Nhanh nhất, kém linh hoạt nhất.

Tải LUT chuyển đổi từ trang hãng máy (Sony, Canon, Panasonic đều có), bỏ vào thư mục LUT của Resolve, rồi chuột phải node → **LUTs** → chọn LUT đó.

Nhược điểm: LUT là bảng tra cố định, nó **cắt** thông tin ở vùng sáng và tối thay vì nén mềm như CST.

> **Đừng dùng hai cách cùng lúc.** Bật Color Managed rồi lại thêm CST là chuyển đổi hai lần, ảnh sẽ sai.

## Đặt CST ở node nào

Hai trường phái, cả hai đều dùng được:

**CST ở node đầu** — mọi chỉnh sửa sau đó diễn ra trong Rec.709. Dễ hình dung, các công cụ phản ứng như bạn quen. Hợp cho người mới.

**CST ở node cuối** — bạn chỉnh trong không gian màu rộng của máy quay, giữ được nhiều thông tin ở vùng sáng hơn. Đây là cách colorist chuyên nghiệp hay làm, nhưng các bánh xe màu phản ứng lạ hơn vì đang làm việc trên dữ liệu log.

Chọn một và giữ nhất quán trong cả project.

## Chuỗi node đề xuất cho footage LOG

```
01 CST          chuyển LOG → Rec.709
02 Balance      cân bằng trắng, điểm đen, điểm trắng
03 Contrast     tương phản
04 Color        sửa hue, saturation
05 Secondary    da người, vùng cục bộ
06 Look         LUT sáng tạo hoặc color warper
07 Finishing    vignette, làm nét
```

## Profile của các máy phổ biến

| Máy | Input Color Space | Input Gamma |
|---|---|---|
| Sony (S-Log3) | S-Gamut3.Cine | S-Log3 |
| Canon (C-Log3) | Canon Cinema Gamut | Canon Log 3 |
| Panasonic (V-Log) | V-Gamut | V-Log |
| Fujifilm (F-Log) | F-Log Gamut | F-Log |
| DJI (D-Log) | DJI D-Gamut | D-Log |
| GoPro (Protune Flat) | Protune Native | Protune Flat |
| Blackmagic | Blackmagic Design Wide Gamut | Blackmagic Design Film |

Không chắc máy mình quay ở profile nào: xem metadata clip ở trang Media, hoặc tra trong menu quay của máy.

## Kiểm tra đã đúng chưa

Sau khi áp CST, trước khi chỉnh gì:

- **Waveform** — ảnh phải trải gần hết từ 0 đến khoảng 1000, không dồn cục ở giữa.
- **Vectorscope** — có màu rõ ràng chứ không co cụm vào tâm.
- Ảnh trông **bình thường**, không xám nhưng cũng chưa đẹp. Đẹp là việc của các node sau.

## Lỗi hay gặp

**Áp CST xong ảnh cháy trắng** — sai Input Gamma. Kiểm tra lại profile máy quay.

**Ảnh vẫn xám sau khi áp CST** — có thể bạn đặt Output Gamma là `Linear`. Đổi về `Gamma 2.4`.

**Màu trong Resolve đẹp, xuất ra nhạt** — thường do màn hình Mac dùng profile Display P3 còn video xuất ra Rec.709. Kiểm tra **Project Settings → Color Management → Output color space** đúng là Rec.709 Gamma 2.4, và xem thử file xuất ra bằng VLC thay vì QuickTime.
