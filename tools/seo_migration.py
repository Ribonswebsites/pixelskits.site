from pathlib import Path
from datetime import date
import json

ROOT = Path(__file__).resolve().parents[1]
TODAY = date.today().isoformat()

pages = [
    {
        "file": "image-compressor.html", "slug": "image-compressor", "title": "Image Compressor Online Free | Pixelskits", "description": "Compress JPG, PNG, and WebP images online for free with Pixelskits. Reduce image file size in your browser without uploading files or creating an account.", "h1": "Free Image Compressor", "eyebrow": "IMAGE TOOLS", "intro": "Make images smaller for websites, email, social media, and storage. Pixelskits compresses JPEG, PNG, and WebP files directly in your browser, so your original files stay on your device.", "features": ["Compress JPG, PNG, and WebP images", "Choose a practical balance of quality and file size", "Preview the before-and-after size", "Download instantly with no account"], "keywords": "image compressor online free, compress JPG, compress PNG, reduce image file size, image compressor no upload"
    },
    {
        "file": "image-converter.html", "slug": "image-converter", "title": "Image Converter Online Free: PNG, JPG & WebP | Pixelskits", "description": "Convert PNG, JPG, JPEG, and WebP images online for free with Pixelskits. Change image formats privately in your browser with no upload and no account.", "h1": "Free Image Converter", "eyebrow": "IMAGE TOOLS", "intro": "Convert common image formats in seconds. Pixelskits helps you switch between PNG, JPG, JPEG, and WebP while keeping the process private and browser-based.", "features": ["Convert PNG to JPG and JPG to PNG", "Convert images to WebP for smaller websites", "Keep transparency when the output format supports it", "Process files locally with no server upload"], "keywords": "image converter online free, PNG to JPG, JPG to PNG, WebP converter, convert image format"
    },
    {
        "file": "resize-image.html", "slug": "resize-image", "title": "Resize Image Online Free: Change Image Dimensions | Pixelskits", "description": "Resize images online for free by pixels or percentage with Pixelskits. Set exact dimensions, lock the aspect ratio, and download privately in your browser.", "h1": "Free Image Resizer", "eyebrow": "IMAGE TOOLS", "intro": "Set the exact width and height you need for websites, marketplaces, documents, and social posts. Pixelskits resizes images without requiring an upload or sign-in.", "features": ["Set exact width and height in pixels", "Resize by percentage for quick adjustments", "Lock the aspect ratio to prevent distortion", "Download the resized image immediately"], "keywords": "resize image online free, change image dimensions, resize photo, image resizer no upload"
    },
    {
        "file": "remove-background.html", "slug": "remove-background", "title": "Remove Image Background Free Online | Pixelskits", "description": "Remove backgrounds from images online for free with Pixelskits. Create transparent PNG files using browser-based AI with no account required.", "h1": "Free Background Remover", "eyebrow": "AI IMAGE TOOLS", "intro": "Create clean transparent cutouts for product photos, profile images, thumbnails, and designs. Pixelskits uses browser-based processing where available, so your image stays private.", "features": ["Remove backgrounds from portrait and product images", "Export a transparent PNG", "Use the tool without an account", "Keep files on your device during browser processing"], "keywords": "remove background from image free, background remover online, transparent PNG maker, AI background remover"
    },
    {
        "file": "pdf-tools.html", "slug": "pdf-tools", "title": "Free PDF Tools Online: Convert, Merge & Edit | Pixelskits", "description": "Use free PDF tools from Pixelskits to convert Word files, create PDFs from images, merge documents, edit pages, and convert PDF pages to images.", "h1": "Free PDF Tools", "eyebrow": "PDF TOOLS", "intro": "Handle everyday PDF tasks in one place. Pixelskits includes PDF conversion, merging, editing, image export, and Word document tools with simple browser-based workflows.", "features": ["Convert PDF to Word and Word to PDF", "Create a PDF from one or more images", "Merge multiple PDF files into one", "Convert PDF pages to JPG, PNG, or WebP"], "keywords": "free PDF tools online, PDF to Word, Word to PDF, merge PDF, image to PDF, PDF converter"
    },
    {
        "file": "photo-editor.html", "slug": "photo-editor", "title": "Free Online Photo Editor: Filters, Text & Adjustments | Pixelskits", "description": "Edit photos online for free with Pixelskits. Adjust colour, brightness, contrast, filters, text, borders, watermarks, and more directly in your browser.", "h1": "Free Online Photo Editor", "eyebrow": "IMAGE STUDIO", "intro": "Make quick, useful edits without installing software. Pixelskits brings essential photo adjustments and creative effects together in a private browser editor.", "features": ["Adjust brightness, contrast, saturation, and hue", "Apply photo filters and cinematic colour effects", "Add text, borders, frames, and watermarks", "Export edited images without an account"], "keywords": "free online photo editor, edit photo online, photo filters, add text to image, image editor no download"
    },
    {
        "file": "creator-tools.html", "slug": "creator-tools", "title": "Free YouTube Thumbnail & Social Media Makers | Pixelskits", "description": "Create YouTube thumbnails, channel banners, Instagram posts, stories, X banners, and LinkedIn banners free with Pixelskits creator tools.", "h1": "Free Creator Design Tools", "eyebrow": "CREATOR STUDIO", "intro": "Design social graphics at the right dimensions for the platform you use. Pixelskits provides ready-sized canvases for thumbnails, banners, posts, and stories.", "features": ["Create YouTube thumbnails at 1280×720", "Design YouTube channel art at 2560×1440", "Make Instagram posts and stories", "Build X and LinkedIn profile banners"], "keywords": "YouTube thumbnail maker free, social media post maker, YouTube banner maker, Instagram post maker, LinkedIn banner maker"
    },
    {
        "file": "qr-code-generator.html", "slug": "qr-code-generator", "title": "QR Code Generator Free Online | Pixelskits", "description": "Generate a QR code from any URL or text for free with Pixelskits. Customise and download a high-resolution QR code in your browser with no sign-up.", "h1": "Free QR Code Generator", "eyebrow": "UTILITY TOOLS", "intro": "Turn a link or message into a downloadable QR code in seconds. Pixelskits keeps the workflow simple, free, and available without an account.", "features": ["Generate QR codes from URLs or plain text", "Download a high-resolution PNG", "Create codes for print, packaging, and social profiles", "Use the generator without registration"], "keywords": "QR code generator free, QR code maker online, create QR code from URL, downloadable QR code"
    },
]

style = """
:root{color-scheme:dark;--bg:#08080f;--panel:#111321;--text:#f2f4ff;--muted:#a4acc9;--accent:#0ce4fa;--orange:#ff4d1c}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 10% 0%,#18213f 0,#08080f 42%);color:var(--text);font-family:Inter,system-ui,-apple-system,Segoe UI,sans-serif;line-height:1.65}a{color:inherit}.wrap{max-width:1050px;margin:auto;padding:0 22px}.top{padding:22px 0;border-bottom:1px solid #252a40}.brand{font-weight:900;letter-spacing:-.04em;font-size:1.25rem;text-decoration:none}.brand span{color:var(--accent)}nav{float:right;display:flex;gap:18px;color:var(--muted);font-size:.9rem}nav a{text-decoration:none}main{padding:78px 0 70px}.eyebrow{color:var(--accent);font-size:.76rem;font-weight:800;letter-spacing:.18em}.hero{max-width:780px}.hero h1{font-size:clamp(2.5rem,7vw,5.5rem);line-height:1.02;letter-spacing:-.065em;margin:15px 0 20px}.hero p{font-size:1.18rem;color:var(--muted);max-width:700px}.button{display:inline-block;background:var(--orange);padding:13px 20px;border-radius:999px;text-decoration:none;font-weight:800;margin-top:15px}.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin:52px 0}.card{background:rgba(17,19,33,.88);border:1px solid #2a3047;border-radius:18px;padding:24px}.card h2{font-size:1.15rem;margin:0 0 8px}.card p,.card li{color:var(--muted)}.related{border-top:1px solid #252a40;padding:30px 0 20px}.related a{display:inline-block;margin:7px 12px 7px 0;color:var(--accent)}footer{border-top:1px solid #252a40;padding:28px 0 50px;color:var(--muted);font-size:.9rem}@media(max-width:680px){nav{float:none;margin-top:12px;gap:12px;flex-wrap:wrap}.grid{grid-template-columns:1fr}main{padding-top:50px}}
"""

def page_html(p):
    canonical = f"https://pixelskits.site/{p['file']}"
    related = ''.join(f'<a href="{q["file"]}">{q["h1"].replace("Free ", "")}</a>' for q in pages if q is not p)[:900]
    schema = {
      "@context":"https://schema.org", "@graph":[
        {"@type":"WebPage","@id":canonical+"#webpage","url":canonical,"name":p["title"],"description":p["description"],"isPartOf":{"@id":"https://pixelskits.site/#website"},"inLanguage":"en-US","breadcrumb":{"@id":canonical+"#breadcrumb"}},
        {"@type":"BreadcrumbList","@id":canonical+"#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Pixelskits","item":"https://pixelskits.site/"},{"@type":"ListItem","position":2,"name":p["h1"],"item":canonical}]},
        {"@type":"WebApplication","name":p["h1"],"url":canonical,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","isAccessibleForFree":True,"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"provider":{"@type":"Organization","name":"Pixelskits","url":"https://pixelskits.site/"}}
      ]
    }
    lis=''.join(f'<li>{x}</li>' for x in p['features'])
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{p['title']}</title><meta name="description" content="{p['description']}"><meta name="keywords" content="{p['keywords']}"><meta name="author" content="Ribon Patil"><meta name="robots" content="index,follow,max-image-preview:large"><link rel="canonical" href="{canonical}"><link rel="sitemap" type="application/xml" href="/sitemap.xml"><meta property="og:type" content="website"><meta property="og:site_name" content="Pixelskits"><meta property="og:title" content="{p['title']}"><meta property="og:description" content="{p['description']}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="https://pixelskits.site/og-image.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{p['title']}"><meta name="twitter:description" content="{p['description']}"><meta name="twitter:image" content="https://pixelskits.site/og-image.png"><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script><style>{style}</style></head><body><header class="top"><div class="wrap"><a class="brand" href="index.html">Pixels<span>kits</span></a><nav><a href="index.html">All tools</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy</a></nav></div></header><main><div class="wrap"><section class="hero"><div class="eyebrow">{p['eyebrow']} · PIXELSKITS</div><h1>{p['h1']}</h1><p>{p['intro']}</p><a class="button" href="index.html#features">Open Pixelskits tools</a></section><section class="grid"><article class="card"><h2>What you can do</h2><ul>{lis}</ul></article><article class="card"><h2>Why use Pixelskits?</h2><p>Pixelskits is a free browser-based toolkit. There is no account, subscription, installation, or routine server upload. Open the tool, process your file, and save the result to your device.</p><p>It works on modern desktop and mobile browsers and is designed for quick everyday tasks.</p></article></section><section class="related"><h2>Explore more Pixelskits tools</h2>{related}</section></div></main><footer><div class="wrap"><strong>Pixelskits</strong> — free image, PDF, photo, and creator tools. <a href="index.html">Return to the Pixelskits home page</a>.</div></footer></body></html>'''

for p in pages:
    (ROOT / p['file']).write_text(page_html(p), encoding='utf-8')

index = ROOT / 'index.html'
text = index.read_text(encoding='utf-8')
text = text.replace('<title>Pixelskits — Free Image & PDF Tools Online | No Upload Required</title>', '<title>Pixelskits | Free Online Image &amp; PDF Tools</title>')
text = text.replace('<meta name="description" content="Pixelskits: 30+ free image & PDF tools — compress, convert, remove background with AI, merge PDF, resize, edit photos, make YouTube thumbnails & QR codes. Runs 100% in your browser. No upload. No account. Instant.">', '<meta name="description" content="Pixelskits is a free online toolkit for compressing, converting, resizing, editing, and removing image backgrounds, plus PDF tools, QR codes, and creator graphics. Private, browser-based, and no account required.">')
text = text.replace('<meta name="keywords" content="', '<meta name="keywords" content="Pixelskits, free online image tools, free PDF tools, image compressor, image converter, image resizer, remove background, photo editor, QR code generator, YouTube thumbnail maker, creator tools, browser-based image tools, no upload tools, private image processing, ')
text = text.replace('"alternateName": ["Pixelskits Free Tools", "Pixelskits Image Tools"],', '"alternateName": ["Pixelskits Tools"],')
text = text.replace('<meta property="og:title" content="Pixelskits — Free Image & PDF Tools | AI Background Remover, Compress, Convert">', '<meta property="og:title" content="Pixelskits | Free Online Image &amp; PDF Tools">')
text = text.replace('<meta name="twitter:title" content="Pixelskits — Free Image & PDF Tools | No Upload, No Account">', '<meta name="twitter:title" content="Pixelskits | Free Online Image &amp; PDF Tools">')
nav = '''<!-- SEO LANDING PAGES: crawlable category architecture -->
    <section aria-labelledby="seo-pages-heading" style="padding:42px 20px;max-width:1180px;margin:0 auto;">
      <h2 id="seo-pages-heading">Explore Pixelskits tools</h2>
      <p>Open a focused tool guide, then launch the free browser-based tool.</p>
      <p><a href="image-compressor.html">Image Compressor</a> · <a href="image-converter.html">Image Converter</a> · <a href="resize-image.html">Image Resizer</a> · <a href="remove-background.html">Background Remover</a> · <a href="pdf-tools.html">PDF Tools</a> · <a href="photo-editor.html">Photo Editor</a> · <a href="creator-tools.html">Creator Tools</a> · <a href="qr-code-generator.html">QR Code Generator</a></p>
    </section>

'''
marker = '    <!-- ══ MOBILE LEGAL STRIP ══ -->'
if nav not in text:
    text = text.replace(marker, nav + marker)
index.write_text(text, encoding='utf-8')

urls = ['https://pixelskits.site/'] + [f"https://pixelskits.site/{p['file']}" for p in pages] + ['https://pixelskits.site/contact.html','https://pixelskits.site/privacy.html','https://pixelskits.site/terms.html','https://pixelskits.site/cookies.html']
xml = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url in urls:
    xml += [f'  <url><loc>{url}</loc><lastmod>{TODAY}</lastmod></url>']
xml += ['</urlset>']
(ROOT/'sitemap.xml').write_text('\n'.join(xml)+'\n', encoding='utf-8')

# Keep this truthful and easy to replace once Search Console supplies a token.
robots = ROOT/'robots.txt'
r = robots.read_text(encoding='utf-8')
if 'Sitemap: https://pixelskits.site/sitemap.xml' not in r:
    r += '\nSitemap: https://pixelskits.site/sitemap.xml\n'
robots.write_text(r, encoding='utf-8')
print(f'Generated {len(pages)} SEO landing pages, updated homepage metadata/navigation, and rebuilt sitemap with {len(urls)} canonical URLs.')
