import os
from wing_3D.data_ingestion import ingest_experimental, ingest_XFLR5
import matplotlib.pyplot as plt
from matplotlib import rc


rc('text', usetex=True)
plt.style.use('seaborn')


experiment = ingest_experimental('3D_balance/corr_test.txt')
simulation = ingest_XFLR5("XFLR5/finalRe735000-45m s.txt")


for y_label in ['C_L', 'C_D', 'C_m']:
    for i in range(3):
        if i == 0:
            plt.plot(experiment['alpha'], experiment[y_label], label="experimental", marker="o")
            val = "exp"
        elif i == 1:
            plt.plot(simulation['alpha'], simulation[y_label], label="simulated", marker="x")
            val = "sim"
        else:
            plt.plot(experiment['alpha'], experiment[y_label], label="experimental", marker="o")
            plt.plot(simulation['alpha'], simulation[y_label], label="simulated", marker="x")
            val = "exp_sim"
        plt.legend()
        plt.xlabel(r'$\alpha$ [deg]')
        plt.ylabel(f'${y_label}$ [-]')
        # plt.title(f'${["Lift", "Drag", "Moment"][["C_L", "C_D", "C_m"].index(y_label)]}$ curve')
        os.chdir('graphs')
        plt.grid()
        plt.savefig(f"alpha_vs_{y_label}_{val}.pdf", format='pdf')
        os.chdir('..')
        plt.show()

# Let's now make a drag polar.
for i in range(3):
    if i == 0:
        plt.plot(simulation['C_D'], simulation['C_L'], marker="x", label="simulation")
        val = "sim"
    elif i == 1:
        plt.plot(experiment['C_D'], experiment['C_L'], marker="o", label="experimental")
        val = "exp"
    else:
        plt.plot(simulation['C_D'], simulation['C_L'], marker="x", label="simulation")
        plt.plot(experiment['C_D'], experiment['C_L'], marker="o", label="experimental")
        val = "exp_sim"
    plt.ylabel('Lift coefficient [-]')
    plt.xlabel('Drag coefficient [-]')
    os.chdir('graphs')
    plt.grid()
    plt.legend()
    plt.savefig(f'drag_polar_{val}.pdf', format='pdf')
    plt.show()
    os.chdir('..')
