# Scope — đọc Parade, Waveform

Mắt người **tự thích nghi** với màu ám — nhìn lâu là quen. Màn hình cũng mỗi cái một khác. Scope là thước đo **không nói dối**.

**Mở:** icon **Scopes** ở **ngoài cùng bên phải** hàng palette. Đổi loại bằng menu thả xuống góc trên phải khung scope (đang ghi **Parade** trong ảnh chụp ở trang trước).

## Parade

`★★★ Hằng ngày` — dùng để cân bằng trắng

Ba cột **đỏ, xanh lá, xanh dương** đặt cạnh nhau. Trục dọc là độ sáng, từ 0 (đáy) tới 1023 (đỉnh).

| Thấy gì | Nghĩa | Sửa |
|---|---|---|
| Ba cột **chân ngang nhau, đỉnh ngang nhau** | Cân bằng trắng **đúng** | — |
| Cột xanh dương cao hơn hai cột kia | Ảnh **ám xanh** | Temp lên |
| Cột đỏ cao hơn | Ảnh **ám cam/đỏ** | Temp xuống |
| Cột xanh lá cao hơn | Ảnh **ám xanh lá** | Tint lên |

> Chỉ so ở những vùng **đáng lẽ trung tính** (trắng, xám, đen). Cảnh hoàng hôn thì cột đỏ cao hơn là đúng.

## Waveform

`★★★ Hằng ngày` — dùng để đặt độ sáng

Một khối duy nhất cho độ sáng. Trái sang phải tương ứng trái sang phải trong khung hình.

| Thấy gì | Nghĩa |
|---|---|
| Đáy chạm khoảng **0** | Có điểm đen thật — tốt |
| Đáy lơ lửng ở 100–200 | Ảnh bị **xám, bạc** — kéo Lift xuống |
| Đỉnh khoảng **900–1000** | Đủ sáng, chưa cháy — tốt |
| Đỉnh **dẹt phẳng ở 1023** | **Cháy** — mất chi tiết, kéo Gain hoặc Highlights xuống |
| Dồn cục ở giữa | Ảnh **thiếu tương phản** — điển hình của footage LOG |

## Vectorscope

`★★☆ Thường dùng` — dùng cho màu da

Một vòng tròn. **Càng xa tâm càng đậm màu**, hướng chỉ loại màu.

**Đường skin tone line:** vạch chéo hướng khoảng **11 giờ**. Da người, **bất kể màu da gì**, nằm trên hoặc rất gần vạch này.

**Cách kiểm tra da:** dùng Window khoanh riêng khuôn mặt — Vectorscope chỉ hiện màu của vùng đó. Lệch khỏi vạch thì chỉnh ở node Secondary.

## Histogram

`★☆☆` — giống biểu đồ của máy ảnh. Quen với chụp ảnh thì dễ đọc, nhưng Parade và Waveform chính xác hơn để chỉnh video.

## Thứ tự nhìn scope khi chỉnh một clip

1. **Waveform** → đặt điểm đen, điểm trắng (node 01)
2. **Parade** → cân bằng trắng (node 01)
3. **Vectorscope** → kiểm tra da người (node 04)
