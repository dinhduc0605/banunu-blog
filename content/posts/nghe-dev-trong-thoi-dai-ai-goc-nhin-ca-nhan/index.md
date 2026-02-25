+++
title = 'Nghề dev trong thời đại AI: góc nhìn cá nhân sau nhiều lần “hype”'
date = 2026-02-25T21:05:00+09:00
tags = ['AI', 'Developer', 'Career']
categories = ['Tech']
description = 'AI đang thay đổi nghề dev, nhưng không theo cách nhiều người tưởng. Đây là góc nhìn thực dụng của mình.'
+++

Mình nghĩ nghề dev trong 3-5 năm tới sẽ không biến mất. Nhưng nó sẽ đổi form rất mạnh.

Đổi ở đâu? Không phải ở chuyện “có còn viết code hay không”. Mà là ở câu hỏi: **ai chịu trách nhiệm khi hệ thống chạy sai?**

## 1) AI đang tăng tốc thật, nhưng không phải mọi nơi đều tăng

Có khá nhiều dữ liệu cho thấy AI giúp dev làm nhanh hơn ở nhiều task (viết nháp, boilerplate, scaffold, test khung...).

Nhưng cũng có các nghiên cứu cho kết quả ngược lại trong task phức tạp: dev giàu kinh nghiệm có thể chậm đi vì phải kiểm tra/sửa output AI, hoặc bị nhiễu bởi lời giải “trông có vẻ đúng”.

Tức là, hiệu quả không còn phụ thuộc mỗi “công cụ xịn”, mà phụ thuộc vào:
- loại task
- mức độ rõ ràng của yêu cầu
- năng lực review của team

Vì vậy mình không tin vào câu “AI giúp nhanh hơn 100% trong mọi trường hợp”.

## 2) Vai trò dev đang dịch chuyển từ “người gõ” sang “người ra quyết định”

Trước đây bottleneck là viết code cho kịp.
Giờ bottleneck dần thành:
- định nghĩa bài toán đúng
- chọn trade-off đúng
- phát hiện lỗi logic ở edge case
- giữ hệ thống an toàn và dễ vận hành

Nói đơn giản: AI có thể làm được phần “generate”. Dev phải giữ phần “judge”.

Nếu chỉ giỏi prompt mà yếu tư duy hệ thống, bạn sẽ chạy rất nhanh… theo hướng sai.

## 3) Mặt trái lớn nhất: ảo giác năng suất

Mình thấy đây là rủi ro dễ dính nhất.

Team có thể tăng số PR, tăng tốc merge, nhưng đồng thời:
- code churn tăng
- bug hậu kỳ tăng
- thời gian debug production tăng

Nếu chỉ đo output ngắn hạn (số dòng code, số PR), ta rất dễ tưởng là tốt lên.

Mình thích một nguyên tắc đơn giản: đo cả tốc độ lẫn chất lượng.
Ít nhất nên theo dõi thêm bug rate, rollback rate, và thời gian xử lý sự cố.

## 4) Vậy dev nên học gì để không bị bỏ lại?

Theo mình, có 4 nhóm kỹ năng ngày càng quan trọng:

1. **System design**: hiểu kiến trúc, boundary, scaling, fault tolerance.
2. **Security mindset**: biết nghi ngờ output AI, chú ý data leak, permission, injection.
3. **Domain understanding**: hiểu nghiệp vụ sâu để biết “đúng sai thực tế”, không chỉ “đúng cú pháp”.
4. **AI collaboration**: biết chia task cho AI, viết prompt tốt, và review có phương pháp.

Dev tương lai không phải “ít code hơn thì yếu đi”.
Dev tương lai là “viết ít hơn nhưng quyết định khó hơn”.

## 5) Góc nhìn cá nhân của mình

Mình không bi quan về nghề dev. Mình cũng không lạc quan mù quáng.

Mình tin 3 điều:

- AI sẽ thay phần việc lặp lại, và đó là điều tốt.
- Dev giỏi sẽ càng có leverage lớn hơn trước.
- Dev không chịu nâng cấp tư duy hệ thống sẽ bị tụt nhanh, dù vẫn “biết dùng tool AI”.

Nghề này chưa chết. Nó chỉ đang buộc chúng ta trưởng thành nhanh hơn.

## Kết

Nếu phải tóm trong một câu:

**AI không lấy mất nghề dev. AI lấy mất phiên bản cũ của nghề dev.**

Phiên bản mới đòi hỏi ít “tay gõ” hơn, nhưng nhiều trách nhiệm hơn.
Và thật ra, đó cũng là hướng phát triển đáng mong chờ.

---

## Nguồn tham khảo

1. Stack Overflow Developer Survey 2024 (AI section)  
   https://survey.stackoverflow.co/2024/ai

2. ACM: Measuring GitHub Copilot’s impact on productivity  
   https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/

3. METR study (experienced OSS developers, mixed results)  
   https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

4. Jellyfish AI Metrics in Review (speed vs quality signals)  
   https://jellyfish.co/blog/2025-ai-metrics-in-review/

5. GetDX AI-assisted engineering impact report  
   https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/

6. Databricks State of AI (enterprise adoption trends)  
   https://www.databricks.com/blog/state-ai-enterprise-adoption-growth-trends
