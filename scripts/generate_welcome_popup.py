import base64
import os

# Load base64 of the wolf avatar thumbnail
wolf_thumb_path = 'assets/profile/wolf_popup_thumb.png'
with open(wolf_thumb_path, 'rb') as f:
    avatar_b64 = base64.b64encode(f.read()).decode('utf-8')

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="vignette-bg" cx="50%" cy="50%" r="70%" fx="50%" fy="50%">
      <stop offset="0%" stop-color="#08181A" />
      <stop offset="60%" stop-color="#03080A" />
      <stop offset="100%" stop-color="#010304" />
    </radialGradient>

    <linearGradient id="modal-glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0A1F21" stop-opacity="0.96" />
      <stop offset="50%" stop-color="#061416" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#030A0C" stop-opacity="0.99" />
    </linearGradient>

    <!-- Neon Accents -->
    <linearGradient id="neon-emerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#20D9D2" />
      <stop offset="100%" stop-color="#39F59A" />
    </linearGradient>

    <linearGradient id="btn-primary-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#39F59A" />
      <stop offset="100%" stop-color="#1DB580" />
    </linearGradient>

    <linearGradient id="term-box-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#040F11" />
      <stop offset="100%" stop-color="#020809" />
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

    <!-- Clip Path for Wolf Avatar (radius 92 at center 240, 310) -->
    <clipPath id="avatar-clip">
      <circle cx="240" cy="310" r="92" />
    </clipPath>

    <!-- Grid Pattern for full screen backdrop -->
    <pattern id="cyber-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#0E2D28" stroke-width="0.7" opacity="0.35" />
      <circle cx="40" cy="40" r="1" fill="#1C5E53" opacity="0.4" />
    </pattern>
  </defs>

  <style>
    /* Keyframe Animations */
    @keyframes modalPopUp {{
      0% {{
        transform: scale(0.68) translateY(60px);
        opacity: 0;
      }}
      55% {{
        transform: scale(1.02) translateY(-6px);
        opacity: 1;
      }}
      75% {{
        transform: scale(0.995) translateY(2px);
      }}
      100% {{
        transform: scale(1) translateY(0);
        opacity: 1;
      }}
    }}

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
      0% {{ r: 96px; opacity: 0.9; stroke-width: 2px; }}
      50% {{ opacity: 0.5; }}
      100% {{ r: 148px; opacity: 0; stroke-width: 0.5px; }}
    }}

    @keyframes textFadeIn {{
      from {{ opacity: 0; transform: translateX(-6px); }}
      to {{ opacity: 1; transform: translateX(0); }}
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

    /* Animation Assignment */
    .modal-container {{
      transform-origin: 600px 340px;
      animation: modalPopUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
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

    .type-line-1 {{ animation: textFadeIn 0.35s ease forwards; animation-delay: 0.4s; opacity: 0; }}
    .type-line-2 {{ animation: textFadeIn 0.35s ease forwards; animation-delay: 0.65s; opacity: 0; }}
    .type-line-3 {{ animation: textFadeIn 0.35s ease forwards; animation-delay: 0.9s; opacity: 0; }}
    .type-line-4 {{ animation: textFadeIn 0.35s ease forwards; animation-delay: 1.15s; opacity: 0; }}
    .chips-group {{ animation: textFadeIn 0.4s ease forwards; animation-delay: 1.35s; opacity: 0; }}
    .buttons-group {{ animation: textFadeIn 0.4s ease forwards; animation-delay: 1.55s; opacity: 0; }}

    .cursor {{ animation: blinkCursor 0.8s infinite; }}

    /* Button Hovers */
    .btn-interactive {{
      cursor: pointer;
      transition: all 0.25s ease;
    }}
    .btn-interactive:hover {{
      filter: url(#neon-glow);
    }}

    /* Soundwave equalizer bars */
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
  <rect x="2" y="2" width="1196" height="676" rx="14" fill="none" stroke="#0E332B" stroke-width="1.5" />

  <!-- Full-Screen Laser Scan Line -->
  <g class="scan-beam">
    <line x1="0" y1="0" x2="1200" y2="0" stroke="url(#neon-emerald)" stroke-width="2" opacity="0.75" filter="url(#neon-glow)" />
    <polygon points="0,0 1200,0 1200,-25 0,-25" fill="url(#neon-emerald)" opacity="0.08" />
  </g>

  <!-- Floating Matrix Micro-Nodes -->
  <circle cx="120" cy="90" r="1.5" fill="#39F59A" opacity="0.6" />
  <circle cx="1080" cy="110" r="1.5" fill="#20D9D2" opacity="0.7" />
  <circle cx="80" cy="590" r="1.5" fill="#20D9D2" opacity="0.5" />
  <circle cx="1120" cy="560" r="1.5" fill="#39F59A" opacity="0.6" />

  <!-- ======================================================== -->
  <!-- 2. THE MODAL POP-UP WINDOW                               -->
  <!-- ======================================================== -->
  <g class="modal-container">
    <!-- Pop-up Window Outer Shadow / Glow Halo -->
    <rect x="76" y="36" width="1048" height="608" rx="20" fill="none" stroke="#39F59A" stroke-width="3" opacity="0.25" filter="url(#neon-glow)" />
    
    <!-- Pop-up Window Main Glass Box -->
    <rect x="80" y="40" width="1040" height="600" rx="18" fill="url(#modal-glass)" stroke="#1A574C" stroke-width="1.8" />

    <!-- Secondary Inner Accent Line -->
    <rect x="84" y="44" width="1032" height="592" rx="14" fill="none" stroke="#20D9D2" stroke-width="0.8" opacity="0.3" />

    <!-- Corner Cyber HUD Brackets -->
    <!-- Top-Left Bracket -->
    <path d="M 80 75 L 80 40 L 115 40" fill="none" stroke="#39F59A" stroke-width="3" />
    <circle cx="92" cy="52" r="2" fill="#39F59A" />

    <!-- Top-Right Bracket -->
    <path d="M 1085 40 L 1120 40 L 1120 75" fill="none" stroke="#39F59A" stroke-width="3" />
    <circle cx="1108" cy="52" r="2" fill="#39F59A" />

    <!-- Bottom-Left Bracket -->
    <path d="M 80 605 L 80 640 L 115 640" fill="none" stroke="#20D9D2" stroke-width="3" />
    <circle cx="92" cy="628" r="2" fill="#20D9D2" />

    <!-- Bottom-Right Bracket -->
    <path d="M 1085 640 L 1120 640 L 1120 605" fill="none" stroke="#20D9D2" stroke-width="3" />
    <circle cx="1108" cy="628" r="2" fill="#20D9D2" />

    <!-- ======================================================== -->
    <!-- 3. MODAL WINDOW HEADER BAR (OS CHROME)                   -->
    <!-- ======================================================== -->
    <path d="M 80 58 Q 80 40 98 40 L 1102 40 Q 1120 40 1120 58 L 1120 84 L 80 84 Z" fill="#081E1C" />
    <line x1="80" y1="84" x2="1120" y2="84" stroke="#1A574C" stroke-width="1.5" />

    <!-- Mac Traffic Light Buttons with Neon Glow -->
    <circle cx="110" cy="62" r="6.5" fill="#FF5F56" />
    <circle cx="132" cy="62" r="6.5" fill="#FFBD2E" />
    <circle cx="154" cy="62" r="6.5" fill="#27C93F" />

    <!-- Modal Title -->
    <text x="600" y="66" text-anchor="middle" class="font-mono" font-size="12" font-weight="700" fill="#9BAEAA" letter-spacing="1">
      ⚡ PACKHUNTER-OS v4.2 // SECURITY PROTOCOL: AUTHENTICATED // INCOMING_VISITOR_DETECTED
    </text>

    <!-- Header Right Buttons: Fullscreen & Status -->
    <rect x="910" y="52" width="86" height="20" rx="4" fill="#051416" stroke="#1C5E53" stroke-width="1" />
    <text x="953" y="66" text-anchor="middle" class="font-mono" font-size="9" font-weight="700" fill="#20D9D2">⛶ FULLSCREEN</text>

    <rect x="1004" y="52" width="98" height="20" rx="4" fill="#061F17" stroke="#39F59A" stroke-width="1" />
    <circle cx="1016" cy="62" r="3.5" fill="#39F59A" />
    <text x="1058" y="66" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">200 OK LIVE</text>

    <!-- ======================================================== -->
    <!-- 4. MODAL CONTENT: LEFT PANEL (CYBER WOLF AVATAR & RADAR) -->
    <!-- ======================================================== -->
    <!-- Left Background Glow -->
    <circle cx="240" cy="310" r="140" fill="#1C5E53" opacity="0.12" filter="url(#neon-glow)" />

    <!-- Sonar Radar Ping Wave -->
    <circle cx="240" cy="310" class="sonar-ping" fill="none" stroke="#39F59A" />

    <!-- Outer Rotating Targeting Reticle (Clockwise) -->
    <g class="reticle-cw">
      <circle cx="240" cy="310" r="126" fill="none" stroke="#1C5E53" stroke-dasharray="8 12 18 10" stroke-width="1.8" opacity="0.75" />
      <circle cx="240" cy="310" r="132" fill="none" stroke="#39F59A" stroke-dasharray="4 28" stroke-width="2.5" opacity="0.8" />
    </g>

    <!-- Inner Segmented Arc (Counter-Clockwise) -->
    <g class="reticle-ccw">
      <circle cx="240" cy="310" r="110" fill="none" stroke="#20D9D2" stroke-dasharray="16 22 8 22" stroke-width="1.5" opacity="0.65" />
    </g>

    <!-- Avatar Decorative Reticle Crosshairs -->
    <line x1="240" y1="166" x2="240" y2="182" stroke="#39F59A" stroke-width="2" />
    <line x1="240" y1="438" x2="240" y2="454" stroke="#39F59A" stroke-width="2" />
    <line x1="96" y1="310" x2="112" y2="310" stroke="#20D9D2" stroke-width="2" />
    <line x1="368" y1="310" x2="384" y2="310" stroke="#20D9D2" stroke-width="2" />

    <!-- Masked Cyber Wolf Avatar Image (Base64 Retina 360x360 rendered at 184x184) -->
    <image href="data:image/png;base64,{avatar_b64}" x="148" y="218" width="184" height="184" clip-path="url(#avatar-clip)" preserveAspectRatio="xMidYMid slice" />

    <!-- Avatar Inner & Outer Neon Glow Borders -->
    <circle cx="240" cy="310" r="92" fill="none" stroke="#39F59A" stroke-width="3" filter="url(#subtle-glow)" />
    <circle cx="240" cy="310" r="95" fill="none" stroke="#20D9D2" stroke-width="1.2" opacity="0.8" />

    <!-- Holographic Avatar HUD Pill -->
    <rect x="156" y="416" width="168" height="22" rx="11" fill="#071B19" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="170" cy="427" r="3.5" fill="#39F59A" />
    <text x="244" y="431" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="700" fill="#39F59A" letter-spacing="0.5">
      CYBER WOLF AI CORE
    </text>

    <!-- Animated Audio Equalizer Visualizer (Musica WebRTC Stream) -->
    <g transform="translate(176, 5)">
      <rect class="eq-1" x="0" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-2" x="12" y="446" width="6" height="4" rx="2" fill="#20D9D2" />
      <rect class="eq-3" x="24" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-4" x="36" y="446" width="6" height="4" rx="2" fill="#20D9D2" />
      <rect class="eq-5" x="48" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-6" x="60" y="446" width="6" height="4" rx="2" fill="#20D9D2" />
      <rect class="eq-7" x="72" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-8" x="84" y="446" width="6" height="4" rx="2" fill="#20D9D2" />
      <rect class="eq-9" x="96" y="446" width="6" height="4" rx="2" fill="#39F59A" />
      <rect class="eq-10" x="108" y="446" width="6" height="4" rx="2" fill="#20D9D2" />
    </g>

    <!-- Live Stream Sub-label -->
    <text x="240" y="482" text-anchor="middle" class="font-mono" font-size="9.5" fill="#9BAEAA">
      Musica Zero-DB • 96kHz / 24-bit Stereo
    </text>
    <text x="240" y="498" text-anchor="middle" class="font-mono" font-size="9" fill="#20D9D2">
      Latency: &lt;18ms • WebRTC Transport
    </text>

    <!-- Vertical Panel Divider -->
    <line x1="410" y1="104" x2="410" y2="580" stroke="#143D36" stroke-width="1.2" stroke-dasharray="4 4" />

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
    <text x="434" y="196" class="font-sans" font-size="16" font-weight="700" fill="#39F59A">
      Robinson J.
      <tspan font-weight="400" fill="#9BAEAA"> — Full-Stack Engineer &amp; System Architect</tspan>
    </text>

    <!-- Terminal Output Box -->
    <rect x="434" y="216" width="644" height="196" rx="10" fill="url(#term-box-bg)" stroke="#1A574C" stroke-width="1.2" />
    <path d="M 434 226 Q 434 216 444 216 L 1068 216 Q 1078 216 1078 226 L 1078 244 L 434 244 Z" fill="#081E1C" />
    <line x1="434" y1="244" x2="1078" y2="244" stroke="#1A574C" stroke-width="1" />
    <circle cx="452" cy="230" r="4" fill="#FF5F56" />
    <circle cx="466" cy="230" r="4" fill="#FFBD2E" />
    <circle cx="480" cy="230" r="4" fill="#27C93F" />
    <text x="500" y="234" class="font-mono" font-size="10" fill="#9BAEAA">terminal@packhunter-cynic: ~ /welcome_boot.sh</text>

    <!-- Animated Terminal Lines -->
    <!-- Line 1: Command & Auth -->
    <g class="type-line-1" transform="translate(452, 270)">
      <text x="0" y="0" class="font-mono" font-size="12" font-weight="700" fill="#39F59A">➜</text>
      <text x="16" y="0" class="font-mono" font-size="12" font-weight="600" fill="#20D9D2">~/system</text>
      <text x="96" y="0" class="font-mono" font-size="12" fill="#F4F7F6">./init_handshake.sh --target=visitor --mode=full_access</text>
    </g>

    <!-- Line 2: Identity Verification -->
    <g class="type-line-2" transform="translate(452, 302)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[AUTH: 0.18s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#F4F7F6">Profile: </text>
      <text x="168" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#39F59A">PackhunterforCynic (Robinson J.)</text>
      <text x="435" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">• MCA '25 • Bengaluru</text>
    </g>

    <!-- Line 3: System Pipeline -->
    <g class="type-line-3" transform="translate(452, 334)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[CORE: 0.44s]</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" fill="#20D9D2">WebSockets/WebRTC</text>
      <text x="260" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="275" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Phaser 4 Engine</text>
      <text x="400" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="415" y="0" class="font-mono" font-size="11.5" fill="#20D9D2">Gemini AI</text>
      <text x="495" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">|</text>
      <text x="510" y="0" class="font-mono" font-size="11.5" fill="#39F59A">Lighthouse 99</text>
    </g>

    <!-- Line 4: Status Ready -->
    <g class="type-line-4" transform="translate(452, 366)">
      <text x="0" y="0" class="font-mono" font-size="11.5" fill="#9BAEAA">[STATUS]</text>
      <rect x="75" y="-12" width="22" height="15" rx="3" fill="#0A3326" />
      <text x="80" y="0" class="font-mono" font-size="11" font-weight="900" fill="#39F59A">✓</text>
      <text x="105" y="0" class="font-mono" font-size="11.5" font-weight="700" fill="#39F59A">200 OK — 24 Repositories &amp; 6 Production Demos Ready</text>
      <text x="540" y="0" class="font-mono cursor" font-size="14" font-weight="900" fill="#39F59A">_</text>
    </g>

    <!-- Interactive Domain Chips Bar -->
    <g class="chips-group" transform="translate(434, 428)">
      <!-- Chip 1: WebRTC -->
      <rect x="0" y="0" width="120" height="26" rx="6" fill="#07221C" stroke="#1C5E53" stroke-width="1" />
      <text x="60" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">📡 WebRTC / P2P</text>

      <!-- Chip 2: AI / ML -->
      <rect x="128" y="0" width="136" height="26" rx="6" fill="#07221C" stroke="#1C5E53" stroke-width="1" />
      <text x="196" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#20D9D2">🧠 Gemini AI / RAG</text>

      <!-- Chip 3: Game Dev -->
      <rect x="272" y="0" width="126" height="26" rx="6" fill="#07221C" stroke="#1C5E53" stroke-width="1" />
      <text x="335" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🎮 Phaser 4 2D</text>

      <!-- Chip 4: Next.js -->
      <rect x="406" y="0" width="112" height="26" rx="6" fill="#07221C" stroke="#1C5E53" stroke-width="1" />
      <text x="462" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#20D9D2">⚡ Next.js App</text>

      <!-- Chip 5: Docker -->
      <rect x="526" y="0" width="118" height="26" rx="6" fill="#07221C" stroke="#1C5E53" stroke-width="1" />
      <text x="585" y="17" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">🐳 Docker Core</text>
    </g>

    <!-- High-Impact Action Buttons at Bottom of Pop-up -->
    <g class="buttons-group" transform="translate(434, 474)">
      <!-- Primary Button: Enter Workstation Dashboard -->
      <g class="btn-interactive" filter="url(#subtle-glow)">
        <rect x="0" y="0" width="330" height="46" rx="8" fill="url(#btn-primary-grad)" />
        <text x="165" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="800" fill="#040C0E" letter-spacing="0.3">
          🚀 ENTER WORKSTATION DASHBOARD ↘
        </text>
      </g>

      <!-- Secondary Button: Launch Live Full-Screen Portfolio -->
      <g class="btn-interactive">
        <rect x="344" y="0" width="300" height="46" rx="8" fill="#071E1C" stroke="#20D9D2" stroke-width="1.5" />
        <text x="494" y="28" text-anchor="middle" class="font-sans" font-size="13" font-weight="700" fill="#20D9D2" letter-spacing="0.3">
          🌐 OPEN LIVE WEB PORTFOLIO ↗
        </text>
      </g>
    </g>

    <!-- Bottom Status Strip of Pop-up Modal -->
    <rect x="80" y="604" width="1040" height="36" rx="0" fill="#040F11" />
    <line x1="80" y1="604" x2="1120" y2="604" stroke="#143D36" stroke-width="1" />
    <circle cx="106" cy="622" r="3" fill="#39F59A" />
    <text x="120" y="626" class="font-mono" font-size="10" fill="#9BAEAA">
      SECURE PROTOCOL ACTIVE • CLICK BANNER OR SCROLL DOWN TO EXPLORE DASHBOARD &amp; PRODUCTION PROJECTS
    </text>
    <text x="1090" y="626" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#39F59A">
      ▼ SCROLL TO EXPLORE
    </text>
  </g>
</svg>
'''

output_path = 'assets/welcome_popup.svg'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f"Successfully generated {output_path}, size: {os.path.getsize(output_path)} bytes")
