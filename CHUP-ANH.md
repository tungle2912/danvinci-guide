# Bàn giao: chụp ảnh và nội dung còn lại

File này dành cho session sau. Đọc hết trước khi làm.

## 1. Công cụ điều khiển Resolve

| Việc | Cách |
|---|---|
| Lua bridge | Tool `mcp__davinci-resolve-lua__run_lua`. Nếu báo bridge chết: nhờ người dùng mở project rồi bấm **Workspace → Scripts → resolve_mcp_bridge** |
| Đổi trang | `resolve:OpenPage("edit")` (media, cut, edit, fusion, color, fairlight, deliver) |
| Biên dịch công cụ click | `tools/build-tools.sh` → tạo `/tmp/wl/winlist` và `/tmp/wl/click` |
| Click chuột | `/tmp/wl/click <x> <y>` (toạ độ point). `osascript ... click at` **không** tới được UI của Resolve |
| Phím tắt | `osascript -e 'tell application "System Events" to keystroke "z" using shift down'` (phải activate Resolve trước) |
| Chụp toàn cửa sổ | `tools/winshot.sh <tên> 1600` — không cần đưa Resolve lên trước |
| Chụp một vùng | `tools/crop.sh <tên> x0 y0 x1 y1 [rộng]` — toạ độ tỉ lệ 0..1 của cửa sổ |
| Chụp menu xổ, hộp thoại | `tools/screen-crop.sh <tên> x y w h [rộng]` — toạ độ point màn hình (menu xổ là cửa sổ riêng, `winshot` không thấy) |

Cửa sổ Resolve: vị trí (0, 33), cỡ 1728×1005 point; màn hình Retina, 1 point = 2 pixel.

Trước mỗi click, kiểm tra Resolve đang ở trên cùng (`osascript -e 'tell application "System Events" to get name of first process whose frontmost is true'` phải ra `Resolve`) — tránh click nhầm sang ứng dụng khác của người dùng.

Fusion qua Lua: `fusion:GetCurrentComp()`, `comp.CurrentFrame.FlowView:SetPos(tool, x, y)`, `comp.CurrentFrame:ViewOn(tool, 1|2)` — chỉ dùng được khi đang ở trang Fusion.

**Tránh:** `InsertFusionTitleIntoTimeline` — nó chèn dồn vào V1 và cắt đôi clip.

## 2. Project demo

Project **So tay DaVinci - Demo**, timeline **Demo - Vlog**, 25 fps.

| Track | Nội dung |
|---|---|
| V1 | 6 clip LOG 4K xen kẽ: đĩa phô mai rau củ / cô gái ở trại cừu Kazakhstan. Mọi clip đã có grade 6 node |
| V2 | Trống |
| A1 "Giong noi" | `/Users/mac/davinci/audio/giong-noi.wav` — giọng đọc tiếng Việt (tạo bằng `say -v Linh`) |
| A2 "Nhac nen" | `/Users/mac/davinci/audio/nhac-nen-20s.wav` — nhạc nền tự tạo |

- Clip đầu V1 có comp Fusion: MediaIn → Merge1 ← `TieuDe` (Text+ "PHO MAI & RAU CU") → MediaOut1.
- Render Queue có 2 job chưa render (YouTube 1080p, TikTok 1080p).
- Bin: `01 Footage`, `02 Audio`, `03 Nhac`, `04 Do hoa`, `05 Timelines`.
- Trang Photo cần ảnh tĩnh: xuất vài still từ footage ra `/Users/mac/davinci/stills/` rồi nạp vào.

## 3. Danh sách ảnh cần chụp

Khuôn mỗi mục: [tools/shots/FORMAT.md](tools/shots/FORMAT.md). Ảnh lưu vào `assets/img/`, rồi nhúng vào đúng heading ghi trong mục.

| Khu | File danh sách | Số mục | Trạng thái |
|---|---|---|---|
| Cut | [tools/shots/cut.md](tools/shots/cut.md) | 38 | P1/P2 tự chụp xong (17 ảnh); còn 8 ảnh P1/P2 chụp tay — xem mục 5 |
| Photo | [tools/shots/photo.md](tools/shots/photo.md) | 30 | **Chưa làm** — cần người dùng quyết định ảnh + dựng album (xem mục 5) |
| Fusion | [tools/shots/fusion.md](tools/shots/fusion.md) | 35 | P1/P2 tự chụp xong (12 ảnh); còn 14 ảnh P1/P2 chụp tay — xem mục 5 |
| Fairlight | `tools/shots/fairlight.md` | — | **Chưa viết** |
| Deliver | `tools/shots/deliver.md` | — | **Chưa viết** |
| Media | `tools/shots/media.md` | — | **Chưa viết** |
| Edit | `tools/shots/edit.md` | — | **Chưa viết** |
| Color | `tools/shots/color.md` | — | **Chưa viết** |
| Bắt đầu + Luồng | `tools/shots/start-flows.md` | — | **Chưa viết** |

Gợi ý cho các file chưa viết (đọc từng trang, đề xuất ảnh cắt vùng cho mỗi nút/panel được mô tả):

- **Fairlight:** cột kênh Mixer, cửa sổ Dialogue Leveler, Ducker, hộp Normalize Audio Levels, Noise Reduction, EQ, Dynamics, Loudness meter, hộp Patch Input/Output khi thu giọng, automation, tay nắm fade trên clip. Đã có: `page-fairlight.png`, `fairlight-effects.png`.
- **Deliver:** menu Preset xổ ra, form rút gọn (preset YouTube), ba tab Video/Audio/File của Custom Export, Advanced Settings mở rộng, Subtitle Settings, Render Queue có job, đang render, Quick Export, hộp lưu preset, menu Entire Timeline / In/Out Range. Đã có: `page-deliver.png`.
- **Media:** Media Storage, Media Pool dạng list/thumbnail, menu chuột phải bin, hộp luật Smart Bin, hỏi đổi frame rate khi nạp, Clip Attributes, Metadata, Clone Tool, Relink, Generate Optimized/Proxy. Đã có: `page-media.png`.
- **Edit:** toolbar timeline, đầu track, Timeline View Options, overlay khi kéo clip vào Viewer, con trỏ ripple/roll, Inspector tab Video, menu tốc độ trên clip, Effects Library, Text+ Inspector, curve editor keyframe, track phụ đề, hộp Compound Clip, multicam, Edit Index. Đã có: `page-edit.png`.
- **Color:** Primaries ở chế độ Color Wheels (ảnh `color-pal-primaries.png` hiện đang ở chế độ Color Bars — chụp lại), ống hút cân bằng trắng, kết quả `⇧H` của Qualifier, Power Window trên viewer, đồ thị Tracker, từng scope (Parade, Waveform, Vectorscope, Histogram), menu chuột phải node, Gallery có still, LUT Browser, Color Management trong Project Settings, ví dụ Hue vs Sat, wipe/split screen. Đã có: `page-color.png`, `color-6-nodes.png`, 15 ảnh `color-pal-*.png`.
- **Bắt đầu + Luồng:** cửa sổ Project Manager, Project Settings → Master Settings, Color Management, Preferences auto save, thanh trang dưới đáy; mỗi bước chính của 4 luồng ở `03-luong/` một ảnh kết quả.

## 4. Nội dung

Nội dung các trang đã viết xong. Khi nhúng ảnh, giữ nguyên heading đang có (trang khác link tới anchor). Thêm trang mới thì cập nhật `SUMMARY.md`. Xong chạy `python3 tools/checklinks.py`.

Hai điểm nên kiểm tra lại trên Resolve khi chụp:
- **Analyze clips for people** (nhận diện khuôn mặt trong Media Pool) đang ghi là `Studio`, nhưng manual không ghi.
- Số bản backup mặc định trong **Preferences → Project Save and Load** (manual ghi hai bộ số khác nhau) — xem `01-bat-dau/tao-du-an.md`.

## 5. Tiến độ (phiên tự chụp bằng MCP)

Theo thoả thuận: ưu tiên **P1 + P2**, bỏ P3. Ảnh nào tự động hoá được thì đã chụp + nhúng; ảnh cần thao tác chuột tay (kéo-giữ, hover, thu âm, vẽ, track, panel khó) thì liệt kê dưới đây kèm thao tác — các bước đầy đủ đã có sẵn trong `tools/shots/{cut,fusion}.md`.

### Đã chụp xong và nhúng (29 ảnh)
- **Cut (17):** CUT-01, 05, 07, 08, 09, 10, 11, 12, 26, 29, 30, 31, 32, 34, 35, 37, 38.
- **Fusion (12):** FUS-01, 02, 05, 06, 07, 08, 10, 13, 17, 18, 19, 24.

### Lưu ý thay đổi project
- Đã **thêm keyframe Center cho `TieuDe`** (comp clip 1): chữ tiêu đề trượt từ trái vào giữa trong khung 0→30 (modifier `Path1`). Việc này để chụp được FUS-24 và khớp ví dụ keyframe ở README Fusion. **Giữ hay bỏ tuỳ bạn** (bỏ: chọn TieuDe → Layout → xoá keyframe Center, hoặc Undo).

### Còn phải chụp tay — Cut (8 ảnh P1/P2)
| ID | Ưu | Vì sao phải tay | Thao tác chính |
|---|---|---|---|
| CUT-03 | P1 | Nút chế độ Viewer là overlay chỉ hiện khi rê chuột — `screencapture` không bắt được | Rê chuột lên góc trên trái Viewer, chụp màn hình tay |
| CUT-14 | P1 | Smart Indicator nhấp nháy, cần đứng yên vài giây | Đặt con trỏ sát điểm cắt, chọn clip Media Pool, chờ icon sáng |
| CUT-19 | P1 | Nút Source Tape sáng + thumbnail sáng là trạng thái hover | Bấm Source Tape, bấm clip trại cừu, chụp tay |
| CUT-13 | P2 | Rê chuột trên thumbnail + bấm I/O rồi giữ chuột | Theo bước CUT-13 |
| CUT-16 | P2 | Cần chọn clip nguồn trong bin 01 Footage, đặt I/O, bấm Place On Top | Chụp xong `⌘Z` |
| CUT-18 | P2 | **Không thấy icon Audio Only / Video Only ở layout chuẩn Cut 21 free** | Kiểm tra lại (có thể chỉ hiện khi đang kéo clip); nếu không có thì bỏ ảnh |
| CUT-24 | P2 | Kéo-giữ mép clip + chụp hẹn giờ | `⌘⇧5` → Timer 5s |
| CUT-36 | P2 | Thu Voiceover cần quyền micro (macOS hỏi) | Tự cho phép micro rồi chụp |

### Còn phải chụp tay — Fusion (14 ảnh P1/P2)
| ID | Ưu | Vì sao phải tay | Thao tác chính |
|---|---|---|---|
| FUS-21 | P1 | Dựng ví dụ Shading 3 lớp (viền + bóng) | Theo bước FUS-21 |
| FUS-26 | P1 | Panel Keyframes khó thao tác tự động (Center đã có keyframe sẵn) | Bấm **Keyframes**, mở tam giác `TieuDe` → hàng Center, zoom-fit |
| FUS-27 | P1 | Panel Spline khó thao tác tự động | Bấm **Spline**, tick Center X, `⌘F` |
| FUS-30 | P1 | Vẽ Polygon từng điểm trên Viewer | Comp thử clip 2, thêm Polygon, bấm điểm |
| FUS-31 | P1 | Đặt ô track bằng tay | Comp thử clip 2, thêm Tracker, kéo ô track |
| FUS-32 | P1 | Track Forward chạy lâu | Tiếp FUS-31, bấm Track Forward |
| FUS-34 | P1 | Dựng Delta Keyer + ống hút màu | Comp thử clip 2 |
| FUS-03 | P2 | Checker underlay + phím `A`, ghép 2 ảnh | Theo bước FUS-03 |
| FUS-15 | P2 | Dựng lower-third (Background+Rectangle+Merge+Text) | Comp thử clip 2 |
| FUS-25 | P2 | Đường chuyển động trên Viewer (Center đã keyframe) | Chọn TieuDe, Viewer 2 xem MediaOut1, con trỏ giữa 2 keyframe |
| FUS-28 | P2 | `⇧L`/`⇧S` trong Spline Editor | Tiếp FUS-27 |
| FUS-29 | P2 | Kéo Ellipse quanh mặt người | Comp thử clip 2: MediaIn→Blur→MediaOut, thêm Ellipse |
| FUS-33 | P2 | Chuỗi menu Connect To | Tiếp FUS-32 |
| FUS-35 | P2 | Tab Matte + phím `A` | Tiếp FUS-34 |

### Trang Photo — chưa làm (cần bạn)
Trang Photo (30 ảnh) **chưa bắt đầu** vì vướng hai việc cần bạn quyết:
1. **Ảnh riêng tư:** phần lớn ảnh demo lấy từ `/Users/mac/davinci/uyen/` (ảnh cá nhân của bạn) và sẽ **xuất hiện công khai trong sách hướng dẫn**. Mình không tự chọn ảnh của bạn để đăng. Bạn cần chọn ~8–12 ảnh JPG thấy OK để công khai (hoặc dùng cách thay thế: xuất vài still từ footage demo — xem mục "Chuẩn bị chung" trong `tools/shots/photo.md`).
2. **Dựng sẵn:** nạp `IMG_7912.CR3` + các ảnh JPG đã chọn, tạo **New Photo Album "Demo - Anh"**, thêm ảnh vào album (các bước ở đầu `tools/shots/photo.md`).

Xong hai việc đó, báo mình — phần lớn ảnh Photo P1/P2 là panel Inspector/menu/hộp thoại, tự chụp được.

### Lưu ý kỹ thuật cho phiên sau
- **Bàn phím tiếng Việt (Telex) làm hỏng chữ gõ qua `osascript keystroke`** (ví dụ gõ `r` sau nguyên âm thành dấu hỏi). Khi cần gõ chữ vào ô: dùng `printf '…' | pbcopy` rồi `⌘V` (dán không qua bộ gõ). Gõ **số** thì bình thường.
- Nếu lỡ bấm **Undock** trên panel Keyframes/Spline (icon ở góc panel), layout loạn: **Workspace → Reset UI Layout** để dock lại.
