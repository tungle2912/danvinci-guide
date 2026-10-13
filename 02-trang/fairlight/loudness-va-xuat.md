# Loudness và kiểm tra trước khi xuất

Bước cuối của mix: bản mix **đủ to** so với chuẩn nền tảng, và **không bao giờ vượt trần**. Hai thứ này đo bằng hai đồng hồ khác nhau.

| Câu hỏi | Xem đồng hồ | Đơn vị |
|---|---|---|
| Có bị rè, vượt trần không? | **Control Room** — số **TP** (true peak) | dBFS |
| Nghe có đủ to như video khác không? | **Loudness** — số **Integrated** | LUFS |

Bật cả hai: nút **Meters** góc trên phải.

---

## Mức to cuối cùng

`★★★ Hằng ngày`

| Thứ | Mức |
|---|---|
| Lời thoại | khoảng −12 dB trên đồng hồ track |
| Nhạc nền dưới lời | khoảng −20 đến −25 dB |
| Đỉnh tổng — không được vượt | −1 dBTP |
| Độ to tổng cho YouTube (**Integrated**) | khoảng −14 LUFS |

Con số −14 LUFS cho YouTube có trong manual. Hai mức lời và nhạc là điểm xuất phát hay dùng, không phải quy định — tai bạn quyết định cuối cùng.

---

## Loudness meter — đo độ to cảm nhận

`★★★ Hằng ngày`

**Là gì:** đồng hồ ngoài cùng bên phải của dải Meters. Không đo đỉnh sóng mà đo **độ to tai người cảm nhận**, theo đơn vị LUFS. Đây là thứ YouTube, Netflix, đài truyền hình dùng để quy định độ to.

LUFS luôn là số âm: −14 to hơn −23.

**Các ô số:**

| Ô | Nghĩa | Dùng để |
|---|---|---|
| **M** (cột đồng hồ) | Độ to tức thời, khung 400 ms | Nhìn chỗ nào bỗng to vọt |
| **Short** | Độ to trung bình gần đây | Theo dõi khi đang phát |
| **Short Max** | Mức Short cao nhất | Soát đoạn to nhất |
| **Range** | Chênh lệch giữa đoạn nhỏ và đoạn to | Bản mix có quá "nhấp nhô" không |
| **Integrated** | Độ to **trung bình của cả phần đã phát** | **Con số chính** để so với chuẩn |

Màu của số **Integrated**: **xanh dương** là nhỏ hơn chuẩn, **vàng** là trong chuẩn, **đỏ** là to hơn chuẩn.

### Đặt chuẩn YouTube

Mặc định meter đo theo chuẩn **−23 LUFS** (chuẩn phát sóng châu Âu). Làm video cho YouTube thì đổi:

1. Bấm menu **ba chấm** góc trên phải Loudness meter.
2. Chọn **YouTube** trong danh sách chuẩn. Danh sách còn có **EBU R128**, **ATSC A/85**, **NETFLIX**...
3. Tick **Absolute Scale** để meter hiện số LUFS thật (−14) thay vì số tương đối (0).

> **Tương đối và tuyệt đối:** mặc định meter hiện **thang tương đối** — số **0** nghĩa là "đúng chuẩn đang chọn". Bật **Absolute Scale** thì thấy luôn số LUFS.

**Đặt mức đích cho cả project:** **Project Settings → Fairlight → Audio Metering → Target Loudness level**. Mặc định −23 LUFS. Đặt −14 thì vạch "0" trên meter dời về −14 LUFS.

### Đo cả video

Số **Integrated** chỉ tính **phần bạn đã phát**. Muốn đo cả video:

1. Đưa con trỏ về đầu timeline.
2. Bấm **Reset** dưới Loudness meter.
3. Phát từ đầu đến cuối, không tua.
4. Đọc số **Integrated** lúc kết thúc.

Bấm **Pause** để tạm dừng đo, bấm lại để đo tiếp.

> **Lock Metering to Transport** (trong menu ba chấm): bật thì mỗi lần nhảy con trỏ sang chỗ khác, kết quả tự xoá. Tiện khi soát từng đoạn. Tắt đi khi muốn đo cộng dồn.

### Đo nhanh không cần phát

`★★☆ Thường dùng`

Chuột phải một clip trên timeline → **Analyze Audio Level** → chọn chuẩn đo → bấm phân tích. Kết quả hiện cạnh mức đích của chuẩn đó.

**Dùng khi:** muốn biết một file nhạc, hoặc một bản mix đã bounce ra, to cỡ nào mà không phải ngồi nghe hết.

---

## Control Room — đỉnh true peak

`★★★ Hằng ngày`

Đồng hồ màu **vàng mù tạt**, cạnh Loudness meter. Hiện tổng của bus đang nghe (mặc định **Bus 1**), đo đỉnh theo dBFS.

Số **TP** trên đầu là **true peak** — đỉnh thật, tính cả đỉnh nằm giữa hai mẫu số. Giữ số này **dưới −1**.

> Đỉnh vượt 0 là bị rè khi xuất. Nén sang AAC hay MP3 còn làm đỉnh nhích lên thêm, nên chừa khoảng 1 dB.

---

## Limiter trên Bus — chặn trần

`★★☆ Thường dùng`

**Là gì:** Fairlight FX **Limiter** chặn mọi đỉnh vượt ngưỡng. Đây là limiter **true peak**, nhìn trước 64 mẫu nên chặn mượt.

**Dùng khi:** luôn đặt ở **Bus 1** trước khi xuất, như một lớp bảo hiểm.

**Cách làm:**
1. Mở **Mixer**, tìm cột **Bus 1** (cột cuối).
2. Bấm **+** ở mục **Effects** → chọn **Limiter**.
3. Đặt **Ceiling** −1 dB.
4. Phát đoạn to nhất. Nhìn **Reduction Meter** — chỉ nên nhích nhẹ ở các đỉnh.

| Thanh | Làm gì |
|---|---|
| **Input Level** | Đẩy mức vào, −18 đến +18 dB. Nút **Soft** cho chặn mềm hơn |
| **Ceiling** | Ngưỡng chặn. 0 dB là không chặn gì |
| **Release** | Thôi chặn nhanh hay chậm, 0.01 đến 1000 ms |
| **Reduction Meter** | Đang bị chặn bao nhiêu |

> **Limiter không thay được việc cân mix.** Nếu Reduction Meter nhảy liên tục vài dB, bản mix đang quá to — hạ fader các track xuống thay vì để limiter ép.

**Bản mix nhỏ quá (Integrated dưới −14 nhiều)?** Tăng **Input Level** của Limiter từng chút, đo lại Integrated. Giữ Ceiling −1 dB.

---

## Kiểm tra trước khi sang Deliver

`★★★ Hằng ngày`

| Kiểm tra | Ở đâu |
|---|---|
| Không track nào đang bật **Solo** | Nút **S** ở đầu track. Solo và Mute ảnh hưởng cả file xuất |
| Không track nào bị **Mute** nhầm | Nút **M** ở đầu track |
| **TP** trên Control Room dưới −1 | Dải Meters |
| **Integrated** quanh −14 LUFS (YouTube) | Loudness meter, đo cả video từ đầu |
| Nhạc không lấn lời ở mọi đoạn | Nghe lại bằng tai nghe, rồi bằng loa điện thoại |
| Thanh âm lượng nghe (cạnh nút loa) và nút **DIM** | Chỉ ảnh hưởng tiếng ra loa, không ảnh hưởng file xuất — nhưng nhớ trả về để nghe đúng |

Xong thì sang trang Deliver, xem [Tab Audio](../deliver/cai-dat-xuat.md#tab-audio) để chọn codec và bitrate tiếng.

> **Nghe trên điện thoại:** phần lớn người xem nghe bằng loa điện thoại. Lời rõ trên loa điện thoại thì gần như chắc chắn rõ ở mọi nơi.
