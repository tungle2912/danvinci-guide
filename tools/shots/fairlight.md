# Danh sách ảnh cần chụp — trang Fairlight (`02-trang/fairlight/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-fairlight.png` (toàn cửa sổ, nhúng ở README) và `fairlight-effects.png` (thư viện hiệu ứng, nhúng ở `giao-dien.md`). Các hình `assets/diagrams/fairlight-*.svg` là sơ đồ vẽ (bố cục trang, đường đi tín hiệu, thứ tự hiệu ứng cho giọng, mức đích theo nền tảng, ducking) — các mục dưới đây bổ sung ảnh thật bên cạnh sơ đồ, không thay sơ đồ.

**Chuẩn bị chung:** mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps; V1 có 6 clip LOG 4K; A1 "Giong noi", A2 "Nhac nen"). Sang trang **Fairlight** (icon nốt nhạc, thứ 7 trong hàng icon trang dưới đáy, ngay trước Deliver; bản 21 không dùng ⇧7 để chuyển trang). Cửa sổ Resolve phóng toàn màn hình, bật **Mixer** ở toolbar phải. Sau mỗi ảnh có thay đổi hiệu ứng, mức hay automation thì `⌘Z` hoặc gỡ plugin để về trạng thái gốc.

---

### FAI-01 — `fairlight-mixer-strip.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/mixer-va-track-fx.md` — ngay sau heading `### Các mục trong cột`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** Mixer đang mở. Menu ba chấm của Mixer → bật hiện nhãn các mục (Show Labels hoặc tên tương đương trong bản 21). Gắn một plugin bất kỳ (ví dụ EQ) vào ô Effects của A1 để ô đó có chữ.
- **Khung chụp:** chỉ một vùng — cột kênh A1 "Giong noi" từ ô Input trên cùng tới fader và tên track dưới cùng, kèm một nửa cột A2 để thấy ranh giới cột.
- **Cần thấy rõ trong ảnh:** Input, Track FX (Dial Lev, Ducker, Voice Iso), Effects có một plugin, Dynamics, EQ, Pan, Bus Sends, nút M/S/R, fader và số dB.
- **Alt + chú thích:** `![Một cột kênh trong Mixer Fairlight](../../assets/img/fairlight-mixer-strip.png)` — *Đọc từ trên xuống: tiếng đi qua các mục theo đúng thứ tự này rồi mới tới fader.*

### FAI-02 — `fairlight-dialogue-leveler.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/mixer-va-track-fx.md` — ngay sau heading `## Dialogue Leveler — giọng đều không cần chỉnh tay`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** ở cột A1, bấm ô **Dial Lev** trong mục Track FX để mở bảng. Bật plugin. Bấm phát vài giây ở đoạn có lời cho đồ thị có sóng.
- **Khung chụp:** chỉ một vùng — riêng cửa sổ Dialogue Leveler.
- **Cần thấy rõ trong ảnh:** nút bật plugin, ô preset, các tuỳ chọn tick (Reduce Background…), thanh mức đích, đồ thị có đường mức đang chạy.
- **Alt + chú thích:** `![Bảng Dialogue Leveler](../../assets/img/fairlight-dialogue-leveler.png)` — *Bật plugin, chọn preset, rồi mới tinh chỉnh từng ô.*

### FAI-03 — `fairlight-ducker.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/mixer-va-track-fx.md` — ngay sau heading `## Ducker — nhạc tự nhỏ khi có lời`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** ở cột A2 "Nhac nen", bấm ô **Ducker** trong Track FX. Bật plugin, chọn nguồn điều khiển là A1 "Giong noi". Phát một đoạn có lời để thấy mức nhạc bị kéo xuống.
- **Khung chụp:** chỉ một vùng — cửa sổ Ducker, kèm cột A2 trong Mixer nếu vừa khung.
- **Cần thấy rõ trong ảnh:** ô chọn nguồn (A1), các núm mức giảm, Attack, Release, đồng hồ cho thấy nhạc đang bị hạ.
- **Alt + chú thích:** `![Bảng Ducker trên track nhạc](../../assets/img/fairlight-ducker.png)` — *Ducker gắn ở track nhạc, nghe track lời để biết lúc nào cần hạ nhạc.*

### FAI-04 — `fairlight-normalize-dialog.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/mixer-va-track-fx.md` — ngay sau heading `## Normalize — cân đều các clip`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** chọn các clip trên A1 → chuột phải → **Normalize Audio Levels**. Mở ô **Normalization Mode** cho thấy chuẩn đang chọn. Chụp xong bấm **Cancel**.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát hộp thoại.
- **Cần thấy rõ trong ảnh:** Normalization Mode, Target Level, tuỳ chọn Independent/Relative, nút Normalize.
- **Alt + chú thích:** `![Hộp thoại Normalize Audio Levels](../../assets/img/fairlight-normalize-dialog.png)` — *Chọn chuẩn đo, đặt mức đích, rồi bấm Normalize.*

### FAI-05 — `fairlight-common-fx-header.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/lam-sach-giong.md` — ngay sau heading `### Nút chung của mọi Fairlight FX`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** kéo **EQ** (Fairlight FX) vào ô Effects của A1 để mở cửa sổ plugin.
- **Khung chụp:** chỉ một vùng — dải đầu cửa sổ plugin, khoảng 600 × 80 px.
- **Cần thấy rõ trong ảnh:** ô Preset với dấu + và hai mũi tên trước/sau, nút A/B cùng mũi tên copy, nút Reset, nút bật/tắt plugin.
- **Alt + chú thích:** `![Dải nút đầu cửa sổ Fairlight FX](../../assets/img/fairlight-common-fx-header.png)` — *Mọi Fairlight FX đều có Preset, A/B và Reset ở đây.*

### FAI-06 — `fairlight-noise-reduction.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/lam-sach-giong.md` — ngay sau heading `## Noise Reduction — giảm ồn nền`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** cần thêm media — một clip giọng có ồn nền rõ (quạt, máy lạnh, xe) dài trên 10 giây, có khoảng lặng ở đầu. Đặt lên A1, gắn **Noise Reduction** vào ô Effects, phát đoạn ồn với **Auto Speech Mode** để đồ thị hiện phổ.
- **Khung chụp:** chỉ một vùng — riêng cửa sổ Noise Reduction.
- **Cần thấy rõ trong ảnh:** nút Auto Speech Mode / Manual, Learn, đồ thị phổ có hai đường (tín hiệu và mức ồn), Threshold, Attack, Sensitivity, Ratio, Dry/Wet.
- **Alt + chú thích:** `![Cửa sổ Noise Reduction đang lọc ồn](../../assets/img/fairlight-noise-reduction.png)` — *Đường dưới là mức ồn Resolve học được; phần dưới đường đó bị giảm.*

### FAI-07 — `fairlight-eq-voice.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/lam-sach-giong.md` — ngay sau heading `## EQ — 3 thao tác cho giọng nói`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** ở cột A1, nhấp đúp ô **EQ** trong Mixer. Bật band thấp kiểu High Pass khoảng 80 Hz, cắt nhẹ một band quanh 300 Hz, nâng nhẹ một band quanh 4 kHz.
- **Khung chụp:** chỉ một vùng — cửa sổ EQ của track.
- **Cần thấy rõ trong ảnh:** đường cong EQ với ba điểm vừa chỉnh, dãy band bên dưới có ô kiểu band, tần số, gain, Q.
- **Alt + chú thích:** `![EQ cho giọng nói với ba thao tác](../../assets/img/fairlight-eq-voice.png)` — *Cắt dưới 80 Hz, bớt đục quanh 300 Hz, nâng rõ quanh 4 kHz.*

### FAI-08 — `fairlight-de-esser.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fairlight/lam-sach-giong.md` — ngay sau heading `## De-Esser — bớt tiếng "s" chói`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** gắn **De-Esser** vào ô Effects của A1, phát đoạn có nhiều âm "s".
- **Khung chụp:** chỉ một vùng — riêng cửa sổ De-Esser.
- **Cần thấy rõ trong ảnh:** ô tần số, Range, Amount, đồng hồ mức giảm đang nhảy.
- **Alt + chú thích:** `![Cửa sổ De-Esser](../../assets/img/fairlight-de-esser.png)` — *Đồng hồ giảm chỉ nhảy khi có âm "s" — nhảy liên tục là đặt quá tay.*

### FAI-09 — `fairlight-dynamics.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/lam-sach-giong.md` — ngay sau heading `## Dynamics — nén, chặn, cổng`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** ở cột A1, nhấp đúp ô **Dynamics** trong Mixer. Bật Compressor, Ratio khoảng 3:1. Phát đoạn có lời.
- **Khung chụp:** chỉ một vùng — cửa sổ Dynamics.
- **Cần thấy rõ trong ảnh:** ba khối Expander/Gate, Compressor, Limiter; Compressor đang bật; đồ thị đường truyền và đồng hồ gain reduction.
- **Alt + chú thích:** `![Cửa sổ Dynamics của track](../../assets/img/fairlight-dynamics.png)` — *Ba khối trong một cửa sổ; bật khối nào thì khối đó mới tác động.*

### FAI-10 — `fairlight-loudness-meter.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/loudness-va-xuat.md` — ngay sau heading `## Loudness meter — đo độ to cảm nhận`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** đặt chuẩn loudness là YouTube (−14). Phát cả timeline từ đầu tới cuối để ô Integrated có số.
- **Khung chụp:** chỉ một vùng — đồng hồ Loudness ngoài cùng bên phải dải Meters, kèm đồng hồ Control Room cạnh nó.
- **Cần thấy rõ trong ảnh:** cột M, các ô Short, Short Max, Range, Integrated có số và màu; đồng hồ Control Room màu vàng.
- **Alt + chú thích:** `![Loudness meter sau khi phát hết timeline](../../assets/img/fairlight-loudness-meter.png)` — *Integrated là con số chính để so với chuẩn của nền tảng.*

### FAI-11 — `fairlight-loudness-options.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/loudness-va-xuat.md` — ngay sau heading `### Đặt chuẩn YouTube`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** bấm menu tuỳ chọn của Loudness meter cho xổ danh sách chuẩn (EBU R128, ATSC A/85, YouTube…).
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt quanh đồng hồ và menu.
- **Cần thấy rõ trong ảnh:** dòng YouTube trong danh sách chuẩn, các lệnh Start/Pause/Reset nếu cùng menu.
- **Alt + chú thích:** `![Menu chọn chuẩn của Loudness meter](../../assets/img/fairlight-loudness-options.png)` — *Chọn YouTube để mức đích là −14 LUFS.*

### FAI-12 — `fairlight-analyze-audio-level.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fairlight/loudness-va-xuat.md` — ngay sau heading `### Đo nhanh không cần phát`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** chuột phải clip trên A2 → **Analyze Audio Level** → chọn chuẩn YouTube → chạy phân tích. Chụp khi đã có kết quả.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát hộp thoại.
- **Cần thấy rõ trong ảnh:** chuẩn đang chọn, kết quả đo đặt cạnh mức đích.
- **Alt + chú thích:** `![Kết quả Analyze Audio Level của clip nhạc](../../assets/img/fairlight-analyze-audio-level.png)` — *Biết clip to cỡ nào mà không phải phát hết.*

### FAI-13 — `fairlight-bus-limiter.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/loudness-va-xuat.md` — ngay sau heading `## Limiter trên Bus — chặn trần`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** trong Mixer, gắn **Limiter** (Fairlight FX) vào ô Effects của cột **Bus 1**, đặt trần −1 dBTP. Phát đoạn to nhất.
- **Khung chụp:** chỉ một vùng — cửa sổ Limiter, kèm cột Bus 1 trong Mixer ở bên cạnh.
- **Cần thấy rõ trong ảnh:** plugin nằm ở cột Bus 1 (không phải A1/A2), ô trần, đồng hồ mức giảm.
- **Alt + chú thích:** `![Limiter gắn trên Bus 1](../../assets/img/fairlight-bus-limiter.png)` — *Gắn ở Bus 1 để chặn trần cho cả bản mix.*

### FAI-14 — `fairlight-patch-input.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fairlight/thu-am-va-chinh-clip.md` — ngay sau heading `### Bước 1 — Nối mic vào track (patch input)`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** menu **Fairlight → Patch Input/Output**. Bên nguồn chọn mic của máy, bên đích chọn track A1. Không bấm Patch, chụp xong đóng cửa sổ.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt sát cửa sổ Patch Input/Output.
- **Cần thấy rõ trong ảnh:** ô chọn loại nguồn và đích, nguồn mic đang sáng, ô A1 đang sáng, nút Patch góc dưới phải.
- **Alt + chú thích:** `![Cửa sổ Patch Input/Output](../../assets/img/fairlight-patch-input.png)` — *Chọn mic bên trái, chọn track bên phải, rồi bấm Patch.*

### FAI-15 — `fairlight-clip-gain.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/thu-am-va-chinh-clip.md` — ngay sau heading `## Clip gain — to nhỏ từng clip`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** tăng chiều cao track A1. Rê chuột lên đường gain ngang trên một clip lời và kéo xuống vài dB để hiện số.
- **Khung chụp:** chỉ một vùng — một clip trên A1 phóng to, khoảng 600 × 200 px.
- **Cần thấy rõ trong ảnh:** đường gain ngang trên dạng sóng, con số dB khi kéo.
- **Alt + chú thích:** `![Đường clip gain trên clip lời](../../assets/img/fairlight-clip-gain.png)` — *Kéo đường ngang lên xuống để đổi mức to của riêng clip đó.*

### FAI-16 — `fairlight-fade-handles.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fairlight/thu-am-va-chinh-clip.md` — ngay sau heading `### Fade đầu, fade cuối`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** rê chuột lên clip nhạc trên A2 cho hiện tay nắm fade ở hai góc trên; kéo tay nắm đầu vào khoảng 1 giây.
- **Khung chụp:** chỉ một vùng — đầu clip trên A2.
- **Cần thấy rõ trong ảnh:** tay nắm fade ở góc trên, đường fade cong, dạng sóng mờ dần.
- **Alt + chú thích:** `![Tay nắm fade ở đầu clip nhạc](../../assets/img/fairlight-fade-handles.png)` — *Kéo tay nắm ở góc trên clip vào trong để tạo fade.*

### FAI-17 — `fairlight-automation-lane.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fairlight/thu-am-va-chinh-clip.md` — ngay sau heading `### Vẽ automation`
- **Trang Resolve:** Fairlight
- **Chuẩn bị:** bật Automation ở thanh công cụ timeline, cho track A2 hiện đường Volume; thêm 4 điểm hạ nhạc ở một đoạn có lời.
- **Khung chụp:** chỉ một vùng — track A2 với đường automation, kèm track A1 phía trên để thấy đoạn lời.
- **Cần thấy rõ trong ảnh:** đường Volume với 4 điểm, đoạn hạ nhạc trùng với clip lời trên A1.
- **Alt + chú thích:** `![Đường automation âm lượng trên track nhạc](../../assets/img/fairlight-automation-lane.png)` — *Bốn điểm tạo một đoạn hạ nhạc đúng chỗ có lời.*
