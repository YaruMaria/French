# course_data.py

from reading_data import READINGS

COURSE_DAYS = {}

# ========================================================
# МЕСЯЦ 1: Дни 1-30
# ========================================================

# ---------- ДЕНЬ 1: УРОК 1 ----------
# ---------- ДЕНЬ 1: УРОК 1 (с цветным блоком транскрипции) ----------
COURSE_DAYS[1] = {
    "title": "Урок 1: Французский алфавит и базовые звуки",
    "type": "lesson",
    "has_alphabet": True,
    "sounds_table": [
        {"sound": "гласный [a]", "russian": "[а] как в словах брать, дань", "letters": "A, a<br>À, à",
         "notes": "Значок ` служит для различения слов."},
        {"sound": "согласный [p]", "russian": "[п] как в слове пар", "letters": "P, p",
         "notes": "Не путайте с русской Р!"},
        {"sound": "согласный [b]", "russian": "[б] как в слове бар", "letters": "B, b",
         "notes": "Не путайте с русской В!"},
        {"sound": "согласный [t]", "russian": "[т] как в слове таз", "letters": "T, t<br>Th, th", "notes": ""},
        {"sound": "согласный [d]", "russian": "[д] как в слове дар", "letters": "D, d", "notes": ""},
        {"sound": "согласный [f]", "russian": "[ф] как в слове факт", "letters": "F, f<br>Ph, ph", "notes": ""},
        {"sound": "согласный [v]", "russian": "[в] как в слове вал", "letters": "V, v<br>W, w", "notes": ""},
        {"sound": "согласный [m]", "russian": "[м] как в слове мак", "letters": "M, m", "notes": ""},
        {"sound": "согласный [n]", "russian": "[н] как в слове наш", "letters": "N, n", "notes": ""},
        {"sound": "согласный [r]", "russian": "[р] как в слове рот (картавый)", "letters": "R, r",
         "notes": "Можно говорить обычный русский [р], но звонко."}
    ],
    "grammar_blocks": [
        {"subtitle": "✍️ Упражнение № 3",
         "text": "Прочтите звуки по транскрипции: [n], [b], [m], [d], [a], [f], [p], [v], [t]"},
        {"subtitle": "🚫 Согласные звуки на конце слов",
         "text": "На конце слов звонкие согласные НЕ превращаются в глухие! [b] не превращается в [p], [d] в [t], [v] в [f]."},
        {"subtitle": "⏳ Удлинение гласных перед [v] и [r]",
         "text": "Если слово оканчивается на звук [v] или [r], то любой ударный гласный перед ним удлиняется."},
        {"subtitle": "📌 Буква 'e' на конце, ударение и четкость гласных",
         "text": "Буква e на конце слов не читается. Ударение ВСЕГДА падает на последний слог."},
        # НОВЫЙ ЦВЕТНОЙ БЛОК
        {
            "subtitle": "🎵 Тренировка произношения звука [a]",
            "text": """
            <div style="background: linear-gradient(135deg, #f9f4e8 0%, #f0ebe0 100%); padding: 25px; border-radius: 20px; margin: 10px 0; border-left: 5px solid #e2b6b6;">
                <p style="color: #8b5e3c; font-weight: 600; margin-bottom: 15px;">🎧 Обратите внимание на долготу гласных!</p>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin-bottom: 20px;">
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">date</span> <span style="color: #7a8a73;">[dat]</span> — дата
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">datte</span> <span style="color: #7a8a73;">[dat]</span> — финик
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">nappe</span> <span style="color: #7a8a73;">[nap]</span> — скатерть
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">natte</span> <span style="color: #7a8a73;">[nat]</span> — коса
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">patte</span> <span style="color: #7a8a73;">[pat]</span> — лапа
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">panne</span> <span style="color: #7a8a73;">[pan]</span> — авария
                    </div>
                    <div style="background: white; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <span style="color: #8fa882; font-weight: 700;">fade</span> <span style="color: #7a8a73;">[fad]</span> — пресный
                    </div>
                    <div style="background: #ffe8e8; padding: 12px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); border-left: 3px solid #e2b6b6;">
                        <span style="color: #8fa882; font-weight: 700;">bave</span> <span style="color: #d47878; font-weight: 600;">[ba:v]</span> — слюна <span style="background: #e2b6b6; padding: 2px 8px; border-radius: 20px; font-size: 0.7rem;">с удлинением!</span>
                    </div>
                </div>

                <p style="color: #8b5e3c; font-weight: 600; margin: 20px 0 15px 0;">⭐ Слова с долгим [a:] (перед [v], [r], [z]):</p>

                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">barbare</span> <span style="color: #d47878; font-weight: 600;">[barbaːr]</span> — варвар
                    </div>
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">radar</span> <span style="color: #d47878; font-weight: 600;">[radaːr]</span> — радар
                    </div>
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">mare</span> <span style="color: #d47878; font-weight: 600;">[maːr]</span> — лужа
                    </div>
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">phare</span> <span style="color: #d47878; font-weight: 600;">[faːr]</span> — фара
                    </div>
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">rare</span> <span style="color: #d47878; font-weight: 600;">[raːr]</span> — редкий
                    </div>
                    <div style="background: #e8f0e4; padding: 12px; border-radius: 12px; border-left: 3px solid #8fa882;">
                        <span style="color: #8fa882; font-weight: 700;">avare</span> <span style="color: #d47878; font-weight: 600;">[avaːr]</span> — скупой
                    </div>
                </div>

                <p style="margin-top: 20px; font-size: 0.85rem; color: #7a8a73; text-align: center; background: white; padding: 10px; border-radius: 12px;">
                    💡 <strong>Запомните правило:</strong> перед звуками <strong style="color: #d47878;">[v], [r], [z]</strong> гласный звук удлиняется!
                </p>
            </div>
            """
        }
    ],
    "vocabulary": [
        {"fr": "Bonjour", "tr": "[bɔ̃ʒuʁ]", "ru": "Здравствуйте"},
        {"fr": "Salut", "tr": "[saly]", "ru": "Привет"},
        {"fr": "Papa", "tr": "[papa]", "ru": "Папа"},
        {"fr": "Maman", "tr": "[mamɑ̃]", "ru": "Мама"},
        {"fr": "Banane", "tr": "[banan]", "ru": "Банан"},
        {"fr": "date", "tr": "[dat]", "ru": "дата"},
        {"fr": "datte", "tr": "[dat]", "ru": "финик"},
        {"fr": "nappe", "tr": "[nap]", "ru": "скатерть"},
        {"fr": "natte", "tr": "[nat]", "ru": "коса"},
        {"fr": "patte", "tr": "[pat]", "ru": "лапа"},
        {"fr": "panne", "tr": "[pan]", "ru": "авария"},
        {"fr": "fade", "tr": "[fad]", "ru": "пресный"},
        {"fr": "bave", "tr": "[ba:v]", "ru": "слюна"},
        {"fr": "barbare", "tr": "[barba:r]", "ru": "варвар"},
        {"fr": "radar", "tr": "[rada:r]", "ru": "радар"},
        {"fr": "mare", "tr": "[ma:r]", "ru": "лужа"},
        {"fr": "phare", "tr": "[fa:r]", "ru": "фара"},
        {"fr": "rare", "tr": "[ra:r]", "ru": "редкий"},
        {"fr": "avare", "tr": "[ava:r]", "ru": "скупой"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Французский алфавит", "url": "/static/audio/alphabet.mp3"},
        {"title": "Упражнение №4: Конечное оглушение", "url": "/static/audio/exercise4.mp3"},
        {"title": "Тренировка звука [a] и долгих гласных", "url": "/static/audio/lesson1_a_sound.mp3"}
    ],
    "practice_tasks": [
        {"id": 1, "type": "quiz",
         "question": "🧩 ЗАДАНИЕ 1: Превращается ли звонкий звук [v] на конце в глухой звук [ф] во французском?",
         "options": ["Да, оглушается", "Нет, звучит звонко"], "correct": "Нет, звучит звонко"},
        {"id": 2, "type": "quiz", "question": "🧩 ЗАДАНИЕ 2: Какой чистый звук дает буквосочетание 'ph'?",
         "options": ["[f]", "[t]", "[d]", "[v]"], "correct": "[f]"},
        {"id": 3, "type": "quiz", "question": "🧩 ЗАДАНИЕ 3: Куда падает ударение во французских словах?",
         "options": ["На первый слог", "На последний слог", "На предпоследний слог"], "correct": "На последний слог"},
        {"id": 4, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'date'", "correct": "[dat]"},
        {"id": 5, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'patte'", "correct": "[pat]"},
        {"id": 6, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'panne'", "correct": "[pan]"},
        {"id": 7, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'nappe'", "correct": "[nap]"},
        {"id": 8, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'rare'", "correct": "[ra:r]"},
        {"id": 9, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'phare'", "correct": "[fa:r]"},
        {"id": 10, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'avare'", "correct": "[ava:r]"},
        {"id": 11, "type": "quiz", "question": "📖 Как переводится слово 'date'?",
         "options": ["дата", "финик", "скатерть", "коса"], "correct": "дата"},
        {"id": 12, "type": "quiz", "question": "📖 Как переводится слово 'patte'?",
         "options": ["лапа", "авария", "скатерть", "лужа"], "correct": "лапа"},
        {"id": 13, "type": "quiz", "question": "📖 Как переводится слово 'mare'?",
         "options": ["море", "лужа", "река", "озеро"], "correct": "лужа"},
        {"id": 14, "type": "quiz", "question": "📖 Как переводится слово 'rare'?",
         "options": ["редкий", "частый", "дорогой", "дешевый"], "correct": "редкий"},
        {"id": 15, "type": "quiz", "question": "📖 Как переводится слово 'avare'?",
         "options": ["щедрый", "скупой", "богатый", "бедный"], "correct": "скупой"},
        {"id": 16, "type": "quiz", "question": "📖 Как переводится слово 'fade'?",
         "options": ["острый", "соленый", "пресный", "сладкий"], "correct": "пресный"},
        {"id": 17, "type": "quiz", "question": "🔊 В каком слове гласный [a] произносится с удлинением?",
         "options": ["patte", "date", "bave", "nappe"], "correct": "bave"},
        {"id": 18, "type": "quiz", "question": "🔊 Перед какими конечными звуками удлиняется гласный во французском?",
         "options": ["[p], [t], [k]", "[v], [r], [z]", "[b], [d], [g]", "[m], [n], [l]"], "correct": "[v], [r], [z]"},
        {"id": 19, "type": "text_input", "question": "🔄 Напишите по-французски 'финик'", "correct": "datte"},
        {"id": 20, "type": "text_input", "question": "🔄 Напишите по-французски 'скатерть'", "correct": "nappe"},
        {"id": 21, "type": "text_input", "question": "🔄 Напишите по-французски 'коса'", "correct": "natte"},
        {"id": 22, "type": "text_input", "question": "🔄 Напишите по-французски 'радар'", "correct": "radar"},
        {"id": 23, "type": "text_input", "question": "🔄 Напишите по-французски 'варвар'", "correct": "barbare"}
    ],
    "question": "Пройдите все 23 карточки практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 2: УРОК 2 ----------
COURSE_DAYS[2] = {
    "title": "Урок 2: Звуки [ε] и [l]: произношение и правила чтения",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "гласный [ε]",
            "russian": "[э] как в русском слове 'этот' (открытый звук)",
            "letters": "È, è<br>Ê, ê<br>Ai, ai<br>Ei, ei<br>E, e",
            "notes": "• È, è: значок ` указывает на звук [ε].<br>• Ê, ê: значок ^ указывает на [ε] (перед согласным — долгий [ε:]).<br>• Буквосочетания ai, ei читаются как один звук [ε].<br>• Буква e читается как [ε] в закрытом слоге."
        },
        {
            "sound": "согласный [l]",
            "russian": "Средний между твердым [л] и мягким [ль]",
            "letters": "L, l",
            "notes": "Поднимите кончик языка чуть выше, чем при русском [л], и прижмите его к альвеолам (бугоркам за зубами)."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "💡 Фонетическая настройка",
            "text": "Французский звук [ε] похож на гласный в словах: <b>мэр, шеф, эра, поэта</b>. Произнесите их несколько раз."
        },
        {
            "subtitle": "⚠️ Грамматическая заметка: Женский род",
            "text": "Местоимения <b>ma</b> (моя) и <b>ta</b> (твоя) употребляются перед словами женского рода. Род слов в русском и французском часто не совпадает!"
        },
        {
            "subtitle": "📝 Правила чтения",
            "text": "• Буквосочетание 'ai' → [ε]<br>• Буква 'e' в закрытом слоге → [ε]<br>• Буква 'è' и 'ê' → [ε]<br>• Артикль 'la' — служебное слово, не переводится"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Фонетическая настройка",
            "text": "Несколько раз прочитайте пары русских слов и сравните ударные звуки в каждой паре:<br><br>"
                    "<b>мэр — померь</b><br>"
                    "<b>шеф — щель</b><br>"
                    "<b>эра — верить</b><br>"
                    "<b>поэта — поели</b><br><br>"
                    "Упражнение поможет вам настроиться на правильное произношение французского [ɛ]: похожий на него русский звук — это ударный гласный в первом слове пары."
        },
        {
            "subtitle": "🎧 Упражнение № 2. Чтение слов с транскрипцией",
            "text": "Прочтите вслух слова и запишите их транскрипцию. Проверьте себя по ключу в конце урока."
        },
        {
            "subtitle": "📝 Упражнение № 4. Словарный диктант",
            "text": "Перепишите слова, произнесите их вслух и запишите перевод. Проверьте себя по словарю."
        },
        {
            "subtitle": "✍️ Упражнение № 5. Письменный перевод",
            "text": "Переведите письменно на французский язык."
        }
    ],
    "vocabulary": [
        {"fr": "là", "tr": "[la]", "ru": "там"},
        {"fr": "elle", "tr": "[εl]", "ru": "она"},
        {"fr": "belle", "tr": "[bεl]", "ru": "красивая"},
        {"fr": "bal", "tr": "[bal]", "ru": "бал"},
        {"fr": "balle", "tr": "[bal]", "ru": "пуля"},
        {"fr": "table", "tr": "[tabl]", "ru": "стол"},
        {"fr": "tel", "tr": "[tεl]", "ru": "такой"},
        {"fr": "pêle-mêle", "tr": "[pɛlmeːl]", "ru": "беспорядок"},
        {"fr": "la", "tr": "[la]", "ru": "артикль ж.р."},
        {"fr": "laine", "tr": "[lεn]", "ru": "шерсть"},
        {"fr": "mal", "tr": "[mal]", "ru": "боль; плохо"},
        {"fr": "malle", "tr": "[mal]", "ru": "чемодан"},
        {"fr": "malade", "tr": "[malad]", "ru": "больной"},
        {"fr": "lettre", "tr": "[lεtr]", "ru": "письмо"},
        {"fr": "lèvre", "tr": "[lεvr]", "ru": "губа"},
        {"fr": "natal", "tr": "[natal]", "ru": "родной"},
        {"fr": "naval", "tr": "[naval]", "ru": "морской"},
        {"fr": "mère", "tr": "[mεr]", "ru": "мать"},
        {"fr": "père", "tr": "[pεr]", "ru": "отец"},
        {"fr": "frère", "tr": "[frεr]", "ru": "брат"},
        {"fr": "tête", "tr": "[tεt]", "ru": "голова"},
        {"fr": "mer", "tr": "[mεr]", "ru": "море"},
        {"fr": "est", "tr": "[ɛ]", "ru": "есть, находится"},
        {"fr": "fer", "tr": "[fɛr]", "ru": "железо"},
        {"fr": "terre", "tr": "[tɛr]", "ru": "земля"},
        {"fr": "verre", "tr": "[vɛr]", "ru": "стекло, стакан"},
        {"fr": "fête", "tr": "[fɛt]", "ru": "праздник"},
        {"fr": "prête", "tr": "[prɛt]", "ru": "готовая"},
        {"fr": "bête", "tr": "[bɛt]", "ru": "животное"},
        {"fr": "rêve", "tr": "[rɛv]", "ru": "мечта"},
        {"fr": "être", "tr": "[ɛtr]", "ru": "быть"},
        {"fr": "ma", "tr": "[ma]", "ru": "моя"},
        {"fr": "mai", "tr": "[mɛ]", "ru": "май"},
        {"fr": "air", "tr": "[ɛr]", "ru": "воздух"},
        {"fr": "faire", "tr": "[fɛr]", "ru": "делать"},
        {"fr": "affaire", "tr": "[afɛr]", "ru": "дело"},
        {"fr": "ta", "tr": "[ta]", "ru": "твоя"}
    ],
    "audio_tracks": [
        {"title": "Упражнение № 2: Слова для транскрипции", "url": "/static/audio/lesson2_ex2.mp3"},
        {"title": "Упражнение № 3: Звук [l]", "url": "/static/audio/lesson2_ex3.mp3"}
    ],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "🔊 Какой звук дает буквосочетание 'ai' во французском?",
         "options": ["[a]", "[e]", "[ε]", "[o]"], "correct": "[ε]"},
        {"id": 2, "type": "quiz", "question": "🔊 Какой звук дает буква 'è'?",
         "options": ["[e]", "[ε]", "[ə]", "[a]"], "correct": "[ε]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как правильно произносится французский звук [l]?",
         "options": ["Как русский твердый [л]", "Как русский мягкий [ль]", "Средний между твердым и мягким, кончик языка у альвеол", "Как английский [l]"],
         "correct": "Средний между твердым и мягким, кончик языка у альвеол"},
        {"id": 4, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'est'", "correct": "[ɛ]"},
        {"id": 5, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'fer'", "correct": "[fɛr]"},
        {"id": 6, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'mer'", "correct": "[mɛr]"},
        {"id": 7, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'terre'", "correct": "[tɛr]"},
        {"id": 8, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'verre'", "correct": "[vɛr]"},
        {"id": 9, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'mère'", "correct": "[mɛr]"},
        {"id": 10, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'père'", "correct": "[pɛr]"},
        {"id": 11, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'frère'", "correct": "[frɛr]"},
        {"id": 12, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'tête'", "correct": "[tɛt]"},
        {"id": 13, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'rêve'", "correct": "[rɛv]"},
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски слово 'письмо'", "correct": "lettre"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски слово 'голова'", "correct": "tête"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски слово 'больной'", "correct": "malade"},
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски слово 'есть, находится'", "correct": "est"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски слово 'май'", "correct": "mai"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски слово 'красивая'", "correct": "belle"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски слово 'стол'", "correct": "table"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски слово 'она'", "correct": "elle"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски слово 'быть'", "correct": "être"},
        {"id": 23, "type": "quiz", "question": "📖 Как переводится слово 'belle'?", "options": ["Красивый/красивая", "Бал", "Пуля", "Она"], "correct": "Красивый/красивая"},
        {"id": 24, "type": "quiz", "question": "📖 Как переводится слово 'table'?", "options": ["Стул", "Стол", "Кровать", "Шкаф"], "correct": "Стол"},
        {"id": 25, "type": "quiz", "question": "📖 Как переводится слово 'lettre'?", "options": ["Книга", "Письмо", "Газета", "Журнал"], "correct": "Письмо"},
        {"id": 26, "type": "quiz", "question": "📖 Как переводится слово 'tête'?", "options": ["Праздник", "Голова", "Животное", "Земля"], "correct": "Голова"},
        {"id": 27, "type": "quiz", "question": "📖 Как переводится слово 'mère'?", "options": ["Отец", "Брат", "Мать", "Сестра"], "correct": "Мать"},
        {"id": 28, "type": "quiz", "question": "📖 Как переводится слово 'frère'?", "options": ["Сестра", "Брат", "Друг", "Сын"], "correct": "Брат"},
        {"id": 29, "type": "quiz", "question": "📖 Как переводится слово 'mer'?", "options": ["Земля", "Небо", "Море", "Река"], "correct": "Море"},
        {"id": 30, "type": "quiz", "question": "🔄 Как будет по-французски 'она'?", "options": ["il", "elle", "on", "ce"], "correct": "elle"},
        {"id": 31, "type": "quiz", "question": "🔄 Как будет по-французски 'там'?", "options": ["ici", "là", "où", "quoi"], "correct": "là"},
        {"id": 32, "type": "quiz", "question": "🔄 Как будет по-французски 'мать'?", "options": ["père", "frère", "mère", "soeur"], "correct": "mère"},
        {"id": 33, "type": "quiz", "question": "🔄 Как будет по-французски 'отец'?", "options": ["mère", "frère", "père", "soeur"], "correct": "père"},
        {"id": 34, "type": "quiz", "question": "🔄 Как будет по-французски 'брат'?", "options": ["soeur", "père", "mère", "frère"], "correct": "frère"},
        {"id": 35, "type": "quiz", "question": "🔄 Как будет по-французски 'праздник'?", "options": ["tête", "fête", "bête", "rêve"], "correct": "fête"},
        {"id": 36, "type": "quiz", "question": "🔄 Как будет по-французски 'мечта'?", "options": ["rêve", "fête", "bête", "tête"], "correct": "rêve"},
        {"id": 37, "type": "quiz", "question": "📚 Какой артикль используется перед существительными женского рода в единственном числе?", "options": ["le", "la", "les", "un"], "correct": "la"},
        {"id": 38, "type": "quiz", "question": "📚 Какой род у французского слова 'table' (стол)?", "options": ["Мужской", "Женский", "Средний", "Не определяется"], "correct": "Женский"},
        {"id": 39, "type": "text_input", "question": "✍️ Переведите на французский: 'Моя мать красивая.'", "correct": "Ma mère est belle"},
        {"id": 40, "type": "text_input", "question": "✍️ Переведите на французский: 'Это письмо.'", "correct": "C'est une lettre"},
        {"id": 41, "type": "text_input", "question": "✍️ Переведите на французский: 'Она больна.'", "correct": "Elle est malade"}
    ],
    "question": "Пройдите все 41 карточку практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 3: ЧТЕНИЕ (Глава I, Часть 1) ----------
COURSE_DAYS[3] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 1,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 4: ТЕСТ 1 (Уроки 1-2) ----------
# ---------- ДЕНЬ 4: ТЕСТ 1 (Уроки 1-2) ----------
COURSE_DAYS[4] = {
    "title": "Тест 1: Уроки 1-2",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        # ========== ЧАСТЬ 1: ДИКТАНТ ПО СЛОВАМ (текстовый ввод) ==========
        {"id": 1, "type": "text_input", "question": "📝 Напишите по-французски: 'Здравствуйте'", "correct": "bonjour"},
        {"id": 2, "type": "text_input", "question": "📝 Напишите по-французски: 'Привет'", "correct": "salut"},
        {"id": 3, "type": "text_input", "question": "📝 Напишите по-французски: 'Папа'", "correct": "papa"},
        {"id": 4, "type": "text_input", "question": "📝 Напишите по-французски: 'Мама'", "correct": "maman"},
        {"id": 5, "type": "text_input", "question": "📝 Напишите по-французски: 'Банан'", "correct": "banane"},
        {"id": 6, "type": "text_input", "question": "📝 Напишите по-французски: 'она'", "correct": "elle"},
        {"id": 7, "type": "text_input", "question": "📝 Напишите по-французски: 'там'", "correct": "là"},
        {"id": 8, "type": "text_input", "question": "📝 Напишите по-французски: 'красивая'", "correct": "belle"},
        {"id": 9, "type": "text_input", "question": "📝 Напишите по-французски: 'стол'", "correct": "table"},
        {"id": 10, "type": "text_input", "question": "📝 Напишите по-французски: 'письмо'", "correct": "lettre"},
        {"id": 11, "type": "text_input", "question": "📝 Напишите по-французски: 'голова'", "correct": "tête"},
        {"id": 12, "type": "text_input", "question": "📝 Напишите по-французски: 'мать'", "correct": "mère"},
        {"id": 13, "type": "text_input", "question": "📝 Напишите по-французски: 'отец'", "correct": "père"},
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски: 'брат'", "correct": "frère"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски: 'море'", "correct": "mer"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски: 'больной'", "correct": "malade"},
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски: 'чемодан'", "correct": "malle"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски: 'шерсть'", "correct": "laine"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски: 'дата'", "correct": "date"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски: 'финик'", "correct": "datte"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски: 'скатерть'", "correct": "nappe"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски: 'лапа'", "correct": "patte"},
        {"id": 23, "type": "text_input", "question": "📝 Напишите по-французски: 'авария'", "correct": "panne"},
        {"id": 24, "type": "text_input", "question": "📝 Напишите по-французски: 'пресный'", "correct": "fade"},
        {"id": 25, "type": "text_input", "question": "📝 Напишите по-французски: 'редкий'", "correct": "rare"},
        {"id": 26, "type": "text_input", "question": "📝 Напишите по-французски: 'скупой'", "correct": "avare"},

        # ========== ЧАСТЬ 2: ФОНЕТИКА ==========
        {"id": 27, "type": "quiz", "question": "🔊 Какой звук дает буквосочетание 'ph' во французском?",
         "options": ["[p]", "[f]", "[ph]", "[v]"], "correct": "[f]"},
        {"id": 28, "type": "quiz", "question": "🔊 Куда падает ударение во французских словах?",
         "options": ["На первый слог", "На последний слог", "На предпоследний слог", "На третий слог"],
         "correct": "На последний слог"},
        {"id": 29, "type": "quiz", "question": "🔊 Как читается буква 'è'?",
         "options": ["[e]", "[ε]", "[ə]", "[a]"], "correct": "[ε]"},
        {"id": 30, "type": "quiz", "question": "🔊 Какой звук дает буквосочетание 'ai'?",
         "options": ["[a]", "[e]", "[ε]", "[o]"], "correct": "[ε]"},
        {"id": 31, "type": "quiz", "question": "🔊 Превращается ли звонкий звук [b] на конце слова в глухой [p]?",
         "options": ["Да", "Нет", "Только в глаголах", "Только в существительных"], "correct": "Нет"},
        {"id": 32, "type": "quiz", "question": "🔊 Как правильно произносится французский звук [l]?",
         "options": ["Твердо, как в русском", "Мягко, как в русском", "Средний между твердым и мягким",
                     "Как английский"],
         "correct": "Средний между твердым и мягким"},
        {"id": 33, "type": "quiz", "question": "🔊 В каком слове гласный [a] произносится с удлинением?",
         "options": ["patte", "date", "bave", "nappe"], "correct": "bave"},
        {"id": 34, "type": "quiz", "question": "🔊 Перед какими конечными звуками удлиняется гласный во французском?",
         "options": ["[p], [t], [k]", "[v], [r], [z]", "[b], [d], [g]", "[m], [n], [l]"],
         "correct": "[v], [r], [z]"},
        {"id": 35, "type": "quiz", "question": "🔊 Как читается буква 'e' на конце французских слов?",
         "options": ["[e]", "[ɛ]", "[ə]", "Не читается"], "correct": "Не читается"},

        # ========== ЧАСТЬ 3: ГРАММАТИКА ==========
        {"id": 36, "type": "quiz",
         "question": "📚 Какой артикль используется перед существительными женского рода в единственном числе?",
         "options": ["le", "la", "les", "un"], "correct": "la"},
        {"id": 37, "type": "quiz", "question": "📚 Какое местоимение переводится как 'она'?",
         "options": ["il", "elle", "on", "ce"], "correct": "elle"},
        {"id": 38, "type": "quiz", "question": "📚 Какой род у французского слова 'table' (стол)?",
         "options": ["Мужской", "Женский", "Средний"], "correct": "Женский"},
        {"id": 39, "type": "quiz", "question": "📚 Как переводится артикль 'la'?",
         "options": ["Неопределенный артикль ж.р.", "Определенный артикль ж.р.", "Неопределенный артикль м.р.",
                     "Определенный артикль м.р."],
         "correct": "Определенный артикль ж.р."},

        # ========== ЧАСТЬ 4: ПЕРЕВОД С РУССКОГО (выбор ответа) ==========
        {"id": 40, "type": "quiz", "question": "🔄 Как переводится 'Bonjour'?",
         "options": ["До свидания", "Спасибо", "Здравствуйте", "Пожалуйста"], "correct": "Здравствуйте"},
        {"id": 41, "type": "quiz", "question": "🔄 Как переводится 'Salut'?",
         "options": ["Добрый вечер", "Привет", "Доброе утро", "Спокойной ночи"], "correct": "Привет"},
        {"id": 42, "type": "quiz", "question": "🔄 Как переводится 'mère'?",
         "options": ["отец", "брат", "мать", "сестра"], "correct": "мать"},
        {"id": 43, "type": "quiz", "question": "🔄 Как переводится 'père'?",
         "options": ["мать", "брат", "отец", "сестра"], "correct": "отец"},
        {"id": 44, "type": "quiz", "question": "🔄 Как переводится 'frère'?",
         "options": ["сестра", "брат", "друг", "сын"], "correct": "брат"},
        {"id": 45, "type": "quiz", "question": "🔄 Как переводится 'mer'?",
         "options": ["земля", "небо", "море", "река"], "correct": "море"},
        {"id": 46, "type": "quiz", "question": "🔄 Как переводится 'tête'?",
         "options": ["праздник", "голова", "животное", "стена"], "correct": "голова"},
        {"id": 47, "type": "quiz", "question": "🔄 Как переводится 'belle'?",
         "options": ["красивый/красивая", "большой", "маленький", "старый"], "correct": "красивый/красивая"},
        {"id": 48, "type": "quiz", "question": "🔄 Как переводится 'là'?",
         "options": ["здесь", "там", "где", "туда"], "correct": "там"},

        # ========== ЧАСТЬ 5: ТРАНСКРИПЦИЯ (проверка знаний) ==========
        {"id": 49, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'est'", "correct": "[ɛ]"},
        {"id": 50, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'fer'", "correct": "[fɛr]"},
        {"id": 51, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'rare'", "correct": "[ra:r]"},
        {"id": 52, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'phare'", "correct": "[fa:r]"}
    ],
    "question": "Пройдите все 52 вопроса теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 5: УРОК 3 ----------
COURSE_DAYS[5] = {
    "title": "Урок 3: Звуки [s] и [z]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 5: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 6: УРОК 4 ----------
COURSE_DAYS[6] = {
    "title": "Урок 4: Звук [e] и несмягчение согласных",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 6: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 7: ЧТЕНИЕ (Глава I, Часть 2) ----------
COURSE_DAYS[7] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 2,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 8: ТЕСТ 2 (Уроки 3-4) ----------
COURSE_DAYS[8] = {
    "title": "Тест 2: Уроки 3-4",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 8: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 9: УРОК 5 ----------
COURSE_DAYS[9] = {
    "title": "Урок 5: Звуки [i], [j], немая h",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 9: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 10: УРОК 6 ----------
COURSE_DAYS[10] = {
    "title": "Урок 6: Звуки [k], [g], [ɔ]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 10: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 11: ЧТЕНИЕ (Глава I, Часть 3) ----------
COURSE_DAYS[11] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 3,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 12: ТЕСТ 3 (Уроки 5-6) ----------
COURSE_DAYS[12] = {
    "title": "Тест 3: Уроки 5-6",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 12: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 13: УРОК 7 ----------
COURSE_DAYS[13] = {
    "title": "Урок 7: Звуки [œ], [ə] и беглое e",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 13: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 14: УРОК 8 ----------
COURSE_DAYS[14] = {
    "title": "Урок 8: Звуки [ʃ], [ʒ] и долгий [a:]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 14: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 15: ЧТЕНИЕ (Глава I, Часть 4) ----------
COURSE_DAYS[15] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 4,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 16: ТЕСТ 4 (Уроки 7-8) ----------
COURSE_DAYS[16] = {
    "title": "Тест 4: Уроки 7-8",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 16: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 17: УРОК 9 ----------
COURSE_DAYS[17] = {
    "title": "Урок 9: Звуки [ø], [y], [u] и полугласный [ɥ]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 17: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 18: УРОК 10 ----------
COURSE_DAYS[18] = {
    "title": "Урок 10: Носовые гласные [ɛ̃] и [œ̃]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 18: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 19: ЧТЕНИЕ (Глава II, Часть 5) ----------
COURSE_DAYS[19] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 5,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 20: ТЕСТ 5 (Уроки 9-10) ----------
COURSE_DAYS[20] = {
    "title": "Тест 5: Уроки 9-10",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 20: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 21: УРОК 11 ----------
COURSE_DAYS[21] = {
    "title": "Урок 11: Звуки [o], [ɔ], [u], [w] и носовой [ɔ̃]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 21: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 22: УРОК 12 ----------
COURSE_DAYS[22] = {
    "title": "Урок 12: Носовой [ɑ̃], согласный [ɲ] и алфавит",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 22: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 23: ЧТЕНИЕ (Глава II, Часть 6) ----------
COURSE_DAYS[23] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 6,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 24: ТЕСТ 6 (Уроки 11-12) ----------
COURSE_DAYS[24] = {
    "title": "Тест 6: Уроки 11-12",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 24: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 25: УРОК 13 ----------
COURSE_DAYS[25] = {
    "title": "Урок 13: Оборот c'est, приветствия и обращения",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 25: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 26: УРОК 14 ----------
COURSE_DAYS[26] = {
    "title": "Урок 14: Порядок слов, местоимения il, elle, ça и предлог à",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 26: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 27: ЧТЕНИЕ (Глава II, Часть 7) ----------
COURSE_DAYS[27] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 7,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 28: ТЕСТ 7 (Уроки 13-14) ----------
COURSE_DAYS[28] = {
    "title": "Тест 7: Уроки 13-14",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос теста 28: Введите 'готово' чтобы завершить тест",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите все вопросы теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 29: УРОК 15 ----------
COURSE_DAYS[29] = {
    "title": "Урок 15: Настоящее время глаголов I группы и глагол être",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [],
    "grammar_blocks": [],
    "vocabulary": [],
    "audio_tracks": [],
    "practice_tasks": [
        {"id": 1, "type": "quiz", "question": "Вопрос дня 29: Введите 'готово' чтобы завершить урок",
         "options": ["готово"], "correct": "готово"}
    ],
    "question": "Пройдите карточки",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 30: ЧТЕНИЕ (Глава II, Часть 8) ----------
COURSE_DAYS[30] = {
    "title": "Чтение: Капитанская дочка",
    "type": "reading",
    "reading_id": "captains_daughter",
    "chapter_part": 8,
    "question": "Пройдите все вопросы по тексту!",
    "correct_answer": "готово"
}

# ========================================================
# МЕСЯЦ 2: Дни 31-61 (заглушки)
# ========================================================

for day_num in range(31, 62):
    if day_num not in COURSE_DAYS:
        COURSE_DAYS[day_num] = {
            "title": f"День {day_num}",
            "type": "lesson",
            "has_alphabet": False,
            "sounds_table": [],
            "grammar_blocks": [],
            "vocabulary": [],
            "audio_tracks": [],
            "practice_tasks": [
                {"id": 1, "type": "quiz", "question": f"Вопрос дня {day_num}: Введите 'готово' чтобы завершить урок",
                 "options": ["готово"], "correct": "готово"}
            ],
            "question": "Пройдите карточки",
            "correct_answer": "готово"
        }

# ========================================================
# МЕСЯЦ 3: Дни 62-92 (заглушки)
# ========================================================

for day_num in range(62, 93):
    if day_num not in COURSE_DAYS:
        COURSE_DAYS[day_num] = {
            "title": f"День {day_num}",
            "type": "lesson",
            "has_alphabet": False,
            "sounds_table": [],
            "grammar_blocks": [],
            "vocabulary": [],
            "audio_tracks": [],
            "practice_tasks": [
                {"id": 1, "type": "quiz", "question": f"Вопрос дня {day_num}: Введите 'готово' чтобы завершить урок",
                 "options": ["готово"], "correct": "готово"}
            ],
            "question": "Пройдите карточки",
            "correct_answer": "готово"
        }