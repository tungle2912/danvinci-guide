# Mixer, Track FX, Normalize, Ducker, Bus

Ba công cụ "tự mix" hữu ích nhất — **Normalize**, **Dialogue Leveler**, **Ducker** — đều có ở bản free. Học ba cái này trước là cân được tiếng cho phần lớn video.

Thứ tự nên làm: **Normalize** clip → **Dialogue Leveler** trên track lời → **Ducker** trên track nhạc → kéo **fader** cân lần cuối.

---

## Normalize — cân đều các clip

`★★★ Hằng ngày` · Làm **đầu tiên**

**Là gì:** lệnh tự đổi âm lượng các clip đang chọn về một mức đích. Chỉ đổi âm lượng, không nén hay xử lý gì thêm.

**Dùng khi:** các clip lời thu ở những lúc khác nhau, to nhỏ không đều. Hoặc trước khi bật Dialogue Leveler.

**Cách làm:**
1. Chọn các clip tiếng trên timeline → chuột phải → **Normalize Audio Levels**.
2. **Normalization Mode:** chọn một chuẩn đo **loudness** (đo độ to **cảm nhận**, hợp để cân các clip với nhau) — hoặc **Sample Peak** / **True Peak** (chỉ đo đỉnh sóng).
3. Đặt mức đích.
4. **Set Level:**

| Chọn | Kết quả | Dùng khi |
|---|---|---|
| **Relative** | Cả nhóm chỉnh **cùng một lượng**, giữ chênh lệch tự nhiên giữa các clip | Lời thoại thu cùng một mic |
| **Independent** | **Mỗi clip chỉnh riêng** để bằng nhau | Tiếng động, nhạc từ nhiều nguồn khác nhau |

Lệnh này có cả ở trang Edit.

**Ví dụ:** vlog quay ba buổi, buổi thứ hai đứng xa máy nên tiếng nhỏ hẳn. Chọn hết clip lời → Normalize → **Independent** để kéo buổi thứ hai lên ngang hai buổi kia. Nếu cả ba buổi to nhỏ gần nhau rồi thì dùng **Relative**.

### Level Matcher — khớp mức theo một clip mẫu

`★☆☆ Tình huống cụ thể`

Khi muốn các clip to **bằng đúng một clip mẫu** thay vì bằng một con số:

1. Chuột phải clip mẫu → **Clip Operations → Level Matching → Capture Level Profile**.
2. Chuột phải clip cần chỉnh → **Clip Operations → Level Matching → Apply Level Profile**. Lặp lại cho từng clip.

---

## Cột kênh trong Mixer

`★★★ Hằng ngày`

Bật Mixer: nút **Mixer** góc trên phải. Mỗi track một cột, bus nằm ở các cột cuối.

Trong [ảnh chụp trang Fairlight](../../assets/img/page-fairlight.png) có ba cột: **A1** (Giong noi), **A2** (Nhac nen), **Bus1**.

Từ trên xuống:

| Mục | Làm gì | Mức |
|---|---|---|
| **Input** | Chọn nguồn thu cho track (mic, cổng vào). Mặc định **No Input** | ★★☆ |
| **Track FX** | Ô có sẵn cho Dialogue Leveler, Ducker và các Track FX khác. Mặc định hiện **Dial Lev** | ★★★ |
| **Order** | Thứ tự xử lý của Effects, Dynamics, EQ. Mặc định **FX DY EQ** | ★☆☆ |
| **Effects** | Bấm **+** để gắn hiệu ứng cho **cả track** | ★★☆ |
| **Effects In** | Tắt/bật **mọi** hiệu ứng ở mục Effects cùng lúc. Không ảnh hưởng Track FX, Dynamics, EQ | ★★☆ |
| **Dynamics** | Bấm đúp để mở nén, chặn, cổng — xem [Dynamics](lam-sach-giong.md#dynamics--nén-chặn-cổng) | ★★☆ |
| **EQ** | Bấm đúp để mở EQ 6 dải — xem [EQ](lam-sach-giong.md#eq--3-thao-tác-cho-giọng-nói) | ★★☆ |
| **Bus Sends** | Gửi thêm một phần tín hiệu sang bus khác. Cần ít nhất hai bus | ★☆☆ |
| **Pan** | Trái phải. Kéo trong ô, hoặc bấm đúp để mở cửa sổ pan | ★★☆ |
| **Tên track** | Bấm đúp để đổi tên | ★★☆ |
| **R S M** | Thu, Solo, Mute — giống nút ở đầu track | ★★★ |
| **Automation** | Bật ghi automation riêng cho track — xem [Automation](thu-am-va-chinh-clip.md#automation--to-nhỏ-theo-thời-gian-cho-cả-track) | ★☆☆ |
| **Fader** | Kéo để chỉnh to nhỏ cả track | ★★★ |

**Fader:**
- Bấm đúp vào núm fader → về **0 dB**.
- Giữ `⇧` khi kéo → chỉnh mịn từng 0,1 dB.

> **Không thấy mục nào đó?** Menu **ba chấm** góc trên phải Mixer → bật mục đó lên. Bật **Show Labels** để hiện tên các mục bên trái.

**Gắn hiệu ứng cho cả track** — ba cách:
- Bấm **+** ở mục **Effects** trong cột → chọn hiệu ứng.
- Kéo hiệu ứng từ panel **Effects** thả lên **đầu track** trên timeline.
- Kéo hiệu ứng thả vào cột trong Mixer.

Rê chuột lên tên hiệu ứng trong cột để hiện nút bật/tắt, mở bảng chỉnh, thay hoặc xoá.

**Copy cài đặt:** chuột phải **số track** trên đầu cột để copy/paste cả cột sang track khác. Giữ `⌥` kéo một hiệu ứng sang cột khác để copy riêng hiệu ứng đó.

---

## Track FX — ba công cụ "tự mix"

Nằm ở mục **Track FX** của từng cột trong Mixer. Cũng chỉnh được ở **Inspector → tab Audio** khi chọn track (bấm **Track Mode**).

| Track FX | Làm gì | Mức |
|---|---|---|
| **Dialogue Leveler** | Giọng đều, không cần chỉnh tay | ★★★ |
| **Ducker** | Nhạc tự nhỏ khi có lời | ★★★ |
| **Voice Isolation** | Tách giọng khỏi tiếng ồn bằng AI | `Studio` |
| **Dialogue Separator** | Chỉnh riêng giọng, nền, tiếng vang phòng | `Studio` |
| **Music Remixer** | Tách nhạc thành giọng hát, trống, bass, guitar, còn lại | `Studio` |

Mặc định chỉ **Voice Isolation** và **Dialogue Leveler** hiện ra.

- Không thấy mục Track FX: menu **ba chấm** góc trên phải Mixer → tick **Track FX**.
- Không thấy Ducker: menu ba chấm → **Visible Track FX** → tick **Ducker**.

---

## Dialogue Leveler — giọng đều không cần chỉnh tay

`★★★ Hằng ngày`

**Là gì:** tự **kéo xuống** chỗ nói to, **nâng lên** chỗ nói nhỏ, **hạ** tiếng nền không phải giọng nói. Không bị hiện tượng "bơm" lên xuống như máy nén.

**Dùng khi:** người nói lúc gần lúc xa mic, quay đầu đi chỗ khác, hai người nói chung một mic.

**Cách làm:**
1. Normalize các clip lời trước — manual khuyên làm vậy để có mức nền tốt.
2. Ở cột track lời, mục **Track FX**, bấm vào ô **Dial Lev** để mở bảng.
3. Bật plugin, chọn preset, tick các tuỳ chọn:

| Mục | Đặt |
|---|---|
| **Preset** | **Allow wider dynamics** (mặc định) · **More lift for low levels** khi nhiều chỗ nói nhỏ · **Lift soft whispery sources** khi nói thì thầm · **Optimize moderate levels** khi giọng đều ở mức vừa |
| **Lift Soft Dialogue** | Bật — manual đánh giá là tuỳ chọn **hữu ích nhất** trong ba cái |
| **Reduce Loud Dialogue** | Bật nếu có chỗ hét to |
| **Background Reduction** | Bật để giảm nhẹ tiếng nền |
| **Output Gain** | Nâng mức ra, từ 0 đến +6 dB |

**Giới hạn:** chỉ dùng cho track mono, stereo hoặc dual-mono. Không dùng cho tiếng đang thu trực tiếp.

**Chỉ một đoạn cần?** Chọn clip → **Inspector → tab Audio** → mục **Dialogue Leveler** của clip.

**Ví dụ:** phỏng vấn hai người ngồi chung một mic. Người gần mic to, người xa nhỏ. Bật Dialogue Leveler, preset **More lift for low levels**, tick **Lift Soft Dialogue** — giọng người xa được nâng lên mà không cần kéo gain từng câu.

---

## Ducker — nhạc tự nhỏ khi có lời

`★★★ Hằng ngày`

**Là gì:** gắn vào **track nhạc**, chọn **track lời** làm nguồn. Mỗi khi có người nói, nhạc tự nhỏ xuống; im lặng thì nhạc to lại. Không nén tiếng.

**Dùng khi:** vlog, video hướng dẫn, podcast có nhạc nền chạy suốt.

**Cách làm:**
1. Bật Ducker trên **track nhạc** (track cần nhỏ đi).
2. **Source:** chọn track lời. Nhiều người nói ở nhiều track: `⌘` + click thêm tên track.
3. Phát thử, chỉnh:

| Thanh | Làm gì | Mặc định | Gợi ý |
|---|---|---|---|
| **Duck Amount** | Nhạc nhỏ đi bao nhiêu dB | 2.7 dB | **2–5 dB** là hợp đa số trường hợp |
| **Lookahead** | Bắt đầu nhỏ đi **trước** khi có lời | 15 ms | Giữ mặc định |
| **Rise Time** | Nhỏ đi nhanh cỡ nào | 10 ms | Giữ mặc định |
| **Hold** | Giữ ở mức nhỏ bao lâu | 150 ms | Tăng nếu nhạc to lên giữa các từ |
| **Recovery Time** | To trở lại chậm cỡ nào | 750 ms | Chỉnh thử — quyết định độ tự nhiên |

**Thêm nguồn trong Inspector:** chọn track nhạc → **Inspector → tab Audio** → bấm **+** bên phải ô **Source 1** để có thêm **Source 2**, **Source 3**.

Đồ thị trong bảng Ducker: đường **xám** là tín hiệu nguồn, đường **vàng** là mức nhạc. Chỗ đường vàng trũng xuống là chỗ nhạc đang bị hạ.

**Ví dụ:** vlog có lời ở A1, nhạc ở A2. Bật Ducker ở A2, Source chọn A1, Duck Amount 4 dB. Nghe thấy nhạc "nhảy" lên ở mỗi chỗ ngắt câu ngắn → tăng **Hold** lên khoảng 300 ms.

> **Cách khác:** Compressor trong Dynamics và Fairlight FX **Limiter** đều có mục **Sidechain** để làm việc tương tự. Ducker là cách dễ nhất.

---

## Bus — track tổng

`★☆☆ Tình huống cụ thể`

**Là gì:** điểm gom tín hiệu. Mặc định mọi track đổ vào một bus tên **Bus 1** — đó là thứ bạn nghe và thứ được xuất ra. Bus 1 có cột riêng ở cuối Mixer.

**Dùng khi:**
- Cần đặt **Limiter** chặn trần cho cả bản mix → gắn vào cột **Bus 1**. Xem [Limiter trên Bus](loudness-va-xuat.md#limiter-trên-bus--chặn-trần).
- Có nhiều track lời, muốn xử lý chung một lần → tạo một bus "Lời", cho các track lời đổ vào.

**Tạo bus:** menu **Fairlight → Bus Format** → **Add Bus**. Đặt tên, chọn định dạng (mono, stereo...), màu. Bấm **OK**.

**Cho track đổ vào bus:** trong cột Mixer, dùng nút **+** ở phần gán bus.

> Video thông thường chỉ cần **Bus 1**. Đừng tạo thêm bus nếu chưa có lý do.
