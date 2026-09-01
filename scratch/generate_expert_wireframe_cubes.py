import math
import re

def render_wireframe_iso_cube(cx, cy, R, style="prominent", side="left"):
    # 6 vertices of a regular hexagon (pointy top)
    v_top = (cx, cy - R)
    v_tr  = (cx + R * math.cos(math.radians(-30)), cy + R * math.sin(math.radians(-30)))
    v_br  = (cx + R * math.cos(math.radians(30)),  cy + R * math.sin(math.radians(30)))
    v_bot = (cx, cy + R)
    v_bl  = (cx + R * math.cos(math.radians(150)), cy + R * math.sin(math.radians(150)))
    v_tl  = (cx + R * math.cos(math.radians(210)), cy + R * math.sin(math.radians(210)))
    v_c   = (cx, cy)
    
    glow_id = "neonGlowL" if side == "left" else "neonGlowR"
    grad_id = "topGradL" if side == "left" else "topGradR"
    
    svg = [f'<!-- Wireframe Iso Cube at ({cx}, {cy}) -->', '<g class="wireframe-iso-cube">']
    
    # Rhombus polygons for 3D faces
    poly_top = f"{v_c[0]:.1f},{v_c[1]:.1f} {v_tl[0]:.1f},{v_tl[1]:.1f} {v_top[0]:.1f},{v_top[1]:.1f} {v_tr[0]:.1f},{v_tr[1]:.1f}"
    poly_left = f"{v_c[0]:.1f},{v_c[1]:.1f} {v_tl[0]:.1f},{v_tl[1]:.1f} {v_bl[0]:.1f},{v_bl[1]:.1f} {v_bot[0]:.1f},{v_bot[1]:.1f}"
    poly_right = f"{v_c[0]:.1f},{v_c[1]:.1f} {v_tr[0]:.1f},{v_tr[1]:.1f} {v_br[0]:.1f},{v_br[1]:.1f} {v_bot[0]:.1f},{v_bot[1]:.1f}"
    
    if style == "prominent":
        svg.append(f'  <polygon class="iso-face-top" points="{poly_top}" fill="url(#{grad_id})" stroke="rgba(0, 255, 170, 0.75)" stroke-width="1.2" />')
        svg.append(f'  <polygon class="iso-face-left" points="{poly_left}" fill="rgba(0, 26, 16, 0.45)" stroke="rgba(0, 217, 143, 0.35)" stroke-width="1" />')
        svg.append(f'  <polygon class="iso-face-right" points="{poly_right}" fill="rgba(0, 16, 10, 0.55)" stroke="rgba(0, 217, 143, 0.25)" stroke-width="1" />')
        svg.append(f'  <polyline class="iso-glow-edge" points="{v_tl[0]:.1f},{v_tl[1]:.1f} {v_top[0]:.1f},{v_top[1]:.1f} {v_tr[0]:.1f},{v_tr[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="1.8" filter="url(#{glow_id})" />')
        svg.append(f'  <line class="iso-spine" x1="{v_c[0]:.1f}" y1="{v_c[1]:.1f}" x2="{v_bot[0]:.1f}" y2="{v_bot[1]:.1f}" stroke="#00ffaa" stroke-width="1.4" filter="url(#{glow_id})" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_top[0]:.1f}" cy="{v_top[1]:.1f}" r="2.8" fill="#00ffaa" filter="url(#{glow_id})" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_c[0]:.1f}" cy="{v_c[1]:.1f}" r="2.2" fill="#00ffaa" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_tr[0]:.1f}" cy="{v_tr[1]:.1f}" r="2" fill="#00d98f" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_tl[0]:.1f}" cy="{v_tl[1]:.1f}" r="2" fill="#00d98f" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_bot[0]:.1f}" cy="{v_bot[1]:.1f}" r="2" fill="#00d98f" />')
        
    elif style == "glass_tint":
        svg.append(f'  <polygon class="iso-face-top" points="{poly_top}" fill="rgba(0, 255, 170, 0.12)" stroke="rgba(0, 255, 170, 0.6)" stroke-width="1.1" />')
        svg.append(f'  <polygon class="iso-face-left" points="{poly_left}" fill="rgba(0, 20, 12, 0.3)" stroke="rgba(0, 217, 143, 0.3)" stroke-width="0.9" />')
        svg.append(f'  <polygon class="iso-face-right" points="{poly_right}" fill="none" stroke="rgba(0, 217, 143, 0.22)" stroke-width="0.9" />')
        svg.append(f'  <polyline class="iso-glow-edge" points="{v_tl[0]:.1f},{v_tl[1]:.1f} {v_top[0]:.1f},{v_top[1]:.1f} {v_tr[0]:.1f},{v_tr[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="1.4" filter="url(#{glow_id})" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_top[0]:.1f}" cy="{v_top[1]:.1f}" r="2.2" fill="#00ffaa" filter="url(#{glow_id})" />')
        
    elif style == "subtle_wireframe":
        svg.append(f'  <polygon class="iso-face-top" points="{poly_top}" fill="none" stroke="rgba(0, 217, 143, 0.45)" stroke-width="0.9" />')
        svg.append(f'  <polygon class="iso-face-left" points="{poly_left}" fill="none" stroke="rgba(0, 217, 143, 0.25)" stroke-width="0.8" />')
        svg.append(f'  <polygon class="iso-face-right" points="{poly_right}" fill="none" stroke="rgba(0, 217, 143, 0.2)" stroke-width="0.8" />')
        svg.append(f'  <line class="iso-spine" x1="{v_c[0]:.1f}" y1="{v_c[1]:.1f}" x2="{v_top[0]:.1f}" y2="{v_top[1]:.1f}" stroke="rgba(0, 255, 170, 0.6)" stroke-width="1" />')
        svg.append(f'  <circle class="iso-dot" cx="{v_top[0]:.1f}" cy="{v_top[1]:.1f}" r="1.8" fill="#00ffaa" />')

    svg.append('</g>')
    return "\n".join(svg)


def generate_expert_left_svg():
    blocks = [
        # (cx, cy, R, style)
        (60, 60, 78, "prominent"),
        (-25, 180, 88, "glass_tint"),
        (145, 195, 72, "subtle_wireframe"),
        (55, 330, 96, "prominent"),
        (190, 360, 64, "subtle_wireframe"),
        (-20, 480, 82, "glass_tint"),
        (105, 510, 88, "prominent"),
        (215, 530, 58, "subtle_wireframe"),
        (45, 670, 92, "glass_tint"),
        (165, 680, 70, "prominent"),
    ]
    
    svg = [
        '<svg viewBox="0 0 480 840" preserveAspectRatio="xMinYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '<defs>',
        '  <filter id="neonGlowL" x="-100%" y="-100%" width="300%" height="300%">',
        '    <feGaussianBlur stdDeviation="2.5" result="blur1"/>',
        '    <feGaussianBlur stdDeviation="6" result="blur2"/>',
        '    <feMerge>',
        '      <feMergeNode in="blur2"/>',
        '      <feMergeNode in="blur1"/>',
        '      <feMergeNode in="SourceGraphic"/>',
        '    </feMerge>',
        '  </filter>',
        '  <linearGradient id="topGradL" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#00ffaa" stop-opacity="0.32"/>',
        '    <stop offset="100%" stop-color="#003b26" stop-opacity="0.06"/>',
        '  </linearGradient>',
        '</defs>',
    ]
    
    for cx, cy, R, st in blocks:
        svg.append(render_wireframe_iso_cube(cx, cy, R, style=st, side="left"))
        
    svg.append('</svg>')
    return "\n".join(svg)


def generate_expert_right_svg():
    blocks = [
        # (cx, cy, R, style)
        (420, 60, 78, "prominent"),
        (505, 180, 88, "glass_tint"),
        (335, 195, 72, "subtle_wireframe"),
        (425, 330, 96, "prominent"),
        (290, 360, 64, "subtle_wireframe"),
        (500, 480, 82, "glass_tint"),
        (375, 510, 88, "prominent"),
        (265, 530, 58, "subtle_wireframe"),
        (435, 670, 92, "glass_tint"),
        (315, 680, 70, "prominent"),
    ]
    
    svg = [
        '<svg viewBox="0 0 480 840" preserveAspectRatio="xMaxYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '<defs>',
        '  <filter id="neonGlowR" x="-100%" y="-100%" width="300%" height="300%">',
        '    <feGaussianBlur stdDeviation="2.5" result="blur1"/>',
        '    <feGaussianBlur stdDeviation="6" result="blur2"/>',
        '    <feMerge>',
        '      <feMergeNode in="blur2"/>',
        '      <feMergeNode in="blur1"/>',
        '      <feMergeNode in="SourceGraphic"/>',
        '    </feMerge>',
        '  </filter>',
        '  <linearGradient id="topGradR" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#00ffaa" stop-opacity="0.32"/>',
        '    <stop offset="100%" stop-color="#003b26" stop-opacity="0.06"/>',
        '  </linearGradient>',
        '</defs>',
    ]
    
    for cx, cy, R, st in blocks:
        svg.append(render_wireframe_iso_cube(cx, cy, R, style=st, side="right"))
        
    svg.append('</svg>')
    return "\n".join(svg)


left_svg_code = generate_expert_left_svg()
right_svg_code = generate_expert_right_svg()

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'(<!-- Left Hexagonal Geometric Blocks -->\s*<div class="hero-hex-blocks hero-hex-left">).*?(</div>\s*<!-- Background Ambient Glow)'

replacement = f"""<!-- Left Hexagonal Geometric Blocks -->
      <div class="hero-hex-blocks hero-hex-left">
{left_svg_code}
      </div>

      <!-- Right Hexagonal Geometric Blocks -->
      <div class="hero-hex-blocks hero-hex-right">
{right_svg_code}
      </div>
      <!-- Background Ambient Glow"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Connecting lines removed completely from hero background SVGs!")
