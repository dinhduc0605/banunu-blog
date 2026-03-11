+++
title = 'Case study AGENTS.md 2026: viết ít hơn, kiểm soát tốt hơn'
date = 2026-03-08T22:50:00+00:00
tags = ['AGENTS.md', 'AI Coding Agent', 'Team nhỏ', 'Engineering Workflow', 'Cost Control']
categories = ['Tech']
description = 'Phân tích case study team nhỏ dùng AI coding agent: khi nào nên viết AGENTS.md, khi nào nên bỏ, và ma trận quyết định để giữ tốc độ mà không phình chi phí.'
og_image = 'og-hero.jpg?v=20260309a'
+++

Nếu năm 2025 là giai đoạn “nhét thật nhiều context cho agent”, thì 2026 bắt đầu có một câu hỏi khó hơn: **AGENTS.md có còn đáng viết dài không?**

Mình vừa xem lại một case vận hành của team nhỏ (7 người, 2 sản phẩm SaaS), và thấy một điểm thú vị: sau khi rút AGENTS.md từ 1.200 dòng xuống khoảng 180 dòng, tỉ lệ task pass test đầu tiên tăng, còn chi phí inference thì giảm rõ.

Điều này không có nghĩa AGENTS.md vô dụng. Ngược lại, nó cho thấy thứ chúng ta cần không phải “nhiều hướng dẫn hơn”, mà là **hướng dẫn đúng loại, đúng chỗ, đúng lúc**.

![Hero: team kỹ sư cân bằng tốc độ và kiểm soát chi phí khi dùng AGENTS.md](hero.jpg)

## Câu chuyện thực tế: khi tài liệu càng dày, agent càng vòng vo

Bối cảnh ban đầu khá quen thuộc: team muốn chuẩn hoá cách agent chạy task nên gom mọi thứ vào AGENTS.md — coding style, release checklist, cách đặt branch, template PR, policy log, thậm chí cả triết lý thiết kế.

Tuần đầu nhìn rất ổn: mọi người yên tâm vì “đã có rulebook”. Nhưng từ tuần thứ hai, các triệu chứng bắt đầu lộ ra:

- Agent mất nhiều vòng để tìm “đoạn rule liên quan” trước khi sửa code.
- Các task nhỏ (rename, sửa test, patch API nhẹ) lại tốn nhiều step không cần thiết.
- Reviewer nhận PR dài hơn mong đợi vì agent cố “tuân thủ toàn bộ hướng dẫn”, kể cả phần không liên quan.

Khi đọc lại nghiên cứu được InfoQ tóm tắt từ ETH Zurich, bức tranh này hợp lý hơn nhiều: AGENTS.md do LLM-generated có thể làm giảm success rate trung bình và làm tăng số bước chạy, kéo theo chi phí inference tăng mạnh. Ngay cả AGENTS.md do con người viết cũng chỉ có lợi nhẹ nếu nội dung thực sự “không thể suy ra từ codebase” ([InfoQ](https://www.infoq.com/news/2026/03/agents-context-file-value-review/), [arXiv](https://arxiv.org/pdf/2602.11988)).

Bài học ở đây: **context không phải cứ nhiều là tốt**. Context tốt phải có tính quyết định.

![Minh họa workflow thừa do AGENTS.md quá rộng khiến agent chạy vòng lặp](section-1.jpg)

## Vì sao team nhỏ dễ “quá tay” với AGENTS.md?

### 1) Sợ agent làm sai nên nhồi mọi thứ vào một file

Tâm lý này rất người: càng lo, càng viết nhiều rule. Nhưng khi rule vượt ngưỡng, agent phải tiêu tốn token để đọc và đối chiếu những thứ không liên quan trực tiếp đến task hiện tại.

### 2) Nhầm giữa “playbook cho người” và “instruction cho agent”

Nhiều nội dung hợp với onboarding con người nhưng không hữu ích cho vòng lặp tool-use của agent. Ví dụ triết lý sản phẩm dài 2 trang có thể rất hay cho team, nhưng không giúp agent fix một lỗi parser nhanh hơn.

### 3) Không gắn rule với trigger vận hành cụ thể

Cursor Automations cho thấy hướng đúng hơn: chạy theo trigger và task scope rõ ràng (PR opened, CI completed, scheduled run...), tức là rule nên đi kèm hoàn cảnh thực thi thay vì dồn chung một chỗ ([Cursor Docs](https://cursor.com/docs/cloud-agent/automations)).

Cộng đồng kỹ sư trên Hacker News cũng đang tranh luận mạnh về sandbox, isolation và mức autonomy phù hợp cho agent; điểm chung là ai cũng quay về bài toán “giới hạn đúng phạm vi” thay vì thả agent chạy full quyền ([Hacker News](https://news.ycombinator.com/item?id=47185250)).

Ngoài ra, theo dõi nhịp tin trên TechCrunch về làn sóng AI products cho thấy tốc độ ra tính năng đang rất nhanh; nếu không có khung kiểm soát gọn, team nhỏ rất dễ bị cuốn theo tool mới mà quên bài toán reliability nội bộ ([TechCrunch AI](https://techcrunch.com/tag/artificial-intelligence/)).

## Ma trận quyết định: khi nào nên viết AGENTS.md, khi nào nên bỏ

Thay vì hỏi “có nên có AGENTS.md không?”, team trong case study chuyển sang hỏi: **task này có thật sự cần instruction file riêng không?**

Họ dùng ma trận 2x2 theo hai trục:

- **Mức độ đặc thù của repo** (thấp/cao)
- **Rủi ro tuân thủ hoặc vận hành** (thấp/cao)

Kết quả áp dụng rất thực dụng:

### Ô 1 — Đặc thù thấp + rủi ro thấp

Không dùng AGENTS.md riêng. Chỉ cần prompt ngắn + tiêu chí done + test command.

### Ô 2 — Đặc thù cao + rủi ro thấp

Dùng AGENTS.md mini (100-200 dòng), tập trung vào:

- command build/test đặc thù
- map thư mục khó đoán
- quy ước đặt tên nội bộ

### Ô 3 — Đặc thù thấp + rủi ro cao

Không kéo dài AGENTS.md. Thay bằng policy checks ở CI/CD (security scan, dependency gate, approval rule).

### Ô 4 — Đặc thù cao + rủi ro cao

Mới cần AGENTS.md đầy đủ hơn, nhưng vẫn bắt buộc chia module và gắn version, tránh một file monolith.

![Minh họa team dùng decision matrix để quyết định phạm vi AGENTS.md](section-2.jpg)

## Action steps có thể làm ngay trong tuần này

Nếu Boss đang chạy team nhỏ, mình đề xuất checklist 5 bước này để giảm “cognitive tax” từ agent:

1. **Audit AGENTS.md hiện tại**  
   Gắn nhãn từng đoạn: “non-inferable” (không thể suy từ code) hoặc “inferable”. Xoá/di chuyển phần inferable.

2. **Tách rule theo workflow thay vì theo chủ đề**  
   Ví dụ: `agents-pr-review.md`, `agents-release-hotfix.md`, `agents-migration.md`.

3. **Đặt trần độ dài cho mỗi file hướng dẫn**  
   Team case study đặt hard limit 220 dòng/file. Vượt ngưỡng thì phải tách.

4. **Đo 3 chỉ số trong 2 sprint**  
   - pass rate ở lần test đầu  
   - step trung bình mỗi task  
   - token/cost mỗi PR

5. **Quy ước “ngắn trước, dài sau”**  
   Task mới bắt đầu bằng instruction ngắn. Chỉ mở rộng khi có bằng chứng thất bại lặp lại.

Điểm mấu chốt: đừng biến AGENTS.md thành nơi chứa mọi lo lắng của team 😅. Nó phải là “đòn bẩy thực thi”, không phải “bách khoa toàn thư”.

## Kết luận

AGENTS.md vẫn hữu ích trong 2026, nhưng hiệu quả nhất khi nó được viết như **hợp đồng vận hành tối thiểu**: ngắn, sắc, không nhập nhằng, gắn thẳng vào tác vụ và rủi ro cụ thể.

Team nhỏ thắng đường dài không phải vì ép agent đọc nhiều hơn, mà vì biết **lọc đúng thứ cần đọc**. Nếu cần một nguyên tắc để bắt đầu: *thứ gì codebase tự nói được thì đừng bắt AGENTS.md nói lại*.

---

## Nguồn tham khảo

1. InfoQ — New Research Reassesses the Value of AGENTS.md Files for AI Coding  
   https://www.infoq.com/news/2026/03/agents-context-file-value-review/

2. arXiv — Repository-Level AI Agent Instructions: Overengineering or Necessary Guidance?  
   https://arxiv.org/pdf/2602.11988

3. Cursor Docs — Automations  
   https://cursor.com/docs/cloud-agent/automations

4. Hacker News — Discussion: Let's discuss sandbox isolation  
   https://news.ycombinator.com/item?id=47185250

5. TechCrunch — Artificial Intelligence tag (industry trend stream)  
   https://techcrunch.com/tag/artificial-intelligence/
