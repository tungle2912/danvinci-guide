# Metadata Editor

`★★☆ Thường dùng`

**Là gì:** panel hiện và cho gõ **thông tin về clip** — cảnh, take, từ khoá, ghi chú, đánh giá sao.

**Dùng khi:** dự án nhiều clip (phỏng vấn, phim ngắn, sự kiện). Gõ một lần, về sau tìm và lọc clip trong vài giây bằng [Smart Bin](bin.md#3-smart-bin).

**Mở:** bấm nút **Metadata** trên Interface Toolbar. Panel nằm bên phải trang Media. Trang Edit cũng có panel này.

Chọn một clip là metadata của nó hiện ra. **Chọn nhiều clip thì chỉ hiện clip cuối cùng** — nhưng gõ vào thì áp cho cả nhóm.

> Metadata là thông tin **trong project**. File trên ổ không bị sửa.

---

## Phần header — không sửa được

Khối trên cùng hiện thông tin kỹ thuật đọc từ file, chỉ để xem:

- Tên file và đường dẫn thư mục
- Độ dài
- Codec hình, frame rate, độ phân giải
- Codec tiếng, sample rate, số kênh

**Dùng khi:** kiểm tra nhanh một clip có đúng 4K, đúng 25 fps, có tiếng hay không — mà không cần mở cửa sổ nào khác.

**Metadata tự có sẵn:** nhiều file đã mang metadata khi nạp vào. Máy quay Blackmagic ghi thông tin máy và thông tin gõ trên máy. File WAV từ máy thu (Broadcast WAVE) có thể ghi sẵn scene, take, tên từng mic. Ảnh tĩnh mang theo EXIF. Tất cả hiện luôn trong Metadata Editor.

---

## Hai menu thả xuống ở đầu panel

Có **hàng trăm trường metadata**, nên Resolve chia nhóm bằng hai menu:

| Menu | Vị trí | Làm gì | Mức |
|---|---|---|---|
| **Metadata Presets** | Trái | Chọn bộ trường tự tạo của bạn. Mặc định là `Default` | ★☆☆ |
| **Metadata Groups** | Phải | Đổi giữa các nhóm trường có sẵn, chia theo đầu việc | ★★★ |

Mở panel lần đầu, clip hiện nhóm **Clip Details**: timecode đầu/cuối, độ dài, bit depth…

Các nhóm có sẵn gồm **Shot & Scene**, **Clip Details**, **Camera**, **Tech Details**, **Stereo 3D & VFX**, **Audio Trax**, và vài nhóm khác. Chọn **All Groups** để thấy mọi trường cùng lúc.

| Nhóm | Mở khi |
|---|---|
| **Shot & Scene** | Gõ cảnh, cú máy, take, keyword, đánh giá sao — **nhóm dùng nhiều nhất** |
| **Clip Details** | Xem thông số cơ bản của clip |
| **Camera** | Xem thông số máy quay |
| **Custom** | Xem các trường bạn tự tạo |

### Tạo bộ trường riêng (preset)

`★☆☆ Tình huống cụ thể`

**Dùng khi:** chỉ cần 6–7 trường, không muốn cuộn qua cả trăm trường.

1. **DaVinci Resolve → Preferences → User → Metadata** → bấm **New**.
2. Tick từng trường muốn có. Tick tên nhóm để lấy cả nhóm. Rê chuột lên nhóm → bấm **Open** để xem trường bên trong.
3. Bấm **Save** dưới **Metadata Options**.
4. Bấm **Save** của cửa sổ Preferences.

Sửa preset: chọn → **Edit**. Xoá: chọn → **Delete**.

Dùng: chọn preset ở menu **Metadata Presets**, đặt menu nhóm bên phải về **All Groups** để thấy đủ trường của preset.

---

## Những trường đáng gõ

Không cần gõ hết. Những trường này đủ cho hầu hết dự án (đa số nằm trong nhóm **Shot & Scene**):

| Trường | Gõ gì | Dùng để | Mức |
|---|---|---|---|
| **Scene** | Số cảnh | Nhóm các take cùng cảnh | ★★☆ |
| **Shot** | Số cú máy | | ★★☆ |
| **Take** | Số lần quay | | ★★☆ |
| **Good Take** | Tick nếu dùng được | Lọc nhanh bằng Smart Bin | ★★★ |
| **Keywords** | Từ khoá — xem mục dưới | Điều kiện cho Smart Bin | ★★★ |
| **Description** | Ghi chú tự do | "out nét ở giây 12", "có tiếng xe" | ★★☆ |
| **Comments** | Ghi chú thêm | Nhắn cho người dựng cùng | ★☆☆ |
| **Rating** | 1–5 sao | Xếp hạng take | ★★☆ |

### Đánh giá sao

`★★☆ Thường dùng`

Trong nhóm **Shot & Scene**, bấm vào sao để chấm 1 tới 5. Bấm lại để đổi.

**Dùng:** tạo Smart Bin điều kiện **Rating** ≥ 4 sao → có ngay bin "take hay nhất".

### Gõ keyword — dạng thẻ

`★★★ Hằng ngày` với dự án nhiều clip.

Ô **Keywords** khác các ô khác: mỗi từ khoá thành một **thẻ** có nền. Cách này giúp gõ thống nhất, không mỗi lần viết một kiểu.

| Việc | Cách làm |
|---|---|
| Thêm keyword | Bấm vào ô **Keywords**, gõ vài chữ → danh sách gợi ý hiện ra (keyword có sẵn và keyword bạn đã dùng). Chọn bằng `↑` `↓`, bấm `Return` |
| Sửa keyword | **Bấm đúp** thẻ → sửa → `Return` |
| Xoá keyword | Bấm thẻ để chọn → `Delete` |

> **Dùng tag màu của Finder:** bật **Preferences → User → Editing → Import Finder tags as Keywords**. Tag màu bạn gắn trong Finder sẽ thành keyword khi nạp file.

---

## Gõ cho nhiều clip một lúc

`★★★ Hằng ngày`

1. Chọn nhóm trường ở menu **Metadata Groups** (ví dụ **Shot & Scene**).
2. Chọn nhiều clip trong Media Pool: `⇧`-click, `⌘`-click, hoặc kéo khung.
3. Gõ vào trường cần. Trường nào bạn sửa sẽ **tự được tick**.
4. Bấm **Save** (đáy panel).

Cả nhóm nhận cùng giá trị. Quên bấm **Save** mà chọn clip khác thì Resolve hỏi có lưu không.

> Gõ **một clip** thì không cần bấm Save — sửa xong là lưu ngay.

**Ví dụ — 40 clip quay ở quán cà phê:** chọn cả 40 → **Keywords** gõ `quán-cafe` → **Save**. Xong chọn riêng 12 clip có nhân vật An → thêm keyword `an` → **Save**.

> **Thứ tự nên làm:** gõ cho **nhóm** trước (cảnh, địa điểm, nhân vật), rồi mới gõ **từng clip** (take, mô tả hành động).

---

## Sửa nhanh ngay trong Media Pool

`★★☆ Thường dùng`

Không cần mở Metadata Editor cho các trường hay dùng. Chuyển Media Pool sang **List view**, bốn cột này **gõ thẳng được**:

- **Name** (Clip Name)
- **Description**
- **Keyword**
- **Comments**

**Cách gõ:** bấm một lần vào ô của clip, **chờ một nhịp**, bấm lần nữa → ô mở ra cho gõ.

Hiện cột: chuột phải vào tiêu đề cột → tick cột cần.

### Nhập liệu nhanh bằng Inspector — tab File

`★★☆ Thường dùng`

Bật **Inspector** → tab **File**. Ở đây có bộ trường rút gọn: **Timecode**, **Date Created**, **Camera**, **Reel**, **Scene**, **Shot**, **Take**, **Good Take**, **Clip Color**, **Name**, **Comments**.

**Auto Select Next Unsorted Clip:** tick ô này thì gõ xong bấm `Return` là Resolve **tự nhảy sang clip kế tiếp**, con trỏ đứng sẵn ở đúng ô đó. Gõ take cho 50 clip liền một mạch, không cần cầm chuột.

Nút **Next Clip** chuyển sang clip kế, dù ô trên có tick hay không.

---

## Tự tạo trường metadata

`★☆☆ Tình huống cụ thể`

**Dùng khi:** cần trường mà Resolve không có, ví dụ "Khách duyệt", "Mã sản phẩm".

1. Mở menu ba chấm của panel Metadata → **Create Custom Metadata**.
2. Đặt tên trường, chọn kiểu, chọn có **hiện ở mọi project** hay không.
3. Lặp lại cho trường khác.

| Kiểu trường | Dùng cho |
|---|---|
| **Text Input** | Một dòng chữ |
| **Text Area** | Nhiều dòng |
| **Numeric** | Số |
| **Timecode** | Một mốc timecode |
| **Checkbox** | Bật/tắt |

Xem các trường này: menu nhóm bên phải → **Custom**. Sắp xếp, sửa, xoá: menu ba chấm → **Manage Custom Metadata**.

Trường tự tạo dùng được làm điều kiện Smart Bin như trường có sẵn.

---

## Xuất và nhập metadata

`★☆☆ Tình huống cụ thể`

**Dùng khi:** người khác đã gõ metadata trong project của họ, bạn muốn lấy sang project mình mà không gõ lại.

**Xuất:**

1. Mở project có metadata. Muốn xuất một phần thì chọn clip trước.
2. **File → Export Metadata From → Media Pool** (mọi clip) hoặc **→ Selected Clips**.
3. Đặt tên, chọn chỗ lưu → **Save**. Ra file `.csv` (mở bằng Excel, Numbers) hoặc `.ale` (cho Avid).

**Nhập:**

1. Mở project đích.
2. **File → Import Metadata To → Media Pool** hoặc **→ Selected Clips**.
3. Chọn file `.csv` hoặc `.ale` → **Open**.
4. Chọn cách khớp clip. Mặc định khớp theo **tên file** và **timecode đầu/cuối**.
5. Chọn cách gộp → **OK**.

| Cách gộp | Nghĩa là |
|---|---|
| **Only update metadata items with entries in the source file** | Mặc định. Chỉ ghi các ô có giá trị trong file. An toàn nhất |
| **Update all metadata fields available in the source file** | Ghi đè mọi trường có trong file, kể cả ô trống |
| **… and clear others** | Như trên, và **xoá** các trường không có trong file |

> Muốn gõ hàng loạt bằng bảng tính: xuất ra `.csv`, gõ trong Excel, rồi nhập lại.

---

## Metadata bằng AI

`Studio`

Các công cụ này dùng DaVinci Neural Engine. Bản free không có.

| Công cụ | Làm gì |
|---|---|
| **Slate ID** | Nút trên cùng panel Metadata. Đọc chữ trên bảng clapper, tự điền Scene, Take, ngày, camera. Cần chạy **Analyze for Slate** trước |
| **Audio Classification** | Nghe tiếng clip, gán loại: Dialogue, Effect, Music, Silence |
| **Analyze clips for people** | Nhận diện khuôn mặt, tạo keyword theo người |
| **Transcription** | Chép lời thoại thành chữ |

Chạy từ: chuột phải clip → **AI Tools**, hoặc nút **AI Clip Analysis** trên Media Pool.

---

## Vì sao nên bỏ công gõ

Metadata là thứ làm [Smart Bin](bin.md#3-smart-bin) chạy được. Không có metadata thì Smart Bin chỉ lọc được theo thông số kỹ thuật.

Gõ đủ thì bạn có những bin kiểu "mọi cú cận của An trong quán" hay "mọi b-roll quay ngoài trời" chỉ bằng vài điều kiện.

Với dự án dưới 20 clip thì không cần. Với dự án phỏng vấn 200 clip thì nửa giờ gõ keyword tiết kiệm nhiều giờ tìm kiếm về sau.

> Gõ metadata **trước** khi bắt tay dựng. Đang dựng dở thì không ai muốn quay lại gõ.

---

## Mẹo: quy ước keyword

Đặt quy ước trước khi gõ, nếu không keyword sẽ loạn. Nửa số clip gõ `quán`, nửa kia gõ `nhà-hàng` thì tìm không ra đủ.

```
nhân vật:  an, binh, chi
loại:      phỏng-vấn, b-roll, cận, toàn
chất:      tốt, tạm, hỏng
```

Rồi tạo Smart Bin cho từng tổ hợp hay dùng.

> **Gắn keyword hàng loạt bằng kéo thả:** chọn nhiều clip, kéo lên một Smart Bin tự tạo trong nhóm **Keywords**. Xem [Smart Bin tự tạo](bin.md#smart-bin-tự-tạo).
