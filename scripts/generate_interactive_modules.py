import os
import xml.etree.ElementTree as ET

# Directory check
os.makedirs('assets', exist_ok=True)

# ========================================================
# 1. GENERATE 5 MODULAR NAV BUTTONS (208 x 44)
# ========================================================
nav_buttons = [
    {
        'filename': 'assets/nav_btn_workstation.svg',
        'num': '01',
        'title': 'NEURAL WORKSTATION',
        'color': '#00F2FE'
    },
    {
        'filename': 'assets/nav_btn_engines.svg',
        'num': '02',
        'title': 'FLAGSHIP ENGINES',
        'color': '#39F59A'
    },
    {
        'filename': 'assets/nav_btn_ai.svg',
        'num': '03',
        'title': 'AI &amp; OPTICS LAB',
        'color': '#00F2FE'
    },
    {
        'filename': 'assets/nav_btn_arsenal.svg',
        'num': '04',
        'title': 'TECH ARSENAL',
        'color': '#39F59A'
    },
    {
        'filename': 'assets/nav_btn_telemetry.svg',
        'num': '05',
        'title': 'LIVE TELEMETRY',
        'color': '#00F2FE'
    }
]

for btn in nav_buttons:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 208 44" width="208" height="44">
  <defs>
    <linearGradient id="bg-{btn['num']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="60%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <filter id="glow-{btn['num']}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .font-mono {{ font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }}
    @keyframes pulseLed {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.45; transform: scale(0.85); }}
    }}
    .led {{ transform-origin: 18px 22px; animation: pulseLed 2s infinite ease-in-out; }}
    .btn-frame:hover {{ stroke: {btn['color']}; }}
  </style>
  <rect class="btn-frame" x="2" y="2" width="204" height="40" rx="8" fill="url(#bg-{btn['num']})" stroke="#22272E" stroke-width="1.2" />
  <circle cx="18" cy="22" r="4.5" fill="{btn['color']}" class="led" filter="url(#glow-{btn['num']})" />
  <text x="32" y="26" class="font-mono" font-size="11" font-weight="700" fill="#F0F6FC" letter-spacing="0.3">
    {btn['num']} // {btn['title']}
  </text>
  <path d="M 194 18 L 198 22 L 194 26" fill="none" stroke="{btn['color']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>'''
    with open(btn['filename'], 'w', encoding='utf-8') as f:
        f.write(svg)
    ET.fromstring(svg)
    print(f"Generated {btn['filename']}")


# ========================================================
# 2. GENERATE 6 STANDALONE INTERACTIVE PROJECT CARDS (536 x 284)
# ========================================================

# Common styles and defs for all cards
def card_head(engine_num, category, live_status, live_color):
    return f'''
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="60%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <filter id="card-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>
  <style>
    .font-mono {{ font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }}
    .font-sans {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    @keyframes pulseRing {{
      0% {{ r: 6; opacity: 1; }}
      100% {{ r: 22; opacity: 0; }}
    }}
    .ping {{ animation: pulseRing 2s cubic-bezier(0, 0.2, 0.8, 1) infinite; }}
  </style>
  <rect x="2" y="2" width="532" height="280" rx="14" fill="url(#card-bg)" stroke="#22272E" stroke-width="1.5" />
  <path d="M 2 16 Q 2 2 16 2 L 518 2 Q 532 2 532 16 L 532 44 L 2 44 Z" fill="#121212" />
  <line x1="2" y1="44" x2="534" y2="44" stroke="#22272E" stroke-width="1.2" />
  <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
  <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
  <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">{engine_num} // {category}</text>
  <rect x="414" y="13" width="104" height="20" rx="4" fill="#0A1813" stroke="{live_color}" stroke-width="1" />
  <text x="466" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="{live_color}">● {live_status}</text>
'''

# --- 1. Musica Audio Card ---
card_musica = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 01", "REAL-TIME MESH", "LIVE DEMO", "#39F59A")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">📡 Musica Audio Platform</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Zero-DB WebSockets &amp; WebRTC real-time audio core</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  <circle cx="70" cy="158" r="14" fill="#0A1218" stroke="#00F2FE" stroke-width="2" />
  <circle cx="70" cy="158" r="6" fill="#00F2FE" />
  <circle cx="70" cy="158" class="ping" fill="none" stroke="#00F2FE" stroke-width="1.5" />
  <text x="70" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#8B949E">PEER_A</text>

  <g transform="translate(100, 140)">
    <rect x="0" y="0" width="4" height="34" rx="2" fill="#00F2FE" />
    <rect x="10" y="0" width="4" height="24" rx="2" fill="#39F59A" />
    <rect x="20" y="0" width="4" height="36" rx="2" fill="#00F2FE" />
    <rect x="30" y="0" width="4" height="18" rx="2" fill="#39F59A" />
  </g>

  <rect x="175" y="132" width="138" height="52" rx="6" fill="#061219" stroke="#00F2FE" stroke-width="1.2" />
  <text x="244" y="153" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">WS SIGNALING</text>
  <text x="244" y="171" text-anchor="middle" class="font-mono" font-size="9.5" fill="#39F59A">&lt;18ms LATENCY</text>

  <g transform="translate(332, 140)">
    <rect x="0" y="0" width="4" height="36" rx="2" fill="#00F2FE" />
    <rect x="10" y="0" width="4" height="28" rx="2" fill="#39F59A" />
    <rect x="20" y="0" width="4" height="34" rx="2" fill="#00F2FE" />
    <rect x="30" y="0" width="4" height="20" rx="2" fill="#39F59A" />
  </g>

  <circle cx="448" cy="158" r="14" fill="#0A1813" stroke="#39F59A" stroke-width="2" />
  <circle cx="448" cy="158" r="6" fill="#39F59A" />
  <circle cx="448" cy="158" class="ping" fill="none" stroke="#39F59A" stroke-width="1.5" />
  <text x="448" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#8B949E">PEER_B</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="38" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>
    <rect x="84" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="118" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Node.js</text>
    <rect x="160" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="194" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">WebRTC</text>
    <rect x="236" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="274" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Socket.IO</text>
    <rect x="320" y="0" width="64" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="352" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Docker</text>
    <rect x="392" y="0" width="96" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="440" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Zero-DB Matrix</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#00F2FE">[ 🎧 Launch Musica Live App ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">musica-apvs.vercel.app</text>
</svg>'''

# --- 2. Ben 10 Game Card ---
card_game = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 02", "DETERMINISTIC P2P", "LIVE GAME", "#39F59A")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎮 Ben 10: Alien Battle Arena</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">2D fighting engine in Phaser 4 with PeerJS direct multiplayer</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  <text x="40" y="138" class="font-mono" font-size="10" font-weight="700" fill="#39F59A">PLAYER 1 // FOURARMS</text>
  <rect x="40" y="146" width="160" height="12" rx="3" fill="#161B22" />
  <rect x="40" y="146" width="134" height="12" rx="3" fill="#39F59A" />

  <circle cx="244" cy="154" r="18" fill="#051218" stroke="#00F2FE" stroke-width="1.8" />
  <text x="244" y="159" text-anchor="middle" class="font-mono" font-size="11" font-weight="800" fill="#00F2FE">VS</text>

  <text x="286" y="138" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">PLAYER 2 // HEATBLAST</text>
  <rect x="286" y="146" width="160" height="12" rx="3" fill="#161B22" />
  <rect x="286" y="146" width="115" height="12" rx="3" fill="#00F2FE" />

  <text x="40" y="184" class="font-mono" font-size="9.5" fill="#8B949E">Canvas: 60 FPS • P2P State Sync</text>
  <text x="496" y="184" text-anchor="end" class="font-mono" font-size="9.5" fill="#39F59A">Zero Server Lag • Web Audio</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="38" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Phaser 4</text>
    <rect x="84" y="0" width="74" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="121" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React 19</text>
    <rect x="166" y="0" width="78" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="205" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">TypeScript</text>
    <rect x="252" y="0" width="64" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="284" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PeerJS</text>
    <rect x="324" y="0" width="78" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="363" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Web Audio</text>
    <rect x="410" y="0" width="78" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="449" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">P2P Mesh</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#39F59A">[ 🎮 Play Battle Arena Live ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">game-rovenor.vercel.app</text>
</svg>'''

# --- 3. PlantSense AI Card ---
card_plantsense = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 03", "VISION AI &amp; VECTOR RAG", "FASTAPI LIVE", "#00F2FE")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🌱 PlantSense Botanical AI</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Gemini Vision AI multimodal pathology with ChromaDB vector RAG</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  
  <rect x="40" y="126" width="72" height="64" rx="6" fill="#051218" stroke="#00F2FE" stroke-width="1" stroke-dasharray="3 3" />
  <path d="M 76 136 C 60 148 60 168 76 178 C 92 168 92 148 76 136 Z" fill="none" stroke="#39F59A" stroke-width="2" />
  <line x1="76" y1="138" x2="76" y2="176" stroke="#39F59A" stroke-width="1.2" />
  <text x="76" y="186" text-anchor="middle" class="font-mono" font-size="8.5" font-weight="700" fill="#00F2FE">99.4% CONF</text>

  <!-- Neural Net Connectors -->
  <line x1="120" y1="158" x2="160" y2="158" stroke="#00F2FE" stroke-width="1.5" />
  <circle cx="170" cy="144" r="5" fill="#39F59A" />
  <circle cx="170" cy="158" r="5" fill="#00F2FE" />
  <circle cx="170" cy="172" r="5" fill="#39F59A" />
  <line x1="175" y1="144" x2="205" y2="154" stroke="#22272E" stroke-width="1" />
  <line x1="175" y1="158" x2="205" y2="158" stroke="#00F2FE" stroke-width="1" />
  <line x1="175" y1="172" x2="205" y2="162" stroke="#22272E" stroke-width="1" />
  <circle cx="210" cy="158" r="6" fill="#00F2FE" />

  <!-- ChromaDB RAG Box -->
  <rect x="236" y="128" width="160" height="60" rx="6" fill="#051218" stroke="#00F2FE" stroke-width="1.2" />
  <text x="316" y="148" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">ChromaDB RAG</text>
  <text x="316" y="164" text-anchor="middle" class="font-mono" font-size="9" fill="#8B949E">Cosine Distance Metric</text>
  <text x="316" y="178" text-anchor="middle" class="font-mono" font-size="9" fill="#39F59A">Instant Remedy Protocol</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="34" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Python</text>
    <rect x="76" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="110" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">FastAPI</text>
    <rect x="152" y="0" width="82" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="193" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Gemini AI</text>
    <rect x="242" y="0" width="80" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="282" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">ChromaDB</text>
    <rect x="330" y="0" width="74" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="367" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">RAG Net</text>
    <rect x="412" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="450" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision AI</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#00F2FE">[ 🌱 Launch Botanical AI Showcase ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">robinsonj.vercel.app</text>
</svg>'''

# --- 4. CAMX Digital Camera Lab Card ---
card_camx = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 04", "OPTICS &amp; COMPUTER VISION", "OPTICS LAB", "#00F2FE")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">📷 CAMX Digital Camera Lab</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Hands-free optics simulator with EV100, landmarks, voice commands</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  
  <!-- Aperture Iris Icon -->
  <circle cx="75" cy="154" r="24" fill="#061219" stroke="#00F2FE" stroke-width="1.2" />
  <polygon points="75,134 91,146 84,166 62,166 57,146" fill="none" stroke="#39F59A" stroke-width="1.8" />
  <circle cx="75" cy="154" r="8" fill="#00F2FE" opacity="0.3" />
  <text x="75" y="190" text-anchor="middle" class="font-mono" font-size="8.5" fill="#00F2FE">f/1.8 APERTURE</text>

  <text x="130" y="142" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">EV100 Exposure: +1.3 EV</text>
  <text x="130" y="157" class="font-mono" font-size="9.5" fill="#8B949E">Focal Length: 50mm Equivalent</text>
  <text x="130" y="172" class="font-mono" font-size="9.5" fill="#39F59A">Facial Landmarks: 468 Points 3D</text>
  <text x="130" y="187" class="font-mono" font-size="9.5" fill="#8B949E">Voice Control: Web Speech API</text>

  <rect x="390" y="130" width="102" height="56" rx="6" fill="#051218" stroke="#22272E" stroke-width="1" />
  <path d="M 400 168 Q 420 138 440 158 T 480 148" fill="none" stroke="#00F2FE" stroke-width="2" />
  <text x="441" y="178" text-anchor="middle" class="font-mono" font-size="8" fill="#39F59A">OPTICS CURVE</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="82" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="41" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>
    <rect x="90" y="0" width="70" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="125" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">WebRTC</text>
    <rect x="168" y="0" width="102" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="219" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Optics Physics</text>
    <rect x="278" y="0" width="78" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="317" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Voice API</text>
    <rect x="364" y="0" width="84" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="406" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision Lab</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#00F2FE">[ 📷 Explore CAMX Digital Optics ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">robinsonj.vercel.app</text>
</svg>'''

# --- 5. Havilah Studio Card ---
card_havilah = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 05", "CINEMATIC MULTIMEDIA", "LIVE DEMO", "#39F59A")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎥 Havilah Studio Portfolio</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Cinematic multimedia portfolio powered by Bun runtime &amp; GSAP</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  
  <line x1="40" y1="158" x2="496" y2="158" stroke="#22272E" stroke-width="1.5" />
  <path d="M 40 178 Q 150 138 268 158 T 496 142" fill="none" stroke="#00F2FE" stroke-width="2.5" />
  
  <circle cx="160" cy="151" r="7" fill="#00F2FE" />
  <circle cx="280" cy="159" r="7" fill="#39F59A" />
  <circle cx="400" cy="151" r="7" fill="#00F2FE" />

  <text x="40" y="188" class="font-mono" font-size="9.5" fill="#8B949E">GSAP Smooth Tweens • 60 FPS Canvas Coord</text>
  <text x="496" y="188" text-anchor="end" class="font-mono" font-size="9.5" fill="#39F59A">Bun High-Throughput Bundling</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="82" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="41" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>
    <rect x="90" y="0" width="56" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="118" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Bun</text>
    <rect x="154" y="0" width="66" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="187" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React</text>
    <rect x="228" y="0" width="60" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="258" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">GSAP</text>
    <rect x="296" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="330" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vercel</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#39F59A">[ 🎥 Launch Havilah Studio Live ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">havilah-alpha.vercel.app</text>
</svg>'''

# --- 6. HSE Media Suite Card ---
card_hse = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 536 284" width="100%" height="100%">
{card_head("ENGINE 06", "LIGHTHOUSE 99 PERFORMANCE", "LIVE DEMO", "#39F59A")}
  <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎬 HSE Media Production Suite</text>
  <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Next.js App Router multi-media engine with automated audits</text>

  <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
  
  <circle cx="80" cy="154" r="28" fill="#061219" stroke="#161B22" stroke-width="4" />
  <circle cx="80" cy="154" r="28" fill="none" stroke="#00F2FE" stroke-width="4" stroke-dasharray="160 20" stroke-linecap="round" />
  <text x="80" y="160" text-anchor="middle" class="font-mono" font-size="17" font-weight="900" fill="#FFFFFF">99</text>
  <text x="80" y="192" text-anchor="middle" class="font-mono" font-size="8" font-weight="700" fill="#39F59A">LIGHTHOUSE</text>

  <text x="136" y="142" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">Next.js App Router: Dynamic Edge Cache</text>
  <text x="136" y="157" class="font-mono" font-size="9" fill="#8B949E">SEO Score: 100 • Accessibility: 100 • Best Practices: 100</text>
  <text x="136" y="172" class="font-mono" font-size="9.5" font-weight="700" fill="#39F59A">Lighthouse Performance: 99 Verified</text>
  <text x="136" y="187" class="font-mono" font-size="9" fill="#8B949E">Tailwind CSS v4 • Continuous Automated CI Auditing</text>

  <!-- Chips -->
  <g transform="translate(24, 214)">
    <rect x="0" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="38" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Next.js</text>
    <rect x="84" y="0" width="76" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="122" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Tailwind</text>
    <rect x="168" y="0" width="56" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="196" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PHP</text>
    <rect x="232" y="0" width="68" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="266" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Vercel</text>
    <rect x="308" y="0" width="86" height="24" rx="4" fill="#0D1117" stroke="#21262D" stroke-width="1" />
    <text x="351" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Score 99</text>
  </g>

  <!-- Action URL -->
  <text x="24" y="262" class="font-mono" font-size="11" font-weight="700" fill="#39F59A">[ 🎬 Launch HSE Media Suite Live ↗ ]</text>
  <text x="512" y="262" text-anchor="end" class="font-mono" font-size="10.5" fill="#8B949E">hse-indol.vercel.app</text>
</svg>'''

cards = [
    ('assets/card_musica.svg', card_musica),
    ('assets/card_game.svg', card_game),
    ('assets/card_plantsense.svg', card_plantsense),
    ('assets/card_camx.svg', card_camx),
    ('assets/card_havilah.svg', card_havilah),
    ('assets/card_hse.svg', card_hse),
]

for filename, content in cards:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    ET.fromstring(content)
    print(f"Generated {filename}")

print("All modular interactive cards generated and XML-validated!")
