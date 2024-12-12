# Data Pipeline Project

This project demonstrates communication between two Docker containers:
- **Producer**: Generates data and sends it to the consumer.
- **Consumer**: Processes the data received from the producer.

The communication is established using HTTP requests, where the producer makes POST requests to the consumer's API endpoint.

---

## **Project Structure**

```plaintext
data_pipeline_project/
├── docker-compose.yml
├── producer/
│   ├── Dockerfile
│   └── producer.py
├── consumer/
│   ├── Dockerfile
│   └── consumer.py
```

---

## **Prerequisites**

1. **Install Docker**
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
2. **Install Docker Compose**
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

---

## **Setup and Execution**

Follow these steps to build and run the project:

### **1. Clone the Repository**
If this project is in a Git repository, clone it:
```bash
git clone <repository_url>
cd data_pipeline_project
```

### **2. Build the Docker Images**
Build the images for both the producer and consumer:
```bash
docker-compose build
```

### **3. Run the Services**
Start the containers using:
```bash
docker-compose up
```

This will start:
- **Producer**: Sends data every 5 seconds.
- **Consumer**: Processes incoming data on port `8000`.

### **4. Verify Communication**

#### **Check Logs**
- **Producer Logs**:
  ```bash
  docker-compose logs producer
  ```
  Example output:
  ```plaintext
  Response from consumer: {'status': 'success', 'processed_message': 'HELLO FROM PRODUCER!'}
  ```

- **Consumer Logs**:
  ```bash
  docker-compose logs consumer
  ```
  Example output:
  ```plaintext
  Received data: {'message': 'Hello from producer!'}
  ```

#### **Test Consumer API Manually**
You can send test data to the consumer directly using `curl`:
```bash
curl -X POST http://localhost:8000/process \
-H "Content-Type: application/json" \
-d '{"message": "Test"}'
```

Expected response:
```json
{
    "status": "success",
    "processed_message": "TEST"
}
```

---

## **Stop the Services**
To stop and remove the containers:
```bash
docker-compose down
```

---

## **Future Extensions**
- **Persist Data**: Store processed data in a database like PostgreSQL or MongoDB.
- **Scalability**: Use Docker Swarm or Kubernetes to scale the producer and consumer services.
- **Messaging System**: Introduce RabbitMQ or Kafka for asynchronous communication.

---

Enjoy testing your data pipeline! 🚀
