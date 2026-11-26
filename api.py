from fastapi import FastAPI
import socket
import datetime

app = FastAPI(
    title="Tienda API - Kubernetes",
    description="API para la práctica de despliegue a Kubernetes con GitHub Actions Self-Hosted Runner",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "mensaje": "Bienvenido a la Tienda API en Kubernetes",
        "version": "1.0.0",
        "pod_hostname": socket.gethostname(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/productos")
def listar_productos():
    return [
        {"id": 1, "nombre": "Laptop Pro", "precio": 18500.0, "stock": 10},
        {"id": 2, "nombre": "Teclado Mecanico", "precio": 1200.0, "stock": 25},
        {"id": 3, "nombre": "Mouse Inalambrico", "precio": 450.0, "stock": 40}
    ]

@app.get("/health")
def health():
    return {"status": "ok", "app": "tienda-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
