package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
	"time"
)

type StatusRecorder struct {
	http.ResponseWriter
	Status int
}

func (r *StatusRecorder) WriteHeader(status int) {
	r.Status = status
	r.ResponseWriter.WriteHeader(status)
}

func WithLogging(h http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		recorder := &StatusRecorder{
			ResponseWriter: w,
			Status:         200,
		}
		h.ServeHTTP(recorder, r)
		log.Printf("Handling request for %s from %s, status: %d", r.URL.Path, r.RemoteAddr, recorder.Status)
	})
}

func dateTimeRecorder() {
	for {
		currentTime := time.Now().String()
		fmt.Println(currentTime)
		time.Sleep(time.Second)
	}
}

func main() {
	httpRequestHandler := http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
		response := "Server response time: " + time.Now().String()
		fmt.Fprintln(resp, response)
	})
	handlerWithLogging := WithLogging(httpRequestHandler)
	http.Handle("/", handlerWithLogging)
	defaultPort := os.Getenv("PORT")
	if len(defaultPort) == 0 {
		defaultPort = "8080"
	}

	go dateTimeRecorder()

	err := http.ListenAndServe(":"+defaultPort, nil)
	if err != nil {
		fmt.Println(err)
	}

}
