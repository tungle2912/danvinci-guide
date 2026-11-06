# Nguồn tham khảo

## Manual gốc trong máy

Bản PDF đầy đủ nhất đi kèm phần mềm:

```
/Applications/DaVinci Resolve/DaVinci Resolve Manual.pdf
```

Hơn 4000 trang. Mọi phím tắt trong tài liệu này đều đối chiếu với file đó.

Khi tài liệu ghi `tr.` hoặc `p` kèm một số, đó là số trang của *DaVinci Resolve 21 Reference Manual* (bản tháng 7/2026). Gõ số đó vào ô trang của Preview là tới đúng chỗ. Vài chương nên mở đầu tiên:

| Chương | Trang | Dùng khi |
|---|---|---|
| 1 — Introduction to DaVinci Resolve | 13 | Tám trang, cách đổi trang (tr.20–21) |
| 2 — Using the DaVinci Resolve User Interface | 55 | Panel, Viewer, thao tác chung |
| 3 — Managing Projects and Project Libraries | 75 | Tạo, xuất, khôi phục project, backup |
| 4 — System and User Preferences | 97 | GPU, bộ nhớ, **Project Save and Load**, **Keyboard Customization** (tr.125–128) |
| 6 — Project Settings | 139 | Độ phân giải, frame rate, quản lý màu, cache |
| 8 — Improving Performance, Proxies, and the Render Cache | 196 | Phát lại giật, proxy, optimized media |
| 10 — HDR Setup and Grading | 259 | HDR (phần lớn là `Studio`, tr.261) |

> **Mẹo:** Muốn biết một tính năng có ở bản free không, tìm tên nó trong PDF (⌘F trong Preview). Tính năng chỉ có ở Studio thường có tiêu đề kèm *(Studio Version Only)* hoặc câu *"…only available in DaVinci Resolve Studio"*.

Mở nhanh bằng Terminal:

```bash
open "/Applications/DaVinci Resolve/DaVinci Resolve Manual.pdf"
```

## Sáu cuốn hướng dẫn miễn phí của Blackmagic

Blackmagic phát hành miễn phí bộ sách dạy chính thức cho Resolve 20, kèm file bài tập và bài thi trực tuyến. Tải tại [trang Training của Blackmagic Design](https://www.blackmagicdesign.com/products/davinciresolve/training):

| Sách | Nội dung |
|---|---|
| [The Beginner's Guide to DaVinci Resolve 20](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Beginners-Guide.pdf) | Nhập môn toàn diện, bắt đầu từ đây |
| [The Editor's Guide](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Editors-Guide.pdf) | Dựng nâng cao, trim, metadata, multicam |
| [The Colorist Guide](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Colorist-Guide.pdf) | Chỉnh màu chuyên sâu |
| [The Fairlight Audio Guide](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Fairlight-Audio-Post.pdf) | Hậu kỳ âm thanh |
| [The Visual Effects Guide](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Fusion-Visual-Effects.pdf) | Fusion cơ bản |
| [Advanced Visual Effects](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-20-Advanced-Visual-Effects.pdf) | Compositing, phông xanh, hạt 3D |

Sách viết cho Resolve 20, dùng được gần như nguyên vẹn cho 21.

## Diễn đàn và cộng đồng

- [Diễn đàn chính thức Blackmagic](https://forum.blackmagicdesign.com) — nơi kỹ sư của hãng trả lời trực tiếp
- [r/davinciresolve](https://www.reddit.com/r/davinciresolve/) — hỏi đáp nhanh

## Các nguồn đã dùng khi viết tài liệu này

Phần so sánh Free và Studio: các mục AI, hiệu ứng, màu đối chiếu với manual gốc (có số trang). Riêng giới hạn xuất file lấy từ [Toolfarm](https://www.toolfarm.com/tutorial/in-depth-davinci-resolve-studio-vs-the-free-version/), [CineD](https://www.cined.com/davinci-resolve-an-in-depth-comparison-between-the-free-and-studio-version/), [Storyblocks](https://www.storyblocks.com/resources/tutorials/davinci-resolve-free-vs-studio).

Phần quản lý màu và thứ tự node: [Frame.io Insider](https://blog.frame.io/2024/01/08/color-management-nodes-davinci-resolve/), [diễn đàn Blackmagic](https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=154766), [Filmmaking Elements](https://filmmakingelements.com/color-management-in-davinci-resolve/).

Phần video dọc: [4K Shooters](https://4kshooters.net/2022/10/16/how-to-edit-export-high-quality-instagram-reels-in-davinci-resolve-18), [dvresolve.com](https://dvresolve.com/tutorial/reformatting-vertical-video-social-media/).

Phần hiệu năng: [Miracamp](https://www.miracamp.com/learn/davinci-resolve/how-to-fix-laggy-playback-in-davinci-resolve-optimize-timeline-performance), [Elements.tv](https://elements.tv/blog/davinci-resolve-5-ways-to-achieve-better-playback-performance/).

Phím tắt: đối chiếu toàn bộ với manual gốc, không lấy từ blog.
