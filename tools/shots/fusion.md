# Danh sách ảnh cần chụp — trang Fusion (`02-trang/fusion/`)

Khuôn mục: xem `FORMAT.md`. Ảnh đã có: `page-fusion.png` (toàn cửa sổ, README), `fusion-merge-inputs.png` (cận cảnh ba đầu vào Merge, đã nhúng ở `node-co-ban.md` mục `## Đầu vào và đầu ra` — không chụp lại). `fusion-layout.svg`, `fusion-merge.svg` là sơ đồ vẽ.

Không đề xuất ảnh cho Planar Tracker / Planar Transform / Camera Tracker / Surface Tracker: không có trong bản free 21.0.4 (trang đã ghi `Studio`). Magic Mask cũng là `Studio`.

**Chuẩn bị chung:**
1. Mở project "So tay DaVinci - Demo", timeline "Demo - Vlog" (25 fps).
2. **Comp có sẵn:** ở trang Edit đặt con trỏ lên **clip đầu tiên** của V1 (phô mai) → sang trang **Fusion**. Comp: `MediaIn1 → Merge1 ← TieuDe (Text+) → MediaOut1`. Dùng comp này cho mọi ảnh về Merge, Text+, keyframe, Spline. Trước khi thêm keyframe thử nghiệm: bật **Clips**, chuột phải thumbnail clip 1 → **Create New Composition** để làm trên bản sao; xong thì **Load** lại comp gốc và xoá bản thử.
3. **Comp thử:** cho Mask, Tracker, Delta Keyer dùng **clip thứ 2** (trại cừu, có người và chuyển động máy). Chụp xong: Clips → chuột phải → **Reset Current Composition**.
4. Workspace → Layout Presets → Fusion Presets → **Default** trước khi bắt đầu. Hai Viewer đang bật.

---

### FUS-01 — `fusion-toolbar-top.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Thanh trên cùng`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1. Chuột phải thanh trên cùng → bật hiện chữ cạnh icon. Bật Nodes và Inspector, tắt các panel khác.
- **Khung chụp:** chỉ một vùng — toàn dải thanh trên cùng (cắt làm hai nửa trái/phải ghép dọc nếu quá dài).
- **Cần thấy rõ trong ảnh:** bên trái Full Height, Media Pool, Effects, Clips, Nodes; bên phải Spline, Keyframes, Metadata, Inspector, Inspector Height.
- **Alt + chú thích:** `![Thanh nút trên cùng trang Fusion](../../assets/img/fusion-toolbar-top.png)` — *Nút bên trái mở kho clip/node, bên phải mở Spline, Keyframes, Inspector.*

### FUS-02 — `fusion-viewer-header.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `### Thanh tiêu đề Viewer`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe bấm `1` (Viewer trái xem chữ), MediaOut1 ở Viewer phải.
- **Khung chụp:** chỉ một vùng — thanh tiêu đề Viewer trái, toàn chiều ngang Viewer.
- **Cần thấy rõ trong ảnh:** menu zoom (%), tên node "TieuDe" ở giữa, nút Color/Alpha, Split Wipe, SubView, Viewer LUT, ROI, menu `...`.
- **Alt + chú thích:** `![Thanh tiêu đề Viewer trang Fusion](../../assets/img/fusion-viewer-header.png)` — *Tên giữa thanh cho biết Viewer đang xem node nào.*

### FUS-03 — `fusion-viewer-alpha.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Viewer` (đặt cuối mục, trước `### Đưa node lên Viewer`) — hoặc sau đoạn "Kênh alpha là gì" trong `### Thanh tiêu đề Viewer` nếu muốn sát nội dung
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1. Viewer trái xem TieuDe ở chế độ màu, menu `...` → bật **Checker Underlay**; chụp. Bấm vào Viewer, bấm `A` để xem alpha; chụp.
- **Khung chụp:** chỉ một vùng — riêng khung hình Viewer trái; ghép hai ảnh cạnh nhau.
- **Cần thấy rõ trong ảnh:** trái: chữ trên nền caro; phải: chữ trắng trên nền đen (alpha).
- **Alt + chú thích:** `![Text+ trên nền caro và kênh alpha](../../assets/img/fusion-viewer-alpha.png)` — *Caro là chỗ trong suốt; ở kênh alpha, trắng là đặc, đen là trong suốt.*

### FUS-04 — `fusion-view-dots.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `### Đưa node lên Viewer`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, Node Editor zoom vào khoảng 200%. Rê chuột lên node Merge1 để hiện hai chấm tròn góc dưới trái; MediaOut1 đang ở Viewer 2 (chấm trắng).
- **Khung chụp:** chỉ một vùng — cận cảnh Merge1 và MediaOut1 trong Node Editor.
- **Cần thấy rõ trong ảnh:** hai chấm xem Viewer trên Merge1; chấm trắng dưới MediaOut1.
- **Alt + chú thích:** `![Chấm xem Viewer dưới node](../../assets/img/fusion-view-dots.png)` — *Bấm chấm trái hoặc phải để đưa node lên Viewer tương ứng; chấm trắng là đang được xem.*

### FUS-05 — `fusion-time-ruler.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Time Ruler và nút phát`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, phát một lượt để có vạch cache xanh lá; dừng với con trỏ khoảng giữa.
- **Khung chụp:** chỉ một vùng — Time Ruler + hàng nút phát ngay dưới Viewer, toàn chiều ngang.
- **Cần thấy rõ trong ảnh:** hai vạch vàng In/Out, con trỏ đỏ, vạch cache xanh lá, ô vùng render (trái), ô khung hiện tại (phải), nút loa.
- **Alt + chú thích:** `![Time Ruler và nút phát trang Fusion](../../assets/img/fusion-time-ruler.png)` — *Hai vạch vàng là In/Out của clip; vạch xanh lá là khung đã cache.*

### FUS-06 — `fusion-toolbar-nodes.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Thanh công cụ dưới Time Ruler`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, rê chuột lên icon Text+ để hiện tooltip.
- **Khung chụp:** chỉ một vùng — hàng icon thanh công cụ dưới Time Ruler, toàn chiều ngang (có thể cắt hai nửa ghép dọc).
- **Cần thấy rõ trong ảnh:** nhóm Background/FastNoise/Text+/Paint; nhóm màu, mờ; nhóm Merge/ChannelBooleans/MatteControl/Resize/Transform; nhóm Rectangle/Ellipse/Polygon/BSpline; nhóm hạt; nhóm 3D; tooltip "Text+".
- **Alt + chú thích:** `![Thanh công cụ node dưới Time Ruler](../../assets/img/fusion-toolbar-nodes.png)` — *Người mới chỉ cần ba nhóm đầu và nhóm Mask.*

### FUS-07 — `fusion-inspector-header.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `### Thanh tên node — đầu Inspector`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe.
- **Khung chụp:** chỉ một vùng — đầu Inspector: trang Tools/Modifiers, thanh tên node và hàng tab icon.
- **Cần thấy rõ trong ảnh:** công tắc bật/tắt, tên "TieuDe", màu, Versions, Pin, Lock, Reset; hàng tab Text/Layout/Transform/Shading/Image/Settings.
- **Alt + chú thích:** `![Thanh tên node đầu Inspector](../../assets/img/fusion-inspector-header.png)` — *Công tắc, tên, màu, Versions, Pin, Lock, Reset của node đang chọn.*

### FUS-08 — `fusion-effects-library.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Effects Library`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** bấm **Effects** trên thanh trên; mở **Tools → Composite** (hoặc Blur); rê chuột lên một tên node để hiện mô tả.
- **Khung chụp:** chỉ một vùng — panel Effects Library (bên trái), từ ô tìm kiếm tới hết danh sách.
- **Cần thấy rõ trong ảnh:** bốn mục Tools, Open FX, Templates, LUTs; nhóm con đang mở; danh sách node.
- **Alt + chú thích:** `![Effects Library trong trang Fusion](../../assets/img/fusion-effects-library.png)` — *Kho mọi node của Fusion, chia nhóm.*

### FUS-09 — `fusion-clips-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/giao-dien.md` — ngay sau heading `## Clips — dải thumbnail`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** bấm **Clips**; chuột phải thumbnail clip 1 (viền cam).
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt dải thumbnail + menu.
- **Cần thấy rõ trong ảnh:** viền cam clip đang mở; Create New Composition, tên phiên bản (Composition 1) → Load/Delete/Rename, Reset Current Composition.
- **Alt + chú thích:** `![Dải Clips và menu chuột phải](../../assets/img/fusion-clips-menu.png)` — *Tạo thêm phiên bản comp hoặc reset về MediaIn → MediaOut.*

### FUS-10 — `fusion-select-tool.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Thêm node`
- **Trang Resolve:** Fusion (hộp Select Tool)
- **Chuẩn bị:** comp clip 1, bấm khoảng trống Node Editor, bấm `⇧Space`, gõ `blu`.
- **Khung chụp:** chỉ một vùng — hộp Select Tool nổi trên Node Editor kèm một phần node xung quanh.
- **Cần thấy rõ trong ảnh:** ô gõ có chữ "blu", danh sách gợi ý (Blur, …) với một dòng đang tô sáng.
- **Alt + chú thích:** `![Hộp Select Tool mở bằng Shift Space](../../assets/img/fusion-select-tool.png)` — *Gõ vài chữ, chọn bằng mũi tên, Return để thêm node.*
- **Ghi chú:** Esc để đóng, không thêm node.

### FUS-11 — `fusion-node-context-menu.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Xoá, tắt tạm, khoá node`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chuột phải TieuDe → rê tới **Modes** cho menu con hiện.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt node + menu.
- **Cần thấy rõ trong ảnh:** Modes → Pass Through (⌘P), Lock (⌘L), Update (⌘U); các mục Insert Tool, Replace Tool trong menu chính.
- **Alt + chú thích:** `![Menu chuột phải node, mục Modes](../../assets/img/fusion-node-context-menu.png)` — *Tắt tạm, khoá, ngừng cập nhật node.*

### FUS-12 — `fusion-node-passthrough.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Xoá, tắt tạm, khoá node` (sau bảng, đặt sau FUS-11)
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe, `⌘P`. Chụp. `⌘P` lại.
- **Khung chụp:** chỉ một vùng — cận cảnh chuỗi bốn node.
- **Cần thấy rõ trong ảnh:** TieuDe mờ đi (Pass Through) so với các node khác.
- **Alt + chú thích:** `![Node TieuDe đang tắt tạm](../../assets/img/fusion-node-passthrough.png)` — *Node tắt tạm hiện mờ; hình đi xuyên qua như không có node.*

### FUS-13 — `fusion-merge-inspector.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `### Thông số Merge trong Inspector`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn Merge1, tab **Merge**.
- **Khung chụp:** chỉ một vùng — Inspector từ thanh tên Merge1 tới hết tab Merge (Edges).
- **Cần thấy rõ trong ảnh:** ba tab Merge/Channels/Settings; Center X/Y, Size, Angle, Flip, Apply Mode = Normal, Operator = Over, Blend, Subtractive/Additive, Edges.
- **Alt + chú thích:** `![Inspector của node Merge](../../assets/img/fusion-merge-inspector.png)` — *Merge tự có Center, Size, Angle cho lớp trên.*

### FUS-14 — `fusion-transform-inspector.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Transform`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp thử (clip 2), chọn MediaIn1, thêm **Transform**; Size 0.8, mở menu **Edges** chọn **Mirror**; đưa Transform lên Viewer 1.
- **Khung chụp:** chỉ một vùng — Viewer 1 (hình thu nhỏ có viền soi gương) + Inspector tab Controls; ghép cạnh nhau.
- **Cần thấy rõ trong ảnh:** Center, Pivot, Size, Angle, Flip, Edges = Mirror; hiệu ứng mép soi gương trên Viewer.
- **Alt + chú thích:** `![Node Transform với Edges Mirror](../../assets/img/fusion-transform-inspector.png)` — *Edges quyết định phần mép lộ ra khi dời hoặc thu nhỏ hình.*

### FUS-15 — `fusion-background-lower-third.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Background`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp thử (clip 2) làm đúng ví dụ lower third: Background đen alpha 0.7 + Rectangle (Corner Radius 0.3) nối vào mask, Merge lên MediaIn1, Text+ "Ten nhan vat" Merge lên trên. MediaOut1 ở Viewer 2. Chọn Background1, tab Color.
- **Khung chụp:** toàn cửa sổ (đây là kết quả nhiều node cần thấy cùng lúc) — hoặc ghép Node Editor + Viewer 2.
- **Cần thấy rõ trong ảnh:** chuỗi node Background → Rectangle (đường xanh dương), hai Merge; thanh nền bo góc với chữ trên video; Inspector Type = Solid Color.
- **Alt + chú thích:** `![Thanh lower third từ Background, Rectangle, Merge](../../assets/img/fusion-background-lower-third.png)` — *Nền đen bán trong suốt, bo góc bằng Rectangle, chữ ghép lên trên.*

### FUS-16 — `fusion-new-fusion-clip.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/node-co-ban.md` — ngay sau heading `## Fusion Clip và Fusion Composition`
- **Trang Resolve:** Edit
- **Chuẩn bị:** ở trang Edit, chọn clip 2 và clip 3 trên V1, chuột phải cho menu hiện.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt timeline + menu.
- **Cần thấy rõ trong ảnh:** mục **New Fusion Clip…**, **Create Referenced Fusion Composition** (nếu có trong menu này), **Reset Fusion Composition**.
- **Alt + chú thích:** `![Menu New Fusion Clip ở trang Edit](../../assets/img/fusion-new-fusion-clip.png)` — *Gom nhiều clip chồng nhau thành một comp.*
- **Ghi chú:** Esc, không tạo Fusion Clip.

### FUS-17 — `fusion-text-viewer-toolbar.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Gõ chữ ngay trên Viewer`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe, MediaOut1 ở Viewer 2; thanh công cụ chữ hiện dọc cạnh Viewer.
- **Khung chụp:** chỉ một vùng — Viewer 2 kèm thanh công cụ chữ, phóng vùng nút.
- **Cần thấy rõ trong ảnh:** Allow Typing in Viewer, Allow Manual Kerning, ba nút Text Outline; khung viền quanh chữ PHO MAI & RAU CU.
- **Alt + chú thích:** `![Thanh công cụ chữ trên Viewer](../../assets/img/fusion-text-viewer-toolbar.png)` — *Gõ, kerning tay, hiện khung viền chữ ngay trên hình.*

### FUS-18 — `fusion-text-tab-text.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Tab Text`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe, tab **Text**.
- **Khung chụp:** chỉ một vùng — Inspector từ ô Styled Text tới Write On.
- **Cần thấy rõ trong ảnh:** ô chữ "PHO MAI & RAU CU", Font Open Sans Bold, Color, Size ≈ 0.09, Tracking, Line Spacing, V/H Anchor, Write On (Start/End), hình thoi keyframe bên phải.
- **Alt + chú thích:** `![Tab Text của node Text+](../../assets/img/fusion-text-tab-text.png)` — *Nội dung, font, cỡ, màu và thanh Write On.*

### FUS-19 — `fusion-text-tab-layout.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Tab Layout`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe, tab **Layout**, mở menu **Type** cho xổ.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector tab Layout + menu Type.
- **Cần thấy rõ trong ảnh:** Type: Point/Frame/Circle/Path; Center X/Y, Size, Rotation, Angle X/Y/Z, Background Color; hình thoi keyframe cạnh Center.
- **Alt + chú thích:** `![Tab Layout của Text+](../../assets/img/fusion-text-tab-layout.png)` — *Vị trí và kiểu sắp xếp cả khối chữ; keyframe Center để chữ trượt.*

### FUS-20 — `fusion-text-tab-transform.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Tab Transform`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1 (bản sao), TieuDe, tab **Transform**, menu Transform = **Characters**, đặt rotation Y = 45 để thấy từng ký tự xoay. Viewer 2 xem MediaOut1.
- **Khung chụp:** chỉ một vùng — Inspector tab Transform + Viewer 2; ghép cạnh nhau.
- **Cần thấy rõ trong ảnh:** menu Characters/Words/Lines, Spacing, Pivot, X/Y/Z, Shear, Size; từng ký tự xoay riêng.
- **Alt + chú thích:** `![Tab Transform: xoay từng ký tự](../../assets/img/fusion-text-tab-transform.png)` — *Biến đổi từng ký tự, từ hoặc dòng quanh tâm riêng.*
- **Ghi chú:** trả Y về 0.

### FUS-21 — `fusion-text-tab-shading.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Tab Shading`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1 (bản sao), TieuDe, tab **Shading**: làm ví dụ "chữ trắng viền đen có bóng đổ" — lớp 1 Text Fill trắng; lớp 2 Text Outline đen, Thickness nhỏ, Outside Only; lớp 3 Text Fill đen Opacity 0.6, Softness 5, Offset 0.005/−0.005. Đang chọn lớp 2.
- **Khung chụp:** chỉ một vùng — Inspector tab Shading (hàng số 1–8 tới Offset) + Viewer 2 cận chữ; ghép cạnh nhau.
- **Cần thấy rõ trong ảnh:** hàng số lớp 1–8, Enabled, Appearance = Text Outline, Thickness, Outside Only; chữ có viền và bóng.
- **Alt + chú thích:** `![Tab Shading: viền và bóng đổ cho chữ](../../assets/img/fusion-text-tab-shading.png)` — *Tối đa tám lớp: tô chữ, viền, bóng, khối nền.*

### FUS-22 — `fusion-follower-timing.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Follower — chữ hiện lần lượt`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1 (bản sao), chuột phải ô Styled Text của TieuDe → **Follower**. Trang **Modifiers** → tab **Timing**, mở menu **Order**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector (trang Modifiers) + menu.
- **Cần thấy rõ trong ảnh:** trang Modifiers đang chọn; các tab Follower; Order (Left to right … Manual curve), Delay Type.
- **Alt + chú thích:** `![Follower, tab Timing](../../assets/img/fusion-follower-timing.png)` — *Chọn hướng chạy và độ trễ giữa các ký tự.*

### FUS-23 — `fusion-macro-editor.png`
- **Ưu tiên:** P3
- **Chèn vào:** `02-trang/fusion/chu-dong.md` — ngay sau heading `## Lưu thành Fusion Title dùng lại ở trang Edit`
- **Trang Resolve:** Fusion (cửa sổ Macro Editor)
- **Chuẩn bị:** comp clip 1, chọn TieuDe và Merge1 (không chọn MediaIn/MediaOut), chuột phải → **Macro → Create Macro**. Gõ Macro Name "TieuDeDemo", mở mục TieuDe, tick Export cho Styled Text.
- **Khung chụp:** hộp thoại — chụp toàn màn hình rồi cắt cửa sổ Macro Editor.
- **Cần thấy rõ trong ảnh:** ô Macro Name, danh sách node mở rộng, cột Export có tick ở Styled Text, menu ba chấm.
- **Alt + chú thích:** `![Macro Editor](../../assets/img/fusion-macro-editor.png)` — *Tick Export cho thông số muốn sửa từ trang Edit.*
- **Ghi chú:** đóng không lưu.

### FUS-24 — `fusion-keyframe-diamond.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/keyframe-va-spline.md` — ngay sau heading `## Keyframe trong Inspector`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1 — README đã keyframe Center của TieuDe (khung 0 và khung cuối chuyển động). Đứng đúng trên một keyframe; tab Layout. Chụp ảnh A. Dời con trỏ sang khung không có keyframe; chụp ảnh B.
- **Khung chụp:** chỉ một vùng — hàng Center X/Y trong Inspector kèm hình thoi và mũi tên hai bên; ghép A và B.
- **Cần thấy rõ trong ảnh:** A: hình thoi cam; B: hình thoi xám với mũi tên nhảy keyframe.
- **Alt + chú thích:** `![Nút keyframe hình thoi: cam và xám](../../assets/img/fusion-keyframe-diamond.png)` — *Cam là đang đứng trên keyframe; xám là chưa có keyframe ở khung này.*

### FUS-25 — `fusion-motion-path.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/keyframe-va-spline.md` — ngay sau heading `### Keyframe vị trí tạo ra đường đi`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, chọn TieuDe, Viewer 2 xem MediaOut1; con trỏ giữa hai keyframe.
- **Khung chụp:** chỉ một vùng — Viewer 2.
- **Cần thấy rõ trong ảnh:** đường chuyển động từ mép trái vào giữa, các điểm keyframe trên đường.
- **Alt + chú thích:** `![Đường chuyển động của chữ trên Viewer](../../assets/img/fusion-motion-path.png)` — *Kéo điểm trên đường để sửa quỹ đạo ngay trên hình.*

### FUS-26 — `fusion-keyframes-editor.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/keyframe-va-spline.md` — ngay sau heading `## Keyframes Editor`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, bấm **Keyframes** (tắt Spline). Bấm tam giác cạnh TieuDe để mở hàng Center.
- **Khung chụp:** chỉ một vùng — toàn panel Keyframes Editor.
- **Cần thấy rõ trong ảnh:** thanh MediaIn1, Merge1, TieuDe; hàng keyframe Center với hai điểm; nút Time Stretch và Spreadsheet góc dưới trái; ô Time góc dưới phải; dạng sóng âm (nếu bật).
- **Alt + chú thích:** `![Keyframes Editor trang Fusion](../../assets/img/fusion-keyframes-editor.png)` — *Mỗi node một thanh; dời keyframe hay độ dài clip theo thời gian.*

### FUS-27 — `fusion-spline-editor.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/keyframe-va-spline.md` — ngay sau heading `## Spline Editor`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp clip 1, bấm **Spline**; tick chỉ thông số Center X của TieuDe ở danh sách trái; `⌘F` vừa khít; chọn hai điểm.
- **Khung chụp:** chỉ một vùng — toàn panel Spline Editor (danh sách trái, đồ thị, thanh công cụ dưới).
- **Cần thấy rõ trong ảnh:** bốn vùng; đường cong Center X với hai keyframe đang chọn; thanh công cụ dưới.
- **Alt + chú thích:** `![Spline Editor trang Fusion](../../assets/img/fusion-spline-editor.png)` — *Trục ngang là thời gian, trục dọc là giá trị.*

### FUS-28 — `fusion-spline-smooth-linear.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/keyframe-va-spline.md` — ngay sau heading `## Làm chuyển động mượt`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** như FUS-27. Chọn hai điểm, `⇧L` (Linear) — chụp đồ thị; `⇧S` (Smooth) — chụp lần nữa. Ảnh thứ ba: cận thanh công cụ dưới với sáu nút đầu.
- **Khung chụp:** chỉ một vùng — đồ thị Spline (A: Linear, B: Smooth) ghép cạnh nhau, dưới là cận hàng nút.
- **Cần thấy rõ trong ảnh:** đường thẳng xiên so với đường cong thoải; nút Smooth, Linear, Invert, Step In, Step Out, Reverse.
- **Alt + chú thích:** `![Linear và Smooth trong Spline Editor](../../assets/img/fusion-spline-smooth-linear.png)` — *Linear chuyển động đều; Smooth chậm lại khi tới keyframe.*

### FUS-29 — `fusion-ellipse-blur-mask.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `## Rectangle và Ellipse`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp thử (clip 2): MediaIn1 → **Blur** (Blur Size ~20) → MediaOut1; chọn Blur, thêm **Ellipse** (tự nối đầu vào xanh dương). Kéo ellipse quanh mặt cô gái, tick **Invert**, Soft Edge 0.1. Chọn Ellipse1, Viewer 2 xem MediaOut1.
- **Khung chụp:** toàn cửa sổ hoặc ghép: Viewer 2 + Node Editor + Inspector tab Controls.
- **Cần thấy rõ trong ảnh:** đường xanh dương từ Ellipse vào Blur; khung ellipse quanh mặt; nền mờ, mặt rõ; Invert tick, Soft Edge.
- **Alt + chú thích:** `![Ellipse đảo ngược giới hạn Blur](../../assets/img/fusion-ellipse-blur-mask.png)` — *Mờ nền, giữ rõ mặt người bằng mask Ellipse Invert.*

### FUS-30 — `fusion-polygon-viewer.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `## Polygon`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp thử (clip 2), MediaIn1 ở Viewer 1. Bỏ chọn mọi node, thêm **Polygon** (đứng riêng). Bấm khoảng 8 điểm quanh người/con cừu, có vài điểm cong (bấm-kéo), khép hình bằng bấm điểm đầu. Chọn vài điểm.
- **Khung chụp:** chỉ một vùng — Viewer 1 kèm thanh công cụ Polyline dọc cạnh Viewer.
- **Cần thấy rõ trong ảnh:** hình polygon khép kín, điểm và tay nắm Bézier; thanh Polyline (Click Append, Insert and Modify, Draw Append, Modify Only, Done, Close).
- **Alt + chú thích:** `![Vẽ Polygon trên Viewer](../../assets/img/fusion-polygon-viewer.png)` — *Bấm từng điểm, bấm-kéo cho điểm cong, bấm lại điểm đầu để khép.*

### FUS-31 — `fusion-tracker-pattern.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `### Bước 1 — Nối và đặt ô track`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** comp thử (clip 2): MediaIn1 → **Tracker1** (đầu vào Background vàng). Đưa Tracker1 lên Viewer 1. Rê chuột lên ô track để hiện khung pattern (liền) và vùng tìm (nét đứt); kéo tay nắm góc trên trái đặt lên một chi tiết tương phản (đầu cừu, cột rào, mép mũ).
- **Khung chụp:** chỉ một vùng — Viewer 1 cận quanh ô track, gồm ô phóng to trợ giúp.
- **Cần thấy rõ trong ảnh:** khung pattern liền, khung vùng tìm nét đứt, tay nắm góc, ô phóng to.
- **Alt + chú thích:** `![Ô track: pattern và vùng tìm](../../assets/img/fusion-tracker-pattern.png)` — *Khung liền bám chi tiết; khung nét đứt là vùng tìm.*

### FUS-32 — `fusion-tracker-inspector.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `### Bước 2 — Track`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** tiếp FUS-31, bấm **Track Forward** cho chạy hết. Đổi tên tracker trong Tracker List thành "Cuu". Chụp Inspector tab Tracker và Viewer 1 có đường chuyển động.
- **Khung chụp:** ghép hai vùng: Inspector tab Tracker (nút track đầu tab, Tracker List) + Viewer 1 (đường track với vạch keyframe).
- **Cần thấy rõ trong ảnh:** bốn nút Track Reverse/Backward from Current/Forward from Current/Forward, nút Stop, Tracker List có "Cuu", nút Add; đường track trên hình.
- **Alt + chú thích:** `![Tracker sau khi track: Inspector và đường chuyển động](../../assets/img/fusion-tracker-inspector.png)` — *Mỗi vạch nhỏ trên đường là một keyframe vị trí.*

### FUS-33 — `fusion-tracker-connect-to.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `### Bước 3 — Gắn thứ khác bám theo`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** tiếp FUS-32. Thêm Text+ "Cuu" và Merge lên MediaIn1. Chọn Text+, tab Layout, chuột phải hàng Center → **Connect To** → **Tracker1** → mở tới **Cuu: Offset position**.
- **Khung chụp:** menu xổ — cần chụp toàn màn hình rồi cắt Inspector + chuỗi menu.
- **Cần thấy rõ trong ảnh:** Connect To → Tracker1 → Cuu: Offset position.
- **Alt + chú thích:** `![Nối Center của chữ vào dữ liệu track](../../assets/img/fusion-tracker-connect-to.png)` — *Cách B: chữ đi theo điểm đã track.*

### FUS-34 — `fusion-delta-keyer.png`
- **Ưu tiên:** P1
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `### Cách làm cơ bản`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** demo không có phông xanh — dùng clip 2 (trại cừu) chỉ để minh hoạ giao diện: MediaIn1 → **DeltaKeyer1** → MediaOut1. Tab **Key**, kéo ống nhỏ giọt cạnh **Background Color** thả lên mảng cỏ (hoặc trời) để có kết quả key tạm. DeltaKeyer1 ở Viewer 1.
- **Khung chụp:** chỉ một vùng — Inspector DeltaKeyer1 tab Key (hàng bảy tab, Background Color + ống nhỏ giọt, Gain, Balance).
- **Cần thấy rõ trong ảnh:** bảy tab Key, Pre-Matte, Matte, Fringe, Tuning, Mask, Settings; ô màu đã hút; ống nhỏ giọt.
- **Alt + chú thích:** `![Delta Keyer, tab Key](../../assets/img/fusion-delta-keyer.png)` — *Kéo ống nhỏ giọt thả lên phông để hút màu nền.*
- **Ghi chú:** Nếu muốn ảnh thật về phông xanh, cần nạp một clip green screen miễn phí — demo hiện không có.

### FUS-35 — `fusion-delta-keyer-matte.png`
- **Ưu tiên:** P2
- **Chèn vào:** `02-trang/fusion/mask-tracker-keyer.md` — ngay sau heading `### Tinh chỉnh`
- **Trang Resolve:** Fusion
- **Chuẩn bị:** tiếp FUS-34. Tab **Matte**. Viewer 1 bấm `A` xem alpha.
- **Khung chụp:** ghép: Inspector tab Matte (Threshold Low/High, Clean Background, Clean Foreground, Replace Mode) + Viewer 1 kênh alpha.
- **Cần thấy rõ trong ảnh:** các thông số tab Matte; hình đen trắng của alpha.
- **Alt + chú thích:** `![Delta Keyer tab Matte và kênh alpha](../../assets/img/fusion-delta-keyer-matte.png)` — *Xem alpha: trắng là đặc, đen là trong suốt; chỉnh Threshold và Clean.*
