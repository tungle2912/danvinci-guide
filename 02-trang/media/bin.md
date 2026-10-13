# Bin, Power Bin, Smart Bin

Có **ba loại bin** trong Media Pool, mỗi loại nằm ở một khu riêng trong Bin List. Chúng hoạt động khác hẳn nhau.

| Loại | Chứa gì | Dùng chung giữa các project? | Mức |
|---|---|---|---|
| **Bin** | Clip bạn kéo vào | Không | ★★★ |
| **Power Bin** | Clip bạn kéo vào | **Có** | ★★☆ |
| **Smart Bin** | Không chứa gì — tự lọc clip theo điều kiện | Tuỳ chọn | ★★☆ |

Hiện/ẩn khu Power Bins và Smart Bins: **menu tuỳ chọn Media Pool** (ba chấm) → tick **Show Power Bins** / **Show Smart Bins**.

## 1. Bin thường

`★★★ Hằng ngày`

Thư mục thủ công. Kéo gì vào thì nó nằm đó.

- Tạo: chuột phải trong Bin List → **Add Bin**, hoặc `⇧⌘N` (**File → New Bin**)
- Lồng nhau bao nhiêu cấp cũng được

Mọi thứ nạp vào project mặc định nằm ở bin **Master** trên cùng.

**Thao tác với bin:**

| Việc | Cách |
|---|---|
| Tạo bin con | Chuột phải một bin → **Add Bin** |
| Gom clip đã chọn vào bin mới | Chuột phải clip → **Create Bin With Selected Clips** |
| Đổi tên | Chọn bin, bấm vào tên lần nữa, gõ, `Return`. Hoặc chuột phải → **Rename Bin** |
| Chuyển clip sang bin khác | Kéo clip thả vào bin đích |
| Lồng bin vào bin khác | Kéo bin thả vào bin kia |
| Xoá bin | Chọn bin → `Delete`. Hoặc chuột phải → **Delete Bin**. Bin con bên trong bị xoá theo |
| Nạp thẳng vào một bin | Bấm chọn bin đó trước, rồi mới nạp |

> **Xoá bin không xoá file trên ổ.** Chỉ bỏ clip khỏi project.

**Sắp thứ tự bin:** chuột phải vùng trống Bin List → **Sort By** → **Name**, **Date Created**, **Date Modified**, hoặc **User Sort**.

Chọn **User Sort** rồi kéo bin lên xuống theo ý. Một vạch cam cho biết bin sẽ rơi vào đâu. Thứ tự bạn kéo được **nhớ lại** kể cả khi đổi sang kiểu sắp khác rồi quay về.

### Cách chia bin cho một dự án vừa

```
Master
├── 01 Footage
│   ├── A-cam
│   └── B-roll
├── 02 Audio
├── 03 Nhạc
├── 04 Đồ hoạ
└── 05 Timelines
```

Đánh số ở đầu tên để bin luôn sắp đúng thứ tự.

> **Dùng lại cấu trúc bin cho mọi dự án:** tạo sẵn một bộ thư mục rỗng trên ổ theo đúng cây trên. Mỗi dự án mới, kéo bộ thư mục đó từ Finder thả vào **Bin List** — Resolve dựng lại đúng cây bin, kể cả khi thư mục trống.

---

## 2. Power Bin

`★★☆ Thường dùng`

**Mặc định ẩn.** Đây là bin **dùng chung cho mọi project trong cùng database**.

Dùng để chứa những thứ bạn cần ở mọi dự án:

- Mẫu chữ, lower third đã làm sẵn
- Logo, watermark
- Thư viện tiếng động
- Nhạc nền hay dùng
- LUT dưới dạng clip tham chiếu

Tạo: hiện khu Power Bins → chuột phải trong đó → **Add Bin**.

Power Bin lồng nhau được như bin thường. Khu Power Bin có vạch chia kéo được để to nhỏ so với bin thường và Smart Bin.

> Đây là tính năng tiết kiệm thời gian nhất mà ít người biết. Làm xong một bộ lower third đẹp, bỏ vào Power Bin, dự án sau mở ra là có sẵn.

**Lưu ý:** Power Bin cũng chỉ lưu đường dẫn. Để logo, nhạc trong một thư mục **cố định** trên ổ, đừng dời đi, nếu không mọi project đều thấy clip offline.

---

## 3. Smart Bin

`★★☆ Thường dùng`

Không chứa clip. Nó là **bộ lọc tự chạy** — bạn đặt điều kiện, clip nào thoả thì tự xuất hiện.

Tạo: hiện khu Smart Bins → chuột phải → **Add Smart Bin** (có chỗ ghi **Create Smart Bin**) → đặt tên và điều kiện → **Create Smart Bin**.

### Hộp thoại tạo Smart Bin

| Phần | Làm gì |
|---|---|
| **Tên** | Tên bin |
| **Show in all projects** | Tick thì Smart Bin hiện ở **mọi** project, trong thư mục **User Smart Bins** |
| **Match: All / Any** | **All** = clip phải thoả mọi điều kiện. **Any** = thoả một điều kiện là đủ |
| **Ô tick đầu mỗi dòng** | Tạm tắt một điều kiện mà không phải xoá |
| **Menu thứ nhất** — nhóm metadata | Chọn nhóm: các nhóm của Metadata Editor, **Media Pool Properties** (mọi cột của Media Pool), **Color Timeline Properties** |
| **Menu thứ hai** — trường | Trường cụ thể trong nhóm đó |
| **Menu thứ ba** — so sánh | **is**, **contains**, khoảng số, khoảng ngày, đúng/sai, màu flag, màu marker… tuỳ trường |
| **Nút +** | Thêm một điều kiện. Giữ `⌥` bấm để thêm một **nhóm** điều kiện lồng bên trong |

Trong lúc bạn sửa điều kiện, dải thumbnail trong hộp thoại cập nhật luôn để bạn thấy bộ lọc đang bắt được clip nào.

### Ví dụ điều kiện hữu ích

| Muốn lọc | Đặt điều kiện |
|---|---|
| Mọi cảnh phỏng vấn | Keywords **contains** `phỏng vấn` |
| Mọi take tốt | Good Take **is** `true` |
| Footage quay 4K | Resolution **is** `3840x2160` |
| Clip dài trên 1 phút | Duration **greater than** `00:01:00:00` |
| Clip quay hôm nay | Date Created **is** hôm nay |

Ghép nhiều điều kiện bằng **All** (và) hoặc **Any** (hoặc).

**Ví dụ nhóm lồng:** muốn "mọi take tốt **và** (là phỏng vấn **hoặc** là b-roll)". Match **All** cho dòng Good Take. Giữ `⌥` bấm **+** để thêm nhóm con đặt **Any**, trong đó hai dòng Keywords.

### Sửa, nhân bản, xoá Smart Bin

| Việc | Cách |
|---|---|
| Sửa điều kiện | **Bấm đúp** Smart Bin → sửa → **OK** |
| Đổi tên | Chuột phải → **Rename** |
| Nhân bản | Chuột phải → **Duplicate**. Tiện khi cần biến thể của một bộ lọc phức tạp |
| Xoá | Chuột phải → **Delete Smart Bin** → **Delete**. Clip không bị xoá |
| Gom vào thư mục | Chuột phải khu Smart Bins → **Add Folder**, rồi kéo Smart Bin vào. Chọn thư mục là thấy clip của mọi Smart Bin bên trong |

### Smart Bin tự tạo

Resolve tự sinh Smart Bin theo metadata có sẵn: **Timelines**, **Keywords**, **People**, **Shot**, **Scene**, **Offline Clips**… Mỗi loại là một nhóm đóng sẵn trong khu Smart Bins, bấm tam giác để mở.

Chọn loại nào được tự tạo: **Preferences → User → Editing → Automatic Smart Bins**.

> **Mẹo gắn keyword hàng loạt:** chọn nhiều clip, **kéo thả lên một Smart Bin tự tạo** thuộc nhóm Keywords, Shot hoặc Scene. Mọi clip đó nhận luôn keyword/shot/scene của bin. Kéo lên Smart Bin loại khác thì không có tác dụng.

### Smart Bin chỉ tốt bằng metadata của bạn

Smart Bin lọc dựa trên metadata. Nếu bạn không gõ metadata thì nó chỉ lọc được theo thông tin kỹ thuật (độ phân giải, fps, ngày tạo).

Muốn dùng Smart Bin hiệu quả, phải đầu tư vào [Metadata Editor](metadata.md) trước.

Nội dung Smart Bin **cập nhật tự động** — gắn thêm keyword cho một clip là nó xuất hiện ngay trong Smart Bin tương ứng.

---

## Gắn nhãn màu cho bin

`★☆☆ Tình huống cụ thể`

Dự án nhiều bin thì gắn màu để nhận ra nhanh. Có **tám màu**.

Chuột phải bin → **Color Tag** → chọn màu. Tên bin hiện nền màu đó.

Sau đó lọc theo màu để chỉ hiện các bin cùng nhãn: menu **Color Tag Filter** ngay bên phải nút Bin List → chọn màu. Muốn hiện lại hết: **Show All**.

Cách dùng thường thấy: đỏ cho footage chưa xem, vàng cho đang dựng, xanh cho đã xong.

---

## Xuất nhập bin và timeline

`★☆☆ Tình huống cụ thể`

| Định dạng | Chứa gì | Xuất | Nhập |
|---|---|---|---|
| `.drb` | Một hay nhiều bin (DaVinci Resolve Bin) | Chuột phải bin → **Export Bin**, hoặc **File → Export → Export Bin** | Chuột phải Media Pool → **Import Bin**, hoặc **File → Import → Import Bin** |
| `.drt` | Một timeline (DaVinci Resolve Timeline) | Chọn timeline → **File → Export → Export AAF, XML, DRT** (`⇧⌘O`) → chọn loại `.drt` | **File → Import Timeline → Import AAF, XML, DRT** (`⇧⌘I`) |
| `.drp` | Cả project | **File → Export Project** | |

`.drb` tiện khi muốn chuyển một bộ đồ hoạ sang dự án khác mà không mang cả project.

**Những gì đi theo và không đi theo:**

- `.drb` mang theo metadata, điểm `I` `O`, timeline trong bin. **Không** mang file media.
- `.drt` chỉ mang timeline và thông tin clip. **Không** mang file media.
- Bin hay timeline nhập vào có thêm chữ **import** ở cuối tên để khỏi trùng.
- Sang máy khác, có thể phải [nối lại media](nap-media.md#media-offline--khi-clip-hiện-đỏ).

**Xuất nhiều timeline một lúc:** chọn các timeline → chuột phải → **Timelines → Export → DaVinci Resolve Timeline Files** → chọn thư mục. Mỗi file giữ đúng tên timeline.

Power Bin cũng xuất nhập được bằng `.drb` như bin thường.

---

## Đồng bộ bin với thư mục trên ổ

`★☆☆ Tình huống cụ thể`

Cho một bin **tự cập nhật** khi có file mới bỏ vào thư mục tương ứng trên ổ.

1. Nạp thư mục thành bin bằng **Add Folder and SubFolders into Media Pool (Create Bins)** (trang Media), hoặc nút **Import Media Folder** (trang Cut).
2. Chuột phải bin đó → **Automatically Resync Media Files**.

Từ đó, file mới bỏ vào thư mục sẽ **tự xuất hiện** trong bin.

Chỉ đồng bộ một lần: chuột phải bin → **Resync Media Files**.

**Điều kiện để chạy được:**

- Bin có **ít nhất một clip**.
- Mọi clip trong bin nằm **cùng một thư mục** trên ổ.
- **Tên bin trùng tên thư mục** chứa clip.
- Thư mục con tạo **sau** khi nạp thì không được theo dõi. Nạp lại thư mục cha để bắt thư mục con mới.

File bị xoá khỏi thư mục thì clip trong bin chuyển sang **offline**, metadata vẫn giữ.

**Ví dụ:** người làm đồ hoạ lưu lower third vào thư mục `CG` trên ổ mạng. Bạn nạp `CG` thành bin, bật Automatically Resync Media Files. Mỗi file họ lưu xong là hiện ngay trong bin của bạn.
