from flask import Flask, render_template_string

app = Flask(__name__)

# Райондор боюнча бөлүнгөн жумуштар
jobs = [
    {
        "location": "📍 Центр (Ала-Тоо)",
        "jobs": [
            {"title": "Промоутер (парк)", "price": "200 сом/саат", "wa": "996700112233"},
            {"title": "Кафеге официант", "price": "1200 сом", "wa": "996555001122"}
        ]
    },
    {
        "location": "📍 Түштүк магистраль",
        "jobs": [
            {"title": "Курьер (вело)", "price": "1500 сом/күн", "wa": "996777112233"}
        ]
    },
    {
        "location": "📍 Дордой / Түндүк",
        "jobs": [
            {"title": "Жүктөгүч (грузчик)", "price": "2000 сом", "wa": "996500889977"}
        ]
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
    <title>ЖУМУШ КАРТА - Локация боюнча</title>
    <style>
        :root { --accent: #00ff41; --bg: #050505; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: #fff; margin: 0; padding: 20px; }
        .header { text-align: center; padding: 30px 0; border-bottom: 2px solid var(--accent); margin-bottom: 30px; }
        .location-section { margin-bottom: 40px; }
        .location-title { 
            background: #111; 
            padding: 10px 15px; 
            border-radius: 8px; 
            color: var(--accent); 
            font-weight: bold; 
            border: 1px solid #333;
            margin-bottom: 15px;
        }
        .job-card { 
            background: #161616; 
            padding: 20px; 
            border-radius: 15px; 
            margin-bottom: 15px; 
            border: 1px solid #222;
            transition: 0.3s;
        }
        .job-card:hover { border-color: var(--accent); }
        .price { color: var(--accent); font-size: 1.2rem; font-weight: bold; }
        .wa-btn { 
            display: inline-block; 
            margin-top: 15px; 
            background: #25d366; 
            color: #fff; 
            padding: 10px 20px; 
            border-radius: 30px; 
            text-decoration: none; 
            font-weight: bold; 
            font-size: 0.9rem;
        }
    </style>
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
</head>
<body>
    <div class="header">
        <h1 style="margin:0;">ЖУМУШ КАРТА</h1>
        <p style="color:#666;">Өз районуңдан жумуш тап!</p>
    </div>

    <div style="max-width: 600px; margin: 0 auto;">
        {% for area in jobs %}
        <div class="location-section">
            <div class="location-title">{{ area.location }}</div>
            {% for job in area.jobs %}
            <div class="job-card">
                <div style="font-size: 1.1rem; font-weight: bold;">{{ job.title }}</div>
                <div class="price">{{ job.price }}</div>
                <a href="https://wa.me/{{ job.wa }}" class="wa-btn">WhatsApp-тан жазуу</a>
            </div>
            {% endfor %}
        </div>
        {% endfor %}
    </div>
    
    <div style="text-align:center; color:#333; margin-top:50px;">
        <p>© 2026 ЖУМУШ БАР - БИШКЕК</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

# Vercel үчүн маанилүү
app = app
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Бул жерде убактылуу жумуштар сакталат (база кошулганга чейин)
jobs = [
    {"location": "📍 Центр", "title": "Официант", "price": "1200 сом", "wa": "996..."},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖУМУШ КАРТА</title>
    <style>
        :root { --accent: #00ff41; --bg: #050505; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: #fff; margin: 0; padding: 20px; }
        
        /* Жаңы баскычтардын стили */
        .nav-buttons { display: flex; justify-content: center; gap: 10px; margin-bottom: 30px; }
        .btn { 
            padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 0.9rem;
            transition: 0.3s; border: 1px solid var(--accent);
        }
        .btn-login { color: var(--accent); background: transparent; }
        .btn-add { background: var(--accent); color: #000; }
        .btn:hover { opacity: 0.8; transform: translateY(-2px); }

        .header { text-align: center; padding: 20px 0; border-bottom: 1px solid #222; margin-bottom: 20px; }
        .job-card { background: #111; padding: 20px; border-radius: 15px; margin-bottom: 15px; border: 1px solid #222; }
        .price { color: var(--accent); font-weight: bold; }
    </style>
</head>
<body>
    <div class="header">
        <h1>ЖУМУШ КАРТА</h1>
    </div>

    <div class="nav-buttons">
        <a href="#" class="btn btn-login">Кирүү / Катталуу</a>
        <a href="#" class="btn btn-add">+ Жумуш кошуу</a>
    </div>

    <div style="max-width: 600px; margin: 0 auto;">
        <p style="text-align: center; color: #666;">Учурдагы жумуштар:</p>
        {% for job in jobs %}
        <div class="job-card">
            <div style="color: var(--accent); font-size: 0.8rem;">{{ job.location }}</div>
            <div style="font-size: 1.2rem; margin: 5px 0;">{{ job.title }}</div>
            <div class="price">{{ job.price }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Убактылуу база (сайт өчкөндө маалымат тазаланат, кийин чыныгы базага туташтырабыз)
jobs = [
    {"location": "📍 Центр", "title": "Официант", "price": "1200 сом", "wa": "996555001122"}
]

# БАШКЫ БАРАКЧА
HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
    <title>ЖУМУШ КАРТА</title>
    <style>
        :root { --accent: #00ff41; --bg: #050505; }
        body { font-family: sans-serif; background: var(--bg); color: #fff; text-align: center; padding: 20px; }
        .btn-group { margin-bottom: 30px; }
        .btn { padding: 12px 20px; border-radius: 8px; text-decoration: none; font-weight: bold; margin: 5px; display: inline-block; }
        .btn-green { background: var(--accent); color: #000; }
        .btn-outline { border: 1px solid var(--accent); color: var(--accent); }
        .card { background: #111; padding: 15px; border-radius: 10px; margin: 10px auto; max-width: 400px; border: 1px solid #222; }
    </style>
</head>
<body>
    <h1>ЖУМУШ КАРТА</h1>
    <div class="btn-group">
        <a href="/login" class="btn btn-outline">Кирүү / Каттоо</a>
        <a href="/add" class="btn btn-green">+ Жумуш кошуу</a>
    </div>
    
    <h3>Учурдагы жумуштар:</h3>
    {% for job in jobs %}
    <div class="card">
        <p><b>{{ job.location }}</b></p>
        <p>{{ job.title }} - <span style="color:var(--accent)">{{ job.price }}</span></p>
        <a href="https://wa.me/{{ job.wa }}" style="color:#25d366; text-decoration:none;">WhatsApp</a>
    </div>
    {% endfor %}
</body>
</html>
"""

# ЖУМУШ КОШУУ БАРАКЧАСЫ
HTML_ADD = """
<!DOCTYPE html>
<html lang="ky">
<head><title>Жумуш кошуу</title></head>
<body style="background:#050505; color:white; text-align:center; font-family:sans-serif;">
    <h2>Жаңы жумуш кошуу</h2>
    <form method="POST" style="display:inline-block; text-align:left; background:#111; padding:20px; border-radius:10px;">
        Район: <br><input name="location" placeholder="Мисалы: Центр" required style="margin-bottom:10px;"><br>
        Жумуштун аты: <br><input name="title" placeholder="Мисалы: Ашпозчу" required style="margin-bottom:10px;"><br>
        Акысы: <br><input name="price" placeholder="1500 сом" required style="margin-bottom:10px;"><br>
        WhatsApp номер: <br><input name="wa" placeholder="996700112233" required style="margin-bottom:20px;"><br>
        <button type="submit" style="background:#00ff41; border:none; padding:10px; width:100%; font-weight:bold;">ЖАРЫЯЛОО</button>
    </form>
    <br><br><a href="/" style="color:gray;">Артка кайт</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_MAIN, jobs=jobs)

@app.route('/add', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        new_job = {
            "location": "📍 " + request.form.get('location'),
            "title": request.form.get('title'),
            "price": request.form.get('price'),
            "wa": request.form.get('wa')
        }
        jobs.append(new_job)
        return redirect('/')
    return render_template_string(HTML_ADD)

@app.route('/login')
def login():
    return "<h3>Бул бөлүм жакында ишке кирет (Каттоо базасы түзүлүүдө...)</h3><a href='/'>Артка</a>"

app = app
