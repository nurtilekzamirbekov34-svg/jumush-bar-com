from flask import Flask, render_template_string

app = Flask(__name__)

# Жумуштардын тизмеси
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Мобилограф", "price": "45000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Программист", "price": "80000 сом", "wa": "996700112233"},
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
        :root {
            --bg: #0d0d0d;
            --card-bg: #1a1a1a;
            --accent: #00ff41;
            --text: #ffffff;
            --gray: #888888;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
            width: 100%;
            max-width: 500px;
        }
        h1 {
            font-size: 2rem;
            letter-spacing: 2px;
            color: var(--text);
            margin-bottom: 20px;
        }
        .nav-buttons {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-bottom: 30px;
        }
        .btn {
            padding: 12px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 0.9rem;
            transition: 0.3s;
        }
        .btn-outline {
            border: 1px solid var(--accent);
            color: var(--accent);
        }
        .btn-fill {
            background-color: var(--accent);
            color: #000;
        }
        .btn:hover {
            opacity: 0.8;
            transform: translateY(-2px);
        }
        .job-card {
            background-color: var(--card-bg);
            width: 100%;
            max-width: 450px;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 15px;
            border: 1px solid #222;
            transition: 0.3s;
        }
        .job-card:hover {
            border-color: var(--accent);
        }
        .location {
            font-size: 0.8rem;
            color: var(--gray);
            margin-bottom: 5px;
        }
        .title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 8px;
        }
        .price {
            color: var(--accent);
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 15px;
        }
        .wa-link {
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 5px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>ЖУМУШ КАРТА</h1>
        <div class="nav-buttons">
            <a href="#" class="btn btn-outline">Кирүү / Каттоо</a>
            <a href="#" class="btn btn-fill">+ Жумуш кошуу</a>
        </div>
        <p style="color: var(--gray); font-size: 0.9rem;">Учурдагы жумуштар:</p>
    </div>

    {% for job in jobs %}
    <div class="job-card">
        <div class="location">📍 {{ job.loc }} • {{ job.cat }}</div>
        <div class="title">{{ job.title }}</div>
        <div class="price">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" class="wa-link">WhatsApp жазуу →</a>
    </div>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

if __name__ == "__main__":
    app.run()
