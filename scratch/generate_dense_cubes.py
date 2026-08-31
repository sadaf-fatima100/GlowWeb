import math

def generate_cube(cx, cy, radius=56, height=62, style="wireframe_glow", side="left"):
    dx = radius
    dy = radius * 0.57735
    
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

def build_cluster(side="left"):
    styles = ["filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass", "wireframe_bright", "glass_top", "wireframe_subtle", "filled_glass"]
    
    if side == "left":
        # Dense interlocking mesh starting from y = -60 (filling top completely)
        cols = [
            (0, -60, 10),   # x = 10
            (1, -12, 10),   # x = 66
            (2, -60, 9),    # x = 122
            (3, -12, 8),    # x = 178
            (4, 36, 7),     # x = 234
            (5, 84, 6),     # x = 290
            (6, 132, 5),    # x = 346
            (7, 180, 4),    # x = 402
        ]
        
        radius = 56
        h_step = 56
        v_step = 96
        
        svg_cubes = []
        c_idx = 0
        for col_idx, y_start, count in cols:
            cx = 10 + col_idx * h_step
            for i in range(count):
                cy = y_start + i * v_step
                st = styles[(c_idx + i * 2 + col_idx) % len(styles)]
                svg_cubes.append(generate_cube(cx, cy, radius=56, height=64, style=st, side="left"))
                c_idx += 1
        
        return "\n".join(svg_cubes)
    else:
        cols = [
            (0, -60, 10),   # x = 470
            (1, -12, 10),   # x = 414
            (2, -60, 9),    # x = 358
            (3, -12, 8),    # x = 302
            (4, 36, 7),     # x = 246
            (5, 84, 6),     # x = 190
            (6, 132, 5),    # x = 134
            (7, 180, 4),    # x = 78
        ]
        
        radius = 56
        h_step = 56
        v_step = 96
        
        svg_cubes = []
        c_idx = 0
        for col_idx, y_start, count in cols:
            cx = 470 - col_idx * h_step
            for i in range(count):
                cy = y_start + i * v_step
                st = styles[(c_idx + i * 2 + col_idx) % len(styles)]
                svg_cubes.append(generate_cube(cx, cy, radius=56, height=64, style=st, side="right"))
                c_idx += 1
        
        return "\n".join(svg_cubes)

left_svg = build_cluster("left")
right_svg = build_cluster("right")

with open("scratch/dense_left_cubes.svg", "w", encoding="utf-8") as f:
    f.write(left_svg)

with open("scratch/dense_right_cubes.svg", "w", encoding="utf-8") as f:
    f.write(right_svg)

print("Dense interlocking cubes generated successfully!")
