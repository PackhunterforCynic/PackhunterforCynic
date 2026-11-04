import base64
import os

# 1. Prepare base64 of the authentic Cyber Wolf Avatar
wolf_path = 'assets/profile/wolf_popup_thumb.png'
with open(wolf_path, 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="vignette-bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#071924" />
      <stop offset="50%" stop-color="#040D14" />
      <stop offset="100%" stop-color="#010508" />
    </radialGradient>

    <linearGradient id="modal-glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" stop-opacity="0.97" />
      <stop offset="50%" stop-color="#05131C" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#02090F" stop-opacity="0.99" />
    </linearGradient>

    <!-- Neon Cyan & Emerald -->
    <linearGradient id="neon-cyan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>

    <!-- Amber & Gold Rim Gradient (Matches Avatar Rim Glow) -->
    <linearGradient id="neon-gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF9100" />
      <stop offset="100%" stop-color="#00F2FE" />
    </linearGradient>

    <linearGradient id="btn-primary-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#00C49F" />
    </linearGradient>

    <linearGradient id="term-box-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#030C12" />
      <stop offset="100%" stop-color="#02070A" />
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

    <!-- Clip Path for Wolf Avatar (radius 95 at center 240, 310) -->
    <clipPath id="avatar-clip">
      <circle cx="240" cy="310" r="95" />
    </clipPath>

    <!-- Grid Pattern for full screen backdrop -->
    <pattern id="cyber-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#0B2A3D" stroke-width="0.7" opacity="0.4" />
      <circle cx="40" cy="40" r="1" fill="#00F2FE" opacity="0.3" />
    </pattern>
  </defs>

  <style>
    /* Safe CSS Keyframes (No transform overrides on translated groups!) */
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
      font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', 'Consolas', monospace;
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

    /* Button Hovers */
    .btn-interactive {{
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .btn-interactive:hover {{
      filter: url(#neon-glow);
    }}

    /* Equalizer Bars */
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
  <!-- 1. FULL-SCREEN BACKDROP OVERLAY & MATRIX GRID            -->
  <!-- ======================================================== -->
  <!-- Radial Vignette -->
  <rect x="0" y="0" width="1200" height="680" fill="url(#vignette-bg)" />

  <!-- Cyber Grid -->
  <rect x="0" y="0" width="1200" height="680" fill="url(#cyber-grid)" />

  <!-- Outer Full-Screen Border -->
  <rect x="2" y="2" width="1196" height="676" rx="14" fill="none" stroke="#0E394A" stroke-width="1.5" />

  <!-- Full-Screen Laser Scan Line -->
  <g class="scan-beam">
    <line x1="0" y1="0" x2="1200" y2="0" stroke="url(#neon-cyan-grad)" stroke-width="2" opacity="0.8" filter="url(#neon-glow)" />
    <polygon points="0,0 1200,0 1200,-25 0,-25" fill="url(#neon-cyan-grad)" opacity="0.08" />
  </g>

  <!-- Matrix Coordinates Display -->
  <text x="32" y="24" class="font-mono" font-size="10" fill="#15536B">SYS_LOC: 12.9716° N, 77.5946° E [BENGALURU, INDIA]</text>
  <text x="1168" y="24" text-anchor="end" class="font-mono" font-size="10" fill="#15536B">PACKHUNTER-OS v5.0 // NEURAL WORKSTATION</text>

  <!-- ======================================================== -->
  <!-- 2. THE MODAL POP-UP WINDOW                               -->
  <!-- ======================================================== -->
  <g id="modal-window">
    <!-- Pop-up Window Outer Shadow / Glow Halo -->
    <rect x="76" y="36" width="1048" height="608" rx="20" fill="none" stroke="#00F2FE" stroke-width="3" opacity="0.25" filter="url(#neon-glow)" />
    
    <!-- Pop-up Window Main Glass Box -->
    <rect x="80" y="40" width="1040" height="600" rx="18" fill="url(#modal-glass)" stroke="#12444C" stroke-width="1.8" />

    <!-- Secondary Inner Accent Line -->
    <rect x="84" y="44" width="1032" height="592" rx="14" fill="none" stroke="#00F2FE" stroke-width="0.8" opacity="0.3" />

    <!-- Corner Cyber HUD Brackets -->
    <!-- Top-Left Bracket -->
    <path d="M 80 75 L 80 40 L 115 40" fill="none" stroke="#00F2FE" stroke-width="3" />
    <circle cx="92" cy="52" r="2.5" fill="#00F2FE" />

    <!-- Top-Right Bracket -->
    <path d="M 1085 40 L 1120 40 L 1120 75" fill="none" stroke="#00F2FE" stroke-width="3" />
    <circle cx="1108" cy="52" r="2.5" fill="#00F2FE" />

    <!-- Bottom-Left Bracket -->
    <path d="M 80 605 L 80 640 L 115 640" fill="none" stroke="#FF9100" stroke-width="3" />
    <circle cx="92" cy="628" r="2.5" fill="#FF9100" />

    <!-- Bottom-Right Bracket -->
    <path d="M 1085 640 L 1120 640 L 1120 605" fill="none" stroke="#FF9100" stroke-width="3" />
    <circle cx="1108" cy="628" r="2.5" fill="#FF9100" />

    <!-- ======================================================== -->
    <!-- 3. MODAL WINDOW HEADER BAR (OS CHROME)                   -->
    <!-- ======================================================== -->
    <path d="M 80 58 Q 80 40 98 40 L 1102 40 Q 1120 40 1120 58 L 1120 84 L 80 84 Z" fill="#061824" />
    <line x1="80" y1="84" x2="1120" y2="84" stroke="#12444C" stroke-width="1.5" />

    <!-- Mac Traffic Light Buttons with Neon Glow -->
    <circle cx="110" cy="62" r="6.5" fill="#FF5F56" />
    <circle cx="132" cy="62" r="6.5" fill="#FFBD2E" />
    <circle cx="154" cy="62" r="6.5" fill="#27C93F" />

    <!-- Modal Title -->
    <text x="600" y="66" text-anchor="middle" class="font-mono" font-size="12" font-weight="700" fill="#9BAEAA" letter-spacing="1">
      ⚡ PACKHUNTER-OS v5.0 // NEURAL NEXUS // INCOMING_VISITOR_AUTHENTICATED
    </text>

    <!-- Header Right Buttons: Fullscreen & Status -->
    <rect x="910" y="52" width="86" height="20" rx="4" fill="#04121A" stroke="#12444C" stroke-width="1" />
    <text x="953" y="66" text-anchor="middle" class="font-mono" font-size="9" font-weight="700" fill="#00F2FE">⛶ FULLSCREEN</text>

    <rect x="1004" y="52" width="98" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <circle cx="1016" cy="62" r="3.5" fill="#39F59A" />
    <text x="1058" y="66" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">200 OK LIVE</text>

    <!-- ======================================================== -->
    <!-- 4. MODAL CONTENT: LEFT PANEL (MATCHING CYBER WOLF AVATAR)-->
    <!-- ======================================================== -->
    <!-- Left Background Glow -->
    <circle cx="240" cy="310" r="140" fill="#0E3D52" opacity="0.25" filter="url(#neon-glow)" />

    <!-- Sonar Radar Ping Wave -->
    <circle cx="240" cy="310" class="sonar-ping" fill="none" stroke="#00F2FE" />

    <!-- Outer Rotating Targeting Reticle (Clockwise) -->
    <g class="reticle-cw">
      <circle cx="240" cy="310" r="128" fill="none" stroke="#12444C" stroke-dasharray="8 12 18 10" stroke-width="1.8" opacity="0.8" />
      <circle cx="240" cy="310" r="134" fill="none" stroke="#00F2FE" stroke-dasharray="4 28" stroke-width="2.5" opacity="0.85" />
    </g>

    <!-- Inner Segmented Arc (Counter-Clockwise) -->
    <g class="reticle-ccw">
      <circle cx="240" cy="310" r="112" fill="none" stroke="#FF9100" stroke-dasharray="16 22 8 22" stroke-width="1.5" opacity="0.75" />
    </g>

    <!-- Radar Crosshairs -->
    <line x1="240" y1="160" x2="240" y2="178" stroke="#00F2FE" stroke-width="2" />
    <line x1="240" y1="442" x2="240" y2="460" stroke="#00F2FE" stroke-width="2" />
    <line x1="90" y1="310" x2="108" y2="310" stroke="#FF9100" stroke-width="2" />
    <line x1="372" y1="310" x2="390" y2="310" stroke="#FF9100" stroke-width="2" />

    <!-- MASKED CYBER WOLF AI AVATAR (Matches Robinson's GitHub Avatar 1:1) -->
    <image href="data:image/png;base64,{avatar_b64}" x="145" y="215" width="190" height="190" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />

    <!-- Dual Glowing Neon Rings around Avatar (Cyan + Gold Rim matching avatar) -->
    <circle cx="240" cy="310" r="95" fill="none" stroke="#00F2FE" stroke-width="3" filter="url(#subtle-glow)" />
    <circle cx="240" cy="310" r="99" fill="none" stroke="#FF9100" stroke-width="1.5" opacity="0.85" />

    <!-- Avatar HUD Title Pill -->
    <rect x="156" y="416" width="168" height="22" rx="11" fill="#071924" stroke="#12444C" stroke-width="1.2" />
    <circle cx="170" cy="427" r="3.5" fill="#00F2FE" />
    <text x="244" y="431" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE" letter-spacing="0.5">
      CYBER WOLF AI CORE
    </text>

    <!-- Animated Audio Equalizer Visualizer (Musica WebRTC Stream) -->
    <g transform="translate(176, 5)">
      <rect class="eq-1" x="0" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-2" x="12" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-3" x="24" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-4" x="36" y="446" width="6" height="4" rx="2" fill="#FF9100" />
      <rect class="eq-5" x="48" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-6" x="60" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-7" x="72" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-8" x="84" y="446" width="6" height="4" rx="2" fill="#FF9100" />
      <rect class="eq-9" x="96" y="446" width="6" height="4" rx="2" fill="#00F2FE" />
      <rect class="eq-10" x="108" y="446" width="6" height="4" rx="2" fill="#39F59A" />
    </g>

    <!-- Live Stream Sub-label -->
    <text x="240" y="482" text-anchor="middle" class="font-mono" font-size="9.5" fill="#9BAEAA">
      Musica Zero-DB • 96kHz / 24-bit Stereo
    </text>
    <text x="240" y="498" text-anchor="middle" class="font-mono" font-size="9" fill="#00F2FE">
      Latency: &lt;18ms • WebRTC Transport
    </text>

    <!-- Vertical Panel Divider -->
    <line x1="410" y1="104" x2="410" y2="580" stroke="#12444C" stroke-width="1.2" stroke-dasharray="4 4" />

    <!-- ======================================================== -->
    <!-- 5. MODAL CONTENT: RIGHT PANEL (WELCOME & IDENTITY)       -->
    <!-- ======================================================== -->
    <!-- Alert Banner / Badge -->
    <g transform="translate(434, 106)">
      <rect x="0" y="0" width="224" height="24" rx="12" fill="#0A2A22" stroke="#39F59A" stroke-width="1.2" />
      <circle cx="14" cy="12" r="4" fill="#39F59A" />
      <text x="26" y="16" class="font-mono" font-size="10.5" font-weight="800" fill="#39F59A" letter-spacing="0.5">
        ⚡ INCOMING VISITOR DETECTED
      </text>
    </g>

    <!-- Main Hero Heading -->
    <text x="434" y="164" class="font-sans" font-size="28" font-weight="900" fill="#F4F7F6" letter-spacing="-0.5">
      WELCOME TO PACKHUNTER WORKSTATION
    </text>

    <!-- Subheading / Identity -->
    <text x="434" y="196" class="font-sans" font-size="16" font-weight="700" fill="#00F2FE">
      Robinson J.
      <tspan font-weight="400" fill="#9BAEAA"> — Full-Stack Engineer &amp; System Architect</tspan>
    </text>

    <!-- Terminal Output Box -->
    <rect x="434" y="216" width="644" height="196" rx="10" fill="url(#term-box-bg)" stroke="#12444C" stroke-width="1.2" />
    <path d="M 434 226 Q 434 216 444 216 L 1068 216 Q 1078 216 1078 226 L 1078 244 L 434 244 Z" fill="#081E2B" />
    <line x1="434" y1="244" x2="1078" y2="244" stroke="#12444C" stroke-width="1" />
    <circle cx="452" cy="230" r="4" fill="#FF5F56" />
    <circle cx="466" cy="230" r="4" fill="#FFBD2E" />
    <circle cx="480" cy="230" r="4" fill="#27C93F" />
    <text x="500" y="234" class="font-mono" font-size="10" fill="#9BAEAA">terminal@packhunter-cynic: ~ /welcome_boot.sh</text>

    <!-- Terminal Lines (Always 100% visible, syntax highlighted!) -->
    <!-- Line 1: Command & Auth -->
    <g transform="translate(452, 272)">
      <text x="0" y="0" class="font-mono" font-size="12" font-weight="700" fill="#39F59A">➜</text>
      <text x="16" y="0" class="font-mono" font-size="12" font-weight="600" fill="#00F2FE">~/system</text>
      <text x="96" y="0" class="font-mono" font-size="12" fill="#F4F7F6">./init_handshake.sh --target=visitor --mode=full_access</text>
    </g>

    <!-- Line 2: Identity Verification -->
    <g transform="translate(452, 304)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[AUTH: 0.18s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#F4F7F6">Profile: </text>
      <text x="168" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#00F2FE">PackhunterforCynic (Robinson J.)</text>
      <text x="435" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">• MCA '25 • Bengaluru</text>
    </g>

    <!-- Line 3: System Pipeline -->
    <g transform="translate(452, 336)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[CORE: 0.44s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#00F2FE">WebSockets/WebRTC</text>
      <text x="260" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="275" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Phaser 4 Engine</text>
      <text x="400" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="415" y="0" class="font-mono" font-size="11.5" fill="#00F2FE">Gemini AI</text>
      <text x="495" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="510" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Lighthouse 99</text>
    </g>

    <!-- Line 4: Status Ready -->
    <g transform="translate(452, 368)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[STATUS]</text>
      <rect x="75" y="-12" width="22" height="15" rx="3" fill="#0A3326" />
      <text x="80" y="0" class="font-mono" font-size="11" font-weight="900" fill="#39F59A">✓</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#39F59A">200 OK — 24 Repositories &amp; 6 Production Demos Ready</text>
      <text x="540" y="0" class="font-mono cursor" font-size="14" font-weight="900" fill="#00F2FE">_</text>
    </g>

    <!-- Interactive Domain Chips Bar (Firmly positioned at y=426) -->
    <g transform="translate(434, 426)">
      <!-- Chip 1: WebRTC -->
      <rect x="0" y="0" width="120" height="26" rx="6" fill="#07221C" stroke="#12444C" stroke-width="1" />
      <text x="60" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">📡 WebRTC / P2P</text>

      <!-- Chip 2: AI / ML -->
      <rect x="128" y="0" width="136" height="26" rx="6" fill="#07221C" stroke="#12444C" stroke-width="1" />
      <text x="196" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">🧠 Gemini AI / RAG</text>

      <!-- Chip 3: Game Dev -->
      <rect x="272" y="0" width="126" height="26" rx="6" fill="#07221C" stroke="#12444C" stroke-width="1" />
      <text x="335" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🎮 Phaser 4 2D</text>

      <!-- Chip 4: Next.js -->
      <rect x="406" y="0" width="112" height="26" rx="6" fill="#07221C" stroke="#12444C" stroke-width="1" />
      <text x="462" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">⚡ Next.js App</text>

      <!-- Chip 5: Docker -->
      <rect x="526" y="0" width="118" height="26" rx="6" fill="#07221C" stroke="#12444C" stroke-width="1" />
      <text x="585" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🐳 Docker Core</text>
    </g>

    <!-- High-Impact Action Buttons (Firmly positioned at y=472!) -->
    <g transform="translate(434, 472)">
      <!-- Primary Button: Enter Workstation Dashboard -->
      <g class="btn-interactive" filter="url(#subtle-glow)">
        <rect x="0" y="0" width="324" height="46" rx="8" fill="url(#btn-primary-grad)" />
        <text x="162" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="800" fill="#030C12" letter-spacing="0.3">
          🚀 ENTER WORKSTATION DASHBOARD ↘
        </text>
      </g>

      <!-- Secondary Button: Launch Live Full-Screen Portfolio -->
      <g class="btn-interactive">
        <rect x="336" y="0" width="308" height="46" rx="8" fill="#061824" stroke="#00F2FE" stroke-width="1.5" />
        <text x="490" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="700" fill="#00F2FE" letter-spacing="0.3">
          🌐 OPEN LIVE WEB PORTFOLIO ↗
        </text>
      </g>
    </g>

    <!-- Bottom Status Strip of Pop-up Modal -->
    <rect x="80" y="604" width="1040" height="36" rx="0" fill="#030B10" />
    <line x1="80" y1="604" x2="1120" y2="604" stroke="#12444C" stroke-width="1" />
    <circle cx="106" cy="622" r="3" fill="#00F2FE" />
    <text x="120" y="626" class="font-mono" font-size="10" fill="#9BAEAA">
      SECURE PROTOCOL ACTIVE • CLICK BANNER OR SCROLL DOWN TO EXPLORE DASHBOARD &amp; PRODUCTION PROJECTS
    </text>
    <text x="1090" y="626" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">
      ▼ SCROLL TO EXPLORE
    </text>
  </g>
</svg>
'''

with open('assets/welcome_popup.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f"Generated pixel-perfect assets/welcome_popup.svg, size: {os.path.getsize('assets/welcome_popup.svg')} bytes")

