from fastapi import FastAPI

app = FastAPI(
    title="order-service",
    description="Sample order API with status information",
    version="1.0.0",
)

@app.get("/health")
def health():
    return {"status": "UP", "application": "order-service"}

@app.get("/api/orders")
def orders():
    return [
        {"order_id": "ORD-1001", "item": "Laptop", "quantity": 1, "status": "CONFIRMED"},
        {"order_id": "ORD-1002", "item": "Keyboard", "quantity": 2, "status": "PROCESSING"},
        {"order_id": "ORD-1003", "item": "Mouse", "quantity": 1, "status": "SHIPPED"},
    ]

