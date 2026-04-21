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
    <title>ЖУМУШ КАРТА</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Montserrat', sans-serif;
            background: radial-gradient(circle at top right, #1a1a2e, #0f0f0f);
            color: #fff;
            min-height: 100vh;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .container { width: 100%; max-width: 480px; }
        
        .header {
            text-align: center;
            padding: 40px 0;
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        h1 {
            font-weight: 700;
            font-size: 24px;
            text-transform: uppercase;
            letter-spacing: 4px;
            background: linear-gradient(to right, #00ff41, #00d2ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        .nav-btns { display: flex; gap: 12px; justify-content: center; padding: 0 20px; }
        
        .btn {
            flex: 1;
            padding: 14px;
            border-radius: 12px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            text-align: center;
            transition: all 0.4s;
            border: 1px solid rgba(0, 255, 65, 0.5);
        }
        
        .btn-reg { color: #00ff41; background: transparent; }
        .btn-add { background: #00ff41; color: #000; }
        .btn:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(0, 255, 65, 0.3); }

        .job-card {
            background: rgba(255, 255, 255, 0.05);
            margin-bottom: 16px;
            padding: 20px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            position: relative;
            overflow: hidden;
        }
        
        .job-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 4px; height: 100%;
            background: #00ff41;
        }

        .cat-tag { font-size: 10px; color: #888; text-transform: uppercase; margin-bottom: 4px; }
        .title { font-size: 18px; font-weight: 700; margin-bottom: 4px; }
        .price { font-size: 20px; color: #00ff41; font-weight: 700; margin-bottom: 12px; }
        
        .wa-btn {
            display: inline-block;
            color: #000;
            background: #fff;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Jumush Bar</h1>
            <div class="nav-btns">
                <a href="#" class="btn btn-reg">Кирүү</a>
                <a href="#" class="btn btn-add">+ Жумуш</a>
            </div>
        </div>

        <p style="margin-left: 10px; margin-bottom: 15px; color: #666; font-size: 14px;">Жакын жердеги жумуштар:</p>

        {% for job in jobs %}
        <div class="job-card">
            <p class="cat-tag">{{ job.cat }} • {{ job.loc }}</p>
            <h2 class="title">{{ job.title }}</h2>
            <p class="price">{{ job.price }}</p>
            <a href="https://wa.me/{{ job.wa }}" class="wa-btn">WhatsApp жазуу</a>
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
    <title>ЖУМУШ КАРТА</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Montserrat', sans-serif;
            background: #000;
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
        }

        /* Фондогу сурот */
        .bg-image {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: url('https://images.unsplash.com/photo-1516339901600-2e1a62dc0c45?q=80&w=2000') no-repeat center center/cover;
            opacity: 0.4; /* Суротту бир аз тунарык кылуу */
            filter: blur(8px); /* Плавный фокус */
            z-index: -1;
        }

        .container { width: 100%; max-width: 480px; padding: 20px; }

        /* Анимациялар */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .header {
            text-align: center;
            padding: 40px 20px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(15px);
            border-radius: 30px;
            margin-bottom: 30px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: fadeInUp 0.8s ease-out;
        }

        h1 {
            font-weight: 700;
            font-size: 28px;
            text-transform: uppercase;
            letter-spacing: 5px;
            background: linear-gradient(45deg, #00ff41, #00d2ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 25px;
        }

        .nav-btns { display: flex; gap: 15px; }

        .btn {
            flex: 1;
            padding: 15px;
            border-radius: 15px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 700;
            text-align: center;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .btn-reg { border: 2px solid #00ff41; color: #00ff41; }
        .btn-add { background: #00ff41; color: #000; }

        .btn:active { transform: scale(0.95); }

        .job-card {
            background: rgba(255, 255, 255, 0.07);
            backdrop-filter: blur(10px);
            margin-bottom: 20px;
            padding: 25px;
            border-radius: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: fadeInUp 1s ease-out both;
            transition: 0.4s;
        }

        .job-card:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: #00ff41;
            transform: translateX(5px);
        }

        /* Ар бир карта ар башка убакытта чыгышы учун */
        .job-card:nth-child(3) { animation-delay: 0.2s; }
        .job-card:nth-child(4) { animation-delay: 0.4s; }
        .job-card:nth-child(5) { animation-delay: 0.6s; }

        .cat-tag { font-size: 11px; color: #00ff41; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
        .title { font-size: 20px; font-weight: 700; margin-bottom:
