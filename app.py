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
