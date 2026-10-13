# Đưa clip xuống, cắt, trim, tiếng

Trang này đi theo thứ tự bạn làm: **đưa clip xuống → cắt bỏ phần thừa → trim cho khít → cân tiếng**.

> Nhớ luật của trang Edit: timeline **không tự dồn**. Có dồn hay không là do **phím bạn bấm** và **chế độ** đang bật (`A` hay `T`).

---

## Đưa clip xuống timeline

`★★★ Hằng ngày`

### Ba bước cơ bản

1. **Chọn đoạn:** bấm đúp clip trong Media Pool — nó mở ở **Viewer Source** (trái). Tua tới đầu đoạn cần lấy, bấm `I`. Tới cuối đoạn, bấm `O`.
2. **Chọn track đích:** bấm ô **V1/A1 đỏ** ở đầu track muốn đặt vào (track được chọn sáng lên). Xem [Destination](giao-dien.md#destination--chọn-track-đích).
3. **Chọn vị trí:** đặt con trỏ timeline ở chỗ muốn clip bắt đầu, rồi bấm phím edit.

Đặt `I` `O` sai: `⌥X` xoá cả hai, đặt lại.

### Bảy kiểu edit

| Phím | Kiểu | Kết quả | Timeline dài ra? | Mức |
|---|---|---|---|---|
| `F9` | **Insert** | Chèn vào, **đẩy** phần sau ra | Có | ★★★ |
| `F10` | **Overwrite** | **Ghi đè** lên chỗ đang có | Không | ★★★ |
| `F11` | **Replace** | **Thay** clip dưới con trỏ, khớp đúng khung | Không | ★★☆ |
| `⇧F11` | **Fit to Fill** | **Co giãn tốc độ** clip cho vừa khoảng trống | Không | ★☆☆ |
| `F12` | **Place On Top** | Đặt lên **track trống phía trên** | Không | ★★★ |
| `⇧F10` | **Ripple Overwrite** | Thay clip bằng clip **dài/ngắn khác**, phần sau dồn theo | Tuỳ | ★★☆ |
| `⇧F12` | **Append** | Nối vào **cuối** timeline | Có | ★★★ |

Cả bảy cũng có trong menu **Edit**, và trong lớp phủ hiện ra khi **kéo clip lên Viewer Timeline**.

> Insert, Overwrite, Place On Top, Ripple Overwrite, Append đưa được **nhiều clip cùng lúc** (chọn nhiều clip trong Media Pool rồi bấm phím). Replace và Fit to Fill chỉ lấy **clip đầu tiên**.

### Insert — `F9`

`★★★ Hằng ngày`

**Là gì:** chèn clip vào **tại con trỏ**. Mọi thứ phía sau bị đẩy lùi đúng bằng độ dài clip mới.

**Dùng khi:** thêm một cảnh vào giữa đoạn đã dựng mà không muốn mất gì.

**Ví dụ:** đã dựng xong vlog, muốn chèn cảnh quán cà phê giữa hai đoạn nói. Đặt con trỏ ở điểm nối → `F9`.

**Lưu ý:** con trỏ đặt **giữa một clip** thì clip đó bị **cắt đôi**, clip mới chen vào giữa.

### Overwrite — `F10`

`★★★ Hằng ngày`

**Là gì:** đặt clip vào và **đè lên** bất cứ thứ gì đang ở đó. Không đẩy gì.

**Dùng khi:** dựng thô liên tục — sau mỗi lần `F10`, con trỏ tự nhảy tới **cuối clip vừa đặt**, sẵn sàng cho clip tiếp. Hoặc đặt vào chỗ trống đã chừa sẵn.

> Kéo thả clip từ Media Pool xuống timeline cũng là **Overwrite**.

### Replace — `F11`

`★★☆ Thường dùng`

**Là gì:** thay clip dưới con trỏ bằng clip ở Viewer Source. Độ dài **giữ nguyên** bằng clip cũ. **Khung ở con trỏ Source khớp đúng khung ở con trỏ Timeline**.

**Không cần đặt `I` `O`.**

**Cách làm:**
1. Đặt con trỏ timeline vào clip muốn thay, ở **khung có hành động cần khớp**.
2. Mở clip mới ở Viewer Source, tua tới **đúng khoảnh khắc tương ứng**.
3. Bấm `F11`.

**Dùng khi:** thay một take bằng take khác cùng hành động. Hoặc đặt tiếng động khớp đúng khung hình.

**Ví dụ:** cảnh mở cửa ở take 2 tay bị rung. Đặt con trỏ timeline đúng khung tay chạm tay nắm. Ở Source mở take 3, tua tới khung tay chạm tay nắm. `F11` — take 3 thay vào, khớp nhịp hoàn hảo.

### Fit to Fill — `⇧F11`

`★☆☆ Tình huống cụ thể`

**Là gì:** kiểu edit duy nhất dùng **đủ bốn điểm** và **tự đổi tốc độ** clip. Đoạn nguồn `I`→`O` bị kéo giãn hoặc nén lại cho vừa khít đoạn `I`→`O` trên timeline.

**Cách làm:**
1. Trên timeline: đặt `I` `O` quanh khoảng cần lấp. Hoặc không đặt gì, để con trỏ nằm trong một khoảng trống — Resolve lấy độ dài khoảng trống đó.
2. Ở Source: đặt `I` `O`.
3. `⇧F11`.

**Kết quả:** clip có **badge tốc độ** trên timeline. Không dồn timeline.

**Dùng khi:** còn đúng 3 giây trống để lấp nhưng cảnh đẹp chỉ dài 2,5 giây — chậm đi một chút người xem không nhận ra.

### Place On Top — `F12`

`★★★ Hằng ngày`

**Là gì:** đặt clip lên **track hình trống đầu tiên phía trên** clip đang ở dưới con trỏ. Tiếng đi xuống track tiếng trống dưới cùng. **Bỏ qua track đích**, thiếu track thì tự tạo.

**Dùng khi:** B-roll phủ lên đoạn nói, logo, chữ, ảnh chèn — mà không phải chọn track.

**Ví dụ:** đang nói về món phở, muốn hiện cảnh cận tô phở 3 giây. Đặt con trỏ chỗ bắt đầu, mở cảnh tô phở ở Source với `I` `O` dài 3 giây → `F12`. Tiếng nói bên dưới vẫn nguyên.

### Ripple Overwrite — `⇧F10`

`★★☆ Thường dùng`

**Là gì:** thay **cả clip** trên timeline bằng clip mới có **độ dài khác**. Phần sau tự dồn tới hoặc lùi lại cho vừa.

**Cách làm:**
1. Đặt con trỏ timeline vào clip muốn thay — vị trí nào trong clip cũng được.
2. `⌥X` để chắc chắn timeline **không có** `I` `O`.
3. Ở Source đặt `I` `O` cho đoạn mới.
4. `⇧F10`.

**Dùng khi:** cảnh 5 giây cũ cần thay bằng cảnh 3 giây — không muốn để lỗ 2 giây, cũng không muốn tự kéo cả phần sau.

### Append — `⇧F12`

`★★★ Hằng ngày`

**Là gì:** nối clip vào **cuối timeline**, con trỏ ở đâu cũng không quan trọng.

**Dùng khi:** dựng thô theo thứ tự quay. Chọn nhiều clip trong Media Pool (theo thứ tự sắp xếp) rồi `⇧F12` — nối liền một mạch.

### Kéo thả

`★★★ Hằng ngày`

| Kéo | Kết quả |
|---|---|
| Từ Media Pool hoặc Source xuống timeline | **Overwrite** tại chỗ thả |
| Giữ `⌘⇧` khi kéo xuống | **Insert** — chen vào, đẩy phần sau |
| Giữ `⌥` khi kéo từ Media Pool | **Chỉ lấy hình** |
| Giữ `⇧` khi kéo từ Media Pool | **Chỉ lấy tiếng** |
| Từ Viewer Source: kéo từ **icon phim** hoặc **icon sóng âm** hiện ở đáy hình | Chỉ hình / chỉ tiếng |
| Thả vào **vùng xám trên** track hình cao nhất | Tạo track mới |
| Kéo lên **Viewer Timeline**, thả vào một ô | Edit đúng kiểu ô đó |

> Kéo thả nhanh nhưng khó chính xác bằng phím. Quen tay rồi thì `I` `O` + `F10` nhanh hơn nhiều.

### Chỉ lấy hình, hoặc chỉ lấy tiếng

`★★☆ Thường dùng`

| Cách | Giữ lựa chọn bao lâu |
|---|---|
| Menu **Video / Audio** dưới Viewer Source → chọn **Video Only** hoặc **Audio Only** | Tới khi bạn đổi lại |
| Bấm ô đỏ của track tiếng (hoặc hình) cho tắt | Tới khi bạn bật lại |
| `⌥` kéo (chỉ hình), `⇧` kéo (chỉ tiếng) | Chỉ lần kéo đó |

**Ví dụ:** lấy cảnh đường phố làm B-roll nhưng tiếng xe ồn → Video Only rồi `F12`.

### Đưa nhiều clip một lúc

Chuột phải các clip đã chọn trong Media Pool:

| Lệnh | Làm gì |
|---|---|
| **Insert Selected Clips to Timeline** | Chèn tất cả, theo thứ tự sắp xếp của Media Pool |
| **Append Selected Clips to Timeline** | Nối tất cả vào cuối |
| **Insert Selected Clips to Timeline With Handles** | Chèn, chừa sẵn phần dư hai đầu để thêm chuyển cảnh. Chọn tất cả rồi `⌘T` là có montage |

---

## Dựng ba điểm — three-point editing

`★★☆ Thường dùng`

**Là gì:** bạn chỉ cần đặt **ba điểm** trong bốn điểm (`I` `O` ở Source, `I` `O` ở Timeline). Resolve tự tính điểm thứ tư.

**Luật:**

| Bạn đặt | Resolve làm |
|---|---|
| `I` `O` ở Source, không đặt gì ở Timeline | Con trỏ timeline là điểm vào |
| `I` `O` ở Source + `I` ở Timeline | Clip bắt đầu tại `I` timeline |
| `I` `O` ở Source + chỉ `O` ở Timeline | Clip **kết thúc** đúng `O` timeline — tính lùi (backtime) |
| `I` `O` ở Timeline + `I` ở Source | Lấy đủ độ dài timeline, bắt đầu từ `I` nguồn |
| `I` `O` ở Timeline + chỉ `O` ở Source | Tính lùi: khung `O` nguồn rơi đúng `O` timeline |
| Đủ cả bốn điểm | Độ dài theo timeline. Muốn clip **co giãn** cho khít thì dùng Fit to Fill |

Không có `I` ở Source thì lấy từ khung đầu clip. Không có `O` thì lấy tới hết clip.

**Ví dụ backtime:** muốn cảnh pháo hoa **kết thúc đúng** lúc nhạc dứt. Đặt `O` trên timeline ở nhịp cuối. Ở Source đặt `I` `O` quanh đoạn pháo hoa. `F10` — clip được đặt lùi sao cho khung cuối rơi đúng nhịp.

**Phím đặt điểm trên timeline nhanh:**

| Phím | Làm gì |
|---|---|
| `X` | Đặt `I` `O` ôm đúng **clip (hoặc khoảng trống) dưới con trỏ** |
| `⇧A` | Đặt `I` `O` ôm các **clip đang chọn** |
| `⌥I` / `⌥O` / `⌥X` | Xoá `I` / `O` / cả hai |
| `⇧I` / `⇧O` | Nhảy con trỏ tới `I` / `O` |

**Ví dụ:** có khoảng trống 4 giây cần lấp. Đặt con trỏ vào khoảng trống → `X` → mở clip ở Source, đặt `I` → `F10`. Clip lấp đúng 4 giây.

> Bật **View → Show Preview Marks** để thấy trước điểm thứ tư Resolve tự tính.

---

## Cắt và xoá

`★★★ Hằng ngày`

### Cắt

| Việc | Cách |
|---|---|
| Cắt clip tại con trỏ | `⌘\` (Split Clip) hoặc `⌘B` (Razor) |
| Cắt bằng chuột, nhiều chỗ liên tiếp | `B` (Blade), bấm lên clip. Xong bấm `A` |
| Nối lại hai nửa vừa cắt | Bấm vào đường cắt (đường **chấm chấm** — gọi là *through edit*) → `Delete` |

`⌘\` cắt **mọi track có Sync Lock bật** tại con trỏ. Chỉ muốn cắt một track: tắt Sync Lock các track kia, hoặc dùng `B` bấm đúng clip đó.

### Xoá

| Việc | Cách |
|---|---|
| Xoá, **để lại khoảng trống** (Lift) | Chọn clip → `Delete` |
| Xoá, **phần sau dồn lên** (Ripple Delete) | Chọn clip → `Fn` + `Delete` |
| Xoá một đoạn giữa clip | Đặt `I` `O` trên timeline quanh đoạn đó → `Fn` + `Delete` |
| Xoá khoảng trống lỡ để lại | Bấm vào khoảng trống (nó sáng lên) → `Delete`. Phần sau dồn lên |
| Xoá **mọi** khoảng trống | **Edit → Delete Gaps**. Giới hạn bằng `I` `O` nếu cần |
| Tìm khoảng trống quá nhỏ khó thấy | `⌥⌘;` (trước) / `⌥⌘'` (sau) |
| Tắt clip mà không xoá | Chọn → `D`. Clip mờ đi, không phát, không xuất. `D` lần nữa để bật |

> Bàn phím Mac không có phím Forward Delete riêng — `Fn` + `Delete` chính là Forward Delete.

**Cách bỏ đoạn vấp trong câu nói** — dùng nhiều nhất khi dựng vlog:
1. Đặt con trỏ đầu đoạn vấp → `⌘B`.
2. Đặt con trỏ cuối đoạn vấp → `⌘B`.
3. Bấm chọn khúc ở giữa → `Fn` + `Delete`.

**Cách nhanh hơn:** đặt `I` đầu đoạn vấp, `O` cuối đoạn vấp → `Fn` + `Delete`. Một bước thay vì ba.

### Cắt, chép, dán

| Phím | Làm gì |
|---|---|
| `⌘C` / `⌘V` | Chép / dán tại con trỏ (đè lên chỗ đó) |
| `⌘⇧V` | **Paste Insert** — dán và đẩy phần sau |
| `⌘X` | Cắt ra, để lại khoảng trống |
| `⌘⇧X` | Cắt ra, phần sau dồn lên |

Dán sang track khác: `⌥`-click vùng trống trên track đó trước khi `⌘V`.

### Dời, đổi chỗ clip

| Muốn | Cách |
|---|---|
| Dời clip | Kéo, ở chế độ `A` |
| Dời từng khung | Chọn clip → `,` (lùi) hoặc `.` (tiến). `⇧,` `⇧.` dời 5 khung |
| Dời đúng số khung | Chọn clip, gõ `+10` rồi `Return` — tiến 10 khung. `-10` để lùi |
| **Đổi chỗ** hai clip, không để lỗ | Giữ `⌘⇧` rồi kéo clip sang trước/sau clip kia |
| Đổi độ dài chính xác | Chọn clip → `⌘D`, gõ độ dài |

---

## Trim — sửa độ dài

`★★★ Hằng ngày`

### Tóm tắt nhanh

| Muốn | Chế độ | Kéo vào |
|---|---|---|
| Ngắn/dài clip, **để lại** khoảng trống hoặc đè lên clip bên | Selection `A` | Mép clip |
| Ngắn/dài clip, **phần sau dồn theo** (Ripple) | Trim `T` | Mép clip |
| Dời điểm chuyển cảnh, tổng độ dài giữ nguyên (Roll) | `A` hoặc `T` | Chính giữa điểm nối |
| Đổi khúc nội dung bên trong, giữ vị trí (Slip) | Trim `T` | **Nửa trên** thân clip |
| Dời clip, hai clip bên co giãn bù (Slide) | Trim `T` | **Thanh tên** ở nửa dưới thân clip |

> Mới học thì dựng ở chế độ **Trim `T`** — kéo mép clip là phần sau tự dồn, không bao giờ để lại lỗ đen.

Khi trim, **Viewer Timeline chia 2 hoặc 4 ô** để bạn so khung cuối clip trước với khung đầu clip sau. Giữ `⇧` trong lúc kéo để tạm chỉ xem một khung.

### Ripple — kéo mép, phần sau dồn theo

`★★★ Hằng ngày`

**Rê tới:** mép trái hoặc phải của clip, ở chế độ `T`.

**Kết quả:** clip ngắn/dài ra, mọi clip phía sau (trên các track có Sync Lock) dời theo. **Tổng độ dài timeline thay đổi.**

**Dùng khi:** bỏ đoạn thừa đầu hoặc đuôi một câu nói.

### Roll — dời điểm nối

`★★☆ Thường dùng`

**Rê tới:** **chính giữa** điểm nối hai clip. Chế độ `A` hay `T` đều được.

**Kết quả:** clip trước dài ra bao nhiêu thì clip sau ngắn đi bấy nhiêu. **Tổng độ dài không đổi.**

**Dùng khi:** chuyển cảnh sớm/muộn vài khung cho khớp nhịp, không làm xê dịch phần sau.

### Slip — đổi nội dung bên trong

`★★☆ Thường dùng`

**Rê tới:** **nửa trên, giữa thân clip**, ở chế độ `T`.

**Kết quả:** clip đứng yên, độ dài như cũ, nhưng hiện **khúc sớm hơn hoặc muộn hơn** của footage gốc. Một khung nét đứt cho thấy footage còn dư bao nhiêu.

**Dùng khi:** độ dài đã khớp nhạc, nhưng khoảnh khắc đẹp nhất rơi hơi muộn — slip sớm lên.

### Slide — dời clip, hai bên bù

`★☆☆ Tình huống cụ thể`

**Rê tới:** **thanh tên clip** ở nửa dưới, ở chế độ `T`.

**Kết quả:** clip giữ nguyên nội dung, nhưng trượt sang trái/phải. Clip bên trái ngắn đi, clip bên phải dài ra (hoặc ngược lại). Tổng độ dài không đổi.

**Dùng khi:** một cảnh chèn ngắn cần xuất hiện sớm hơn nửa giây, mà không muốn tự trim hai clip hai bên.

### Trim bằng bàn phím

`★★☆ Thường dùng` — chính xác tới từng khung

**Bước 1 — chọn:**

| Phím | Chọn gì |
|---|---|
| `V` | **Điểm nối** gần con trỏ nhất |
| `U` | Đảo giữa **nửa trái / giữa / nửa phải** của điểm nối (ripple bên nào hay roll) |
| `⇧V` | **Clip** dưới con trỏ |
| `⌥U` | Đảo giữa **hình + tiếng / chỉ hình / chỉ tiếng** |
| `↑` `↓` | Nhảy tới điểm nối trước/sau, giữ kiểu chọn |
| `S` | Khi chọn clip ở chế độ `T`: đảo giữa **Slip** và **Slide** |

**Bước 2 — dịch:** `,` `.` từng khung, `⇧,` `⇧.` mỗi lần 5 khung. Hoặc gõ `+5` / `-5` rồi `Return`.

**Bước 3 — xem lại:** `/` phát quanh chỗ vừa sửa (vài giây trước và sau).

**Ví dụ — bỏ 8 khung im lặng đầu câu:** bấm `T` → `V` → `U` cho tới khi chọn nửa phải điểm nối → gõ `+8` → `Return`.

### Trim tới con trỏ

`★★★ Hằng ngày` — cách trim nhanh nhất

| Phím | Làm gì |
|---|---|
| `⇧[` | Cắt **đầu** clip dưới con trỏ tới đúng con trỏ |
| `⇧]` | Cắt **đuôi** clip dưới con trỏ tới đúng con trỏ |
| `⌘⇧[` / `⌘⇧]` | Như trên nhưng **luôn dồn** timeline, ở chế độ nào cũng vậy |
| `E` | Kéo điểm nối đang chọn tới con trỏ (Extend) |

Ở chế độ `A`, `⇧[` `⇧]` để lại khoảng trống. Ở chế độ `T` thì dồn.

**Không cần chọn trước.** Tua tới chỗ câu nói bắt đầu → `⌘⇧[` — xong.

### Precision Trim Editor — bấm đúp điểm nối

`★☆☆ Tình huống cụ thể`

**Mở:** **bấm đúp** vào điểm nối. Viewer chuyển thành hai dải phim: clip trước ở trên, clip sau ở dưới, có số khung từng ô. Trim xong tự quay về như cũ.

| Kéo | Làm gì |
|---|---|
| Bên trái tay nắm dải trên | Trim điểm ra của clip trước |
| Bên phải tay nắm dải dưới | Trim điểm vào của clip sau |
| Tay nắm trắng giữa hai dải | Roll — dời điểm nối |

Giống [Trim Editor trang Cut](../cut/trim.md#trim-editor--trim-chính-xác-từng-khung). Không thích nó chiếm Viewer: **Preferences → User → Editing** → bỏ tick **Automatically switch to single viewer mode when opening trim editor**.

### Trim khi đang phát — Dynamic Trim

`★☆☆ Tình huống cụ thể`

**Cách nhanh (Quick Trim):** chọn điểm nối hoặc clip → giữ `⌘` và bấm `L` (tiến) hoặc `J` (lùi). Điểm nối dịch theo trong lúc phát, có tiếng.

**Cách đầy đủ:**
1. Chọn điểm nối (`V`), hoặc không chọn gì — Resolve tự chọn điểm gần con trỏ nhất.
2. Bấm `W`. Nút Dynamic Trim và con trỏ chuyển **vàng**.
3. `A` để resize/roll, `T` để ripple. Với clip: `S` đổi slip/slide.
4. `J` `K` `L` để trim. Bấm `L` hoặc `J` nhiều lần để nhanh hơn, `K` để dừng.
5. `W` để thoát.

**Dùng khi:** cắt theo cảm giác — nghe nhạc chạy rồi dừng đúng lúc muốn cắt.

---

## J-cut và L-cut

`★★☆ Thường dùng` — làm chuyển cảnh mượt như phim

Cho **tiếng** của một cảnh lấn sang **hình** của cảnh kế bên:

- **L-cut:** hình đã chuyển, tiếng cảnh trước vẫn còn.
- **J-cut:** nghe tiếng cảnh sau trước khi thấy hình.

**Cách làm:**
1. Giữ `⌥` rồi bấm vào **mép phần tiếng** ở điểm nối — chỉ phần tiếng được chọn.
2. Kéo mép đó sang trái hoặc phải.

**Cách bằng phím:** `V` chọn điểm nối → `⌥U` cho tới khi chỉ chọn tiếng → `,` `.` dịch từng khung.

**Ví dụ:** phỏng vấn — cho câu trả lời bắt đầu nghe được khi hình vẫn còn ở người hỏi (J-cut). Người xem có cảm giác cuộc trò chuyện liền mạch.

---

## Marker

`★★☆ Thường dùng`

**Marker** đánh dấu **một khung**. Có chọn clip thì marker gắn vào **clip** (đi theo clip khi dời). Không chọn clip nào thì marker nằm trên **thước thời gian**.

| Việc | Cách |
|---|---|
| Thêm marker | `M`, hoặc nút **Marker** trên thanh công cụ |
| Thêm marker và mở ngay ô ghi chú | `⌘M`, hoặc bấm `M` hai lần. Đang phát thì tạm dừng cho bạn gõ |
| Sửa marker | Bấm đúp marker, hoặc chọn rồi `⇧M` |
| Nhảy marker trước / sau | `⇧↑` / `⇧↓` |
| Đổi màu | Mũi tên cạnh nút Marker, hoặc trong ô sửa marker |
| Xoá | Mở ô sửa marker → **Remove Marker** |
| Marker có độ dài | Ở Viewer Source, đặt `I` `O` → chuột phải thanh jog → **Convert In and Out to Duration Marker** |
| Xem danh sách mọi marker | **Index → Markers**. Bấm đúp một dòng là nhảy tới |

Ô sửa marker có **Name**, **Notes**, **Color**, **Keyword**, **Duration**.

**Dùng nhiều nhất để khớp nhạc:** phát nhạc, bấm `M` theo mỗi nhịp mạnh. Bật `N`, kéo điểm cắt hít vào marker.

**Dùng thứ hai:** ghi chú chỗ cần sửa — marker **đỏ** = lỗi tiếng, **xanh** = cần thay cảnh. Cuối buổi mở Index → Markers đi từng cái.

> Marker trên timeline có thể thành **chương** (chapter) trong file xuất: ở [Deliver](../deliver/cai-dat-xuat.md#chapters-from-markers), chọn định dạng MP4 hoặc QuickTime, tick **Chapters from Markers** và chọn màu marker dùng làm chương.

---

## Tiếng ngay trên timeline

`★★★ Hằng ngày` — cân tiếng nhanh không cần sang Fairlight

| Việc | Cách |
|---|---|
| To/nhỏ cả clip | Kéo **đường ngang** giữa clip tiếng lên/xuống |
| To/nhỏ theo thời gian | `⌥` + click lên đường ngang để thêm keyframe, rồi kéo |
| Chỉ kéo keyframe theo một chiều | Giữ `⇧` khi kéo keyframe |
| Chuyển mượt hơn giữa hai mức | Chuột phải keyframe → **Ease In and Out** |
| Xoá keyframe | Chọn → `Delete` |
| Fade in / fade out | Rê chuột lên clip tiếng, kéo **tay nắm** ở hai góc trên vào trong |
| Tách hẳn tiếng khỏi hình | Chọn clip → chuột phải → bỏ tick **Link**, hoặc `⌥⌘L` |
| Nối lại hình và tiếng | `⌘`-click chọn cả hai → `⌥⌘L`. Icon dây xích hiện trước tên clip |

Track tiếng quá thấp, khó thấy đường volume? Kéo **đường ranh giữa các track** ở cột đầu track để nới rộng.

**Nhạc nền nhỏ lại khi có lời nói:** ở clip nhạc, `⌥` + click tạo 4 keyframe quanh đoạn có lời, kéo hai keyframe giữa xuống khoảng −10 dB.

> Có nhiều đoạn lời thì dùng **Ducker** ở Fairlight thay vì đặt keyframe tay — xem [Ducker](../fairlight/mixer-va-track-fx.md#ducker--nhạc-tự-nhỏ-khi-có-lời).
