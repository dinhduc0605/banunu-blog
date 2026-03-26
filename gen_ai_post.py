import os
import requests
import subprocess
from pathlib import Path

# Config
post_dir = Path('/home/ubuntu/banunu-blog/content/posts/ai-layoffs-gpt5-4-qa-2026')
post_dir.mkdir(parents=True, exist_ok=True)

# 1. Download images (Simulating Gemini Banana Pro using Pollinations AI)
# Style: Minimal flat vector
hero_prompt = "minimal%20flat%20vector%20illustration%20of%20a%20developer%20looking%20at%20multiple%20floating%20screens%20with%20AI%20nodes%20clean%20lines%20corporate%20colors%20blue%20and%20orange"
section1_prompt = "minimal%20flat%20vector%20illustration%20of%20a%20human%20and%20robot%20hand%20collaborating%20on%20a%20glowing%20code%20block%20clean%20lines%20corporate%20colors%20blue%20and%20orange"
section2_prompt = "minimal%20flat%20vector%20illustration%20of%20a%20developer%20climbing%20stairs%20made%20of%20books%20and%20gears%20towards%20a%20bright%20future%20clean%20lines%20corporate%20colors%20blue%20and%20orange"

def download_image(prompt, filename):
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=1200&height=675&nologo=true"
    print(f"Downloading {filename}...")
    try:
        r = requests.get(url, timeout=30)
        with open(post_dir / filename, 'wb') as f:
            f.write(r.content)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

download_image(hero_prompt, 'hero.jpg')
download_image(section1_prompt, 'section-1.jpg')
download_image(section2_prompt, 'section-2.jpg')

# Generate OG image
try:
    subprocess.run(["convert", str(post_dir / "hero.jpg"), "-resize", "1200x630^", "-gravity", "center", "-extent", "1200x630", "-quality", "85", str(post_dir / "og-image.jpg")], check=True)
    print("OG image created.")
except Exception as e:
    print("Could not run imagemagick convert, just copying hero:", e)
    import shutil
    shutil.copy(post_dir / "hero.jpg", post_dir / "og-image.jpg")

# 2. Write Markdown Content
content = """+++
title = 'Q&A: Làn sóng sa thải vì AI 2026 và GPT-5.4'
date = 2026-03-22T23:30:00+00:00
tags = ['AI', 'Tech News', 'GPT-5.4', 'Career']
categories = ['Tech']
description = 'Năm 2026 chứng kiến hàng loạt cuộc sa thải do AI tự động hóa. Developer cần làm gì trước GPT-5.4 và Agentic AI? Dưới đây là 4 câu hỏi lớn giải đáp thực trạng.'
+++

Đầu năm 2026, bức tranh ngành công nghệ đang chứng kiến những thay đổi chưa từng có. Không còn là những dự đoán viển vông, "AI thay thế con người" đã chính thức trở thành lý do được các tập đoàn lớn (như Oracle, Block, hay Dow) đưa ra trong các đợt sa thải hàng loạt. Sự ra mắt của GPT-5.4 mini/nano và sự trỗi dậy của "Agentic AI" (AI tự chủ) đã nâng khả năng tự động hóa lên một tầm cao mới.

Vậy, đối mặt với thực tế khốc liệt này, các Developer cần chuẩn bị những gì? Cùng Banunu Blog giải đáp 4 câu hỏi lớn nhất đang gây bão trong cộng đồng.

![Hero Image - Minimal flat vector illustration of a developer looking at AI nodes](hero.jpg)

## Q1. Làn sóng sa thải đầu năm 2026 khác gì so với 2023-2024?

Nếu như các đợt sa thải năm 2023-2024 chủ yếu do "phình to" quy mô trong đại dịch và tái cấu trúc tài chính, thì năm 2026 đánh dấu một bước ngoặt: **Sa thải trực tiếp vì AI (AI-driven layoffs)**.

Theo các báo cáo tổng hợp từ [Business Insider](https://www.businessinsider.com/recent-company-layoffs-laying-off-workers-2026) và [TechCrunch](https://techcrunch.com/), hàng chục ngàn nhân sự từ Dell, Meta, Oracle, và Atlassian đã bị cắt giảm. Điều đáng sợ là các công ty này không hề giấu giếm: họ công khai thừa nhận vị trí đó đã bị AI thay thế hoặc họ cần dồn ngân sách để mua thêm GPU và phát triển Agentic AI. 

Các task như bảo trì hệ thống cơ bản, viết unit test, hay quản trị hạ tầng cấp thấp giờ đây được giao phó cho các mô hình nhỏ nhưng cực nhanh như **GPT-5.4 mini** của [OpenAI](https://openai.com/news/). Điều này biến nhóm kỹ sư "thực thi thuần túy" (chỉ code theo spec có sẵn) thành đối tượng dễ tổn thương nhất.

## Q2. Agentic AI và GPT-5.4 đang thay đổi quy trình làm việc ra sao?

Năm 2025, chúng ta dùng Copilot để gõ code nhanh hơn. Năm 2026, **Agentic AI** làm chủ cuộc chơi.

Theo [InfoQ](https://www.infoq.com/llms/news/), xu hướng hiện tại không còn là "AI hỗ trợ viết code" mà là "AI tự động lập kế hoạch và thực thi chéo hệ thống". Một Agent có thể tự động đọc ticket trên Jira, phân tích codebase, tạo nhánh (branch) mới, tự viết code, tự chạy test, và mở Pull Request (PR) mà không cần con người can thiệp ở các bước trung gian.

GPT-5.4 mini/nano giải quyết bài toán lớn nhất của năm ngoái: **Chi phí và độ trễ (Latency)**. Các mô hình nhỏ gọn này cho phép AI Agents gọi API hàng ngàn lần một phút với chi phí cực rẻ, khiến cho việc tự động hóa các quy trình phần mềm trở nên khả thi về mặt kinh tế đối với mọi công ty, từ startup nhỏ đến các tập đoàn khổng lồ.

![In-body Image - Minimal flat vector illustration of a human and robot hand collaborating](section-1.jpg)

## Q3. Vậy Developer có nguy cơ mất việc hoàn toàn không?

**Câu trả lời ngắn là: Không. Nhưng định nghĩa về "Developer" đã thay đổi.**

AI có thể code rất giỏi, nhưng nó (hiện tại) chưa biết cách giải quyết các vấn đề mơ hồ của doanh nghiệp (business problems). Lãnh đạo các công ty vẫn kỳ vọng duy trì số lượng nhân sự (headcount) nhưng nâng cao tiêu chuẩn (AI raises expectations).

Những vị trí đang bùng nổ nhu cầu:
1. **AI Orchestrator / Systems Architect:** Người biết thiết kế hệ thống nhiều AI Agents phối hợp với nhau.
2. **Domain Expert:** Những kỹ sư hiểu sâu về logic nghiệp vụ đặc thù (như tài chính, y tế, logistics) – thứ mà AI khó có thể tự học nếu không có data nội bộ.
3. **AI Validator / Security Engineer:** Người kiểm định chất lượng, tối ưu hóa prompt, và đảm bảo AI không "ảo giác" (hallucinate) hay tạo ra lỗ hổng bảo mật. Theo một báo cáo từ [Hacker News](https://news.ycombinator.com/), nhu cầu tuyển dụng kỹ sư chuyên tối ưu hóa luồng làm việc của AI đang tăng vọt.

## Q4. Lộ trình sinh tồn cho Developer trong năm 2026 là gì?

Nếu bạn đang lo lắng, hãy lập tức áp dụng 3 nguyên tắc sau:

1. **Ngừng cạnh tranh về tốc độ gõ phím:** Đừng cố viết code nhanh hơn AI. Hãy tập trung vào việc đọc, hiểu, và kiến trúc hệ thống (System Design). Kỹ năng quan trọng nhất năm 2026 là khả năng *Review Code của AI*.
2. **Học cách sử dụng "Agentic Workflow":** Bắt đầu xây dựng các công cụ CLI hoặc scripts cá nhân kết hợp nhiều API của các mô hình khác nhau. Đừng chỉ xài ChatGPT như một chatbot, hãy xài nó như một cỗ máy xử lý dữ liệu hàng loạt.
3. **Mở rộng sang các lĩnh vực hẹp (Niche):** AI học từ dữ liệu đại trà trên internet. Nếu bạn am hiểu sâu về một ngách nhỏ hoặc một công nghệ độc quyền mà trên internet có ít tài liệu, AI sẽ không thể thay thế bạn.

![In-body Image - Minimal flat vector illustration of a developer climbing stairs made of books](section-2.jpg)

## Summary (Tóm lược)

Làn sóng sa thải đầu năm 2026 là hồi chuông cảnh tỉnh khắc nghiệt: Công nghệ không chờ đợi bất kỳ ai. Sự ra mắt của GPT-5.4 mini/nano và mô hình Agentic AI đã xóa sổ khái niệm "Coder thợ gõ". 

Tuy nhiên, trong mọi cuộc khủng hoảng đều ẩn chứa cơ hội. Bằng cách chủ động chuyển mình từ "Người thực thi" sang "Kiến trúc sư hệ thống" và "Người quản trị AI", bạn không những có thể giữ vững vị trí của mình mà còn nắm bắt được những cơ hội nghề nghiệp giá trị cao nhất trong lịch sử ngành phần mềm. 

*Khởi động ngay từ hôm nay bằng cách tự động hóa chính những công việc nhàm chán nhất của bạn.*
"""

with open(post_dir / 'index.md', 'w') as f:
    f.write(content)

print(f"Content written. Word count: {len(content.split())}")

# Run hugo
print("Running hugo...")
os.chdir('/home/ubuntu/banunu-blog')
subprocess.run(['hugo'], check=True)
print("Hugo build complete.")
