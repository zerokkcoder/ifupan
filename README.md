# Stock Fupan System

## Project Structure

This project is organized as a monorepo with separate frontend and backend directories.

- **`frontend/`**: Vue 3 + Vite + TypeScript application
- **`backend/`**: FastAPI + Python application

## Quick Start

### Frontend

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies and run the development server:

```bash
npm install
npm run dev
```

### Backend

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment and install dependencies:

```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn app.main:app --reload
```
