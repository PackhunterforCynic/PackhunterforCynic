import os

def create_nav_dock():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 80" width="100%" height="100%">
  <defs>
    <linearGradient id="dock-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E1C" />
      <stop offset="50%" stop-color="#040F11" />
      <stop offset="100%" stop-color="#020809" />
    </linearGradient>
    <linearGradient id="dock-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#39F59A" />
      <stop offset="50%" stop-color="#20D9D2" />
      <stop offset="100%" stop-color="#39F59A" />
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
      fill: #0B2B24;
      stroke: #39F59A;
      filter: url(#btn-glow);
    }
    .dock-btn:hover text {
      fill: #39F59A;
    }

    @keyframes pulseLed {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.9); }
    }
    .led { animation: pulseLed 2s infinite ease-in-out; }
  </style>

  <!-- Dock Outer Frame -->
  <rect x="2" y="2" width="1096" height="76" rx="14" fill="url(#dock-bg)" stroke="#174D43" stroke-width="1.5" />
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#dock-glow)" opacity="0.8" />

  <!-- Corner Brackets -->
  <path d="M 12 18 L 12 10 L 20 10" fill="none" stroke="#39F59A" stroke-width="2" />
  <path d="M 1088 18 L 1088 10 L 1080 10" fill="none" stroke="#39F59A" stroke-width="2" />
  <path d="M 12 62 L 12 70 L 20 70" fill="none" stroke="#20D9D2" stroke-width="2" />
  <path d="M 1088 62 L 1088 70 L 1080 70" fill="none" stroke="#20D9D2" stroke-width="2" />

  <!-- 5 High-Tech Dock Buttons -->
  <!-- Btn 1: Neural Core -->
  <g class="dock-btn" transform="translate(32, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#07181A" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">01 // NEURAL CORE</text>
  </g>

  <!-- Btn 2: Flagship Engines -->
  <g class="dock-btn" transform="translate(242, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#07181A" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#20D9D2" class="led" style="animation-delay: 0.4s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">02 // ENGINES &amp; P2P</text>
  </g>

  <!-- Btn 3: AI & Optics -->
  <g class="dock-btn" transform="translate(452, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#07181A" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" style="animation-delay: 0.8s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">03 // AI &amp; VISION</text>
  </g>

  <!-- Btn 4: Telemetry -->
  <g class="dock-btn" transform="translate(662, 16)">
    <rect x="0" y="0" width="194" height="48" rx="8" fill="#07181A" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#20D9D2" class="led" style="animation-delay: 1.2s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">04 // TELEMETRY</text>
  </g>

  <!-- Btn 5: Uplink -->
  <g class="dock-btn" transform="translate(872, 16)">
    <rect x="0" y="0" width="196" height="48" rx="8" fill="#07181A" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="22" cy="24" r="5" fill="#39F59A" class="led" style="animation-delay: 1.6s;" />
    <text x="36" y="28" class="font-mono" font-size="12" font-weight="700" fill="#F4F7F6">05 // SECURE UPLINK</text>
  </g>
</svg>
'''
    with open('assets/nav_dock.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/nav_dock.svg')

if __name__ == '__main__':
    create_nav_dock()
