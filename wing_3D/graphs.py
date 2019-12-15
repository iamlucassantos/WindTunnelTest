import os
from wing_3D.data_ingestion import ingest_experimental, ingest_XFLR5
import matplotlib.pyplot as plt

print(os.listdir('..'))
# os.chdir('wing_3D')
experiment = ingest_experimental('3D_balance/corr_test.txt')
simulation = ingest_XFLR5("XFLR5/finalRe735000-45m s.txt")


for y_label in ['C_L', 'C_D', 'C_m']:
    plt.plot(experiment['alpha'], experiment[y_label], label="experimental")
    plt.plot(simulation['alpha'], simulation[y_label], label="simulated")
    plt.legend()
    plt.xlabel('AoA [deg]')
    if y_label == "C_L":
        plt.title("Lift curve")
        plt.ylabel("Lift coefficient [-]")
    if y_label == "C_D":
        plt.title("Drag curve")
        plt.ylabel("Drag coefficient [-]")
    if y_label == "C_m":
        plt.title("Moment curve")
        plt.ylabel("Moment coefficient [-]")
    os.chdir('graphs')
    plt.savefig(f"alpha_vs_{y_label}.pdf", format='pdf')
    os.chdir('..')
    plt.show()

# Let's now make a drag polar.
plt.plot(simulation['C_D'], simulation['C_L'])
plt.plot(experiment['C_D'], experiment['C_L'])
plt.title('Drag polar')
plt.ylabel('Lift coefficient [-]')
plt.xlabel('Drag coefficient')
os.chdir('graphs')
plt.savefig('drag_polar.pdf', format='pdf')
plt.show()
os.chdir('..')
