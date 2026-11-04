import sys

def generate_cyber_wolf_svg(cx=200, cy=200, scale=1.0):
    # Base points (left side + center). Center x is 200, center y is 200.
    # Symmetry about x = 200.
    
    # Facets definition: (list of point names, fill_color, stroke_color, stroke_width)
    pts = {
        'crown': (200, 75),
        'forehead_mid': (200, 120),
        'brow_mid': (200, 160),
        'bridge_mid': (200, 205),
        'nose_mid': (200, 245),
        'chin_mid': (200, 280),
        'throat_mid': (200, 325),
        
        # Left side points
        'l_ear_tip': (130, 40),
        'l_ear_outer': (95, 115),
        'l_ear_inner': (165, 95),
        'l_ear_mid': (135, 80),
        
        'l_temple': (140, 145),
        'l_brow_crest': (165, 140),
        'l_eye_in': (175, 175),
        'l_eye_out': (145, 168),
        'l_eye_bot': (162, 184),
        
        'l_cheek_high': (100, 185),
        'l_cheek_mid': (85, 230),
        'l_jaw_angle': (115, 275),
        'l_jaw_sub': (155, 275),
        
        'l_muzzle_top': (165, 210),
        'l_muzzle_mid': (165, 245),
        
        'l_neck_outer': (75, 305),
        'l_neck_mid': (115, 335),
        'l_neck_in': (160, 325),
    }

    # Helper to get point or mirrored point
    def P(name, mirror=False):
        p = pts[name]
        if mirror:
            return (400 - p[0], p[1])
        return p

    def poly_pts(p_list):
        return ' '.join([f"{x},{y}" for x, y in p_list])

    # Left & Right polygon pairs: (left_point_names, fill, stroke)
    facets = [
        # Ears outer
        (['l_ear_outer', 'l_ear_tip', 'l_ear_inner'], '#081D1A', '#174D43', 1),
        (['l_ear_tip', 'l_ear_mid', 'l_ear_inner'], '#0A2E28', '#20D9D2', 1.2),
        (['l_ear_outer', 'l_temple', 'l_ear_inner'], '#061614', '#174D43', 1),
        
        # Forehead & Crown
        (['crown', 'l_ear_inner', 'l_brow_crest'], '#0C2B25', '#174D43', 1),
        (['crown', 'l_brow_crest', 'forehead_mid'], '#0F3830', '#39F59A', 1),
        (['forehead_mid', 'l_brow_crest', 'brow_mid'], '#13473D', '#20D9D2', 1),
        
        # Temple & Cheeks
        (['l_ear_outer', 'l_cheek_high', 'l_temple'], '#081D1A', '#174D43', 1),
        (['l_temple', 'l_cheek_high', 'l_eye_out'], '#0B2520', '#174D43', 1),
        (['l_brow_crest', 'l_temple', 'l_eye_out'], '#0E3029', '#20D9D2', 1),
        (['l_brow_crest', 'l_eye_out', 'l_eye_in'], '#154A3F', '#39F59A', 1.2),
        (['brow_mid', 'l_brow_crest', 'l_eye_in'], '#195B4E', '#39F59A', 1.2),
        
        # Cheek plates
        (['l_cheek_high', 'l_cheek_mid', 'l_eye_out'], '#071A17', '#174D43', 1),
        (['l_eye_out', 'l_cheek_mid', 'l_muzzle_top'], '#0A2621', '#174D43', 1),
        (['l_eye_out', 'l_muzzle_top', 'l_eye_bot'], '#0F3830', '#20D9D2', 1),
        (['l_eye_in', 'l_eye_bot', 'l_muzzle_top'], '#164E42', '#39F59A', 1),
        (['brow_mid', 'l_eye_in', 'bridge_mid'], '#1E6857', '#39F59A', 1.2),
        (['l_eye_in', 'l_muzzle_top', 'bridge_mid'], '#185648', '#20D9D2', 1),
        
        # Snout / Muzzle
        (['bridge_mid', 'l_muzzle_top', 'nose_mid'], '#227763', '#39F59A', 1.2),
        (['l_muzzle_top', 'l_muzzle_mid', 'nose_mid'], '#1A594B', '#20D9D2', 1),
        (['l_cheek_mid', 'l_jaw_angle', 'l_muzzle_mid'], '#081C19', '#174D43', 1),
        (['l_muzzle_mid', 'l_jaw_sub', 'chin_mid'], '#134439', '#20D9D2', 1),
        (['nose_mid', 'l_muzzle_mid', 'chin_mid'], '#20705E', '#39F59A', 1.2),
        
        # Jaw & Chin
        (['l_jaw_angle', 'l_jaw_sub', 'chin_mid'], '#0A221E', '#174D43', 1),
        (['chin_mid', 'l_jaw_sub', 'throat_mid'], '#0E2E28', '#20D9D2', 1),
        (['l_jaw_sub', 'l_neck_in', 'throat_mid'], '#09201C', '#174D43', 1),
        
        # Neck flare
        (['l_cheek_mid', 'l_neck_outer', 'l_jaw_angle'], '#051412', '#174D43', 1),
        (['l_jaw_angle', 'l_neck_outer', 'l_neck_mid'], '#071B18', '#174D43', 1),
        (['l_jaw_angle', 'l_neck_mid', 'l_jaw_sub'], '#0B2722', '#20D9D2', 1),
        (['l_jaw_sub', 'l_neck_mid', 'l_neck_in'], '#081E1A', '#174D43', 1),
    ]

    svg_polys = []
    
    # Draw left and right facets
    for side in [False, True]: # False: Left, True: Right
        for facet, fill, stroke, sw in facets:
            pts_coords = [P(name, mirror=side) for name in facet]
            svg_polys.append(f'<polygon points="{poly_pts(pts_coords)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" />')

    # Cyber Neon Glowing Eyes!
    # Left eye triangle: (l_eye_in, l_eye_out, l_eye_bot)
    svg_eyes = '''
    <!-- Cyber Wolf Neon Laser Eyes -->
    <g filter="url(#eye-glow)">
      <!-- Left Eye -->
      <polygon points="175,175 145,168 162,184" fill="#39F59A" stroke="#20D9D2" stroke-width="1.5" />
      <circle cx="160" cy="176" r="3" fill="#FFFFFF" />
      
      <!-- Right Eye (Mirrored: 400 - x) -->
      <polygon points="225,175 255,168 238,184" fill="#39F59A" stroke="#20D9D2" stroke-width="1.5" />
      <circle cx="240" cy="176" r="3" fill="#FFFFFF" />
    </g>
    
    <!-- Nose bridge neon centerline highlight -->
    <line x1="200" y1="160" x2="200" y2="245" stroke="#39F59A" stroke-width="2" filter="url(#eye-glow)" />
    <!-- Forehead cyber diamond crest -->
    <polygon points="200,95 210,120 200,145 190,120" fill="#20D9D2" stroke="#39F59A" stroke-width="1.5" filter="url(#eye-glow)" />
    '''
    
    return '\n'.join(svg_polys) + '\n' + svg_eyes

if __name__ == '__main__':
    result = generate_cyber_wolf_svg()
    print(f"Generated {len(result.splitlines())} lines of pure vector Cyber Wolf geometry!")

