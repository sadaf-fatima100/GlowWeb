import re

def render_isometric_block(cx, cy, radius, height, style="prominent_glow", side="left"):
    # Isometric 30-degree angles
    dx = radius
    dy = radius * 0.57735  # ~ tan(30) * radius
    
    # Vertices of top face
    p_top = (cx, cy - dy)
    p_right = (cx + dx, cy)
    p_bottom = (cx, cy + dy)
    p_left = (cx - dx, cy)
    
    # Bottom vertices
    p_b_left = (cx - dx, cy + height)
    p_b_bottom = (cx, cy + dy + height)
    p_b_right = (cx + dx, cy + height)
    
    glow_filter = "neonGlowL" if side == "left" else "neonGlowR"
    top_grad = "topGradL" if side == "left" else "topGradR"
    
    pts_top = f"{p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_left[0]:.1f},{p_left[1]:.1f}"
    pts_left = f"{p_left[0]:.1f},{p_left[1]:.1f} {p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_b_bottom[0]:.1f},{p_b_bottom[1]:.1f} {p_b_left[0]:.1f},{p_b_left[1]:.1f}"
    pts_right = f"{p_bottom[0]:.1f},{p_bottom[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_b_right[0]:.1f},{p_b_right[1]:.1f} {p_b_bottom[0]:.1f},{p_b_bottom[1]:.1f}"
    
    svg = [f'<!-- Cube at ({cx}, {cy}) -->', '<g class="hero-3d-cube">']
    
    if style == "prominent_glow":
        # Top Face (Glowing Glass Rhombus)
        svg.append(f'  <polygon points="{pts_top}" fill="url(#{top_grad})" stroke="rgba(0, 255, 170, 0.75)" stroke-width="1.6" />')
        # Left Face (Dark Emerald)
        svg.append(f'  <polygon points="{pts_left}" fill="rgba(0, 32, 20, 0.55)" stroke="rgba(0, 217, 143, 0.35)" stroke-width="1.1" />')
        # Right Face (Deeper Obsidian)
        svg.append(f'  <polygon points="{pts_right}" fill="rgba(0, 18, 11, 0.7)" stroke="rgba(0, 217, 143, 0.25)" stroke-width="1.1" />')
        # Bright Neon Glowing Upper Edges
        svg.append(f'  <polyline points="{p_left[0]:.1f},{p_left[1]:.1f} {p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="2.2" filter="url(#{glow_filter})" />')
        # Vertical Neon Spine Edge
        svg.append(f'  <line x1="{p_bottom[0]:.1f}" y1="{p_bottom[1]:.1f}" x2="{p_b_bottom[0]:.1f}" y2="{p_b_bottom[1]:.1f}" stroke="#00ffaa" stroke-width="1.8" filter="url(#{glow_filter})" />')
        # Interior Center Dashed Axis
        svg.append(f'  <line x1="{p_top[0]:.1f}" y1="{p_top[1]:.1f}" x2="{p_bottom[0]:.1f}" y2="{p_bottom[1]:.1f}" stroke="#00ffaa" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.45" />')
        # Glowing Vertex Nodes
        svg.append(f'  <circle cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="3.2" fill="#00ffaa" filter="url(#{glow_filter})" />')
        svg.append(f'  <circle cx="{p_bottom[0]:.1f}" cy="{p_bottom[1]:.1f}" r="2.8" fill="#00ffaa" />')
        svg.append(f'  <circle cx="{p_right[0]:.1f}" cy="{p_right[1]:.1f}" r="2.2" fill="#00d98f" />')
        svg.append(f'  <circle cx="{p_left[0]:.1f}" cy="{p_left[1]:.1f}" r="2.2" fill="#00d98f" />')
        
    elif style == "wireframe_deep":
        # Wireframe with subtle glow
        svg.append(f'  <polygon points="{pts_top}" fill="rgba(0, 255, 170, 0.08)" stroke="rgba(0, 255, 170, 0.65)" stroke-width="1.4" />')
        svg.append(f'  <polygon points="{pts_left}" fill="rgba(0, 25, 16, 0.35)" stroke="rgba(0, 217, 143, 0.35)" stroke-width="1.1" />')
        svg.append(f'  <polygon points="{pts_right}" fill="none" stroke="rgba(0, 217, 143, 0.25)" stroke-width="1.1" />')
        svg.append(f'  <line x1="{p_left[0]:.1f}" y1="{p_left[1]:.1f}" x2="{p_top[0]:.1f}" y2="{p_top[1]:.1f}" stroke="#00ffaa" stroke-width="1.8" filter="url(#{glow_filter})" />')
        svg.append(f'  <circle cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="2.6" fill="#00ffaa" filter="url(#{glow_filter})" />')
        
    elif style == "glass_faceted":
        # Translucent glass block
        svg.append(f'  <polygon points="{pts_top}" fill="rgba(0, 217, 143, 0.16)" stroke="rgba(0, 255, 170, 0.7)" stroke-width="1.3" />')
        svg.append(f'  <polygon points="{pts_left}" fill="rgba(0, 30, 18, 0.5)" stroke="rgba(0, 217, 143, 0.3)" stroke-width="1" />')
        svg.append(f'  <polygon points="{pts_right}" fill="rgba(0, 16, 10, 0.6)" stroke="rgba(0, 217, 143, 0.22)" stroke-width="1" />')
        svg.append(f'  <polyline points="{p_left[0]:.1f},{p_left[1]:.1f} {p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f}" fill="none" stroke="#00ffaa" stroke-width="1.8" filter="url(#{glow_filter})" />')
        svg.append(f'  <circle cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="3" fill="#00ffaa" filter="url(#{glow_filter})" />')
        svg.append(f'  <circle cx="{p_bottom[0]:.1f}" cy="{p_bottom[1]:.1f}" r="2.5" fill="#00d98f" />')
        
    elif style == "subtle_wireframe":
        # Clean background geometry
        svg.append(f'  <polygon points="{pts_top}" fill="none" stroke="rgba(0, 217, 143, 0.45)" stroke-width="1" />')
        svg.append(f'  <polygon points="{pts_left}" fill="none" stroke="rgba(0, 217, 143, 0.25)" stroke-width="0.9" />')
        svg.append(f'  <polygon points="{pts_right}" fill="none" stroke="rgba(0, 217, 143, 0.2)" stroke-width="0.9" />')
        svg.append(f'  <line x1="{p_top[0]:.1f}" y1="{p_top[1]:.1f}" x2="{p_right[0]:.1f}" y2="{p_right[1]:.1f}" stroke="#00ffaa" stroke-width="1.4" opacity="0.8" />')
        svg.append(f'  <circle cx="{p_top[0]:.1f}" cy="{p_top[1]:.1f}" r="2" fill="#00ffaa" />')

    svg.append('</g>')
    return "\n".join(svg)


def generate_left_hero_svg():
    # Left Cluster Blocks exactly matching reference image media_1788168754840.png
    blocks = [
        # (cx, cy, radius, height, style)
        (50, 45, 95, 115, "prominent_glow"),         # Top-Left Block (Starts right at top)
        (-30, 240, 115, 140, "wireframe_deep"),      # Upper-Left Outer Block
        (135, 290, 110, 135, "prominent_glow"),      # Middle-Left Focal Block (Center of cluster)
        (235, 450, 85, 105, "subtle_wireframe"),     # Inner Staggered Accent Block
        (-20, 490, 105, 130, "glass_faceted"),       # Lower-Left Outer Block
        (85, 620, 125, 155, "prominent_glow"),       # Bottom-Left Foundation Block (Behind card)
    ]
    
    svg = [
        '<svg viewBox="0 0 500 880" preserveAspectRatio="xMinYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '<defs>',
        '  <filter id="neonGlowL" x="-50%" y="-50%" width="200%" height="200%">',
        '    <feGaussianBlur stdDeviation="3" result="blur1"/>',
        '    <feGaussianBlur stdDeviation="7" result="blur2"/>',
        '    <feMerge>',
        '      <feMergeNode in="blur2"/>',
        '      <feMergeNode in="blur1"/>',
        '      <feMergeNode in="SourceGraphic"/>',
        '    </feMerge>',
        '  </filter>',
        '  <linearGradient id="topGradL" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#00ffaa" stop-opacity="0.35"/>',
        '    <stop offset="100%" stop-color="#003b26" stop-opacity="0.08"/>',
        '  </linearGradient>',
        '</defs>',
    ]
    
    # Connecting isometric lattice lines
    svg.append('<!-- Background Connecting Mesh Lines -->')
    svg.append('<g stroke="rgba(0, 217, 143, 0.22)" stroke-width="1" stroke-dasharray="4 4">')
    svg.append('  <line x1="50" y1="45" x2="135" y2="290" />')
    svg.append('  <line x1="135" y1="290" x2="235" y2="450" />')
    svg.append('  <line x1="-30" y1="240" x2="85" y2="620" />')
    svg.append('</g>')
    
    for cx, cy, rad, h, st in blocks:
        svg.append(render_isometric_block(cx, cy, rad, h, style=st, side="left"))
        
    svg.append('</svg>')
    return "\n".join(svg)


def generate_right_hero_svg():
    # Right Cluster Blocks exactly matching reference image media_1788168754840.png
    blocks = [
        # (cx, cy, radius, height, style)
        (450, 45, 95, 115, "prominent_glow"),        # Top-Right Block (Starts right at top)
        (530, 240, 115, 140, "wireframe_deep"),     # Upper-Right Outer Block
        (365, 290, 110, 135, "prominent_glow"),     # Middle-Right Focal Block
        (265, 450, 85, 105, "subtle_wireframe"),    # Inner Staggered Accent Block
        (520, 490, 105, 130, "glass_faceted"),      # Lower-Right Outer Block
        (415, 620, 125, 155, "prominent_glow"),     # Bottom-Right Foundation Block (Behind card)
    ]
    
    svg = [
        '<svg viewBox="0 0 500 880" preserveAspectRatio="xMaxYMin meet" fill="none" xmlns="http://www.w3.org/2000/svg">',
        '<defs>',
        '  <filter id="neonGlowR" x="-50%" y="-50%" width="200%" height="200%">',
        '    <feGaussianBlur stdDeviation="3" result="blur1"/>',
        '    <feGaussianBlur stdDeviation="7" result="blur2"/>',
        '    <feMerge>',
        '      <feMergeNode in="blur2"/>',
        '      <feMergeNode in="blur1"/>',
        '      <feMergeNode in="SourceGraphic"/>',
        '    </feMerge>',
        '  </filter>',
        '  <linearGradient id="topGradR" x1="0%" y1="0%" x2="100%" y2="100%">',
        '    <stop offset="0%" stop-color="#00ffaa" stop-opacity="0.35"/>',
        '    <stop offset="100%" stop-color="#003b26" stop-opacity="0.08"/>',
        '  </linearGradient>',
        '</defs>',
    ]
    
    # Connecting isometric lattice lines
    svg.append('<!-- Background Connecting Mesh Lines -->')
    svg.append('<g stroke="rgba(0, 217, 143, 0.22)" stroke-width="1" stroke-dasharray="4 4">')
    svg.append('  <line x1="450" y1="45" x2="365" y2="290" />')
    svg.append('  <line x1="365" y1="290" x2="265" y2="450" />')
    svg.append('  <line x1="530" y1="240" x2="415" y2="620" />')
    svg.append('</g>')
    
    for cx, cy, rad, h, st in blocks:
        svg.append(render_isometric_block(cx, cy, rad, h, style=st, side="right"))
        
    svg.append('</svg>')
    return "\n".join(svg)


left_svg_code = generate_left_hero_svg()
right_svg_code = generate_right_hero_svg()

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

print("Exact reference 3D isometric hero blocks generated and applied!")
