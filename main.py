from fastapi import FastAPI

app = FastAPI()


# 1. Oddiy tekshirish
@app.get("/")
def home():
    return {"status": "Server ishlayapti", "author": "Davronbek"}


# 2. "Aqlli" funksiya: Ism bilan salomlashish
# Brauzerda: /salom?ism=Ali deb yozilsa ishlaydi
@app.get("/salom")
def salom_ber(ism: str):
    return {"xabar": f"Assalomu alaykum, {ism}! Ishlaringiz yaxshimi?"}


# 3. Chatbot mantig'i (Sun'iy intellektdan oldingi bosqich)
# Biz unga qoidalarni o'rgatamiz
@app.get("/chat")
def bot_bilan_gaplash(savol: str):
    # Kichik harflarga o'tkazamiz (katta-kichik harf muammosi bo'lmasligi uchun)
    savol = savol.lower()

    if "narx" in savol or "pul" in savol:
        javob = "Bizning xizmatlar narxi kelishilgan holda. Boshlang'ich narx: $100"
    elif "wordpress" in savol:
        javob = "Ha, men WordPress bo'yicha mutaxassisman. Qanday yordam kerak?"
    elif "kim" in savol:
        javob = "Men Davronbek yaratgan Python Microservice'man."
    else:
        javob = "Uzr, bu savolga hali javobim yo'q. AI ulaganingizdan keyin aytaman :)"

    return {"bot_javobi": javob}


# Serverni ishga tushirish qismi
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)