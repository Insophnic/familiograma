import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración inicial de la figura
fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Título Principal
plt.title("FAMILIOGRAMA ESTRUCTURAL: CASO J.A. (60 AÑOS)", fontsize=14, fontweight='bold', pad=15)

# --- FUNCIÓN PARA DIBUJAR INTEGRANTES ---
def draw_person(ax, x, y, shape, label, age="", color='#FFFFFF', border_color='#333333', is_patient=False, is_pregnant=False):
    size = 0.6
    
    # Hombre (Cuadrado)
    if shape == 'square':
        patch = patches.Rectangle((x - size/2, y - size/2), size, size, facecolor=color, edgecolor=border_color, linewidth=2)
        ax.add_patch(patch)
        if is_patient: # Doble borde para el caso índice
            patch_inner = patches.Rectangle((x - size/2 + 0.06, y - size/2 + 0.06), size - 0.12, size - 0.12, facecolor='none', edgecolor=border_color, linewidth=1.5)
            ax.add_patch(patch_inner)
            
    # Mujer (Círculo)
    elif shape == 'circle':
        patch = patches.Circle((x, y), size/2, facecolor=color, edgecolor=border_color, linewidth=2)
        ax.add_patch(patch)
        if is_pregnant: # Símbolo interno de gestación
            patch_inner = patches.Circle((x, y), size/4, facecolor='#FFD1DC', edgecolor=border_color, linewidth=1)
            ax.add_patch(patch_inner)
            
    # Etiquetas
    ax.text(x, y - 0.45, label, ha='center', va='top', fontsize=10, fontweight='bold')
    if age:
        ax.text(x, y - 0.68, f"({age})", ha='center', va='top', fontsize=9, color='#555555')

# --- POSICIONAMIENTO DE GENERACIONES ---
# Generación I (Parejas)
y1 = 6.0
x_silvia, x_ja, x_carlos = 2.0, 4.8, 7.8

# Generación II (Hija y Yerno)
y2 = 3.4
x_adriana, x_marco = 4.8, 6.8

# Generación III (Nieto en gestación)
y3 = 1.2
x_bebe = 5.8

# --- DIBUJO DE INTEGRANTES ---
draw_person(ax, x_silvia, y1, 'circle', 'Silvia', '58 a', color='#FFE6E6')
draw_person(ax, x_ja, y1, 'square', 'J.A. (Paciente)', '60 a', color='#D0E1FD', border_color='#1B4F72', is_patient=True)
draw_person(ax, x_carlos, y1, 'square', 'Carlos', '48 a', color='#D0E1FD')

draw_person(ax, x_adriana, y2, 'circle', 'Adriana', '32 a', color='#FFE6E6', is_pregnant=True)
draw_person(ax, x_marco, y2, 'square', 'Marco', '', color='#D0E1FD')

draw_person(ax, x_bebe, y3, 'circle', 'En gestación', 'Bebé', color='#FFF2CC')

# --- DIBUJO DE RELACIONES Y LÍNEAS ---

# 1. Divorcio JA y Silvia (Línea discontinua con doble barra // y zigzag de conflicto)
ax.plot([x_silvia + 0.3, x_ja - 0.3], [y1, y1], color='#C0392B', lw=1.5, linestyle='--')
ax.text(3.3, y1, '//', color='#C0392B', fontsize=18, fontweight='bold', ha='center', va='center')
ax.text(3.3, y1 + 0.25, 'Divorcio (hace 20a)\nRelación mala ⚡', color='#C0392B', fontsize=8, ha='center')

# 2. Pareja Actual JA y Carlos (Doble línea de convivencia)
ax.plot([x_ja + 0.3, x_carlos - 0.3], [y1 + 0.05, y1 + 0.05], color='#27AE60', lw=2)
ax.plot([x_ja + 0.3, x_carlos - 0.3], [y1 - 0.05, y1 - 0.05], color='#27AE60', lw=2)
ax.text((x_ja + x_carlos)/2, y1 + 0.25, 'Pareja actual / Convivencia', color='#27AE60', fontsize=8, ha='center', fontweight='bold')

# Delimitación de Hogar Actual (Casa propia)
rect_hogar = patches.FancyBboxPatch((x_ja - 0.5, y1 - 0.9), (x_carlos - x_ja) + 1.0, 1.5,
                                    boxstyle="round,pad=0.1", fill=False, edgecolor='#27AE60', linestyle=':', linewidth=1.5)
ax.add_patch(rect_hogar)
ax.text(x_carlos + 0.1, y1 - 0.75, '🏠 Casa propia\n(Todos los servicios)', fontsize=8, color='#1E8449')

# 3. Unión filial (JA / Silvia -> Adriana)
ax.plot([x_ja, x_ja], [y1 - 0.3, y2 + 0.8], color='#333333', lw=1.5)
ax.plot([x_ja, x_adriana], [y2 + 0.8, y2 + 0.3], color='#333333', lw=1.5)

# Buena relación y distancia geográfica
ax.annotate('', xy=(x_adriana - 0.25, y2 + 0.3), xytext=(x_ja - 0.1, y1 - 0.3),
            arrowprops=dict(arrowstyle="<->", color="#2980B9", lw=2, linestyle='-'))
ax.text(3.9, 4.6, 'Buena relación\n(Vive en Chihuahua)', fontsize=8, color='#2980B9', fontweight='bold', ha='center')

# 4. Matrimonio Adriana y Marco
ax.plot([x_adriana + 0.3, x_marco - 0.3], [y2, y2], color='#333333', lw=1.5)

# 5. Descendencia (Adriana / Marco -> Bebé)
x_union_padres = (x_adriana + x_marco) / 2
ax.plot([x_union_padres, x_union_padres], [y2, y2 - 0.8], color='#333333', lw=1.5)
ax.plot([x_union_padres, x_bebe], [y2 - 0.8, y2 - 0.8], color='#333333', lw=1.5)
ax.plot([x_bebe, x_bebe], [y2 - 0.8, y3 + 0.3], color='#333333', lw=1.5)

# --- SIMBOLOGÍA / LEYENDA ---
rect_leg = patches.FancyBboxPatch((0.3, 0.3), 3.2, 2.2, boxstyle="round,pad=0.1", facecolor='#FAFAFA', edgecolor='#CCCCCC', linewidth=1)
ax.add_patch(rect_leg)
ax.text(0.4, 2.2, "SIMBOLOGÍA", fontsize=9, fontweight='bold')

ax.add_patch(patches.Rectangle((0.5, 1.8), 0.2, 0.2, facecolor='#D0E1FD', edgecolor='black'))
ax.text(0.8, 1.83, "Hombre", fontsize=8)

ax.add_patch(patches.Circle((0.6, 1.55), 0.1, facecolor='#FFE6E6', edgecolor='black'))
ax.text(0.8, 1.5, "Mujer", fontsize=8)

ax.add_patch(patches.Rectangle((0.5, 1.15), 0.2, 0.2, facecolor='#D0E1FD', edgecolor='#1B4F72', linewidth=2))
ax.add_patch(patches.Rectangle((0.52, 1.17), 0.16, 0.16, facecolor='none', edgecolor='#1B4F72', linewidth=1))
ax.text(0.8, 1.2, "Caso Índice (Paciente)", fontsize=8)

ax.plot([0.5, 0.7], [0.9, 0.9], color='#27AE60', lw=2)
ax.text(0.8, 0.85, "Convivencia / Pareja", fontsize=8)

ax.plot([0.5, 0.7], [0.6, 0.6], color='#C0392B', lw=1.5, linestyle='--')
ax.text(0.8, 0.55, "Divorcio / Conflicto", fontsize=8)

plt.tight_layout()
plt.show()