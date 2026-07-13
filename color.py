import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# =========================================================================
# 1. ENTERPRISE DESIGN TOKENS (Color Architecture & System Consts)
# =========================================================================
DESIGN_TOKENS = {
    "palette": {
        "surface_sky": "#4BA3E3",       # Canvas background
        "surface_cloud": "#FFFFFF",     # High-contrast elements
        "accent_path": "#E5A647",       # Warm dirt track focus
        
        # Hierarchical Green Brand Layers (Depth Scaling)
        "brand_depth": "#1B5E20",       # Distant anchoring hills
        "brand_secondary": "#2E7D32",   # Midground meadow
        "brand_primary": "#66BB6A",     # Foreground high-vibrancy focus
        
        # Micro-Interaction Accents
        "butterfly_blue": "#03A9F4",
        "butterfly_gold": "#FF9800",
        "flower_core": "#FFD54F",
        "insect_body": "#2D1A12",
        
        # High-Contrast Semantic Rainbow Spectrum (WCAG Compliant)
        "rainbow": [
            "#E53935",  # Dynamic Red
            "#FB8C00",  # Monarch Orange
            "#FDD835",  # Sunflower Yellow
            "#43A047",  # Meadow Green
            "#00ACC1",  # Deep Cyan Blue
            "#3949AB",  # Royal Indigo
            "#8E24AA"   # Velvet Violet
        ]
    },
    "canvas": {
        "width": 10.0,
        "height": 6.5,
        "resolution_steps": 400
    }
}

# =========================================================================
# 2. ENCAPSULATED DRAWING MODULES
# =========================================================================

def initialize_canvas(tokens):
    """Configures the structural window canvas bounding box."""
    fig, ax = plt.subplots(
        figsize=(tokens["canvas"]["width"], tokens["canvas"]["height"]), 
        facecolor=tokens["palette"]["surface_sky"]
    )
    ax.set_xlim(0, tokens["canvas"]["width"])
    ax.set_ylim(0, tokens["canvas"]["height"])
    ax.axis('off')  # Removes viewport grid artifacts
    return fig, ax

def render_rainbow(ax, tokens):
    """Generates the concentric rainbow array centered below the baseline."""
    center_point = (5.0, -1.2)
    outer_radius = 6.6
    thickness = 0.22
    
    for index, color in enumerate(tokens["palette"]["rainbow"]):
        current_radius = outer_radius - (index * thickness)
        rainbow_arch = patches.Wedge(
            center=center_point, 
            r=current_radius, 
            theta1=0, 
            theta2=180, 
            width=thickness, 
            color=color, 
            alpha=0.95, 
            zorder=1
        )
        ax.add_patch(rainbow_arch)

def render_topography(ax, tokens):
    """Plots functional curves simulating organic atmospheric hills."""
    x = np.linspace(0, tokens["canvas"]["width"], tokens["canvas"]["resolution_steps"])
    pal = tokens["palette"]
    
    # Layer 1: Distant Background Topology
    y_distant = 2.5 + 0.25 * np.sin(x * 0.8) + 0.1 * np.cos(x * 2.0)
    ax.fill_between(x, 0, y_distant, color=pal["brand_depth"], zorder=2)
    
    # Layer 2: Midground Structural Topology
    y_mid = 1.8 + 0.35 * np.sin(x * 0.6 + 1.2)
    ax.fill_between(x, 0, y_mid, color=pal["brand_secondary"], zorder=3)
    
    # Layer 3: Foreground Main Canvas Topology
    y_foreground = 1.1 + 0.45 * np.cos(x * 0.5 - 0.8)
    ax.fill_between(x, 0, y_foreground, color=pal["brand_primary"], zorder=4)
    
    return x, y_foreground

def render_winding_path(ax, tokens):
    """Calculates and constructs the progressive tapering vector path."""
    pal = tokens["palette"]
    y_path = np.linspace(0, 1.5, 150)
    
    # Path curvature center line mapping (S-Curve algorithm)
    x_center = 4.8 + 1.35 * np.sin(y_path * 2.3) - 0.45 * y_path
    
    # Perspective Compression: Taper width narrower as y increases
    path_width = 1.25 * (1.5 - y_path) / 1.5 + 0.16
    
    x_left_bound = x_center - (path_width / 2)
    x_right_bound = x_center + (path_width / 2)
    
    # Loop coordinate bounds to create solid dynamic polygon shape
    poly_x = np.concatenate([x_left_bound, x_right_bound[::-1]])
    poly_y = np.concatenate([y_path, y_path[::-1]])
    
    ax.fill(poly_x, poly_y, color=pal["accent_path"], zorder=5)

def render_cloud_system(ax, cx, cy, scaling, tokens):
    """Generates structural UI cloud cluster assets."""
    white = tokens["palette"]["surface_cloud"]
    
    sub_circles = [
        (cx, cy, 0.42 * scaling),
        (cx - 0.32 * scaling, cy - 0.05 * scaling, 0.32 * scaling),
        (cx + 0.32 * scaling, cy - 0.05 * scaling, 0.32 * scaling),
        (cx - 0.15 * scaling, cy + 0.22 * scaling, 0.37 * scaling),
        (cx + 0.15 * scaling, cy + 0.22 * scaling, 0.37 * scaling)
    ]
    for x, y, radius in sub_circles:
        ax.add_patch(patches.Circle((x, y), radius, color=white, alpha=0.92, zorder=3.5, lw=0))

def render_butterfly(ax, bx, by, wing_color, tokens):
    """Plots localized stylized butterfly vector markers."""
    pal = tokens["palette"]
    
    # Asymmetric Wing Node Placement
    ax.add_patch(patches.Ellipse((bx - 0.08, by + 0.05), 0.14, 0.23, angle=32, color=wing_color, zorder=7))
    ax.add_patch(patches.Ellipse((bx + 0.08, by + 0.05), 0.14, 0.23, angle=-32, color=wing_color, zorder=7))
    
    # Structural Core Body
    ax.add_patch(patches.Ellipse((bx, by), 0.03, 0.18, color=pal["insect_body"], zorder=8))

def populate_vegetation(ax, x_steps, y_bounds, tokens):
    """Scatters dynamic flora elements using bounded spatial distribution."""
    np.random.seed(42)  # Ensures layout render determinism
    pal = tokens["palette"]
    total_flowers = 50
    
    rand_x = np.random.uniform(0.2, 9.8, total_flowers)
    rand_y = []
    
    for fx in rand_x:
        # Interpolate max vertical safety line for foreground clipping zone
        max_y_limit = 1.1 + 0.45 * np.cos(fx * 0.5 - 0.8)
        rand_y.append(np.random.uniform(0.08, max_y_limit - 0.08))
        
    # Batch scatter call optimization for performance
    ax.scatter(rand_x, rand_y, color=pal["surface_cloud"], s=35, zorder=6, edgecolors='none')
    ax.scatter(rand_x, rand_y, color=pal["flower_core"], s=8, zorder=6.5)

# =========================================================================
# 3. MAIN CODESET EXECUTION PIPELINE
# =========================================================================
def run_engine():
    # Setup Architecture
    fig, ax = initialize_canvas(DESIGN_TOKENS)
    
    # Draw Background Layers
    render_rainbow(ax, DESIGN_TOKENS)
    
    # Draw Topography Systems
    x_terrain, y_terrain = render_topography(ax, DESIGN_TOKENS)
    render_winding_path(ax, DESIGN_TOKENS)
    
    # Populate Environmental Atmospheric Items
    render_cloud_system(ax, 2.0, 2.6, 1.15, DESIGN_TOKENS)
    render_cloud_system(ax, 7.8, 2.4, 1.25, DESIGN_TOKENS)
    render_cloud_system(ax, 0.8, 5.3, 0.75, DESIGN_TOKENS)
    render_cloud_system(ax, 9.2, 4.9, 0.85, DESIGN_TOKENS)
    
    # Deploy Insect Vectors
    render_butterfly(ax, 1.4, 2.9, DESIGN_TOKENS["palette"]["butterfly_blue"], DESIGN_TOKENS)
    render_butterfly(ax, 8.7, 2.5, DESIGN_TOKENS["palette"]["butterfly_gold"], DESIGN_TOKENS)
    
    # Scatter Flora Layer
    populate_vegetation(ax, x_terrain, y_terrain, DESIGN_TOKENS)
    
    # Clean up Layout Frame Wrapping and Compile Output
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

if __name__ == "__main__":
    run_engine()