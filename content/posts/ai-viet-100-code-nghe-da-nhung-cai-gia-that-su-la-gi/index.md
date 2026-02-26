+++
title = 'AI viết 100% code: Nghe đã, nhưng cái giá thật sự là gì?'
date = 2026-02-25T15:00:00+09:00
tags = ['AI', 'Coding', 'Developer', 'Productivity']
categories = ['Tech']
+++

Dạo gần đây chắc ai làm tech cũng thấy cụm câu này xuất hiện dày đặc: **"AI giờ viết gần hết code rồi"**.

<img src="hero-ai-code-responsibility.png?v=20260226a" alt="Ảnh minh hoạ hero: AI coding và trách nhiệm kỹ thuật của con người" style="display:block;width:100%;height:auto;margin:.6rem 0 1rem;" />

Nghe thì vừa phấn khích 🤩, vừa hơi rén 😅.
- Phấn khích vì năng suất tăng thật 🚀
- Rén vì nếu cái gì cũng "AI làm hộ", vậy kỹ năng cốt lõi của dev sẽ đi về đâu?

Mình đọc khá nhiều thảo luận trên Reddit và các bài viết có trích dẫn từ X, rồi thấy một điểm rất rõ:

> **AI đang thay thế tốc độ gõ code, nhưng chưa thay thế được người chịu trách nhiệm cho hệ thống.**


## 1) "AI viết 100% code" là có thật không? 🤔

Có, nhưng cần hiểu **đúng ngữ cảnh**.

Ví dụ trong một bài của Fortune, Boris Cherny (Anthropic) nói cá nhân anh ấy đã có giai đoạn để AI viết 100% code, và phần lớn code tại công ty cũng được AI tạo ra ở mức rất cao.

- Bài Fortune: [Top engineers at Anthropic, OpenAI say AI now writes 100% of their code](https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/)
- Bài đăng X của Boris (được Fortune trích): [x.com/bcherny/status/2015979257038831967](https://x.com/bcherny/status/2015979257038831967)
- Bài đăng X của roon/OpenAI (được Fortune trích): [x.com/tszzl/status/2015262304913469808](https://x.com/tszzl/status/2015262304913469808)

Nhưng ngay trong bài đó cũng có một chi tiết quan trọng: người phát ngôn Anthropic nói mức công ty nằm trong khoảng **70–90%**, không phải 100% tuyệt đối cho mọi team, mọi ngữ cảnh.

Nói ngắn gọn: câu "100%" có thể đúng cho cá nhân hoặc giai đoạn cụ thể, nhưng rất dễ bị hiểu sai thành "toàn ngành đã như vậy".

## 2) Cộng đồng dev đang tranh luận gì? 💬

Thread Reddit này có lượng thảo luận lớn và phản ứng rất trái chiều:

- Reddit r/artificial: [Top engineers at Anthropic & OpenAI: AI now writes 100% of our code](https://www.reddit.com/r/artificial/comments/1qrjbpc/top_engineers_at_anthropic_openai_ai_now_writes/)

Một bên nói: "Rất tốt, tăng năng suất mạnh".
Một bên phản biện: "AI vẫn yếu ở edge case lạ, framework ít phổ biến, và bài toán thực tế nhiều ràng buộc".

Điểm mình thấy đáng chú ý là: **tranh luận không còn xoay quanh việc có dùng AI hay không, mà xoay quanh việc dùng AI tới mức nào mà vẫn giữ chất lượng**.

## 3) Nút thắt mới: từ "viết code" sang "đánh giá code" 🧠

Trước đây bottleneck là code cho kịp deadline.
Giờ bottleneck chuyển thành:
- Đọc output AI đủ kỹ chưa?
- Có thấy lỗi logic ở biên hiếm không?
- Có phát hiện dead code, over-engineering, hoặc sai kiến trúc không?

Trong bài Fortune ở trên cũng có nhắc lại nhận xét của Andrej Karpathy: model vẫn có thể mắc "subtle conceptual errors", over-complicate và để lại dead code.

Nghĩa là AI giúp ta đi nhanh, nhưng **đi nhanh sai hướng thì vẫn là sai**.

## 4) Tác dụng phụ âm thầm: kỹ năng tư duy bị mòn

Một thread dài trên r/MachineLearning nói rất thẳng về chuyện cộng đồng đang tối ưu theo "đậu/được accept" hơn là tư duy nghiên cứu thực chất:

- Reddit r/MachineLearning: [[D] Some thoughts about an elephant in the room no one talks about](https://www.reddit.com/r/MachineLearning/comments/1qo6sai/d_some_thoughts_about_an_elephant_in_the_room_no/)

Dù bối cảnh là học thuật, mình thấy nó giống dev team ngoài đời ở một điểm:

> Khi tối ưu quá mạnh cho output ngắn hạn, kỹ năng reasoning dài hạn sẽ teo dần.

Nếu dev chỉ còn kỹ năng prompt mà thiếu kỹ năng đặt câu hỏi đúng, thì khi AI trả lời sai sẽ rất khó nhận ra sai ở đâu.

## 5) Nên dùng AI kiểu nào để vừa nhanh vừa bền? ⚖️

Mình thấy cách an toàn nhất là tách 2 mode rõ ràng:

### Mode A — AI-first (tăng tốc) ⚡
Dùng AI cho:
- scaffold nhanh
- viết test nháp
- migration/script cơ học
- refactor lặp lại

### Mode B — Human-first (chịu trách nhiệm) 🛡️
Con người giữ quyền quyết định ở:
- architecture
- security boundary
- data integrity
- rollback strategy
- trade-off cuối cùng

<img src="mode-a-vs-mode-b.png?v=20260226a" alt="Ảnh minh hoạ: Tách rõ mode tăng tốc và mode chịu trách nhiệm." style="display:block;width:100%;height:auto;margin:.5rem 0;" />

Nói dễ nhớ:

> **AI được quyền viết nhiều. Con người vẫn phải là người chịu trách nhiệm cuối.**

## 6) Checklist 5 câu trước khi merge code do AI sinh ✅

1. Nếu feature fail ở production, mình có giải thích rõ root cause được không?
2. Edge case quan trọng đã có test chưa?
3. Có chạm permission/data/race condition không?
4. Kịch bản rollback là gì?
5. Mình hiểu "vì sao chọn cách này", hay chỉ vì AI đề xuất vậy?

Nếu chưa trả lời mạch lạc 5 câu này, mình nghĩ chưa nên merge.

<img src="checklist-5-cau.png?v=20260226a" alt="Ảnh minh hoạ: Checklist nhanh trước khi merge." style="display:block;width:100%;height:auto;margin:.5rem 0;" />

## Kết 🎯

AI coding không còn là xu hướng nữa, mà là hiện tại.

Nhưng điều quyết định chất lượng sản phẩm vẫn không đổi: **tư duy kỹ thuật + trách nhiệm của con người**.

Code có thể do AI viết.
Hệ quả thì team mình là người nhận.

Nên dùng AI mạnh tay, nhưng đừng giao luôn tay lái.

---

## Nguồn tham khảo

1. Fortune — Top engineers at Anthropic, OpenAI say AI now writes 100% of their code  
   https://fortune.com/2026/01/29/100-percent-of-code-at-anthropic-and-openai-is-now-ai-written-boris-cherny-roon/

2. X post (Boris Cherny, theo trích dẫn trong Fortune)  
   https://x.com/bcherny/status/2015979257038831967

3. X post (roon/OpenAI, theo trích dẫn trong Fortune)  
   https://x.com/tszzl/status/2015262304913469808

4. Reddit thread tổng hợp thảo luận về claim "100% code"  
   https://www.reddit.com/r/artificial/comments/1qrjbpc/top_engineers_at_anthropic_openai_ai_now_writes/

5. Reddit r/MachineLearning — thảo luận về lệch trọng tâm giữa output và năng lực reasoning  
   https://www.reddit.com/r/MachineLearning/comments/1qo6sai/d_some_thoughts_about_an_elephant_in_the_room_no/

6. Reddit r/MachineLearning — ví dụ thảo luận prompt-injection trong quy trình review  
   https://www.reddit.com/r/MachineLearning/comments/1r3oekq/d_icml_every_paper_in_my_review_batch_contains/
