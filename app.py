from flask import Flask, render_template_string

app = Flask(__name__)

jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Мобилограф", "price": "45,000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Программист", "price": "80,000 сом", "wa": "996700112233"},
    {"cat": "Кызмат", "loc": "Бишкек", "title": "Администратор", "price": "30,000 сом", "wa": "996500445566"}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
    <title>JUMUSH BAR | PRO</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;600;800&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --neon: #00ff41;
            --glass: rgba(255, 255, 255, 0.05);
            --border: rgba(255, 255, 255, 0.1);
            --bg: #050505;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: white;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Плавный фон */
        .gradient-bg {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at 50% -20%, #1a3a1e, #050505);
            z-index: -1;
        }

        .container { width: 100%; max-width: 440px; margin: 0 auto; padding: 25px; }

        /* Плавный анимациялар */
        @keyframes reveal {
            from { opacity: 0; transform: translateY(20px) scale(0.98); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }

        .header {
            text-align: center;
            padding: 50px 20px;
            animation: reveal 1s cubic-bezier(0.2, 0.8, 0.2, 1);
        }

        .logo {
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 32px;
            letter-spacing: -1px;
            margin-bottom: 30px;
            background: linear-gradient(to bottom, #fff, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .nav-btns { display: flex; gap: 12px; margin-top: 20px; }

        .btn {
            flex: 1;
            padding: 16px;
            border-radius: 18px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            text-align: center;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            font-family: 'Outfit', sans-serif;
        }

        .btn-primary { background: white; color: black; }
        .btn-secondary { background: var(--glass); color: white; border: 1px solid var(--border); backdrop-filter: blur(10px); }

        .btn:hover { transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
        .btn:active { transform: scale(0.96); }

        .job-list-title {
            font-size: 13px;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin: 20px 0 15px 5px;
            font-weight: 600;
        }

        .job-card {
            background: var(--glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 24px;
            margin-bottom: 16px;
            animation: reveal 1s cubic-bezier(0.2, 0.8, 0.2, 1) both;
            transition: 0.3s;
        }

        .job-card:hover {
            background: rgba(255, 255, 255, 0.08);
            border-color: rgba(255, 255, 255, 0.2);
        }

        .cat-badge {
            display: inline-block;
            padding: 4px 10px;
            background: rgba(0, 255, 65, 0.1);
            color: var(--neon);
            border-radius: 8px;
            font-size: 10px;
            font-weight: 700;
            margin-bottom: 12px;
            text-transform: uppercase;
        }

        .job-title {
            font-family: 'Outfit', sans-serif;
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 4px;
        }

        .job-price {
            font-size: 24px;
            font-weight: 300;
            color: #fff;
            margin-bottom: 20px;
        }

        .wa-action {
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: var(--neon);
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
            border-top: 1px solid var(--border);
            padding-top: 15px;
        }

        /* Ар бир карта кечигип чыгат */
        .job-card:nth-child(1) { animation-delay: 0.1s; }
        .job-card:nth-child(2) { animation-delay: 0.2s; }
        .job-card:nth-child(3) { animation-delay: 0.3s; }

    </style>
</head>
<body>
    <div class="gradient-bg"></div>
    <div class="container">
        <header class="header">
            <div class="logo">JUMUSH BAR</div>
            <div class="nav-btns">
                <a href="#" class="btn btn-secondary">Катталуу</a>
                <a href="#" class="btn btn-primary">+ Жумуш кошуу</a>
            </div>
        </header>

        <p class="job-list-title">Жакын жерде</p>

        {% for job in jobs %}
        <div class="job-card">
            <span class="cat-badge">{{ job.cat }} • {{ job.loc }}</span>
            <h2 class="job-title">{{ job.title }}</h2>
            <div class="job-price">{{ job.price }}</div>
            <a href="https://wa.me/{{ job.wa }}" class="wa-action">
                <span>WhatsApp жазуу</span>
                <span>→</span>
            </a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

app = app
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Убактылуу база (сайт жаңыланганда тазаланат)
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Профессионал Мобилограф", "price": "50,000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Python Программист", "price": "100,000 сом", "wa": "996700112233"}
]

# --- ДИЗАЙН СТИЛДЕРИ (CSS) ---
COMMON_STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&family=Inter:wght@300;600&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --bg: #050505; --glass: rgba(255,255,255,0.05); --border: rgba(255,255,255,0.1); }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Inter', sans-serif; background: var(--bg); color: white; overflow-x: hidden; }
    .container { max-width: 450px; margin: 0 auto; padding: 20px; }
    .btn { display: block; width: 100%; padding: 16px; border-radius: 16px; text-decoration: none; font-weight: 700; text-align: center; transition: 0.3s; border: none; cursor: pointer; }
    .btn-primary { background: white; color: black; font-family: 'Outfit'; }
    .btn-secondary { background: var(--glass); color: white; border: 1px solid var(--border); backdrop-filter: blur(10px); }
    .glass-card { background: var(--glass); border: 1px solid var(--border); backdrop-filter: blur(20px); border-radius: 24px; padding: 25px; margin-bottom: 15px; animation: fadeInUp 0.8s ease forwards; }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
</style>
"""

# --- БАШКЫ БЕТ ---
INDEX_HTML = COMMON_STYLE + """
<div class="container">
    <header style="text-align: center; padding: 40px 0;">
        <h1 style="font-family: 'Outfit'; font-size: 32px; letter-spacing: -1px; margin-bottom: 25px;">JUMUSH BAR</h1>
        <div style="display: flex; gap: 10px;">
            <a href="#" class="btn btn-secondary" style="flex: 1;">Катталуу</a>
            <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1;">+ Жумуш кошуу</a>
        </div>
    </header>

    <p style="color: #666; font-size: 13px; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 15px;">Жакын жерде:</p>

    {% for job in jobs %}
    <div class="glass-card">
        <span style="color: var(--neon); font-size: 10px; font-weight: 800; text-transform: uppercase;">● {{ job.cat }} • {{ job.loc }}</span>
        <h2 style="font-family: 'Outfit'; font-size: 20px; margin: 8px 0;">{{ job.title }}</h2>
        <div style="font-size: 24px; font-weight: 300; margin-bottom: 20px;">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" style="color: var(--neon); text-decoration: none; font-weight: 600; display: flex; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 15px;">
            <span>WhatsApp жазуу</span> <span>→</span>
        </a>
    </div>
    {% endfor %}
</div>
"""

# --- ЖУМУШ КОШУУ БЕТИ ---
ADD_JOB_HTML = COMMON_STYLE + """
<div class="container">
    <div class="glass-card" style="margin-top: 50px;">
        <h2 style="font-family: 'Outfit'; margin-bottom: 20px; text-align: center;">Жаңы жарыя</h2>
        <form method="POST">
            <input type="text" name="title" placeholder="Жумуштун аты" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid var(--border); background:rgba(0,0,0,0.3); color:white;" required>
            <input type="text" name="price" placeholder="Айлыгы (мис: 40,000 сом)" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid var(--border); background:rgba(0,0,0,0.3); color:white;" required>
            <input type="text" name="loc" placeholder="Шаар/Район" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid var(--border); background:rgba(0,0,0,0.3); color:white;" required>
            <select name="cat" style="width:100%; padding:15px; margin-bottom:12px; border-radius:12px; border:1px solid var(--border); background:rgba(0,0,0,0.3); color:white;">
                <option value="Медиа">Медиа</option>
                <option value="IT">IT</option>
                <option value="Кызмат">Кызмат</option>
            </select>
            <input type="text" name="wa" placeholder="WhatsApp (мис: 996555112233)" style="width:100%; padding:15px; margin-bottom:20px; border-radius:12px; border:1px solid var(--border); background:rgba(0,0,0,0.3); color:white;" required>
            <button type="submit" class="btn btn-primary">Жарыялоо</button>
            <a href="{{ url_for('index') }}" style="display:block; text-align:center; margin-top:15px; color:#666; text-decoration:none; font-size:14px;">Артка кайтуу</a>
        </form>
    </div>
</div>
"""

@app.route('/')
def index():
    return render_template_string(INDEX_HTML, jobs=jobs)

@app.route('/add', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        new_job = {
            "title": request.form.get('title'),
            "price": request.form.get('price'),
            "loc": request.form.get('loc'),
            "cat": request.form.get('cat'),
            "wa": request.form.get('wa')
        }
        jobs.insert(0, new_job)
        return redirect(url_for('index'))
    return render_template_string(ADD_JOB_HTML)

if __name__ == "__main__":
    app.run()
