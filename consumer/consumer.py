from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/process")
async def process_data(request: Request):
    data = await request.json()
    print(f"Received data: {data}")
    response = {"status": "success", "processed_message": data["message"].upper()}
    return response
