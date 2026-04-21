from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

# Жумуштардын тизмеси
jobs = [
    {"location": "Бишкек", "title": "Мобилограф / Видеомейкер", "price": "40 000 сом", "wa": "996555001122"},
    {"location": "Ош", "title": "SMM адиси", "price": "25 000 сом", "wa": "996700112233"},
    {"location": "Бишкек", "title": "Графикалык дизайнер", "price": "50 000 сом", "wa": "996500445566"}
]

HTML_MAIN = """
<!DOCTYPE html>
<html lang="ky">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JUMUSH BAR | Профессионалдык деңгээл</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #000000;
            --secondary: #64748b;
            --accent: #2563eb;
            --bg: #f8fafc;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            margin: 0;
            background-color: var(--bg);
            /* Фонго заманбап, ак-боз эстетикадагы сүрөт */
            background-image: linear-gradient(rgba(248, 250, 252, 0.9), rgba(248, 250, 252, 0.9)), 
                              url('https://images.unsplash.com/photo-1497215728101-856f4ea42174?q=80&w=2070&auto=format&fit=crop');
            background-size: cover;
            background-attachment: fixed;
            color: var(--primary);
        }

        header {
            padding: 80px 20px 40px;
            text-align: center;
        }

        h1 {
            font-weight: 800;
            font-size: 3.5rem;
            margin: 0;
            letter-spacing: -2px;
            background: linear-gradient(to right, #000, #444);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            color: var(--secondary);
            font-size: 1.1rem;
            margin-top: 10px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        .nav-actions {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 50px;
        }

        .btn {
            padding: 14px 28px;
            border-radius: 12px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .btn-black {
            background: #000;
            color: #fff;
        }

        .btn-black:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .btn-ghost {
            border: 1px solid #e2e8f0;
            color: #000;
            background: rgba(255,255,255,0.5);
            backdrop-filter: blur(10px);
        }

        .btn-ghost:hover {
            background: rgba(255,255,255,0.8);
        }

        /* Заманбап жумуш карталары */
        .job-card {
            background: rgba(255, 255, 255, 0.
    
