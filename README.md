# HNG12 Backend Task API

This Flask-based API classifies a given number and provides interesting mathematical properties about it, along with a fun fact from the Numbers API.
## 🚀 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Summiedev/hng-backend-2.git
```

### 2️⃣ Navigate into the project directory
```bash
cd hng-backend-2
```

### 3️⃣ Create a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate   # On Windows
```

### 4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run the application
```bash
python app.py
```

### 6️⃣ Access the API locally
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser or use Postman/cURL.

## 📌 API Documentation

### Base URL:
```
https://hng-backend-2-w4oe.onrender.com
```

### Endpoint:
```
GET https://hng-backend-2-w4oe.onrender.com/api/classify-number?number=371
```

### Response Format (200 OK):
```json
{
	"digit_sum": 11,
	"fun_fact": "371 is a narcissistic number.",
	"is_perfect": false,
	"is_prime": false,
	"number": 371,
	"properties": [
		"armstrong",
		"odd"
	]
}
```

## 🛠 Example Usage

### Using Insomnia or Postman
```
GET https://hng-backend-2-w4oe.onrender.com/api/classify-number?number=<num>
```

### Using Python Requests:
```python
import requests

response = requests.get("https://hng-backend-2-w4oe.onrender.com/api/classify-number?number=<num>")
print(response.json())
```

## 📌 Deployment

- Hosting platform: Render
- Public API URL: Your Public API URL

## 🌍 CORS Handling

CORS is enabled to allow cross-origin requests, ensuring the API is accessible from different domains.

## 📌 Version Control & Documentation

- **GitHub Repository:** View Source Code
- **Repository Visibility:** Public
- **Documentation:** This README file contains all necessary details.

## 🔗 Hire Python Developers
Looking for skilled Python developers? Check out [HNG Tech Python Developers](https://hng.tech/hire/python-developers).
