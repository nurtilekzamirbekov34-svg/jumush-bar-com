from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Убактылуу база (Сайт иштеп турганда маалыматтар сакталат)
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Профессионал Мобилограф", "price": "60,000 сом", "wa": "996555001122", "icon": "🎥"},
    {"cat": "IT", "loc": "Ош", "title": "Python Программист", "price": "120,000 сом", "wa": "996700112233", "icon": "💻"},
    {"cat": "Кызмат", "loc": "Бишкек", "title": "Администратор", "price": "35,000 сом", "wa": "996500445566", "icon": "🛠️"}
]

# --- БҮТҮН ДИЗАЙН (CSS) ---
STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --glass: rgba(15, 15, 15, 0.75); --border: rgba(255, 255, 255, 0.12); }
    * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
    
    body { 
        font-family: 'Inter', sans-serif; 
        color: white; 
        background: #000 url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1350&q=80') no-repeat center center fixed;
        background-size: cover;
    }

    /* Фонду караңгылатуу катмары */
    body::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at top, rgba(0,0,0,0.4), rgba(0,0,0,0.9));
        z-index: -1;
    }

    .container { max-width: 480px; margin: 0 auto; padding: 25px; min-height: 100vh; }

    /* Жогорку бөлүк */
    header { text-align: center; padding: 50px 0 30px 0; animation: fadeInDown 1s ease; }
    .logo { font-family: 'Outfit'; font-size: 48px; font-weight: 900; letter-spacing: -2px; margin-bottom: 10px; text-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    
    /* Издөө тилкеси */
    .search-bar {
        background: var(--glass); border: 1px solid var(--border); backdrop-filter: blur(15px);
        border-radius: 20px; padding: 15px 20px; margin-bottom: 30px; display: flex; align-items: center;
    }
    .search-bar input { background: transparent; border: none; color: white; width: 100%; outline: none; font-size: 16px; }

    /* Карталар */
    .glass-card { 
        background: var(--glass); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border); border-radius: 32px; padding: 25px; margin-bottom: 20px; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease both;
    }
    .glass-card:hover { transform: translateY(-8px); border-color: var(--neon); box-shadow: 0 20px 40px rgba(0, 255, 65, 0.15); }

    .badge {
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(255,255,255,0.08); padding: 6px 14px; border-radius: 12px;
        font-size: 11px; font-weight: 800; color: var(--neon); text-transform: uppercase; margin-bottom: 15px;
    }

    .job-title { font-family: 'Outfit'; font-size: 24px; font-weight: 700; margin-bottom: 6px; }
    .price { font-size: 28px; font-weight: 300; color: #fff; margin-bottom: 25px; }

    /* Баскычтар */
    .btn { 
        display: block; width: 100%; padding: 18px; border-radius: 22px; 
        text-decoration: none; font-weight: 800; text-align: center; 
        transition: 0.3s; cursor: pointer; font-family: 'Outfit'; border: none;
    }
    .btn-primary { background: white; color: black; margin-bottom: 12px; }
    .btn-secondary { background: rgba(255,255,255,0.1); color: white; border: 1px solid var(--border); }
    .btn:active { transform: scale(0.95); }

    .wa-action {
        display: flex; justify-content: space-between; align-items: center;
        color: var(--neon); text-decoration: none; font-weight: 700; font-size: 15px;
        border-top: 1px solid var(--border); padding-top: 18px;
    }

    /* Анимациялар */
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-40px); } to { opacity: 1; transform: translateY(0); } }

    /* Форма талаалары */
    .input-field {
        width: 100%; padding: 18px; margin-bottom: 15px; border-radius: 18px;
        border: 1px solid var(--border); background: rgba(0,0,0,0.5); color: white; outline: none;
    }
</style>
"""

# --- БАШКЫ БЕТ (INDEX) ---
INDEX_HTML = STYLE + """
<div class="container">
    <header>
        <div class="logo">JUMUSH BAR</div>
        <p style="color: #999; font-size: 14px; margin-bottom: 30px;">Кыргызстандагы №1 жумуш издөө порталы</p>
        
        <div class="search-bar">
            <input type="text" placeholder="Жумуш издөө (мис: Мобилограф)">
        </div>

        <div style="display: flex; gap: 12px; margin-bottom: 20px;">
            <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1.2;">+ Жарыя кошуу</a>
            <a href="#" class="btn btn-secondary" style="flex: 0.8;">Катталуу</a>
        </div>
    </header>

    {% for job in jobs %}
    <div class="glass-card">
        <div class="badge">
            <span>{{ job.icon }}</span> {{ job.cat }} • {{ job.loc }}
        </div>
        <h2 class="job-title">{{ job.title }}</h2>
        <div class="price">{{ job.price }}</div>
        <a href="https://wa.me/{{ job.wa }}" class="wa-action">
            <span>WhatsApp аркылуу байланышуу</span>
            <span style="font-size: 20px;">→</span>
        </a>
    </div>
    {% endfor %}

    <footer style="text-align: center; padding: 40px 0; color: #555; font-size: 12px; letter-spacing: 1px;">
        © 2026 JUMUSH BAR | Дизайн: @zam1rbekovibe
    </footer>
</div>
"""

# --- ЖУМУШ КОШУУ БЕТИ (ADD) ---
ADD_JOB_HTML = STYLE + """
<div class="container">
    <div class="glass-card" style="margin-top: 50px;">
        <h2 style="font-family: 'Outfit'; font-size: 30px; margin-bottom: 25px; text-align: center;">Жаңы жарыя</h2>
        <form method="POST">
            <input type="text" name="title" class="input-field" placeholder="Жумуштун аты" required>
            <input type="text" name="price" class="input-field" placeholder="Айлыгы (мис: 50,000 сом)" required>
            <input type="text" name="loc" class="input-field" placeholder="Кайсыл жерде? (мис: Бишкек)" required>
            <select name="cat" class="input-field">
                <option value="Медиа">🎥 Медиа</option>
                <option value="IT">💻 IT</option>
                <option value="Кызмат">🛠️ Кызмат</option>
                <option value="Башка">💼 Башка</option>
            </select>
            <input type="text" name="wa" class="input-field" placeholder="WhatsApp (мис: 996700...)" required>
            <button type="submit" class="btn btn-primary" style="margin-top: 10px;">Жарыялоо</button>
            <a href="{{ url_for('index') }}" style="display:block; text-align:center; margin-top:20px; color:#999; text-decoration:none; font-size:14px;">← Артка кайтуу</a>
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
        icons = {"Медиа": "🎥", "IT": "💻", "Кызмат": "🛠️", "Башка": "💼"}
        
        new_job = {
            "title": request.form.get('title'),
            "price": request.form.get('price'),
            "loc": request.form.get('loc
