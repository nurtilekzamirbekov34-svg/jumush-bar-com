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
