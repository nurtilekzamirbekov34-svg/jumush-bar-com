from flask import Flask, render_template_string, request, redirect, url_for

# Бул жерде 'app' өзгөрмөсү ачык болушу шарт
app = Flask(__name__)

# Убактылуу база
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Мобилограф", "price": "60,000 сом", "wa": "996555001122", "icon": "🎥"},
    {"cat": "IT", "loc": "Ош", "title": "Программист", "price": "120,000 сом", "wa": "996700112233", "icon": "💻"}
]

STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --glass: rgba(15, 15, 15, 0.85); --border: rgba(255, 255, 255, 0.1); }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { 
        font-family: 'Inter', sans-serif; background: #000 url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
        background-size: cover; color: white;
    }
    body::before { content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); z-index: -1; }
    .container { max-width: 480px; margin: 0 auto; padding: 20px; }
    .glass-card { background: var(--glass); backdrop-filter: blur(15px); border: 1px solid var(--border); border-radius: 25px; padding: 25px; margin-bottom: 20px; }
    .btn { display: block; width: 100%; padding: 18px; border-radius: 20px; text-decoration: none; text-align: center; font-weight: 800; border: none; cursor: pointer; font-family: 'Outfit'; }
    .btn-primary { background: white; color: black; }
    input, select { width: 100%; padding: 15px; margin-bottom: 12px; border-radius: 15px; border: 1px solid var(--border); background: rgba(0,0,0,0.6); color: white; }
</style>
"""

INDEX_HTML = STYLE + """
<div class="container">
    <header style="text-align: center; padding: 50px 0;">
        <h1 style="font-family: 'Outfit'; font-size: 45px; letter-spacing: -2px;">JUMUSH BAR</h1>
        <div style="display: flex; gap: 10px; margin-top: 30px;">
            <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1;">+ Жарыя кошуу</a>
        </div>
    </header>
    {% for job in jobs %}
    <div class="glass-card">
        <div style="color: var(--neon); font-size: 11px; font-weight: 800; text-transform: uppercase;">{{ job.icon }} {{ job.cat }} • {{ job.loc }}</div>
        <h2 style="font-family: 'Outfit'; font-size: 24px; margin: 8px 0;">{{ job.title }}</h2>
        <div style="font-size: 26px; font-weight: 300; color: #eee;">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" style="color: var(--neon); text-decoration: none; display: block; margin-top: 20px; border-top: 1px solid var(--border); padding-top: 15px; font-weight: 600;">WhatsApp байланыш →</a>
    </div>
    {% endfor %}
</div>
"""

ADD_HTML = STYLE + """
<div class="container">
    <div class="glass-card" style="margin-top: 50px;">
        <h2 style="text-align: center; margin-bottom: 25px; font-family: 'Outfit'; font-size: 28px;">Жаңы жарыя</h2>
        <form method="POST">
            <input type="text" name="title" placeholder="Жумуштун аты" required>
            <input type="text" name="price" placeholder="Айлыгы" required>
            <input type="text" name="loc" placeholder="Шаар" required>
            <select name="cat">
                <option value="Медиа">🎥 Медиа</option>
                <option value="IT">💻 IT</option>
                <option value="Кызмат">🛠️ Кызмат</option>
            </select>
            <input type="text" name="wa" placeholder="WhatsApp (996...)" required>
            <button type="submit" class="btn btn-primary">Жарыялоо</button>
            <a href="{{ url_for('index') }}" style="display:block; text-align:center; margin-top:20px; color:#999; text-decoration:none;">← Артка кайтуу</a>
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
        cat = request.form.get('cat')
        icons = {"Медиа": "🎥", "IT": "💻", "Кызмат": "🛠️"}
        new_job = {
            "title": request.form.get('title'),
            "price": request.form.get('price'),
            "loc": request.form.get('loc'),
            "cat": cat,
            "icon": icons.get(cat, "💼"),
            "wa": request.form.get('wa')
        }
        jobs.insert(0, new_job)
        return redirect(url_for('index'))
    return render_template_string(ADD_HTML)

# Vercel үчүн эң маанилүү жери ушул:
# 'if __name__ == "__main__":' кереги жок, Vercel 'app'ти өзү табат.
