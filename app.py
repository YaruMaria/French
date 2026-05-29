from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from course_data import COURSE_DAYS
from reading_data import READINGS

app = Flask(__name__)
app.secret_key = 'ultra_secure_and_secret_key_french_84_days'

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///french_course.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Модели Базы Данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    progress = db.relationship('Progress', backref='user', lazy=True)
    advanced_progress = db.relationship('AdvancedProgress', backref='user', lazy=True)
    reading_progress = db.relationship('ReadingProgress', backref='user', lazy=True)


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day_id = db.Column(db.String(50), nullable=False)


class AdvancedProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day_id = db.Column(db.String(50), nullable=False)
    lesson_name = db.Column(db.String(200))


class ReadingProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reading_id = db.Column(db.String(50), nullable=False)
    part_num = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, default=False)


# Создание таблиц БД
with app.app_context():
    db.create_all()

# Данные для продвинутого курса
ADVANCED_DAYS = {
    # ========== ДЕНЬ 1: В МАГАЗИНЕ ==========
    1: {
        "title": "🎯 В магазине",
        "type": "shopping_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 2: ЧТЕНИЕ (Глава 5, часть 2/2) ==========
    2: {
        "title": "📖 Чтение: Капитанская дочка (Глава V, часть 2/2 — La lettre du père)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 18,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 3: ТРАНСПОРТ / МЕТРО ==========
    3: {
        "title": "🚇 В транспорте — практика",
        "type": "transport_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 4: ЧТЕНИЕ (Глава 6, часть 1/2) ==========
    4: {
        "title": "📖 Чтение: Капитанская дочка (Глава VI, часть 1/2 — L'arrivée de Pougatcheff)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 19,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 5: В КАФЕ / РЕСТОРАНЕ ==========
    5: {
        "title": "☕ В кафе / ресторане",
        "type": "cafe_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 6: ЧТЕНИЕ (Глава 6, часть 2/2) ==========
    6: {
        "title": "📖 Чтение: Капитанская дочка (Глава VI, часть 2/2 — Les préparatifs)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 20,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 7: В ТЕАТРЕ / КИНО ==========
    7: {
        "title": "🎬 В театре / кино",
        "type": "cinema_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 8: ЧТЕНИЕ (Глава 7, часть 1/2) ==========
    8: {
        "title": "📖 Чтение: Капитанская дочка (Глава VII, часть 1/2 — L'assaut, la nuit avant)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 21,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 9: В МУЗЕЕ ==========
    9: {
        "title": "🖼️ В музее",
        "type": "museum_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 10: ЧТЕНИЕ (Глава 7, часть 2/2) ==========
    10: {
        "title": "📖 Чтение: Капитанская дочка (Глава VII, часть 2/2 — La mort du commandant)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 22,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 11: В ОТЕЛЕ / ГОСТИНИЦЕ ==========
    11: {
        "title": "🏨 В отеле / гостинице",
        "type": "hotel_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 12: ЧТЕНИЕ (Глава 8, часть 1/2) ==========
    12: {
        "title": "📖 Чтение: Капитанская дочка (Глава VIII, часть 1/2 — La grâce inattendue)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 23,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 13: НА ВОКЗАЛЕ / В АЭРОПОРТУ ==========
    13: {
        "title": "🚉 На вокзале / в аэропорту",
        "type": "station_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 14: ЧТЕНИЕ (Глава 8, часть 2/2) ==========
    14: {
        "title": "📖 Чтение: Капитанская дочка (Глава VIII, часть 2/2 - Le souper chez Pougatcheff)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 24,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 15: У ВРАЧА / В АПТЕКЕ ==========
    15: {
        "title": "👨‍⚕️ У врача / в аптеке",
        "type": "doctor_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 16: ЧТЕНИЕ (Глава 9, часть 1/2) ==========
    16: {
        "title": "📖 Чтение: Капитанская дочка (Глава IX, часть 1/2 - La séparation)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 25,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 17: НА ПОЧТЕ ==========
    17: {
        "title": "📮 На почте",
        "type": "post_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 18: ЧТЕНИЕ (Глава 9, часть 2/2) ==========
    18: {
        "title": "📖 Чтение: Капитанская дочка (Глава IX, часть 2/2 - Le départ et le cadeau)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 26,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 19: НА ЭКСКУРСИИ ==========
    19: {
        "title": "🗺️ На экскурсии",
        "type": "excursion_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 20: ЧТЕНИЕ (Глава 10, полностью) ==========
    20: {
        "title": "📖 Чтение: Капитанская дочка (Глава X - Le siège)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 27,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 21: ПОТЕРЯЛСЯ / СПРОСИТЬ ДОРОГУ ==========
    21: {
        "title": "🧭 Потерялся / спросить дорогу",
        "type": "lost_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 22: ЧТЕНИЕ (Глава 11) ==========
    22: {
        "title": "📖 Чтение: Капитанская дочка (Глава XI - XII)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 29,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 23: РАЗГОВОР С ДРУЗЬЯМИ ==========
    23: {
        "title": "👥 Разговор с друзьями — практика",
        "type": "friends_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 24: ЧТЕНИЕ (Глава 12) ==========
    24: {
        "title": "📖 Чтение: Капитанская дочка (Глава XIII - XIV)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 30,
        "correct_answer": "готово"
    },
}
# Заполним заглушками на 24 дня



# ========================================================
# ГЛАВНАЯ СТРАНИЦА
# ========================================================
@app.route('/')
def index():
    months_info = {
        1: {"title": "Базовый курс: Месяц 1",
            "desc": "Фонетика, правила чтения, базовая лексика и грамматика. Чтение 'Капитанской дочки'.",
            "badge": "Уровень A1"},
        2: {"title": "Базовый курс: Месяц 2",
            "desc": "Продолжаем изучение грамматики, времена глаголов, лексика. Чтение 'Капитанской дочки'.",
            "badge": "Уровень A2.1"},
        3: {"title": "Базовый курс: Месяц 3",
            "desc": "Завершаем базовый курс: все основные времена и наклонения. Чтение 'Капитанской дочки'.",
            "badge": "Уровень A2.2+"},
        4: {"title": "Продвинутый курс (24 дня)",
            "desc": "Разговорный французский на каждый день: магазин, транспорт, кафе, театр, музей, отель и многое другое.",
            "badge": "Уровень B1", "advanced": True}
    }
    return render_template('index.html', months=months_info)


# ========================================================
# СТРАНИЦА МЕСЯЦА
# ========================================================
@app.route('/month/<int:month_id>')
def month_view(month_id):
    if month_id not in [1, 2, 3, 4]:
        flash('Такой месяц не найден в программе.', 'error')
        return redirect(url_for('index'))

    is_advanced = (month_id == 4)
    user_id = session.get('user_id')
    completed_days = []

    if user_id:
        if is_advanced:
            completed = AdvancedProgress.query.filter_by(user_id=user_id).all()
            completed_days = [p.day_id for p in completed]
        else:
            completed = Progress.query.filter_by(user_id=user_id).all()
            completed_days = [p.day_id for p in completed]

    # ========== ГЛАВНОЕ ИСПРАВЛЕНИЕ ЗДЕСЬ ==========
    month_days = {}

    if is_advanced:
        # Для продвинутого курса (месяц 4) - берем из ADVANCED_DAYS
        for key, data in ADVANCED_DAYS.items():
            month_days[key] = data
    else:
        # Для месяцев 1, 2, 3 - берем из COURSE_DAYS
        # ВАЖНО: нужно брать ТОЛЬКО дни для этого месяца!
        if month_id == 1:
            day_range = range(1, 31)  # Дни 1-30
        elif month_id == 2:
            day_range = range(31, 62)  # Дни 31-61 (исправлено!)
        elif month_id == 3:
            day_range = range(62, 68)  # Дни 62-92
        else:
            day_range = []

        for day_num in day_range:
            if day_num in COURSE_DAYS:
                month_days[day_num] = COURSE_DAYS[day_num]

    # Для отладки - выведем в консоль, какие дни загрузились
    print(f"=== Month {month_id} loaded {len(month_days)} days ===")
    print(f"First 10 days: {list(month_days.keys())[:10]}")

    return render_template('month.html',
                           month_id=month_id,
                           days=month_days,
                           completed_days=completed_days,
                           COURSE_DAYS=COURSE_DAYS,
                           month_name=month_id,
                           is_advanced=is_advanced)


# ========================================================
# СТРАНИЦА ОБЫЧНОГО УРОКА/ТЕСТА
# ========================================================
@app.route('/day/<day_id>', methods=['GET', 'POST'])
def day(day_id):
    try:
        day_id_int = int(day_id)
        if day_id_int in COURSE_DAYS:
            day_id = day_id_int
    except (ValueError, TypeError):
        pass

    if day_id not in COURSE_DAYS:
        flash('Такой урок не найден!', 'error')
        return redirect(url_for('index'))

    day_item = COURSE_DAYS[day_id]

    try:
        day_num = int(day_id)
        if 1 <= day_num <= 30:
            month_id = 1
        elif 31 <= day_num <= 61:
            month_id = 2
        elif 62 <= day_num <= 92:
            month_id = 3
        else:
            month_id = 1
    except:
        month_id = 1

    feedback = None
    is_correct = False
    already_completed = False
    user_id = session.get('user_id')

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        correct = day_item.get('correct_answer', '').strip().lower()

        if user_answer == correct:
            is_correct = True
            feedback = "✅ Правильно! Отличная работа!"

            if user_id:
                existing = Progress.query.filter_by(user_id=user_id, day_id=str(day_id)).first()
                if not existing:
                    new_progress = Progress(user_id=user_id, day_id=str(day_id))
                    db.session.add(new_progress)
                    db.session.commit()
                    feedback = "✅ Правильно! Прогресс сохранен! 🎉"
                else:
                    already_completed = True
                    feedback = "✅ Правильно! (Вы уже проходили этот урок)"
        else:
            is_correct = False
            feedback = f"❌ Неправильно. Правильный ответ: {correct}"

    if user_id and not already_completed:
        existing = Progress.query.filter_by(user_id=user_id, day_id=str(day_id)).first()
        if existing:
            already_completed = True

    total_days = 92

    if day_item.get('type') == 'reading':
        reading_id = day_item.get('reading_id', 'captains_daughter')
        chapter_part = day_item.get('chapter_part', 1)
        reading_data = READINGS.get(reading_id, {})
        part_data = reading_data.get('parts', {}).get(chapter_part, {})
        reading_info = {
            'title': reading_data.get('title', 'La Fille du capitaine'),
            'subtitle': part_data.get('title', f'Partie {chapter_part}'),
            'text': part_data.get('text', '<p>Текст не найден</p>'),
            'questions': part_data.get('questions', [])
        }
        return render_template('reading.html',
                               day_id=day_id,
                               day=day_item,
                               reading=reading_info,
                               questions=reading_info['questions'],
                               part_num=chapter_part,
                               total_parts=reading_data.get('total_parts', 8),
                               reading_id=reading_id,
                               prev_part=chapter_part - 1 if chapter_part > 1 else None,
                               next_part=chapter_part + 1 if chapter_part < reading_data.get('total_parts',
                                                                                             8) else None,
                               feedback=feedback,
                               already_completed=already_completed,
                               total_days=total_days,
                               month_id=month_id)

    return render_template('day.html',
                           day_id=day_id,
                           day=day_item,
                           feedback=feedback,
                           is_correct=is_correct,
                           already_completed=already_completed,
                           total_days=total_days,
                           month_id=month_id)


# ========================================================
# СТРАНИЦА ПРОДВИНУТОГО УРОКА
# ========================================================
@app.route('/advanced_day/<int:day_id>', methods=['GET', 'POST'])
def advanced_day(day_id):
    if day_id not in ADVANCED_DAYS:
        flash('Продвинутый урок не найден!', 'error')
        return redirect(url_for('index'))

    day_item = ADVANCED_DAYS[day_id]
    user_id = session.get('user_id')
    feedback = None
    already_completed = False

    # Если это чтение — загружаем текст и вопросы
    # Если это чтение — загружаем текст и вопросы
    if day_item.get('type') == 'advanced_reading':
        reading_id = day_item.get('reading_id', 'captains_daughter')
        chapter_part = day_item.get('chapter_part', 1)
        reading_data = READINGS.get(reading_id, {})
        part_data = reading_data.get('parts', {}).get(chapter_part, {})
        day_item['reading_data'] = {
            'title': part_data.get('title', f'Часть {chapter_part}'),
            'text': part_data.get('text', '<p>Текст не найден</p>'),
            'questions': part_data.get('questions', [])
        }

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()
        correct = day_item.get('correct_answer', '').strip().lower()

        if user_answer == correct:
            if user_id:
                existing = AdvancedProgress.query.filter_by(user_id=user_id, day_id=str(day_id)).first()
                if not existing:
                    new_progress = AdvancedProgress(user_id=user_id, day_id=str(day_id), lesson_name=day_item['title'])
                    db.session.add(new_progress)
                    db.session.commit()
                    feedback = "✅ Успех! Вы освоили этот урок! 🎉"
                else:
                    already_completed = True
                    feedback = "✅ Вы уже проходили этот урок."
        else:
            feedback = f"❌ Введите 'готово', чтобы отметить урок как пройденный."

    if user_id:
        existing = AdvancedProgress.query.filter_by(user_id=user_id, day_id=str(day_id)).first()
        if existing:
            already_completed = True

    return render_template('advanced_day.html', day=day_item, day_id=day_id, feedback=feedback,
                           already_completed=already_completed)

# ========================================================
# СТРАНИЦА ПРОГРЕССА ЧТЕНИЯ
# ========================================================
@app.route('/reading_tracker', methods=['GET', 'POST'])
def reading_tracker():
    user_id = session.get('user_id')
    if not user_id:
        flash('Войдите, чтобы отслеживать прогресс чтения.', 'error')
        return redirect(url_for('login'))

    reading_data = READINGS.get("captains_daughter", {})
    total_parts = reading_data.get('total_parts', 16)
    completed_parts = []

    completed_records = ReadingProgress.query.filter_by(user_id=user_id, reading_id="captains_daughter").all()
    for record in completed_records:
        completed_parts.append(record.part_num)

    if request.method == 'POST':
        part_to_mark = int(request.form.get('part_num', 0))
        if 1 <= part_to_mark <= total_parts:
            existing = ReadingProgress.query.filter_by(user_id=user_id, reading_id="captains_daughter",
                                                       part_num=part_to_mark).first()
            if not existing:
                new_progress = ReadingProgress(user_id=user_id, reading_id="captains_daughter", part_num=part_to_mark,
                                               completed=True)
                db.session.add(new_progress)
                db.session.commit()
                flash(f'Часть {part_to_mark} отмечена как прочитанная!', 'success')
                return redirect(url_for('reading_tracker'))
            else:
                flash(f'Вы уже отмечали часть {part_to_mark}.', 'info')

        return redirect(url_for('reading_tracker'))

    parts_info = []
    for i in range(1, total_parts + 1):
        part_data = reading_data.get('parts', {}).get(i, {})
        parts_info.append({
            'num': i,
            'title': part_data.get('title', f'Часть {i}'),
            'completed': i in completed_parts
        })

    return render_template('reading_tracker.html', parts=parts_info, total_parts=total_parts)


# ========================================================
# РЕГИСТРАЦИЯ
# ========================================================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if User.query.filter_by(username=username).first():
            flash('Пользователь с таким именем уже существует!', 'error')
            return redirect(url_for('register'))

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        session['user_id'] = new_user.id
        session['username'] = new_user.username

        flash(f'Аккаунт успешно создан! Добро пожаловать на курс, {new_user.username}! 🎉', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', is_register=True)


# ========================================================
# ВХОД
# ========================================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Добро пожаловать, {user.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неверное имя пользователя или пароль.', 'error')

    return render_template('login.html', is_register=False)


# ========================================================
# ВЫХОД
# ========================================================
@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('index'))


# ========================================================
# ЛИЧНЫЙ КАБИНЕТ / ПРОГРЕСС
# ========================================================
@app.route('/progress')
def progress():
    user_id = session.get('user_id')
    if not user_id:
        flash('Войдите, чтобы увидеть свой прогресс.', 'error')
        return redirect(url_for('login'))

    completed = Progress.query.filter_by(user_id=user_id).all()
    completed_advanced = AdvancedProgress.query.filter_by(user_id=user_id).all()
    completed_reading = ReadingProgress.query.filter_by(user_id=user_id, reading_id="captains_daughter").all()

    completed_days_str = [p.day_id for p in completed]
    advanced_count = len(completed_advanced)
    reading_count = len(completed_reading)

    numeric_completed = []
    for d in completed_days_str:
        try:
            numeric_completed.append(int(d))
        except (ValueError, TypeError):
            pass

    total_days = 92
    completed_count = len([d for d in numeric_completed if 1 <= d <= 92])
    percent = int((completed_count / total_days) * 100) if total_days > 0 else 0

    month1_count = sum(1 for d in numeric_completed if 1 <= d <= 30)
    month2_count = sum(1 for d in numeric_completed if 31 <= d <= 61)
    month3_count = sum(1 for d in numeric_completed if 62 <= d <= 92)
    tests_passed = len([d for d in completed_days_str if d.startswith('test_')])

    return render_template(
        'progress.html',
        completed_days=sorted(numeric_completed),
        total=total_days,
        count=completed_count,
        percent=percent,
        days=COURSE_DAYS,
        month1_count=month1_count,
        month2_count=month2_count,
        month3_count=month3_count,
        tests_passed=tests_passed,
        advanced_count=advanced_count,
        reading_count=reading_count,
        total_advanced=24,
        total_reading_parts=16
    )


# ========================================================
# СЛОВАРИК (все выученные слова)
# ========================================================
@app.route('/dictionary')
def dictionary():
    user_id = session.get('user_id')
    if not user_id:
        flash('Войдите, чтобы увидеть свой словарик.', 'error')
        return redirect(url_for('login'))

    completed = Progress.query.filter_by(user_id=user_id).all()
    completed_days = [p.day_id for p in completed]

    learned_words = []
    for day_id in completed_days:
        try:
            day_num = int(day_id)
            if day_num in COURSE_DAYS and COURSE_DAYS[day_num].get('type') == 'lesson':
                vocabulary = COURSE_DAYS[day_num].get('vocabulary', [])
                for word in vocabulary:
                    # Простая проверка, чтобы не было дублей (по желанию можно усложнить)
                    if word not in learned_words:
                        learned_words.append(word)
        except (ValueError, TypeError):
            pass

    return render_template('dictionary.html',
                           words=learned_words,
                           total_words=len(learned_words))


if __name__ == '__main__':
    app.run(debug=True)