from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 1. Ma'lumot qolipi (Model)
# WordPressdan bizga qanday ma'lumot kelishini oldindan aytamiz
class XabarModel(BaseModel):
    ism: str
    xabar: str
    email: str | None = None


@app.get("/")
def home():
    return {"status": "Tizim alo darajada ishlayapti", "version": "3.0"}


# 2. POST so'rov (Ma'lumot qabul qilish)
# Bu funksiya WordPressdan kelgan ma'lumotni oladi
@app.post("/kontakt-form")
def xabarni_tekshir(data: XabarModel):
    # Logika: Agar xabarda yomon so'z bo'lsa, rad etamiz
    yomon_sozlar = ["spam", "reklama", "ahmoq"]

    xabar_kichik = data.xabar.lower()

    for soz in yomon_sozlar:
        if soz in xabar_kichik:
            return {
                "success": False,
                "javob": f"Kechirasiz {data.ism}, sizning xabaringizda taqiqlangan so'z ('{soz}') bor."
            }

    # Agar hammasi toza bo'lsa:
    return {
        "success": True,
        "javob": f"Rahmat {data.ism}! Xabaringiz qabul qilindi. Biz sizga {data.email} orqali chiqamiz."
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)