from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = 'premium_key_2026'

# Убактылуу база
users = {}
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Мобилограф", "price": "45000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Программист", "price": "80000 сом", "wa": "996700112233"},
    {"cat": "Кызмат", "loc": "Бишкек", "title": "Администратор", "price": "30000 сом", "wa": "996500445566"}
]

HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JUMUSH BAR | Professional</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root { --bg: #ffffff; --text: #0f172a; --accent: #2563eb; --card: rgba(255, 255, 255, 0.8); }
        
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin: 0; background: var(--bg); color: var(--text);
            overflow-x: hidden;
        }

        /* Анимацияланган фон */
        .animated-bg {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1; background: linear-gradient(120deg, #f8fafc 0%, #e2e8f0 100%);
        }
        .shape {
            position: absolute; border-radius: 50%;
            background: linear-gradient(45deg, rgba(37,99,235,0.05), rgba(37,99,235,0.02));
            animation: move 20s infinite alternate;
        }

        @keyframes move {
            from { transform: translate(0, 0); }
            to { transform: translate(100px, 100px); }
        }

        header { padding: 60px 20px; text-align: center; }
        h1 { font-size: 3.5rem; font-weight: 800; letter-spacing: -2px; margin: 0; }
        
        .container { max-width: 900px; margin: 0 auto; padding: 20px; }

        /* Категориялар */
        .categories {
            display: flex; gap: 10px; overflow-x: auto; padding: 20px 0;
            justify-content: center; scrollbar-width: none;
        }
        .cat-tag {
            padding: 8px 20px; background: white; border: 1px solid #e2e8f0;
            border-radius: 50px; font-size: 0.9rem; white-space: nowrap; cursor: pointer;
        }

        /* Карта стили */
        .job-card {
            background: var(--card); backdrop-filter: blur(20px);
            border: 1px solid rgba(0,0,0,0.05); border-radius: 24px;
            padding: 25px; margin-bottom: 20px; display: flex;
            justify-content: space-between; align-items: center;
            transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .job-card:hover { transform: translateY(-5px); box-shadow: 0 20px 40px rgba(0,0,0,0.05); border-color: #000; }

        .btn-black {
            background: #000; color: #fff; padding: 14px 28px;
            border-radius: 14px; text-decoration: none; font-weight: 600;
        }
        
        .price { font-size: 1.4rem; font-weight: 800; color: #000; }
        .wa-btn {
            color: #25d366; text-decoration: none; font-weight: 700;
            padding: 8px 16px; border: 1.5px solid #25d366; border-radius: 12px;
        }
        .wa-btn:hover { background: #25d366; color: #fff; }

        .user-auth { position: absolute; top: 20px; right: 20px; }
    </style>
</head>
<body>
    <div class="animated-bg">
        <div class="shape" style="width: 400px; height: 400px; top: -100px; left: -100px;"></div>
        <div class="shape" style="width: 300px; height: 300px; bottom: 10%; right: 5%; animation-duration: 15s;"></div>
    </div>

    <div class="user-auth">
        {% if user %}
            <span>{{ user }}</span> | <a href="/logout">Чыгуу</a>
        {% else %}
            <a href="/login" class="cat-tag" style="text-decoration:none;">Кирүү</a>
        {% endif %}
    </div>

    <header>
        <h1>Jumush Bar</h1>
        <p style="color: #64748b;">Профессионалдык жумуш издөө жана жарыялоо</p>
    </header>

    <div class="container">
        <div style="text-align:center; margin-bottom: 40px;">
            <a href="/add" class="btn-black">+ Жарыя кошуу</a>
        </div>

        <div class="categories">
            <div class="cat-tag">Бардыгы</div>
