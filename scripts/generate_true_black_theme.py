import os
import base64
import xml.etree.ElementTree as ET

# Load Cyber Wolf Avatar Base64
wolf_path = 'assets/profile/wolf_popup_thumb.png'
with open(wolf_path, 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

# ========================================================
# 1. assets/welcome_popup.svg (TRUE PITCH BLACK THEME)
# ========================================================
def build_welcome_popup():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%">
  <defs>
    <!-- True Pitch Black Background Gradients -->
    <radialGradient id="vignette-bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#080808" />
      <stop offset="50%" stop-color="#030303" />
      <stop offset="100%" stop-color="#000000" />
    </radialGradient>

    <linearGradient id="modal-glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" stop-opacity="0.98" />
      <stop offset="50%" stop-color="#070707" stop-opacity="0.99" />
      <stop offset="100%" stop-color="#020202" stop-opacity="1" />
    </linearGradient>

    <!-- Neon Accents -->
    <linearGradient id="neon-cyan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>

    <linearGradient id="btn-primary-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#00D287" />
    </linearGradient>

    <linearGradient id="term-box-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050505" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>

    <!-- Glow Filters -->
    <filter id="neon-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="subtle-glow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <clipPath id="avatar-clip">
      <circle cx="240" cy="310" r="95" />
    </clipPath>

    <!-- Pitch Black Grid Pattern -->
    <pattern id="cyber-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#161A1D" stroke-width="0.8" opacity="0.6" />
      <circle cx="40" cy="40" r="1" fill="#00F2FE" opacity="0.35" />
    </pattern>
  </defs>

  <style>
    @keyframes laserScan {{
      0% {{ transform: translateY(0px); opacity: 0; }}
      15% {{ opacity: 0.9; }}
      85% {{ opacity: 0.9; }}
      100% {{ transform: translateY(680px); opacity: 0; }}
    }}

    @keyframes spinClockwise {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}

    @keyframes spinCounterClockwise {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(-360deg); }}
    }}

    @keyframes sonarWave {{
      0% {{ r: 98px; opacity: 0.9; stroke-width: 2px; }}
      50% {{ opacity: 0.5; }}
      100% {{ r: 154px; opacity: 0; stroke-width: 0.5px; }}
    }}

    @keyframes blinkCursor {{
      0%, 100% {{ opacity: 1; }}
      50% {{ opacity: 0; }}
    }}

    @keyframes eqBar {{
      0%, 100% {{ height: 4px; y: 446px; }}
      50% {{ height: 22px; y: 428px; }}
    }}

    .font-mono {{
      font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace;
    }}
    .font-sans {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    }}

    .scan-beam {{
      animation: laserScan 4.5s ease-in-out infinite;
    }}

    .reticle-cw {{
      transform-origin: 240px 310px;
      animation: spinClockwise 22s linear infinite;
    }}

    .reticle-ccw {{
      transform-origin: 240px 310px;
      animation: spinCounterClockwise 14s linear infinite;
    }}

    .sonar-ping {{
      transform-origin: 240px 310px;
      animation: sonarWave 2.8s ease-out infinite;
    }}

    .cursor {{ animation: blinkCursor 0.8s infinite; }}

    .btn-interactive {{
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .btn-interactive:hover {{
      filter: url(#neon-glow);
    }}

    .eq-1 {{ animation: eqBar 0.9s ease-in-out infinite 0.1s; }}
    .eq-2 {{ animation: eqBar 0.7s ease-in-out infinite 0.25s; }}
    .eq-3 {{ animation: eqBar 1.1s ease-in-out infinite 0.05s; }}
    .eq-4 {{ animation: eqBar 0.6s ease-in-out infinite 0.4s; }}
    .eq-5 {{ animation: eqBar 0.8s ease-in-out infinite 0.15s; }}
    .eq-6 {{ animation: eqBar 1.0s ease-in-out infinite 0.3s; }}
    .eq-7 {{ animation: eqBar 0.75s ease-in-out infinite 0.5s; }}
    .eq-8 {{ animation: eqBar 0.95s ease-in-out infinite 0.2s; }}
    .eq-9 {{ animation: eqBar 0.65s ease-in-out infinite 0.35s; }}
    .eq-10 {{ animation: eqBar 0.85s ease-in-out infinite 0.1s; }}
  </style>

  <!-- ======================================================== -->
  <!-- 1. PURE BLACK BACKDROP OVERLAY & GRID                    -->
  <!-- ======================================================== -->
  <rect x="0" y="0" width="1200" height="680" fill="url(#vignette-bg)" />
  <rect x="0" y="0" width="1200" height="680" fill="url(#cyber-grid)" />
  <rect x="2" y="2" width="1196" height="676" rx="14" fill="none" stroke="#22272E" stroke-width="1.5" />

  <!-- Laser Scan Line -->
  <g class="scan-beam">
    <line x1="0" y1="0" x2="1200" y2="0" stroke="url(#neon-cyan-grad)" stroke-width="2" opacity="0.8" filter="url(#neon-glow)" />
    <polygon points="0,0 1200,0 1200,-25 0,-25" fill="url(#neon-cyan-grad)" opacity="0.08" />
  </g>

  <!-- Telemetry Header Text -->
  <text x="32" y="24" class="font-mono" font-size="10" fill="#484F58">SYS_LOC: 12.9716° N, 77.5946° E [BENGALURU, INDIA]</text>
  <text x="1168" y="24" text-anchor="end" class="font-mono" font-size="10" fill="#484F58">PACKHUNTER-OS v5.1 // PURE BLACK OLED THEME</text>

  <!-- ======================================================== -->
  <!-- 2. THE MODAL POP-UP WINDOW                               -->
  <!-- ======================================================== -->
  <g id="modal-window">
    <!-- Glow Halo -->
    <rect x="76" y="36" width="1048" height="608" rx="20" fill="none" stroke="#00F2FE" stroke-width="2.5" opacity="0.22" filter="url(#neon-glow)" />
    
    <!-- Main Modal Pitch Black Box -->
    <rect x="80" y="40" width="1040" height="600" rx="18" fill="url(#modal-glass)" stroke="#2D333B" stroke-width="1.8" />

    <!-- Sharp Inner Cyber Line -->
    <rect x="84" y="44" width="1032" height="592" rx="14" fill="none" stroke="#00F2FE" stroke-width="0.8" opacity="0.35" />

    <!-- Corner Brackets -->
    <path d="M 80 75 L 80 40 L 115 40" fill="none" stroke="#00F2FE" stroke-width="3" />
    <circle cx="92" cy="52" r="2.5" fill="#00F2FE" />

    <path d="M 1085 40 L 1120 40 L 1120 75" fill="none" stroke="#00F2FE" stroke-width="3" />
    <circle cx="1108" cy="52" r="2.5" fill="#00F2FE" />

    <path d="M 80 605 L 80 640 L 115 640" fill="none" stroke="#39F59A" stroke-width="3" />
    <circle cx="92" cy="628" r="2.5" fill="#39F59A" />

    <path d="M 1085 640 L 1120 640 L 1120 605" fill="none" stroke="#39F59A" stroke-width="3" />
    <circle cx="1108" cy="628" r="2.5" fill="#39F59A" />

    <!-- ======================================================== -->
    <!-- 3. WINDOW HEADER BAR                                     -->
    <!-- ======================================================== -->
    <path d="M 80 58 Q 80 40 98 40 L 1102 40 Q 1120 40 1120 58 L 1120 84 L 80 84 Z" fill="#121212" />
    <line x1="80" y1="84" x2="1120" y2="84" stroke="#2D333B" stroke-width="1.5" />

    <!-- Traffic Lights -->
    <circle cx="110" cy="62" r="6.5" fill="#FF5F56" />
    <circle cx="132" cy="62" r="6.5" fill="#FFBD2E" />
    <circle cx="154" cy="62" r="6.5" fill="#27C93F" />

    <!-- Window Title -->
    <text x="600" y="66" text-anchor="middle" class="font-mono" font-size="12" font-weight="700" fill="#8B949E" letter-spacing="1">
      ⚡ PACKHUNTER-OS v5.1 // NEURAL WORKSTATION // AUTHENTICATED
    </text>

    <!-- Header Right Buttons -->
    <rect x="910" y="52" width="86" height="20" rx="4" fill="#0A0A0A" stroke="#2D333B" stroke-width="1" />
    <text x="953" y="66" text-anchor="middle" class="font-mono" font-size="9" font-weight="700" fill="#00F2FE">⛶ FULLSCREEN</text>

    <rect x="1004" y="52" width="98" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <circle cx="1016" cy="62" r="3.5" fill="#39F59A" />
    <text x="1058" y="66" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">200 OK LIVE</text>

    <!-- ======================================================== -->
    <!-- 4. LEFT PANEL: CYBER WOLF AVATAR & RADAR                 -->
    <!-- ======================================================== -->
    <circle cx="240" cy="310" r="140" fill="#00F2FE" opacity="0.08" filter="url(#neon-glow)" />

    <circle cx="240" cy="310" class="sonar-ping" fill="none" stroke="#00F2FE" />

    <g class="reticle-cw">
      <circle cx="240" cy="310" r="128" fill="none" stroke="#22272E" stroke-dasharray="8 12 18 10" stroke-width="1.8" />
      <circle cx="240" cy="310" r="134" fill="none" stroke="#00F2FE" stroke-dasharray="4 28" stroke-width="2.5" opacity="0.9" />
    </g>

    <g class="reticle-ccw">
      <circle cx="240" cy="310" r="112" fill="none" stroke="#39F59A" stroke-dasharray="16 22 8 22" stroke-width="1.5" opacity="0.8" />
    </g>

    <!-- Crosshairs -->
    <line x1="240" y1="160" x2="240" y2="178" stroke="#00F2FE" stroke-width="2" />
    <line x1="240" y1="442" x2="240" y2="460" stroke="#00F2FE" stroke-width="2" />
    <line x1="90" y1="310" x2="108" y2="310" stroke="#39F59A" stroke-width="2" />
    <line x1="372" y1="310" x2="390" y2="310" stroke="#39F59A" stroke-width="2" />

    <!-- Avatar Image -->
    <image href="data:image/png;base64,{avatar_b64}" x="145" y="215" width="190" height="190" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />

    <!-- Dual Glowing Rings (Cyan + Emerald) -->
    <circle cx="240" cy="310" r="95" fill="none" stroke="#00F2FE" stroke-width="3" filter="url(#subtle-glow)" />
    <circle cx="240" cy="310" r="99" fill="none" stroke="#39F59A" stroke-width="1.5" opacity="0.9" />

    <!-- Avatar Badge -->
    <rect x="156" y="416" width="168" height="22" rx="11" fill="#0A0A0A" stroke="#2D333B" stroke-width="1.2" />
    <circle cx="170" cy="427" r="3.5" fill="#00F2FE" />
    <text x="244" y="431" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE" letter-spacing="0.5">
      CYBER WOLF AI CORE
    </text>

    <!-- Audio Equalizer -->
    <g transform="translate(176, 5)">
      <rect class="eq-1" x="0" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-2" x="12" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-3" x="24" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-4" x="36" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-5" x="48" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-6" x="60" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-7" x="72" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-8" x="84" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-9" x="96" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-10" x="108" y="446" width="6" height="4" rx="2" fill="#39F59A" />
    </g>

    <text x="240" y="482" text-anchor="middle" class="font-mono" font-size="9.5" fill="#8B949E">
      Musica Zero-DB • 96kHz / 24-bit Stereo
    </text>
    <text x="240" y="498" text-anchor="middle" class="font-mono" font-size="9" fill="#00F2FE">
      Latency: &lt;18ms • WebRTC Transport
    </text>

    <!-- Panel Divider -->
    <line x1="410" y1="104" x2="410" y2="580" stroke="#22272E" stroke-width="1.2" stroke-dasharray="4 4" />

    <!-- ======================================================== -->
    <!-- 5. RIGHT PANEL: CONTENT & TERMINAL                       -->
    <!-- ======================================================== -->
    <!-- Pill Badge -->
    <g transform="translate(434, 106)">
      <rect x="0" y="0" width="224" height="24" rx="12" fill="#0A1813" stroke="#39F59A" stroke-width="1.2" />
      <circle cx="14" cy="12" r="4" fill="#39F59A" />
      <text x="26" y="16" class="font-mono" font-size="10.5" font-weight="800" fill="#39F59A" letter-spacing="0.5">
        ⚡ INCOMING VISITOR DETECTED
      </text>
    </g>

    <!-- Hero Title -->
    <text x="434" y="164" class="font-sans" font-size="28" font-weight="900" fill="#FFFFFF" letter-spacing="-0.5">
      WELCOME TO PACKHUNTER WORKSTATION
    </text>

    <!-- Subtitle -->
    <text x="434" y="196" class="font-sans" font-size="16" font-weight="700" fill="#00F2FE">
      Robinson J.
      <tspan font-weight="400" fill="#8B949E"> — Full-Stack Engineer &amp; System Architect</tspan>
    </text>

    <!-- Terminal Box (Pure Pitch Black) -->
    <rect x="434" y="216" width="644" height="196" rx="10" fill="url(#term-box-bg)" stroke="#22272E" stroke-width="1.2" />
    <path d="M 434 226 Q 434 216 444 216 L 1068 216 Q 1078 216 1078 226 L 1078 244 L 434 244 Z" fill="#121212" />
    <line x1="434" y1="244" x2="1078" y2="244" stroke="#22272E" stroke-width="1" />
    <circle cx="452" cy="230" r="4" fill="#FF5F56" />
    <circle cx="466" cy="230" r="4" fill="#FFBD2E" />
    <circle cx="480" cy="230" r="4" fill="#27C93F" />
    <text x="500" y="234" class="font-mono" font-size="10" fill="#8B949E">terminal@packhunter-cynic: ~ /welcome_boot.sh</text>

    <!-- Terminal Lines -->
    <g transform="translate(452, 272)">
      <text x="0" y="0" class="font-mono" font-size="12" font-weight="700" fill="#39F59A">➜</text>
      <text x="16" y="0" class="font-mono" font-size="12" font-weight="600" fill="#00F2FE">~/system</text>
      <text x="96" y="0" class="font-mono" font-size="12" fill="#F0F6FC">./init_handshake.sh --target=visitor --mode=full_access</text>
    </g>

    <g transform="translate(452, 304)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#8B949E">[AUTH: 0.18s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#F0F6FC">Profile: </text>
      <text x="168" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#00F2FE">PackhunterforCynic (Robinson J.)</text>
      <text x="435" y="0" class="font-mono" font-size="11.5" fill="#8B949E">• MCA '25 • Bengaluru</text>
    </g>

    <g transform="translate(452, 336)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#8B949E">[CORE: 0.44s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#00F2FE">WebSockets/WebRTC</text>
      <text x="260" y="0" class="font-mono" font-size="11.5" fill="#8B949E">|</text>
      <text x="275" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Phaser 4 Engine</text>
      <text x="400" y="0" class="font-mono" font-size="11.5" fill="#8B949E">|</text>
      <text x="415" y="0" class="font-mono" font-size="11.5" fill="#00F2FE">Gemini AI</text>
      <text x="495" y="0" class="font-mono" font-size="11.5" fill="#8B949E">|</text>
      <text x="510" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Lighthouse 99</text>
    </g>

    <g transform="translate(452, 368)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#8B949E">[STATUS]</text>
      <rect x="75" y="-12" width="22" height="15" rx="3" fill="#0A2A1E" />
      <text x="80" y="0" class="font-mono" font-size="11" font-weight="900" fill="#39F59A">✓</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#39F59A">200 OK — 24 Repositories &amp; 6 Production Demos Ready</text>
      <text x="540" y="0" class="font-mono cursor" font-size="14" font-weight="900" fill="#00F2FE">_</text>
    </g>

    <!-- Chips Row (y = 426) -->
    <g transform="translate(434, 426)">
      <rect x="0" y="0" width="120" height="26" rx="6" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="60" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">📡 WebRTC / P2P</text>

      <rect x="128" y="0" width="136" height="26" rx="6" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="196" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">🧠 Gemini AI / RAG</text>

      <rect x="272" y="0" width="126" height="26" rx="6" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="335" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🎮 Phaser 4 2D</text>

      <rect x="406" y="0" width="112" height="26" rx="6" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="462" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">⚡ Next.js App</text>

      <rect x="526" y="0" width="118" height="26" rx="6" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="585" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🐳 Docker Core</text>
    </g>

    <!-- Action Buttons (y = 472) -->
    <g transform="translate(434, 472)">
      <g class="btn-interactive" filter="url(#subtle-glow)">
        <rect x="0" y="0" width="324" height="46" rx="8" fill="url(#btn-primary-grad)" />
        <text x="162" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="800" fill="#000000" letter-spacing="0.3">
          🚀 ENTER WORKSTATION DASHBOARD ↘
        </text>
      </g>

      <g class="btn-interactive">
        <rect x="336" y="0" width="308" height="46" rx="8" fill="#0A0A0A" stroke="#00F2FE" stroke-width="1.5" />
        <text x="490" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="700" fill="#00F2FE" letter-spacing="0.3">
          🌐 OPEN LIVE WEB PORTFOLIO ↗
        </text>
      </g>
    </g>

    <!-- Modal Footer -->
    <rect x="80" y="604" width="1040" height="36" rx="0" fill="#0A0A0A" />
    <line x1="80" y1="604" x2="1120" y2="604" stroke="#22272E" stroke-width="1" />
    <circle cx="106" cy="622" r="3" fill="#00F2FE" />
    <text x="120" y="626" class="font-mono" font-size="10" fill="#8B949E">
      SECURE PROTOCOL ACTIVE • CLICK BANNER OR SCROLL DOWN TO EXPLORE DASHBOARD &amp; PRODUCTION PROJECTS
    </text>
    <text x="1090" y="626" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">
      ▼ SCROLL TO EXPLORE
    </text>
  </g>
</svg>
'''

# ========================================================
# 2. assets/nav_dock.svg (TRUE PITCH BLACK THEME)
# ========================================================
def build_nav_dock():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 80" width="100%" height="100%">
  <defs>
    <linearGradient id="dock-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="50%" stop-color="#070707" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <linearGradient id="dock-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#39F59A" />
      <stop offset="100%" stop-color="#00F2FE" />
    </linearGradient>
    <filter id="btn-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    
    .dock-btn {
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .dock-btn:hover rect {
      fill: #161B22;
      stroke: #00F2FE;
      filter: url(#btn-glow);
    }
    .dock-btn:hover text {
      fill: #00F2FE;
    }

    @keyframes pulseLed {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .led { animation: pulseLed 2s infinite ease-in-out; }
  </style>

  <rect x="2" y="2" width="1096" height="76" rx="14" fill="url(#dock-bg)" stroke="#22272E" stroke-width="1.5" />
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#dock-glow)" opacity="0.85" />

  <path d="M 12 18 L 12 10 L 20 10" fill="none" stroke="#00F2FE" stroke-width="2" />
  <path d="M 1088 18 L 1088 10 L 1080 10" fill="none" stroke="#00F2FE" stroke-width="2" />
  <path d="M 12 62 L 12 70 L 20 70" fill="none" stroke="#39F59A" stroke-width="2" />
  <path d="M 1088 62 L 1088 70 L 1080 70" fill="none" stroke="#39F59A" stroke-width="2" />

  <!-- 5 Buttons -->
  <g class="dock-btn" transform="translate(32, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F0F6FC">01 // NEURAL CORE</text>
  </g>

  <g class="dock-btn" transform="translate(242, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" style="animation-delay: 0.4s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F0F6FC">02 // ENGINES &amp; P2P</text>
  </g>

  <g class="dock-btn" transform="translate(452, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" style="animation-delay: 0.8s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F0F6FC">03 // AI &amp; VISION</text>
  </g>

  <g class="dock-btn" transform="translate(662, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" style="animation-delay: 1.2s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F0F6FC">04 // TELEMETRY</text>
  </g>

  <g class="dock-btn" transform="translate(872, 16)">
    <rect x="0" y="0" width="196" height="48" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" style="animation-delay: 1.6s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F0F6FC">05 // SECURE UPLINK</text>
  </g>
</svg>
'''

# ========================================================
# 3. assets/showcase_musica_game.svg (TRUE PITCH BLACK)
# ========================================================
def build_showcase_musica_game():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="60%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <linearGradient id="glow-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    
    @keyframes wavePulse {
      0%, 100% { transform: scaleY(0.4); }
      50% { transform: scaleY(1.1); }
    }
    @keyframes peerPing {
      0% { r: 6; opacity: 1; }
      100% { r: 24; opacity: 0; }
    }
    .wave-bar { transform-origin: bottom; animation: wavePulse 1.2s ease-in-out infinite alternate; }
    .ping-ring { animation: peerPing 2s cubic-bezier(0, 0.2, 0.8, 1) infinite; }
  </style>

  <!-- Left: Musica Platform -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 01 // REAL-TIME MESH</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">📡 Musica Audio Platform</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Zero-DB WebSockets &amp; WebRTC real-time audio core</text>

    <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <circle cx="70" cy="158" r="14" fill="#0A1218" stroke="#00F2FE" stroke-width="2" />
    <circle cx="70" cy="158" r="6" fill="#00F2FE" />
    <circle cx="70" cy="158" class="ping-ring" fill="none" stroke="#00F2FE" stroke-width="1.5" />
    <text x="70" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#8B949E">PEER_A</text>

    <g transform="translate(100, 140)">
      <rect class="wave-bar" x="0" y="0" width="4" height="34" rx="2" fill="#00F2FE" style="animation-delay: 0.1s;" />
      <rect class="wave-bar" x="10" y="0" width="4" height="24" rx="2" fill="#39F59A" style="animation-delay: 0.3s;" />
      <rect class="wave-bar" x="20" y="0" width="4" height="36" rx="2" fill="#00F2FE" style="animation-delay: 0.05s;" />
      <rect class="wave-bar" x="30" y="0" width="4" height="18" rx="2" fill="#39F59A" style="animation-delay: 0.4s;" />
      <rect class="wave-bar" x="40" y="0" width="4" height="30" rx="2" fill="#00F2FE" style="animation-delay: 0.2s;" />
      <rect class="wave-bar" x="50" y="0" width="4" height="22" rx="2" fill="#39F59A" style="animation-delay: 0.5s;" />
      <rect class="wave-bar" x="60" y="0" width="4" height="34" rx="2" fill="#00F2FE" style="animation-delay: 0.15s;" />
      <rect class="wave-bar" x="70" y="0" width="4" height="26" rx="2" fill="#39F59A" style="animation-delay: 0.35s;" />
    </g>

    <rect x="200" y="138" width="130" height="40" rx="6" fill="#0A1218" stroke="#00F2FE" stroke-width="1.2" />
    <text x="265" y="155" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">WS SIGNALING</text>
    <text x="265" y="170" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">&lt;18ms LATENCY</text>

    <g transform="translate(350, 140)">
      <rect class="wave-bar" x="0" y="0" width="4" height="28" rx="2" fill="#00F2FE" style="animation-delay: 0.25s;" />
      <rect class="wave-bar" x="10" y="0" width="4" height="34" rx="2" fill="#39F59A" style="animation-delay: 0.1s;" />
      <rect class="wave-bar" x="20" y="0" width="4" height="20" rx="2" fill="#00F2FE" style="animation-delay: 0.4s;" />
      <rect class="wave-bar" x="30" y="0" width="4" height="36" rx="2" fill="#39F59A" style="animation-delay: 0.15s;" />
      <rect class="wave-bar" x="40" y="0" width="4" height="24" rx="2" fill="#00F2FE" style="animation-delay: 0.3s;" />
    </g>

    <circle cx="465" cy="158" r="14" fill="#0A1813" stroke="#39F59A" stroke-width="2" />
    <circle cx="465" cy="158" r="6" fill="#39F59A" />
    <circle cx="465" cy="158" class="ping-ring" fill="none" stroke="#39F59A" stroke-width="1.5" style="animation-delay: 1s;" />
    <text x="465" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#8B949E">PEER_B</text>

    <!-- Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="86" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="43" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="94" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="132" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Node.js</text>

      <rect x="178" y="0" width="80" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="218" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">WebRTC</text>

      <rect x="266" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="304" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Socket.IO</text>

      <rect x="350" y="0" width="68" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="384" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Docker</text>

      <rect x="426" y="0" width="86" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="469" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Zero-DB</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎧 musica-apvs.vercel.app ↗]  •  [github.com/PackhunterforCynic/musica ↗]
    </text>
  </g>

  <!-- Right: Ben 10 Alien Arena -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 02 // DETERMINISTIC P2P</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE GAME</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎮 Ben 10: Alien Battle Arena</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">2D fighting engine in Phaser 4 with PeerJS direct multiplayer</text>

    <rect x="24" y="112" width="486" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <text x="40" y="134" class="font-mono" font-size="9.5" font-weight="700" fill="#39F59A">PLAYER 1 // FOURARMS</text>
    <rect x="40" y="140" width="180" height="10" rx="3" fill="#121212" stroke="#22272E" stroke-width="1" />
    <rect x="41" y="141" width="150" height="8" rx="2" fill="url(#glow-cyan)" />

    <text x="266" y="134" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">PLAYER 2 // HEATBLAST</text>
    <rect x="266" y="140" width="180" height="10" rx="3" fill="#121212" stroke="#22272E" stroke-width="1" />
    <rect x="267" y="141" width="130" height="8" rx="2" fill="#00F2FE" />

    <circle cx="242" cy="158" r="18" fill="#0A1218" stroke="#00F2FE" stroke-width="1.5" />
    <text x="242" y="162" text-anchor="middle" class="font-mono" font-size="11" font-weight="900" fill="#00F2FE">VS</text>

    <text x="40" y="174" class="font-mono" font-size="9" fill="#8B949E">Canvas Tick: 60 FPS</text>
    <text x="40" y="188" class="font-mono" font-size="9" fill="#00F2FE">State Sync: Deterministic PeerJS</text>
    <text x="266" y="174" class="font-mono" font-size="9" fill="#8B949E">Audio: Web Audio API Synth</text>
    <text x="266" y="188" class="font-mono" font-size="9" fill="#39F59A">Zero Server Lag: Browser P2P</text>

    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="80" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="40" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Phaser 4</text>

      <rect x="88" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="126" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React 19</text>

      <rect x="172" y="0" width="90" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="217" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">TypeScript</text>

      <rect x="270" y="0" width="74" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="307" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PeerJS</text>

      <rect x="352" y="0" width="84" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="394" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Web Audio</text>

      <rect x="444" y="0" width="66" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="477" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">P2P Mesh</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎮 game-rovenor.vercel.app ↗]  •  [github.com/PackhunterforCynic/game ↗]
    </text>
  </g>
</svg>
'''

# ========================================================
# 4. assets/showcase_ai_camx.svg (TRUE PITCH BLACK)
# ========================================================
def build_showcase_ai_camx():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg-ai" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="60%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  </style>

  <!-- Left: PlantSense AI -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg-ai)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 03 // VISION AI &amp; VECTOR RAG</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● FASTAPI LIVE</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🌱 PlantSense Botanical AI</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Gemini Vision AI multimodal pathology with ChromaDB vector RAG</text>

    <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <rect x="40" y="124" width="70" height="68" rx="4" fill="#0A0A0A" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="4 4" />
    <path d="M 75 132 C 60 145 60 170 75 182 C 90 170 90 145 75 132 Z" fill="#0E241E" stroke="#39F59A" stroke-width="1.5" />
    <line x1="75" y1="135" x2="75" y2="180" stroke="#00F2FE" stroke-width="1.2" />
    <text x="75" y="198" text-anchor="middle" class="font-mono" font-size="8" fill="#00F2FE">99.4% CONF</text>

    <line x1="116" y1="158" x2="148" y2="158" stroke="#00F2FE" stroke-width="2" />

    <g transform="translate(156, 126)">
      <circle cx="10" cy="14" r="5" fill="#39F59A" />
      <circle cx="10" cy="34" r="5" fill="#39F59A" />
      <circle cx="10" cy="54" r="5" fill="#39F59A" />
      <circle cx="50" cy="24" r="6" fill="#00F2FE" />
      <circle cx="50" cy="44" r="6" fill="#00F2FE" />
      <circle cx="90" cy="34" r="7" fill="#39F59A" />

      <line x1="10" y1="14" x2="50" y2="24" stroke="#22272E" stroke-width="1" />
      <line x1="10" y1="34" x2="50" y2="24" stroke="#22272E" stroke-width="1" />
      <line x1="10" y1="34" x2="50" y2="44" stroke="#22272E" stroke-width="1" />
      <line x1="10" y1="54" x2="50" y2="44" stroke="#22272E" stroke-width="1" />
      <line x1="50" y1="24" x2="90" y2="34" stroke="#39F59A" stroke-width="1.5" />
      <line x1="50" y1="44" x2="90" y2="34" stroke="#00F2FE" stroke-width="1.5" />
    </g>

    <rect x="270" y="126" width="160" height="64" rx="6" fill="#0A1218" stroke="#00F2FE" stroke-width="1.2" />
    <text x="350" y="146" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">ChromaDB RAG</text>
    <text x="350" y="162" text-anchor="middle" class="font-mono" font-size="8.5" fill="#8B949E">Cosine Distance Metric</text>
    <text x="350" y="176" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">Instant Remedy Retrieval</text>

    <!-- Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="70" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="35" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Python</text>

      <rect x="78" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="116" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">FastAPI</text>

      <rect x="162" y="0" width="86" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="205" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Gemini AI</text>

      <rect x="256" y="0" width="94" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="303" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">ChromaDB</text>

      <rect x="358" y="0" width="70" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="393" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">RAG Net</text>

      <rect x="436" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="474" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision AI</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🌱 robinsonj.vercel.app ↗]  •  [github.com/PackhunterforCynic ↗]
    </text>
  </g>

  <!-- Right: CAMX Optics -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg-ai)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 04 // OPTICS &amp; COMPUTER VISION</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● SHOWCASE</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">📷 CAMX Digital Camera Lab</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Hands-free optics simulator with EV100, landmarks, voice commands</text>

    <rect x="24" y="112" width="486" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <g transform="translate(80, 158)">
      <circle cx="0" cy="0" r="32" fill="#0A1218" stroke="#22272E" stroke-width="1.5" />
      <polygon points="0,-24 16,-12 10,10 -12,18 -22,-2" fill="#081014" stroke="#00F2FE" stroke-width="1.2" />
      <circle cx="0" cy="0" r="10" fill="#000000" stroke="#39F59A" stroke-width="1.5" />
      <text x="0" y="44" text-anchor="middle" class="font-mono" font-size="8.5" fill="#00F2FE">f/1.8 APERTURE</text>
    </g>

    <g transform="translate(145, 128)">
      <text x="0" y="14" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">EV100 Exposure: +1.3 EV</text>
      <text x="0" y="28" class="font-mono" font-size="9" fill="#8B949E">Focal Length: 50mm Equivalent</text>
      <text x="0" y="42" class="font-mono" font-size="9" fill="#39F59A">Facial Landmarks: 468 Points 3D</text>
      <text x="0" y="56" class="font-mono" font-size="9" fill="#8B949E">Voice Control: Web Speech API</text>
    </g>

    <g transform="translate(390, 138)">
      <rect x="0" y="0" width="84" height="42" rx="4" fill="#0A1218" stroke="#22272E" stroke-width="1" />
      <path d="M 6 28 Q 24 6 42 22 T 78 18" fill="none" stroke="#00F2FE" stroke-width="1.8" />
      <text x="42" y="36" text-anchor="middle" class="font-mono" font-size="7.5" fill="#39F59A">OPTICS CURVE</text>
    </g>

    <!-- Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="90" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="45" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="98" y="0" width="80" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="138" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">WebRTC</text>

      <rect x="186" y="0" width="96" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="234" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Optics Physics</text>

      <rect x="290" y="0" width="86" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="333" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Voice API</text>

      <rect x="384" y="0" width="70" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="419" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision Lab</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [📷 robinsonj.vercel.app ↗]  •  [github.com/PackhunterforCynic ↗]
    </text>
  </g>
</svg>
'''

# ========================================================
# 5. assets/showcase_havilah_hse.svg (TRUE PITCH BLACK)
# ========================================================
def build_showcase_havilah_hse():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg-web" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="60%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <linearGradient id="score-ring-hse" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  </style>

  <!-- Left: Havilah Studio -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg-web)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 05 // CINEMATIC MULTIMEDIA</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎥 Havilah Studio Portfolio</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Cinematic multimedia portfolio powered by Bun runtime &amp; GSAP</text>

    <rect x="24" y="112" width="488" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <line x1="40" y1="145" x2="480" y2="145" stroke="#22272E" stroke-width="2" />
    <circle cx="160" cy="145" r="7" fill="#00F2FE" />
    <circle cx="280" cy="145" r="7" fill="#39F59A" />
    <circle cx="400" cy="145" r="7" fill="#00F2FE" />
    <path d="M 40 165 C 100 135 180 185 280 145 C 380 105 440 165 480 135" fill="none" stroke="#00F2FE" stroke-width="1.8" />
    <text x="40" y="186" class="font-mono" font-size="9" fill="#8B949E">GSAP Smooth Tweens • 60 FPS • Bun High-Throughput Bundling</text>

    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="86" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="43" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="94" y="0" width="60" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="124" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Bun</text>

      <rect x="162" y="0" width="68" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="196" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React</text>

      <rect x="238" y="0" width="66" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="271" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">GSAP</text>

      <rect x="312" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="350" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vercel</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎥 havilah-alpha.vercel.app ↗]  •  [github.com/PackhunterforCynic/havilah ↗]
    </text>
  </g>

  <!-- Right: HSE Media Suite -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg-web)" stroke="#22272E" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#121212" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#22272E" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">ENGINE 06 // LIGHTHOUSE 99 PERFORMANCE</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#FFFFFF">🎬 HSE Media Production Suite</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#8B949E">Next.js App Router multi-media engine with automated audits</text>

    <rect x="24" y="112" width="486" height="92" rx="8" fill="#000000" stroke="#1F2428" stroke-width="1" />
    
    <g transform="translate(70, 158)">
      <circle cx="0" cy="0" r="30" fill="none" stroke="#22272E" stroke-width="5" />
      <circle cx="0" cy="0" r="30" fill="none" stroke="url(#score-ring-hse)" stroke-width="5" stroke-dasharray="182 8" stroke-linecap="round" />
      <text x="0" y="8" text-anchor="middle" class="font-sans" font-size="18" font-weight="900" fill="#00F2FE">99</text>
      <text x="0" y="44" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">LIGHTHOUSE</text>
    </g>

    <g transform="translate(130, 130)">
      <text x="0" y="14" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">Next.js App Router: Dynamic Edge Cache</text>
      <text x="0" y="28" class="font-mono" font-size="9" fill="#8B949E">SEO Score: 100 • Accessibility: 100</text>
      <text x="0" y="42" class="font-mono" font-size="9" fill="#39F59A">Lighthouse Performance: 99 Verified</text>
      <text x="0" y="56" class="font-mono" font-size="9" fill="#8B949E">Tailwind CSS v4 • Continuous Auditing</text>
    </g>

    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="80" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="40" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Next.js</text>

      <rect x="88" y="0" width="80" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="128" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Tailwind</text>

      <rect x="176" y="0" width="60" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="206" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PHP</text>

      <rect x="244" y="0" width="76" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="282" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Vercel</text>

      <rect x="328" y="0" width="94" height="24" rx="5" fill="#0D1117" stroke="#21262D" stroke-width="1" />
      <text x="375" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Score 99</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎬 hse-indol.vercel.app ↗]  •  [github.com/PackhunterforCynic/hse ↗]
    </text>
  </g>
</svg>
'''

# ========================================================
# 6. assets/tech_arsenal.svg (TRUE PITCH BLACK)
# ========================================================
def build_tech_arsenal():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 320" width="100%" height="100%">
  <defs>
    <linearGradient id="arsenal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="50%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <linearGradient id="bar-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    
    .tech-row {
      transition: all 0.2s ease;
    }
  </style>

  <rect x="2" y="2" width="1096" height="316" rx="14" fill="url(#arsenal-bg)" stroke="#22272E" stroke-width="1.5" />
  
  <path d="M 2 16 Q 2 2 16 2 L 1084 2 Q 1098 2 1098 16 L 1098 44 L 2 44 Z" fill="#121212" />
  <line x1="2" y1="44" x2="1098" y2="44" stroke="#22272E" stroke-width="1.2" />

  <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
  <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
  <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#8B949E">
    ⚡ SYSTEM CAPABILITIES // CORE ENGINEERING ARSENAL &amp; ARCHITECTURE
  </text>
  <rect x="970" y="13" width="112" height="20" rx="4" fill="#0A1813" stroke="#39F59A" stroke-width="1" />
  <text x="1026" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">VERIFIED 2026</text>

  <!-- 4 Columns -->
  <g transform="translate(32, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#00F2FE">01 // REAL-TIME MESH</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#22272E" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">WebRTC (P2P Audio/Video)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">WebSockets &amp; Socket.IO</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Zero-DB Volatile State Core</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Web Audio API Synthesis</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">REST &amp; Streaming Protocols</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <line x1="288" y1="64" x2="288" y2="260" stroke="#1F2428" stroke-width="1" stroke-dasharray="4 4" />

  <g transform="translate(308, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#39F59A">02 // LANGUAGES &amp; RUNTIME</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#22272E" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">TypeScript &amp; JavaScript</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Python (FastAPI &amp; ML)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Node.js &amp; Bun Runtime</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="205" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">SQL &amp; PostgreSQL Engine</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">C++ / Object-Oriented</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="170" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <line x1="564" y1="64" x2="564" y2="260" stroke="#1F2428" stroke-width="1" stroke-dasharray="4 4" />

  <g transform="translate(584, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#00F2FE">03 // AI &amp; GAME ENGINES</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#22272E" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Next.js App Router (v15)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">React 19 &amp; Tailwind CSS v4</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Gemini Vision AI Pipeline</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">ChromaDB Vector RAG</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Phaser 4 &amp; GSAP 2D</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <line x1="840" y1="64" x2="840" y2="260" stroke="#1F2428" stroke-width="1" stroke-dasharray="4 4" />

  <g transform="translate(860, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#39F59A">04 // CLOUD &amp; SYSTEMS</text>
    <line x1="0" y1="8" x2="200" y2="8" stroke="#22272E" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Docker &amp; Containerization</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Git &amp; GitHub Actions CI/CD</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Linux Shell Scripting</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Vercel Edge Network</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F0F6FC">Lighthouse 99 Auditing</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#121212" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <!-- Bottom Strip -->
  <line x1="2" y1="280" x2="1098" y2="280" stroke="#22272E" stroke-width="1" />
  <circle cx="24" cy="298" r="3.5" fill="#00F2FE" />
  <text x="36" y="302" class="font-mono" font-size="10" fill="#8B949E">
    CORE METRICS: 24 REPOSITORIES • 6 PRODUCTION SYSTEMS • HIGH-THROUGHPUT ARCHITECTURE
  </text>
  <text x="1076" y="302" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">
    ✓ TRUE BLACK OLED
  </text>
</svg>
'''

# ========================================================
# 7. assets/footer_uplink.svg (TRUE PITCH BLACK)
# ========================================================
def build_footer_uplink():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 110" width="100%" height="100%">
  <defs>
    <linearGradient id="footer-bg-nexus" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E0E0E" />
      <stop offset="50%" stop-color="#060606" />
      <stop offset="100%" stop-color="#000000" />
    </linearGradient>
    <linearGradient id="neon-glow-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.2" />
      <stop offset="30%" stop-color="#00F2FE" stop-opacity="0.95" />
      <stop offset="70%" stop-color="#39F59A" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0.2" />
    </linearGradient>
    <filter id="pulse-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    
    @keyframes emitterPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }
    .pulse-dot {
      animation: emitterPulse 2.5s infinite ease-in-out;
    }
  </style>

  <rect x="2" y="2" width="1096" height="106" rx="14" fill="url(#footer-bg-nexus)" stroke="#22272E" stroke-width="1.5" />
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#neon-glow-line)" />

  <g transform="translate(32, 38)">
    <circle cx="8" cy="8" r="5" fill="#00F2FE" class="pulse-dot" />
    <text x="24" y="12" class="font-mono" font-size="14" font-weight="800" fill="#FFFFFF" letter-spacing="1">
      ROBINSON J. // PACKHUNTERFORCYNIC
    </text>
    <text x="24" y="32" class="font-sans" font-size="11.5" fill="#8B949E">
      Engineered for Scale, Low-Latency WebRTC &amp; High-Throughput System Architecture
    </text>
    <text x="24" y="48" class="font-mono" font-size="9.5" fill="#00F2FE">
      Verified Identity: MCA '25 • Bengaluru, Karnataka, India • 24 Verified Repositories
    </text>
  </g>

  <g transform="translate(820, 30)">
    <rect x="0" y="0" width="248" height="52" rx="8" fill="#0D1117" stroke="#21262D" stroke-width="1.2" />
    <circle cx="20" cy="26" r="6" fill="#00F2FE" />
    <text x="36" y="22" class="font-mono" font-size="11" font-weight="800" fill="#00F2FE">200 OK — ALL ONLINE</text>
    <text x="36" y="38" class="font-mono" font-size="9" fill="#8B949E">PACKHUNTER-OS v5.1 // TRUE BLACK</text>
  </g>
</svg>
'''

# Write all SVGs
def generate_all():
    files = {
        'assets/welcome_popup.svg': build_welcome_popup(),
        'assets/nav_dock.svg': build_nav_dock(),
        'assets/showcase_musica_game.svg': build_showcase_musica_game(),
        'assets/showcase_ai_camx.svg': build_showcase_ai_camx(),
        'assets/showcase_havilah_hse.svg': build_showcase_havilah_hse(),
        'assets/tech_arsenal.svg': build_tech_arsenal(),
        'assets/footer_uplink.svg': build_footer_uplink(),
    }
    for path, content in files.items():
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        ET.parse(path) # Verify valid XML
        print(f"Generated {path} (True Black, Valid XML, {os.path.getsize(path)} bytes)")

if __name__ == '__main__':
    generate_all()
