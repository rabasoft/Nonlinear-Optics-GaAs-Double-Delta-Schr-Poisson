# =========================================================================================
# Programa para generar las gráficas del manuscrito AUTOCONSISTENTE 3.2  2da revisión =====
# Agrupa la superficie y su correspondiente vista superior marcando el area óptima    =====
# Cálculo autoconsistente algoritmo Dz de una estructura Doble Delta dopada en GaAs   =====
#==========================================================================================
# Copyright Eddy Rabanales Marquez Sept 2026.     UJAT-DAIA-IEE, UAEM-FCQeI-DIATS.    =====
#==========================================================================================
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FuncFormatter
from pathlib import Path
#=================================================================================
def dibuja_region(x_min, x_max, y_min, y_max, ax):
   # Coordenadas de los vértices del rectángulo (el último punto cierra el ciclo)
    rect_x = [x_min, x_max, x_max, x_min, x_min]
    rect_y = [y_min, y_min, y_max, y_max, y_min]
    rect_z = [0, 0, 0, 0, 0]
    # Dibujamos el contorno con un color contrastante y mayor grosor
    ax.plot(rect_x, rect_y, rect_z, color='black', linewidth=3, zorder=5, label='Región>80%')
#=================================================================================
# ==========================================
# 1. CARGAR LOS DATOS SIMULADOS
# ==========================================
print("Cargando datos del archivo...")
        #'datos_superficies_opticas 200 nm 4.npz'
        #'datos_superficies_opticas 200nm 5.npz'
        #'datos_superficies_opticas 6.npz2.npz'
nfile = Path(__file__).parent.parent / 'data' / 'optical_coefficients.npz'
datos = np.load(nfile)
if str(nfile).find('npz2')<0:        # Se trata de superficie con base (ASIM, d)
    print('superficie (ASIM, d) identificada')
    lb_x = r'$\mathrm{\gamma}$'; 
    lb_y = '$d$ (Å)'
    Val_x= datos['Asim_grid']
    Val_y= datos['d_grid']
else:                           # Se trata de superficie con base (F, B)
    print('superficie (F, B) identificada')
    lb_x = '$F$ (kV/cm)';
    lb_y = '$B$ (T)'
    Val_x= datos['F_grid']
    Val_y= datos['B_grid']

# Extraer las matrices de COEF OPT
MAX_NOR  = datos['MAX_NOR']
MAX_SHG  = datos['MAX_SHG']
MAX_THG  = datos['MAX_THG']
print("Datos cargados correctamente.")

# ==========================================
# 2. CONFIGURACIÓN DE FORMATO CIENTÍFICO (Nivel JCR)
# ==========================================
plt.rcParams.update({'mathtext.fontset': 'cm', 'font.family': 'serif', 'font.size': 16})

# ==========================================
# 3. GENERACIÓN DEL PANEL 3D IZQUIERDO
# ==========================================                                                                            .
fig = plt.figure(figsize=(14, 7)) 
'''
# --- PANEL 1: NOR ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf1 = ax1.plot_surface(Val_x, Val_y, MAX_NOR, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax1.set_xlabel(lb_x, labelpad=8, size=18)
ax1.set_ylabel(lb_y, labelpad=8, size=18)
ax1.set_zlabel(r'MAX|$\chi_{0}^{(2)}$|$\times 10^{-3}$ (m/V)', labelpad=5)
ax1.view_init(elev=45, azim=-65)
'''

'''
# --- PANEL 2: SHG ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf1 = ax1.plot_surface(Val_x, Val_y, MAX_SHG, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax1.set_xlabel(lb_x, labelpad=8, size=18)
ax1.set_ylabel(lb_y, labelpad=8, size=18)
ax1.set_zlabel(r'MAX|$\chi_{2\omega}^{(2)}$|$\times 10^{-5}$ (m/V)', labelpad=5)
ax1.view_init(elev=45, azim=-65)
'''


# --- PANEL 3: THG ---
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf1 = ax1.plot_surface(Val_x, Val_y, MAX_THG, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax1.set_xlabel(lb_x, labelpad=8, size=18)
ax1.set_ylabel(lb_y, labelpad=8, size=18)
ax1.set_zlabel(r'MAX|$\chi_{3\omega}^{(3)}$|$\times 10^{-11}$ (m$^2$/V$^2$)', labelpad=10)
ax1.view_init(elev=45, azim=-65)           #Valor inicial: ax3.view_init(elev=25, azim=225)

# ===============================================
# 4. GENERACIÓN DEL  PANEL 3D DERECHO Vista TOP==
# ===============================================
'''
# --- PANEL 1: NOR ---
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(Val_x, Val_y, MAX_NOR, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax2.set_xlabel(lb_x, labelpad=6, size=18)
ax2.set_ylabel(lb_y, labelpad=12, size=18)
ax2.text2D(0.38, 0.90, r'MAX|$\chi_{0}^{(2)}$|$\times 10^{-3}$ (m/V)', transform=ax2.transAxes, rotation=0, color='black')
ax2.set_zticks([np.min(MAX_NOR), np.max(MAX_NOR)])
dibuja_region(0.125, 0.625, 67, 144, ax2)  # γ ∈ [0.125, 0.625] and d ∈ [67.0, 144.0] Å
ax2.view_init(elev=90, azim=-90)
'''

'''
# --- PANEL 2: SHG ---
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(Val_x, Val_y, MAX_SHG, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax2.set_xlabel(lb_x, labelpad=6, size=18)
ax2.set_ylabel(lb_y, labelpad=12, size=18)
ax2.text2D(0.38, 0.90, r'MAX|$\chi_{2\omega}^{(2)}$|$\times 10^{-5}$ (m/V)', transform=ax2.transAxes, rotation=0, color='black')
ax2.set_zticks([np.min(MAX_SHG), np.max(MAX_SHG)])
dibuja_region(0.240, 0.375, 103, 166, ax2) # γ ∈ [0.250, 0.375] and d ∈ [103.0, 166.0] Å.
ax2.view_init(elev=90, azim=-90)
'''


# --- PANEL 3: THG ---
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(Val_x, Val_y, MAX_THG, cmap='jet', linewidth=0.1, edgecolor='k', alpha=0.8)
ax2.set_xlabel(lb_x, labelpad=6, size=18)
ax2.set_ylabel(lb_y, labelpad=12, size=18)
ax2.text2D(0.38, 0.90, r'MAX|$\chi_{3\omega}^{(3)}$|$\times 10^{-11}$ (m$^2$/V$^2$)', transform=ax2.transAxes, rotation=0, color='black')
ax2.set_zticks([np.min(MAX_THG), np.max(MAX_THG)])
dibuja_region(-0.030, 0.050, 142, 183, ax2) # γ ∈ [0.000, 0.050] and d ∈ [139.0, 180.0] Å
ax2.view_init(elev=90, azim=-90)           #Valor inicial: ax3.view_init(elev=25, azim=225)

# Barra de color lateral como referencia de magnitud
#cbar = fig.colorbar(surf3, shrink=0.5, aspect=12, pad=0.1)
#cbar.set_label('Magnitud Máxima', rotation=270, labelpad=20)
# Ajuste de márgenes para evitar solapamientos entre paneles
plt.tight_layout()
plt.subplots_adjust(wspace=0.15) 
plt.show()
