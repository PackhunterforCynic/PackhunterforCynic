import os
from generate_vector_wolf import generate_cyber_wolf_svg

wolf_geom = generate_cyber_wolf_svg(cx=200, cy=200)

svg_doc = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%" height="100%">
  <defs>
    <radialGradient id="wolf-bg" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#0E2E28" />
      <stop offset="60%" stop-color="#061614" />
      <stop offset="100%" stop-color="#020808" />
    </radialGradient>
    <filter id="eye-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <rect width="400" height="400" rx="20" fill="url(#wolf-bg)" stroke="#174D43" stroke-width="2" />
  
  <!-- Cyber Radar Rings -->
  <circle cx="200" cy="200" r="160" fill="none" stroke="#174D43" stroke-width="1" stroke-dasharray="8 8" opacity="0.6" />
  <circle cx="200" cy="200" r="180" fill="none" stroke="#39F59A" stroke-width="1.5" stroke-dasharray="4 24" opacity="0.7" />

  {wolf_geom}
</svg>
'''

with open('assets/profile/cyber_wolf_vector.svg', 'w', encoding='utf-8') as f:
    f.write(svg_doc)

print('Saved assets/profile/cyber_wolf_vector.svg')

