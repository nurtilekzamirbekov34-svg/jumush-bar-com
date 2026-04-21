from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Убактылуу база
jobs = [
    {"location": "📍 Центр", "title": "Официант", "price": "1200 сом", "wa": "996555001122"}
]

# БАШКЫ БЕТТИН ДИЗАЙНЫ
HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />
    <title>ЖУМУШ КАРТА</title>
    <style>
        :root { --accent: #00ff41; --bg: #050505; --card-bg: rgba(20, 20, 20, 0.9); }
        body { 
            font-family: 'Inter', sans-serif; 
            background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                        url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?q=80&w=1974&auto=format&fit=crop');
            background-size: cover; background-position: center; background-attachment: fixed;
            color: #fff; text-align: center; padding: 20px; margin: 0;
        }
        header { padding-top: 60px; }
        h1 { font-size: 3rem; text-shadow: 0 0 20px var(--accent); text-transform: uppercase; margin: 0; }
        .btn-group { margin: 40px 0; }
        .btn { padding: 15px 30px; border-radius: 50px; text-decoration: none; font-weight: bold; margin: 10px; display: inline-block; transition: 0.3s; }
        .btn-green { background: var(--accent); color: #000; box-shadow: 0 0 15px var(--accent); }
        .btn-outline { border: 2px solid #fff; color: #fff; backdrop-filter: blur(5px); }
        .card { 
            background: var(--card-bg); padding: 25px; border-radius: 25px; margin: 20px auto; 
            max-width: 500px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);
            transition: 0.4s; text-align: left;
        }
        .price { font-size: 1.6rem; color: var(--accent); font-weight: 900; }
        .wa-link { color: #25d366; text-decoration: none; font-weight: bold; border: 1px solid #25d366; padding: 8px 15px; border-radius: 12px; }
    </style>
</head>
<body>
    <header>
        <h1>ЖУМУШ КАРТА</h1>
        <p>Бишкек: Ыкчам жана ишенимдүү жумуштар</p>
    </header>
    <div class="btn-group">
        <a href="/login" class="btn btn-outline">👤 КИРҮҮ</a>
        <a href="/add" class="btn btn-green">🚀 ЖУМУШ КОШУУ</a>
    </div>
    <div class="container">
        {% for job in jobs %}
        <div class="card">
            <h3 style="color: var(--accent); margin: 0;">{{ job.location }}</h3>
            <p style="font-size: 1.3rem; margin: 10px 0;">{{ job.title }}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="price">{{ job.price }}</span>
                <a href="https://wa.me/{{ job.wa }}" class="wa-link">WhatsApp</a>
            </div>
        </div>
        {% endfor %}
    </div>
    <footer style="margin-top: 50px; opacity: 0.5;"><p>© 2026 JUMUSH BAR</p></footer>
</body>
</html>
"""

# ЖУМУШ КОШУУ БЕТИНИН ДИЗАЙНЫ
HTML_ADD = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Жумуш кошуу</title>
    <style>
        body { background: #050505; color: white; font-family: sans-serif; text-align: center; padding: 50px; }
        form { background: #111; padding: 30px; border-radius: 20px; display: inline-block; border: 1px solid #222; }
        input { display: block; width: 250px; padding: 12px; margin-bottom: 15px; background: #222; border: none; color: white; border-radius: 10px; }
        button { background: #00ff41; border: none; padding: 12px; width: 100%; font-weight: bold; cursor: pointer; border-radius: 10px; }
    </style>
</head>
<body>
    <h2>Жаңы жумуш жарыялоо</h2>
    <form method="POST">
        <input name="location" placeholder="Район (мис: Ала-Тоо)" required>
        <input name="title" placeholder="Жумуштун аты" required>
        <input name="price" placeholder="Акысы (мис: 1500 сом)" required>
        <input name="wa" placeholder="WhatsApp (996...)" required>
        <button type="submit">ЖАРЫЯЛОО</button>
    </form>
    <br><a href="/" style="color: gray; text-decoration: none;">← Артка</a>
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
    return "<h3>Каттоо базасы даярдалууда...</h3><a href='/'>Артка</a>"

# Бул жер маанилүү!
app = app
from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'jumush-bar-2026'

jobs = [
    {"location": "📍 Бишкек", "title": "Мобилограф жардамчысы", "price": "1500 сом", "wa": "996..."},
]

HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JUMUSH BAR | Жумуш Карта</title>
    <style>
        :root { --accent: #00ff41; }
        body, html { margin: 0; padding: 0; height: 100%; font-family: 'Inter', sans-serif; background: #000; color: white; }
        
        /* Видео фондун стили */
        .video-bg {
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; filter: brightness(0.4);
            object-fit: cover;
        }

        .overlay {
            position: relative; z-index: 1;
            padding: 20px; text-align: center;
        }

        h1 { font-size: 3.5rem; letter-spacing: 5px; text-shadow: 0 0 20px var(--accent); margin-top: 50px; }
        
        .btn {
            padding: 15px 30px; border-radius: 50px; text-decoration: none;
            font-weight: bold; transition: 0.3s; display: inline-block; margin: 10px;
        }
        .btn-primary { background: var(--accent); color: black; box-shadow: 0 0 20px var(--accent); }
        .btn-outline { border: 2px solid white; color: white; backdrop-filter: blur(5px); }

        .job-container { max-width: 600px; margin: 50px auto; }
        .job-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 25px; border-radius: 25px; margin-bottom: 20px;
            text-align: left; transition: 0.4s;
        }
        .job-card:hover { transform: translateY(-10px); border-color: var(--accent); }
    </style>
</head>
<body>
    <video autoplay muted loop class="video-bg">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-business-people-working-together-in-an-office-4340-large.mp4" type="video/mp4">
    </video>

    <div class="overlay">
        <h1>JUMUSH BAR</h1>
        <p style="font-size: 1.2rem; opacity: 0.8;">Бишкек шаарындагы эң тез жумуш табуу кызматы</p>
        
        <div style="margin: 40px 0;">
            <a href="/login" class="btn btn-outline">👤 КИРҮҮ</a>
            <a href="/add" class="btn btn-primary">🚀 ЖАРЫЯ КОШУУ</a>
        </div>

        <div class="job-container">
            <h2 style="text-align: left; border-left: 4px solid var(--accent); padding-left: 15px;">ЖАҢЫ ЖУМУШТАР</h2>
            {% for job in jobs %}
            <div class="job-card">
                <span style="color: var(--accent); font-size: 0.8rem; font-weight: bold;">{{ job.location }}</span>
                <h3 style="margin: 10px 0;">{{ job.title }}</h3>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 1.5rem; font-weight: bold;">{{ job.price }}</span>
                    <a href="https://wa.me/{{ job.wa }}" style="color: #25d366; text-decoration: none; border: 1px solid #25d366; padding: 5px 15px; border-radius: 10px;">WhatsApp</a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_MAIN, jobs=jobs)

@app.route('/add')
def add():
    return "Жумуш кошуу формасы (база туташтырылгандан кийин ишке кирет)"

@app.route('/login')
def login():
    return "Кирүү барагы"

app = app
