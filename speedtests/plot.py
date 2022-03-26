from matplotlib import pyplot as plt
import pandas as pd

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