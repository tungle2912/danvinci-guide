# Phụ đề — subtitle track

Resolve có **track phụ đề riêng**, khác track hình. Mỗi track phụ đề thường là **một ngôn ngữ**. Phụ đề trên track này xuất được **thành file `.srt`** hoặc **in thẳng vào hình**.

| Cách | Bản free? | Hợp với |
|---|---|---|
| Gõ tay từng câu | Có | Video ngắn, ít lời |
| Nhập file `.srt` làm sẵn ở nơi khác | Có | Video dài, đã có bản dịch |
| **Create Subtitles from Audio** — AI tự nghe và gõ | `Studio` | Mọi video có lời |

> **Phụ đề hay chữ Text+?** Phụ đề: nhiều câu, nằm dưới đáy, xuất được file riêng, gõ nhanh. Text+: vài dòng chữ to, cần hiệu ứng, đặt bất cứ đâu — xem [Chữ](chu-va-hieu-ung.md#chữ--text-text).

---

## Thêm track phụ đề

`★★★ Hằng ngày`

Chuột phải vào **đầu track** bất kỳ → **Add Subtitle Track**.

Track **Subtitle 1** hiện ở **trên cùng** timeline. Đầu track có ô đích **ST1**, khoá, Sync Lock, và nút bật/tắt.

**Đổi tên track ngay:** bấm đúp tên → gõ tên ngôn ngữ, ví dụ `Tieng Viet`, `English`. **Tên track được dùng làm tên file** khi xuất phụ đề.

| Nên biết | |
|---|---|
| Nhiều ngôn ngữ | Mỗi ngôn ngữ một track |
| Chỉ **một** track phụ đề hiện trên hình | Bật track này là các track phụ đề khác tự tắt |
| Ẩn vùng track phụ đề cho gọn | **Timeline View Options** → nút **Subtitle** |

Ẩn vùng track **không tắt** phụ đề trên hình. Muốn tắt thì bấm nút tắt ở đầu track.

---

## Gõ phụ đề tay

`★★★ Hằng ngày`

### Cách làm

1. Có nhiều track phụ đề: bấm ô **ST1** (hoặc ST2…) của track cần thêm.
2. Đặt con trỏ ở **khung người nói bắt đầu câu**.
3. Thêm một câu phụ đề — chọn một trong:
   - Chuột phải lên track phụ đề → **Add Subtitle**.
   - Inspector → tab **Captions** → **Create Caption** (lần đầu) hoặc **Add New** (từ câu thứ hai).
   - **Effects → Titles** → kéo **Subtitle** thả vào track phụ đề.
4. Clip phụ đề đang được chọn → gõ nội dung vào ô chữ trong tab **Captions** của Inspector.
5. Kéo hai mép clip phụ đề cho **khớp lúc bắt đầu và hết câu**.

Mọi câu đã gõ hiện thành **danh sách** ở cuối tab Captions. Nút **Prev** / **Next** để đi qua từng câu. Bấm một câu là nhảy tới và sửa được ngay.

### Gõ nhanh cả video

1. Phát tới câu đầu, dừng (`K`), thêm phụ đề, gõ.
2. Kéo mép phải clip phụ đề tới hết câu.
3. Phát tiếp tới câu sau. Lặp lại.

> **Nghe được chỗ hết câu:** nới cao track tiếng lời và bật dạng sóng — chỗ sóng phẳng là lúc ngừng nói.

### Sửa clip phụ đề

Clip phụ đề sửa như clip thường: kéo dời, kéo mép, cắt bằng `B`, trim ở chế độ `T`, nudge bằng `,` `.`.

**Hiện/ẩn mượt:** clip phụ đề có **tay nắm fade** ở hai góc như clip hình.

### Kiểm tra độ dài câu

**Project Settings → Subtitles** có ba ngưỡng:

| Ngưỡng | Ý nghĩa |
|---|---|
| **Max characters per line** | Số ký tự tối đa một dòng |
| **Min duration** | Câu phải hiện ít nhất bao lâu |
| **Max CPS** | Số ký tự mỗi giây tối đa — vượt là người xem đọc không kịp |

Câu nào **đọc không kịp** thì chỉ số CPS của câu đó **chuyển đỏ**. Kéo dài clip ra hoặc rút gọn câu.

Mỗi track đặt ngưỡng riêng: chọn đầu track → Inspector → tab **Track** → bỏ tick **Use Project Settings**.

### Tìm và thay chữ

Bấm **kính lúp** ở góc trên phải Inspector phụ đề. Gõ từ cần tìm → **Search**. Bật **Replace**, gõ từ mới → **Replace** (một chỗ) hoặc **Replace All** (cả track).

**Dùng khi:** gõ sai tên người suốt cả video.

---

## Nhập file .srt

`★★☆ Thường dùng`

Resolve đọc được `.srt`, `.srtx`, `.vtt`, `.xml`, `.ttml`.

### Cách làm

1. Chuột phải nền Media Pool → **Import Subtitle** → chọn file. File hiện trong Media Pool với badge phụ đề.
2. Đưa xuống timeline — chọn một trong:

| Cách | Khi nào |
|---|---|
| Chuột phải file → **Insert Selected Subtitles to Timeline Using Timecode** | File `.srt` làm **từ chính bản dựng này** — timecode khớp sẵn |
| Kéo file thả vào **vùng xám trên track hình cao nhất** | Tự tạo track phụ đề mới |
| Kéo file thả vào track phụ đề có sẵn | Thêm vào track đó |

Khi kéo, file **tự tách** thành từng câu riêng. Câu đầu nằm chỗ bạn thả.

3. Lệch giờ? Chọn hết các câu (quét chuột) rồi kéo sớm/muộn cả khối.

**Ví dụ:** gửi video cho người dịch, nhận lại file `en.srt`. Thêm track `English`, nhập file, dùng **Insert … Using Timecode**.

> Timecode trong file `.srt` thường bắt đầu từ `00:00:00`, còn timeline Resolve mặc định bắt đầu `01:00:00:00`. Nếu **Using Timecode** không khớp, dùng cách kéo thả rồi căn câu đầu cho đúng.

---

## Kiểu chữ phụ đề

`★★☆ Thường dùng`

### Cho cả track

1. Bấm **đầu track** phụ đề (hoặc chọn một câu bất kỳ trên track).
2. Inspector → tab **Track**.
3. Chỉnh:

| Nhóm | Gồm |
|---|---|
| **Style** | Font, kiểu chữ, màu, cỡ, giãn dòng, giãn chữ, căn lề |
| **Position** | Vị trí X Y, Zoom, Opacity, điểm neo chữ |
| **Drop Shadow** | Bóng đổ |
| **Stroke** | Viền chữ |
| **Background** | Nền sau chữ |

**Phụ đề luôn đọc được:** chữ trắng + **Stroke** đen mỏng, hoặc **Background** đen mờ.

> Chọn font **có đủ dấu tiếng Việt**. Font thiếu dấu sẽ hiện ô vuông hoặc dấu lệch — kiểm tra bằng câu có chữ `ặ`, `ỡ`, `ự`.

### Cho một câu, một chữ

Chọn câu → tab **Captions** → tick **Customize Caption**. Chỉnh kiểu chỉ cho câu đó. Bôi đen vài chữ trong ô nội dung rồi chỉnh — chỉ những chữ đó đổi.

**Dùng khi:** tô vàng một từ khoá, in nghiêng tên bài hát.

### Lưu kiểu để dùng lại

Menu **⋯** góc trên phải Inspector phụ đề → **Save Track as Preset**. Lần sau: chọn track → **⋯** → tên preset → **Load Preset**. Có **Export Preset** / **Import Preset** để mang sang máy khác.

### Kiểu bằng mẫu Fusion

Kéo một **mẫu chữ Fusion** từ Effects thả lên **đầu track phụ đề** — cả track đổi theo mẫu đó, đè lên kiểu trong Inspector.

**AI Animated Subtitles** (chữ sáng lên theo từng từ đang nói) là `Studio`.

### Hai câu cùng lúc — Subtitle Region

`★☆☆ Tình huống cụ thể`

Hai người nói chồng lên nhau, muốn hiện hai câu cùng lúc ở hai vị trí:

1. Chuột phải **trong** track phụ đề (không phải đầu track) → **Add Subtitle Region**. Track chia làm hai tầng R1, R2.
2. Mỗi region có kiểu và vị trí riêng — đặt R2 lệch sang phải chẳng hạn.
3. Kéo câu lên/xuống để đổi region.

Tối đa 3 region mỗi track.

### Gắn phụ đề theo clip

Chọn clip hình và các câu phụ đề của nó → **Clip → Linked Clips** (`⌥⌘L`). Dời clip là phụ đề đi theo.

**Dùng khi:** đổi thứ tự các đoạn phỏng vấn sau khi đã gõ phụ đề.

---

## Create Subtitles from Audio — AI tự tạo

`Studio`

**Là gì:** Resolve nghe lời nói trên timeline và tự tạo track phụ đề có dấu câu, viết hoa tên riêng.

**Ở đâu:** **Timeline → AI Tools → Create Subtitles from Audio**.

**Tuỳ chọn:** Language, Caption Preset, Max Characters per Line, Lines (một hay hai dòng), Gap Between Subtitles.

**Tiếng Việt:** không có sẵn — phải tải thêm **Extended AI Transcription Support Package** từ trình quản lý tải thêm của Resolve.

> **Bản free không có tính năng này.** Cách thay thế: tạo file `.srt` bằng công cụ chuyển giọng nói thành chữ khác, rồi [nhập vào](#nhập-file-srt). Sửa lỗi chính tả bằng [Tìm và thay chữ](#tìm-và-thay-chữ).

---

## Xuất phụ đề

`★★★ Hằng ngày`

### Ra file riêng — từ trang Edit

| Cách | Định dạng |
|---|---|
| **File → Export Subtitle** | `.srt`, `.vtt` |
| Chuột phải đầu track phụ đề → **Export Subtitle** | `.srt`, `.vtt` |

### Lúc render — trang Deliver

Ở [Deliver](../deliver/cai-dat-xuat.md#subtitle-settings), tab **Video**, cuối danh sách có nhóm **Subtitle Settings**:

1. Tick **Export Subtitle**.
2. Chọn **Format**:

| Format | Kết quả | Hợp với |
|---|---|---|
| **Burn into video** | Chữ **in thẳng vào hình**, không tắt được | TikTok, Reels, Shorts, video chạy tự động không tiếng |
| **As a separate file** | File phụ đề **đi kèm** video. Chọn **Export As**: SRT, WebVTT, IMSC1, DFXP. Tick chọn track nào xuất | YouTube (tải `.srt` lên riêng), nhiều ngôn ngữ |
| **As embedded captions** | Nhúng phụ đề vào trong file video (MXF OP1A, QuickTime) | Giao cho đài truyền hình |

**Burn into video** chỉ in **track phụ đề đang bật**. Muốn xuất ba bản ba ngôn ngữ in sẵn: bật track 1 → render → bật track 2 → render…

> **YouTube:** xuất `.srt` riêng rồi tải lên cùng video thường tốt hơn in vào hình — người xem bật/tắt được, chọn được ngôn ngữ.
