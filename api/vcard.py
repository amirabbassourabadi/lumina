from http.server import BaseHTTPRequestHandler
import os
import urllib.request
import urllib.parse

# این دو متغیر رو تو پنل Vercel، بخش Environment Variables ست کن
# هیچ‌وقت مستقیم تو کد ننویسشون
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# محتوای vCard - این مقادیر رو با اطلاعات واقعی خودت جایگزین کن
VCARD_CONTENT = """BEGIN:VCARD
VERSION:3.0
FN:Lumina AI Visual Studio
ORG:Lumina AI Visual Studio
TITLE:AI Visual Content for Luxury Jewelry Brands
TEL;TYPE=CELL:+98912XXXXXXX
EMAIL:info@lumina-studio.ir
URL:https://lumina-studio.ir
END:VCARD
"""


def notify_scan():
    """یه پیام به تلگرام خودت می‌فرسته - اگه شکست بخوره، جلوی نمایش vCard رو نمی‌گیره"""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": "📇 یه نفر QR کارت ویزیت لومینا رو اسکن کرد.",
        }).encode()
        urllib.request.urlopen(url, data=data, timeout=3)
    except Exception:
        pass


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        notify_scan()
        self.send_response(200)
        self.send_header("Content-Type", "text/vcard; charset=utf-8")
        self.send_header("Content-Disposition", 'attachment; filename="Lumina.vcf"')
        self.end_headers()
        self.wfile.write(VCARD_CONTENT.encode("utf-8"))
        return
