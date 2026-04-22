from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Убактылуу база
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Профессионал Мобилограф", "price": "50,000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Python Программист", "price": "100,000 сом", "wa": "996700112233"}
]

# --- ГЛОБАЛДЫК СТИЛДЕР (Премиум Дизайн) ---
COMMON_STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&family=Inter:wght@300;600&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --bg: #050505; --glass: rgba(255,255,255,0.05); --border: rgba(255,255,255,0.1); }
    * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    body { font-family: 'Inter', sans-serif; background: var(--bg); color: white; overflow-x: hidden; }
    .container { max-width: 450px; margin: 0 auto; padding: 20px; }
    @keyframes reveal { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    .glass-card { 
        background: var(--glass); border: 1px solid var(--border); backdrop-filter: blur(20px); 
        border-radius: 24px; padding: 25px; margin-bottom: 15px; animation: reveal 0.8s ease forwards;
    }
    .btn { 
        display: block; width: 100%; padding: 16px; border-radius: 16px; 
        text-decoration: none; font-weight: 700; text-align: center; 
        transition: 0.3s; border: none; cursor: pointer; 
    }
    .btn-primary { background: white; color: black; font-family: 'Outfit'; }
    .btn-secondary { background: var(--glass); color: white; border: 1px solid var(--border); }
    input, select {
        width: 100%; padding: 15px; margin-bottom: 15px; 
        border-radius: 12px; border: 1px solid var(--border); 
        background: rgba(0,0,0,0.4); color: white;
    }
</style>
"""

# --- БАШКЫ БЕТ (Ушул жерде SEO тегдери бар) ---
INDEX_HTML = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>JUMUSH BAR | Жумуш издөө Бишкек жана Кыргызстан</title>
    <meta name="description" content="Бишкек жана Кыргызстан боюнча эң акыркы жумуш жарыялары. Мобилограф, IT жана кызмат көрсөтүү вакансиялары.">
    <meta name="keywords" content="жумуш, бишкек жумуш, вакансиялар кыргызстан, мобилограф, жумуш издөө, jumush bar, иш издөө">
    <meta name="google-site-verification" content="dQctr8uZKssnExslN2rknNpoEx7HkQtmovkfU1whtdE" />

    """ + COMMON_STYLE + """
</head>
<body>
    <div class="container">
        <header style="text-align: center; padding: 40px 0;">
            <h1 style="font-family: 'Outfit'; font-size: 36px; font-weight: 800; margin-bottom: 30px;">JUMUSH BAR</h1>
            <div style="display: flex; gap: 12px;">
                <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1;">+ Жумуш кошуу</a>
                <a href="#" class="btn btn-secondary" style="flex: 1;">Кирүү</a>
            </div>
        </header>

        {% for job in jobs %}
        <div class="glass-card">
            <span style="color: var(--neon); font-size: 10px; font-weight: 800; text-transform: uppercase;">{{ job.cat }} • {{ job.loc }}</span>
            <h2 style="font-family: 'Outfit'; font-size: 20px; margin: 10px 0;">{{ job.title }}</h2>
            <div style="font-size: 24px; font-weight: 300; margin-bottom: 20px;">{{ job.price }}</div>
            <a href="https://wa.me/{{ job.wa }}" style="color: var(--neon); text-decoration: none; font-weight: 600; display: flex; justify-content: space-between; border-top: 1px solid var(--border); padding-top: 15px;">
                <span>WhatsApp жазуу</span> <span>→</span>
            </a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

# --- ЖУМУШ КОШУУ БЕТИ ---
ADD_JOB_HTML = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Жаңы жарыя кошуу</title>
    """ + COMMON_STYLE + """
</head>
<body>
    <div class="container">
        <div class="glass-card" style="margin-top: 40px;">
            <h2 style="font-family: 'Outfit'; font-size: 24px; margin-bottom: 25px; text-align: center;">Жаңы жарыя</h2>
            <form method="POST">
                <input type="text" name="title" placeholder="Жумуштун аты" required>
                <input type="text" name="price" placeholder="Айлыгы" required>
                <input type="text" name="loc" placeholder="Шаар" required>
                <select name="cat">
                    <option value="Медиа">Медиа</option>
                    <option value="IT">IT</option>
                    <option value="Кызмат">Кызмат</option>
                </select>
                <input type="text" name="wa" placeholder="WhatsApp" required>
                <button type="submit" class="btn btn-primary">Жарыялоо</button>
                <a href="{{ url_for('index') }}" style="display:block; text-align:center; margin-top:20px; color:#666; text-decoration:none;">← Артка кайтуу</a>
            </form>
        </div>
    </div>
</body>
</html>
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
