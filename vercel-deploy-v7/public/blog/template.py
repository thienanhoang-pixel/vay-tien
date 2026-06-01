# Template HTML cho bài viết blog SEO
TEMPLATE = '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | hotrotaichinh.top</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://hotrotaichinh.top/og-image.jpg">
  <meta property="og:url" content="https://hotrotaichinh.top/blog/{slug}">
  <meta property="og:type" content="article">
  <link rel="canonical" href="https://hotrotaichinh.top/blog/{slug}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{{--primary:#0a2540;--accent:#00c896;--light:#f7f9fc;--text:#1a2e44;--muted:#6b7c93;}}
    *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
    body{{font-family:'Be Vietnam Pro',sans-serif;background:var(--light);color:var(--text);}}
    .site-header{{background:var(--primary);height:64px;padding:0 24px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;}}
    .site-logo{{color:#fff;font-size:1.2rem;font-weight:800;text-decoration:none;display:flex;align-items:center;gap:8px;}}
    .site-logo span{{color:var(--accent);}}
    .header-cta{{background:var(--accent);color:var(--primary);font-size:.82rem;font-weight:700;padding:8px 16px;border-radius:20px;text-decoration:none;}}
    .article-wrap{{max-width:820px;margin:0 auto;padding:40px 24px 80px;}}
    .article-tag{{display:inline-block;background:rgba(0,200,150,.12);color:var(--accent);font-size:.75rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:4px 14px;border-radius:20px;margin-bottom:16px;}}
    h1{{font-size:clamp(1.6rem,4vw,2.4rem);color:var(--primary);line-height:1.25;margin-bottom:16px;font-weight:800;}}
    .article-meta{{color:var(--muted);font-size:.85rem;margin-bottom:32px;padding-bottom:20px;border-bottom:2px solid #e8eef4;}}
    .article-body h2{{font-size:1.35rem;font-weight:700;color:var(--primary);margin:36px 0 14px;padding-left:14px;border-left:4px solid var(--accent);}}
    .article-body h3{{font-size:1.1rem;font-weight:700;color:var(--primary);margin:24px 0 10px;}}
    .article-body p{{line-height:1.85;color:#2d4060;margin-bottom:16px;font-size:1rem;}}
    .article-body ul,.article-body ol{{padding-left:24px;margin-bottom:16px;}}
    .article-body li{{line-height:1.8;color:#2d4060;margin-bottom:6px;}}
    .article-body strong{{color:var(--primary);}}
    .highlight-box{{background:linear-gradient(135deg,rgba(0,200,150,.08),rgba(0,200,150,.03));border:1px solid rgba(0,200,150,.25);border-radius:14px;padding:24px;margin:28px 0;}}
    .highlight-box p{{margin:0;}}
    .cta-box{{background:linear-gradient(135deg,var(--primary),#163a6b);border-radius:18px;padding:36px;text-align:center;margin:40px 0;}}
    .cta-box h3{{color:#fff;font-size:1.4rem;margin-bottom:10px;}}
    .cta-box p{{color:rgba(255,255,255,.75);margin-bottom:24px;}}
    .cta-btn{{display:inline-block;background:var(--accent);color:var(--primary);font-weight:800;font-size:1.05rem;padding:14px 36px;border-radius:12px;text-decoration:none;transition:transform .15s;}}
    .cta-btn:hover{{transform:translateY(-2px);}}
    .site-footer{{background:var(--primary);color:rgba(255,255,255,.5);text-align:center;padding:24px;font-size:.82rem;}}
    .site-footer a{{color:var(--accent);text-decoration:none;}}
    @media(max-width:600px){{.article-wrap{{padding:24px 16px 60px;}}}}
  </style>
</head>
<body>
<header class="site-header">
  <a href="/" class="site-logo">💰 <span>Kết Nối Tài Chính 24/7</span></a>
  <a href="/" class="header-cta">Vay ngay →</a>
</header>

<article class="article-wrap">
  <span class="article-tag">📚 Kiến thức tài chính</span>
  <h1>{title}</h1>
  <div class="article-meta">📅 Cập nhật: {date} &nbsp;·&nbsp; ⏱ Đọc trong 5 phút</div>
  <div class="article-body">
{body}
  </div>

  <div class="cta-box">
    <h3>Bạn đang cần vay tiền gấp?</h3>
    <p>Kiểm tra điều kiện miễn phí — kết nối 20+ tổ chức tài chính uy tín, duyệt trong 5 phút.</p>
    <a href="/" class="cta-btn">Kiểm tra điều kiện ngay →</a>
  </div>
</article>

<footer class="site-footer">
  <p>© 2026 Kết Nối Tài Chính 24/7 · <a href="/">Trang chủ</a> · <a href="/blog/">Kiến thức tài chính</a></p>
</footer>
</body>
</html>'''
