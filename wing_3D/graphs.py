import os
from wing_3D.data_ingestion import ingest_experimental, ingest_XFLR5
import matplotlib.pyplot as plt
from matplotlib import rc


rc('text', usetex=True)


experiment = ingest_experimental('3D_balance/corr_test.txt')
simulation = ingest_XFLR5("XFLR5/finalRe735000-45m s.txt")


for y_label in ['C_L', 'C_D', 'C_m']:
    plt.plot(experiment['alpha'], experiment[y_label], label="experimental", marker="o")
    plt.plot(simulation['alpha'], simulation[y_label], label="simulated", marker="o")
    plt.legend()
    plt.xlabel(r'$\alpha$ [deg]')
    plt.ylabel(f'${y_label}$ [-]')
    # plt.title(f'${["Lift", "Drag", "Moment"][["C_L", "C_D", "C_m"].index(y_label)]}$ curve')
    os.chdir('graphs')
    plt.savefig(f"alpha_vs_{y_label}.pdf", format='pdf')
    os.chdir('..')
    plt.show()

# Let's now make a drag polar.
plt.plot(simulation['C_D'], simulation['C_L'], marker="o")
plt.plot(experiment['C_D'], experiment['C_L'], marker="o")
# plt.title('Drag polar')
plt.ylabel('Lift coefficient [-]')
plt.xlabel('Drag coefficient [-]')
os.chdir('graphs')
plt.savefig('drag_polar.pdf', format='pdf')
plt.show()
os.chdir('..')
