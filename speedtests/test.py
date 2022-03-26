import grequests


ITERATIONS = 100
URL = "http://localhost:3000/file"
FILENAME = "./results.csv"

results = (grequests.get(URL) for _ in range(ITERATIONS))
results = grequests.map(results)


with open(FILENAME, "w") as f:
    # write header
    f.write("Index;Time [s];\n")
    for i, res in enumerate(results, 1):        
        # check for valid status code
        if res.status_code != 200:
            raise Exception(f"Statuscode: {res.status_code}")

        # write results to file
        f.write(";".join([str(i), str(res.elapsed.total_seconds()), "\n"]))

