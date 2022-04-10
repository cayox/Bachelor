package main

import (
	"log"
	"net/http"
)

// create HTTP Handle Func that serves the testfile
func fileServe(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "./testfile.html")
}

func main() {
	http.HandleFunc("/file", fileServe)

	log.Println("Listening on :3000...")
	err := http.ListenAndServe(":3000", nil)
	if err != nil {
		log.Fatal(err)
	}
}
