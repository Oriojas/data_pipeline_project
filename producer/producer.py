import requests
import time

def produce_data():
    data = {"message": "Hello from producer!"}
    try:
        response = requests.post("http://consumer:8000/process", json=data)
        print(f"Response from consumer: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to consumer: {e}")

if __name__ == "__main__":
    while True:
        produce_data()
        time.sleep(5)  # Produce data every 5 seconds
