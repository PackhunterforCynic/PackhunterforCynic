import os

def create_tech_arsenal():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 320" width="100%" height="100%">
  <defs>
    <linearGradient id="arsenal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E1C" />
      <stop offset="50%" stop-color="#051416" />
      <stop offset="100%" stop-color="#02090B" />
    </linearGradient>
    <linearGradient id="bar-emerald" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#20D9D2" />
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
  <rect x="2" y="2" width="1096" height="316" rx="14" fill="url(#arsenal-bg)" stroke="#174D43" stroke-width="1.5" />
  
  <!-- Header Bar -->
  <path d="M 2 16 Q 2 2 16 2 L 1084 2 Q 1098 2 1098 16 L 1098 44 L 2 44 Z" fill="#09221F" />
  <line x1="2" y1="44" x2="1098" y2="44" stroke="#174D43" stroke-width="1.2" />

  <circle cx="20" cy="23" r="4.5" fill="#39F59A" />
  <circle cx="34" cy="23" r="4.5" fill="#20D9D2" />
  <text x="48" y="27" class="font-mono" font-size="11" font-weight="700" fill="#9BAEAA">
    ⚡ SYSTEM CAPABILITIES // CORE ENGINEERING ARSENAL &amp; ARCHITECTURE
  </text>
  <rect x="970" y="13" width="112" height="20" rx="4" fill="#061F17" stroke="#39F59A" stroke-width="1" />
  <text x="1026" y="27" text-anchor="middle" class="font-mono" font-size="9.5" font-weight="800" fill="#39F59A">VERIFIED 2026</text>

  <!-- 4 Columns Grid -->
  <!-- Col 1: Real-Time & Protocols -->
  <g transform="translate(32, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#39F59A">01 // REAL-TIME MESH</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#174D43" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">WebRTC (P2P Audio/Video)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">WebSockets &amp; Socket.IO</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Zero-DB Volatile State Core</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Web Audio API Synthesis</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">REST &amp; Streaming Protocols</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>
  </g>

  <!-- Vertical Divider 1 -->
  <line x1="288" y1="64" x2="288" y2="260" stroke="#143D36" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 2: Languages & Runtime -->
  <g transform="translate(308, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#20D9D2">02 // LANGUAGES &amp; RUNTIME</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#174D43" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">TypeScript &amp; JavaScript</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Python (FastAPI &amp; ML)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Node.js &amp; Bun Runtime</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="205" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">SQL &amp; PostgreSQL Engine</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">C++ / Object-Oriented</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="170" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>
  </g>

  <!-- Vertical Divider 2 -->
  <line x1="564" y1="64" x2="564" y2="260" stroke="#143D36" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 3: AI & Web Engines -->
  <g transform="translate(584, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#39F59A">03 // AI &amp; GAME ENGINES</text>
    <line x1="0" y1="8" x2="230" y2="8" stroke="#174D43" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Next.js App Router (v15)</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="210" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">React 19 &amp; Tailwind CSS v4</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="215" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Gemini Vision AI Pipeline</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">ChromaDB Vector RAG</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Phaser 4 &amp; GSAP 2D</text>
      <rect x="0" y="16" width="220" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="185" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>
  </g>

  <!-- Vertical Divider 3 -->
  <line x1="840" y1="64" x2="840" y2="260" stroke="#143D36" stroke-width="1" stroke-dasharray="4 4" />

  <!-- Col 4: Systems & DevOps -->
  <g transform="translate(860, 64)">
    <text x="0" y="0" class="font-mono" font-size="12" font-weight="800" fill="#20D9D2">04 // CLOUD &amp; SYSTEMS</text>
    <line x1="0" y1="8" x2="200" y2="8" stroke="#174D43" stroke-width="1" />

    <g class="tech-row" transform="translate(0, 24)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Docker &amp; Containerization</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 56)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Git &amp; GitHub Actions CI/CD</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 88)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Linux Shell Scripting</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="180" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 120)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Vercel Edge Network</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="195" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>

    <g class="tech-row" transform="translate(0, 152)">
      <text x="0" y="10" class="font-sans" font-size="11" font-weight="600" fill="#F4F7F6">Lighthouse 99 Auditing</text>
      <rect x="0" y="16" width="200" height="5" rx="2.5" fill="#0D2622" />
      <rect x="0" y="16" width="190" height="5" rx="2.5" fill="url(#bar-emerald)" />
    </g>
  </g>

  <!-- Bottom Status Strip -->
  <line x1="2" y1="280" x2="1098" y2="280" stroke="#174D43" stroke-width="1" />
  <circle cx="24" cy="298" r="3.5" fill="#39F59A" />
  <text x="36" y="302" class="font-mono" font-size="10" fill="#9BAEAA">
    CORE METRICS: 24 REPOSITORIES • 6 PRODUCTION SYSTEMS • HIGH-THROUGHPUT REAL-TIME ARCHITECTURE
  </text>
  <text x="1076" y="302" text-anchor="end" class="font-mono" font-size="10" font-weight="700" fill="#39F59A">
    ✓ 100% PURE VECTOR SVG
  </text>
</svg>
'''
    with open('assets/tech_arsenal.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/tech_arsenal.svg')

if __name__ == '__main__':
    create_tech_arsenal()
