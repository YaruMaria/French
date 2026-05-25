from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from course_data import COURSE_DAYS

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
    day_id = db.Column(db.Integer, nullable=False)


# Создание таблиц БД в контексте приложения
with app.app_context():
    db.create_all()


# 1. Главная страница (Выбор месяца)
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


# 2. Страница конкретного месяца (ИСПРАВЛЕННАЯ ВЕРСИЯ)
@app.route('/month/<int:month_id>')
def month_view(month_id):
    # Убедись, что список месяцев прописан ровно так
    if month_id not in [1, 2, 3]:
        flash('Такой месяц не найден в программе.', 'error')
        return redirect(url_for('index'))

    user_id = session.get('user_id')
    completed_days = []
    if user_id:
        completed = Progress.query.filter_by(user_id=user_id).all()
        completed_days = [p.day_id for p in completed]

    # Фильтруем дни, которые относятся к выбранному месяцу
    month_days = {}
    for day_id, data in COURSE_DAYS.items():
        if month_id == 1 and 1 <= day_id <= 28:
            month_days[day_id] = data
        elif month_id == 2 and 29 <= day_id <= 56:
            month_days[day_id] = data
        elif month_id == 3 and 57 <= day_id <= 84:
            month_days[day_id] = data

    return render_template('month.html', month_id=month_id, days=month_days, completed_days=completed_days)


# Страница регистрации
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


# Страница входа
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


# Выход из аккаунта
@app.route('/logout')
def logout():
    session.clear()
    flash('Вы вышли из системы.', 'success')
    return redirect(url_for('index'))


# Страница конкретного дня (ИСПРАВЛЕННАЯ ВЕРСИЯ)
@app.route('/day/<int:day_id>', methods=['GET', 'POST'])
def day(day_id):
    # Проверяем, существует ли такой день
    if day_id not in COURSE_DAYS:
        flash('Такой урок не найден!', 'error')
        return redirect(url_for('index'))

    # Загружаем данные дня из COURSE_DAYS
    day_item = COURSE_DAYS[day_id]

    feedback = None
    is_correct = False
    already_completed = False
    user_id = session.get('user_id')

    # Проверка правильности ответа (для финальной отправки формы)
    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip().lower()

        # Если пользователь отправил "готово" - значит прошел все карточки
        if user_answer == "готово":
            is_correct = True
            feedback = "✅ Отлично! Вы успешно прошли все задания дня!"

            # Сохраняем прогресс в базу данных
            if user_id:
                existing = Progress.query.filter_by(user_id=user_id, day_id=day_id).first()
                if not existing:
                    new_progress = Progress(user_id=user_id, day_id=day_id)
                    db.session.add(new_progress)
                    db.session.commit()
                    feedback = "✅ Поздравляю! День засчитан и сохранен в прогрессе! 🎉"
                else:
                    already_completed = True
                    feedback = "✅ Этот день уже был пройден ранее!"
        else:
            correct = day_item.get('correct_answer', '').strip().lower()
            if user_answer == correct:
                is_correct = True
                feedback = "✅ Правильно! Отличная работа!"

                if user_id:
                    existing = Progress.query.filter_by(user_id=user_id, day_id=day_id).first()
                    if not existing:
                        new_progress = Progress(user_id=user_id, day_id=day_id)
                        db.session.add(new_progress)
                        db.session.commit()
                        feedback = "✅ Правильно! Прогресс сохранен! 🎉"
                    else:
                        already_completed = True
                        feedback = "✅ Правильно! (Вы уже проходили этот урок)"
            else:
                is_correct = False
                feedback = f"❌ Неправильно. Попробуйте еще раз!"

    # Проверяем, пройден ли уже этот день (при GET запросе)
    if user_id and not already_completed:
        existing = Progress.query.filter_by(user_id=user_id, day_id=day_id).first()
        if existing:
            already_completed = True

    # Общее количество дней
    total_days = len(COURSE_DAYS)

    return render_template('day.html',
                           day_id=day_id,
                           day=day_item,
                           feedback=feedback,
                           is_correct=is_correct,
                           already_completed=already_completed,
                           total_days=total_days
                           )


# Личный кабинет / Прогресс
@app.route('/progress')
def progress():
    user_id = session.get('user_id')
    if not user_id:
        flash('Войдите, чтобы увидеть свой прогресс.', 'error')
        return redirect(url_for('login'))

    completed = Progress.query.filter_by(user_id=user_id).all()
    completed_days = [p.day_id for p in completed]

    total_days = len(COURSE_DAYS)
    completed_count = len(completed_days)
    percent = int((completed_count / total_days) * 100) if total_days > 0 else 0

    month1_count = sum(1 for d in completed_days if 1 <= d <= 28)
    month2_count = sum(1 for d in completed_days if 29 <= d <= 56)
    month3_count = sum(1 for d in completed_days if 57 <= d <= 84)

    return render_template(
        'progress.html',
        completed_days=sorted(completed_days),
        total=total_days,
        count=completed_count,
        percent=percent,
        days=COURSE_DAYS,
        month1_count=month1_count,
        month2_count=month2_count,
        month3_count=month3_count
    )


if __name__ == '__main__':
    app.run(debug=True)