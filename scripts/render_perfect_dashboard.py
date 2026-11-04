import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_img_path = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3\.user_uploaded\media_1793780391287_94b2dfd5.jpg'
base_dir = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3'
im = Image.open(base_img_path).convert('RGBA')

# Fonts
font_sig = ImageFont.truetype(r'C:\Windows\Fonts\segoesc.ttf', 13)
font_name = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 12.5)
font_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 7.5)
font_info = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 8)
font_about = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 8.5)
font_about_bold = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 8.5)
font_proj_title = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 9.5)
font_proj_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 7.2)
font_badge = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 6.2)
font_pill = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 7.8)

draw = ImageDraw.Draw(im)

# ----------------------------------------------------
# 1. RETOUCH BANNER SIGNATURE
# ----------------------------------------------------
# Surjya is strictly in x: 762 to 828, y: 74 to 118
# Fill with dark forest night tone
dark_forest = (7, 21, 24, 255)
draw.rectangle([762, 74, 828, 118], fill=dark_forest)
# Write Robinson
draw.text((760, 80), 'Robinson', font=font_sig, fill='#F4F7F6')
# Underline under Robinson
draw.line([(764, 102), (824, 102)], fill='#39F59A', width=1)

# ----------------------------------------------------
# 2. RETOUCH PILL 2: 'ECE Engineer' -> 'MCA Graduate'
# ----------------------------------------------------
# Pill 2 text is at x: 324 to 392, y: 142 to 158
draw.rectangle([324, 142, 392, 158], fill='#0B1517')
draw.text((326, 145), 'MCA Graduate', font=font_pill, fill='#F4F7F6')

# ----------------------------------------------------
# 3. RETOUCH LEFT PROFILE CARD
# ----------------------------------------------------
# Clear area from y: 345 to 488, x: 20 to 210
draw.rectangle([20, 345, 210, 488], fill='#0B1517')

# Name
draw.text((25, 348), 'Robinson J.', font=font_name, fill='#F4F7F6')

# Headline
draw.text((25, 366), 'Full-Stack Engineer | Real-Time Systems', font=font_sub, fill='#9BAEAA')
draw.text((25, 378), 'Software Development | WebRTC | AI/ML', font=font_sub, fill='#9BAEAA')

# 1. Location
draw.ellipse([25, 401, 33, 409], fill='#39F59A')
draw.ellipse([27, 403, 31, 407], fill='#0B1517')
draw.text((38, 401), 'Bengaluru, Karnataka, India', font=font_info, fill='#F4F7F6')

# 2. Email
draw.rectangle([25, 421, 33, 427], outline='#39F59A', width=1)
draw.line([(25, 421), (29, 424), (33, 421)], fill='#39F59A', width=1)
draw.text((38, 420), 'robinson30122000@gmail.com', font=font_info, fill='#F4F7F6')

# 3. Portfolio
draw.ellipse([25, 440, 31, 446], outline='#20D9D2', width=1)
draw.ellipse([28, 443, 34, 449], outline='#20D9D2', width=1)
draw.text((38, 440), 'https://robinsonj.vercel.app', font=font_info, fill='#20D9D2')

# 4. LinkedIn
draw.rounded_rectangle([25, 460, 33, 468], radius=2, fill='#20D9D2')
draw.text((27, 460), 'in', font=font_badge, fill='#0B1517')
draw.text((38, 460), 'linkedin.com/in/robinson-mj', font=font_info, fill='#20D9D2')

# ----------------------------------------------------
# 4. RETOUCH ABOUT ME CARD
# ----------------------------------------------------
# Clear area x: 228 to 712, y: 192 to 306
draw.rectangle([228, 192, 712, 306], fill='#0B1517')

draw.text((235, 195), "I'm a Computer Science postgraduate (MCA '25) who turns complex", font=font_about, fill='#F4F7F6')
draw.text((235, 208), 'challenges into data-driven, real-time, and scalable solutions across', font=font_about, fill='#F4F7F6')
draw.text((235, 221), 'software development, real-time communications, and intelligent AI systems.', font=font_about, fill='#F4F7F6')

# Bullet 1
draw.ellipse([235, 241, 245, 251], fill='#39F59A')
draw.text((237, 241), '✓', font=font_about_bold, fill='#0B1517')
draw.text((250, 241), 'Building:', font=font_about_bold, fill='#F4F7F6')
draw.text((292, 241), 'Real-time WebRTC platforms, interactive 2D games, AI diagnostic suites', font=font_about, fill='#F4F7F6')

# Bullet 2
draw.ellipse([235, 260, 245, 270], fill='#39F59A')
draw.text((237, 260), '✓', font=font_about_bold, fill='#0B1517')
draw.text((250, 260), 'Exploring:', font=font_about_bold, fill='#F4F7F6')
draw.text((298, 260), 'Vector RAG retrieval (ChromaDB), distributed signaling, zero-DB stores', font=font_about, fill='#F4F7F6')

# Bullet 3
draw.ellipse([235, 279, 245, 289], fill='#39F59A')
draw.text((237, 279), '✓', font=font_about_bold, fill='#0B1517')
draw.text((250, 279), 'Goal:', font=font_about_bold, fill='#F4F7F6')
draw.text((276, 279), 'To grow as a versatile engineer architecting resilient, scalable solutions', font=font_about, fill='#F4F7F6')

# ----------------------------------------------------
# 5. RETOUCH FEATURED PROJECTS (Clear entire interior)
# ----------------------------------------------------
# Clear area x: 228 to 712, y: 338 to 560
draw.rectangle([228, 338, 712, 560], fill='#0B1517')

cards_data = [
    {
        'col': 0, 'row': 0,
        'title': 'Musica Platform ↗',
        'sub1': 'Zero-DB WebSockets & WebRTC',
        'sub2': 'audio streaming platform.',
        'badges': ['TypeScript', 'Node.js', 'WebRTC', 'Docker'],
        'thumb': f'{base_dir}/thumb_musica_final.png'
    },
    {
        'col': 1, 'row': 0,
        'title': 'Ben 10: Battle Arena ↗',
        'sub1': '2D fighting arena in Phaser 4',
        'sub2': 'with PeerJS P2P multiplayer.',
        'badges': ['Phaser 4', 'React 19', 'PeerJS', 'Audio'],
        'thumb': f'{base_dir}/thumb_game_final.png'
    },
    {
        'col': 0, 'row': 1,
        'title': 'PlantSense AI ↗',
        'sub1': 'Gemini Vision AI diagnosis with',
        'sub2': 'ChromaDB vector RAG pipeline.',
        'badges': ['Python', 'FastAPI', 'Gemini', 'ChromaDB'],
        'thumb': f'{base_dir}/thumb_plantsense_final.png'
    },
    {
        'col': 1, 'row': 1,
        'title': 'Digital Camera Lab ↗',
        'sub1': 'Hands-free optics simulator with',
        'sub2': 'EV100, landmarks & voice.',
        'badges': ['TypeScript', 'WebRTC', 'Optics', 'Voice'],
        'thumb': f'{base_dir}/thumb_camx_final.png'
    },
    {
        'col': 0, 'row': 2,
        'title': 'Havilah Studio ↗',
        'sub1': 'Cinematic multimedia portfolio',
        'sub2': 'with Bun runtime & GSAP.',
        'badges': ['TypeScript', 'Bun', 'React', 'GSAP'],
        'thumb': f'{base_dir}/thumb_havilah_final.png'
    },
    {
        'col': 1, 'row': 2,
        'title': 'HSE Media Suite ↗',
        'sub1': 'Next.js App Router multi-media',
        'sub2': 'engine with automated audits.',
        'badges': ['Next.js', 'Tailwind', 'PHP', 'Vercel'],
        'thumb': f'{base_dir}/thumb_hse_final.png'
    }
]

for c in cards_data:
    cx1 = 230 if c['col'] == 0 else 474
    cx2 = 468 if c['col'] == 0 else 712
    cy1 = 340 + c['row'] * 68
    cy2 = cy1 + 64
    
    # Card container
    draw.rounded_rectangle([cx1, cy1, cx2, cy2], radius=6, fill='#0B1517', outline='#174D43', width=1)
    
    # Rounded thumbnail on left (96x58)
    th_x, th_y = cx1 + 3, cy1 + 3
    th_img = Image.open(c['thumb']).resize((96, 58), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (96, 58), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 96, 58], radius=5, fill=255)
    im.paste(th_img, (th_x, th_y), mask)
    draw.rounded_rectangle([th_x, th_y, th_x + 96, th_y + 58], radius=5, outline='#174D43', width=1)
    
    # Text info on right
    tx = cx1 + 104
    # Title
    draw.text((tx, cy1 + 5), c['title'], font=font_proj_title, fill='#39F59A')
    # Subtitles
    draw.text((tx, cy1 + 19), c['sub1'], font=font_proj_sub, fill='#9BAEAA')
    draw.text((tx, cy1 + 29), c['sub2'], font=font_proj_sub, fill='#9BAEAA')
    # Badges
    bx = tx
    by = cy1 + 43
    for b in c['badges']:
        bw = int(len(b) * 4.3 + 8)
        draw.rounded_rectangle([bx, by, bx + bw, by + 13], radius=3, fill='#071E18', outline='#174D43', width=1)
        draw.text((bx + 4, by + 2), b, font=font_badge, fill='#39F59A')
        bx += bw + 3

# Save master image
out_master = 'assets/dashboard.png'
im.save(out_master, quality=98)
print('Master dashboard generated successfully at:', out_master)
