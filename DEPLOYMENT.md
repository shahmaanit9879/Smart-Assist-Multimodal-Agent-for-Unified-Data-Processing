# Deployment Instructions

1. Clone the repo.  
2. Install dependencies: pip install -r requirements.txt  
3. Run API: python src/serve.py  
4. (Optional) Build Docker: docker build -t smartassist .  
5. Run in Docker: docker run -p 8080:8080 smartassist
