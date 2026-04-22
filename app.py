from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Убактылуу база
jobs = [
    {"cat": "Медиа", "loc": "Бишкек", "title": "Профессионал Мобилограф", "price": "50,000 сом", "wa": "996555001122"},
    {"cat": "IT", "loc": "Ош", "title": "Python Программист", "price": "100,000 сом", "wa": "996700112233"}
]

# --- СТИЛЬ ЖАНА ФОН ---
STYLE = """
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;800&family=Inter:wght@300;600&display=swap" rel="stylesheet">
<style>
    :root { --neon: #00ff41; --glass: rgba(0, 0, 0, 0.6); --border: rgba(255, 255, 255, 0.15); }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body { 
        font-family: 'Inter', sans-serif; 
        color: white; 
        background-color: #000;
        /* ЖУМУШЧУЛАРДЫН СҮРӨТҮ УШУЛ ЖЕРДЕ */
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.85)), 
                          url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }

    .container { max-width: 450px; margin: 0 auto; padding: 25px; min-height: 100vh; }

    .glass-card { 
        background: var(--glass); 
        backdrop-filter: blur(12px); 
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border); 
        border-radius: 28px; 
        padding: 25px; 
        margin-bottom: 20px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        animation: fadeInUp 0.8s ease;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .btn { 
        display: block; width: 100%; padding: 18px; border-radius: 20px; 
        text-decoration: none; font-weight: 700; text-align: center; 
        transition: 0.3s; border: none; cursor: pointer; font-family: 'Outfit';
    }
    .btn-primary { background: var(--neon); color: #000; }
    .btn-secondary { background: rgba(255,255,255,0.1); color: #fff; border: 1px solid var(--border); }
    
    .job-title { font-family: 'Outfit'; font-size: 22px; font-weight: 700; margin: 10px 0; color: #fff; }
    .price { font-size: 26px; font-weight: 300; margin-bottom: 20px; color: var(--neon); }
    
    .wa-link { 
        color: #fff; text-decoration: none; font-weight: 600; 
        display: flex; justify-content: space-between; align-items: center;
        border-top: 1px solid var(--border); padding-top: 15px; font-size: 14px;
    }

    input, select {
        width: 100%; padding: 16px; margin-bottom: 15px; border-radius: 15px;
        border: 1px solid var(--border); background: rgba(0,0,0,0.7); color: white;
    }
</style>
"""

INDEX_HTML = STYLE + """
<div class="container">
    <header style="text-align: center; padding: 60px 0 40px 0;">
        <h1 style="font-family: 'Outfit'; font-size: 42px; font-weight: 800; letter-spacing: -2px; margin-bottom: 35px; text-shadow: 0 4px 15px rgba(0,0,0,1);">JUMUSH BAR</h1>
        <div style="display: flex; gap: 15px;">
            <a href="{{ url_for('add_job') }}" class="btn btn-primary" style="flex: 1.2;">+ Жарыя кошуу</a>
            <a href="#" class="btn btn-secondary" style="flex: 0.8;">Кирүү</a>
        </div>
    </header>

    {% for job in jobs %}
    <div class="glass-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="color: var(--neon); font-size: 11px; font-weight: 8
import os
from flask import Flask, render_template_string, request, redirect, url_for
from supabase import create_client, Client

app = Flask(__name__)

# СУПАБЕЙС ТУТАШТЫРУУ (Бул маалыматтарды Supabase панелинден аласың)
SUPABASE_URL = "СЕНИН_SUPABASE_URL_УШУЛ_ЖЕРГЕ"
SUPABASE_KEY = "СЕНИН_SUPABASE_KEY_УШУЛ_ЖЕРГЕ"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- СТИЛЬ (Мурункудай калат, өзгөртүлгөн жок) ---
STYLE = """ ... (мурунку дизайн коддору) ... """

@app.route('/')
def index():
    # Базадан бардык жумуштарды алуу
    response = supabase.table("jobs").select("*").order("created_at", desc=True).execute()
    db_jobs = response.data
    return render_template_string(INDEX_HTML, jobs=db_jobs)

@app.route('/add', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        cat = request.form.get('cat')
        icons = {"Медиа": "🎥", "IT": "💻", "Кызмат": "🛠️"}
        
        new_data = {
            "title": request.form.get('title'),
            "price": request.form.get('price'),
            "loc": "Бишкек",
            "cat": cat,
            "icon": icons.get(cat, "💼"),
            "wa": request.form.get('wa')
        }
        # Базага жаңы маалымат кошуу
        supabase.table("jobs").insert(new_data).execute()
        return redirect(url_for('index'))
    return render_template_string(ADD_JOB_HTML)
