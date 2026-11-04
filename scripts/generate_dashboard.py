import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base_img_path = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3\.user_uploaded\media_1793780391287_94b2dfd5.jpg'
base_dir = r'C:\Users\ADMIN\.gemini\antigravity\brain\ae268e06-c5bf-48f0-b659-dc19ec359bf3'
im = Image.open(base_img_path).convert('RGBA')

# Fonts
font_sig = ImageFont.truetype(r'C:\Windows\Fonts\segoesc.ttf', 20)
font_name = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 13)
font_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 8)
font_info = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 8)
font_about = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 9)
font_about_bold = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 9)
font_proj_title = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 10)
font_proj_sub = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 7)
font_badge = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 6)

draw = ImageDraw.Draw(im)

# 1. Update Signature in Banner:
# Sample background to seamlessly patch Surjya
bg_sig = im.crop((700, 45, 850, 65)).resize((150, 50))
im.paste(bg_sig, (700, 70))
# Re-draw Robinson ♡ in cursive
draw.text((720, 80), 'Robinson ♡', font=font_sig, fill='#F4F7F6')

# 2. Update Profile Card Text:
# Clear Surjya Sarathi Rout area
draw.rectangle([25, 344, 200, 362], fill='#0B1517')
draw.text((28, 346), 'Robinson J.', font=font_name, fill='#F4F7F6')

# Clear ECE Engineer subtitle
draw.rectangle([25, 364, 202, 400], fill='#0B1517')
draw.text((28, 366), 'Full-Stack Engineer | Real-Time Systems', font=font_sub, fill='#9BAEAA')
draw.text((28, 378), 'Software Development | WebRTC | AI/ML', font=font_sub, fill='#9BAEAA')

# Clear Location, Email, URL, LinkedIn
draw.rectangle([45, 410, 195, 428], fill='#0B1517')
draw.text((48, 414), 'Bengaluru, Karnataka, India', font=font_info, fill='#F4F7F6')

draw.rectangle([45, 432, 195, 448], fill='#0B1517')
draw.text((48, 436), 'robinson30122000@gmail.com', font=font_info, fill='#F4F7F6')

draw.rectangle([45, 452, 195, 468], fill='#0B1517')
draw.text((48, 456), 'https://robinsonj.vercel.app', font=font_info, fill='#20D9D2')

draw.rectangle([45, 472, 195, 490], fill='#0B1517')
draw.text((48, 476), 'linkedin.com/in/robinson-mj', font=font_info, fill='#20D9D2')

# 3. Update About Me Card:
draw.rectangle([235, 195, 708, 305], fill='#0B1517')
draw.text((236, 198), "I'm a Computer Science postgraduate (MCA '25) who turns complex", font=font_about, fill='#F4F7F6')
draw.text((236, 212), 'challenges into data-driven, real-time, and scalable solutions across', font=font_about, fill='#F4F7F6')
draw.text((236, 226), 'software development, real-time communications, and AI systems.', font=font_about, fill='#F4F7F6')

# Checkmarks & Bullets
draw.ellipse([236, 246, 246, 256], fill='#39F59A')
draw.text((238, 246), '✓', font=font_about_bold, fill='#0B1517')
draw.text((252, 246), 'Building: Real-time WebRTC platforms, interactive 2D games, AI diagnostic suites', font=font_about, fill='#F4F7F6')

draw.ellipse([236, 264, 246, 274], fill='#39F59A')
draw.text((238, 264), '✓', font=font_about_bold, fill='#0B1517')
draw.text((252, 264), 'Exploring: Vector RAG retrieval (ChromaDB), distributed signaling, zero-DB stores', font=font_about, fill='#F4F7F6')

draw.ellipse([236, 282, 246, 292], fill='#39F59A')
draw.text((238, 282), '✓', font=font_about_bold, fill='#0B1517')
draw.text((252, 282), 'Goal: To grow as a versatile engineer architecting resilient, scalable solutions', font=font_about, fill='#F4F7F6')

# 4. Update Featured Projects (6 projects)
projects = [
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

for p in projects:
    col = p['col']
    row = p['row']
    tx = 232 if col == 0 else 476
    ty = 342 + row * 68
    
    # 1. Paste rounded thumbnail (98x56)
    th_img = Image.open(p['thumb']).resize((98, 56), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (98, 56), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, 98, 56], radius=5, fill=255)
    im.paste(th_img, (tx, ty), mask)
    draw.rounded_rectangle([tx, ty, tx + 98, ty + 56], radius=5, outline='#174D43', width=1)
    
    # 2. Text info area
    info_x = tx + 104
    draw.rectangle([info_x, ty - 2, info_x + 130, ty + 58], fill='#0B1517')
    # Title
    draw.text((info_x, ty), p['title'], font=font_proj_title, fill='#39F59A')
    # Subtitle
    draw.text((info_x, ty + 14), p['sub1'], font=font_proj_sub, fill='#9BAEAA')
    draw.text((info_x, ty + 23), p['sub2'], font=font_proj_sub, fill='#9BAEAA')
    # Tag pills
    bx = info_x
    by = ty + 38
    for badge in p['badges']:
        bw = len(badge) * 4.2 + 8
        draw.rounded_rectangle([bx, by, bx + bw, by + 13], radius=3, fill='#071E18', outline='#174D43', width=1)
        draw.text((bx + 4, by + 2), badge, font=font_badge, fill='#39F59A')
        bx += bw + 3

# 5. Update Navigation Pill 2 from 'ECE Engineer' to 'MCA Postgraduate'
draw.rectangle([390, 142, 475, 162], fill='#0B1517')
font_pill = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 8)
draw.text((395, 147), '🎓 MCA Graduate', font=font_pill, fill='#39F59A')

out_path = f'{base_dir}/dashboard_master_v1.png'
im.save(out_path, quality=95)
print('Master dashboard generated at:', out_path)

