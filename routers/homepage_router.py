from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["Homepage"])

# Simple homepage endpoint
@router.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <h2>🛠️ Technische Aufgabe für Backend-Entwickler</h2>
    <p><strong>👤 Autor:</strong> Amir Roshanzadeh</p>
    <hr>
    <p>📘 Über das <strong>Swagger UI</strong> können Sie das API-Design einsehen und testen:</p>
    <p>🔗 <a href='http://localhost:8000/docs'>http://localhost:8000/docs</a></p>
    """
    