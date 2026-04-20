from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Убактылуу база
jobs = [
    {"id": 1, "category": "⚡ Тез арада", "title": "Кафеге жардамчы", "price": "800 сом", "time": "Бүгүн 18:00", "phone": "996700123456", "desc": "Идиш аяктарга жардам берүү керек."},
    {"id": 2, "category": "📢 Промоутер", "title": "Флаер таратуу", "price": "150 сом/саат", "time": "3 саат", "phone": "996555112233", "desc": "Ала-Тоо аянтында флаер таратуу."},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ЖУМУШ БАР - Ыкчам жумуш тактасы</title>
    <style>
        :root { --primary: #00ff41; --dark: #0f0f0f; --card: #1a1a1a; }
        body { font-family: 'Inter', sans-serif; background: var(--dark); color: #fff; margin: 0; padding: 0; }
        .header { background: #000; padding: 30px 20px; text-align: center; border-bottom: 1px solid #333; }
        .container { max-width: 500px; margin: 0 auto; padding: 20px; }
        .job-card { background: var(--card); border-radius: 20px; padding: 20px; margin-bottom: 15px; border: 1px solid #333; transition: 0.3s; }
        .job-card:hover { border-color: var(--primary); }
        .badge { background: var(--primary); color: #000; padding: 4px 10px; border-radius: 8px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }
        .title { font-size: 1.3rem; font-weight: bold; margin: 10px 0; }
        .price { color: var(--primary); font-size: 1.1rem; font-weight: bold; }
        .btn { display: block; width: 100%; padding: 15px; border-radius: 15px; border: none; font-weight: bold; cursor: pointer; text-decoration: none; text-align: center; margin-top: 10px; }
        .btn-post { background: var(--primary); color: #000; margin-bottom: 20px; }
        .btn-wa { background: #25d366; color: #fff; }
        input, select, textarea { width: 100%; padding: 12px; margin-top: 10px; border-radius: 10px; border: 1px solid #333; background: #222; color: #fff; box-sizing: border-box; }
        .footer { text-align: center; color: #444; font-size: 0.8rem; margin: 40px 0; letter-spacing: 2px; }
    </style>
</head>
<body>
    <div class="header">
        <h1 style="margin:0; letter-spacing:3px;">ЖУМУШ БАР</h1>
        <p style="color:#666;">Азыр иште, азыр тап!</p>
    </div>
    <div class="container">
        <a href="#post" class="btn btn-post">+ ЖАРЫЯ БЕРҮҮ (Акысыз)</a>

        {% for job in jobs %}
        <div class="job-card">
            <span class="badge">{{ job.category }}</span>
            <div class="title">{{ job.title }}</div>
            <div class="price">{{ job.price }} <span style="color:#666; font-size:0.8rem;">/ {{ job.time }}</span></div>
            <p style="color:#aaa; font-size:0.9rem;">{{ job.desc }}</p>
            <a href="https://wa.me/{{ job.phone }}" class="btn btn-wa">WhatsApp-тан жазуу</a>
        </div>
        {% endfor %}

        <div id="post" style="margin-top:50px; background:#111; padding:20px; border-radius:20px;">
            <h3>Жаңы жарыя</h3>
            <form action="/add" method="POST">
                <select name="category">
                    <option>⚡ Тез арада</option>
                    <option>📢 Промоутер</option>
                    <option>📦 Курьер</option>
                    <option>🧼 Тазалык</option>
                    <option>🙋 Жардамчы</option>
                </select>
                <input type="text" name="title" placeholder="Жумуштун аталышы..." required>
                <input type="text" name="price" placeholder="Төлөмү (мис: 1000 сом)..." required>
                <input type="text" name="time" placeholder="Убактысы (мис: 4 саат)..." required>
                <input type="text" name="phone" placeholder="WhatsApp (мис: 996700112233)..." required>
                <textarea name="desc" placeholder="Кыскача маалымат..." rows="3"></textarea>
                <button type="submit" class="btn btn-post">ЖАРЫЯЛОО</button>
            </form>
        </div>
        <div class="footer">DESIGN BY ZAMIRBEKOVIBE</div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, jobs=jobs)

@app.route('/add', methods=['POST'])
def add():
    new_job = {
        "id": len(jobs) + 1,
        "category": request.form.get('category'),
        "title": request.form.get('title'),
        "price": request.form.get('price'),
        "time": request.form.get('time'),
        "phone": request.form.get('phone'),
        "desc": request.form.get('desc')
    }
    jobs.insert(0, new_job)
    return redirect(url_for('index'))
