from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Убактылуу жумуштардын тизмеси
jobs = [
    {"location": "📍 Центр", "title": "Официант (кечки нөөмөт)", "price": "1200 сом/күн", "wa": "996555001122"},
    {"location": "📍 Дордой", "title": "Жүктөгүч (грузчик)", "price": "2000 сом/күн", "wa": "996700112233"},
    {"location": "📍 Түштүк магистраль", "title": "Курьер", "price": "1500 сом/күн", "wa": "996500445566"}
]

HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖУМУШ КАРТА</title>
    <style>
        :root { --accent: #00ff41; --bg: #0a0a0a; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: white; margin: 0; padding: 0; }
        .promo { background: var(--accent); color: black; padding: 10px; font-weight: bold; text-align: center; font-size: 0.8rem; }
        header { background: #000; padding: 40px 20px; text-align: center; border-bottom: 1px solid #222; }
        .container { max-width: 500px; margin: 20px auto; padding: 0 15px; }
        .add-btn { background: var(--accent); color: black; display: block; text-align: center; padding: 18px; border-radius: 15px; text-decoration: none; font-weight: bold; margin-bottom: 30px; transition: 0.3s; }
        .add-btn:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(0,255,65,0.4); }
        .job-card { background: #161616; padding: 20px; border-radius: 20px; margin-bottom: 15px; border: 1px solid #222; transition: 0.3s; }
        .job-card:hover { border-color: var(--accent); }
        .job-title { font-size: 1.2rem; margin: 5px 0; font-weight: bold; }
        .price { color: var(--accent); font-size: 1.4rem; font-weight: 900; }
        .wa-btn { background: #25d366; color: white; text-decoration: none; padding: 12px 25px; border-radius: 10px; display: inline-block; font-weight: bold; margin-top: 15px; }
        footer { text-align: center; padding: 50px; color: #444; font-size: 0.8rem; }
    </style>
</head>
<body>
    <div class="promo">БИШКЕК ШААРЫ БОЮНЧА АКЫСЫЗ ЖАРЫЯЛАР ПЛАТФОРМАСЫ</div>
    <header>
        <h1 style="margin:0; font-size: 2.5rem; text-shadow: 0 0 15px var(--accent);">ЖУМУШ КАРТА</h1>
        <p style="color: #888;">Өзүңө жакын жумушту тап</p>
    </header>

    <div class="container">
        <a href="/add" class="add-btn">+ ЖУМУШ ЖАРЫЯЛОО</a>

        <h2 style="font-size: 1rem; color: #666; text-transform: uppercase; letter-spacing: 1px;">Жаңы жарыялар:</h2>

        {% for job in jobs %}
        <div class="job-card">
            <div style="color: #666; font-size: 0.8rem;">{{ job.location }}</div>
            <div class="job-title">{{ job.title }}</div>
            <div style="margin-top: 15px; display: flex; justify-content: space-between; align-items: center;">
                <span class="price">{{ job.price }}</span>
                <a href="https://wa.me/{{ job.wa }}" class="wa-link"><span class="wa-btn">WhatsApp</span></a>
            </div>
        </div>
        {% endfor %}
    </div>

    <footer>© 2026 JUMUSH BAR | КЫРГЫЗСТАН</footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_MAIN, jobs=jobs)

@app.route('/add')
def add():
    return "<h3>Азырынча жарыя берүү үчүн бизге жазыңыз. <br> База туташтырылгандан кийин өзүңүз кошо аласыз.</h3><a href='/'>Артка</a>"

app = app
