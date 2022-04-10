from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib
import pandas as pd
import sys
from datetime import timedelta

def plot_webserver():
    GO_FILE = "./results_go.csv"
    FLASK_FILE = "./results_flask.csv"

    go_data = pd.read_csv(GO_FILE, sep=";")
    flask_data = pd.read_csv(FLASK_FILE, sep=";")

    fig, ax = plt.subplots()
    fig.suptitle('Antwortzeit bei asynchronen Anfragen einer HTML Datei')

    ax.plot(go_data["Index"], go_data["Time [s]"], label="Go (HTTP)")
    ax.plot(flask_data["Index"], flask_data["Time [s]"], label="Python (Flask)")

    ax.set_xlabel("Request Nummer")
    ax.set_ylabel("Zeit [s]")

    ax.grid()
    ax.legend()

    plt.savefig("results.png")

def plot_validation():
    def parse_time(time):
        minutes, seconds = [int(x) for x in time.split(":")]
        return timedelta(minutes=minutes, seconds=seconds).total_seconds()

    TESTHUB_FILE = "./mousetracking_testhub.csv"
    MANUAL_FILE = "./mousetracking.csv"

    testhub_data = pd.read_csv(TESTHUB_FILE, sep=";", decimal=",")
    testhub_data["Zeit"] = testhub_data["Zeit"].apply(parse_time)

    manual_data = pd.read_csv(MANUAL_FILE, sep=";", decimal=",")
    manual_data["Zeit"] = manual_data["Zeit"].apply(parse_time)

    labels = ["Manuell", "TestHub"]
    width = 0.35
    for col in testhub_data.columns[1:5]:
        print(f"Plotting {col}")
        fig, ax = plt.subplots()

        data_before = [0, 0]
        for i, (label, color) in enumerate(zip(["Folgetest", "Wartung einsehen", "neue Wartung"], ["#1e3a8a", "#2563eb", "#93c5fd"])):
            data = (manual_data[col][i], testhub_data[col][i])
            ax.bar(labels, data, width, label=label, bottom=data_before, color=color, zorder=3)
            data_before[0] += data[0]
            data_before[1] += data[1]

        ax.set_ylabel(col if col != "Cursordistanz" else "Mauszeigerdistanz [m]")
        if col == "Zeit":
            ax.set_ylabel("Zeit [m:ss]")
            def format_func(x, pos):
                minutes = int((x % 3600) // 60)
                seconds = int(x % 60)

                return "{:d}:{:02d}".format(minutes, seconds)

            formatter = FuncFormatter(format_func)
            ax.yaxis.set_major_formatter(formatter)
            # this ensures each bar has a 'date' label
            ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(base=1))
        elif col == "Mausrad_Ticks":
            ax.set_ylabel("Mausrad Ticks")
            
        ax.grid(zorder=0)
        ax.legend()

        # plt.show()
        plt.savefig(f"validierung_{col}.png", )
        plt.close()


# 
f = {"webserver": plot_webserver, "validation": plot_validation}[sys.argv[1]]()
