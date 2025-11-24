# 1. Asos sifatida rasmiy Python 3.10 versiyasini olamiz (Linux ichida Linux)
FROM python:3.10

# 2. Konteyner ichida /app degan papka ochamiz va o'sha yerda ishlaymiz
WORKDIR /app

# 3. requirements.txt faylini konteynerga nusxalaymiz
COPY requirements.txt .

# 4. Kerakli kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# 5. Qolgan barcha kodlarni (main.py) konteynerga nusxalaymiz
COPY . .

# 6. Konteyner ishga tushganda shu buyruq bajarilsin
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]