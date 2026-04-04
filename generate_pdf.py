#!/usr/bin/env python3
"""
Manager Today × Claude Cowork 課程講義
社群風格 PDF 生成器 (1080×1080px × 12 頁)
"""

import os, glob, io, sys
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.lib.utils import ImageReader

# ──────────────────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────────────────
BRAND  = "Manager Today × Claude Cowork"
OUTPUT = os.path.expanduser("~/Desktop/claude_cowork_講義.pdf")
W = H  = 1080
TOTAL  = 12
PAD    = 72      # page outer margin
CPAD   = 40      # card inner padding

# Palette
BG     = (237, 235, 230)   # #EDEBE6 暖米白
ACCENT = (201, 100,  66)   # #C96442 Claude 橘
TEXTC  = ( 26,  24,  20)   # #1A1814 近黑
WHITE  = (255, 255, 255)
DIM    = (140, 132, 120)   # 輔助文字
DIVID  = (214, 210, 203)   # 分隔線
ACLT   = (247, 228, 218)   # 淡橘
SHAD   = (194, 186, 174)   # 陰影

# Font dir
FONT_DIR = "/home/user/fonts"

# ──────────────────────────────────────────────────────────
# FONTS
# ──────────────────────────────────────────────────────────
def _load(weight, size):
    path = os.path.join(FONT_DIR, f"NotoSerifCJKtc-{weight}.otf")
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    # fallback: search system
    for base in ["/usr/share/fonts", "/usr/local/share/fonts",
                 os.path.expanduser("~/.fonts")]:
        hits = glob.glob(os.path.join(base, "**", f"*CJK*{weight}*"), recursive=True)
        for h in hits:
            try: return ImageFont.truetype(h, size)
            except: pass
    try:    return ImageFont.load_default(size=size)
    except: return ImageFont.load_default()

def load_fonts():
    return {
        "h1"   : _load("Bold",     72),
        "h2"   : _load("Bold",     50),
        "h3"   : _load("SemiBold", 38),
        "h4"   : _load("SemiBold", 29),
        "body" : _load("Regular",  26),
        "small": _load("Light",    22),
        "tag"  : _load("SemiBold", 20),
        "badge": _load("Bold",     30),
        "brand": _load("Light",    19),
        "num"  : _load("Bold",     54),
    }

# ──────────────────────────────────────────────────────────
# DRAWING HELPERS
# ──────────────────────────────────────────────────────────
def tsize(font, text):
    bb = font.getbbox(text)
    return bb[2] - bb[0], bb[3] - bb[1]

def lh(font, extra=8):
    a, d = font.getmetrics()
    return a + d + extra

def txt(draw, x, y, text, font, fill=None):
    """Draw text with bbox-offset correction so (x,y) = visual top-left."""
    if fill is None: fill = TEXTC
    bb = font.getbbox(text)
    draw.text((x - bb[0], y - bb[1]), text, font=font, fill=fill)
    return bb[3] - bb[1]

def txt_c(draw, cx, cy, text, font, fill=None):
    """Draw text centred on (cx, cy)."""
    if fill is None: fill = TEXTC
    tw, th = tsize(font, text)
    txt(draw, cx - tw // 2, cy - th // 2, text, font, fill)

def wrap(font, text, max_w):
    """CJK-safe character-by-character word wrap."""
    lines = []
    for para in text.split('\n'):
        if not para:
            lines.append('')
            continue
        cur = ''
        for ch in para:
            if font.getbbox(cur + ch)[2] <= max_w:
                cur += ch
            else:
                if cur: lines.append(cur)
                cur = ch
        if cur: lines.append(cur)
    return lines

def txtwrap(draw, x, y, text, font, max_w, fill=None, leading=6):
    """Draw wrapped text; return new y after last line."""
    if fill is None: fill = TEXTC
    a, d = font.getmetrics()
    step = a + d + leading
    for line in wrap(font, text, max_w):
        bb = font.getbbox(line) if line else (0, 0, 0, 0)
        draw.text((x - bb[0], y - bb[1]), line, font=font, fill=fill)
        y += step
    return y

def card(draw, x, y, w, h, r=18, bg=None, shadow=True):
    if bg is None: bg = WHITE
    if shadow:
        draw.rounded_rectangle([x+4, y+6, x+w+4, y+h+6], radius=r, fill=SHAD)
    draw.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=bg)

def pill(draw, x, y, text, font, bg=None, fg=WHITE, ph=18, pv=9):
    if bg is None: bg = ACCENT
    tw, th = tsize(font, text)
    pw = tw + ph * 2
    draw.rounded_rectangle([x, y, x+pw, y+th+pv*2],
                            radius=(th + pv * 2) // 2, fill=bg)
    bb = font.getbbox(text)
    draw.text((x + ph - bb[0], y + pv - bb[1]), text, font=font, fill=fg)
    return pw, th + pv * 2

def badge(draw, cx, cy, n, fonts, r=32):
    draw.ellipse([cx-r+3, cy-r+4, cx+r+3, cy+r+4], fill=SHAD)
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=ACCENT)
    txt_c(draw, cx, cy, str(n), fonts['badge'], fill=WHITE)

def acbar(draw, x, y, h=56, w=6):
    draw.rectangle([x, y, x+w, y+h], fill=ACCENT)

def footer(draw, fonts, pg):
    y0 = H - PAD - 32
    draw.line([(PAD, y0), (W-PAD, y0)], fill=DIVID, width=1)
    txt(draw, PAD, y0+10, BRAND, fonts['brand'], fill=DIM)
    pstr = f"{pg:02d} / {TOTAL:02d}"
    tw, _ = tsize(fonts['brand'], pstr)
    txt(draw, W - PAD - tw, y0+10, pstr, fonts['brand'], fill=ACCENT)

def new_page():
    img = Image.new('RGB', (W, H), BG)
    return img, ImageDraw.Draw(img)


# ──────────────────────────────────────────────────────────
# PAGE 01 – 封面
# ──────────────────────────────────────────────────────────
def p01_cover(F):
    img, draw = new_page()
    # Decorative corners
    draw.rectangle([W-180, 0, W, 180], fill=ACLT)
    draw.rectangle([W-90,  0, W,  90], fill=ACCENT)
    draw.rectangle([0, H-110, 110, H], fill=ACLT)

    y = PAD
    pill(draw, PAD, y, "  2024 完整講義  ", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=116, w=7)
    x0 = PAD + 22
    txt(draw, x0, y+4,  "Claude Cowork", F['h1'], fill=TEXTC)
    txt(draw, x0, y+4+lh(F['h1'], extra=2), "共工術", F['h1'], fill=ACCENT)
    y += 116 + 22

    # Sub-card
    card(draw, PAD, y, W-PAD*2, 118, r=16)
    txt(draw, PAD+CPAD, y+18,
        "主管如何用 AI 讓工作效率翻 3 倍", F['h4'], fill=TEXTC)
    txt(draw, PAD+CPAD, y+18+lh(F['h4'], extra=4),
        "從提示詞設計到每日工作流，系統性掌握 Claude", F['body'], fill=DIM)
    y += 138

    # 3 stat boxes
    stats = [("20萬", "Token 上限"), ("12頁", "完整講義"), ("6步驟", "系統方法")]
    bw = (W - PAD*2 - 20) // 3
    for i, (v, l) in enumerate(stats):
        bx = PAD + i*(bw+10)
        card(draw, bx, y, bw, 110, r=14)
        txt(draw, bx+26, y+16, v, F['h3'], fill=ACCENT)
        txt(draw, bx+26, y+16+lh(F['h3'], extra=2), l, F['small'], fill=DIM)

    footer(draw, F, 1)
    return img

# ──────────────────────────────────────────────────────────
# PAGE 02 – 痛點
# ──────────────────────────────────────────────────────────
def p02_pain(F):
    img, draw = new_page()
    y = PAD
    pill(draw, PAD, y, "課程背景", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=66, w=7)
    txt(draw, PAD+22, y,      "你是否也有這些",  F['h2'], fill=TEXTC)
    txt(draw, PAD+22, y+lh(F['h2'], extra=2), "職場痛點？", F['h2'], fill=ACCENT)
    y += lh(F['h2'])*2 + 24

    pains = [
        ("▪", "被瑣事淹沒，沒時間思考策略",
              "開會、回信、寫報告排滿行事曆，主管核心價值無法發揮"),
        ("▪", "AI 工具用了，卻沒效果",
              "下了指令卻收到廢話，嘗試幾次就放棄，白白浪費時間"),
        ("▪", "不知道怎麼「對 AI 說話」",
              "提示詞寫不好，同樣工具別人用得很爽，自己卡關沮喪"),
        ("▪", "看著同事用 AI 起飛，自己焦慮",
              "數位轉型浪潮來臨，擔心自身競爭力被快速侵蝕"),
    ]

    cw = W - PAD*2
    ch, gap = 114, 12
    for i, (bull, title, desc) in enumerate(pains):
        cy = y + i*(ch+gap)
        card(draw, PAD, cy, cw, ch, r=16)
        draw.ellipse([PAD+CPAD-4, cy+ch//2-16, PAD+CPAD+28, cy+ch//2+20],
                     fill=ACLT)
        txt(draw, PAD+CPAD, cy+ch//2-14, bull, F['h4'], fill=ACCENT)
        tx = PAD+CPAD+46
        txt(draw, tx, cy+18, title, F['h4'], fill=TEXTC)
        txt(draw, tx, cy+18+lh(F['h4'], extra=2), desc, F['small'], fill=DIM)

    footer(draw, F, 2)
    return img

# ──────────────────────────────────────────────────────────
# PAGE 03 – 工具介紹
# ──────────────────────────────────────────────────────────
def p03_intro(F):
    img, draw = new_page()
    y = PAD
    pill(draw, PAD, y, "工具介紹", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=52, w=7)
    txt(draw, PAD+22, y, "什麼是 Claude？", F['h2'], fill=TEXTC)
    y += lh(F['h2'], extra=22)

    card(draw, PAD, y, W-PAD*2, 118, r=16)
    txtwrap(draw, PAD+CPAD, y+20,
            "由 Anthropic 開發的企業級 AI 助理，以安全性、長脈絡理解、\n"
            "精準中文寫作著稱。是主管、知識工作者的最佳 AI 搭檔。",
            F['body'], W-PAD*2-CPAD*2, fill=TEXTC, leading=6)
    y += 138

    feats = [
        ("◆", "超長脈絡視窗",  "支援 200K Token\n整份報告一次分析"),
        ("◆", "精準中文寫作",  "中英混排流暢\n輸出可直接使用"),
        ("◆", "邏輯思維清晰",  "不亂掰、懂追問\n主動澄清模糊需求"),
        ("◆", "企業安全合規",  "不用訓練資料\n適合處理機敏資訊"),
    ]

    cw = W - PAD*2
    fw = (cw - 16) // 2
    fh = 136
    for i, (ico, ttl, desc) in enumerate(feats):
        row, col = divmod(i, 2)
        fx = PAD + col*(fw+16)
        fy = y + row*(fh+14)
        card(draw, fx, fy, fw, fh, r=14)
        draw.ellipse([fx+CPAD-4, fy+18, fx+CPAD+28, fy+52], fill=ACLT)
        txt(draw, fx+CPAD, fy+20, ico, F['h4'], fill=ACCENT)
        txt(draw, fx+CPAD+38, fy+18, ttl, F['h4'], fill=TEXTC)
        txtwrap(draw, fx+CPAD+38, fy+18+lh(F['h4'], extra=4), desc,
                F['small'], fw-CPAD-38-16, fill=DIM, leading=4)

    footer(draw, F, 3)
    return img


# ──────────────────────────────────────────────────────────
# PAGE 04 – 三款工具比較
# ──────────────────────────────────────────────────────────
def p04_compare(F):
    img, draw = new_page()
    y = PAD
    pill(draw, PAD, y, "工具比較", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=52, w=7)
    txt(draw, PAD+22, y, "三款 AI 工具比較", F['h2'], fill=TEXTC)
    y += lh(F['h2'], extra=22)

    cw = W - PAD*2          # 936
    c0, c1 = 210, (cw-210)//3   # label col, data cols
    cols = [c0, c1, c1, cw-c0-c1*2]
    headers = ["功能項目", "Claude", "ChatGPT", "Gemini"]
    rh = 72

    # Header row
    card(draw, PAD, y, cw, rh, r=12, bg=ACCENT, shadow=False)
    x0 = PAD
    for ci, (cw_c, hdr) in enumerate(zip(cols, headers)):
        if ci == 0:
            txt(draw, x0+18, y+rh//2-14, hdr, F['tag'], fill=WHITE)
        else:
            tw, th = tsize(F['h4'], hdr)
            txt(draw, x0+(cw_c-tw)//2, y+rh//2-th//2, hdr, F['h4'], fill=WHITE)
        x0 += cw_c
    y += rh + 6

    rows = [
        ("中文寫作品質",  "◆◆◆◆◆", "◆◆◆◆",  "◆◆◆"),
        ("長文脈絡理解",  "◆◆◆◆◆", "◆◆◆◆",  "◆◆◆◆"),
        ("邏輯推理能力",  "◆◆◆◆◆", "◆◆◆◆◆", "◆◆◆◆"),
        ("企業安全合規",  "◆◆◆◆◆", "◆◆◆",   "◆◆◆◆"),
        ("介面易用度",    "◆◆◆◆",  "◆◆◆◆◆", "◆◆◆◆"),
        ("免費方案豐富",  "◆◆◆",   "◆◆◆◆",  "◆◆◆◆◆"),
    ]

    for ri, (feat, c1v, c2v, c3v) in enumerate(rows):
        bg = (244, 242, 237) if ri % 2 == 0 else WHITE
        card(draw, PAD, y, cw, rh-4, r=10, bg=bg, shadow=False)
        x0 = PAD
        for ci, (cw_c, val) in enumerate(zip(cols, [feat, c1v, c2v, c3v])):
            fc = ACCENT if ci == 1 else (TEXTC if ci == 0 else DIM)
            fn = F['small']
            tw, th = tsize(fn, val)
            if ci == 0:
                txt(draw, x0+18, y+rh//2-th//2-2, val, fn, fill=TEXTC)
            else:
                txt(draw, x0+(cw_c-tw)//2, y+rh//2-th//2-2, val, fn, fill=fc)
            x0 += cw_c
        y += rh + 2

    y += 10
    txt(draw, PAD, y, "▸ ◆ 越多表示該項越強；依 2024 年實測結果，僅供參考",
        F['small'], fill=DIM)

    footer(draw, F, 4)
    return img

# ──────────────────────────────────────────────────────────
# GENERIC STEP PAGE SHELL
# ──────────────────────────────────────────────────────────
def step_shell(F, pg, step_n, title, subtitle, content_fn):
    img, draw = new_page()
    y = PAD

    br = 36
    bx, by = PAD + br, y + br
    badge(draw, bx, by, step_n, F, r=br)

    tx = PAD + br*2 + 20
    txt(draw, tx, y+4,  f"Step {step_n}", F['tag'], fill=ACCENT)
    txt(draw, tx, y+4+lh(F['tag'], extra=2), title, F['h2'], fill=TEXTC)
    y += br*2 + 16

    txtwrap(draw, PAD, y, subtitle, F['body'], W-PAD*2, fill=DIM, leading=6)
    y += lh(F['body'], extra=18)

    draw.line([(PAD, y), (W-PAD, y)], fill=DIVID, width=1)
    y += 18

    content_fn(draw, img, y, F)
    footer(draw, F, pg)
    return img

# ──────────────────────────────────────────────────────────
# PAGE 05 – Step 1：設定 AI 角色
# ──────────────────────────────────────────────────────────
def p05_step1(F):
    def content(draw, img, y, F):
        items = [
            ("01", "確立 Claude 的專業身份",
                   "例：「你是一位資深 B2B 行銷總監，熟悉台灣科技業生態，\n擅長用數據說故事…」"),
            ("02", "設定語氣與輸出風格",
                   "例：「請用正式但不生硬的中文，條列重點，\n每點不超過 30 字，避免廢話開場」"),
            ("03", "加入限制條件",
                   "例：「不用 emoji，不重複我說過的話，\n如需澄清請先問我，不要自行假設」"),
        ]
        cw = W - PAD*2
        for i, (num, title, desc) in enumerate(items):
            cy = y + i * 154
            card(draw, PAD, cy, cw, 140, r=16)
            draw.ellipse([PAD+CPAD-4, cy+20, PAD+CPAD+32, cy+56], fill=ACLT)
            txt(draw, PAD+CPAD, cy+22, num, F['tag'], fill=ACCENT)
            tx = PAD+CPAD+50
            txt(draw, tx, cy+18, title, F['h4'], fill=TEXTC)
            txtwrap(draw, tx, cy+18+lh(F['h4'], extra=4), desc,
                    F['small'], cw-CPAD-50-20, fill=DIM, leading=4)

    return step_shell(F, 5, 1, "設定 AI 角色",
        "告訴 Claude「它是誰」，輸出品質立刻提升 80%", content)

# ──────────────────────────────────────────────────────────
# PAGE 06 – Step 2：給足脈絡
# ──────────────────────────────────────────────────────────
def p06_step2(F):
    def content(draw, img, y, F):
        items = [
            ("Background\n背景脈絡",
             "你的公司、產品、目標客群、當前挑戰是什麼？\n給越多，Claude 的建議越貼近你的實際情境。"),
            ("Objective\n任務目標",
             "這次你希望達成什麼？給 Claude 明確的成功標準，\n例如「輸出一份可直接寄出的提案大綱」。"),
            ("Reference\n參考資料",
             "貼入相關文件、數據、上次版本、競品範例，\n讓 AI 有料可用，避免憑空發揮。"),
        ]
        cw = W - PAD*2
        for i, (label, desc) in enumerate(items):
            cy = y + i * 154
            card(draw, PAD, cy, cw, 140, r=16)
            lines = label.split('\n')
            pill(draw, PAD+CPAD, cy+18, lines[0], F['tag'], bg=ACCENT, fg=WHITE)
            pw, ph = tsize(F['tag'], lines[0])
            txt(draw, PAD+CPAD + pw + 56, cy+22, lines[1], F['small'], fill=DIM)
            txtwrap(draw, PAD+CPAD, cy+18+46, desc,
                    F['body'], cw-CPAD*2, fill=TEXTC, leading=6)

    return step_shell(F, 6, 2, "給足脈絡",
        "AI 的輸出品質 = 你給的脈絡品質，垃圾進、垃圾出", content)


# ──────────────────────────────────────────────────────────
# PAGE 07 – Step 3：精準下指令
# ──────────────────────────────────────────────────────────
def p07_step3(F):
    def content(draw, img, y, F):
        card(draw, PAD, y, W-PAD*2, 108, r=16, bg=ACLT, shadow=True)
        txt(draw, PAD+CPAD, y+16, "◆ 黃金指令公式", F['h4'], fill=ACCENT)
        txt(draw, PAD+CPAD, y+16+lh(F['h4'], extra=6),
            "角色設定  ＋  任務說明  ＋  輸出格式  ＋  限制條件  ＋  範例",
            F['body'], fill=TEXTC)
        y += 128

        tips = [
            ("▪", "指定輸出格式",
                  "「請以 Markdown 表格呈現」「請用五個條列重點」"),
            ("▪", "給予 2-3 個範例（Few-Shot）",
                  "「參考以下格式輸出：[你的範例]，風格保持一致」"),
            ("▪", "設定字數與語氣",
                  "「每點不超過 30 字」「語氣正式但不生硬，避免制式開場」"),
        ]
        cw = W - PAD*2
        for i, (ico, title, desc) in enumerate(tips):
            cy = y + i * 128
            card(draw, PAD, cy, cw, 114, r=14)
            txt(draw, PAD+CPAD, cy+20, ico, F['h4'], fill=ACCENT)
            txt(draw, PAD+CPAD+34, cy+18, title, F['h4'], fill=TEXTC)
            txt(draw, PAD+CPAD+34, cy+18+lh(F['h4'], extra=4),
                desc, F['small'], fill=DIM)

    return step_shell(F, 7, 3, "精準下指令",
        "一個結構清晰的提示詞，能讓 Claude 第一次就命中目標", content)

# ──────────────────────────────────────────────────────────
# PAGE 08 – Step 4：迭代優化輸出
# ──────────────────────────────────────────────────────────
def p08_step4(F):
    def content(draw, img, y, F):
        steps = [
            ("01", "評估初稿方向",
                   "找出哪裡對、哪裡需調整，不要動輒全部重來"),
            ("02", "定點精準修改",
                   "「第二段邏輯不清，請重寫」比「重新來過」有效 5 倍"),
            ("03", "追問深挖細節",
                   "「這個點很好，請展開並給出三個具體例子」"),
            ("04", "鎖定並整理終稿",
                   "滿意後請 Claude「整理最終版」，確保格式一致"),
        ]
        cw = W - PAD*2
        ch = 106
        for i, (num, title, desc) in enumerate(steps):
            cy = y + i*(ch+12)
            card(draw, PAD, cy, cw, ch, r=14)
            txt(draw, PAD+CPAD, cy+ch//2-30, num, F['num'], fill=ACLT)
            tx = PAD+CPAD+82
            txt(draw, tx, cy+18, title, F['h4'], fill=TEXTC)
            txt(draw, tx, cy+18+lh(F['h4'], extra=4), desc, F['small'], fill=DIM)

    return step_shell(F, 8, 4, "迭代優化輸出",
        "把 Claude 當高階編輯，不斷精煉，直到滿意為止", content)

# ──────────────────────────────────────────────────────────
# PAGE 09 – Step 5：建立提示模板庫
# ──────────────────────────────────────────────────────────
def p09_step5(F):
    def content(draw, img, y, F):
        txt(draw, PAD, y,
            "建立專屬你職位的提示詞模板庫，重複使用，效率倍增",
            F['body'], fill=DIM)
        y += lh(F['body'], extra=16)

        templates = [
            ("週報模板",    "角色+背景+格式固定\n每週只需填入本週數據"),
            ("會議記錄",    "自動分類決議事項\n行動清單 / 待確認項目"),
            ("提案框架",    "問題→方案→效益→風險\n→行動，結構完整"),
            ("Email 模板",  "主旨明確，首段結論\n條列說明，結尾行動呼籲"),
        ]

        cw = W - PAD*2
        fw = (cw - 16) // 2
        fh = 132
        for i, (title, desc) in enumerate(templates):
            row, col = divmod(i, 2)
            fx = PAD + col*(fw+16)
            fy = y + row*(fh+16)
            card(draw, fx, fy, fw, fh, r=14)
            # Left accent stripe
            draw.rounded_rectangle([fx, fy, fx+6, fy+fh], radius=14, fill=ACCENT)
            txt(draw, fx+22, fy+18, title, F['h4'], fill=ACCENT)
            txtwrap(draw, fx+22, fy+18+lh(F['h4'], extra=6), desc,
                    F['small'], fw-40, fill=DIM, leading=5)

    return step_shell(F, 9, 5, "建立提示模板庫",
        "好的模板是資產，讓你的 AI 效率可以被複製與傳承", content)

# ──────────────────────────────────────────────────────────
# PAGE 10 – Step 6：整合進工作流
# ──────────────────────────────────────────────────────────
def p10_step6(F):
    def content(draw, img, y, F):
        flows = [
            ("早晨",  "▸ 每日優先任務整理與排序\n▸ 昨日會議行動項目追蹤"),
            ("上午",  "▸ 文件起草與即時優化\n▸ Email 快速回覆範本"),
            ("下午",  "▸ 會議準備與議程規劃\n▸ 數據摘要與洞察分析"),
            ("傍晚",  "▸ 週報 / 日報自動生成\n▸ 隔日任務預規劃"),
        ]
        cw = W - PAD*2
        fw = (cw - 16) // 2
        fh = 148
        for i, (time_label, tasks) in enumerate(flows):
            row, col = divmod(i, 2)
            fx = PAD + col*(fw+16)
            fy = y + row*(fh+16)
            card(draw, fx, fy, fw, fh, r=14)
            pill(draw, fx+20, fy+18, time_label, F['tag'],
                 bg=ACCENT, fg=WHITE)
            txtwrap(draw, fx+20, fy+18+48, tasks,
                    F['body'], fw-44, fill=TEXTC, leading=8)

    return step_shell(F, 10, 6, "整合進工作流",
        "把 Claude 嵌入每日行事曆，讓效率提升成為新習慣", content)


# ──────────────────────────────────────────────────────────
# PAGE 11 – 進階魔法一二三
# ──────────────────────────────────────────────────────────
def p11_magic(F):
    img, draw = new_page()
    y = PAD
    pill(draw, PAD, y, "進階技巧", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=66, w=7)
    txt(draw, PAD+22, y,      "進階魔法",       F['h2'], fill=TEXTC)
    txt(draw, PAD+22, y+lh(F['h2'], extra=2),
        "一 ▸ 二 ▸ 三",  F['h2'], fill=ACCENT)
    y += lh(F['h2'])*2 + 26

    magics = [
        ("一", "思維鏈  Chain of Thought",
               "指令末加上「請一步步思考後再回答」，複雜任務準確率大幅提升。\n"
               "▸ 適用：邏輯推理、多方案評估、風險分析"),
        ("二", "範例學習  Few-Shot Prompting",
               "在指令中附上 2-3 個你滿意的範例，Claude 會學習你的格式與語氣。\n"
               "▸ 適用：固定格式報告、品牌語氣寫作、特定結構輸出"),
        ("三", "角色扮演  Role-Play Scenario",
               "讓 Claude 扮演「挑剔的客戶」或「競爭對手」來挑戰你的方案。\n"
               "▸ 適用：提案預演、產品壓力測試、談判情境演練"),
    ]

    cw = W - PAD*2
    ch = 148
    for i, (num, title, desc) in enumerate(magics):
        cy = y + i*(ch+16)
        card(draw, PAD, cy, cw, ch, r=16)
        txt(draw, PAD+CPAD, cy+ch//2-34, num, F['num'], fill=ACLT)
        tx = PAD+CPAD+80
        txt(draw, tx, cy+16, title, F['h4'], fill=TEXTC)
        txtwrap(draw, tx, cy+16+lh(F['h4'], extra=6), desc,
                F['small'], cw-CPAD-80-20, fill=DIM, leading=5)

    footer(draw, F, 11)
    return img

# ──────────────────────────────────────────────────────────
# PAGE 12 – 行動清單
# ──────────────────────────────────────────────────────────
def p12_action(F):
    img, draw = new_page()
    y = PAD
    pill(draw, PAD, y, "行動清單", F['tag'])
    y += 50

    acbar(draw, PAD, y, h=66, w=7)
    txt(draw, PAD+22, y,      "學完就做！",    F['h2'], fill=ACCENT)
    txt(draw, PAD+22, y+lh(F['h2'], extra=2),
        "本週行動清單",  F['h2'], fill=TEXTC)
    y += lh(F['h2'])*2 + 24

    groups = [
        ("本日", [
            "▸ 申請 Claude.ai 帳號（免費版即可開始）",
            "▸ 用「角色設定法」完成一封工作 Email",
        ]),
        ("本週", [
            "▸ 建立你的第一個提示模板（週報或會議記錄）",
            "▸ 用 Step 1–3 公式完成一份提案或報告",
            "▸ 試驗「思維鏈」技巧於一個複雜決策情境",
        ]),
        ("本月", [
            "▸ 建立完整個人提示詞模板庫（5 個以上）",
            "▸ 將 Claude 整合進每日晨間工作流程",
            "▸ 教會一位同事使用 Claude，鞏固自己的學習",
        ]),
    ]

    cw = W - PAD*2
    for period, items in groups:
        line_height = lh(F['body'], extra=4)
        ch = CPAD + len(items) * line_height + CPAD//2
        card(draw, PAD, y, cw, ch, r=14)
        pw, ph = pill(draw, PAD+CPAD, y+16, period, F['tag'],
                      bg=ACCENT, fg=WHITE)
        ty = y + 16 + ph + 12
        for item in items:
            txt(draw, PAD+CPAD, ty, item, F['body'], fill=TEXTC)
            ty += line_height
        y += ch + 14

    footer(draw, F, 12)
    return img

# ──────────────────────────────────────────────────────────
# PDF ASSEMBLY
# ──────────────────────────────────────────────────────────
def build_pdf(pages):
    out_dir = os.path.dirname(OUTPUT)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    c = rl_canvas.Canvas(OUTPUT, pagesize=(W, H))
    for img in pages:
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        c.drawImage(ImageReader(buf), 0, 0, W, H)
        c.showPage()
    c.save()
    print(f"  ✓  Saved → {OUTPUT}")

# ──────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────
def main():
    print("Loading fonts …")
    F = load_fonts()
    # Quick sanity check
    for k, v in F.items():
        print(f"  {k:6s}: {v}")

    builders = [
        p01_cover, p02_pain,  p03_intro, p04_compare,
        p05_step1, p06_step2, p07_step3, p08_step4,
        p09_step5, p10_step6, p11_magic, p12_action,
    ]
    pages = []
    for i, fn in enumerate(builders, 1):
        print(f"  Rendering page {i:02d}/{TOTAL} – {fn.__name__} …")
        pages.append(fn(F))

    print(f"Building PDF …")
    build_pdf(pages)
    print("Done!")

if __name__ == "__main__":
    main()
