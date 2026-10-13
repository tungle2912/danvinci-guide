# LUT và quản lý màu

Ba công cụ cùng làm một việc — **biến đổi màu theo công thức có sẵn** — nhưng khác nhau ở chỗ đặt và độ an toàn:

| Công cụ | Là gì | Mức |
|---|---|---|
| **LUT** | File bảng tra màu (.cube…). Áp vào là ra một look | ★★★ |
| **Color Space Transform** (CST) | Hiệu ứng chuyển không gian màu bằng toán học, không cắt dữ liệu | ★★☆ |
| **Color Management** của project | Resolve tự chuyển màu cho mọi clip | ★★☆ |

Quay LOG và cần biết **chọn cách nào**: xem [Footage LOG sang Rec.709](../../03-luong/log-sang-rec709.md). Trang này nói **mỗi nút ở đâu, làm gì**.

---

## LUT là gì

LUT (Lookup Table) là một file không có giao diện. Nó ghi sẵn: màu vào thế này thì ra thế kia.

Hai loại hay gặp:

| Loại | Làm gì | Đặt ở đâu trong chuỗi node |
|---|---|---|
| **LUT kỹ thuật** (chuyển đổi) | Đưa footage LOG về Rec.709. Hãng máy quay phát hành | **Đầu chuỗi** — xem [Đặt CST ở node nào](../../03-luong/log-sang-rec709.md#đặt-cst-ở-node-nào) |
| **LUT sáng tạo** (look) | Tạo tông màu: phim, teal-orange, đen trắng… | **Sau khi đã cân bằng** — node 05 Look trong [chuỗi 6 node](node.md#chuỗi-6-node-cơ-bản) |

> Quy tắc "không đặt LUT ở node 01" trong trang [Node](node.md#bốn-nguyên-tắc) là nói về **LUT sáng tạo**. LUT look được thiết kế cho ảnh **đã chuẩn** — đặt trước khi cân bằng thì ra màu sai.

**Định dạng Resolve đọc được:** `.cube` (1D, 3D, shaper), Panasonic VLUT, CLF, DCTL.

---

## Ba chỗ đặt LUT

| Chỗ | Cách | Mức | Ghi chú |
|---|---|---|---|
| **Trong node** | Chuột phải node → **LUT** → chọn | ★★★ | **Nên dùng.** LUT nằm trong grade, copy grade là copy theo |
| **Clip nguồn** | Chuột phải clip (Media Pool hoặc dải clip) → **3D LUT** → chọn | ★☆☆ | Tiện, nhưng manual lưu ý **không copy được sang timeline khác** bằng ColorTrace |
| **Cả project** | **Project Settings** → **Color Management** → **Lookup Tables** | ★☆☆ | Áp cho **mọi clip** của timeline |

### Áp LUT trong node — ba cách

1. **Chuột phải node** → **LUT** → chọn nhóm (**3D LUT**, **1D Input LUT**, **1D Output LUT**, **DCTL**, **CLF**) → chọn file.
2. **Kéo** LUT từ LUT Browser **thả lên node**. Node đã có LUT thì bị thay.
3. **Chuột phải node** → **LUT** → **Favorites** — danh sách LUT đã gắn sao.

> Giữ `⌥` khi rê chuột trong menu LUT → Viewer **xem trước** từng LUT ngay.

Xem node đang dùng LUT nào: chuột phải node → **Reveal Selected LUT**.

### LUT là bước cuối trong node

Trong **một node**, LUT luôn áp **sau** mọi chỉnh sửa khác của node đó.

**Lợi dụng điều này:** LUT làm cháy vùng sáng → trong **cùng node** đó, kéo Gain hoặc Highlights xuống. Ảnh được hạ sáng **trước khi** vào LUT, chi tiết quay lại.

### Giảm độ mạnh LUT

LUT quá tay → chọn node chứa LUT → palette **Key** → **Key Output Gain** về khoảng **0.5**. Xem [Key](palette-khac.md#key--giảm-cường-độ-node).

---

## LUT Browser

`★★☆ Thường dùng` · Nút **LUTs** trên toolbar.

Mọi LUT trong máy, xếp theo nhóm ở cột trái, có **ảnh xem trước**.

| Việc | Cách |
|---|---|
| Xem trước trên **clip đang chỉnh** | Option menu của LUT Browser → **Live Preview**. Chọn node, rồi rê chuột qua LUT |
| Gắn sao (Favorites) | Rê chuột lên LUT → bấm **ngôi sao** góc trên phải. Hoặc chuột phải → **Add to Favorites** |
| Tìm | Mở nhóm → bấm **kính lúp** → gõ tên |
| Đổi kiểu xem | Nút **Column** / **Thumbnail** góc trên phải |
| Áp vào node đang chọn | Chuột phải LUT → **Apply LUT to Current Node** |
| So 16 LUT cùng lúc | `⌘`+bấm chọn nhiều LUT → Viewer **Split Screen** → **Selected LUTs** |
| Làm mới sau khi chép LUT mới vào | Chuột phải vùng trống → **Refresh** |

### Cài LUT mua/tải về

1. **Project Settings** (`⇧9`) → **Color Management** → mục **Lookup Tables** → bấm **Open LUT Folder**.
2. Chép file `.cube` vào thư mục vừa mở. Nên tạo thư mục con theo tên bộ LUT.
3. Quay lại, bấm **Update Lists**.

Thư mục mặc định trên macOS: `Library/Application Support/Blackmagic Design/DaVinci Resolve/LUT/`.

> Bản tải từ **Mac App Store** dùng thư mục khác. Luôn dùng nút **Open LUT Folder** cho chắc.

### Xuất grade thành LUT

Chuột phải clip trên dải clip → **Generate LUT** → **33 Point Cube**.

Chỉ gồm chỉnh ở **Color Wheels**, **Custom Curves** và vài Resolve FX (CST, ACES Transform, Gamut Mapping). Qualifier, Window, Blur bị **bỏ qua**.

**Dùng khi:** muốn mang look sang máy quay để xem lúc quay, hoặc dùng ở phần mềm khác.

---

## Color Space Transform

`★★☆ Thường dùng` · Có trong bản **free**.

**Là gì:** hiệu ứng Resolve FX. Làm việc như LUT chuyển đổi, nhưng dùng **toán học của Color Management** nên **không cắt** vùng sáng, vùng tối.

**Dùng khi:** chuyển LOG → Rec.709 mà muốn thấy rõ phép chuyển nằm ở node nào.

**Cách thêm:**
1. Chọn node (hoặc tạo node mới `⌥S`).
2. Nút **Effects** trên toolbar → nhóm **Resolve FX Color** → kéo **Color Space Transform** thả lên node.
3. Chỉnh thông số ở tab **Settings** của bảng Effects.

### Thông số

| Thông số | Đặt gì |
|---|---|
| **Input Color Space** / **Input Gamma** | Profile máy quay — bảng [profile máy phổ biến](../../03-luong/log-sang-rec709.md#profile-của-các-máy-phổ-biến) |
| **Output Color Space** / **Output Gamma** | Rec.709 / Gamma 2.4 cho YouTube, TV |
| **Swap** | Đảo chiều vào ↔ ra |
| **Tone Mapping Method** | Cách nén dải sáng khi chuyển |
| **Gamut Mapping Method** | Cách nén độ đậm khi chuyển sang không gian màu hẹp hơn |

**Tone Mapping — chọn gì:**

| Lựa chọn | Làm gì | Dùng khi |
|---|---|---|
| **None** | Không nén | Hai đầu cùng dải sáng |
| **Clip** | Cắt cụt phần vượt | Hiếm khi |
| **Simple** | Nén bằng một đường cong đơn giản | Nhanh, đủ dùng |
| **Luminance Mapping** | Như DaVinci, chính xác hơn khi mọi clip cùng một chuẩn (Rec.709, Rec.2020) | Footage chuẩn video |
| **DaVinci** | Nén mềm cả vùng sáng và tối, giảm bão hoà ở hai đầu | **Footage máy quay LOG**, trộn nhiều máy |
| **Saturation Preserving** | Nén mềm nhưng giữ độ đậm ở vùng sáng | Muốn màu đậm, chịu chỉnh thêm |

### Một CST cho mọi clip cùng máy — Shared Node

Có 40 clip quay bằng cùng máy Sony S-Log3:

1. Ở clip đầu tiên, dựng node CST như trên.
2. Chuột phải node đó → **Save as Shared Node**. Node tự **khoá** để khỏi sửa nhầm.
3. Ở clip khác: chuột phải Node Editor → **Add Node** → tên Shared Node (cuối danh sách).

Sửa Shared Node ở một clip → **mọi clip dùng nó đổi theo**.

---

## Color Management của project

`★★☆` · **Project Settings** (`⇧9`) → **Color Management** → **Color science**.

### Bốn lựa chọn Color science

| Lựa chọn | Làm gì | Hợp với |
|---|---|---|
| **DaVinci YRGB** (mặc định) | Resolve **không đụng** màu. Bạn tự chuyển bằng LUT hoặc CST | Footage thường (điện thoại, máy ảnh không LOG). Người muốn thấy rõ mọi bước trong node |
| **DaVinci YRGB Color Managed** | Resolve **tự chuyển** mọi clip về không gian màu chung (manual gọi là RCM) | Trộn nhiều máy quay LOG khác nhau |
| **DaVinci YRGB Color Managed (Legacy)** | Bản cũ, để mở project cũ | Project làm từ bản Resolve cũ |
| **ACEScc / ACEScct** | Chuẩn ACES của ngành phim | Làm theo quy trình xưởng phim |

### Bật Color Managed — cách đơn giản

1. **Color science** → **DaVinci YRGB Color Managed**.
2. Tick **Automatic Color Management**.
3. **Color processing mode** → **SDR**.
4. **Output color space** → Rec.709 (cho YouTube, TV).

Resolve tự đoán Input Color Space theo loại file. Đoán sai (hay gặp với LOG): chuột phải clip trong Media Pool → **Input Color Space** → chọn đúng profile.

Bỏ tick **Automatic Color Management** thì có danh sách **preset**:

| Preset | Dùng khi |
|---|---|
| **SDR Rec.709** (mặc định) | YouTube, TV, mạng xã hội — **chọn cái này nếu không chắc** |
| **SDR P3 Broadcast / SDR P3 Cinema / SDR Rec.2020** | Giao hàng gamut rộng hoặc chiếu rạp |
| **DaVinci Wide Gamut** | Chỉnh trong không gian rộng nhất, cho cả SDR và HDR |
| **HDR P3 Broadcast / HDR Rec.2020** | Làm video HDR |
| **Custom** | Tự đặt mọi thứ |

> **Đổi Color science khi đã chỉnh xong là mọi grade lệch.** Quyết định trước khi bắt đầu chỉnh màu.

### Cách nào cho mình?

| Tình huống | Chọn |
|---|---|
| Quay điện thoại, máy ảnh chế độ màu thường | **DaVinci YRGB** — không cần chuyển gì |
| Một máy quay LOG, muốn thấy rõ từng bước | **DaVinci YRGB** + **CST** ở node đầu |
| Nhiều máy LOG khác hãng | **DaVinci YRGB Color Managed** |
| Có LUT chính hãng, cần nhanh | **DaVinci YRGB** + LUT chuyển đổi ở node đầu |

> **Đừng chuyển hai lần.** Đã bật Color Managed thì **không** thêm CST hay LUT chuyển đổi nữa — ảnh sẽ bị chuyển chồng, màu sai.
