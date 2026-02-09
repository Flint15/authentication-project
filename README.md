# Authentication Project ⸜(｡˃ ᵕ ˂ )⸝♡

## 🛠️ Tech Stack

### Frontend

- [TypeScript](https://www.typescriptlang.org/)
- HTML5/CSS3

### Backend

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18.0.0 or higher)

```bash
  node --version  # Should be v18+
```

- **npm** (v9.0.0 or higher)

```bash
  npm --version  # Should be v9+
```

- **Python** (3.9 or higher)

```bash
  python --version  # Should be 3.9+
```

### Installation

1. **Clone the repository**

```bash
   git clone https://github.com/Flint15/authentication-project.git
   cd authentication-project
```

2. **Install frontend dependencies**

```bash
   npm install
```

3. **Set up Python backend**

```bash
   cd backend

   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
```

### Running the Application

**Run Backend and Frontend Separately**

Terminal 1 - Backend:

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python server.py
```

Server runs at `http://127.0.0.1:5000`

Terminal 2 - Frontend Compilation (watch mode):

```bash
npm run dev
```
