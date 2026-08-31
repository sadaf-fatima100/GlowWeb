import re

def generate_cube(cx, cy, radius=54, height=60, style="wireframe_glow", side="left"):
    dx = radius
    dy = radius * 0.57735  # ~ 31.17
    
    p_top = (cx, cy - dy)
    p_right = (cx + dx, cy)
    p_bottom = (cx, cy + dy)
    p_left = (cx - dx, cy)
    
    p_b_left = (cx - dx, cy + height)
    p_b_bottom = (cx, cy + dy + height)
    p_b_right = (cx + dx, cy + height)
    
    glow_id = "neonGlowLeft" if side == "left" else "neonGlowRight"
    grad_id = "topGlowGradLeft" if side == "left" else "topGlowGradRight"
    
    svg = []
    
    pts_top = f"{p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_left[0]:.1f},{p_left[1]:.1f}"
    pts_left = f"{p_left[0]:.1f},{p_left[1]:.1f} {p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_b_bottom[0]:.1f},{p_b_bottom[1]:.1f} {p_b_left[0]:.1f},{p_b_left[1]:.1f}"
    pts_right = f"{p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_b_right[0]:.1f},{p_b_right[1]:.1f} {p_b_bottom[0]:.1f},{p_b_bottom[1]:.1f}"
    
    if style == "filled_glass":
        svg.append(f'<g class="iso-cube style-filled_glass">')
        svg.append(f'  <polygon class="cube-face-top" points="{pts_top}" fill="url(#{grad_id})" stroke="rgba(0,255,170,0.65)" stroke-width="1.2"/>')
        svg.append(f'  <polygon class="cube-face-left" points="{pts_left}" fill="rgba(0,35,22,0.55)" stroke="rgba(0,217,143,0.3)" stroke-width="0.9"/>')
        svg.append(f'  <polygon class="cube-face-right" points="{pts_right}" fill="rgba(0,20,12,0.7)" stroke="rgba(0,217,143,0.22)" stroke-width="0.9"/>')
        svg.append(f'  <polyline class="cube-glow-edge" points="{p_left[0]:.1f},{p_left[1]:.1f} {p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="1.6" filter="url(#{glow_id})"/>')
        svg.append(f'  <circle class="cube-glow-dot" cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="2.2" fill="#00ffaa" filter="url(#{glow_id})"/>')
        svg.append(f'  <circle class="cube-glow-dot" cx="{p_bottom[0]:.1f}" cy="{p_bottom[1]:.1f}" r="1.8" fill="#00d98f"/>')
        svg.append(f'</g>')
    elif style == "wireframe_bright":
        svg.append(f'<g class="iso-cube style-wireframe_bright">')
        svg.append(f'  <polygon class="cube-face-top" points="{pts_top}" fill="none" stroke="rgba(0,255,170,0.75)" stroke-width="1.3"/>')
        svg.append(f'  <polygon class="cube-face-left" points="{pts_left}" fill="none" stroke="rgba(0,217,143,0.35)" stroke-width="0.9"/>')
        svg.append(f'  <polygon class="cube-face-right" points="{pts_right}" fill="none" stroke="rgba(0,217,143,0.25)" stroke-width="0.9"/>')
        svg.append(f'  <line class="cube-glow-edge" x1="{p_bottom[0]:.1f}" y1="{p_bottom[1]:.1f}" x2="{p_b_bottom[0]:.1f}" y2="{p_b_bottom[1]:.1f}" stroke="#00ffaa" stroke-width="1.5" filter="url(#{glow_id})"/>')
        svg.append(f'  <circle class="cube-glow-dot" cx="{p_bottom[0]:.1f}" cy="{p_bottom[1]:.1f}" r="2" fill="#00ffaa" filter="url(#{glow_id})"/>')
        svg.append(f'</g>')
    elif style == "wireframe_subtle":
        svg.append(f'<g class="iso-cube style-wireframe_subtle">')
        svg.append(f'  <polygon class="cube-face-top" points="{pts_top}" fill="none" stroke="rgba(0,217,143,0.4)" stroke-width="0.9"/>')
        svg.append(f'  <polygon class="cube-face-left" points="{pts_left}" fill="none" stroke="rgba(0,217,143,0.2)" stroke-width="0.8"/>')
        svg.append(f'  <polygon class="cube-face-right" points="{pts_right}" fill="none" stroke="rgba(0,217,143,0.18)" stroke-width="0.8"/>')
        svg.append(f'</g>')
    elif style == "glass_top":
        svg.append(f'<g class="iso-cube style-glass_top">')
        svg.append(f'  <polygon class="cube-face-top" points="{pts_top}" fill="rgba(0,255,170,0.14)" stroke="rgba(0,255,170,0.6)" stroke-width="1.1"/>')
        svg.append(f'  <polygon class="cube-face-left" points="{pts_left}" fill="none" stroke="rgba(0,217,143,0.28)" stroke-width="0.8"/>')
        svg.append(f'  <polygon class="cube-face-right" points="{pts_right}" fill="none" stroke="rgba(0,217,143,0.22)" stroke-width="0.8"/>')
        svg.append(f'  <polyline class="cube-glow-edge" points="{p_left[0]:.1f},{p_left[1]:.1f} {p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="1.5" filter="url(#{glow_id})"/>')
        svg.append(f'  <circle class="cube-glow-dot" cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="2" fill="#00ffaa" filter="url(#{glow_id})"/>')
        svg.append(f'</g>')
    return "\n".join(svg)

def build_left_svg():
    styles = ["filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass"]
    cols = [
        (0, -60, 11),   # x = 10
        (1, -12, 11),   # x = 64
        (2, -60, 10),   # x = 118
        (3, -12, 9),    # x = 172
        (4, 36, 8),     # x = 226
        (5, 84, 7),     # x = 280
        (6, 132, 6),    # x = 334
        (7, 180, 5),    # x = 388
    ]
    
    h_step = 54
    v_step = 92
    
    svg = []
    svg.append('<svg viewBox="0 0 520 960" preserveAspectRatio="xMinYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">')
    svg.append('<defs>')
    svg.append('  <filter id="neonGlowLeft" x="-100%" y="-100%" width="300%" height="300%">')
    svg.append('    <feGaussianBlur stdDeviation="3" result="blur1"/>')
    svg.append('    <feGaussianBlur stdDeviation="7" result="blur2"/>')
    svg.append('    <feMerge>')
    svg.append('      <feMergeNode in="blur2"/>')
    svg.append('      <feMergeNode in="blur1"/>')
    svg.append('      <feMergeNode in="SourceGraphic"/>')
    svg.append('    </feMerge>')
    svg.append('  </filter>')
    svg.append('  <linearGradient id="topGlowGradLeft" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#00d98f" stop-opacity="0.32"/>')
    svg.append('    <stop offset="100%" stop-color="#004830" stop-opacity="0.08"/>')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    c_idx = 0
    for col_idx, y_start, count in cols:
        cx = 10 + col_idx * h_step
        for i in range(count):
            cy = y_start + i * v_step
            st = styles[(c_idx + i * 2 + col_idx) % len(styles)]
            svg.append(generate_cube(cx, cy, radius=54, height=60, style=st, side="left"))
            c_idx += 1
            
    svg.append('</svg>')
    return "\n".join(svg)

def build_right_svg():
    styles = ["filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass"]
    cols = [
        (0, -60, 11),   # x = 510
        (1, -12, 11),   # x = 456
        (2, -60, 10),   # x = 402
        (3, -12, 9),    # x = 348
        (4, 36, 8),     # x = 294
        (5, 84, 7),     # x = 240
        (6, 132, 6),    # x = 186
        (7, 180, 5),    # x = 132
    ]
    
    h_step = 54
    v_step = 92
    
    svg = []
    svg.append('<svg viewBox="0 0 520 960" preserveAspectRatio="xMaxYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">')
    svg.append('<defs>')
    svg.append('  <filter id="neonGlowRight" x="-100%" y="-100%" width="300%" height="300%">')
    svg.append('    <feGaussianBlur stdDeviation="3" result="blur1"/>')
    svg.append('    <feGaussianBlur stdDeviation="7" result="blur2"/>')
    svg.append('    <feMerge>')
    svg.append('      <feMergeNode in="blur2"/>')
    svg.append('      <feMergeNode in="blur1"/>')
    svg.append('      <feMergeNode in="SourceGraphic"/>')
    svg.append('    </feMerge>')
    svg.append('  </filter>')
    svg.append('  <linearGradient id="topGlowGradRight" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('    <stop offset="0%" stop-color="#00d98f" stop-opacity="0.32"/>')
    svg.append('    <stop offset="100%" stop-color="#004830" stop-opacity="0.08"/>')
    svg.append('  </linearGradient>')
    svg.append('</defs>')
    
    c_idx = 0
    for col_idx, y_start, count in cols:
        cx = 510 - col_idx * h_step
        for i in range(count):
            cy = y_start + i * v_step
            st = styles[(c_idx + i * 2 + col_idx) % len(styles)]
            svg.append(generate_cube(cx, cy, radius=54, height=60, style=st, side="right"))
            c_idx += 1
            
    svg.append('</svg>')
    return "\n".join(svg)

left_cluster = build_left_svg()
right_cluster = build_right_svg()

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace hero hex blocks section
pattern = r'(<!-- Left Hexagonal Geometric Blocks -->\s*<div class="hero-hex-blocks hero-hex-left">).*?(</div>\s*<!-- Background Ambient Glow)'

replacement = f"""<!-- Left Hexagonal Geometric Blocks -->
      <div class="hero-hex-blocks hero-hex-left">
{left_cluster}
      </div>

      <!-- Right Hexagonal Geometric Blocks -->
      <div class="hero-hex-blocks hero-hex-right">
{right_cluster}
      </div>
      <!-- Background Ambient Glow"""

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully injected dense interlocking 3D cube mesh into index.html!")
