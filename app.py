from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from course_data import COURSE_DAYS
from reading_data import READINGS  # ДОБАВЛЯЕМ ИМПОРТ

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


class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day_id = db.Column(db.String(50), nullable=False)


# Создание таблиц БД
with app.app_context():
    db.create_all()


# ========================================================
# ГЛАВНАЯ СТРАНИЦА
# ========================================================
@app.route('/')
def index():
    months_info = {
        1: {"title": "Месяц 1: Фундамент и Выживание",
            "desc": "Научитесь читать с нуля, строить первые фразы, заказывать еду в кафе и ориентироваться в городе.",
            "badge": "Уровень A1"},
        2: {"title": "Месяц 2: Разгон и Прошлое время",
            "desc": "Заговорите о своих привычках, планах и прошлом опыте. Освоите времена Passé Composé и Futur Proche.",
            "badge": "Уровень A2.1"},
        3: {"title": "Месяц 3: Свободное общение",
            "desc": "Научитесь выражать мнение, шутить, использовать французский сленг и местоимения-заменители.",
            "badge": "Уровень A2.2+"}
    }
    return render_template('index.html', months=months_info)


# ========================================================
# СТРАНИЦА МЕСЯЦА
# ========================================================
@app.route('/month/<int:month_id>')
def month_view(month_id):
    if month_id not in [1, 2, 3]:
        flash('Такой месяц не найден в программе.', 'error')
        return redirect(url_for('index'))

    user_id = session.get('user_id')
    completed_days = []
    if user_id:
        completed = Progress.query.filter_by(user_id=user_id).all()
        completed_days = [p.day_id for p in completed]

    # Распределение дней по месяцам
    month_days = {}
    for key, data in COURSE_DAYS.items():
        if not isinstance(key, int):
            continue
        day_id = key
        if month_id == 1 and 1 <= day_id <= 30:
            month_days[day_id] = data
        elif month_id == 2 and 31 <= day_id <= 61:
            month_days[day_id] = data
        elif month_id == 3 and 62 <= day_id <= 92:
            month_days[day_id] = data

    month_days = dict(sorted(month_days.items()))

    return render_template('month.html',
                           month_id=month_id,
                           days=month_days,
                           completed_days=completed_days,
                           COURSE_DAYS=COURSE_DAYS,
                           month_name=month_id)


# ========================================================
# СТРАНИЦА УРОКА/ТЕСТА/ЧТЕНИЯ
# ========================================================
@app.route('/day/<day_id>', methods=['GET', 'POST'])
def day(day_id):
    # Пробуем преобразовать в число
    try:
        day_id_int = int(day_id)
        if day_id_int in COURSE_DAYS:
            day_id = day_id_int
    except (ValueError, TypeError):
        pass

    # Проверяем существование
    if day_id not in COURSE_DAYS:
        flash('Такой урок не найден!', 'error')
        return redirect(url_for('index'))

    day_item = COURSE_DAYS[day_id]

    # Определяем месяц для навигации
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

    # Обработка ответа
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

    # Проверяем, пройден ли урок ранее
    if user_id and not already_completed:
        existing = Progress.query.filter_by(user_id=user_id, day_id=str(day_id)).first()
        if existing:
            already_completed = True

    total_days = 92

    # ====================================================
    # ЕСЛИ ЭТО ДЕНЬ ЧТЕНИЯ (type == 'reading')
    # ====================================================
    if day_item.get('type') == 'reading':
        reading_id = day_item.get('reading_id', 'captains_daughter')
        chapter_part = day_item.get('chapter_part', 1)

        # Получаем данные из reading_data.py
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

    # ====================================================
    # ЕСЛИ ЭТО ТЕСТ ИЛИ ОБЫЧНЫЙ УРОК
    # ====================================================
    return render_template('day.html',
                           day_id=day_id,
                           day=day_item,
                           feedback=feedback,
                           is_correct=is_correct,
                           already_completed=already_completed,
                           total_days=total_days,
                           month_id=month_id)


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

    # Разделяем числовые уроки и тесты
    numeric_completed = []
    test_completed = []
    for p in completed:
        day_id = p.day_id
        if isinstance(day_id, int) or (isinstance(day_id, str) and day_id.isdigit()):
            numeric_completed.append(int(day_id))
        else:
            test_completed.append(day_id)

    total_days = 92
    completed_count = len([d for d in numeric_completed if 1 <= d <= 92])
    percent = int((completed_count / total_days) * 100) if total_days > 0 else 0

    # Прогресс по месяцам (только числовые уроки)
    month1_count = sum(1 for d in numeric_completed if 1 <= d <= 30)
    month2_count = sum(1 for d in numeric_completed if 31 <= d <= 61)
    month3_count = sum(1 for d in numeric_completed if 62 <= d <= 92)

    # Количество пройденных тестов
    tests_passed = len(test_completed)

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
        tests_passed=tests_passed
    )


if __name__ == '__main__':
    app.run(debug=True)