# Source Tape, Fast Review, Sync Bin

Ba công cụ giúp **xem footage nhanh** — thứ chiếm nhiều thời gian nhất khi dựng.

---

## Source Tape

`★★☆ Thường dùng`

**Là gì:** nối **mọi clip trong bin** thành **một cuộn băng dài liền mạch** trong Viewer. Thay vì mở từng clip một, bạn tua một mạch từ đầu đến cuối.

**Dùng khi:** footage nhiều clip ngắn (quay điện thoại, vlog du lịch) và bạn cần xem hết một lượt để chọn đoạn.

**Cách mở:** bấm **nút thứ 2** trong bốn nút chế độ ở **góc trên trái Viewer**.

**Cách dùng:**
1. Chọn bin chứa footage.
2. Bật Source Tape.
3. Tua bằng `J` `K` `L` (bấm `L` nhiều lần để tua nhanh hơn).
4. Gặp đoạn dùng được: `I`, `O`, rồi bấm một nút edit (thường là **Append**).
5. Tua tiếp.

**Clip đang phát được tô sáng trong Media Pool** — bạn luôn biết mình đang ở clip nào.

**Bấm một clip trong Media Pool** → con trỏ Source Tape nhảy ngay tới khung đầu của clip đó.

### Thứ tự clip trong cuộn băng

Theo cách sắp xếp đang chọn ở Media Pool. Đổi ở menu **Sort Media By** (góc trên Media Pool):

| Sắp theo | Hợp khi |
|---|---|
| **Timecode** / **Date Time** | Footage quay theo trình tự thời gian — vlog, sự kiện |
| **Scene Shot** | Phim có kịch bản, đã gõ metadata cảnh/cú máy |
| **Clip Name** | Tên file đã đặt có ý nghĩa |
| **Camera** | Nhiều máy quay |
| **Custom** | Tự kéo thả sắp xếp |

### Thu hẹp phạm vi cuộn băng

Dự án lớn thì cuộn băng chứa cả bộ phim — quá dài. Thu hẹp lại:

Khi Source Tape đang chạy, **đường dẫn bin** hiện ở **thanh tiêu đề Media Pool** (kiểu `Master › Ngày 1 › Máy A`). **Bấm vào một cấp** trong đường dẫn đó để cuộn băng chỉ còn clip trong bin đó. Bấm `Master` để mở rộng lại.

**Ví dụ:** dự án du lịch 5 ngày, mỗi ngày một bin. Bấm `Ngày 3` là cuộn băng chỉ còn footage ngày 3.

---

## Fast Review

`★☆☆ Tình huống cụ thể`

**Là gì:** phát tua nhanh **có chọn lọc** — clip dài tua rất nhanh, clip ngắn phát gần tốc độ thật.

**Dùng khi:** vừa đổ thẻ xong, muốn xem lướt toàn bộ footage để nắm có những gì. Hoặc xem lại nhanh bản dựng.

**Cách dùng:** bấm nút **Fast Review** ở **thanh dưới đáy Viewer**. Hoạt động trên cả Source Tape lẫn Timeline.

**Vì sao thông minh:** clip quay 5 phút cảnh phong cảnh thì bạn chỉ cần thấy lướt qua. Clip 3 giây quay nhanh khoảnh khắc thì cần thấy rõ. Fast Review tự cân đối cho bạn.

---

## Sync Bin

`★☆☆ Tình huống cụ thể` — nhưng cực mạnh khi đúng tình huống

**Là gì:** khi bạn quay **nhiều máy cùng lúc**, Sync Bin hiện **mọi góc máy tại đúng khoảnh khắc** con trỏ timeline đang đứng. Bạn chỉ cần tua timeline — các góc máy khác tự tua theo.

**Dùng khi:** podcast quay 2–3 máy, phỏng vấn, sự kiện, talkshow, nấu ăn.

### Bước 1 — Chuẩn bị footage

Mỗi clip cần hai thứ:

**Thời gian chung.** Hai cách:
- Máy quay chuyên nghiệp đã **jam-sync timecode** — Resolve tự khớp.
- Không có timecode chung (điện thoại + máy ảnh, đa số người dùng) — dùng **đồng bộ bằng tiếng** ở bước 2.

**Tên máy quay riêng biệt.** Đặt theo chữ (A, B, C) hoặc số (1, 2, 3).
Máy không tự ghi tên thì sửa tay: chọn clip → **Metadata Editor** → trường **Camera #**.

### Bước 2 — Đồng bộ trong Sync Clips window

Mở bằng icon **Sync Clips** ở **trên cùng Media Pool**.

Cửa sổ có Viewer đa góc bên trái, Viewer thường bên phải, và một timeline bên dưới cho thấy các clip xếp theo thời gian.

Bốn nút **Sync By** (từ trái sang phải):

| Nút | Khớp theo | Dùng khi |
|---|---|---|
| **Timecode** | Timecode trong file | Máy chuyên nghiệp đã jam-sync. Mặc định |
| **Audio** | Phân tích tiếng | **Không có timecode chung** — mọi máy đều thu được cùng một tiếng (tiếng nói, tiếng nhạc) |
| **In Point** | Điểm `I` bạn đặt cho từng clip | Có tiếng vỗ tay, clapper, đèn flash ở đầu |
| **Out Point** | Điểm `O` bạn đặt | Có clapper ở cuối |

Chọn kiểu → bấm **Sync** → kiểm tra → bấm **Save Sync** góc dưới phải.

> **Mẹo cho người không có timecode:** trước khi quay, vỗ tay một cái thật to trước mọi máy. Lúc đồng bộ, nếu **Audio** không chạy thì đặt `I` đúng khung vỗ tay ở từng clip rồi dùng **In Point**.

**Đồng bộ tay:** kéo từng clip trên timeline của cửa sổ. Chỉnh từng khung bằng `,` (lùi) và `.` (tiến). Thêm `⇧` để dịch 5 khung một lần.

Lưu xong, một **Multicam clip** mới xuất hiện trong Media Pool. Các clip đã đồng bộ có **icon mũi tên** ở góc trên trái thumbnail.

Sửa lại sau: chuột phải thumbnail → **Open Sync Group**.

### Bước 3 — Dựng

1. Đưa clip của **một máy** xuống timeline làm nền (thường là máy toàn cảnh).
2. Bấm tab **Sync Bin** trên toolbar.
3. Tua timeline. Sync Bin hiện mọi góc máy khác **đúng tại khoảnh khắc đó**.
4. Thấy góc nào đẹp hơn: đặt `I` `O` trên timeline quanh đoạn cần đổi, chọn góc máy đó, bấm **Source Overwrite**.

**Ví dụ thực tế:** podcast 2 người, 3 máy (toàn cảnh, cận người A, cận người B). Đặt máy toàn cảnh xuống timeline. Tua đến chỗ người A nói → chọn cận A → Source Overwrite. Tua đến chỗ người B đáp → chọn cận B → Source Overwrite. Một tiếng podcast dựng xong trong khoảng thời gian bằng hai lần xem lại.
