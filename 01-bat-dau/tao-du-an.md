# Tạo project đúng ngay từ đầu

Phần lớn rắc rối về sau (video giật, tiếng lệch hình, xuất ra mờ) bắt nguồn từ năm phút đầu tiên. Làm đúng ở đây thì về sau không phải sửa.

| Bước | Làm ở đâu | Mức |
|---|---|---|
| [1. Tạo project](#bước-1--tạo-project-trong-project-manager) | Project Manager | `★★★ Hằng ngày` |
| [2. Frame rate](#bước-2--frame-rate-thứ-không-sửa-được-về-sau) | Project Settings → Master Settings | `★★★ Hằng ngày` |
| [3. Độ phân giải](#bước-3--độ-phân-giải) | Project Settings → Master Settings | `★★★ Hằng ngày` |
| [4. Quản lý màu](#bước-4--chọn-cách-quản-lý-màu) | Project Settings → Color Management | `★★☆ Thường dùng` |
| [5. Nơi lưu cache](#bước-5--nơi-lưu-cache-và-file-tạo-ra) | Project Settings → Master Settings → Working Folders | `★★☆ Thường dùng` |
| [6. Tự động lưu](#bước-6--tự-động-lưu-và-bản-sao-lưu) | Preferences → User → Project Save and Load | `★★★ Hằng ngày` |

## Bước 1 — Tạo project trong Project Manager

**Project Manager** là cửa sổ hiện ra đầu tiên khi mở Resolve. Đang làm dở thì mở lại bằng `⇧1`, hoặc nút **ngôi nhà** góc dưới phải.

**Tạo project mới:**
1. Bấm **New Project** ở đáy cửa sổ (hoặc bấm đúp icon **Untitled Project**).
2. Gõ tên. Nên có ngày tháng, ví dụ `2026-10 Vlog Da Lat`.
3. Xem ô **Media Location** — nơi Resolve lưu file nó tự tạo ra (tiếng thu voiceover…). Bấm **Change Location** nếu ổ đó sắp đầy.
4. Bấm **Create**. Resolve mở project ở trang Media.

**Chuột phải một project** trong Project Manager:

| Mục | Làm gì | Mức |
|---|---|---|
| **Rename** | Đổi tên | ★★☆ |
| **Open in Read Only Mode** | Mở mà không sợ sửa nhầm | ★☆☆ |
| **Project Backups** | Mở lại bản sao lưu tự động — xem [Bước 6](#bước-6--tự-động-lưu-và-bản-sao-lưu) | ★★☆ |
| **Export Project** | Xuất file `.drp` — chỉ project, không kèm media | ★★☆ |
| **Export Project With Stills and LUTs** | Như trên, kèm still trong Gallery và LUT đang dùng | ★☆☆ |
| **Export Project Archive** | Gói cả project lẫn media thành một thư mục `.dra` | ★☆☆ |
| **Load Project Settings to Current Project** | Chép thiết lập của project này sang project đang mở | ★☆☆ |

Nhập project từ máy khác: kéo file `.drp` thả vào Project Manager, hoặc bấm **Import** ở đáy cửa sổ.

> **Resolve lưu project trong một "project library" (thư viện project), không phải file rời.** Nút góc trên trái Project Manager mở thanh **Project Libraries** — xem project đang nằm ở thư viện nào. Muốn mang project sang máy khác thì dùng **Export Project** hoặc **Export Project Archive**. Chỉ copy thư mục footage là không đủ.

## Bước 2 — Frame rate, thứ không sửa được về sau

Mở **Project Settings** (`⇧9`, hoặc nút **bánh răng** góc dưới phải) → **Master Settings** → nhóm **Timeline Format** → **Timeline frame rate**.

Đặt đúng bằng frame rate bạn quay. Quay 24 thì để 24, quay 30 thì để 30.

> **Manual ghi rõ: khi Media Pool đã có file, frame rate của project không đổi được nữa.** Nên đặt trước khi nạp media.

Lần đầu nạp clip vào Media Pool trống, nếu frame rate clip khác project, Resolve hỏi có đổi project cho khớp không. **Chọn Change.** Chọn Don't Change là bị khoá ở frame rate cũ.

Cách an toàn để timeline khớp clip: nạp clip vào Media Pool, chọn clip → chuột phải → **Create Timeline Using Selected Clips**. Xem thêm [Tạo timeline và Timeline Settings](../02-trang/edit/timeline-nang-cao.md#tạo-timeline-và-timeline-settings).

## Bước 3 — Độ phân giải

Cùng nhóm **Timeline Format**, ô **Timeline resolution**:

| Làm gì | Đặt |
|---|---|
| Video ngang thông thường | 1920×1080 |
| Video 4K | 3840×2160 |
| TikTok, Reels, Shorts | 1920×1080 rồi tick **Use vertical resolution** → thành 1080×1920 |

**Use vertical resolution** đảo chiều ngang và dọc của khung. Muốn một project có cả bản ngang lẫn bản dọc thì để project ngang, chỉ đổi riêng timeline dọc — xem [Timeline Settings](../02-trang/edit/timeline-nang-cao.md#timeline-settings--mỗi-timeline-một-cỡ-khung) và [Luồng: video dọc](../03-luong/video-doc.md).

Timeline resolution đổi được bất cứ lúc nào — Resolve tự tính lại mọi chỉnh sửa theo cỡ mới. Nó cũng **khác** resolution lúc xuất: dựng ở 1080 cho nhẹ máy rồi xuất 4K được. Xem [Tối ưu hiệu năng](../04-tham-khao/hieu-nang.md#bước-3--hạ-timeline-resolution).

**Clip khác cỡ khung xử lý thế nào:** **Project Settings → Image Scaling → Input Scaling → Mismatched resolution files**. Mặc định **Scale entire image to fit** (giữ toàn hình, có viền đen).

## Bước 4 — Chọn cách quản lý màu

**Project Settings → Color Management → Color science**. Quyết định trước khi bắt đầu chỉnh màu — đổi sau khi đã chỉnh là mọi grade lệch.

| Color science | Resolve làm gì | Hợp với |
|---|---|---|
| **DaVinci YRGB** (mặc định) | Không tự chuyển gì. Bạn tự chuyển bằng node **Color Space Transform** hoặc LUT | Quay điện thoại, máy ảnh màu thường. Một máy LOG mà muốn thấy rõ từng bước |
| **DaVinci YRGB Color Managed** | Tự chuyển mọi clip về không gian màu chung | Trộn nhiều máy LOG khác hãng, muốn ít thao tác |
| **DaVinci YRGB Color Managed (Legacy)** | Bản cũ, để mở project cũ | Project từ bản Resolve cũ |
| **ACEScc / ACEScct** | Chuẩn ACES của ngành phim | Quy trình xưởng phim |

**Bật Color Managed — cách đơn giản:**
1. **Color science** → **DaVinci YRGB Color Managed**.
2. Tick **Automatic Color Management**.
3. **Color processing mode** → **SDR**.
4. **Output color space** → Rec.709 (YouTube, TV, mạng xã hội).

Resolve tự đoán không gian màu đầu vào theo loại file. Đoán sai (hay gặp với LOG): chuột phải clip trong Media Pool → **Input Color Space** → chọn đúng profile máy quay.

> **Đừng chuyển hai lần.** Đã bật Color Managed thì không thêm CST hay LUT chuyển đổi nữa. Chi tiết: [LUT và quản lý màu](../02-trang/color/lut-va-quan-ly-mau.md#color-management-của-project) và [Luồng: LOG sang Rec.709](../03-luong/log-sang-rec709.md).

## Bước 5 — Nơi lưu cache và file tạo ra

**Project Settings → Master Settings → Working Folders**:

| Ô | Chứa gì | Mặc định |
|---|---|---|
| **Project media location** | File Resolve tự tạo (tiếng voiceover…) | Đặt lúc tạo project |
| **Proxy generation location** | Proxy media | — |
| **Cache files location** | Render cache | Thư mục ẩn `CacheClip` trên ổ đầu tiên trong danh sách Media Storage của Preferences |
| **Gallery stills location** | Still lưu ở Gallery trang Color | Thư mục ẩn `.gallery` trên cùng ổ đó |

Trỏ **Cache files location** vào một ổ SSD nhanh, đừng để chung ổ với footage nếu có thể. Ổ cache bị rút ra thì Resolve sẽ báo.

Cùng trang Master Settings, nhóm **Optimized Media and Render Cache** chọn định dạng và độ phân giải của proxy, optimized media, render cache — xem [Tối ưu hiệu năng](../04-tham-khao/hieu-nang.md).

**Dùng lại thiết lập cho mọi project:** menu ba chấm của cửa sổ Project Settings → **Save Current Settings as Preset**. Chọn preset → **Set As Default Preset** để project mới tự dùng.

## Bước 6 — Tự động lưu và bản sao lưu

**DaVinci Resolve → Preferences → User → Project Save and Load**. Đây là thiết lập của máy, áp cho mọi project.

| Ô | Làm gì | Nên |
|---|---|---|
| **Live Save** | Lưu liên tục khi bạn làm. Bật sẵn mặc định | Để bật |
| **Project Backups** | Lưu bản sao đầy đủ định kỳ: mặc định mỗi 10 phút trong giờ gần nhất, 8 bản theo giờ, 5 bản theo ngày | Bật |
| **Project backup location** | Nơi lưu bản sao. Mặc định thư mục `ProjectBackup` trên ổ scratch | Trỏ sang ổ khác ổ hệ thống nếu có |
| **Timeline Backups** | Lưu bản sao riêng từng timeline | Bật nếu hay sửa lớn |

Manual ghi hai bộ số mặc định khác nhau (đoạn Timeline Backups ghi 2 bản theo giờ, 2 bản theo ngày). Số thật trên máy bạn hiện ngay trong các ô này.

**Mở bản sao lưu:** Project Manager → chuột phải project → **Project Backups** → chọn bản → **Load**. Bản sao mở thành project riêng, không đè bản gốc.

**Khôi phục timeline:** chuột phải timeline trong Media Pool → **Restore Timeline Backup**. Xem [Timeline Backup](../02-trang/edit/timeline-nang-cao.md#timeline-backup--điểm-khôi-phục).

Chữ **Edited** cạnh tên project ở đầu cửa sổ nghĩa là còn thay đổi chưa lưu. Lưu tay: `⌘S`.

## Sau khi tạo xong

1. [Nạp media](../02-trang/media/nap-media.md) và [chia bin](../02-trang/media/bin.md).
2. Có thẻ nhớ chưa backup: [Clone Tool](../02-trang/media/clone-tool.md).
3. Đi theo một luồng: [Vlog YouTube](../03-luong/vlog-youtube.md), [Video dọc](../03-luong/video-doc.md), [LOG sang Rec.709](../03-luong/log-sang-rec709.md).
