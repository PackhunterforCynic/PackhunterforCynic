import os
import xml.etree.ElementTree as ET

# 1. Update nav_dock.svg
def update_nav_dock():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 80" width="100%" height="100%">
  <defs>
    <linearGradient id="dock-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#071924" />
      <stop offset="50%" stop-color="#040D14" />
      <stop offset="100%" stop-color="#02070B" />
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
      fill: #0A2638;
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

  <!-- Dock Outer Frame -->
  <rect x="2" y="2" width="1096" height="76" rx="14" fill="url(#dock-bg)" stroke="#12444C" stroke-width="1.5" />
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#dock-glow)" opacity="0.85" />

  <!-- Corner Brackets -->
  <path d="M 12 18 L 12 10 L 20 10" fill="none" stroke="#00F2FE" stroke-width="2" />
  <path d="M 1088 18 L 1088 10 L 1080 10" fill="none" stroke="#00F2FE" stroke-width="2" />
  <path d="M 12 62 L 12 70 L 20 70" fill="none" stroke="#FF9100" stroke-width="2" />
  <path d="M 1088 62 L 1088 70 L 1080 70" fill="none" stroke="#FF9100" stroke-width="2" />

  <!-- 5 High-Tech Dock Buttons -->
  <!-- Btn 1: Neural Core -->
  <g class="dock-btn" transform="translate(32, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">01 // NEURAL CORE</text>
  </g>

  <!-- Btn 2: Flagship Engines -->
  <g class="dock-btn" transform="translate(242, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" style="animation-delay: 0.4s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">02 // ENGINES &amp; P2P</text>
  </g>

  <!-- Btn 3: AI & Optics -->
  <g class="dock-btn" transform="translate(452, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" style="animation-delay: 0.8s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">03 // AI &amp; VISION</text>
  </g>

  <!-- Btn 4: Telemetry -->
  <g class="dock-btn" transform="translate(662, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#FF9100" class="led" style="animation-delay: 1.2s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">04 // TELEMETRY</text>
  </g>

  <!-- Btn 5: Uplink -->
  <g class="dock-btn" transform="translate(872, 16)">
    <rect x="0" y="0" width="196" height="48" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#00F2FE" class="led" style="animation-delay: 1.6s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">05 // SECURE UPLINK</text>
  </g>
</svg>
'''
    with open('assets/nav_dock.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/nav_dock.svg')

# 2. Update showcase_musica_game.svg
def update_showcase_musica_game():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" />
      <stop offset="60%" stop-color="#05131C" />
      <stop offset="100%" stop-color="#02090F" />
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

  <!-- Left Card: Musica Platform -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#12444C" stroke-width="1.2" />

    <!-- Status Dots -->
    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 01 // REAL-TIME MESH</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <!-- Project Title -->
    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">📡 Musica Audio Platform</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">Zero-DB WebSockets &amp; WebRTC real-time audio core</text>

    <!-- Vector WebRTC Wave & P2P Mesh Diagram -->
    <rect x="24" y="112" width="488" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <!-- P2P Peer 1 -->
    <circle cx="70" cy="158" r="14" fill="#082638" stroke="#00F2FE" stroke-width="2" />
    <circle cx="70" cy="158" r="6" fill="#00F2FE" />
    <circle cx="70" cy="158" class="ping-ring" fill="none" stroke="#00F2FE" stroke-width="1.5" />
    <text x="70" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#9BAEAA">PEER_A</text>

    <!-- Animated Data Waves -->
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

    <!-- Signaling WebSocket Cloud -->
    <rect x="200" y="138" width="130" height="40" rx="6" fill="#082638" stroke="#00F2FE" stroke-width="1.2" />
    <text x="265" y="155" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">WS SIGNALING</text>
    <text x="265" y="170" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">&lt;18ms LATENCY</text>

    <!-- Animated Data Waves Right -->
    <g transform="translate(350, 140)">
      <rect class="wave-bar" x="0" y="0" width="4" height="28" rx="2" fill="#00F2FE" style="animation-delay: 0.25s;" />
      <rect class="wave-bar" x="10" y="0" width="4" height="34" rx="2" fill="#39F59A" style="animation-delay: 0.1s;" />
      <rect class="wave-bar" x="20" y="0" width="4" height="20" rx="2" fill="#00F2FE" style="animation-delay: 0.4s;" />
      <rect class="wave-bar" x="30" y="0" width="4" height="36" rx="2" fill="#39F59A" style="animation-delay: 0.15s;" />
      <rect class="wave-bar" x="40" y="0" width="4" height="24" rx="2" fill="#00F2FE" style="animation-delay: 0.3s;" />
    </g>

    <!-- P2P Peer 2 -->
    <circle cx="465" cy="158" r="14" fill="#082638" stroke="#39F59A" stroke-width="2" />
    <circle cx="465" cy="158" r="6" fill="#39F59A" />
    <circle cx="465" cy="158" class="ping-ring" fill="none" stroke="#39F59A" stroke-width="1.5" style="animation-delay: 1s;" />
    <text x="465" y="186" text-anchor="middle" class="font-mono" font-size="9" fill="#9BAEAA">PEER_B</text>

    <!-- Tech Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="86" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="43" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="94" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="132" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Node.js</text>

      <rect x="178" y="0" width="80" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="218" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">WebRTC</text>

      <rect x="266" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="304" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Socket.IO</text>

      <rect x="350" y="0" width="68" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="384" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Docker</text>

      <rect x="426" y="0" width="86" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="469" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Zero-DB</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎧 musica-apvs.vercel.app ↗]  •  [github.com/PackhunterforCynic/musica ↗]
    </text>
  </g>

  <!-- Right Card: Ben 10 Alien Battle Arena -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#12444C" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 02 // DETERMINISTIC P2P</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE GAME</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">🎮 Ben 10: Alien Battle Arena</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">2D fighting engine in Phaser 4 with PeerJS direct multiplayer</text>

    <!-- Vector Arcade HUD & Game Loop Diagram -->
    <rect x="24" y="112" width="486" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <!-- Health Bar 1 -->
    <text x="40" y="134" class="font-mono" font-size="9.5" font-weight="700" fill="#39F59A">PLAYER 1 // FOURARMS</text>
    <rect x="40" y="140" width="180" height="10" rx="3" fill="#071924" stroke="#12444C" stroke-width="1" />
    <rect x="41" y="141" width="150" height="8" rx="2" fill="url(#glow-cyan)" />

    <!-- Health Bar 2 -->
    <text x="266" y="134" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">PLAYER 2 // HEATBLAST</text>
    <rect x="266" y="140" width="180" height="10" rx="3" fill="#071924" stroke="#12444C" stroke-width="1" />
    <rect x="267" y="141" width="130" height="8" rx="2" fill="#00F2FE" />

    <!-- Center Versus Radar -->
    <circle cx="242" cy="158" r="18" fill="#082638" stroke="#00F2FE" stroke-width="1.5" />
    <text x="242" y="162" text-anchor="middle" class="font-mono" font-size="11" font-weight="900" fill="#00F2FE">VS</text>

    <!-- Telemetry status inside diagram -->
    <text x="40" y="174" class="font-mono" font-size="9" fill="#9BAEAA">Canvas Tick: 60 FPS</text>
    <text x="40" y="188" class="font-mono" font-size="9" fill="#00F2FE">State Sync: Deterministic PeerJS</text>
    <text x="266" y="174" class="font-mono" font-size="9" fill="#9BAEAA">Audio: Web Audio API Synth</text>
    <text x="266" y="188" class="font-mono" font-size="9" fill="#39F59A">Zero Server Lag: Browser P2P</text>

    <!-- Tech Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="80" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="40" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Phaser 4</text>

      <rect x="88" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="126" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React 19</text>

      <rect x="172" y="0" width="90" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="217" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">TypeScript</text>

      <rect x="270" y="0" width="74" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="307" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PeerJS</text>

      <rect x="352" y="0" width="84" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="394" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Web Audio</text>

      <rect x="444" y="0" width="66" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="477" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">P2P Mesh</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎮 game-rovenor.vercel.app ↗]  •  [github.com/PackhunterforCynic/game ↗]
    </text>
  </g>
</svg>
'''
    with open('assets/showcase_musica_game.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/showcase_musica_game.svg')

# 3. Update showcase_ai_camx.svg
def update_showcase_ai_camx():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg-ai" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" />
      <stop offset="60%" stop-color="#05131C" />
      <stop offset="100%" stop-color="#02090F" />
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, monospace; }
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
  </style>

  <!-- Left Card: PlantSense AI -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg-ai)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#12444C" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 03 // VISION AI &amp; VECTOR RAG</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● FASTAPI LIVE</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">🌱 PlantSense Botanical AI</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">Gemini Vision AI multimodal pathology with ChromaDB vector RAG</text>

    <!-- Vector Neural Net & Vector Bounding Box -->
    <rect x="24" y="112" width="488" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <!-- Botanical Leaf Scan Bounding Box -->
    <rect x="40" y="124" width="70" height="68" rx="4" fill="#071924" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="4 4" />
    <path d="M 75 132 C 60 145 60 170 75 182 C 90 170 90 145 75 132 Z" fill="#0E332B" stroke="#39F59A" stroke-width="1.5" />
    <line x1="75" y1="135" x2="75" y2="180" stroke="#00F2FE" stroke-width="1.2" />
    <text x="75" y="198" text-anchor="middle" class="font-mono" font-size="8" fill="#00F2FE">99.4% CONF</text>

    <!-- Arrow to Neural Net -->
    <line x1="116" y1="158" x2="148" y2="158" stroke="#00F2FE" stroke-width="2" />

    <!-- Neural Synapse Nodes -->
    <g transform="translate(156, 126)">
      <circle cx="10" cy="14" r="5" fill="#39F59A" />
      <circle cx="10" cy="34" r="5" fill="#39F59A" />
      <circle cx="10" cy="54" r="5" fill="#39F59A" />
      <circle cx="50" cy="24" r="6" fill="#00F2FE" />
      <circle cx="50" cy="44" r="6" fill="#00F2FE" />
      <circle cx="90" cy="34" r="7" fill="#39F59A" />

      <line x1="10" y1="14" x2="50" y2="24" stroke="#12444C" stroke-width="1" />
      <line x1="10" y1="34" x2="50" y2="24" stroke="#12444C" stroke-width="1" />
      <line x1="10" y1="34" x2="50" y2="44" stroke="#12444C" stroke-width="1" />
      <line x1="10" y1="54" x2="50" y2="44" stroke="#12444C" stroke-width="1" />
      <line x1="50" y1="24" x2="90" y2="34" stroke="#39F59A" stroke-width="1.5" />
      <line x1="50" y1="44" x2="90" y2="34" stroke="#00F2FE" stroke-width="1.5" />
    </g>

    <!-- ChromaDB Vector RAG Box -->
    <rect x="270" y="126" width="160" height="64" rx="6" fill="#082638" stroke="#00F2FE" stroke-width="1.2" />
    <text x="350" y="146" text-anchor="middle" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">ChromaDB RAG</text>
    <text x="350" y="162" text-anchor="middle" class="font-mono" font-size="8.5" fill="#9BAEAA">Cosine Distance Metric</text>
    <text x="350" y="176" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">Instant Remedy Retrieval</text>

    <!-- Tech Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="70" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="35" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Python</text>

      <rect x="78" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="116" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">FastAPI</text>

      <rect x="162" y="0" width="86" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="205" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Gemini AI</text>

      <rect x="256" y="0" width="94" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="303" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">ChromaDB</text>

      <rect x="358" y="0" width="70" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="393" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">RAG Net</text>

      <rect x="436" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="474" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision AI</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🌱 robinsonj.vercel.app ↗]  •  [github.com/PackhunterforCynic ↗]
    </text>
  </g>

  <!-- Right Card: CAMX Digital Camera Lab -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg-ai)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#12444C" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 04 // OPTICS &amp; COMPUTER VISION</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● SHOWCASE</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">📷 CAMX Digital Camera Lab</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">Hands-free optics simulator with EV100, landmarks, voice commands</text>

    <!-- Vector Camera Aperture & Optics HUD -->
    <rect x="24" y="112" width="486" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <!-- Vector Camera Aperture Iris -->
    <g transform="translate(80, 158)">
      <circle cx="0" cy="0" r="32" fill="#082638" stroke="#12444C" stroke-width="1.5" />
      <polygon points="0,-24 16,-12 10,10 -12,18 -22,-2" fill="#071924" stroke="#00F2FE" stroke-width="1.2" />
      <circle cx="0" cy="0" r="10" fill="#02070B" stroke="#39F59A" stroke-width="1.5" />
      <text x="0" y="44" text-anchor="middle" class="font-mono" font-size="8.5" fill="#00F2FE">f/1.8 APERTURE</text>
    </g>

    <!-- Optics Telemetry -->
    <g transform="translate(145, 128)">
      <text x="0" y="14" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">EV100 Exposure: +1.3 EV</text>
      <text x="0" y="28" class="font-mono" font-size="9" fill="#9BAEAA">Focal Length: 50mm Equivalent</text>
      <text x="0" y="42" class="font-mono" font-size="9" fill="#39F59A">Facial Landmarks: 468 Points 3D</text>
      <text x="0" y="56" class="font-mono" font-size="9" fill="#9BAEAA">Voice Control: Web Speech API</text>
    </g>

    <g transform="translate(390, 138)">
      <rect x="0" y="0" width="84" height="42" rx="4" fill="#082638" stroke="#12444C" stroke-width="1" />
      <path d="M 6 28 Q 24 6 42 22 T 78 18" fill="none" stroke="#00F2FE" stroke-width="1.8" />
      <text x="42" y="36" text-anchor="middle" class="font-mono" font-size="7.5" fill="#39F59A">OPTICS CURVE</text>
    </g>

    <!-- Tech Badges -->
    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="90" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="45" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="98" y="0" width="80" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="138" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">WebRTC</text>

      <rect x="186" y="0" width="96" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="234" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Optics Physics</text>

      <rect x="290" y="0" width="86" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="333" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Voice API</text>

      <rect x="384" y="0" width="70" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="419" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vision Lab</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [📷 robinsonj.vercel.app ↗]  •  [github.com/PackhunterforCynic ↗]
    </text>
  </g>
</svg>
'''
    with open('assets/showcase_ai_camx.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/showcase_ai_camx.svg')

# 4. Update showcase_havilah_hse.svg
def update_showcase_havilah_hse():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 290" width="100%" height="100%">
  <defs>
    <linearGradient id="card-bg-web" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" />
      <stop offset="60%" stop-color="#05131C" />
      <stop offset="100%" stop-color="#02090F" />
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

  <!-- Left Card: Havilah Studio -->
  <g transform="translate(0, 0)">
    <rect x="2" y="2" width="536" height="284" rx="14" fill="url(#card-bg-web)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 522 2 Q 536 2 536 16 L 536 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="538" y2="44" stroke="#12444C" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 05 // CINEMATIC MULTIMEDIA</text>
    <rect x="420" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="471" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">🎥 Havilah Studio Portfolio</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">Cinematic multimedia portfolio powered by Bun runtime &amp; GSAP</text>

    <rect x="24" y="112" width="488" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <line x1="40" y1="145" x2="480" y2="145" stroke="#12444C" stroke-width="2" />
    <circle cx="160" cy="145" r="7" fill="#00F2FE" />
    <circle cx="280" cy="145" r="7" fill="#39F59A" />
    <circle cx="400" cy="145" r="7" fill="#00F2FE" />
    <path d="M 40 165 C 100 135 180 185 280 145 C 380 105 440 165 480 135" fill="none" stroke="#00F2FE" stroke-width="1.8" />
    <text x="40" y="186" class="font-mono" font-size="9" fill="#9BAEAA">GSAP Smooth Tweens • 60 FPS • Bun High-Throughput Bundling</text>

    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="86" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="43" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">TypeScript</text>

      <rect x="94" y="0" width="60" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="124" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Bun</text>

      <rect x="162" y="0" width="68" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="196" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">React</text>

      <rect x="238" y="0" width="66" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="271" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">GSAP</text>

      <rect x="312" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="350" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Vercel</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎥 havilah-alpha.vercel.app ↗]  •  [github.com/PackhunterforCynic/havilah ↗]
    </text>
  </g>

  <!-- Right Card: HSE Media Suite -->
  <g transform="translate(562, 0)">
    <rect x="2" y="2" width="534" height="284" rx="14" fill="url(#card-bg-web)" stroke="#12444C" stroke-width="1.5" />
    <path d="M 2 16 Q 2 2 16 2 L 520 2 Q 534 2 534 16 L 534 44 L 2 44 Z" fill="#061824" />
    <line x1="2" y1="44" x2="536" y2="44" stroke="#12444C" stroke-width="1.2" />

    <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
    <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
    <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">ENGINE 06 // LIGHTHOUSE 99 PERFORMANCE</text>
    <rect x="418" y="13" width="102" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
    <text x="469" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">● LIVE DEMO</text>

    <text x="24" y="78" class="font-sans" font-size="21" font-weight="800" fill="#F4F7F6">🎬 HSE Media Production Suite</text>
    <text x="24" y="98" class="font-sans" font-size="12" fill="#9BAEAA">Next.js App Router multi-media engine with automated audits</text>

    <rect x="24" y="112" width="486" height="92" rx="8" fill="#030C12" stroke="#103B47" stroke-width="1" />
    
    <g transform="translate(70, 158)">
      <circle cx="0" cy="0" r="30" fill="none" stroke="#103B47" stroke-width="5" />
      <circle cx="0" cy="0" r="30" fill="none" stroke="url(#score-ring-hse)" stroke-width="5" stroke-dasharray="182 8" stroke-linecap="round" />
      <text x="0" y="8" text-anchor="middle" class="font-sans" font-size="18" font-weight="900" fill="#00F2FE">99</text>
      <text x="0" y="44" text-anchor="middle" class="font-mono" font-size="8.5" fill="#39F59A">LIGHTHOUSE</text>
    </g>

    <g transform="translate(130, 130)">
      <text x="0" y="14" class="font-mono" font-size="9.5" font-weight="700" fill="#00F2FE">Next.js App Router: Dynamic Edge Cache</text>
      <text x="0" y="28" class="font-mono" font-size="9" fill="#9BAEAA">SEO Score: 100 • Accessibility: 100</text>
      <text x="0" y="42" class="font-mono" font-size="9" fill="#39F59A">Lighthouse Performance: 99 Verified</text>
      <text x="0" y="56" class="font-mono" font-size="9" fill="#9BAEAA">Tailwind CSS v4 • Continuous Auditing</text>
    </g>

    <g transform="translate(24, 218)">
      <rect x="0" y="0" width="80" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="40" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Next.js</text>

      <rect x="88" y="0" width="80" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="128" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Tailwind</text>

      <rect x="176" y="0" width="60" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="206" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">PHP</text>

      <rect x="244" y="0" width="76" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="282" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#39F59A">Vercel</text>

      <rect x="328" y="0" width="94" height="24" rx="5" fill="#071924" stroke="#12444C" stroke-width="1" />
      <text x="375" y="16" text-anchor="middle" class="font-mono" font-size="10" font-weight="600" fill="#00F2FE">Score 99</text>
    </g>

    <text x="24" y="266" class="font-mono" font-size="10.5" font-weight="700" fill="#00F2FE">
      [🎬 hse-indol.vercel.app ↗]  •  [github.com/PackhunterforCynic/hse ↗]
    </text>
  </g>
</svg>
'''
    with open('assets/showcase_havilah_hse.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/showcase_havilah_hse.svg')

# 5. Update tech_arsenal.svg
def update_tech_arsenal():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 320" width="100%" height="100%">
  <defs>
    <linearGradient id="arsenal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" />
      <stop offset="50%" stop-color="#05131C" />
      <stop offset="100%" stop-color="#02090F" />
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

  <!-- Container Box -->
  <rect x="2" y="2" width="1096" height="316" rx="14" fill="url(#arsenal-bg)" stroke="#12444C" stroke-width="1.5" />
  
  <!-- Header Bar -->
  <path d="M 2 16 Q 2 2 16 2 L 1084 2 Q 1098 2 1098 16 L 1098 44 L 2 44 Z" fill="#061824" />
  <line x1="2" y1="44" x2="1098" y2="44" stroke="#12444C" stroke-width="1.2" />

  <circle cx="20" cy="23" r="4.5" fill="#00F2FE" />
  <circle cx="34" cy="23" r="4.5" fill="#39F59A" />
  <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">
    ⚡ SYSTEM CAPABILITIES // CORE ENGINEERING ARSENAL &amp; ARCHITECTURE
  </text>
  <rect x="970" y="13" width="112" height="20" rx="4" fill="#06221B" stroke="#39F59A" stroke-width="1" />
  <text x="1026" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">VERIFIED 2026</text>

  <!-- 4 Columns Grid -->
  <!-- Col 1: Real-Time & Protocols -->
  <g transform="translate(32, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#00F2FE">01 // REAL-TIME MESH</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#12444C" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">WebRTC (P2P Audio/Video)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">WebSockets &amp; Socket.IO</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Zero-DB Volatile State Core</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Web Audio API Synthesis</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">REST &amp; Streaming Protocols</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <!-- Vertical Divider 1 -->
  <line x1="288" y1="64" x2="288" y2="260" stroke="#12444C" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 2: Languages & Runtime -->
  <g transform="translate(308, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#39F59A">02 // LANGUAGES &amp; RUNTIME</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#12444C" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">TypeScript &amp; JavaScript</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Python (FastAPI &amp; ML)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Node.js &amp; Bun Runtime</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="205" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">SQL &amp; PostgreSQL Engine</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">C++ / Object-Oriented</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="170" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <!-- Vertical Divider 2 -->
  <line x1="564" y1="64" x2="564" y2="260" stroke="#12444C" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 3: AI & Web Engines -->
  <g transform="translate(584, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#00F2FE">03 // AI &amp; GAME ENGINES</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#12444C" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Next.js App Router (v15)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">React 19 &amp; Tailwind CSS v4</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Gemini Vision AI Pipeline</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">ChromaDB Vector RAG</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Phaser 4 &amp; GSAP 2D</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <!-- Vertical Divider 3 -->
  <line x1="840" y1="64" x2="840" y2="260" stroke="#12444C" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 4: Systems & DevOps -->
  <g transform="translate(860, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#FF9100">04 // CLOUD &amp; SYSTEMS</text>
    <line x1="0" y1="8" x2="200" y2="8" stroke="#12444C" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Docker &amp; Containerization</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Git &amp; GitHub Actions CI/CD</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Linux Shell Scripting</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Vercel Edge Network</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Lighthouse 99 Auditing</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#071924" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-cyan)" />
    </g>
  </g>

  <!-- Bottom Status Strip -->
  <line x1="2" y1="280" x2="1098" y2="280" stroke="#12444C" stroke-width="1" />
  <circle cx="24" cy="298" r="3.5" fill="#00F2FE" />
  <text x="36" y="302" class="font-mono" font-size="10" fill="#9BAEAA">
    CORE METRICS: 24 REPOSITORIES • 6 PRODUCTION SYSTEMS • HIGH-THROUGHPUT REAL-TIME ARCHITECTURE
  </text>
  <text x="1076" y="302" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#00F2FE">
    ✓ 100% PURE VECTOR SVG
  </text>
</svg>
'''
    with open('assets/tech_arsenal.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/tech_arsenal.svg')

# 6. Update footer_uplink.svg
def update_footer_uplink():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 110" width="100%" height="100%">
  <defs>
    <linearGradient id="footer-bg-nexus" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E2B" />
      <stop offset="50%" stop-color="#05131C" />
      <stop offset="100%" stop-color="#02090F" />
    </linearGradient>
    <linearGradient id="neon-glow-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.2" />
      <stop offset="30%" stop-color="#00F2FE" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#39F59A" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#FF9100" stop-opacity="0.2" />
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

  <!-- Container Box -->
  <rect x="2" y="2" width="1096" height="106" rx="14" fill="url(#footer-bg-nexus)" stroke="#12444C" stroke-width="1.5" />
  
  <!-- Top Neon Line -->
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#neon-glow-line)" />

  <!-- Left: Signature & Credential -->
  <g transform="translate(32, 38)">
    <circle cx="8" cy="8" r="5" fill="#00F2FE" class="pulse-dot" />
    <text x="24" y="12" class="font-mono" font-size="14" font-weight="800" fill="#F4F7F6" letter-spacing="1">
      ROBINSON J. // PACKHUNTERFORCYNIC
    </text>
    <text x="24" y="32" class="font-sans" font-size="11.5" fill="#9BAEAA">
      Engineered for Scale, Low-Latency WebRTC &amp; High-Throughput System Architecture
    </text>
    <text x="24" y="48" class="font-mono" font-size="9.5" fill="#00F2FE">
      Verified Identity: MCA '25 • Bengaluru, Karnataka, India • 24 Verified Repositories
    </text>
  </g>

  <!-- Right: Verification & End-of-Stream Badge -->
  <g transform="translate(820, 30)">
    <rect x="0" y="0" width="248" height="52" rx="8" fill="#061824" stroke="#12444C" stroke-width="1.2" />
    <circle cx="20" cy="26" r="6" fill="#00F2FE" />
    <text x="36" y="22" class="font-mono" font-size="11" font-weight="800" fill="#00F2FE">200 OK — ALL ONLINE</text>
    <text x="36" y="38" class="font-mono" font-size="9" fill="#9BAEAA">PACKHUNTER-OS v5.0 // PURE SVG</text>
  </g>
</svg>
'''
    with open('assets/footer_uplink.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Updated assets/footer_uplink.svg')

if __name__ == '__main__':
    update_nav_dock()
    update_showcase_musica_game()
    update_showcase_ai_camx()
    update_showcase_havilah_hse()
    update_tech_arsenal()
    update_footer_uplink()
