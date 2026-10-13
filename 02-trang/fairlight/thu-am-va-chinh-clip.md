# Thu âm, clip gain, fade, automation

---

## Thu giọng đọc trên Fairlight

`★★☆ Thường dùng`

**Là gì:** thu thẳng từ mic vào một track trên timeline, đúng vị trí con trỏ.

**Dùng khi:** thu lời dẫn (voiceover) cho video, thu lại một câu bị hỏng, thu nhiều take để chọn.

> **Chỉ cần thu nhanh một đoạn?** Trang Cut và Edit có công cụ **Record Voiceover** gọn hơn: **Timeline → Record Voiceover**, hoặc icon micro nhỏ. Chọn **Audio Input**, **Record Track**, bấm nút thu. Sang Fairlight khi cần kiểm soát nhiều hơn.

### Bước 1 — Nối mic vào track (patch input)

Track phải được nối với một nguồn vào thì mới bật thu được. Mặc định cột Mixer ghi **No Input**.

**Cách nhanh (thủ công):**
1. Trong Mixer, bấm ô **Input** trên đầu cột track muốn thu → chọn **Input**. Hoặc menu **Fairlight → Patch Input/Output**.
2. Trong cửa sổ **Patch Input/Output**: chọn nguồn vào (mic của máy, hoặc cổng của sound card), và chọn track đích.
3. Bấm **Patch** ở góc dưới phải.

**Cách tự động (đặt một lần, dùng mãi):**
1. **Fairlight → Patch Input/Output**.
2. Menu tuỳ chọn góc trên phải → **Setup I/O Names**.
3. Tick cột **Default** ở nguồn vào muốn dùng làm mặc định. Đóng bảng.

Từ giờ bấm **R** ở track nào là nguồn đó tự nối vào track đó.

### Bước 2 — Bật thu cho track (arm)

Bấm nút **R** ở **đầu track** hoặc ở **cột Mixer**. Track chưa nối nguồn vào thì không bật được **R**.

### Bước 3 — Thu

1. Đặt con trỏ ở chỗ muốn bắt đầu.
2. Bấm nút **Record** trên thanh phát. Sóng âm vẽ ra ngay khi đang thu — không thấy sóng là mic chưa vào.
3. Dừng: bấm **Stop** hoặc `Space`.

### Nghe gì khi đang thu

Menu **Fairlight → Input Monitor Style**:

| Chọn | Nghe gì |
|---|---|
| **Input** | Chỉ nghe tiếng mic, không bao giờ nghe track |
| **Auto** | Track đã bật R thì nghe mic; khi phát thì nghe track |
| **Record** | Chỉ nghe mic khi đang thực sự thu |
| **Mute** | Không nghe gì |
| **Repro** | Nghe lại đúng cái vừa thu, phát từ track |

> Thu bằng mic và loa ngoài thì đeo tai nghe, hoặc chọn **Mute** — tránh tiếng loa lọt ngược vào mic.

### File thu nằm ở đâu

- **Trên ổ cứng:** **File → Project Settings → Master Settings → Working Folders → Project media location**.
- **Trong Media Pool:** clip thu được bỏ vào bin đang chọn. Muốn gom riêng thì tạo bin "Thu âm" và chọn nó trước khi thu.

**Đặt tiền tố tên file:** chuột phải đầu track thu → **Set Track Record Name**. Ví dụ đặt "VO" thì các file thu ra bắt đầu bằng "VO".

### Thu nhiều take chồng lên nhau

Thu lại đúng đoạn cũ thì take mới **đè lên** take cũ khi phát, nhưng take cũ **không mất** — Resolve xếp chúng thành lớp trong cùng track.

- Xem các lớp: **View → Show Audio Track Layers**.
- Lớp trên cùng là lớp được nghe. Kéo đoạn hay nhất lên trên để dùng.
- Ghép xong muốn gộp lại một lớp: **Timeline → Flatten Audio Track Layers**.

**Ví dụ:** đọc lời dẫn 1 phút, câu thứ ba bị vấp. Đặt con trỏ trước câu ba, thu lại riêng câu đó. Take mới đè lên đúng chỗ, phần còn lại giữ nguyên.

---

## Sửa clip trên timeline Fairlight

`★★☆ Thường dùng`

Phần lớn thao tác giống trang Edit. Khác chính là **ba chế độ chọn** trên thanh công cụ:

| Chế độ | Dùng khi |
|---|---|
| **Pointer Mode** | Chọn clip, kéo clip, kéo mép clip. Chế độ mặc định |
| **Range Mode** | Chọn **một khoảng** trên một hay nhiều clip — để xoá, chỉnh gain, cắt riêng khoảng đó |
| **Focus Mode** | Công cụ đổi theo vị trí chuột: nửa trên sóng âm là chọn khoảng, nửa dưới là kéo clip, sát đường gain là chỉnh gain |

### Phím hay dùng

| Phím | Làm gì |
|---|---|
| `⌘\` | Cắt đôi clip tại con trỏ (**Timeline → Split Clip**), trên các track đang chọn |
| `⌘B` | **Razor** — cắt tại con trỏ |
| `⇧[` | **Trim Start** — kéo đầu mọi clip chạm con trỏ về đúng con trỏ |
| `⇧]` | **Trim End** — kéo đuôi mọi clip chạm con trỏ về đúng con trỏ |
| `⇧⌘T` | **Trim to Selection** — bỏ hết phần ngoài vùng chọn |
| `⌘⌥E` | **Smart Zoom** — phóng to track đang chọn |

Track nào không muốn bị ảnh hưởng thì **khoá** lại.

### Đè hay chồng lớp

Mặc định Fairlight ở chế độ **đè** (Overwrite): kéo clip chồng lên clip khác thì phần bị chồng bị cắt đi (vẫn lấy lại được bằng kéo mép).

Bật **Timeline → Layered Audio Editing** để clip chồng lên thành **lớp**, giống cách thu nhiều take ở trên.

> Nhớ: ở chế độ lớp, xoá clip ở trên thì clip bên dưới **lộ ra** và phát tiếp. Dễ bất ngờ nếu quên.

---

## Clip gain — to nhỏ từng clip

`★★★ Hằng ngày`

**Là gì:** mức to nhỏ riêng của một clip, tách khỏi fader của track. Chỉnh clip gain trước, fader để dành cân cả track.

**Dùng khi:** một câu nói nhỏ hơn các câu khác, một tiếng động quá to.

**Cách làm:**

| Cách | Làm thế nào |
|---|---|
| **Kéo trên clip** | Rê chuột lên đường gain trên clip, kéo lên xuống |
| **Inspector** | Chọn clip → **Inspector → tab Audio → Volume** |
| **Chỉ một đoạn trong clip** | Dùng công cụ chọn khoảng (Range hoặc Focus Mode) quét đoạn đó, rồi kéo đường gain — Resolve tự thêm keyframe ở hai đầu |

Không thấy đường gain: **Timeline View Options → Gain Line**, hoặc **Fairlight → Show Clip Gain Line**.

**Keyframe trên đường gain:**
- Thêm: giữ `⌥` rồi bấm lên đường gain. Cần ít nhất hai keyframe mới có thay đổi.
- Xoá: giữ `⌘⌥` rồi bấm vào keyframe.
- Kéo keyframe lên xuống để đổi mức, sang ngang để đổi thời điểm.

**Ví dụ:** câu "chào mọi người" ở đầu vlog nhỏ hơn hẳn phần sau. Range Mode quét đúng câu đó, kéo đường gain lên 4 dB.

### Copy mức to sang clip khác

Chọn clip đã chỉnh, `⌘C`. Chọn clip đích, chuột phải → **Paste Attributes** → tick **Volume** (mức to), **Plugins** (hiệu ứng), **Equalizer** (EQ) → **Apply**.

Với cả track: chuột phải đầu track → **Copy Attributes**, rồi chuột phải đầu track khác → **Paste Attributes**.

Xoá: chuột phải → **Remove Attributes**. Tick **Volume** là xoá hết keyframe gain của clip.

---

## Fade và crossfade

`★★★ Hằng ngày`

### Fade đầu, fade cuối

1. Rê chuột lên clip — hiện **tay nắm** ở góc trên trái và góc trên phải.
2. Kéo tay nắm vào trong. Kéo càng xa fade càng dài.
3. Kéo **chấm trên đường cong** fade: lên xuống đổi độ dốc, sang ngang đổi dáng cong.

**Fade tới con trỏ:** đặt con trỏ trên clip → menu **Trim → Fade In to Playhead** hoặc **Fade Out to Playhead**.

### Crossfade giữa hai clip

Hai clip nối nhau, muốn chuyển mượt:

1. Thêm fade out ở cuối clip trước, fade in ở đầu clip sau.
2. Kéo clip sau chồng lên clip trước đúng bằng độ dài fade.
3. Thả ra — hai fade chồng nhau thành crossfade.

Bấm đúp vào crossfade để chỉnh trong **Inspector → tab Transition**: **Duration**, **Alignment**, **Fade In** / **Fade Out** (−3 dB, 0 dB, +3 dB).

> **Không có crossfade vẫn không bị "tách":** mặc định Resolve tự chèn một crossfade rất ngắn (1,5 ms) giữa hai clip sát nhau để tránh tiếng bụp. Tuỳ chọn này là **Enable Soft Fades** trong **Project Settings → Fairlight**.

### Fade hàng loạt

`★☆☆ Tình huống cụ thể`

Cần fade cho hàng chục clip cùng lúc: chọn các clip và track, dùng các lệnh **Batch Fades** trong menu **Fairlight**. Cửa sổ Batch Fades cho đặt dáng và độ dài (tính bằng khung hình) của **Fade In**, **Cross Fade**, **Fade Out**. Clip rời nhau được fade đầu cuối; clip sát nhau được crossfade.

Cửa sổ nhớ cài đặt lần trước, nên lần sau chỉ cần chọn **Apply Batch Fades** trong menu **Fairlight**.

---

## Automation — to nhỏ theo thời gian cho cả track

`★☆☆ Tình huống cụ thể`

**Là gì:** ghi lại thay đổi của fader (hoặc pan, EQ, hiệu ứng) theo thời gian, cho **cả track**. Khác với keyframe clip gain chỉ áp cho một clip.

**Dùng khi:** nhạc cần to lên ở đoạn không lời rồi nhỏ lại, hoặc tiếng vang tăng dần khi nhân vật đi vào hang.

> Video đơn giản thì **clip gain** và **Ducker** là đủ. Chỉ dùng automation khi cần chỉnh cả track theo thời gian.

### Vẽ automation

1. Bấm **Toggle Automation** bên phải thanh phát (chuyển đỏ khi bật).
2. Ở đầu track, menu automation đang ghi **None** → chọn thông số muốn chỉnh, ví dụ fader.
3. Clip tối đi, hiện một **đường automation** màu xám.
4. Thêm điểm: giữ `⌥` rồi bấm lên đường. Xoá điểm: giữ `⌘⌥` rồi bấm. Hoặc dùng **Pencil** để vẽ.
5. Kéo các điểm lên xuống. Đường đã có automation chuyển sang **xanh lá**.

Đổi nhanh giữa xem clip và xem automation: `F4`.

Điểm automation nối nhau bằng **đường thẳng**. Muốn fade cong tự nhiên thì đặt vài điểm tạo dáng cong.

### Ghi automation bằng cách kéo fader

Bật **Toggle Automation** như trên. Trong cột Mixer, bật nút **Automation** của track (ngay trên fader), bấm phát, kéo fader theo ý. Resolve ghi lại từng chuyển động. Bấm chuột phải vào nút này để chọn **Safe** (khoá không ghi) hoặc **Off**.

**Ví dụ:** đoạn mở đầu 10 giây chỉ có hình và nhạc, sau đó mới nói. Vẽ automation fader nhạc: 0 dB ở 10 giây đầu, xuống −12 dB ngay trước câu nói đầu tiên.
