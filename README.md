### Risikoanalyse API

Dieses Projekt wurde im Rahmen eines technischen Auswahlverfahrens erstellt.

### 📝 Beschreibung

Eine einfache REST API zur Verwaltung von Risiken und zugehörigen Aufgaben.

- Beim Erstellen eines Risikos werden im Hintergrund zwei Aufgaben erzeugt.
- Nach ca. 10 Sekunden wird der Status automatisch auf `completed` gesetzt.
- Die API unterstützt das Anlegen, Abrufen und Testen von Risiken.

---

###  Startanleitung

## 1️⃣ Lokale Ausführung (ohne Docker)

#### Voraussetzungen:

- Python 3.11+
- Git
- pip

### Schritte:

#### 1. Projekt klonen
```bash
git clone https://github.com/roshanzadeh1994/risk_assessment.git
```
```bash
cd risk_assessment
```

#### 2. Virtuelle Umgebung erstellen
```bash
python -m venv venv
```
### Aktivieren:
#### Windows:

```bash
venv\Scripts\activate
```
#### Linux/macOS:
```bash
source venv/bin/activate
```
#### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```
#### 4. App starten
```bash
uvicorn main:app --reload
```
- ##### API läuft jetzt unter:
```bash
http://localhost:8000
 ```

- ##### Swagger-Dokumentation:
```bash
http://localhost:8000/docs
```
---

## 2️⃣ Ausführung mit Docker

#### Schritte:
```bash
git clone https://github.com/roshanzadeh1994/risk_assessment.git
```
```bash
cd risk_assessment
```
#### 1. Image bauen

```bash
docker build -t risk-api .
 ```

#### 2. Container starten

```bash
docker run -p 8000:8000 risk-api
 ```


- ##### API:
  ```bash
  http://localhost:8000
  ```

- ##### Swagger UI:
  ```bash
  http://localhost:8000/docs
  ```
---

### 🧪 Tests ausführen
Die Anwendung enthält mehrere modulare Tests (8 Dateien),
die sich im Ordner /tests befinden und unterschiedliche Funktionalitäten prüfen –
z. B. Risikoerstellung, Validierung, Statusänderung und Fehlerfälle.

Tests können mit folgendem Befehl ausgeführt werden:
```bash 
pytest
```

---

### 🔄 CI (Continuous Integration)

Dieses Projekt verwendet GitHub Actions zum automatischen Testen bei jedem Commit/Push auf den `main` Branch.  
Die Konfiguration befindet sich in `.github/workflows/CI.yml`.

