# =========================================================================================
# Programa para generar mapas 2D superpuestas  Manuscrito AUTOCONSISTENTE 3.2 2da rev.=====
# Para visualizar Element de matriz (Mij), energías subb Eij y COEF vs (gamma, d)     =====
# Cálculo autoconsistente algoritmo Dz de una estructura Doble Delta dopada en GaAs   =====
#==========================================================================================
# Copyright Eddy Rabanales Marquez Oct 2026.      UJAT-DAIA-IEE, UAEM-FCQeI-DIATS.    =====
#==========================================================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from   pathlib import Path
Ry   = 5.8341           #Constante de Rydberg en meV ($\epsilon_r$ = 12.5). Ry = 5.24 para $\epsilon_r$ = 13.18 
a0   = 98.72030089;     #Radio de Bohr 'reducido' en Angstrom
# Define la ruta absoluta al archivo .npz de forma dinámica
# __file__ es este script. parent es 'src'. El segundo parent es la raíz del repositorio
ruta_datos1 = Path(__file__).parent.parent / 'data' / 'energies_and_matrix_elements.npz'
ruta_datos2 = Path(__file__).parent.parent / 'data' / 'optical_coefficients.npz'

# ==========================================
# 1. CONFIGURACIÓN DE FUENTES (Nivel JCR)
# ==========================================
# Tamaños grandes y tipografía LaTeX para legibilidad óptima al reducir la imagen
plt.rcParams.update({
    'mathtext.fontset': 'cm',
    'font.family': 'serif',
    'font.size': 18,         # Tamaño base grande
    'axes.labelsize': 22,    # Etiquetas de ejes (gamma, d) aún más grandes
    'axes.titlesize': 18,    # Títulos de los paneles
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'legend.fontsize': 16
})

# ==========================================
# 2. CARGAR LOS DATOS
# ==========================================
print("Cargando datos Mij y Eij del archivo .npz ...")
datos = np.load(ruta_datos1)
# Extraer mallas espaciales
gamma = datos['Asim_grid']
d     = datos['d_grid']
# Extraer matrices
Mij_NOR = np.abs(datos['Mij_NOR'])
Mij_SHG = np.abs(datos['Mij_SHG'])
Mij_THG = np.abs(datos['Mij_THG'])
E10     = datos['E10']
E20     = datos['E20']
E30     = datos['E30']

#---- Cargar datos de los Coeficientes de archivo .npz
data = np.load(ruta_datos2)
NOR = data['MAX_NOR']
SHG = data['MAX_SHG']
THG = data['MAX_THG']

# ==========================================
# 3. FUNCIÓN PARA MARCAR LA REGIÓN >80%
# ==========================================
def agregar_region_optima(ax, rect_):
    g_min = rect_[0];    g_max = rect_[1]
    d_min = rect_[2];    d_max = rect_[3]
    # Intervalo de valores para gama: [g_min, g_max]
    # Intervalo de valores para d:    [d_min, d_max] 
    # Creamos un rectángulo (x_esquina, y_esquina, ancho, alto)
    rect = patches.Rectangle(
        (g_min, d_min), g_max - g_min, d_max - d_min,
        linewidth=3.5, edgecolor='white', facecolor='none', linestyle='--', zorder=10
    )
    # Sombra negra sutil para que contraste sin importar el color de fondo del mapa
    rect_shadow = patches.Rectangle(
        (g_min, d_min), g_max - g_min, d_max - d_min,
        linewidth=5, edgecolor='black', facecolor='none', linestyle='-', zorder=9, alpha=0.6
    )
    ax.add_patch(rect_shadow)
    ax.add_patch(rect)

# ==========================================
# 4. GENERACIÓN DE LA FIGURA
# ==========================================
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 7.3))
cmap_choice = 'turbo' # Mapa perceptualmente uniforme y colorido
cbar_kwargs = {'orientation': 'horizontal', 'fraction': 0.06, 'pad': 0.14}


# =================PANELES DEL NOR=========================================
# --- PANEL A: Elemento de Matriz (Dipolo) ---
# contourf hace el rellenado de color continuo (heatmap suavizado)
Area_NOR = [0.15, 0.65, 67.0, 140.0]
cp1 = ax1.contourf(gamma, d, Mij_NOR, levels=50, cmap=cmap_choice)
ax1.set_title(r'(a) Dipole factor $M_{01}^{2}(M_{11}-M_{00})$')
ax1.set_xlabel(r'$\gamma$')
ax1.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax1, Area_NOR)
cbar1 = fig.colorbar(cp1, ax=ax1, **cbar_kwargs)
vmin, vmax = cp1.get_clim();      vmid = (vmin + vmax) / 2.0
cbar1.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f}'])
cbar1.ax.tick_params(labelsize=15) 

# --- PANEL B: Energía de Subbanda ---
cp2 = ax2.contourf(gamma, d, E10*Ry, levels=50, cmap=cmap_choice) # Usamos plasma para diferenciar energías
ax2.set_title(r'(b) Subband energy $E_{10}$')
ax2.set_xlabel(r'$\gamma$')
ax2.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax2, Area_NOR)
cbar2 = fig.colorbar(cp2, ax=ax2, **cbar_kwargs)
vmin, vmax = cp2.get_clim();       vmid = (vmin + vmax) / 2.0
cbar2.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f} (meV)'])
cbar2.ax.tick_params(labelsize=15)

# --- PANEL C: Coeficiente Total NOR ---
cp3 = ax3.contourf(gamma, d, NOR, levels=50, cmap=cmap_choice)
# Añadimos líneas de contorno sólidas encima para marcar topología
ax3.contour(gamma, d, NOR, levels=20, colors='black', linewidths=0.5, alpha=0.5)
ax3.set_title(r'(c) NOR amplitude')
ax3.set_xlabel(r'$\gamma$')
ax3.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax3, Area_NOR)
cbar3 = fig.colorbar(cp3, ax=ax3, **cbar_kwargs)
vmin, vmax = cp3.get_clim();       vmid = (vmin + vmax) / 2.0
cbar3.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', fr'{vmax:.2f} $\times 10^{{-3}}$ (m/V)'])
cbar3.ax.tick_params(labelsize=15)


'''
# =================PANELES DEL SHG=========================================
# --- PANEL A: Elemento de Matriz (Dipolo) ---
# contourf hace el rellenado de color continuo (heatmap suavizado)
Area_SHG = [0.25, 0.375, 103.0, 166.0]
cp1 = ax1.contourf(gamma, d, Mij_SHG, levels=50, cmap=cmap_choice)
ax1.set_title(r'(a) Dipole factor $|M_{01}M_{12}M_{20}|$')
ax1.set_xlabel(r'$\gamma$')
ax1.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax1, Area_SHG)
cbar1 = fig.colorbar(cp1, ax=ax1, **cbar_kwargs)
vmin, vmax = cp1.get_clim();      vmid = (vmin + vmax) / 2.0
cbar1.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f}'])
cbar1.ax.tick_params(labelsize=15)

# --- PANEL B: Energía de Subbanda ---
cp2 = ax2.contourf(gamma, d, E10*Ry, levels=50, cmap=cmap_choice) # Usamos plasma para diferenciar energías
ax2.set_title(r'(b) Subband energy $E_{10}$')
ax2.set_xlabel(r'$\gamma$')
ax2.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax2, Area_SHG)
cbar2 = fig.colorbar(cp2, ax=ax2, **cbar_kwargs)
vmin, vmax = cp2.get_clim();       vmid = (vmin + vmax) / 2.0
cbar2.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f} (meV)'])
cbar2.ax.tick_params(labelsize=15)

# --- PANEL C: Coeficiente Total SHG ---
cp3 = ax3.contourf(gamma, d, SHG, levels=50, cmap=cmap_choice)
# Añadimos líneas de contorno sólidas encima para marcar topología
ax3.contour(gamma, d, SHG, levels=20, colors='black', linewidths=0.5, alpha=0.5)
ax3.set_title(r'(c) SHG amplitude')
ax3.set_xlabel(r'$\gamma$')
ax3.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax3, Area_SHG)
cbar3 = fig.colorbar(cp3, ax=ax3, **cbar_kwargs)
vmin, vmax = cp3.get_clim();       vmid = (vmin + vmax) / 2.0
cbar3.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', fr'{vmax:.2f} $\times 10^{{-5}}$ (m/V)'])
cbar3.ax.tick_params(labelsize=15)
'''

'''
# =================PANELES DEL THG=========================================
# --- PANEL A: Elemento de Matriz (Dipolo) ---
# contourf hace el rellenado de color continuo (heatmap suavizado)
Area_THG = [0.00, 0.05, 139.0, 180.0]
cp1 = ax1.contourf(gamma, d, Mij_THG, levels=50, cmap=cmap_choice)
ax1.set_title(r'(a) Dipole factor $|M_{01}M_{12}M_{23}M_{30}|$')
ax1.set_xlabel(r'$\gamma$')
ax1.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax1, Area_THG)
cbar1 = fig.colorbar(cp1, ax=ax1, **cbar_kwargs)
vmin, vmax = cp1.get_clim();      vmid = (vmin + vmax) / 2.0
cbar1.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f}'])
cbar1.ax.tick_params(labelsize=15) 

# --- PANEL B: Energía de Subbanda ---
cp2 = ax2.contourf(gamma, d, E30*Ry, levels=50, cmap=cmap_choice) # Usamos plasma para diferenciar energías
ax2.set_title(r'(b) Subband energy $E_{30}$')
ax2.set_xlabel(r'$\gamma$')
ax2.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax2, Area_THG)
cbar2 = fig.colorbar(cp2, ax=ax2, **cbar_kwargs)
vmin, vmax = cp2.get_clim();       vmid = (vmin + vmax) / 2.0
cbar2.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', f'{vmax:.2f} (meV)'])
cbar2.ax.tick_params(labelsize=15)

# --- PANEL C: Coeficiente Total THG ---
cp3 = ax3.contourf(gamma, d, THG, levels=50, cmap=cmap_choice)
# Añadimos líneas de contorno sólidas encima para marcar topología
ax3.contour(gamma, d, THG, levels=20, colors='black', linewidths=0.5, alpha=0.5)
ax3.set_title(r'(c) THG amplitude')
ax3.set_xlabel(r'$\gamma$')
ax3.set_ylabel(r'$d$ (Å)', labelpad=0)
agregar_region_optima(ax3, Area_THG)
cbar3 = fig.colorbar(cp3, ax=ax3, **cbar_kwargs)
vmin, vmax = cp3.get_clim();       vmid = (vmin + vmax) / 2.0
cbar3.set_ticks([vmin, vmid, vmax], labels=[f'{vmin:.2f}', f'{vmid:.2f}', fr'{vmax:.2f} $\times 10^{{-11}}$ (m$^2$/V$^2$)'])
cbar3.ax.tick_params(labelsize=15)
'''

# ==========================================
# 5. AJUSTES FINALES
# ==========================================
plt.tight_layout()
plt.subplots_adjust(wspace=0.3, bottom=0.1) # Espacio entre paneles para que no choquen las barras de color
plt.show()
