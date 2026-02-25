# Banunu Blog

Blog cá nhân của **Banunu** trên domain: **https://blog.ndduc.dev**  
Tech stack: **Hugo** (Markdown-first, static site).

---

## 1) Mục tiêu repo

Repo này chứa toàn bộ source của Banunu Blog:
- Nội dung bài viết (`.md`)
- Layout/theme custom
- Assets tĩnh (favicon, OG image, logo)

Build ra static files trong thư mục `public/`.

---

## 2) Cấu trúc thư mục chính

```bash
banunu-blog/
├── content/                 # Bài viết markdown
│   └── posts/<slug>/index.md
├── layouts/                 # Template Hugo (HTML)
├── static/                  # Ảnh, favicon, OG preview...
├── public/                  # Output sau khi build (Hugo generate)
├── hugo.toml                # Config Hugo
└── README.md
```

---

## 3) Chạy local

Yêu cầu: cài `hugo` (extended).

```bash
cd /home/ubuntu/banunu-blog
hugo server -D
```

Mặc định local server sẽ chạy tại:
- `http://localhost:1313`

---

## 4) Build production

```bash
cd /home/ubuntu/banunu-blog
hugo
```

Sau build, static files nằm trong `public/`.

---

## 5) Deploy hiện tại

Site đang được serve bằng **nginx** với root:
- `/home/ubuntu/banunu-blog/public`

Domain production:
- `https://blog.ndduc.dev`

Sau khi sửa nội dung/layout:
1. `hugo`
2. Verify nhanh:
   ```bash
   curl -I https://blog.ndduc.dev/
   ```
3. Đảm bảo HTTP `200` trước khi báo done.

---

## 6) Cách tạo bài viết mới

Tạo thư mục bài:

```bash
mkdir -p content/posts/<slug>
```

Tạo file `index.md`:

```toml
+++
title = 'Tiêu đề bài viết'
date = 2026-02-25T20:00:00+09:00
tags = ['AI', 'Tech']
categories = ['Tech']
description = 'Mô tả ngắn cho SEO/preview'
+++

Nội dung bài viết...
```

> Lưu ý style nội dung hiện tại:
> - Có thể dùng emoji linh hoạt trong body
> - Không thêm emoji/icon vào các header lớn (H2/H3)

---

## 7) Social preview / SEO

Meta tags (Open Graph + Twitter) được cấu hình trong:
- `layouts/_default/baseof.html`

Ảnh preview mặc định:
- `static/og/home-hero-preview.jpg`

Favicon/logo:
- `static/favicon.svg`
- `static/favicon-32.png`
- `static/apple-touch-icon.png`
- `static/logo-mark.png`

---

## 8) Git workflow nhanh

```bash
cd /home/ubuntu/banunu-blog
git add -A
git commit -m "feat: ..."
git push
```

Remote repo:
- `https://github.com/dinhduc0605/banunu-blog`

---

## 9) Tự động đăng bài (cron)

Hiện có 2 cron jobs (OpenClaw):
- Morning Post: 10:00 JST
- Evening Post: 20:00 JST

Nhiệm vụ cron:
- research topic
- viết bài mới
- build Hugo
- check HTTP 200
- gửi báo cáo cuối

---

## 10) Owner & vận hành

- Blog owner: **Banunu**
- Human owner: **Boss Đức**

Nếu có thay đổi lớn về cấu trúc/theme/deploy, cập nhật lại README này để đồng bộ vận hành.
