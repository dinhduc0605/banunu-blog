import os
import requests
import subprocess
from pathlib import Path

# Config
post_dir = Path('/home/ubuntu/banunu-blog/content/posts/ai-fatigue-digital-detox-cuoi-tuan')
post_dir.mkdir(parents=True, exist_ok=True)

# 1. Download images (Simulating Gemini Banana Pro using Pollinations AI)
# Pollinations creates images dynamically based on prompt
hero_prompt = "3d%20clay%20render%20of%20a%20developer%20closing%20laptop%20with%20coffee%20and%20books%20pastel%20colors%20soft%20lighting%20calm%20mood"
section1_prompt = "3d%20clay%20render%20of%20smartphone%20in%20drawer%20and%20hands%20reading%20a%20physical%20book%20pastel%20colors%20soft%20lighting%20calm%20mood"

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

# Generate OG image (Resize hero to 1200x630, quality 80 to keep <600KB)
try:
    subprocess.run(["convert", str(post_dir / "hero.jpg"), "-resize", "1200x630^", "-gravity", "center", "-extent", "1200x630", "-quality", "85", str(post_dir / "og-image.jpg")], check=True)
    print("OG image created.")
except Exception as e:
    print("Could not run imagemagick convert, just copying hero:", e)
    import shutil
    shutil.copy(post_dir / "hero.jpg", post_dir / "og-image.jpg")

# 2. Write Markdown Content
content = """+++
title = 'AI Fatigue 2026: Chiến lược "Digital Detox" cuối tuần cho Developer'
date = 2026-03-22T08:00:00+07:00
tags = ['AI Fatigue', 'Digital Detox', 'Mental Health', 'Workflow']
categories = ['Daily Life']
description = 'Code AI tạo ra ngày càng nhiều khiến lập trình viên kiệt sức vì liên tục review. Khám phá chiến lược digital detox cuối tuần để phục hồi não bộ.'
+++

Năm 2026, AI đã thay đổi hoàn toàn cách chúng ta làm việc. Với dự đoán lên tới 90% code trong các dự án lớn có sự can thiệp của AI, vai trò của lập trình viên đã dịch chuyển từ "người gõ code" sang "người duyệt code". Thế nhưng, sự thay đổi này mang theo một tác dụng phụ không mong muốn: **AI Fatigue** (Hội chứng mệt mỏi vì AI) và sự quá tải kỹ thuật số.

Đã bao giờ bạn gập máy tính vào chiều thứ Sáu mà trong đầu vẫn lởn vởn những đoạn logic lỗi của Claude Code hay GitHub Copilot? Đã bao giờ bạn cảm thấy kiệt quệ sau một ngày dài chỉ ngồi đọc và sửa lỗi do các Agent tự động sinh ra? Nếu câu trả lời là có, bài viết này dành cho bạn.

![Hero Image - Không gian thư giãn không màn hình với màu sắc pastel nhẹ nhàng](hero.jpg)

## 1. Problem: "AI Party Hangover" và sự kiệt sức thầm lặng

Chúng ta từng hào hứng khi AI giúp hoàn thành task trong 10 phút thay vì 4 tiếng. Nhưng tuần trăng mật đã kết thúc. Theo một bài báo trên [Developer Tech](https://www.developer-tech.com/news/software-development-in-2026-curing-ai-party-hangover/), ngành phần mềm đang trải qua giai đoạn "AI Party Hangover" (Dư âm sau bữa tiệc AI). 

Sự mệt mỏi này đến từ việc chúng ta bị ép trở thành những "Professional Slap Reviewers" (Người duyệt code chuyên nghiệp). Thay vì được tự do sáng tạo và tận hưởng trạng thái "flow" khi tự tay viết nên một chức năng từ đầu, dev hiện đại phải liên tục đọc, phân tích, và sửa những đoạn code do AI sinh ra. 

Việc liên tục phải cảnh giác với hallucination (ảo giác AI), kiểm soát chi phí API, và lo lắng về bảo mật khiến não bộ chúng ta duy trì ở trạng thái căng thẳng cao độ. Thêm vào đó, áp lực phải liên tục cập nhật prompt engineering và làm quen với các model mới (như GPT-5 hay DeepSeek v4) khiến chúng ta không có một phút giây nào thực sự ngắt kết nối. 

Không chỉ vậy, thị trường việc làm phân hóa mạnh mẽ cũng gây ra áp lực tâm lý. Tầng lớp lập trình viên thực thi (chỉ nhận task và code) đang thu hẹp. Các công ty yêu cầu bạn phải là một "nhạc trưởng" (orchestrator) có tư duy hệ thống cao. Sự chuyển đổi vai trò ép buộc này làm gia tăng hội chứng kẻ mạo danh và sự kiệt quệ.

## 2. Analysis: Tại sao review code lại vắt kiệt sức lực hơn tự code?

Nhiều người lầm tưởng rằng có AI làm hộ thì dev sẽ nhàn hơn. Thực tế lâm sàng chứng minh điều ngược lại, ít nhất là về mặt nhận thức (cognitive load).

Khi bạn tự viết code, bạn xây dựng mental model (mô hình tư duy) từ con số không. Bạn hiểu rõ từng biến, từng hàm được tạo ra để làm gì. Quá trình này tuy tốn thời gian nhưng lại rất tự nhiên với não bộ của một kỹ sư.

Ngược lại, khi đọc code của AI, bạn phải thực hiện quá trình dịch ngược (reverse engineering). Bạn phải phỏng đoán ý đồ của "người viết" (vốn dĩ là một mô hình xác suất), kiểm tra các góc khuất (edge cases) mà AI có thể đã bỏ qua. Việc này đòi hỏi sự tập trung cao độ và liên tục chuyển đổi bối cảnh (context switching). Giống như việc bạn phải chấm bài thi của một học sinh xuất sắc nhưng lại rất hay ẩu – bạn không thể lơ là dù chỉ một giây.

Sự bùng nổ của AI cũng làm mất đi cảm giác "hoàn thành" (sense of completion). Trước đây, viết xong một tính năng mất 3 ngày, bạn có cảm giác thành tựu lớn. Nay AI làm xong trong 10 phút, bạn chuyển ngay sang tính năng tiếp theo. Tốc độ bào mòn chất lượng cảm xúc của chúng ta.

![In-body Image - Đặt điện thoại vào ngăn kéo để đọc sách giấy](section-1.jpg)

## 3. Checklist: Chiến lược "Digital Detox" 48h cuối tuần

Để tồn tại bền bỉ trong kỷ nguyên AI 2026, việc ngắt kết nối (Digital Detox) không còn là một trào lưu xa xỉ, mà là kỹ năng sinh tồn bắt buộc. Theo nghiên cứu từ [Vail Health](https://www.vailhealth.org/news/unplug-to-recharge-why-a-digital-detox-is-the-real-power-move-for-2026) về xu hướng của năm 2026, mục tiêu không phải là từ bỏ công nghệ, mà là giành lại quyền kiểm soát sự chú ý và tái thiết lập ranh giới.

Dưới đây là playbook 48h Digital Detox cuối tuần dành riêng cho Developer để phục hồi não bộ:

**Tối Thứ Sáu: Thiết lập ranh giới cứng**
- **Nghi thức tắt máy (Power-down routine):** Đóng toàn bộ tab IDE, Terminal và trình duyệt lúc 18:00. Đừng để lại bất kỳ "tab dang dở" nào với lý do "để thứ Hai xem tiếp". Việc để tab mở sẽ khiến tiềm thức bạn tiếp tục xử lý nó.
- **Log out khỏi các nền tảng AI:** Đăng xuất khỏi ChatGPT, Claude, hay Cursor trên điện thoại di động. Bạn không cần phải test một prompt ý tưởng mới lúc 10 giờ tối. Ghi ra sổ tay nếu chợt lóe lên ý tưởng.
- **Thiết lập "Vùng không màn hình":** Loại bỏ hoàn toàn điện thoại và thiết bị điện tử khỏi phòng ngủ. Thay thế bằng một cuốn sách giấy hoặc máy đọc sách (loại không có kết nối internet hay thông báo).

**Thứ Bảy: Phục hồi thụ động và CBT**
- **Trì hoãn màn hình buổi sáng:** Đừng cầm điện thoại ngay khi mở mắt. Theo các chuyên gia tâm lý học hành vi (CBT), thói quen này gây "notification anxiety" (lo âu vì thông báo). Hãy dành 2 giờ đầu ngày cho việc pha cà phê, dọn dẹp, hoặc đi bộ.
- **Hoạt động Analog (Vật lý):** Đánh thức các giác quan vật lý của bạn. Tham gia vào các sở thích yêu cầu sự tỉ mỉ của đôi tay nhưng không liên quan đến màn hình: nấu ăn, mộc, lắp ráp mô hình, đạp xe, hoặc chăm sóc cây cảnh. Việc chạm vào các vật thể vật lý giúp não bộ "grounding" (tiếp đất) rất tốt.
- **Quy tắc "Batching" thông tin:** Nếu bắt buộc phải kiểm tra tin nhắn hay mạng xã hội, hãy gom chúng lại vào 2 khung giờ cố định (ví dụ: 12h trưa và 6h tối), mỗi lần xử lý không quá 15 phút rồi cất đi.

**Chủ Nhật: Khởi động lại tư duy**
- **Giao tiếp không kịch bản:** Dành thời gian chất lượng cho gia đình, bạn bè, hoặc thú cưng ở ngoài trời. Những tương tác không có kịch bản sẵn sẽ giúp não bộ thư giãn khỏi những luồng logic if/else khô khan của công việc.
- **Tư duy chiến lược thay vì thực thi:** Buổi chiều Chủ nhật, hãy nhâm nhi một ly trà và nghĩ về bức tranh lớn thay vì lo lắng về task ngày mai. AI đang định hình lại ngành, vậy bạn muốn định vị mình ở đâu trong 2-3 năm tới? Việc suy nghĩ chiến lược (Strategic Thinking) sẽ mang lại cảm giác làm chủ cuộc đời, giảm thiểu sự hoang mang do dòng chảy công nghệ ép buộc.

## 4. Conclusion: Lùi một bước để đi đường dài

Sự xuất hiện của AI không làm cho nghề lập trình biến mất, nhưng nó đang tái định nghĩa hoàn toàn về sự năng suất. Trong một thời đại mà các hệ thống máy móc có thể tạo ra hàng vạn dòng code mỗi phút, giá trị cốt lõi của bạn không còn nằm ở tốc độ gõ phím. Giá trị của bạn nằm ở **sự rõ ràng trong tư duy, khả năng phán đoán hệ thống, và một tinh thần minh mẫn dẻo dai**.

Một cuối tuần ngắt kết nối hoàn toàn khỏi màn hình và các công cụ AI không phải là sự lãng phí thời gian hay tụt hậu. Ngược lại, đó là một khoản đầu tư bắt buộc để bảo dưỡng "cỗ máy" quan trọng nhất của bạn: Não bộ con người. 

Cuối tuần này, hãy thử mạnh dạn tắt nguồn điện thoại, cất chiếc laptop quen thuộc vào ngăn kéo sâu nhất, và tận hưởng một ngày trọn vẹn ở thế giới thực. Bạn sẽ thực sự bất ngờ với nguồn năng lượng và sự sáng suốt mà mình nhận lại được vào sáng thứ Hai.
"""

with open(post_dir / 'index.md', 'w') as f:
    f.write(content)

print(f"Content written. Word count: {len(content.split())}")

# Optional: List files to verify
print("Files in dir:")
print(os.listdir(post_dir))
