import os

def create_footer_uplink():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 110" width="100%" height="100%">
  <defs>
    <linearGradient id="footer-bg-nexus" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#081E1C" />
      <stop offset="50%" stop-color="#051416" />
      <stop offset="100%" stop-color="#02090B" />
    </linearGradient>
    <linearGradient id="neon-glow-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#39F59A" stop-opacity="0.2" />
      <stop offset="30%" stop-color="#39F59A" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#20D9D2" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#20D9D2" stop-opacity="0.2" />
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
  <rect x="2" y="2" width="1096" height="106" rx="14" fill="url(#footer-bg-nexus)" stroke="#174D43" stroke-width="1.5" />
  
  <!-- Top Neon Line -->
  <rect x="15" y="2" width="1070" height="2" rx="1" fill="url(#neon-glow-line)" />

  <!-- Left: Signature & Credential -->
  <g transform="translate(32, 38)">
    <circle cx="8" cy="8" r="5" fill="#39F59A" class="pulse-dot" />
    <text x="24" y="12" class="font-mono" font-size="14" font-weight="800" fill="#F4F7F6" letter-spacing="1">
      ROBINSON J. // PACKHUNTERFORCYNIC
    </text>
    <text x="24" y="32" class="font-sans" font-size="11.5" fill="#9BAEAA">
      Engineered for Scale, Low-Latency WebRTC &amp; High-Throughput System Architecture
    </text>
    <text x="24" y="48" class="font-mono" font-size="9.5" fill="#20D9D2">
      Verified Identity: MCA '25 • Bengaluru, Karnataka, India • 24 Verified Repositories
    </text>
  </g>

  <!-- Right: Verification & End-of-Stream Badge -->
  <g transform="translate(820, 30)">
    <rect x="0" y="0" width="248" height="52" rx="8" fill="#08221D" stroke="#1A574C" stroke-width="1.2" />
    <circle cx="20" cy="26" r="6" fill="#39F59A" />
    <text x="36" y="22" class="font-mono" font-size="11" font-weight="800" fill="#39F59A">200 OK — ALL ONLINE</text>
    <text x="36" y="38" class="font-mono" font-size="9" fill="#9BAEAA">PACKHUNTER-OS v5.0 // PURE SVG</text>
  </g>
</svg>
'''
    with open('assets/footer_uplink.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/footer_uplink.svg')

if __name__ == '__main__':
    create_footer_uplink()
