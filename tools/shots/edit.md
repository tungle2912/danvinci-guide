# Danh sách ảnh cần chụp — trang Edit (`02-trang/edit/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-edit.png` (toàn cửa sổ, đã nhúng ở README). Các hình `assets/diagrams/edit-*.svg` là sơ đồ vẽ, không phải ảnh chụp — các mục dưới đây bổ sung ảnh thật bên cạnh sơ đồ, không thay sơ đồ.

**Chuẩn bị chung:** mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps; V1 có 6 clip LOG 4K — đĩa phô mai/rau củ và cô gái ở trại cừu Kazakhstan; A1 "Giong noi", A2 "Nhac nen"; clip 1 có Fusion Text+ "PHO MAI & RAU CU"). Sang trang **Edit** (icon Edit trong hàng icon dưới đáy cửa sổ). Cửa sổ Resolve phóng toàn màn hình. Sau mỗi ảnh có thay đổi timeline thì `⌘Z` hoàn tác về trạng thái gốc.

---

### EDT-01 — `edit-track-header.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/edit/giao-dien.md` — ngay sau heading `### Nút ở đầu mỗi track — từ trái sang phải`
- **Trang Resolve:** Edit
- **Chuẩn bị:** mở một clip trong bin `01 Footage` lên Source Viewer (bấm đúp) để cột ô xanh nguồn hiện ở đầu track. Kéo nới cao V1, A1 cho đủ chỗ thấy hết nút. Tắt ô đỏ Destination của A2 (bấm vào ô) để ảnh có cả ô sáng lẫn ô tối.
- **Khung chụp:** chỉ một vùng — cột đầu track bên trái timeline, từ V1 tới A2.
- **Cần thấy rõ trong ảnh:** ô xanh nguồn (V1, A1), ô đỏ Destination (V1, A1 sáng, A2 tối), nút Lock, Sync Lock, Solo (track tiếng), Mute/Enable, tên track "Giong noi", "Nhac nen".
- **Alt + chú thích:** `![Đầu track trang Edit, ô xanh nguồn và ô đỏ đích](../../assets/img/edit-track-header.png)` — *Ô đỏ A2 đang tối nên lệnh cắt, xoá bỏ qua track nhạc.*

### EDT-02 — `edit-timeline-toolbar.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/giao-dien.md` — ngay sau heading `## Thanh công cụ trên timeline`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chế độ chuột Selection (`A`), Snapping và Linked Selection đang bật. Không chọn clip nào.
- **Khung chụp:** chỉ một vùng — toàn bộ dải toolbar ngay trên timeline, từ nút Timeline View Options tới thanh trượt zoom và nút nghe ngoài cùng bên phải.
- **Cần thấy rõ trong ảnh:** bốn nút chế độ chuột (Selection, Trim, Dynamic Trim, Blade), ba nút edit, Snapping, Linked Selection, Position Lock, nút Flag/Marker, thanh zoom.
- **Alt + chú thích:** `![Thanh công cụ trên timeline trang Edit](../../assets/img/edit-timeline-toolbar.png)` — *Nút đang sáng là chế độ chuột đang dùng.*

### EDT-03 — `edit-viewer-overlay.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `### Kéo thả`
- **Trang Resolve:** Edit
- **Chuẩn bị:** mở clip 2 trong bin `01 Footage` lên Source Viewer. Kéo hình từ Source Viewer sang Timeline Viewer, giữ chuột, chưa thả — lớp phủ bảy ô kiểu edit hiện ra.
- **Khung chụp:** chỉ một vùng — Timeline Viewer (bên phải) đang hiện lớp phủ.
- **Cần thấy rõ trong ảnh:** bảy ô Insert, Overwrite, Replace, Fit to Fill, Place On Top, Append, Ripple Overwrite; ô dưới con trỏ đang sáng.
- **Alt + chú thích:** `![Lớp phủ bảy kiểu edit trên Timeline Viewer](../../assets/img/edit-viewer-overlay.png)` — *Thả clip vào ô nào thì Resolve dùng kiểu edit đó.*

### EDT-04 — `edit-trim-2up.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `### Ripple — kéo mép, phần sau dồn theo`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chế độ Trim (`T`). Giữ chuột kéo mép phải clip 2 trên V1 sang trái vài khung, chưa thả — Viewer chuyển sang hiển thị 2 hình (mặc định Resolve gộp thành một Viewer lớn khi trim).
- **Khung chụp:** chỉ một vùng — vùng Viewer và phần timeline quanh điểm nối đang kéo.
- **Cần thấy rõ trong ảnh:** hai hình cạnh nhau (khung cuối clip 2, khung đầu clip 3), mép đang kéo được tô sáng, ô báo số khung đang dời.
- **Alt + chú thích:** `![Viewer hiện hai hình khi ripple trim](../../assets/img/edit-trim-2up.png)` — *Bên trái là khung cuối clip trước, bên phải là khung đầu clip sau.*

### EDT-05 — `edit-trim-4up.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `### Slip — đổi nội dung bên trong`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chế độ Trim (`T`). Giữ chuột kéo phần giữa (nửa trên) clip 3 trên V1 sang phải, chưa thả — Viewer hiện 4 hình.
- **Khung chụp:** chỉ một vùng — vùng Viewer và clip 3 trên timeline (thấy khung bóng của phần media thừa).
- **Cần thấy rõ trong ảnh:** bốn hình: khung cuối clip trước, khung đầu và khung cuối mới của clip 3, khung đầu clip sau; khung bóng media thừa trên timeline.
- **Alt + chú thích:** `![Viewer hiện bốn hình khi slip clip](../../assets/img/edit-trim-4up.png)` — *Hai hình giữa là khung đầu và khung cuối mới của clip đang slip.*

### EDT-06 — `edit-dynamic-trim.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `### Trim khi đang phát — Dynamic Trim`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chế độ Trim (`T`), bấm chọn điểm nối giữa clip 2 và clip 3 trên V1, rồi bấm `W`.
- **Khung chụp:** chỉ một vùng — toolbar timeline (nút Dynamic Trim) và đoạn timeline quanh điểm nối.
- **Cần thấy rõ trong ảnh:** nút Dynamic Trim sáng, con trỏ phát chuyển vàng, điểm nối đang chọn.
- **Alt + chú thích:** `![Dynamic Trim đang bật, con trỏ vàng](../../assets/img/edit-dynamic-trim.png)` — *Con trỏ vàng là dấu hiệu J K L sẽ trim chứ không phát.*

### EDT-07 — `edit-precision-trim.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `### Precision Trim Editor — bấm đúp điểm nối`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chế độ Selection (`A`), bấm đúp điểm nối giữa clip 2 và clip 3 trên V1.
- **Khung chụp:** chỉ một vùng — vùng Viewer đang hiện Precision Trim Editor (thay chỗ hai Viewer), kèm thanh nút dưới Viewer.
- **Cần thấy rõ trong ảnh:** dải phim clip trước ở trên, clip sau ở dưới, số khung trên từng ô, tay nắm trắng giữa hai dải, hai nút trim 1 khung hai bên nút phát.
- **Alt + chú thích:** `![Precision Trim Editor ở điểm nối clip 2 và 3](../../assets/img/edit-precision-trim.png)` — *Thấy từng khung hai bên điểm nối để trim chính xác.*

### EDT-08 — `edit-jl-cut-timeline.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `## J-cut và L-cut`
- **Trang Resolve:** Edit
- **Chuẩn bị:** cần clip có tiếng gắn liền hình. Kéo clip 4 xuống V2/A3 có tiếng gốc (hoặc dùng clip có tiếng đi kèm). `⌥`-bấm giữa điểm nối phần tiếng giữa hai clip, bấm `,` vài lần cho tiếng vào sớm (J-cut). Nới cao track tiếng, bật dạng sóng.
- **Khung chụp:** chỉ một vùng — đoạn timeline quanh điểm nối, đủ thấy track hình và track tiếng.
- **Cần thấy rõ trong ảnh:** điểm nối tiếng lệch so với điểm nối hình; dạng sóng.
- **Alt + chú thích:** `![J-cut trên timeline, tiếng vào trước hình](../../assets/img/edit-jl-cut-timeline.png)` — *Điểm nối tiếng nằm trước điểm nối hình: J-cut.*

### EDT-09 — `edit-marker-dialog.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/dung-va-cat.md` — ngay sau heading `## Marker`
- **Trang Resolve:** Edit — hộp thoại
- **Chuẩn bị:** đặt con trỏ trên clip 3, bấm `M` hai lần. Gõ tên "Doi nhac" vào ô Name, chọn màu Yellow.
- **Khung chụp:** hộp thoại marker — cửa sổ riêng, cần chụp toàn màn hình rồi cắt.
- **Cần thấy rõ trong ảnh:** ô Name, Notes, Duration, ô chọn màu, nút Delete, Done.
- **Alt + chú thích:** `![Hộp thoại marker](../../assets/img/edit-marker-dialog.png)` — *Bấm `M` hai lần để mở; nút Delete xoá marker.*

### EDT-10 — `edit-inspector-video.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/edit/inspector.md` — ngay sau heading `## Tab Video`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chọn clip 2 trên V1, mở Inspector (nút góc trên phải), tab **Video**. Đặt Zoom 1.200 để có giá trị khác mặc định.
- **Khung chụp:** chỉ một vùng — panel Inspector bên phải, từ hàng tab tới hết nhóm Cropping.
- **Cần thấy rõ trong ảnh:** hàng tab Video / Audio / Effects / Transition / Image / File, nhóm Transform (Zoom, Position, Rotation Angle, Anchor Point, Pitch, Yaw, Flip), nút keyframe và nút reset của từng thông số.
- **Alt + chú thích:** `![Tab Video của Inspector, nhóm Transform](../../assets/img/edit-inspector-video.png)` — *Mỗi thông số có nút keyframe (hình thoi) và nút reset ở mép phải.*

### EDT-11 — `edit-retime-controls.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/inspector.md` — ngay sau heading `### Speed ramp — nhanh chậm trong cùng một clip`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chọn clip 5 trên V1, bấm `⌘R`. Bấm mũi tên xổ dưới số tốc độ → **Add Speed Point** ở giữa clip, kéo nửa sau lên 200%.
- **Khung chụp:** chỉ một vùng — clip 5 trên timeline, phóng to cho rõ thanh tốc độ.
- **Cần thấy rõ trong ảnh:** thanh tốc độ trên clip, hai đoạn 100% và 200%, điểm speed point ở giữa, mũi tên xổ menu.
- **Alt + chú thích:** `![Retime Controls trên clip, hai đoạn tốc độ](../../assets/img/edit-retime-controls.png)` — *Kéo đỉnh trên của đoạn sau để đổi tốc độ đoạn đó.*

### EDT-12 — `edit-keyframe-editor.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/chu-va-hieu-ung.md` — ngay sau heading `### Keyframe Editor — xem mọi keyframe`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chọn clip 1 trên V1, trong Inspector đặt keyframe Zoom ở đầu clip (1.000) và cuối clip (1.200). Bấm nút **Keyframes** (hình thoi) góc dưới phải clip trên timeline.
- **Khung chụp:** chỉ một vùng — clip 1 trên timeline cùng dải Keyframe Editor mở bên dưới.
- **Cần thấy rõ trong ảnh:** nút Keyframes trên clip, dải keyframe nhóm Transform, hai hình thoi keyframe, nút mở Curve Editor.
- **Alt + chú thích:** `![Keyframe Editor dưới clip 1](../../assets/img/edit-keyframe-editor.png)` — *Mỗi hình thoi là một keyframe; kéo để dời theo thời gian.*

### EDT-13 — `edit-curve-editor.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/chu-va-hieu-ung.md` — ngay sau heading `### Curve Editor — chỉnh độ mượt`
- **Trang Resolve:** Edit
- **Chuẩn bị:** như EDT-12, rồi bấm nút **Curve Editor** (đường cong) trên clip. Chọn keyframe thứ hai, bấm nút Ease In.
- **Khung chụp:** chỉ một vùng — clip 1 và dải Curve Editor bên dưới.
- **Cần thấy rõ trong ảnh:** đường cong Zoom, keyframe đang chọn, các nút Linear / Ease In / Ease Out / Hold.
- **Alt + chú thích:** `![Curve Editor với keyframe ease](../../assets/img/edit-curve-editor.png)` — *Đường cong thoải dần khi tới keyframe: chuyển động dừng mượt.*

### EDT-14 — `edit-transition-inspector.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/chu-va-hieu-ung.md` — ngay sau heading `### Chỉnh chuyển cảnh trong Inspector`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chọn điểm nối giữa clip 1 và clip 2 trên V1, bấm `⌘T` để thêm Cross Dissolve mặc định. Bấm chọn chuyển cảnh, mở Inspector.
- **Khung chụp:** chỉ một vùng — panel Inspector đang hiện chuyển cảnh, kèm đoạn timeline có chuyển cảnh.
- **Cần thấy rõ trong ảnh:** Duration, Alignment, Start/End Ratio, Ease, Transition Curve; khối chuyển cảnh trên timeline.
- **Alt + chú thích:** `![Inspector của Cross Dissolve](../../assets/img/edit-transition-inspector.png)` — *Đổi Duration và Alignment ngay trong Inspector.*

### EDT-15 — `edit-effects-library.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/chu-va-hieu-ung.md` — ngay sau heading `## Thư viện Effects — cây thư mục`
- **Trang Resolve:** Edit
- **Chuẩn bị:** mở panel **Effects** (góc trên trái), bấm nhóm **Toolbox → Video Transitions**.
- **Khung chụp:** chỉ một vùng — panel Effects, cột cây thư mục và danh sách bên phải.
- **Cần thấy rõ trong ảnh:** các nhóm Toolbox (Video Transitions, Audio Transitions, Titles, Generators, Effects), Open FX, Audio FX, Fusion Titles; ô tìm kiếm.
- **Alt + chú thích:** `![Thư viện Effects trang Edit](../../assets/img/edit-effects-library.png)` — *Cây thư mục bên trái, danh sách hiệu ứng bên phải.*

### EDT-16 — `edit-subtitle-track.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/edit/phu-de.md` — ngay sau heading `## Gõ phụ đề tay`
- **Trang Resolve:** Edit
- **Chuẩn bị:** chuột phải đầu track → **Add Subtitle Track**, đổi tên thành "Tieng Viet". Thêm hai câu phụ đề ở clip 1 và clip 2, gõ "Pho mai va rau cu" và "Mot buoi sang o trai cuu". Chọn câu thứ hai, mở Inspector tab **Captions**.
- **Khung chụp:** toàn cửa sổ (cần thấy cùng lúc track phụ đề, Viewer có chữ và Inspector).
- **Cần thấy rõ trong ảnh:** track "Tieng Viet" trên cùng timeline với hai clip phụ đề, ô ST1, chữ phụ đề trên Timeline Viewer, tab Captions với ô nội dung và danh sách câu.
- **Alt + chú thích:** `![Track phụ đề và tab Captions](../../assets/img/edit-subtitle-track.png)` — *Gõ chữ trong tab Captions; danh sách mọi câu nằm ở cuối tab.*

### EDT-17 — `edit-subtitle-deliver.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/phu-de.md` — ngay sau heading `### Lúc render — trang Deliver`
- **Trang Resolve:** Deliver
- **Chuẩn bị:** làm như EDT-16 để timeline có track phụ đề. Sang Deliver, tab **Video**, kéo xuống cuối, tick **Export Subtitle**, Format chọn **As a separate file**, Export As **SRT**.
- **Khung chụp:** chỉ một vùng — nhóm Subtitle Settings trong Render Settings.
- **Cần thấy rõ trong ảnh:** ô Export Subtitle, Format, Export As, danh sách track phụ đề có ô tick.
- **Alt + chú thích:** `![Subtitle Settings ở trang Deliver](../../assets/img/edit-subtitle-deliver.png)` — *Chọn Burn into video để in chữ vào hình, hoặc xuất file riêng.*

### EDT-18 — `edit-compound-dialog.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/timeline-nang-cao.md` — ngay sau heading `### Cách tạo`
- **Trang Resolve:** Edit — hộp thoại
- **Chuẩn bị:** chọn clip 1 và clip 2 trên V1 (kèm Text+ ở clip 1), chuột phải → **New Compound Clip**. Gõ tên "Mo dau".
- **Khung chụp:** hộp thoại New Compound Clip — cửa sổ riêng, cần chụp toàn màn hình rồi cắt.
- **Cần thấy rõ trong ảnh:** ô Start Timecode, ô Compound clip name, nút Create.
- **Alt + chú thích:** `![Hộp thoại New Compound Clip](../../assets/img/edit-compound-dialog.png)` — *Đặt tên để dễ tìm lại compound clip trong Media Pool.*

### EDT-19 — `edit-multicam-viewer.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/edit/timeline-nang-cao.md` — ngay sau heading `### Bước 3 — cắt chọn góc`
- **Trang Resolve:** Edit
- **Chuẩn bị:** project demo không có footage nhiều góc máy. Cần thêm 2–4 clip quay cùng một cảnh từ nhiều góc, có tiếng chung (hoặc tạm dùng 4 clip demo khác nhau để minh hoạ giao diện). Chọn các clip trong Media Pool → chuột phải → **Create New Multicam Clip Using Selected Clips**, Angle Sync **Sound** (hoặc **In** với clip demo). Đưa multicam clip xuống timeline, Source Viewer chuyển sang **Multicam**, lưới 2x2.
- **Khung chụp:** chỉ một vùng — Source Viewer ở chế độ Multicam và Timeline Viewer bên cạnh.
- **Cần thấy rõ trong ảnh:** lưới 2x2 các góc có số Angle 1–4, góc đang dùng có viền đỏ (hình + tiếng) hoặc xanh, menu chọn Multicam ở góc trên Source Viewer.
- **Alt + chú thích:** `![Source Viewer ở chế độ Multicam lưới 2x2](../../assets/img/edit-multicam-viewer.png)` — *Bấm số 1–4 trong khi phát để cắt sang góc đó.*

### EDT-20 — `edit-edit-index.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/timeline-nang-cao.md` — ngay sau heading `## Edit Index — danh sách mọi điểm cắt`
- **Trang Resolve:** Edit
- **Chuẩn bị:** bấm nút **Index** góc trên trái, chọn tab **Edit Index**. Bấm một dòng ở giữa danh sách.
- **Khung chụp:** chỉ một vùng — panel Edit Index bên trái.
- **Cần thấy rõ trong ảnh:** các cột số thứ tự, Reel, Track, Source In/Out, Record In/Out; dòng đang chọn; nút ⋯.
- **Alt + chú thích:** `![Edit Index liệt kê mọi điểm cắt](../../assets/img/edit-edit-index.png)` — *Bấm một dòng là con trỏ nhảy tới clip đó trên timeline.*

### EDT-21 — `edit-timeline-view-options.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/edit/giao-dien.md` — ngay sau heading `## Timeline View Options — đổi cách timeline hiện`
- **Trang Resolve:** Edit
- **Chuẩn bị:** bấm nút **Timeline View Options** (ngoài cùng bên trái toolbar timeline) cho bảng tuỳ chọn xổ ra.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt; lấy bảng tuỳ chọn và một chút toolbar phía dưới.
- **Cần thấy rõ trong ảnh:** các kiểu hiện track hình (filmstrip, thumbnail, tên), tuỳ chọn Audio Waveforms, các thanh trượt độ cao track, nút Subtitle.
- **Alt + chú thích:** `![Bảng Timeline View Options](../../assets/img/edit-timeline-view-options.png)` — *Chọn cách hiện clip hình và bật dạng sóng tiếng ở đây.*
