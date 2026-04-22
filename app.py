from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Временная база данных (будет работать, пока сайт запущен)
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Профессиональный Мобилограф", "price": "60,000 сом", "wa": "996555001122", "icon": "🎥"},
    {"cat": "IT", "loc": "Ош", "title": "Python Разработчик", "price": "120,000 сом", "wa": "996700112233", "icon": "💻"},
    {"cat": "Услуги", "loc": "Бишкек", "title": "SMM Менеджер", "price": "45,000 сом", "wa": "996500445566", "icon": "📱"}
]

# --- ЕДИНЫЙ ДИЗАЙН (CSS) ---
STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --glass: rgba(15, 15, 15, 0.8); --border: rgba(255, 255, 255, 0.1); }
    * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    
    body { 
        font-family: 'Inter', sans-serif; 
        color: white; 
        background: #000 url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
        background-size: cover;
    }

    body::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(180deg, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.9) 100%);
        z-index: -1;
    }

    .container { max-width: 480px; margin: 0 auto; padding: 20px; min-height: 100vh; }

    header { text-align: center; padding: 60px 0 30px 0; }
    .logo { font-family: 'Outfit'; font-size: 45px; font-weight: 900; letter-spacing: -2px; margin-bottom: 5px; }
    
    .search-bar {
        background: var(--glass); border: 1px solid var(--border); backdrop-filter: blur(15px);
        border-radius: 20px; padding: 15px 20px; margin-bottom: 30px;
    }
    .search-bar input { background: transparent; border: none; color: white; width: 100%; outline: none; font-size: 16px; }

    .glass-card { 
        background: var(--glass); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border); border-radius: 28px; padding: 25px; margin-bottom: 20px; 
        transition: 0.3s ease; animation: fadeInUp 0.6s ease both;
    }
    .glass-card:hover { transform: translateY(-5px); border-color: var(--neon); }

    .badge {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(255,255,255,0.08); padding: 6px 12px; border-radius: 10px;
        font-size: 11px; font-weight: 800; color: var(--neon); text-transform: uppercase; margin-bottom: 15px;
    }

    .job-title { font-family: 'Outfit'; font-size: 22px; font-weight: 700; margin-bottom: 5px; }
    .price { font-size: 26px; font-weight: 300; color: #fff; margin-bottom: 20px; }

    .btn { 
        display: block; width: 100%; padding: 18px; border-radius: 20px; 
        text-decoration: none; font-weight: 800; text-align: center; 
        transition: 0.3s; cursor: pointer; font-family: 'Outfit'; border: none;
    }
    .btn-primary { background: white; color: black; margin-bottom: 12px; }
    .btn-secondary { background: rgba(255,255,255,0.1); color: white; border: 1px solid var(--border); }

    .wa-link {
        display: flex; justify-content: space-between; align-items: center;
        color: var(--neon); text-decoration: none; font-weight: 700;
        border-top: 1px solid var(--border); padding-top: 15px;
    }

    @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

    input, select {
        width: 100%; padding: 16px; margin-bottom: 15px; border-radius: 15px;
        border: 1px solid var(--border); background: rgba(0,0,0,0.5); color: white; outline: none;
    }
</style>
"""

# --- ГЛАВНАЯ СТРАНИЦА ---
INDEX_HTML = STYLE + """
<div class="container">
    <header>
        <div class="logo">JUMUSH BAR</div>
        <p style="color: #999; font-size: 13px; margin-bottom: 30px;">Твой путь к новой работе начинается здесь</p>
        
        <div class="search-bar">
            <input type="text" placeholder="Поиск работы (например: Мобилограф)">
        </div>

        <div style="display: flex; gap: 10px; margin-bottom: 20px;">
            <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1.2;">+ Добавить</a>
            <a href="#" class="btn btn-secondary" style="flex: 0.8;">Войти</a>
        </div>
    </header>

    {% for job in jobs %}
    <div class="glass-card">
        <div class="badge"><span>{{ job.icon }}</span> {{ job.cat }} • {{ job.loc }}</div>
        <h2 class="job-title">{{ job.title }}</h2>
        <div class="price">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" class="wa-link">
            <span>Написать в WhatsApp</span> <span>→</span>
        </a>
    </div>
    {% endfor %}
</div>
"""

# --- СТРАНИЦА ДОБАВЛЕНИЯ ---
ADD_HTML = STYLE + """
<div class="container">
    <div class="glass-card" style="margin-top: 50px;">
        <h2 style="font-family: 'Outfit'; margin-bottom: 25px; text-align: center;">Новая вакансия</h2>
        <form method="POST">
            <input type="text" name="title" placeholder="Название вакансии" required>
            <input type="text" name="price" placeholder="Зарплата (например: 50к)" required>
            <input type="text" name="loc" placeholder="Город (например: Бишкек)" required>
            <select name="cat">
                <option value="Медиа">🎥 Медиа</option>
                <option value="IT">💻 IT</option>
                <option value="Услуги">🛠️ Услуги</option>
            </select>
            <input type="text" name="wa" placeholder="WhatsApp (без +)" required>
            <button type="submit" class="btn btn-primary">Опубликовать</button>
            <a href="{{ url_for('index') }}" style="display:block; text-align:center; margin-top:20px; color:#999; text-decoration:none;">Назад</a>
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
        icons = {"Медиа": "🎥", "IT": "💻", "Услуги": "🛠️"}
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

if __name__ == "__main__":
    app.run()
