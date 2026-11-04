import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_img_path = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3\.user_uploaded\media_1793780391287_94b2dfd5.jpg'
base_dir = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3'

# 1. Load and upscale base reference image to 2x Retina (2048 x 1364)
base_1x = Image.open(base_img_path).convert('RGBA')
im = base_1x.resize((2048, 1364), Image.LANCZOS)
draw = ImageDraw.Draw(im)

# 2. Typography at 2x Retina
font_sig = ImageFont.truetype(r'C:\Windows\Fonts\segoesc.ttf', 24)
font_name = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 25)
font_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 14.5)
font_info = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 15.5)
font_about = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 16.5)
font_about_bold = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 16.5)
font_proj_title = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 18.5)
font_proj_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 14)
font_badge = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 11.5)
font_pill = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 15)

# Helper function to draw external link icon
def draw_ext_link(d, x, y, size=11, color='#39F59A'):
    d.line([(x, y + size), (x + size, y)], fill=color, width=2)
    d.line([(x + size - 5, y), (x + size, y)], fill=color, width=2)
    d.line([(x + size, y), (x + size, y + 5)], fill=color, width=2)

# ----------------------------------------------------
# 1. RETOUCH BANNER SIGNATURE WITH FEATHERED BLEND
# ----------------------------------------------------
patch = im.crop((1420, 160, 1500, 230)).resize((140, 75))
mask_sig = Image.new('L', (140, 75), 0)
mask_sig_draw = ImageDraw.Draw(mask_sig)
mask_sig_draw.rounded_rectangle([6, 6, 134, 69], radius=15, fill=255)
mask_sig = mask_sig.filter(ImageFilter.GaussianBlur(8))
im.paste(patch, (1518, 155), mask_sig)

# Write Robinson
draw.text((1520, 160), 'Robinson', font=font_sig, fill='#F4F7F6')
# Underline under Robinson
draw.line([(1526, 204), (1646, 204)], fill='#39F59A', width=2)

# ----------------------------------------------------
# 2. RETOUCH PILL 2: 'ECE Engineer' -> 'MCA Graduate'
# ----------------------------------------------------
draw.rectangle([648, 284, 784, 316], fill='#0B1517')
draw.text((652, 290), 'MCA Graduate', font=font_pill, fill='#F4F7F6')

# ----------------------------------------------------
# 3. RETOUCH LEFT PROFILE CARD & CYBER WOLF AVATAR
# ----------------------------------------------------
# Integrate user's Cyber Wolf Tech Avatar
wolf_path = r'd:\Robinson\PROJECTS\git-profile\Cyber Wolf AI Tech Avatar.png'
if os.path.exists(wolf_path):
    wolf = Image.open(wolf_path).convert('RGBA')
    cx, cy = 227, 497
    r = 130
    d = r * 2
    # Clear old avatar area
    draw.ellipse([cx - r - 4, cy - r - 4, cx + r + 4, cy + r + 4], fill='#071214')
    # Paste circular wolf avatar
    wolf_resized = wolf.resize((d, d), Image.LANCZOS)
    wolf_mask = Image.new('L', (d, d), 0)
    ImageDraw.Draw(wolf_mask).ellipse([0, 0, d, d], fill=255)
    im.paste(wolf_resized, (cx - r, cy - r), wolf_mask)
    # Double neon rings
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline='#39F59A', width=3)
    draw.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], outline='#20D9D2', width=1)

# Clear text area x: 40 to 420, y: 690 to 976
draw.rectangle([40, 690, 420, 976], fill='#0B1517')

# Name
draw.text((50, 696), 'Robinson J.', font=font_name, fill='#F4F7F6')

# Headline
draw.text((50, 732), 'Full-Stack Engineer | Real-Time Systems', font=font_sub, fill='#9BAEAA')
draw.text((50, 756), 'Software Development | WebRTC | AI/ML', font=font_sub, fill='#9BAEAA')

# 1. Location
draw.ellipse([50, 802, 66, 818], fill='#39F59A')
draw.ellipse([54, 806, 62, 814], fill='#0B1517')
draw.text((76, 802), 'Bengaluru, Karnataka, India', font=font_info, fill='#F4F7F6')

# 2. Email
draw.rectangle([50, 842, 66, 854], outline='#39F59A', width=2)
draw.line([(50, 842), (58, 848), (66, 842)], fill='#39F59A', width=2)
draw.text((76, 840), 'robinson30122000@gmail.com', font=font_info, fill='#F4F7F6')

# 3. Portfolio
draw.ellipse([50, 880, 62, 892], outline='#20D9D2', width=2)
draw.ellipse([56, 886, 68, 898], outline='#20D9D2', width=2)
draw.text((76, 880), 'https://robinsonj.vercel.app', font=font_info, fill='#20D9D2')

# 4. LinkedIn
draw.rounded_rectangle([50, 920, 66, 936], radius=4, fill='#20D9D2')
draw.text((54, 920), 'in', font=font_badge, fill='#0B1517')
draw.text((76, 920), 'linkedin.com/in/robinson-mj', font=font_info, fill='#20D9D2')

# ----------------------------------------------------
# 4. RETOUCH ABOUT ME CARD
# ----------------------------------------------------
draw.rectangle([456, 384, 1424, 612], fill='#0B1517')

draw.text((470, 390), "I'm a Computer Science postgraduate (MCA '25) who turns complex", font=font_about, fill='#F4F7F6')
draw.text((470, 416), 'challenges into data-driven, real-time, and scalable solutions across', font=font_about, fill='#F4F7F6')
draw.text((470, 442), 'software development, real-time communications, and intelligent AI systems.', font=font_about, fill='#F4F7F6')

# Bullet 1
draw.ellipse([470, 482, 490, 502], fill='#39F59A')
draw.text((474, 482), '✓', font=font_about_bold, fill='#0B1517')
draw.text((500, 482), 'Building:', font=font_about_bold, fill='#F4F7F6')
draw.text((584, 482), 'Real-time WebRTC platforms, interactive 2D games, AI diagnostic suites', font=font_about, fill='#F4F7F6')

# Bullet 2
draw.ellipse([470, 520, 490, 540], fill='#39F59A')
draw.text((474, 520), '✓', font=font_about_bold, fill='#0B1517')
draw.text((500, 520), 'Exploring:', font=font_about_bold, fill='#F4F7F6')
draw.text((596, 520), 'Vector RAG retrieval (ChromaDB), distributed signaling, zero-DB stores', font=font_about, fill='#F4F7F6')

# Bullet 3
draw.ellipse([470, 558, 490, 578], fill='#39F59A')
draw.text((474, 558), '✓', font=font_about_bold, fill='#0B1517')
draw.text((500, 558), 'Goal:', font=font_about_bold, fill='#F4F7F6')
draw.text((552, 558), 'To grow as a versatile engineer architecting resilient, scalable solutions', font=font_about, fill='#F4F7F6')

# ----------------------------------------------------
# 5. RETOUCH FEATURED PROJECTS
# ----------------------------------------------------
draw.rectangle([456, 676, 1424, 1120], fill='#0B1517')

cards_data = [
    {
        'col': 0, 'row': 0,
        'title': 'Musica Platform',
        'sub1': 'Zero-DB WebSockets & WebRTC',
        'sub2': 'audio streaming platform.',
        'badges': ['TypeScript', 'Node.js', 'WebRTC', 'Docker'],
        'thumb': f'{base_dir}/thumb_musica_final.png'
    },
    {
        'col': 1, 'row': 0,
        'title': 'Ben 10: Battle Arena',
        'sub1': '2D fighting arena in Phaser 4',
        'sub2': 'with PeerJS P2P multiplayer.',
        'badges': ['Phaser 4', 'React 19', 'PeerJS', 'Audio'],
        'thumb': f'{base_dir}/thumb_game_final.png'
    },
    {
        'col': 0, 'row': 1,
        'title': 'PlantSense AI',
        'sub1': 'Gemini Vision AI diagnosis with',
        'sub2': 'ChromaDB vector RAG pipeline.',
        'badges': ['Python', 'FastAPI', 'Gemini', 'ChromaDB'],
        'thumb': f'{base_dir}/thumb_plantsense_final.png'
    },
    {
        'col': 1, 'row': 1,
        'title': 'Digital Camera Lab',
        'sub1': 'Hands-free optics simulator with',
        'sub2': 'EV100, landmarks & voice.',
        'badges': ['TypeScript', 'WebRTC', 'Optics', 'Voice'],
        'thumb': f'{base_dir}/thumb_camx_final.png'
    },
    {
        'col': 0, 'row': 2,
        'title': 'Havilah Studio',
        'sub1': 'Cinematic multimedia portfolio',
        'sub2': 'with Bun runtime & GSAP.',
        'badges': ['TypeScript', 'Bun', 'React', 'GSAP'],
        'thumb': f'{base_dir}/thumb_havilah_final.png'
    },
    {
        'col': 1, 'row': 2,
        'title': 'HSE Media Suite',
        'sub1': 'Next.js App Router multi-media',
        'sub2': 'engine with automated audits.',
        'badges': ['Next.js', 'Tailwind', 'PHP', 'Vercel'],
        'thumb': f'{base_dir}/thumb_hse_final.png'
    }
]

for c in cards_data:
    cx1 = 460 if c['col'] == 0 else 948
    cx2 = 936 if c['col'] == 0 else 1424
    cy1 = 680 + c['row'] * 136
    cy2 = cy1 + 128
    
    # Card container
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=12, fill='#0B1517', outline='#174D43', width=2)
    
    # Rounded thumbnail on left (192x116)
    th_x, th_y = cx1 + 6, cy1 + 6
    th_img = Image.open(c['thumb']).resize((192, 116), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (192, 116), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 192, 116], radius=10, fill=255)
    im.paste(th_img, (th_x, th_y), mask)
    draw.rounded_rectangle([th_x, th_y, th_x + 192, th_y + 116], radius=10, outline='#174D43', width=2)
    
    # Text info on right
    tx = cx1 + 208
    # Title
    draw.text((tx, cy1 + 10), c['title'], font=font_proj_title, fill='#39F59A')
    title_w = draw.textlength(c['title'], font=font_proj_title)
    draw_ext_link(draw, tx + int(title_w) + 8, cy1 + 12, size=11, color='#39F59A')
    
    # Subtitles
    draw.text((tx, cy1 + 38), c['sub1'], font=font_proj_sub, fill='#9BAEAA')
    draw.text((tx, cy1 + 58), c['sub2'], font=font_proj_sub, fill='#9BAEAA')
    
    # Badges
    bx = tx
    by = cy1 + 88
    for b in c['badges']:
        bw = int(draw.textlength(b, font=font_badge) + 14)
        draw.rounded_rectangle([bx, by, bx + bw, by + 24], radius=5, fill='#071E18', outline='#174D43', width=1)
        draw.text((bx + 7, by + 4), b, font=font_badge, fill='#39F59A')
        bx += bw + 5

# Save Retina master image
out_master = 'assets/dashboard.png'
im.save(out_master, quality=98)
print('Retina Master dashboard with Cyber Wolf Avatar generated at:', out_master)
