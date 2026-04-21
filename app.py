from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'premium_key_2026'

# Убактылуу база
users = {}
jobs = [
    {"cat": "содержание", "loc": "Бишкек", "title": "Мобилограф", "price": "45000 сом", "wa": "996555001122"},
    {"cat": "ЭТО", "loc": "Ош", "title": "Программист", "price": "80000 сом", "wa": "996700112233"},
    {"cat": "Кызмат", "loc": "Бишкек", "title": "Администратор", "price": "30000 сом", "wa": "996500445566"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
    <title>ЖУМУШ КАРТА</title>
    <style>
        body { font-family: sans-serif; background: #1a1a1a; color: white; text-align: center; padding: 20px; }
        .header h1 { color: #00ff41; }
        .btn { display: inline-block; padding: 10px 20px; margin: 10px; border-radius: 5px; text-decoration: none; font-weight: bold; }
        .btn-green { background: #4CAF50; color: white; }
        .btn-outline { border: 1px solid #4CAF50; color: #4CAF50; }
        .job-card { background: #333; padding: 15px; margin: 10px auto; border-radius: 10px; max-width: 400px; text-align: left; }
        .price { color: #00ff41; font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>ЖУМУШ КАРТА</h1>
        <a href="https://wa.me/996XXXXXXXXX" class="btn btn-outline">Кирүү / Каттоо</a>
        <a href="https://wa.me/996XXXXXXXXX" class="btn btn-green">+ Жумуш кошуу</a>
        <p style="color:#888;">Учурдагы жумуштар:</p>
    </div>

    {% for job in jobs %}
    <div class="job-card">
        <div style="font-size: 0.8rem; color: #888;">📍 {{ job.loc }}</div>
        <div style="font-weight: bold; font-size: 1.2rem;">{{ job.title }}</div>
        <div class="price">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" style="color: #25d366; text-decoration: none;">WhatsApp жазуу →</a>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

# Vercel үчүн маанилүү бөлүк
if __name__ == "__main__":
    app.run()
