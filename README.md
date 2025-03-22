# Maharbote - Fortune Prediction App

A modern web application that predicts your fortune based on your birth day. Built with FastAPI and a beautiful, responsive frontend.

## Features

- 🎯 Fortune predictions based on birth day
- 🌟 Multiple aspects of life predictions:
  - General fortune
  - Today's fortune
  - Love life
  - Career
  - Health
- 💫 Beautiful, responsive UI
- 🚀 Fast and efficient API
- 📱 Mobile-friendly design

## Tech Stack

- Backend: Python FastAPI
- Frontend: HTML, CSS, JavaScript
- Containerization: Docker
- Styling: Custom CSS with modern design

## Prerequisites

- Docker and Docker Compose
- Python 3.11 (for local development)

## Getting Started

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/maharbote.git
cd maharbote
```

2. Build and run the application:
```bash
docker-compose up --build
```

3. Open your browser and visit:
   - Main application: http://localhost:8000
   - API documentation: http://localhost:8000/docs

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /`: Main application page
- `POST /fortune`: Get fortune prediction
  - Request body:
    ```json
    {
        "day": "Monday",
        "aspect": "general"
    }
    ```
- `GET /health`: Health check endpoint

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI for the amazing web framework
- Docker for containerization
- All contributors and users of the application