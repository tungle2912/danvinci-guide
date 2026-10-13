# Metadata Editor

Panel bên phải trang Media. Có ở cả trang Edit.

Chọn một clip là metadata của nó hiện ra. **Chọn nhiều clip thì chỉ hiện clip cuối cùng** — nhưng gõ vào thì áp cho cả nhóm.

## Phần header — không sửa được

Khối trên cùng hiện thông tin kỹ thuật đọc từ file, chỉ để xem:

- Tên file và đường dẫn thư mục
- Độ dài
- Codec hình, frame rate, độ phân giải
- Codec tiếng, sample rate, số kênh

## Hai menu thả xuống ở đầu panel

Có **hàng trăm trường metadata**, nên Resolve chia nhóm bằng hai menu:

| Menu | Vị trí | Làm gì |
|---|---|---|
| **Metadata Presets** | Trái | Chọn bộ trường tự tạo của bạn. Mặc định là `Default` |
| **Metadata Groups** | Phải | Đổi giữa các nhóm trường có sẵn, chia theo đầu việc |

Các nhóm có sẵn gồm **Shot & Scene**, **Clip Details**, **Camera**, **Tech Details**, **Stereo 3D & VFX**, **Audio Trax**, và vài nhóm khác.

Tự tạo bộ trường riêng: **Preferences → User → Metadata**.

## Những trường đáng gõ

Không cần gõ hết. Năm trường này đủ dùng cho hầu hết dự án:

| Trường | Gõ gì | Dùng để |
|---|---|---|
| **Scene** | Số cảnh | Nhóm các take cùng cảnh |
| **Shot** | Số cú máy | |
| **Take** | Số lần quay | |
| **Good Take** | Tick nếu dùng được | Lọc nhanh bằng Smart Bin |
| **Keywords** | Từ khoá, cách nhau bằng dấu phẩy | Điều kiện cho Smart Bin |
| **Description** | Ghi chú tự do | "out nét ở giây 12", "có tiếng xe" |

## Gõ cho nhiều clip một lúc

1. Chọn nhiều clip trong Media Pool.
2. Gõ vào trường trong Metadata Editor.
3. Bấm **Apply** (góc dưới panel).

Cả nhóm nhận cùng giá trị.

## Sửa nhanh ngay trong Media Pool

Không cần mở Metadata Editor cho các trường hay dùng. Chuyển Media Pool sang **List view**, bốn cột này **gõ thẳng được**:

- **Name**
- **Description**
- **Keyword**
- **Comments**

Hiện cột: chuột phải vào tiêu đề cột → tick cột cần.

## Vì sao nên bỏ công gõ

Metadata là thứ làm [Smart Bin](bin.md#3-smart-bin) chạy được. Không có metadata thì Smart Bin chỉ lọc được theo thông số kỹ thuật.

Với dự án dưới 20 clip thì không cần. Với dự án phỏng vấn 200 clip thì nửa giờ gõ keyword tiết kiệm nhiều giờ tìm kiếm về sau.

## Mẹo: quy ước keyword

Đặt quy ước trước khi gõ, nếu không keyword sẽ loạn:

```
nhân vật:  an, binh, chi
loại:      phỏng-vấn, b-roll, cận, toàn
chất:      tốt, tạm, hỏng
```

Rồi tạo Smart Bin cho từng tổ hợp hay dùng.
