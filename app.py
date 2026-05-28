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
        "title": "🎯 В магазине — практика",
        "type": "shopping_practice",
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 2: ЧТЕНИЕ (Глава VII, часть 1) ==========
    2: {
        "title": "Чтение: Капитанская дочка (Глава VII, часть 1/2)",
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

    # ========== ДЕНЬ 4: ЧТЕНИЕ (Глава VII, часть 2) ==========
    4: {
        "title": "Чтение: Капитанская дочка (Глава VII, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 22,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 5: В КАФЕ / РЕСТОРАНЕ ==========
    5: {
        "title": "Практика: В кафе / ресторане",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonsoir, vous avez une table pour deux ?
— Oui, bien sûr, par ici, Madame, Monsieur. Voici la carte.
— Merci. Qu'est-ce que vous nous recommandez ?
— Le plat du jour est un confit de canard avec des pommes de terre.
— Parfait, je vais prendre ça. Et en dessert ?
— La tarte aux pomches est délicieuse.
— D'accord, je prends la tarte. L'addition, s'il vous plaît !""",
            "ru": """— Добрый вечер, у вас есть столик на двоих?
— Да, конечно, сюда, мадам, мсье. Вот меню.
— Спасибо. Что вы нам посоветуете?
— Дежурное блюдо — конфи из утки с картофелем.
— Прекрасно, я возьму это. А на десерт?
— Яблочный пирог восхитителен.
— Хорошо, я беру пирог. Счёт, пожалуйста!"""
        },
        "phrases": [
            {"fr": "Une table pour deux, s'il vous plaît", "ru": "Столик на двоих, пожалуйста"},
            {"fr": "La carte, s'il vous plaît", "ru": "Меню, пожалуйста"},
            {"fr": "Je voudrais commander...", "ru": "Я хотел(а) бы заказать..."},
            {"fr": "Qu'est-ce que vous recommandez ?", "ru": "Что вы рекомендуете?"},
            {"fr": "L'addition, s'il vous plaît", "ru": "Счёт, пожалуйста"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 6: ЧТЕНИЕ (Глава VIII, часть 1) ==========
    6: {
        "title": "Чтение: Капитанская дочка (Глава VIII, часть 1/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 23,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 7: В ТЕАТРЕ / КИНО ==========
    7: {
        "title": "Практика: В театре / кино",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Deux places pour le film de ce soir, s'il vous plaît.
— À quelle séance ?
— À vingt heures.
— Il reste des places au premier rang ?
— Non, désolé, mais il y a des places au milieu de la salle.
— D'accord, je prends ces deux places. C'est combien ?
— Vingt euros. Bonne séance !""",
            "ru": """— Два билета на сегодняшний фильм, пожалуйста.
— На какой сеанс?
— На восемь вечера.
— Есть места в первом ряду?
— Нет, извините, но есть места в середине зала.
— Хорошо, я беру эти два места. Сколько?
— Двадцать евро. Приятного просмотра!"""
        },
        "phrases": [
            {"fr": "Deux places, s'il vous plaît", "ru": "Два билета, пожалуйста"},
            {"fr": "À quelle séance ?", "ru": "На какой сеанс?"},
            {"fr": "Quel film passe ce soir ?", "ru": "Какой фильм идёт сегодня вечером?"},
            {"fr": "C'est à quelle heure ?", "ru": "Во сколько?"},
            {"fr": "J'aimerais m'abonner", "ru": "Я хотел(а) бы купить абонемент"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 8: ЧТЕНИЕ (Глава VIII, часть 2) ==========
    8: {
        "title": "Чтение: Капитанская дочка (Глава VIII, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 24,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 9: В МУЗЕЕ ==========
    9: {
        "title": "Практика: В музее",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonjour, un billet pour le Louvre, s'il vous plaît.
— C'est 17 euros. Vous avez droit au tarif réduit ?
— Oui, je suis étudiant.
— Alors, c'est 13 euros. Voici votre billet. Les audioguides sont à l'accueil.
— Merci. Où se trouve la Joconde ?
— Au premier étage, dans la salle des États. Suivez les panneaux.""",
            "ru": """— Здравствуйте, один билет в Лувр, пожалуйста.
— 17 евро. У вас есть право на льготный билет?
— Да, я студент.
— Тогда 13 евро. Вот ваш билет. Аудиогиды на входе.
— Спасибо. Где находится Джоконда?
— На втором этаже, в зале Штатов. Следуйте за указателями."""
        },
        "phrases": [
            {"fr": "Un billet, s'il vous plaît", "ru": "Один билет, пожалуйста"},
            {"fr": "J'ai droit au tarif réduit", "ru": "У меня есть право на льготный билет"},
            {"fr": "Où se trouve... ?", "ru": "Где находится...?"},
            {"fr": "Est-ce qu'on peut prendre des photos ?", "ru": "Можно фотографировать?"},
            {"fr": "À quelle heure ferme le musée ?", "ru": "Во сколько закрывается музей?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 10: ЧТЕНИЕ (Глава IX, часть 1) ==========
    10: {
        "title": "Чтение: Капитанская дочка (Глава IX, часть 1/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 25,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 11: В ОТЕЛЕ / ГОСТИНИЦЕ ==========
    11: {
        "title": "Практика: В отеле / гостинице",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonsoir, j'ai une réservation au nom de Dupont.
— Oui, Monsieur Dupont. Une chambre double pour deux nuits, c'est bien ça ?
— Exactement. Est-ce que le petit déjeuner est inclus ?
— Oui, il est servi de 7h à 10h au premier étage.
— Parfait. À quelle heure dois-je libérer la chambre ?
— À midi. Voici votre clé, chambre 45.""",
            "ru": """— Добрый вечер, у меня забронирован номер на имя Дюпон.
— Да, мсье Дюпон. Двухместный номер на две ночи, верно?
— Точно. Завтрак включён?
— Да, он подаётся с 7 до 10 на втором этаже.
— Прекрасно. Во сколько я должен освободить номер?
— В 12. Вот ваш ключ, номер 45."""
        },
        "phrases": [
            {"fr": "J'ai une réservation", "ru": "У меня есть бронь"},
            {"fr": "Une chambre pour une nuit", "ru": "Номер на одну ночь"},
            {"fr": "Le petit déjeuner est inclus ?", "ru": "Завтрак включён?"},
            {"fr": "À quelle heure est le check-out ?", "ru": "Во сколько выезд?"},
            {"fr": "Puis-je avoir un autre oreiller ?", "ru": "Можно мне другую подушку?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 12: ЧТЕНИЕ (Глава IX, часть 2) ==========
    12: {
        "title": "Чтение: Капитанская дочка (Глава IX, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 26,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 13: НА ВОКЗАЛЕ / В АЭРОПОРТУ ==========
    13: {
        "title": "Практика: На вокзале / в аэропорту",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonjour, je voudrais un billet pour Lyon, s'il vous plaît.
— Aller simple ou aller-retour ?
— Aller simple. C'est combien ?
— 45 euros. Train de 14h30, quai numéro 3.
— Est-ce qu'il y a un wagon-restaurant ?
— Oui, au milieu du train. Bon voyage !""",
            "ru": """— Здравствуйте, я хотел бы билет до Лиона, пожалуйста.
— В один конец или туда и обратно?
— В один конец. Сколько стоит?
— 45 евро. Поезд в 14:30, платформа номер 3.
— Есть ли вагон-ресторан?
— Да, в середине поезда. Счастливого пути!"""
        },
        "phrases": [
            {"fr": "Un billet pour...", "ru": "Билет до..."},
            {"fr": "Aller simple ou aller-retour ?", "ru": "В один конец или туда и обратно?"},
            {"fr": "À quelle heure part le train ?", "ru": "Во сколько отправляется поезд?"},
            {"fr": "Quel est le quai ?", "ru": "Какая платформа?"},
            {"fr": "Où est le guichet ?", "ru": "Где касса?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 14: ЧТЕНИЕ (Глава X, часть 1) ==========
    14: {
        "title": "Чтение: Капитанская дочка (Глава X, часть 1/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 27,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 15: У ВРАЧА / В АПТЕКЕ ==========
    15: {
        "title": "Практика: У врача / в аптеке",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonjour, docteur, je ne me sens pas bien.
— Qu'est-ce que vous avez ?
— J'ai de la fièvre et je tousse depuis trois jours.
— Je vais vous prescrire des antibiotiques. Prenez une boîte par jour pendant une semaine.
— Merci, docteur. Où est la pharmacie la plus proche ?
— À deux rues d'ici, à gauche.""",
            "ru": """— Здравствуйте, доктор, я плохо себя чувствую.
— Что с вами?
— У меня температура, и я кашляю уже три дня.
— Я выпишу вам антибиотики. Принимайте по одной упаковке в день в течение недели.
— Спасибо, доктор. Где ближайшая аптека?
— Через две улицы отсюда, налево."""
        },
        "phrases": [
            {"fr": "J'ai de la fièvre", "ru": "У меня температура"},
            {"fr": "Je tousse", "ru": "Я кашляю"},
            {"fr": "J'ai mal à la tête / au ventre", "ru": "У меня болит голова / живот"},
            {"fr": "Une ordonnance, s'il vous plaît", "ru": "Рецепт, пожалуйста"},
            {"fr": "Avez-vous quelque chose contre la douleur ?", "ru": "У вас есть что-нибудь от боли?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 16: ЧТЕНИЕ (Глава X, часть 2) ==========
    16: {
        "title": "Чтение: Капитанская дочка (Глава X, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 28,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 17: НА ПОЧТЕ ==========
    17: {
        "title": "Практика: На почте",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonjour, je voudrais envoyer ce colis en Russie.
— Quel poids ?
— Environ deux kilos.
— Ça va coûter 25 euros par voie maritime, ou 40 euros par avion.
— Je préfère par avion. Combien de temps ça va mettre ?
— Environ 10 jours. Vous voulez une assurance ?
— Oui, s'il vous plaît. Voilà.""",
            "ru": """— Здравствуйте, я хотел бы отправить эту посылку в Россию.
— Какой вес?
— Около двух килограммов.
— Это будет стоить 25 евро морем или 40 евро самолётом.
— Я предпочитаю самолётом. Сколько времени это займёт?
— Около 10 дней. Хотите страховку?
— Да, пожалуйста. Вот."""
        },
        "phrases": [
            {"fr": "Je voudrais envoyer cette lettre", "ru": "Я хотел(а) бы отправить это письмо"},
            {"fr": "Combien coûte l'envoi ?", "ru": "Сколько стоит отправка?"},
            {"fr": "Par avion ou par voie maritime ?", "ru": "Самолётом или морем?"},
            {"fr": "Combien de temps ça va prendre ?", "ru": "Сколько времени это займёт?"},
            {"fr": "Je voudrais un timbre pour la France", "ru": "Мне нужна марка во Францию"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 18: ЧТЕНИЕ (Глава XI, часть 1) ==========
    18: {
        "title": "Чтение: Капитанская дочка (Глава XI, часть 1/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 29,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 19: НА ЭКСКУРСИИ ==========
    19: {
        "title": "Практика: На экскурсии",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Bonjour, est-ce que vous faites des visites guidées en russe ?
— Oui, la prochaine visite commence à 14 heures.
— Combien de temps dure la visite ?
— Environ deux heures. Nous allons voir le château et les jardins.
— Est-ce qu'on peut prendre des photos à l'intérieur ?
— Oui, mais sans flash, s'il vous plaît.""",
            "ru": """— Здравствуйте, у вас есть экскурсии на русском языке?
— Да, следующая экскурсия начинается в 14 часов.
— Сколько длится экскурсия?
— Около двух часов. Мы посмотрим замок и сады.
— Можно фотографировать внутри?
— Да, но без вспышки, пожалуйста."""
        },
        "phrases": [
            {"fr": "Une visite guidée en français", "ru": "Экскурсия на французском"},
            {"fr": "À quelle heure commence la visite ?", "ru": "Во сколько начинается экскурсия?"},
            {"fr": "Combien de temps dure la visite ?", "ru": "Сколько длится экскурсия?"},
            {"fr": "Est-ce qu'on peut prendre des photos ?", "ru": "Можно фотографировать?"},
            {"fr": "Quel est le prix de l'entrée ?", "ru": "Сколько стоит вход?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 20: ЧТЕНИЕ (Глава XI, часть 2) ==========
    20: {
        "title": "Чтение: Капитанская дочка (Глава XI, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 30,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 21: РАЗГОВОР С ДРУЗЬЯМИ ==========
    21: {
        "title": "Практика: Разговор с друзьями",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Salut Marie, ça va ?
— Très bien, et toi ?
— Ça va, merci. Qu'est-ce que tu fais ce week-end ?
— Je vais au cinéma avec des amis. Tu veux venir ?
— Avec plaisir ! Quel film ?
— Le nouveau film de Dupontel. Il paraît qu'il est super !
— Super, à quelle heure ?
— À 20h, devant le cinéma. On se retrouve là-bas ?""",
            "ru": """— Привет, Мари, как дела?
— Отлично, а ты?
— Хорошо, спасибо. Что ты делаешь в эти выходные?
— Я иду в кино с друзьями. Хочешь пойти?
— С удовольствием! Какой фильм?
— Новый фильм Дюпонтеля. Говорят, он супер!
— Отлично, во сколько?
— В 8 вечера, перед кинотеатром. Встречаемся там?"""
        },
        "phrases": [
            {"fr": "Ça va ?", "ru": "Как дела?"},
            {"fr": "Qu'est-ce que tu fais ce week-end ?", "ru": "Что ты делаешь в эти выходные?"},
            {"fr": "Tu veux venir ?", "ru": "Хочешь пойти?"},
            {"fr": "On se retrouve où ?", "ru": "Где встречаемся?"},
            {"fr": "À quelle heure ?", "ru": "Во сколько?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 22: ЧТЕНИЕ (Глава XII, часть 1) ==========
    22: {
        "title": "Чтение: Капитанская дочка (Глава XII, часть 1/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 31,
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 23: ПОТЕРЯЛСЯ / СПРОСИТЬ ДОРОГУ ==========
    23: {
        "title": "Практика: Потерялся / спросить дорогу",
        "type": "advanced_lesson",
        "dialogue": {
            "fr": """— Excusez-moi, je suis perdu. Où se trouve la rue de Rivoli ?
— Vous allez tout droit, puis vous prenez la première rue à gauche.
— C'est loin ?
— Non, environ cinq minutes à pied.
— Merci beaucoup ! C'est à quel numéro ?
— Le numéro 50, après le carrefour.""",
            "ru": """— Извините, я потерялся. Где находится улица Риволи?
— Идите прямо, затем поверните на первую улицу налево.
— Это далеко?
— Нет, примерно пять минут пешком.
— Большое спасибо! Какой там номер?
— 50-й, после перекрёстка."""
        },
        "phrases": [
            {"fr": "Je suis perdu(e)", "ru": "Я потерялся / потерялась"},
            {"fr": "Où se trouve... ?", "ru": "Где находится...?"},
            {"fr": "C'est loin d'ici ?", "ru": "Это далеко отсюда?"},
            {"fr": "À quelle distance ?", "ru": "На каком расстоянии?"},
            {"fr": "Pouvez-vous me montrer sur la carte ?", "ru": "Можете показать на карте?"}
        ],
        "correct_answer": "готово"
    },

    # ========== ДЕНЬ 24: ЧТЕНИЕ (Глава XII, часть 2) ==========
    24: {
        "title": "Чтение: Капитанская дочка (Глава XII, часть 2/2)",
        "type": "advanced_reading",
        "reading_id": "captains_daughter",
        "chapter_part": 32,
        "correct_answer": "готово"
    }
}
# Заполним заглушками на 24 дня
for i in range(6, 25):
    ADVANCED_DAYS[i] = {"title": f"Практика: День {i}", "type": "advanced_lesson",
                        "content": "Скоро здесь появится новый полезный диалог!", "correct_answer": "готово"}


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
            # Для продвинутого курса берем из таблицы AdvancedProgress
            completed = AdvancedProgress.query.filter_by(user_id=user_id).all()
            completed_days = [p.day_id for p in completed]
        else:
            completed = Progress.query.filter_by(user_id=user_id).all()
            completed_days = [p.day_id for p in completed]

    month_days = {}
    if is_advanced:
        # === ВАЖНО: Берем данные из ADVANCED_DAYS, а не из COURSE_DAYS ===
        for key, data in ADVANCED_DAYS.items():
            month_days[key] = data
    else:
        for key, data in COURSE_DAYS.items():
            if isinstance(key, int) and 1 <= key <= 92:
                month_days[key] = data
    month_days = dict(sorted(month_days.items()))

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