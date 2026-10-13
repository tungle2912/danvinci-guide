# Footage LOG sang Rec.709

Quay LOG xong mở ra thấy xám xịt, nhạt toẹt, tưởng hỏng. Không hỏng — đó là đúng. LOG là định dạng **giữ thông tin**, không phải định dạng để xem.

Việc của bạn là chuyển nó về Rec.709, không gian màu mà màn hình và YouTube hiểu được.

| Bước | Làm gì |
|---|---|
| 1 | Biết máy quay ở [profile nào](#profile-của-các-máy-phổ-biến) |
| 2 | [Chọn một trong ba cách](#ba-cách-chọn-một) chuyển đổi |
| 3 | [Kiểm tra bằng scope](#kiểm-tra-đã-đúng-chưa) trước khi chỉnh gì thêm |
| 4 | [Chỉnh tiếp bằng chuỗi node](#chuỗi-node-đề-xuất-cho-footage-log) |
| 5 | [Áp cho mọi clip cùng máy](#áp-cho-mọi-clip-cùng-máy) |
| 6 | [Xuất và soát màu](#xuất-và-soát-màu) |

## Ba cách, chọn một

| Cách | Hợp với | Nhìn thấy phép chuyển? |
|---|---|---|
| [1. Color Space Transform](#cách-1--color-space-transform-khuyên-dùng) | Một máy LOG, muốn thấy rõ từng bước | Có — là một node |
| [2. Color Management](#cách-2--color-management-toàn-project) | Trộn nhiều máy LOG khác hãng | Không |
| [3. LUT của hãng](#cách-3--lut-chuyển-đổi-của-hãng) | Cần nhanh, đã có LUT | Có — nhưng cắt vùng sáng |

So sánh đầy đủ: [Cách nào cho mình?](../02-trang/color/lut-va-quan-ly-mau.md#cách-nào-cho-mình)

### Cách 1 — Color Space Transform (khuyên dùng)

Linh hoạt nhất, nhìn rõ từng bước. Project để **Color science: DaVinci YRGB** (mặc định).

1. Sang trang Color, chọn clip. Chọn node 01 (hoặc `⌥S` thêm node). Chuột phải node → **Change Label** → gõ `CST`.
2. Bấm nút **Effects** trên toolbar → nhóm **Resolve FX Color** → kéo **Color Space Transform** thả lên node.
3. Ở tab **Settings** của bảng Effects, đặt:

| Ô | Đặt |
|---|---|
| **Input Color Space** / **Input Gamma** | Đúng profile máy quay, ví dụ `Sony S-Gamut3.Cine` / `Sony S-Log3` — xem [bảng dưới](#profile-của-các-máy-phổ-biến) |
| **Output Color Space** | `Rec.709` |
| **Output Gamma** | `Gamma 2.4` |
| **Tone Mapping Method** | `DaVinci` — nén mềm vùng sáng và tối thay vì cắt cụt |

Bảng đầy đủ các lựa chọn Tone Mapping: [Color Space Transform → Thông số](../02-trang/color/lut-va-quan-ly-mau.md#thông-số).

### Cách 2 — Color Management toàn project

Ít thao tác nhất khi trộn nhiều máy quay.

1. **Project Settings** (`⇧9`) → **Color Management**.
2. **Color science** → **DaVinci YRGB Color Managed**.
3. Tick **Automatic Color Management**. **Color processing mode** → **SDR**.
4. **Output color space** → **Rec.709**.
5. Với từng clip LOG, chuột phải trong Media Pool → **Input Color Space** → chọn profile máy quay. Resolve tự đoán theo loại file, nhưng hay đoán sai với LOG.

Resolve tự xử lý phần còn lại. Đánh đổi: phép chuyển đổi **không hiện trong node graph** nên khó soi khi có gì sai. Chi tiết: [Bật Color Managed — cách đơn giản](../02-trang/color/lut-va-quan-ly-mau.md#bật-color-managed--cách-đơn-giản).

> Quyết định cách 2 **trước khi** chỉnh màu. Đổi Color science khi đã chỉnh xong là mọi grade lệch.

### Cách 3 — LUT chuyển đổi của hãng

Nhanh nhất, kém linh hoạt nhất.

1. Tải LUT chuyển đổi từ trang hãng máy (Sony, Canon, Panasonic đều có).
2. **Project Settings → Color Management → Lookup Tables** → **Open LUT Folder**, chép file `.cube` vào đó, bấm **Update Lists**.
3. Chuột phải node 01 → **LUT** → chọn LUT đó.

Nhược điểm: LUT là bảng tra cố định, nó **cắt** thông tin ở vùng sáng và tối thay vì nén mềm như CST. Xem [Cài LUT mua/tải về](../02-trang/color/lut-va-quan-ly-mau.md#cài-lut-muatải-về).

> **Đừng dùng hai cách cùng lúc.** Bật Color Managed rồi lại thêm CST hay LUT chuyển đổi là chuyển hai lần, ảnh sẽ sai.

## Đặt CST ở node nào

Hai trường phái, cả hai đều dùng được:

**CST ở node đầu** — mọi chỉnh sửa sau đó diễn ra trong Rec.709. Dễ hình dung, các công cụ phản ứng như bạn quen. Hợp cho người mới.

**CST ở node cuối** — bạn chỉnh trong không gian màu rộng của máy quay, giữ được nhiều thông tin ở vùng sáng hơn. Đây là cách colorist chuyên nghiệp hay làm, nhưng các bánh xe màu phản ứng lạ hơn vì đang làm việc trên dữ liệu log.

Chọn một và giữ nhất quán trong cả project.

## Kiểm tra đã đúng chưa

Sau khi áp CST, trước khi chỉnh gì:

- **Waveform** — ảnh phải trải gần hết từ 0 đến khoảng 1000, không dồn cục ở giữa. Xem [Waveform](../02-trang/color/scopes.md#waveform).
- **Vectorscope** — có màu rõ ràng chứ không co cụm vào tâm. Xem [Vectorscope](../02-trang/color/scopes.md#vectorscope).
- Ảnh trông **bình thường**, không xám nhưng cũng chưa đẹp. Đẹp là việc của các node sau.

**So trước/sau:**
- Chọn node CST → `⌘D` bật/tắt riêng node đó.
- `⇧D` bật/tắt toàn bộ grade.
- Grab Still (`⌥⌘G`) lúc chưa chỉnh, rồi bấm đúp still để chia đôi Viewer — xem [Image Wipe](../02-trang/color/giao-dien.md#image-wipe--so-với-still).

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

Đây là [chuỗi 6 node](../02-trang/color/node.md#chuỗi-6-node-cơ-bản) có thêm node CST ở đầu. Dùng Cách 2 thì bỏ node 01.

Cân bằng ở node 02 bằng [Parade](../02-trang/color/scopes.md#parade) và [bánh xe màu](../02-trang/color/can-bang.md#sáng-tối--4-bánh-xe). Look ở node 06: [LUT sáng tạo](../02-trang/color/lut-va-quan-ly-mau.md#lut-là-gì) — quá gắt thì [giảm độ mạnh LUT](../02-trang/color/lut-va-quan-ly-mau.md#giảm-độ-mạnh-lut).

## Áp cho mọi clip cùng máy

Có 40 clip cùng máy, cùng profile:

1. Ở clip đầu tiên, chuột phải node CST → **Save as Shared Node**.
2. Ở clip khác: chuột phải Node Editor → **Add Node** → chọn Shared Node đó (cuối danh sách).
3. Sửa Shared Node ở một clip → mọi clip dùng nó đổi theo.

Xem [Shared Node](../02-trang/color/lut-va-quan-ly-mau.md#một-cst-cho-mọi-clip-cùng-máy--shared-node). Muốn copy cả chuỗi node: [Áp grade cho nhiều clip](../02-trang/color/node.md#áp-grade-cho-nhiều-clip) hoặc [Group](../02-trang/color/node.md#group--nhóm-các-clip-cùng-bối-cảnh).

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

Tên trong menu CST có thể kèm tên hãng (ví dụ `Sony S-Log3`). Không chắc máy mình quay ở profile nào: xem metadata clip ở trang Media ([Metadata Editor](../02-trang/media/metadata.md)), hoặc tra trong menu quay của máy.

## Xuất và soát màu

1. Ở trang Deliver, preset YouTube hoặc TikTok dùng được ngay — xem [Preset theo nền tảng](../02-trang/deliver/preset-theo-nen-tang.md).
2. Dùng Custom Export thì để **Advanced Settings → Color Space Tag** và **Gamma Tag** ở **Same as Project**, **Data Levels** ở **Auto**. Xem [Advanced Settings](../02-trang/deliver/cai-dat-xuat.md#advanced-settings--những-ô-đáng-biết).
3. Render xong, mở file xem thử bằng VLC — QuickTime có cách xử lý màu riêng, dễ làm bạn tưởng màu sai.

## Lỗi hay gặp

**Áp CST xong ảnh cháy trắng** — sai Input Gamma. Kiểm tra lại profile máy quay.

**Ảnh vẫn xám sau khi áp CST** — có thể bạn đặt Output Gamma là `Linear`. Đổi về `Gamma 2.4`.

**Màu sai hẳn, quá đậm hoặc quá tương phản** — chuyển đổi hai lần: đang bật Color Managed mà vẫn thêm CST hoặc LUT chuyển đổi. Bỏ một trong hai.

**Màu trong Resolve đẹp, xuất ra nhạt** — thường do màn hình Mac dùng profile Display P3 còn video xuất ra Rec.709. Kiểm tra **Project Settings → Color Management → Output color space** đúng là Rec.709, và xem thử file xuất ra bằng VLC thay vì QuickTime. Thêm: [Lỗi thường gặp](../04-tham-khao/loi-thuong-gap.md#màu-trong-resolve-đẹp-xuất-ra-nhạt).
