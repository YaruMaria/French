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
# ---------- ДЕНЬ 5: УРОК 3 (Звуки [s] и [z]) ----------
COURSE_DAYS[5] = {
    "title": "Урок 3: Звуки [s] и [z]: произношение и правила чтения",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "согласный [s]",
            "russian": "[с] как в слове сон",
            "letters": "S, s<br>ss<br>C, c<br>Ç, ç",
            "notes": "• Буква s читается как [s] в начале слова и перед согласной.<br>• Удвоенное ss всегда дает [s].<br>• Буква с читается как [s] перед e, i, y.<br>• Значок ç (cédille) указывает, что буква читается как [s] перед a, o."
        },
        {
            "sound": "согласный [z]",
            "russian": "[з] как в слове золото",
            "letters": "S, s<br>Z, z",
            "notes": "• Буква s читается как [z] между двумя гласными.<br>• Буква z всегда дает звук [z]."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "⏳ Удлинение гласных перед звуками [v], [r], [z]",
            "text": "Если слово оканчивается на звук <b>[z]</b>, то любой ударный гласный перед ним, как правило, <b>удлиняется</b>, например: <b>phase [fa:z]</b> — фаза.<br><br>Это правило также работает для звуков <b>[v]</b> и <b>[r]</b>."
        },
        {
            "subtitle": "📝 Важные правила чтения (Запомните!)",
            "text": "• <b>S</b> в начале слова → [s]<br>• <b>S</b> между гласными → [z]<br>• <b>SS</b> (удвоенное) → [s]<br>• <b>C</b> перед e, i, y → [s]<br>• <b>Ç</b> перед a, o → [s]<br>• <b>Z</b> всегда → [z]"
        },
        {
            "subtitle": "💡 Озвончение S между гласными",
            "text": "Когда буква <b>S</b> стоит между двумя гласными, она превращается в звонкий звук <b>[z]</b>.<br><br>Примеры: <b>rose [roːz]</b> — роза, <b>case [kaːz]</b> — ящик.<br>Это важное правило французской фонетики!"
        }
    ],
    "vocabulary": [
        {"fr": "phrase", "tr": "[fra:z]", "ru": "фраза"},
        {"fr": "vase", "tr": "[va:z]", "ru": "ваза"},
        {"fr": "sa", "tr": "[sa]", "ru": "его, её (перед жен. родом)"},
        {"fr": "sale", "tr": "[sal]", "ru": "грязный, -ая, -ое"},
        {"fr": "salle", "tr": "[sal]", "ru": "зал, комната"},
        {"fr": "salade", "tr": "[salad]", "ru": "салат"},
        {"fr": "salaire", "tr": "[sale:r]", "ru": "зарплата"},
        {"fr": "sel", "tr": "[sel]", "ru": "соль"},
        {"fr": "cette", "tr": "[set]", "ru": "эта (жен. род)"},
        {"fr": "veste", "tr": "[vest]", "ru": "куртка"},
        {"fr": "stade", "tr": "[stad]", "ru": "стадион"},
        {"fr": "adresse", "tr": "[adres]", "ru": "адрес"},
        {"fr": "trace", "tr": "[tras]", "ru": "след"},
        {"fr": "place", "tr": "[plas]", "ru": "место"},
        # Дополнительные слова из упражнения №3
        {"fr": "pèse", "tr": "[pɛːz]", "ru": "взвешивает"},
        {"fr": "slave", "tr": "[slaːv]", "ru": "славянин"},
        {"fr": "mer", "tr": "[mɛːr]", "ru": "море"},
        {"fr": "frère", "tr": "[frɛːr]", "ru": "брат"},
        {"fr": "rêve", "tr": "[rɛːv]", "ru": "мечта"},
        {"fr": "avare", "tr": "[avaːr]", "ru": "скупой"},
        {"fr": "thèse", "tr": "[tɛːz]", "ru": "тезис, диссертация"},
        {"fr": "affaire", "tr": "[afɛːr]", "ru": "дело"},
        {"fr": "base", "tr": "[baːz]", "ru": "основа, база"},
        {"fr": "serre", "tr": "[sɛːr]", "ru": "теплица"},
        {"fr": "brave", "tr": "[braːv]", "ru": "храбрый"},
        {"fr": "faire", "tr": "[fɛːr]", "ru": "делать"},
        {"fr": "verre", "tr": "[vɛːr]", "ru": "стекло, стакан"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Чтение слогов (sa, ça, ass, lai...)", "url": "/static/audio/lesson3_1.mp3"},
        {"title": "Упражнение №3: Слова с удлинением гласных", "url": "/static/audio/lesson3_2.mp3"},
        {"title": "Упражнение №4: Слова для запоминания", "url": "/static/audio/lesson3_3.mp3"}
    ],
    "practice_tasks": [
        # ========== ТЕОРЕТИЧЕСКИЕ ВОПРОСЫ (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается буква 'S' в начале слова (например, 'sa', 'salut')?",
         "options": ["[z]", "[s]", "[ʃ]", "[ʒ]"], "correct": "[s]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как читается буква 'C' перед гласными 'e', 'i', 'y'?",
         "options": ["[k]", "[s]", "[g]", "[ʃ]"], "correct": "[s]"},
        {"id": 3, "type": "quiz", "question": "🔊 Что означает значок 'ç' (cédille) под буквой C?",
         "options": ["Буква не читается", "Читается как [k]", "Читается как [s] перед a, o", "Читается как [z]"],
         "correct": "Читается как [s] перед a, o"},
        {"id": 4, "type": "quiz", "question": "🔊 Удвоенное 'ss' во французском дает звук...",
         "options": ["[z]", "[s]", "[ʃ]", "[ʒ]"], "correct": "[s]"},
        {"id": 5, "type": "quiz", "question": "🔊 Когда буква 'S' читается как звонкий звук [z]?",
         "options": ["В начале слова", "Между двумя гласными", "Перед согласной", "На конце слова"],
         "correct": "Между двумя гласными"},
        {"id": 6, "type": "quiz", "question": "🔊 Буква 'Z' во французском всегда читается как...",
         "options": ["[s]", "[z]", "[dz]", "[ʒ]"], "correct": "[z]"},
        {"id": 7, "type": "quiz", "question": "🔊 Какой звук слышится в слове 'rose' (роза) между гласными O и E?",
         "options": ["[s]", "[z]", "[ʒ]", "[ʃ]"], "correct": "[z]"},
        {"id": 8, "type": "quiz", "question": "⏳ Перед какими конечными звуками удлиняется ударный гласный?",
         "options": ["[p], [t], [k]", "[v], [r], [z]", "[b], [d], [g]", "[m], [n], [l]"],
         "correct": "[v], [r], [z]"},
        {"id": 9, "type": "quiz", "question": "⏳ В слове 'phase' [fa:z] ударный гласный произносится...",
         "options": ["Коротко", "С удлинением", "С придыханием", "Носовым"], "correct": "С удлинением"},

        # ========== ПЕРЕВОД ФРАЗ С ФРАНЦУЗСКОГО (text_input) ==========
        {"id": 10, "type": "text_input", "question": "📖 Переведите на русский язык: 'sa mère'", "correct": "его мать"},
        {"id": 11, "type": "text_input", "question": "📖 Переведите на русский язык: 'ma place'",
         "correct": "моё место"},
        {"id": 12, "type": "text_input", "question": "📖 Переведите на русский язык: 'cette phrase'",
         "correct": "эта фраза"},
        {"id": 13, "type": "text_input", "question": "📖 Переведите на русский язык: 'la salle est sale'",
         "correct": "зал грязный"},
        {"id": 14, "type": "text_input", "question": "📖 Переведите на русский язык: 'Nana est belle'",
         "correct": "Нана красивая"},
        {"id": 15, "type": "text_input", "question": "📖 Переведите на русский язык: 'elle est prête'",
         "correct": "она готова"},
        {"id": 16, "type": "text_input", "question": "📖 Переведите на русский язык: 'elle est malade'",
         "correct": "она больна"},

        # ========== ПЕРЕВОД С РУССКОГО НА ФРАНЦУЗСКИЙ (text_input) ==========
        {"id": 17, "type": "text_input", "question": "🔄 Переведите на французский: 'Она готова.'",
         "correct": "elle est prête"},
        {"id": 18, "type": "text_input", "question": "🔄 Переведите на французский: 'Нана больна.'",
         "correct": "nana est malade"},
        {"id": 19, "type": "text_input", "question": "🔄 Переведите на французский: 'Его мать красива.'",
         "correct": "sa mère est belle"},
        {"id": 20, "type": "text_input", "question": "🔄 Переведите на французский: 'Эта куртка грязная.'",
         "correct": "cette veste est sale"},

        # ========== ПЕРЕВОД ОТДЕЛЬНЫХ СЛОВ (quiz) ==========
        {"id": 21, "type": "quiz", "question": "📖 Как переводится слово 'phrase'?",
         "options": ["фраза", "ваза", "место", "адрес"], "correct": "фраза"},
        {"id": 22, "type": "quiz", "question": "📖 Как переводится слово 'vase'?",
         "options": ["ваза", "фраза", "салат", "зал"], "correct": "ваза"},
        {"id": 23, "type": "quiz", "question": "📖 Как переводится слово 'salle'?",
         "options": ["соль", "зал", "грязный", "куртка"], "correct": "зал"},
        {"id": 24, "type": "quiz", "question": "📖 Как переводится слово 'sale'?",
         "options": ["зал", "соль", "грязный", "салат"], "correct": "грязный"},
        {"id": 25, "type": "quiz", "question": "📖 Как переводится слово 'veste'?",
         "options": ["стадион", "адрес", "куртка", "след"], "correct": "куртка"},
        {"id": 26, "type": "quiz", "question": "📖 Как переводится слово 'place'?",
         "options": ["место", "след", "адрес", "стадион"], "correct": "место"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 27, "type": "text_input", "question": "🔄 Напишите по-французски 'фраза'", "correct": "phrase"},
        {"id": 28, "type": "text_input", "question": "🔄 Напишите по-французски 'ваза'", "correct": "vase"},
        {"id": 29, "type": "text_input", "question": "🔄 Напишите по-французски 'зал'", "correct": "salle"},
        {"id": 30, "type": "text_input", "question": "🔄 Напишите по-французски 'грязный'", "correct": "sale"},
        {"id": 31, "type": "text_input", "question": "🔄 Напишите по-французски 'куртка'", "correct": "veste"},
        {"id": 32, "type": "text_input", "question": "🔄 Напишите по-французски 'адрес'", "correct": "adresse"},
        {"id": 33, "type": "text_input", "question": "🔄 Напишите по-французски 'след'", "correct": "trace"},
        {"id": 34, "type": "text_input", "question": "🔄 Напишите по-французски 'место'", "correct": "place"},
        {"id": 35, "type": "text_input", "question": "🔄 Напишите по-французски 'стадион'", "correct": "stade"}
    ],
    "question": "Пройдите все 35 карточек практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 6: УРОК 4 ----------
# ---------- ДЕНЬ 6: УРОК 4 (Звук [e] и несмягчение согласных) ----------
COURSE_DAYS[6] = {
    "title": "Урок 4: Звук [e] и несмягчение согласных",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "гласный [e]",
            "russian": "[e] как в слове щель (но без смягчения согласного!)",
            "letters": "E, e<br>É, é<br>er (на конце глаголов)<br>ez (на конце слов)<br>es (в mes, tes, ses, ces, les, des)",
            "notes": "• Значок ´ (accent aigu) указывает, что e читается как [e].<br>• Окончание -er в глаголах читается [e] (r не читается).<br>• Окончание -ez читается [e] (z не читается).<br>• Слова mes [me], tes [te], ses [se], ces [se], les [le], des [de].<br>• Союз et [e] — и."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "🔊 Несмягчение французских согласных",
            "text": "<b>Французские согласные НЕ смягчаются ни перед [e], ни перед любым другим гласным!</b><br><br>"
                    "Например, если вам нужно выговорить звукосочетание [se], представьте, что вы собрались произнести русское слово <b>сэр</b>, а потом передумали и произнесли слово <b>серенький</b> — звук [c] должен остаться твердым перед [e]."
        },
        {
            "subtitle": "⚠️ Важно: разница между [e] и [ε]",
            "text": "Подмена одного звука другим может привести к непониманию вашей речи!<br><br>"
                    "Пример: <b>Allez!</b> [ale] — Идите! ≠ <b>allais</b> [alɛ] — я шел<br><br>"
                    "Упражнение №2 помогает уловить разницу между [e] и [ε]."
        },
        {
            "subtitle": "📚 Французские глаголы: окончание -er",
            "text": "В буквосочетании <b>er</b> на конце глаголов буква <b>r не читается</b>.<br><br>"
                    "Примеры: parler [parle] — говорить, aimer [eme] — любить, aider [ede] — помогать."
        },
        {
            "subtitle": "📚 Буквосочетание -ez: повелительное наклонение",
            "text": "В буквосочетании <b>ez</b> на конце слов буква <b>z не читается</b>.<br><br>"
                    "На конце глаголов -ez указывает на приказ, просьбу или совет, адресованный нескольким людям или одному человеку на «Вы».<br><br>"
                    "Пример: <b>Fermez!</b> [ferme] — Закройте!"
        },
        {
            "subtitle": "📚 Множественное число: окончание -es",
            "text": "Буквосочетание <b>es</b> на конце существительных <b>не читается</b>.<br><br>"
                    "Оно указывает, что существительное стоит во множественном числе.<br>"
                    "Сравните: affaire [afɛr] — дело → affaires [afɛr] — дела."
        },
        {
            "subtitle": "🔗 Связывание (liaison): произношение s как [z]",
            "text": "Буква <b>s</b> становится произносимой и читается как <b>[z]</b> в словах <b>mes, tes, ses, ces, les, des</b>,<br>"
                    "если они выступают перед словами, начинающимися на гласный звук.<br><br>"
                    "Пример: mes frères [me frɛr] — мои братья<br>"
                    "но mes adresses [me za drɛs] — мои адреса"
        }
    ],
    "vocabulary": [
        # Глаголы с окончанием -er
        {"fr": "parler", "tr": "[parle]", "ru": "говорить"},
        {"fr": "aimer", "tr": "[eme]", "ru": "любить"},
        {"fr": "aider", "tr": "[ede]", "ru": "помогать"},
        {"fr": "aller", "tr": "[ale]", "ru": "идти; ехать"},
        {"fr": "traverser", "tr": "[traverse]", "ru": "переходить, пересекать"},
        {"fr": "frapper", "tr": "[frape]", "ru": "ударять"},
        {"fr": "fermer", "tr": "[ferme]", "ru": "закрывать"},
        {"fr": "cesser", "tr": "[sese]", "ru": "прекращать"},
        {"fr": "laisser", "tr": "[lese]", "ru": "оставлять"},
        {"fr": "baisser", "tr": "[bese]", "ru": "опускать"},
        {"fr": "passer", "tr": "[pase]", "ru": "проходить"},
        {"fr": "répéter", "tr": "[repete]", "ru": "повторять"},
        {"fr": "rester", "tr": "[reste]", "ru": "оставаться"},
        {"fr": "espérer", "tr": "[espere]", "ru": "надеяться"},
        {"fr": "adresser", "tr": "[adrese]", "ru": "адресовать"},

        # Формы повелительного наклонения
        {"fr": "parlez!", "tr": "[parle]", "ru": "говорите!"},
        {"fr": "fermez!", "tr": "[ferme]", "ru": "закройте!"},
        {"fr": "allez!", "tr": "[ale]", "ru": "идите!"},
        {"fr": "aidez!", "tr": "[ede]", "ru": "помогите!"},
        {"fr": "passez!", "tr": "[pase]", "ru": "проходите!"},
        {"fr": "restez!", "tr": "[reste]", "ru": "останьтесь!"},
        {"fr": "répétez!", "tr": "[repete]", "ru": "повторите!"},
        {"fr": "cessez!", "tr": "[sese]", "ru": "прекратите!"},
        {"fr": "traversez!", "tr": "[traverse]", "ru": "переходите!"},
        {"fr": "baissez!", "tr": "[bese]", "ru": "опустите!"},
        {"fr": "laissez!", "tr": "[lese]", "ru": "оставьте!"},
        {"fr": "espérez!", "tr": "[espere]", "ru": "надейтесь!"},
        {"fr": "adressez!", "tr": "[adrese]", "ru": "адресуйте!"},

        # Слова для множественного числа
        {"fr": "la place", "tr": "[la plas]", "ru": "место"},
        {"fr": "les places", "tr": "[le plas]", "ru": "места"},
        {"fr": "sa salle", "tr": "[sa sal]", "ru": "его/её зал"},
        {"fr": "ses salles", "tr": "[se sal]", "ru": "его/её залы"},
        {"fr": "cette balle", "tr": "[sɛt bal]", "ru": "эта пуля"},
        {"fr": "ces balles", "tr": "[se bal]", "ru": "эти пули"},
        {"fr": "la mère", "tr": "[la mɛr]", "ru": "мать"},
        {"fr": "les mères", "tr": "[le mɛr]", "ru": "матери"},
        {"fr": "ta malle", "tr": "[ta mal]", "ru": "твой чемодан"},
        {"fr": "tes malles", "tr": "[te mal]", "ru": "твои чемоданы"},
        {"fr": "ma lettre", "tr": "[ma lɛtr]", "ru": "моё письмо"},
        {"fr": "mes lettres", "tr": "[me lɛtr]", "ru": "мои письма"},
        {"fr": "sa trace", "tr": "[sa tras]", "ru": "его/её след"},
        {"fr": "ses traces", "tr": "[se tras]", "ru": "его/её следы"},
        {"fr": "la tête", "tr": "[la tɛt]", "ru": "голова"},
        {"fr": "les têtes", "tr": "[le tɛt]", "ru": "головы"},
        {"fr": "cette table", "tr": "[sɛt tabl]", "ru": "этот стол"},
        {"fr": "ces tables", "tr": "[se tabl]", "ru": "эти столы"},
        {"fr": "ta phrase", "tr": "[ta fraz]", "ru": "твоя фраза"},
        {"fr": "tes phrases", "tr": "[te fraz]", "ru": "твои фразы"},

        # Примеры связывания (liaison)
        {"fr": "tes vestes", "tr": "[te vɛst]", "ru": "твои куртки"},
        {"fr": "tes affaires", "tr": "[te za fɛr]", "ru": "твои дела"},
        {"fr": "mes traces", "tr": "[me tras]", "ru": "мои следы"},
        {"fr": "mes élèves", "tr": "[me ze lɛv]", "ru": "мои ученики"},
        {"fr": "les salaires", "tr": "[le sa lɛr]", "ru": "зарплаты"},
        {"fr": "les années", "tr": "[le za ne]", "ru": "годы"},

        # Фразы для перевода
        {"fr": "aimer sa mère", "tr": "[eme sa mɛr]", "ru": "любить свою мать"},
        {"fr": "répéter ces phrases", "tr": "[repete se fraz]", "ru": "повторять эти фразы"},
        {"fr": "aller au Tibet", "tr": "[ale o tibɛ]", "ru": "ехать в Тибет"},
        {"fr": "tête-à-tête", "tr": "[tɛt a tɛt]", "ru": "с глазу на глаз"},
        {"fr": "ma terre natale", "tr": "[ma tɛr natal]", "ru": "моя родная земля"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №2: Пары звуков [pe-pɛ], [be-bɛ] и т.д.", "url": "/static/audio/lesson4_2.mp3"},
        {"title": "Упражнение №4: Глаголы с окончанием -er", "url": "/static/audio/lesson4_4.mp3"},
        {"title": "Упражнение №5: Повелительное наклонение -ez", "url": "/static/audio/lesson4_5.mp3"},
        {"title": "Упражнение №8: Связывание и множественное число", "url": "/static/audio/lesson4_8.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Какой звук дает буква É (accent aigu)?",
         "options": ["[ɛ]", "[e]", "[ə]", "[a]"], "correct": "[e]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как читается окончание -er в глаголах (parler, aimer)?",
         "options": ["[er]", "[e]", "[ɛ]", "[ə]"], "correct": "[e]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как читается окончание -ez в глаголах (parlez, fermez)?",
         "options": ["[ez]", "[e]", "[ɛ]", "[ə]"], "correct": "[e]"},
        {"id": 4, "type": "quiz", "question": "🔊 Смягчаются ли французские согласные перед гласным [e]?",
         "options": ["Да, всегда", "Нет, никогда", "Только перед [e]", "Только в конце слов"],
         "correct": "Нет, никогда"},
        {"id": 5, "type": "quiz", "question": "🔊 Какая буква НЕ читается в окончании -er глаголов?",
         "options": ["e", "r", "er читается полностью", "Никакая"], "correct": "r"},
        {"id": 6, "type": "quiz", "question": "🔊 Какая буква НЕ читается в окончании -ez?",
         "options": ["e", "z", "ez читается полностью", "Никакая"], "correct": "z"},

        # ========== УПРАЖНЕНИЕ №5: ПЕРЕВОД ФОРМ ПОВЕЛИТЕЛЬНОГО НАКЛОНЕНИЯ (text_input) ==========
        {"id": 7, "type": "text_input", "question": "📖 Переведите: 'répétez!'", "correct": "повторите"},
        {"id": 8, "type": "text_input", "question": "📖 Переведите: 'laissez!'", "correct": "оставьте"},
        {"id": 9, "type": "text_input", "question": "📖 Переведите: 'passez!'", "correct": "проходите"},
        {"id": 10, "type": "text_input", "question": "📖 Переведите: 'frappez!'", "correct": "ударьте"},
        {"id": 11, "type": "text_input", "question": "📖 Переведите: 'aimez!'", "correct": "любите"},
        {"id": 12, "type": "text_input", "question": "📖 Переведите: 'fermez!'", "correct": "закройте"},
        {"id": 13, "type": "text_input", "question": "📖 Переведите: 'baissez!'", "correct": "опустите"},
        {"id": 14, "type": "text_input", "question": "📖 Переведите: 'allez!'", "correct": "идите"},
        {"id": 15, "type": "text_input", "question": "📖 Переведите: 'parlez!'", "correct": "говорите"},
        {"id": 16, "type": "text_input", "question": "📖 Переведите: 'adressez!'", "correct": "адресуйте"},
        {"id": 17, "type": "text_input", "question": "📖 Переведите: 'restez!'", "correct": "останьтесь"},
        {"id": 18, "type": "text_input", "question": "📖 Переведите: 'traversez!'", "correct": "переходите"},
        {"id": 19, "type": "text_input", "question": "📖 Переведите: 'espérez!'", "correct": "надейтесь"},
        {"id": 20, "type": "text_input", "question": "📖 Переведите: 'aidez!'", "correct": "помогите"},
        {"id": 21, "type": "text_input", "question": "📖 Переведите: 'cessez!'", "correct": "прекратите"},

        # ========== УПРАЖНЕНИЕ №6: ОБРАЗОВАНИЕ МНОЖЕСТВЕННОГО ЧИСЛА (text_input) ==========
        {"id": 22, "type": "text_input", "question": "📝 Допишите множественное число: 'ta phrase → ...'",
         "correct": "tes phrases"},
        {"id": 23, "type": "text_input", "question": "📝 Допишите множественное число: 'ma lettre → ...'",
         "correct": "mes lettres"},
        {"id": 24, "type": "text_input", "question": "📝 Допишите множественное число: 'sa trace → ...'",
         "correct": "ses traces"},
        {"id": 25, "type": "text_input", "question": "📝 Допишите множественное число: 'la tête → ...'",
         "correct": "les têtes"},
        {"id": 26, "type": "text_input", "question": "📝 Допишите множественное число: 'cette table → ...'",
         "correct": "ces tables"},

        # ========== УПРАЖНЕНИЕ №7: ПЕРЕВОД С РУССКОГО (text_input) ==========
        {"id": 27, "type": "text_input", "question": "🔄 Переведите: 'мой стол'", "correct": "ma table"},
        {"id": 28, "type": "text_input", "question": "🔄 Переведите: 'эти места'", "correct": "ces places"},
        {"id": 29, "type": "text_input", "question": "🔄 Переведите: 'твои письма'", "correct": "tes lettres"},
        {"id": 30, "type": "text_input", "question": "🔄 Переведите: 'его комната'", "correct": "sa salle"},
        {"id": 31, "type": "text_input", "question": "🔄 Переведите: 'ее фразы'", "correct": "ses phrases"},
        {"id": 32, "type": "text_input", "question": "🔄 Переведите: 'моя голова'", "correct": "ma tête"},
        {"id": 33, "type": "text_input", "question": "🔄 Переведите: 'этот след'", "correct": "cette trace"},
        {"id": 34, "type": "text_input", "question": "🔄 Переведите: 'повторите!'", "correct": "répétez"},
        {"id": 35, "type": "text_input", "question": "🔄 Переведите: 'прекратите!'", "correct": "cessez"},
        {"id": 36, "type": "text_input", "question": "🔄 Переведите: 'говорите!'", "correct": "parlez"},
        {"id": 37, "type": "text_input", "question": "🔄 Переведите: 'помогите!'", "correct": "aidez"},
        {"id": 38, "type": "text_input", "question": "🔄 Переведите: 'проходите!'", "correct": "passez"},
        {"id": 39, "type": "text_input", "question": "🔄 Переведите: 'останьтесь!'", "correct": "restez"},
        {"id": 40, "type": "text_input", "question": "🔄 Переведите: 'закройте!'", "correct": "fermez"},
        {"id": 41, "type": "text_input", "question": "🔄 Переведите: 'идите!'", "correct": "allez"},
        {"id": 42, "type": "text_input", "question": "🔄 Переведите: 'опустите!'", "correct": "baissez"},
        {"id": 43, "type": "text_input", "question": "🔄 Переведите: 'оставьте!'", "correct": "laissez"},
        {"id": 44, "type": "text_input", "question": "🔄 Переведите: 'поезжайте!'", "correct": "allez"},

        # ========== УПРАЖНЕНИЕ №9: ПЕРЕВОД ФРАЗ (text_input) ==========
        {"id": 45, "type": "text_input", "question": "📖 Переведите: 'aimer sa mère'", "correct": "любить свою мать"},
        {"id": 46, "type": "text_input", "question": "📖 Переведите: 'répéter ces phrases'",
         "correct": "повторять эти фразы"},
        {"id": 47, "type": "text_input", "question": "📖 Переведите: 'aller au Tibet'", "correct": "ехать в Тибет"},
        {"id": 48, "type": "text_input", "question": "📖 Переведите: 'elle est prête'", "correct": "она готова"},
        {"id": 49, "type": "text_input", "question": "📖 Переведите: 'tête-à-tête'", "correct": "с глазу на глаз"},
        {"id": 50, "type": "text_input", "question": "📖 Переведите: 'ma terre natale'", "correct": "моя родная земля"},

        # ========== ДОПОЛНИТЕЛЬНЫЕ ВОПРОСЫ НА ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 51, "type": "quiz", "question": "📖 Как переводится 'parler'?",
         "options": ["говорить", "любить", "помогать", "идти"], "correct": "говорить"},
        {"id": 52, "type": "quiz", "question": "📖 Как переводится 'aimer'?",
         "options": ["говорить", "помогать", "любить", "закрывать"], "correct": "любить"},
        {"id": 53, "type": "quiz", "question": "📖 Как переводится 'fermer'?",
         "options": ["открывать", "закрывать", "оставлять", "прекращать"], "correct": "закрывать"},
        {"id": 54, "type": "quiz", "question": "📖 Как переводится 'répéter'?",
         "options": ["повторять", "надеяться", "оставаться", "проходить"], "correct": "повторять"},

        # ========== ПЕРЕВОД С РУССКОГО (слова, text_input) ==========
        {"id": 55, "type": "text_input", "question": "🔄 Напишите по-французски 'говорить'", "correct": "parler"},
        {"id": 56, "type": "text_input", "question": "🔄 Напишите по-французски 'любить'", "correct": "aimer"},
        {"id": 57, "type": "text_input", "question": "🔄 Напишите по-французски 'помогать'", "correct": "aider"},
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'идти'", "correct": "aller"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'закрывать'", "correct": "fermer"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'повторять'", "correct": "répéter"},
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'оставаться'", "correct": "rester"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'надеяться'", "correct": "espérer"}
    ],
    "question": "Пройдите все 62 карточки практики!",
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
# ---------- ДЕНЬ 8: ТЕСТ 2 (Уроки 3-4 / дни 5-6) ----------
COURSE_DAYS[8] = {
    "title": "Тест 2: Уроки 3-4 (Звуки [s]/[z] и [e])",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        # ============================================================
        # ЧАСТЬ 1: ДИКТАНТ СЛОВ ИЗ УРОКА 3 (звуки [s] и [z])
        # ============================================================
        {"id": 1, "type": "text_input", "question": "📝 Напишите по-французски: 'фраза'", "correct": "phrase"},
        {"id": 2, "type": "text_input", "question": "📝 Напишите по-французски: 'ваза'", "correct": "vase"},
        {"id": 3, "type": "text_input", "question": "📝 Напишите по-французски: 'зал, комната'", "correct": "salle"},
        {"id": 4, "type": "text_input", "question": "📝 Напишите по-французски: 'грязный'", "correct": "sale"},
        {"id": 5, "type": "text_input", "question": "📝 Напишите по-французски: 'салат'", "correct": "salade"},
        {"id": 6, "type": "text_input", "question": "📝 Напишите по-французски: 'зарплата'", "correct": "salaire"},
        {"id": 7, "type": "text_input", "question": "📝 Напишите по-французски: 'соль'", "correct": "sel"},
        {"id": 8, "type": "text_input", "question": "📝 Напишите по-французски: 'эта (жен. род)'", "correct": "cette"},
        {"id": 9, "type": "text_input", "question": "📝 Напишите по-французски: 'куртка'", "correct": "veste"},
        {"id": 10, "type": "text_input", "question": "📝 Напишите по-французски: 'стадион'", "correct": "stade"},
        {"id": 11, "type": "text_input", "question": "📝 Напишите по-французски: 'адрес'", "correct": "adresse"},
        {"id": 12, "type": "text_input", "question": "📝 Напишите по-французски: 'след'", "correct": "trace"},
        {"id": 13, "type": "text_input", "question": "📝 Напишите по-французски: 'место'", "correct": "place"},

        # ============================================================
        # ЧАСТЬ 2: ДИКТАНТ СЛОВ ИЗ УРОКА 4 (звук [e] и глаголы)
        # ============================================================
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски: 'говорить'", "correct": "parler"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски: 'любить'", "correct": "aimer"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски: 'помогать'", "correct": "aider"},
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски: 'идти; ехать'", "correct": "aller"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски: 'переходить'", "correct": "traverser"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски: 'закрывать'", "correct": "fermer"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски: 'прекращать'", "correct": "cesser"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски: 'оставлять'", "correct": "laisser"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски: 'опускать'", "correct": "baisser"},
        {"id": 23, "type": "text_input", "question": "📝 Напишите по-французски: 'проходить'", "correct": "passer"},
        {"id": 24, "type": "text_input", "question": "📝 Напишите по-французски: 'повторять'", "correct": "répéter"},
        {"id": 25, "type": "text_input", "question": "📝 Напишите по-французски: 'оставаться'", "correct": "rester"},
        {"id": 26, "type": "text_input", "question": "📝 Напишите по-французски: 'надеяться'", "correct": "espérer"},

        # ============================================================
        # ЧАСТЬ 3: ФОНЕТИКА И ПРАВИЛА ЧТЕНИЯ (quiz)
        # ============================================================
        {"id": 27, "type": "quiz", "question": "🔊 Когда буква 'S' читается как звонкий звук [z]?",
         "options": ["В начале слова", "Между двумя гласными", "Перед согласной", "На конце слова"],
         "correct": "Между двумя гласными"},
        {"id": 28, "type": "quiz", "question": "🔊 Удвоенное 'ss' во французском дает звук...",
         "options": ["[z]", "[s]", "[ʃ]", "[ʒ]"], "correct": "[s]"},
        {"id": 29, "type": "quiz", "question": "🔊 Что означает значок 'ç' (cédille) под буквой C?",
         "options": ["Буква не читается", "Читается как [k]", "Читается как [s] перед a, o", "Читается как [z]"],
         "correct": "Читается как [s] перед a, o"},
        {"id": 30, "type": "quiz", "question": "🔊 Как читается буква 'C' перед гласными 'e', 'i', 'y'?",
         "options": ["[k]", "[s]", "[g]", "[ʃ]"], "correct": "[s]"},
        {"id": 31, "type": "quiz", "question": "🔊 Какой звук дает буквосочетание 'ph'?",
         "options": ["[p]", "[f]", "[ph]", "[v]"], "correct": "[f]"},
        {"id": 32, "type": "quiz", "question": "🔊 Какой звук дает буква É (accent aigu)?",
         "options": ["[ɛ]", "[e]", "[ə]", "[a]"], "correct": "[e]"},
        {"id": 33, "type": "quiz", "question": "🔊 Как читается окончание -er в глаголах?",
         "options": ["[er]", "[e]", "[ɛ]", "[ə]"], "correct": "[e]"},
        {"id": 34, "type": "quiz", "question": "🔊 Смягчаются ли французские согласные перед гласным [e]?",
         "options": ["Да, всегда", "Нет, никогда", "Только перед [e]", "Только в конце слов"],
         "correct": "Нет, никогда"},
        {"id": 35, "type": "quiz", "question": "🔊 Перед какими конечными звуками удлиняется ударный гласный?",
         "options": ["[p], [t], [k]", "[v], [r], [z]", "[b], [d], [g]", "[m], [n], [l]"],
         "correct": "[v], [r], [z]"},

        # ============================================================
        # ЧАСТЬ 4: ПЕРЕВОД ФРАЗ (text_input)
        # ============================================================
        {"id": 36, "type": "text_input", "question": "📖 Переведите на русский: 'sa mère est belle'",
         "correct": "его мать красива"},
        {"id": 37, "type": "text_input", "question": "📖 Переведите на русский: 'cette veste est sale'",
         "correct": "эта куртка грязная"},
        {"id": 38, "type": "text_input", "question": "📖 Переведите на русский: 'elle est prête'",
         "correct": "она готова"},
        {"id": 39, "type": "text_input", "question": "📖 Переведите на русский: 'aimer sa mère'",
         "correct": "любить свою мать"},
        {"id": 40, "type": "text_input", "question": "📖 Переведите на русский: 'répéter ces phrases'",
         "correct": "повторять эти фразы"},
        {"id": 41, "type": "text_input", "question": "📖 Переведите на русский: 'aller au Tibet'",
         "correct": "ехать в Тибет"},
        {"id": 42, "type": "text_input", "question": "📖 Переведите на русский: 'ma terre natale'",
         "correct": "моя родная земля"},

        # ============================================================
        # ЧАСТЬ 5: ПЕРЕВОД С РУССКОГО НА ФРАНЦУЗСКИЙ (text_input)
        # ============================================================
        {"id": 43, "type": "text_input", "question": "🔄 Переведите на французский: 'Она готова.'",
         "correct": "elle est prête"},
        {"id": 44, "type": "text_input", "question": "🔄 Переведите на французский: 'Нана больна.'",
         "correct": "nana est malade"},
        {"id": 45, "type": "text_input", "question": "🔄 Переведите на французский: 'Его мать красива.'",
         "correct": "sa mère est belle"},
        {"id": 46, "type": "text_input", "question": "🔄 Переведите на французский: 'Эта куртка грязная.'",
         "correct": "cette veste est sale"},
        {"id": 47, "type": "text_input", "question": "🔄 Переведите на французский: 'мои письма'",
         "correct": "mes lettres"},
        {"id": 48, "type": "text_input", "question": "🔄 Переведите на французский: 'твои куртки'",
         "correct": "tes vestes"},
        {"id": 49, "type": "text_input", "question": "🔄 Переведите на французский: 'эти столы'",
         "correct": "ces tables"},
        {"id": 50, "type": "text_input", "question": "🔄 Переведите на французский: 'говорите!'", "correct": "parlez"},
        {"id": 51, "type": "text_input", "question": "🔄 Переведите на французский: 'закройте!'", "correct": "fermez"},
        {"id": 52, "type": "text_input", "question": "🔄 Переведите на французский: 'повторите!'", "correct": "répétez"},
        {"id": 53, "type": "text_input", "question": "🔄 Переведите на французский: 'идите!'", "correct": "allez"},
        {"id": 54, "type": "text_input", "question": "🔄 Переведите на французский: 'помогите!'", "correct": "aidez"},

        # ============================================================
        # ЧАСТЬ 6: ТРАНСКРИПЦИЯ (text_input)
        # ============================================================
        {"id": 55, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'phrase'", "correct": "[fra:z]"},
        {"id": 56, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'vase'", "correct": "[va:z]"},
        {"id": 57, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'parler'", "correct": "[parle]"},
        {"id": 58, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'aimer'", "correct": "[eme]"},
        {"id": 59, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'aller'", "correct": "[ale]"},

        # ============================================================
        # ЧАСТЬ 7: СВЯЗЫВАНИЕ (liaison) - quiz
        # ============================================================
        {"id": 60, "type": "quiz", "question": "🔗 Как читается 's' в словосочетании 'mes adresses'?",
         "options": ["Не читается", "Как [s]", "Как [z]", "Как [ʃ]"], "correct": "Как [z]"},
        {"id": 61, "type": "quiz", "question": "🔗 В каких словах s читается как [z] перед гласным?",
         "options": ["mes, tes, ses, ces, les, des", "Всегда", "Никогда", "Только в начале слов"],
         "correct": "mes, tes, ses, ces, les, des"},
        {"id": 62, "type": "quiz", "question": "📖 Как переводится 'les années'?",
         "options": ["зарплаты", "годы", "адреса", "ученики"], "correct": "годы"},

        # ============================================================
        # ЧАСТЬ 8: ДОПОЛНИТЕЛЬНЫЕ СЛОВА (quiz)
        # ============================================================
        {"id": 63, "type": "quiz", "question": "📖 Как переводится 'phrase'?",
         "options": ["фраза", "ваза", "место", "адрес"], "correct": "фраза"},
        {"id": 64, "type": "quiz", "question": "📖 Как переводится 'veste'?",
         "options": ["стадион", "адрес", "куртка", "след"], "correct": "куртка"},
        {"id": 65, "type": "quiz", "question": "📖 Как переводится 'place'?",
         "options": ["место", "след", "адрес", "стадион"], "correct": "место"},
        {"id": 66, "type": "quiz", "question": "📖 Как переводится 'répéter'?",
         "options": ["повторять", "надеяться", "оставаться", "проходить"], "correct": "повторять"}
    ],
    "question": "Пройдите все 66 вопросов теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 9: УРОК 5 ----------
# ---------- ДЕНЬ 9: УРОК 5 (Звуки [i], [j], немая h и согласные на конце слов) ----------
COURSE_DAYS[9] = {
    "title": "Урок 5: Звуки [i], [j], немая h и согласные на конце слов",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "гласный [i]",
            "russian": "[и] как в слове нить (но с улыбкой!)",
            "letters": "I, i<br>Î, î<br>Y, y",
            "notes": "• Оттяните уголки рта в стороны, настройтесь на улыбку!<br>• Французский [i] очень 'улыбчивый' звук.<br>• Гласные звучат одинаково четко под ударением и без него.<br>• Пример: milice [milis] — милиция (оба [i] четкие)."
        },
        {
            "sound": "полугласный [j]",
            "russian": "[й] как в начале слов яд, ель, ёлка, юг",
            "letters": "ill<br>il<br>i (перед гласной)",
            "notes": "• Буквосочетание ill → [j] (кроме: mille, ville, Lille).<br>• Буквосочетание il → [j] после произносимой гласной (détail [detaj]).<br>• Буква i → [j] перед произносимой гласной (rivière [rivjɛr]).<br>• [j] никогда не ослабляется и не 'заглатывается'!"
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "🔇 Немая буква H",
            "text": "Во французском алфавите есть буква, которая <b>никогда не читается</b> и потому называется <b>немой</b> — <b>h</b> (прописная H).<br><br>"
                    "Примеры: hiver [ivɛr] — зима, habile [abil] — ловкий."
        },
        {
            "subtitle": "🔇 Согласные s, t, d на конце слов",
            "text": "Буквы <b>s, t, d</b> на конце слов, как правило, <b>не читаются</b>.<br><br>"
                    "Примеры:<br>"
                    "• très [trɛ] — очень<br>"
                    "• mais [mɛ] — но<br>"
                    "• ils [il] — они (м.р.)<br>"
                    "• elles [ɛl] — они (ж.р.)<br>"
                    "• tard [tar] — поздно<br>"
                    "• prêt [prɛ] — готов (м.р.)<br>"
                    "• prête [prɛt] — готова (ж.р.) — t читается!"
        },
        {
            "subtitle": "🔗 Связывание с très",
            "text": "Буква <b>s</b> на конце слова <b>très</b> читается как <b>[z]</b> перед словами, начинающимися на гласный или <b>h</b> немую.<br><br>"
                    "Примеры:<br>"
                    "• très avare [trɛzavar] — очень скупой<br>"
                    "• très habile [trɛzabil] — очень ловкий"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Прочтите слова, стараясь запомнить их:",
            "text": "• il [il] — он, она, оно (употребляется вместо французских слов мужского рода)<br>"
                    "• île [il] — остров<br>"
                    "• idée [ide] — идея<br>"
                    "• Yves [iv] — Ив (мужское имя)<br>"
                    "• ici [isi] — здесь<br>"
                    "• fils [fis] — сын (буква l в этом слове не читается)<br>"
                    "• type [tip] — тип<br>"
                    "• vite [vit] — быстро<br>"
                    "• mille [mil] — тысяча<br>"
                    "• ville [vil] — город<br>"
                    "• Lille [lil] — Лилль (город во Франции)"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочтите:",
            "text": "• cette idée [sɛt ide] — эта идея<br>"
                    "• ses idées [sez ide] — его идеи<br>"
                    "• il est libre [il ɛ libr] — он свободен<br>"
                    "• elle est libre [ɛl ɛ libr] — она свободна<br>"
                    "• mes amies [mez ami] — мои подруги<br>"
                    "• les villes [le vil] — города<br>"
                    "• ces systèmes [se sistem] — эти системы"
        },
        {
            "subtitle": "🎧 Упражнение № 4. Прочтите и постарайтесь запомнить глаголы со звуком [i]:",
            "text": "• dîner [dine] — ужинать<br>"
                    "• décider [deside] — решать<br>"
                    "• terminer [termine] — заканчивать<br>"
                    "• imiter [imite] — имитировать<br>"
                    "• arriver [arive] — приезжать<br>"
                    "• visiter [vizite] — посещать<br>"
                    "• dire [dir] — говорить<br>"
                    "• lire [lir] — читать<br>"
                    "• rire [rir] — смеяться<br>"
                    "• vivre [vivr] — жить<br>"
                    "• finir [finir] — заканчивать"
        },
        {
            "subtitle": "🎧 Упражнение № 6. Прочтите и постарайтесь запомнить новые слова:",
            "text": "• habiter [abite] — жить<br>"
                    "• hiver [ivɛr] — зима<br>"
                    "• trahir [trair] — предавать<br>"
                    "• habile [abil] — ловкий, -ая, -ое<br>"
                    "• hybride [ibrid] — гибрид<br>"
                    "• hymne [imn] — гимн<br>"
                    "• hésiter [ezite] — колебаться"
        },
        {
            "subtitle": "🎧 Упражнение № 7. Прочтите слова и постарайтесь запомнить их:",
            "text": "• famille [famij] — семья<br>"
                    "• fille [fij] — дочь<br>"
                    "• il travaille [il travaj] — он работает<br>"
                    "• travail [travaj] — работа<br>"
                    "• détail [detaj] — подробность<br>"
                    "• pièce [pjɛs] — комната<br>"
                    "• ciel [sjɛl] — небо<br>"
                    "• Pierre [pjɛr] — Пьер (мужское имя)<br>"
                    "• pierre [pjɛr] — камень<br>"
                    "• hier [jɛr] — вчера<br>"
                    "• rivière [rivjɛr] — река<br>"
                    "• marié [marje] — женатый, женат<br>"
                    "• mariée [marje] — замужняя, замужем"
        },
        {
            "subtitle": "🎧 Упражнение № 9. Прочтите, обращая внимание на выделенные буквы, и выучите новые слова:",
            "text": "• après [aprɛ] — после<br>"
                    "• très [trɛ] — очень<br>"
                    "• mais [mɛ] — но (союз)<br>"
                    "• ils [il] — они (употребляется вместо французских слов мужского рода)<br>"
                    "• elles [ɛl] — они (употребляется вместо французских слов женского рода)<br>"
                    "• les hivers [lezivɛr] — зимы<br>"
                    "• bas [ba] — низкий, -ая, -ое (при французских словах мужского рода)<br>"
                    "• lait [lɛ] — молоко<br>"
                    "• tard [tar] — поздно<br>"
                    "• il est prêt [ilɛprɛ] — он готов<br>"
                    "• elle est prête [ɛlɛprɛt] — она готова"
        }
    ],
    "vocabulary": [
        {"fr": "il", "tr": "[il]", "ru": "он (для слов мужского рода)"},
        {"fr": "île", "tr": "[il]", "ru": "остров"},
        {"fr": "idée", "tr": "[ide]", "ru": "идея"},
        {"fr": "Yves", "tr": "[iv]", "ru": "Ив (мужское имя)"},
        {"fr": "ici", "tr": "[isi]", "ru": "здесь"},
        {"fr": "fils", "tr": "[fis]", "ru": "сын"},
        {"fr": "type", "tr": "[tip]", "ru": "тип"},
        {"fr": "vite", "tr": "[vit]", "ru": "быстро"},
        {"fr": "mille", "tr": "[mil]", "ru": "тысяча"},
        {"fr": "ville", "tr": "[vil]", "ru": "город"},
        {"fr": "Lille", "tr": "[lil]", "ru": "Лилль"},
        {"fr": "cette idée", "tr": "[sɛt ide]", "ru": "эта идея"},
        {"fr": "ses idées", "tr": "[sez ide]", "ru": "его идеи"},
        {"fr": "il est libre", "tr": "[il ɛ libr]", "ru": "он свободен"},
        {"fr": "elle est libre", "tr": "[ɛl ɛ libr]", "ru": "она свободна"},
        {"fr": "mes amies", "tr": "[mez ami]", "ru": "мои подруги"},
        {"fr": "les villes", "tr": "[le vil]", "ru": "города"},
        {"fr": "ces systèmes", "tr": "[se sistem]", "ru": "эти системы"},
        {"fr": "dîner", "tr": "[dine]", "ru": "ужинать"},
        {"fr": "décider", "tr": "[deside]", "ru": "решать"},
        {"fr": "terminer", "tr": "[termine]", "ru": "заканчивать"},
        {"fr": "imiter", "tr": "[imite]", "ru": "имитировать"},
        {"fr": "arriver", "tr": "[arive]", "ru": "приезжать"},
        {"fr": "visiter", "tr": "[vizite]", "ru": "посещать"},
        {"fr": "dire", "tr": "[dir]", "ru": "говорить"},
        {"fr": "lire", "tr": "[lir]", "ru": "читать"},
        {"fr": "rire", "tr": "[rir]", "ru": "смеяться"},
        {"fr": "vivre", "tr": "[vivr]", "ru": "жить"},
        {"fr": "finir", "tr": "[finir]", "ru": "заканчивать"},
        {"fr": "habiter", "tr": "[abite]", "ru": "жить"},
        {"fr": "hiver", "tr": "[ivɛr]", "ru": "зима"},
        {"fr": "trahir", "tr": "[trair]", "ru": "предавать"},
        {"fr": "habile", "tr": "[abil]", "ru": "ловкий"},
        {"fr": "hybride", "tr": "[ibrid]", "ru": "гибрид"},
        {"fr": "hymne", "tr": "[imn]", "ru": "гимн"},
        {"fr": "hésiter", "tr": "[ezite]", "ru": "колебаться"},
        {"fr": "famille", "tr": "[famij]", "ru": "семья"},
        {"fr": "fille", "tr": "[fij]", "ru": "дочь"},
        {"fr": "il travaille", "tr": "[il travaj]", "ru": "он работает"},
        {"fr": "travail", "tr": "[travaj]", "ru": "работа"},
        {"fr": "détail", "tr": "[detaj]", "ru": "подробность"},
        {"fr": "pièce", "tr": "[pjɛs]", "ru": "комната"},
        {"fr": "ciel", "tr": "[sjɛl]", "ru": "небо"},
        {"fr": "Pierre", "tr": "[pjɛr]", "ru": "Пьер"},
        {"fr": "pierre", "tr": "[pjɛr]", "ru": "камень"},
        {"fr": "hier", "tr": "[jɛr]", "ru": "вчера"},
        {"fr": "rivière", "tr": "[rivjɛr]", "ru": "река"},
        {"fr": "marié", "tr": "[marje]", "ru": "женатый"},
        {"fr": "mariée", "tr": "[marje]", "ru": "замужняя"},
        {"fr": "après", "tr": "[aprɛ]", "ru": "после"},
        {"fr": "très", "tr": "[trɛ]", "ru": "очень"},
        {"fr": "mais", "tr": "[mɛ]", "ru": "но"},
        {"fr": "ils", "tr": "[il]", "ru": "они (м.р.)"},
        {"fr": "elles", "tr": "[ɛl]", "ru": "они (ж.р.)"},
        {"fr": "les hivers", "tr": "[lezivɛr]", "ru": "зимы"},
        {"fr": "bas", "tr": "[ba]", "ru": "низкий"},
        {"fr": "lait", "tr": "[lɛ]", "ru": "молоко"},
        {"fr": "tard", "tr": "[tar]", "ru": "поздно"},
        {"fr": "il est prêt", "tr": "[ilɛprɛ]", "ru": "он готов"},
        {"fr": "elle est prête", "tr": "[ɛlɛprɛt]", "ru": "она готова"},
        {"fr": "Paris et Lille", "tr": "[pari e lil]", "ru": "Париж и Лилль"},
        {"fr": "Anne", "tr": "[an]", "ru": "Анна"},
        {"fr": "direz", "tr": "[dire]", "ru": "скажите"},
        {"fr": "dînez", "tr": "[dine]", "ru": "ужинайте"},
        {"fr": "terminez", "tr": "[termine]", "ru": "заканчивайте"},
        {"fr": "allez", "tr": "[ale]", "ru": "идите"},
        {"fr": "ces rivières", "tr": "[se rivjɛr]", "ru": "эти реки"},
        {"fr": "les pierres", "tr": "[le pjɛr]", "ru": "камни"},
        {"fr": "Elle travaille", "tr": "[ɛl travaj]", "ru": "Она работает"},
        {"fr": "Ma famille est là", "tr": "[ma famij ɛ la]", "ru": "Моя семья там"},
        {"fr": "Sa fille est mariée", "tr": "[sa fij ɛ marje]", "ru": "Его дочь замужем"},
        {"fr": "Yves est marié", "tr": "[iv ɛ marje]", "ru": "Ив женат"},
        {"fr": "Pierre est malade et triste", "tr": "[pjɛr ɛ malad e trist]", "ru": "Пьер болен и грустен"},
        {"fr": "Il travaille ici", "tr": "[il travaj isi]", "ru": "Он работает здесь"},
        {"fr": "libre", "tr": "[libr]", "ru": "свободный"},
        {"fr": "triste", "tr": "[trist]", "ru": "грустный"},
        {"fr": "merci", "tr": "[mersi]", "ru": "спасибо"},
        {"fr": "ami", "tr": "[ami]", "ru": "друг"},
        {"fr": "livre", "tr": "[livr]", "ru": "книга"},
        {"fr": "lycée", "tr": "[lise]", "ru": "лицей"},
        {"fr": "système", "tr": "[sistem]", "ru": "система"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Слова со звуком [i]", "url": "/static/audio/lesson5_1.mp3"},
        {"title": "Упражнение №4: Глаголы со звуком [i]", "url": "/static/audio/lesson5_2.mp3"},
        {"title": "Упражнение №6: Немая H", "url": "/static/audio/lesson5_3.mp3"},
        {"title": "Упражнение №7: Звук [j] (ill, il)", "url": "/static/audio/lesson5_4.mp3"},
        {"title": "Упражнение №9: Конечные согласные", "url": "/static/audio/lesson5_5.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как правильно произносится французский звук [i]?",
         "options": ["Как русский [и], без изменений", "С оттянутыми уголками рта, 'улыбчиво'",
                     "С округленными губами", "Как [ы]"], "correct": "С оттянутыми уголками рта, 'улыбчиво'"},
        {"id": 2, "type": "quiz", "question": "🔊 Как читается слово 'fils' (сын)?",
         "options": ["[fils]", "[fil]", "[fis]", "[fi]"], "correct": "[fis]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как читается слово 'type'?",
         "options": ["[tip]", "[typ]", "[tɪp]", "[tɛp]"], "correct": "[tip]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается буквосочетание 'ill' в слове 'famille'?",
         "options": ["[il]", "[ij]", "[j]", "[ilj]"], "correct": "[j]"},
        {"id": 5, "type": "quiz", "question": "🔊 Какое слово является исключением и читается с [il] вместо [j]?",
         "options": ["famille", "fille", "ville", "travailler"], "correct": "ville"},
        {"id": 6, "type": "quiz", "question": "🔇 Читается ли буква 'h' во французском?",
         "options": ["Да, всегда", "Нет, никогда", "Только в начале слов", "Только в конце слов"],
         "correct": "Нет, никогда"},
        {"id": 7, "type": "quiz", "question": "🔇 Как читается слово 'hiver' (зима)?",
         "options": ["[hivɛr]", "[ivɛr]", "[hivɛ]", "[ivɛ]"], "correct": "[ivɛr]"},
        {"id": 8, "type": "quiz", "question": "🔇 Какие согласные на конце слов обычно НЕ читаются?",
         "options": ["p, b, m", "s, t, d", "c, g, f", "l, r, n"], "correct": "s, t, d"},
        {"id": 9, "type": "quiz", "question": "🔇 Как читается слово 'prêt' (готов, м.р.)?",
         "options": ["[prɛt]", "[prɛ]", "[prɛtə]", "[prɛt]"], "correct": "[prɛ]"},
        {"id": 10, "type": "quiz", "question": "🔇 Как читается слово 'prête' (готова, ж.р.)?",
         "options": ["[prɛt]", "[prɛ]", "[prɛtə]", "[prɛt]"], "correct": "[prɛt]"},

        # ========== УПРАЖНЕНИЕ №3: ПЕРЕВОД НА ФРАНЦУЗСКИЙ ==========
        {"id": 11, "type": "text_input", "question": "📝 Переведите на французский: 'твои подруги'", "correct": "tes amies"},
        {"id": 12, "type": "text_input", "question": "📝 Переведите на французский: 'эти города'", "correct": "ces villes"},
        {"id": 13, "type": "text_input", "question": "📝 Переведите на французский: 'свои системы'", "correct": "ses systèmes"},
        {"id": 14, "type": "text_input", "question": "📝 Переведите на французский: 'его книги'", "correct": "ses livres"},
        {"id": 15, "type": "text_input", "question": "📝 Переведите на французский: 'эти типы'", "correct": "ces types"},
        {"id": 16, "type": "text_input", "question": "📝 Переведите на французский: 'лицеи'", "correct": "les lycées"},
        {"id": 17, "type": "text_input", "question": "📝 Переведите на французский: 'Париж и Лилль'", "correct": "Paris et Lille"},
        {"id": 18, "type": "text_input", "question": "📝 Переведите на французский: 'город находится там'", "correct": "la ville est là"},
        {"id": 19, "type": "text_input", "question": "📝 Переведите на французский: 'Ив свободен'", "correct": "Yves est libre"},
        {"id": 20, "type": "text_input", "question": "📝 Переведите на французский: 'он там'", "correct": "il est là"},
        {"id": 21, "type": "text_input", "question": "📝 Переведите на французский: 'Анна грустна'", "correct": "Anne est triste"},

        # ========== УПРАЖНЕНИЕ №5: ПЕРЕВОД С ФРАНЦУЗСКОГО ==========
        {"id": 22, "type": "text_input", "question": "📖 Переведите на русский: 'faire vite'", "correct": "делать быстро"},
        {"id": 23, "type": "text_input", "question": "📖 Переведите на русский: 'direz!'", "correct": "скажите"},
        {"id": 24, "type": "text_input", "question": "📖 Переведите на русский: 'lire et rire'", "correct": "читать и смеяться"},
        {"id": 25, "type": "text_input", "question": "📖 Переведите на русский: 'dînez là!'", "correct": "ужинайте там"},
        {"id": 26, "type": "text_input", "question": "📖 Переведите на русский: 'terminez!'", "correct": "заканчивайте"},
        {"id": 27, "type": "text_input", "question": "📖 Переведите на русский: 'allez vite!'", "correct": "идите быстро"},

        # ========== УПРАЖНЕНИЕ №8: ПЕРЕВОД ФРАЗ ==========
        {"id": 28, "type": "text_input", "question": "📖 Переведите на русский: 'ces rivières'", "correct": "эти реки"},
        {"id": 29, "type": "text_input", "question": "📖 Переведите на русский: 'les pierres'", "correct": "камни"},
        {"id": 30, "type": "text_input", "question": "📖 Переведите на русский: 'Elle travaille'", "correct": "Она работает"},
        {"id": 31, "type": "text_input", "question": "📖 Переведите на русский: 'Ma famille est là'", "correct": "Моя семья там"},
        {"id": 32, "type": "text_input", "question": "📖 Переведите на русский: 'Sa fille est mariée'", "correct": "Его дочь замужем"},
        {"id": 33, "type": "text_input", "question": "📖 Переведите на русский: 'Yves est marié'", "correct": "Ив женат"},
        {"id": 34, "type": "text_input", "question": "📖 Переведите на русский: 'Pierre est malade et triste'", "correct": "Пьер болен и грустен"},
        {"id": 35, "type": "text_input", "question": "📖 Переведите на русский: 'Il travaille ici'", "correct": "Он работает здесь"},

        # ========== УПРАЖНЕНИЕ №9: НОВЫЕ СЛОВА ==========
        {"id": 36, "type": "quiz", "question": "📖 Как переводится 'après'?",
         "options": ["после", "перед", "очень", "но"], "correct": "после"},
        {"id": 37, "type": "quiz", "question": "📖 Как переводится 'très'?",
         "options": ["после", "очень", "но", "там"], "correct": "очень"},
        {"id": 38, "type": "quiz", "question": "📖 Как переводится 'mais'?",
         "options": ["очень", "после", "но", "и"], "correct": "но"},
        {"id": 39, "type": "quiz", "question": "📖 Как переводится 'ils'?",
         "options": ["они (м.р.)", "они (ж.р.)", "он", "она"], "correct": "они (м.р.)"},
        {"id": 40, "type": "quiz", "question": "📖 Как переводится 'elles'?",
         "options": ["они (м.р.)", "они (ж.р.)", "он", "она"], "correct": "они (ж.р.)"},
        {"id": 41, "type": "text_input", "question": "📝 Переведите на французский: 'зимы'", "correct": "les hivers"},
        {"id": 42, "type": "text_input", "question": "📝 Переведите на французский: 'низкий'", "correct": "bas"},
        {"id": 43, "type": "text_input", "question": "📝 Переведите на французский: 'молоко'", "correct": "lait"},
        {"id": 44, "type": "text_input", "question": "📝 Переведите на французский: 'поздно'", "correct": "tard"},
        {"id": 45, "type": "text_input", "question": "📝 Переведите на французский: 'он готов'", "correct": "il est prêt"},
        {"id": 46, "type": "text_input", "question": "📝 Переведите на французский: 'она готова'", "correct": "elle est prête"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 47, "type": "quiz", "question": "📖 Как переводится 'merci'?",
         "options": ["Пожалуйста", "Спасибо", "Извините", "Здравствуйте"], "correct": "Спасибо"},
        {"id": 48, "type": "quiz", "question": "📖 Как переводится 'triste'?",
         "options": ["Веселый", "Грустный", "Большой", "Маленький"], "correct": "Грустный"},
        {"id": 49, "type": "quiz", "question": "📖 Как переводится 'ami'?",
         "options": ["Подруга", "Друг", "Муж", "Брат"], "correct": "Друг"},
        {"id": 50, "type": "quiz", "question": "📖 Как переводится 'livre'?",
         "options": ["Свободный", "Книга", "Город", "Остров"], "correct": "Книга"},
        {"id": 51, "type": "quiz", "question": "📖 Как переводится 'famille'?",
         "options": ["Дочь", "Семья", "Работа", "Комната"], "correct": "Семья"},
        {"id": 52, "type": "quiz", "question": "📖 Как переводится 'lire'?",
         "options": ["Говорить", "Читать", "Смеяться", "Жить"], "correct": "Читать"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 53, "type": "text_input", "question": "🔄 Напишите по-французски 'друг'", "correct": "ami"},
        {"id": 54, "type": "text_input", "question": "🔄 Напишите по-французски 'книга'", "correct": "livre"},
        {"id": 55, "type": "text_input", "question": "🔄 Напишите по-французски 'семья'", "correct": "famille"},
        {"id": 56, "type": "text_input", "question": "🔄 Напишите по-французски 'работа'", "correct": "travail"},
        {"id": 57, "type": "text_input", "question": "🔄 Напишите по-французски 'спасибо'", "correct": "merci"},
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'грустный'", "correct": "triste"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'зима'", "correct": "hiver"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'они (м.р.)'", "correct": "ils"},
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'они (ж.р.)'", "correct": "elles"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'город'", "correct": "ville"},
        {"id": 63, "type": "text_input", "question": "🔄 Напишите по-французски 'остров'", "correct": "île"},
        {"id": 64, "type": "text_input", "question": "🔄 Напишите по-французски 'идея'", "correct": "idée"},
        {"id": 65, "type": "text_input", "question": "🔄 Напишите по-французски 'здесь'", "correct": "ici"},

        # ========== ТРАНСКРИПЦИЯ ==========
        {"id": 66, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'merci'", "correct": "[mersi]"},
        {"id": 67, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'triste'", "correct": "[trist]"},
        {"id": 68, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'hiver'", "correct": "[ivɛr]"},
        {"id": 69, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'famille'", "correct": "[famij]"},
        {"id": 70, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'travail'", "correct": "[travaj]"},
        {"id": 71, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'ville'", "correct": "[vil]"},
        {"id": 72, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'libre'", "correct": "[libr]"}
    ],
    "question": "Пройдите все 72 карточки практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 10: УРОК 6 ----------
# ---------- ДЕНЬ 10: УРОК 6 (Звуки [k], [g], [ɔ] и правила чтения) ----------
COURSE_DAYS[10] = {
    "title": "Урок 6: Звуки [k], [g], [ɔ] и правила чтения",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "согласный [k]",
            "russian": "[к] как в слове куст",
            "letters": "C, c<br>Qu, qu",
            "notes": "• Буква c читается как [k] перед всеми буквами, кроме e, i, y, h.<br>• Буква u после q не читается (qu → [k])."
        },
        {
            "sound": "звукосочетание [ks]",
            "russian": "[кс]",
            "letters": "X, x",
            "notes": "Буква x читается как [ks], если не находится в позиции между двумя произносимыми гласными."
        },
        {
            "sound": "согласный [g]",
            "russian": "[г] как в слове густо",
            "letters": "G, g<br>Gu, gu",
            "notes": "• Буква g читается как [g] перед всеми буквами, кроме e, i, y.<br>• Буква u после g не читается (gu → [g])."
        },
        {
            "sound": "звукосочетание [gz]",
            "russian": "[гз]",
            "letters": "X, x",
            "notes": "Буква x читается как [gz] между двумя произносимыми гласными звуками."
        },
        {
            "sound": "гласный [ɔ]",
            "russian": "отсутствует",
            "letters": "O, o",
            "notes": "Буква o читается как [ɔ] перед всеми произносимыми согласными, кроме z."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "📝 Правила чтения буквы C",
            "text": "Буква <b>C</b> читается по-разному в зависимости от следующей буквы:<br><br>"
                    "• <b>C → [k]</b> перед a, o, u и согласными<br>"
                    "• <b>C → [s]</b> перед e, i, y<br>"
                    "• <b>Ç (cédille) → [s]</b> перед a, o"
        },
        {
            "subtitle": "📝 Правила чтения буквы G",
            "text": "Буква <b>G</b> также читается по-разному:<br><br>"
                    "• <b>G → [g]</b> перед a, o, u и согласными<br>"
                    "• <b>G → [ʒ]</b> перед e, i, y<br>"
                    "• Буквосочетание <b>gu → [g]</b> (u не читается)"
        },
        {
            "subtitle": "🎯 Французский звук [ɔ] (открытый о)",
            "text": "Чтобы приблизиться к правильному произношению французского [ɔ], проделайте следующее. Перед зеркалом четко произнесите русские звуки [у] и [о]. Повторите это несколько раз, обращая внимание на положение своих губ. Вы увидите, что они сильно напряжены и вытянуты вперед, а разница между [у] и [о] в зеркале малозаметна. Это объясняется тем, что русский звук [о] неоднороден, он начинается кратким призвуком [у]. <b>Избавьтесь от этого призвука</b> — и вы достигнете примерно того, что нужно: французского [ɔ]! Избавьтесь — это значит произносите русское [о], но не вытягивайте губы резко вперед и не напрягайте их.<br><br>"
                    "Попробуем по-другому: представьте, что вы собрались протереть очки, и «дыхните» на воображаемые стекла — ваши губы займут именно то положение, которое требуется для французского [ɔ]. Зафиксируйте на несколько секунд это положение и, не меняя его, произнесите русское [о]. Получится французское [ɔ], словно легко слетающее с губ!"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Прочтите и постарайтесь запомнить слова:",
            "text": "• café [kafe] — кофе; кафе<br>"
                    "• calme [kalm] — спокойный, -ая, -ое<br>"
                    "• capitale [kapital] — столица<br>"
                    "• climat [klima] — климат; погода<br>"
                    "• écrire [ekrir] — писать<br>"
                    "• carte [kart] — карта<br>"
                    "• classe [klas] — класс<br>"
                    "• clé [kle] — ключ<br>"
                    "• article [artikl] — товар<br>"
                    "• quatre [katr] — четыре<br>"
                    "• qui [ki] — кто<br>"
                    "• quitter [kite] — покидать (оставлять)<br>"
                    "• clinique [klinik] — клиника<br>"
                    "• explicable [eksplikabl] — объяснимый, -ая, -ое<br>"
                    "• extase [ekstaz] — экстаз, восторг"
        },
        {
            "subtitle": "🎧 Упражнение № 4. Прочтите и постарайтесь запомнить слова:",
            "text": "• gare [gar] — вокзал<br>"
                    "• garder [garde] — охранять<br>"
                    "• gai [ge] — веселый, -ая, -ое (при французских словах мужского рода)<br>"
                    "• grave [grav] — серьезный, -ая, -ое<br>"
                    "• guide [gid] — гид<br>"
                    "• guerre [gɛr] — война<br>"
                    "• guérir [gerir] — выздоравливать<br>"
                    "• grève [grɛv] — забастовка<br>"
                    "• grammaire [gramɛr] — грамматика<br>"
                    "• glace [glas] — зеркало<br>"
                    "• fatigué [fatige] — усталый, -ая, -ое (при французских словах мужского рода)<br>"
                    "• exact [egzakt] — точный, -ая, -ое (при французских словах мужского рода)"
        },
        {
            "subtitle": "🎧 Упражнение № 7. Прочтите слова и выучите их:",
            "text": "• pomme [pɔm] — яблоко<br>"
                    "• homme [ɔm] — мужчина<br>"
                    "• robe [rɔb] — платье<br>"
                    "• porte [pɔrt] — дверь<br>"
                    "• fort [fɔr] — сильный, -ая, -ое; крепкий, -ая, -ое (при французских словах мужского рода)<br>"
                    "• la Sorbonne [sɔrbɔn] — Сорбонна (Парижский университет)<br>"
                    "• octobre [ɔktɔbr] — октябрь<br>"
                    "• police [pɔlis] — полиция<br>"
                    "• bonne [bɔn] — хороший, -ая, -ое; вкусный, -ая, -ое (при французских словах женского рода)<br>"
                    "• école [ekɔl] — школа<br>"
                    "• téléphone [telefɔn] — телефон<br>"
                    "• notre [nɔtr] — наш, наша, наше<br>"
                    "• votre [vɔtr] — ваш, ваша, ваше<br>"
                    "• donner [dɔne] — давать<br>"
                    "• porter [pɔrte] — носить<br>"
                    "• sonner [sɔne] — звонить<br>"
                    "• apporter [apɔrte] — приносить"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочитайте, перепишите и переведите:",
            "text": "• les articles<br>"
                    "• quatre classes<br>"
                    "• écrire vite<br>"
                    "• quitter Paris<br>"
                    "• Pierre est calme<br>"
                    "• Quittez la clinique !<br>"
                    "• Qui est ta fille ?"
        },
        {
            "subtitle": "🎧 Упражнение № 5. Прочтите, перепишите и переведите:",
            "text": "• La gare est là<br>"
                    "• Yves est gai et Nana est grave<br>"
                    "• Répétez la grammaire!<br>"
                    "• Gardez la gare!<br>"
                    "• Qui est Pierre ? — Il est guide. Il travaille. Il est très fatigué."
        }
    ],
    "vocabulary": [
        {"fr": "café", "tr": "[kafe]", "ru": "кофе; кафе"},
        {"fr": "calme", "tr": "[kalm]", "ru": "спокойный, -ая, -ое"},
        {"fr": "capitale", "tr": "[kapital]", "ru": "столица"},
        {"fr": "climat", "tr": "[klima]", "ru": "климат; погода"},
        {"fr": "écrire", "tr": "[ekrir]", "ru": "писать"},
        {"fr": "carte", "tr": "[kart]", "ru": "карта"},
        {"fr": "classe", "tr": "[klas]", "ru": "класс"},
        {"fr": "clé", "tr": "[kle]", "ru": "ключ"},
        {"fr": "article", "tr": "[artikl]", "ru": "товар"},
        {"fr": "quatre", "tr": "[katr]", "ru": "четыре"},
        {"fr": "qui", "tr": "[ki]", "ru": "кто"},
        {"fr": "quitter", "tr": "[kite]", "ru": "покидать (оставлять)"},
        {"fr": "clinique", "tr": "[klinik]", "ru": "клиника"},
        {"fr": "explicable", "tr": "[eksplikabl]", "ru": "объяснимый, -ая, -ое"},
        {"fr": "extase", "tr": "[ekstaz]", "ru": "экстаз, восторг"},
        {"fr": "gare", "tr": "[gar]", "ru": "вокзал"},
        {"fr": "garder", "tr": "[garde]", "ru": "охранять"},
        {"fr": "gai", "tr": "[ge]", "ru": "веселый, -ая, -ое"},
        {"fr": "grave", "tr": "[grav]", "ru": "серьезный, -ая, -ое"},
        {"fr": "guide", "tr": "[gid]", "ru": "гид"},
        {"fr": "guerre", "tr": "[gɛr]", "ru": "война"},
        {"fr": "guérir", "tr": "[gerir]", "ru": "выздоравливать"},
        {"fr": "grève", "tr": "[grɛv]", "ru": "забастовка"},
        {"fr": "grammaire", "tr": "[gramɛr]", "ru": "грамматика"},
        {"fr": "glace", "tr": "[glas]", "ru": "зеркало"},
        {"fr": "fatigué", "tr": "[fatige]", "ru": "усталый, -ая, -ое"},
        {"fr": "exact", "tr": "[egzakt]", "ru": "точный, -ая, -ое"},
        {"fr": "pomme", "tr": "[pɔm]", "ru": "яблоко"},
        {"fr": "homme", "tr": "[ɔm]", "ru": "мужчина"},
        {"fr": "robe", "tr": "[rɔb]", "ru": "платье"},
        {"fr": "porte", "tr": "[pɔrt]", "ru": "дверь"},
        {"fr": "fort", "tr": "[fɔr]", "ru": "сильный, -ая, -ое; крепкий, -ая, -ое"},
        {"fr": "la Sorbonne", "tr": "[sɔrbɔn]", "ru": "Сорбонна"},
        {"fr": "octobre", "tr": "[ɔktɔbr]", "ru": "октябрь"},
        {"fr": "police", "tr": "[pɔlis]", "ru": "полиция"},
        {"fr": "bonne", "tr": "[bɔn]", "ru": "хороший, -ая, -ое; вкусный, -ая, -ое"},
        {"fr": "école", "tr": "[ekɔl]", "ru": "школа"},
        {"fr": "téléphone", "tr": "[telefɔn]", "ru": "телефон"},
        {"fr": "notre", "tr": "[nɔtr]", "ru": "наш, наша, наше"},
        {"fr": "votre", "tr": "[vɔtr]", "ru": "ваш, ваша, ваше"},
        {"fr": "donner", "tr": "[dɔne]", "ru": "давать"},
        {"fr": "porter", "tr": "[pɔrte]", "ru": "носить"},
        {"fr": "sonner", "tr": "[sɔne]", "ru": "звонить"},
        {"fr": "apporter", "tr": "[apɔrte]", "ru": "приносить"},
        {"fr": "salade", "tr": "[salad]", "ru": "салат"},
        {"fr": "lettre", "tr": "[lɛtr]", "ru": "письмо"},
        {"fr": "veste", "tr": "[vɛst]", "ru": "куртка"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Слова со звуком [k]", "url": "/static/audio/lesson6_1.mp3"},
        {"title": "Упражнение №4: Слова со звуком [g]", "url": "/static/audio/lesson6_2.mp3"},
        {"title": "Упражнение №7: Слова со звуком [ɔ]", "url": "/static/audio/lesson6_3.mp3"},
        {"title": "Упражнение №2 и №5: Фразы для перевода", "url": "/static/audio/lesson6_4.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА И ПРАВИЛА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается буква 'c' в слове 'café'?",
         "options": ["[s]", "[k]", "[g]", "[ʃ]"], "correct": "[k]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как читается буква 'c' в слове 'pièce' (перед e)?",
         "options": ["[k]", "[s]", "[g]", "[ʃ]"], "correct": "[s]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как читается буквосочетание 'qu' в слове 'quatre'?",
         "options": ["[kw]", "[ku]", "[k]", "[g]"], "correct": "[k]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается буква 'x' в слове 'exact'?",
         "options": ["[gz]", "[ks]", "[z]", "[s]"], "correct": "[gz]"},
        {"id": 5, "type": "quiz", "question": "🔊 Как читается буква 'g' в слове 'gare'?",
         "options": ["[ʒ]", "[g]", "[k]", "[ʃ]"], "correct": "[g]"},
        {"id": 6, "type": "quiz", "question": "🔊 Как читается буквосочетание 'gu' в слове 'guerre'?",
         "options": ["[gy]", "[gu]", "[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 7, "type": "quiz", "question": "🔊 Как произносится французский звук [ɔ]?",
         "options": ["Как русский [о] с вытянутыми губами",
                     "Как русский [о] без призвука [у], губы не напрягать",
                     "Как [у]", "Как [а]"], "correct": "Как русский [о] без призвука [у], губы не напрягать"},
        {"id": 8, "type": "quiz", "question": "🔊 Как читается буква 'o' в слове 'pomme'?",
         "options": ["[o]", "[ɔ]", "[u]", "[ə]"], "correct": "[ɔ]"},

        # ========== УПРАЖНЕНИЕ №3: ТРАНСКРИПЦИЯ ==========
        {"id": 9, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'pièce'", "correct": "[pjɛs]"},
        {"id": 10, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'ciel'", "correct": "[sjɛl]"},
        {"id": 11, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'capitale'", "correct": "[kapital]"},
        {"id": 12, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'cahier'", "correct": "[kaje]"},
        {"id": 13, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'difficile'", "correct": "[difisil]"},
        {"id": 14, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'clair'", "correct": "[klɛr]"},
        {"id": 15, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'facile'", "correct": "[fasil]"},
        {"id": 16, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'caisse'", "correct": "[kɛs]"},
        {"id": 17, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'merci'", "correct": "[mersi]"},
        {"id": 18, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'cesser'", "correct": "[sese]"},

        # ========== УПРАЖНЕНИЕ №2: ПЕРЕВОД ФРАЗ ==========
        {"id": 19, "type": "text_input", "question": "📖 Переведите на русский: 'les articles'", "correct": "артикли"},
        {"id": 20, "type": "text_input", "question": "📖 Переведите на русский: 'quatre classes'", "correct": "четыре класса"},
        {"id": 21, "type": "text_input", "question": "📖 Переведите на русский: 'écrire vite'", "correct": "писать быстро"},
        {"id": 22, "type": "text_input", "question": "📖 Переведите на русский: 'quitter Paris'", "correct": "покидать Париж"},
        {"id": 23, "type": "text_input", "question": "📖 Переведите на русский: 'Pierre est calme'", "correct": "Пьер спокоен"},
        {"id": 24, "type": "text_input", "question": "📖 Переведите на русский: 'Quittez la clinique!'", "correct": "Покиньте клинику"},
        {"id": 25, "type": "text_input", "question": "📖 Переведите на русский: 'Qui est ta fille?'", "correct": "Кто твоя дочь"},

        # ========== УПРАЖНЕНИЕ №5: ПЕРЕВОД ФРАЗ ==========
        {"id": 26, "type": "text_input", "question": "📖 Переведите на русский: 'La gare est là'", "correct": "Вокзал там"},
        {"id": 27, "type": "text_input", "question": "📖 Переведите на русский: 'Yves est gai et Nana est grave'",
         "correct": "Ив веселый, а Нана серьезная"},
        {"id": 28, "type": "text_input", "question": "📖 Переведите на русский: 'Répétez la grammaire!'", "correct": "Повторите грамматику"},
        {"id": 29, "type": "text_input", "question": "📖 Переведите на русский: 'Gardez la gare!'", "correct": "Охраняйте вокзал"},
        {"id": 30, "type": "text_input", "question": "📖 Переведите на русский: 'Qui est Pierre? — Il est guide. Il travaille. Il est très fatigué.'",
         "correct": "Кто Пьер? — Он гид. Он работает. Он очень устал"},

        # ========== УПРАЖНЕНИЕ №8: ПЕРЕВОД ФРАЗ ==========
        {"id": 31, "type": "text_input", "question": "📖 Переведите на русский: 'porter la robe'", "correct": "носить платье"},
        {"id": 32, "type": "text_input", "question": "📖 Переведите на русский: 'apporter la salade'", "correct": "приносить салат"},
        {"id": 33, "type": "text_input", "question": "📖 Переведите на русский: 'fermer la porte'", "correct": "закрыть дверь"},
        {"id": 34, "type": "text_input", "question": "📖 Переведите на русский: 'notre école'", "correct": "наша школа"},
        {"id": 35, "type": "text_input", "question": "📖 Переведите на русский: 'votre ami'", "correct": "ваш друг"},
        {"id": 36, "type": "text_input", "question": "📖 Переведите на русский: 'La pomme est très bonne'", "correct": "Яблоко очень вкусное"},

        # ========== УПРАЖНЕНИЕ №9: ПЕРЕВОД С РУССКОГО ==========
        {"id": 37, "type": "text_input", "question": "🔄 Переведите на французский: 'приносить письма'", "correct": "apporter les lettres"},
        {"id": 38, "type": "text_input", "question": "🔄 Переведите на французский: 'носить куртки'", "correct": "porter les vestes"},
        {"id": 39, "type": "text_input", "question": "🔄 Переведите на французский: 'Закройте дверь!'", "correct": "Fermez la porte"},
        {"id": 40, "type": "text_input", "question": "🔄 Переведите на французский: 'Платье грязное'", "correct": "La robe est sale"},
        {"id": 41, "type": "text_input", "question": "🔄 Переведите на французский: 'Салат очень вкусный'", "correct": "La salade est très bonne"},
        {"id": 42, "type": "text_input", "question": "🔄 Переведите на французский: 'Наша школа там'", "correct": "Notre école est là"},
        {"id": 43, "type": "text_input", "question": "🔄 Переведите на французский: 'Принесите ваш товар!'", "correct": "Apportez votre article"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 44, "type": "quiz", "question": "📖 Как переводится 'gare'?",
         "options": ["Поезд", "Вокзал", "Улица", "Город"], "correct": "Вокзал"},
        {"id": 45, "type": "quiz", "question": "📖 Как переводится 'fatigué'?",
         "options": ["Счастливый", "Усталый", "Веселый", "Грустный"], "correct": "Усталый"},
        {"id": 46, "type": "quiz", "question": "📖 Как переводится 'pomme'?",
         "options": ["Груша", "Яблоко", "Апельсин", "Банан"], "correct": "Яблоко"},
        {"id": 47, "type": "quiz", "question": "📖 Как переводится 'porte'?",
         "options": ["Окно", "Дверь", "Стена", "Пол"], "correct": "Дверь"},
        {"id": 48, "type": "quiz", "question": "📖 Как переводится 'école'?",
         "options": ["Университет", "Школа", "Лицей", "Детский сад"], "correct": "Школа"},
        {"id": 49, "type": "quiz", "question": "📖 Как переводится 'notre'?",
         "options": ["Ваш", "Наш", "Их", "Твой"], "correct": "Наш"},
        {"id": 50, "type": "quiz", "question": "📖 Как переводится 'apporter'?",
         "options": ["Носить", "Приносить", "Брать", "Давать"], "correct": "Приносить"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 51, "type": "text_input", "question": "🔄 Напишите по-французски 'столица'", "correct": "capitale"},
        {"id": 52, "type": "text_input", "question": "🔄 Напишите по-французски 'ключ'", "correct": "clé"},
        {"id": 53, "type": "text_input", "question": "🔄 Напишите по-французски 'четыре'", "correct": "quatre"},
        {"id": 54, "type": "text_input", "question": "🔄 Напишите по-французски 'кто'", "correct": "qui"},
        {"id": 55, "type": "text_input", "question": "🔄 Напишите по-французски 'война'", "correct": "guerre"},
        {"id": 56, "type": "text_input", "question": "🔄 Напишите по-французски 'платье'", "correct": "robe"},
        {"id": 57, "type": "text_input", "question": "🔄 Напишите по-французски 'октябрь'", "correct": "octobre"},
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'телефон'", "correct": "téléphone"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'давать'", "correct": "donner"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'звонить'", "correct": "sonner"},

        # ========== ДОПОЛНИТЕЛЬНЫЕ СЛОВА ИЗ УРОКА ==========
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'кофе'", "correct": "café"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'спокойный'", "correct": "calme"},
        {"id": 63, "type": "text_input", "question": "🔄 Напишите по-французски 'писать'", "correct": "écrire"},
        {"id": 64, "type": "text_input", "question": "🔄 Напишите по-французски 'карта'", "correct": "carte"},
        {"id": 65, "type": "text_input", "question": "🔄 Напишите по-французски 'класс'", "correct": "classe"},
        {"id": 66, "type": "text_input", "question": "🔄 Напишите по-французски 'вокзал'", "correct": "gare"},
        {"id": 67, "type": "text_input", "question": "🔄 Напишите по-французски 'гид'", "correct": "guide"},
        {"id": 68, "type": "text_input", "question": "🔄 Напишите по-французски 'яблоко'", "correct": "pomme"},
        {"id": 69, "type": "text_input", "question": "🔄 Напишите по-французски 'мужчина'", "correct": "homme"},
        {"id": 70, "type": "text_input", "question": "🔄 Напишите по-французски 'школа'", "correct": "école"}
    ],
    "question": "Пройдите все 70 карточек практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 11: ЧТЕНИЕ (Глава I, Часть 3) ----------
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
# ---------- ДЕНЬ 12: ТЕСТ 3 (Уроки 5-6 / дни 9-10) ----------
COURSE_DAYS[12] = {
    "title": "Тест 3: Уроки 5-6 (Звуки [i], [j], [k], [g], [ɔ])",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        # ============================================================
        # ЧАСТЬ 1: ДИКТАНТ СЛОВ ИЗ УРОКА 5 (звуки [i], [j])
        # ============================================================
        {"id": 1, "type": "text_input", "question": "📝 Напишите по-французски: 'он'", "correct": "il"},
        {"id": 2, "type": "text_input", "question": "📝 Напишите по-французски: 'остров'", "correct": "île"},
        {"id": 3, "type": "text_input", "question": "📝 Напишите по-французски: 'идея'", "correct": "idée"},
        {"id": 4, "type": "text_input", "question": "📝 Напишите по-французски: 'здесь'", "correct": "ici"},
        {"id": 5, "type": "text_input", "question": "📝 Напишите по-французски: 'сын'", "correct": "fils"},
        {"id": 6, "type": "text_input", "question": "📝 Напишите по-французски: 'тип'", "correct": "type"},
        {"id": 7, "type": "text_input", "question": "📝 Напишите по-французски: 'быстро'", "correct": "vite"},
        {"id": 8, "type": "text_input", "question": "📝 Напишите по-французски: 'тысяча'", "correct": "mille"},
        {"id": 9, "type": "text_input", "question": "📝 Напишите по-французски: 'город'", "correct": "ville"},
        {"id": 10, "type": "text_input", "question": "📝 Напишите по-французски: 'семья'", "correct": "famille"},
        {"id": 11, "type": "text_input", "question": "📝 Напишите по-французски: 'дочь'", "correct": "fille"},
        {"id": 12, "type": "text_input", "question": "📝 Напишите по-французски: 'работа'", "correct": "travail"},
        {"id": 13, "type": "text_input", "question": "📝 Напишите по-французски: 'он работает'", "correct": "il travaille"},
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски: 'подробность'", "correct": "détail"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски: 'комната'", "correct": "pièce"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски: 'небо'", "correct": "ciel"},
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски: 'камень'", "correct": "pierre"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски: 'вчера'", "correct": "hier"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски: 'река'", "correct": "rivière"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски: 'женатый'", "correct": "marié"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски: 'замужняя'", "correct": "mariée"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски: 'зима'", "correct": "hiver"},
        {"id": 23, "type": "text_input", "question": "📝 Напишите по-французски: 'низкий'", "correct": "bas"},
        {"id": 24, "type": "text_input", "question": "📝 Напишите по-французски: 'молоко'", "correct": "lait"},
        {"id": 25, "type": "text_input", "question": "📝 Напишите по-французски: 'поздно'", "correct": "tard"},
        {"id": 26, "type": "text_input", "question": "📝 Напишите по-французски: 'после'", "correct": "après"},
        {"id": 27, "type": "text_input", "question": "📝 Напишите по-французски: 'очень'", "correct": "très"},
        {"id": 28, "type": "text_input", "question": "📝 Напишите по-французски: 'но'", "correct": "mais"},
        {"id": 29, "type": "text_input", "question": "📝 Напишите по-французски: 'они (м.р.)'", "correct": "ils"},
        {"id": 30, "type": "text_input", "question": "📝 Напишите по-французски: 'они (ж.р.)'", "correct": "elles"},

        # ============================================================
        # ЧАСТЬ 2: ДИКТАНТ СЛОВ ИЗ УРОКА 6 (звуки [k], [g], [ɔ])
        # ============================================================
        {"id": 31, "type": "text_input", "question": "📝 Напишите по-французски: 'кофе'", "correct": "café"},
        {"id": 32, "type": "text_input", "question": "📝 Напишите по-французски: 'спокойный'", "correct": "calme"},
        {"id": 33, "type": "text_input", "question": "📝 Напишите по-французски: 'столица'", "correct": "capitale"},
        {"id": 34, "type": "text_input", "question": "📝 Напишите по-французски: 'писать'", "correct": "écrire"},
        {"id": 35, "type": "text_input", "question": "📝 Напишите по-французски: 'карта'", "correct": "carte"},
        {"id": 36, "type": "text_input", "question": "📝 Напишите по-французски: 'класс'", "correct": "classe"},
        {"id": 37, "type": "text_input", "question": "📝 Напишите по-французски: 'ключ'", "correct": "clé"},
        {"id": 38, "type": "text_input", "question": "📝 Напишите по-французски: 'четыре'", "correct": "quatre"},
        {"id": 39, "type": "text_input", "question": "📝 Напишите по-французски: 'кто'", "correct": "qui"},
        {"id": 40, "type": "text_input", "question": "📝 Напишите по-французски: 'покидать'", "correct": "quitter"},
        {"id": 41, "type": "text_input", "question": "📝 Напишите по-французски: 'вокзал'", "correct": "gare"},
        {"id": 42, "type": "text_input", "question": "📝 Напишите по-французски: 'охранять'", "correct": "garder"},
        {"id": 43, "type": "text_input", "question": "📝 Напишите по-французски: 'веселый'", "correct": "gai"},
        {"id": 44, "type": "text_input", "question": "📝 Напишите по-французски: 'серьезный'", "correct": "grave"},
        {"id": 45, "type": "text_input", "question": "📝 Напишите по-французски: 'гид'", "correct": "guide"},
        {"id": 46, "type": "text_input", "question": "📝 Напишите по-французски: 'война'", "correct": "guerre"},
        {"id": 47, "type": "text_input", "question": "📝 Напишите по-французски: 'выздоравливать'", "correct": "guérir"},
        {"id": 48, "type": "text_input", "question": "📝 Напишите по-французски: 'грамматика'", "correct": "grammaire"},
        {"id": 49, "type": "text_input", "question": "📝 Напишите по-французски: 'зеркало'", "correct": "glace"},
        {"id": 50, "type": "text_input", "question": "📝 Напишите по-французски: 'усталый'", "correct": "fatigué"},
        {"id": 51, "type": "text_input", "question": "📝 Напишите по-французски: 'точный'", "correct": "exact"},
        {"id": 52, "type": "text_input", "question": "📝 Напишите по-французски: 'яблоко'", "correct": "pomme"},
        {"id": 53, "type": "text_input", "question": "📝 Напишите по-французски: 'мужчина'", "correct": "homme"},
        {"id": 54, "type": "text_input", "question": "📝 Напишите по-французски: 'платье'", "correct": "robe"},
        {"id": 55, "type": "text_input", "question": "📝 Напишите по-французски: 'дверь'", "correct": "porte"},
        {"id": 56, "type": "text_input", "question": "📝 Напишите по-французски: 'октябрь'", "correct": "octobre"},
        {"id": 57, "type": "text_input", "question": "📝 Напишите по-французски: 'школа'", "correct": "école"},
        {"id": 58, "type": "text_input", "question": "📝 Напишите по-французски: 'телефон'", "correct": "téléphone"},
        {"id": 59, "type": "text_input", "question": "📝 Напишите по-французски: 'наш'", "correct": "notre"},
        {"id": 60, "type": "text_input", "question": "📝 Напишите по-французски: 'ваш'", "correct": "votre"},
        {"id": 61, "type": "text_input", "question": "📝 Напишите по-французски: 'давать'", "correct": "donner"},
        {"id": 62, "type": "text_input", "question": "📝 Напишите по-французски: 'носить'", "correct": "porter"},
        {"id": 63, "type": "text_input", "question": "📝 Напишите по-французски: 'звонить'", "correct": "sonner"},
        {"id": 64, "type": "text_input", "question": "📝 Напишите по-французски: 'приносить'", "correct": "apporter"},

        # ============================================================
        # ЧАСТЬ 3: ФОНЕТИКА И ПРАВИЛА (quiz)
        # ============================================================
        {"id": 65, "type": "quiz", "question": "🔊 Как правильно произносится французский звук [i]?",
         "options": ["Как русский [и], без изменений", "С оттянутыми уголками рта, 'улыбчиво'",
                     "С округленными губами", "Как [ы]"], "correct": "С оттянутыми уголками рта, 'улыбчиво'"},
        {"id": 66, "type": "quiz", "question": "🔊 Как читается слово 'fils' (сын)?",
         "options": ["[fils]", "[fil]", "[fis]", "[fi]"], "correct": "[fis]"},
        {"id": 67, "type": "quiz", "question": "🔊 Как читается буквосочетание 'ill' в слове 'famille'?",
         "options": ["[il]", "[ij]", "[j]", "[ilj]"], "correct": "[j]"},
        {"id": 68, "type": "quiz", "question": "🔇 Читается ли буква 'h' во французском?",
         "options": ["Да, всегда", "Нет, никогда", "Только в начале слов", "Только в конце слов"],
         "correct": "Нет, никогда"},
        {"id": 69, "type": "quiz", "question": "🔇 Какие согласные на конце слов обычно НЕ читаются?",
         "options": ["p, b, m", "s, t, d", "c, g, f", "l, r, n"], "correct": "s, t, d"},
        {"id": 70, "type": "quiz", "question": "🔊 Как читается буква 'c' в слове 'café'?",
         "options": ["[s]", "[k]", "[g]", "[ʃ]"], "correct": "[k]"},
        {"id": 71, "type": "quiz", "question": "🔊 Как читается буква 'c' в слове 'pièce' (перед e)?",
         "options": ["[k]", "[s]", "[g]", "[ʃ]"], "correct": "[s]"},
        {"id": 72, "type": "quiz", "question": "🔊 Как читается буквосочетание 'qu' в слове 'quatre'?",
         "options": ["[kw]", "[ku]", "[k]", "[g]"], "correct": "[k]"},
        {"id": 73, "type": "quiz", "question": "🔊 Как читается буква 'g' в слове 'gare'?",
         "options": ["[ʒ]", "[g]", "[k]", "[ʃ]"], "correct": "[g]"},
        {"id": 74, "type": "quiz", "question": "🔊 Как читается буква 'o' в слове 'pomme'?",
         "options": ["[o]", "[ɔ]", "[u]", "[ə]"], "correct": "[ɔ]"},

        # ============================================================
        # ЧАСТЬ 4: ТРАНСКРИПЦИЯ (text_input)
        # ============================================================
        {"id": 75, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'merci'", "correct": "[mersi]"},
        {"id": 76, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'triste'", "correct": "[trist]"},
        {"id": 77, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'hiver'", "correct": "[ivɛr]"},
        {"id": 78, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'famille'", "correct": "[famij]"},
        {"id": 79, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'travail'", "correct": "[travaj]"},
        {"id": 80, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'café'", "correct": "[kafe]"},
        {"id": 81, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'quatre'", "correct": "[katr]"},
        {"id": 82, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'gare'", "correct": "[gar]"},
        {"id": 83, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'pomme'", "correct": "[pɔm]"},
        {"id": 84, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'école'", "correct": "[ekɔl]"},

        # ============================================================
        # ЧАСТЬ 5: ПЕРЕВОД ФРАЗ (text_input)
        # ============================================================
        {"id": 85, "type": "text_input", "question": "📖 Переведите на русский: 'cette idée'", "correct": "эта идея"},
        {"id": 86, "type": "text_input", "question": "📖 Переведите на русский: 'il est libre'", "correct": "он свободен"},
        {"id": 87, "type": "text_input", "question": "📖 Переведите на русский: 'mes amies'", "correct": "мои подруги"},
        {"id": 88, "type": "text_input", "question": "📖 Переведите на русский: 'Paris est là'", "correct": "Париж находится там"},
        {"id": 89, "type": "text_input", "question": "📖 Переведите на русский: 'faire vite'", "correct": "делать быстро"},
        {"id": 90, "type": "text_input", "question": "📖 Переведите на русский: 'lire et rire'", "correct": "читать и смеяться"},
        {"id": 91, "type": "text_input", "question": "📖 Переведите на русский: 'Elle travaille'", "correct": "Она работает"},
        {"id": 92, "type": "text_input", "question": "📖 Переведите на русский: 'Ma famille est là'", "correct": "Моя семья там"},
        {"id": 93, "type": "text_input", "question": "📖 Переведите на русский: 'Les articles'", "correct": "Артикли"},
        {"id": 94, "type": "text_input", "question": "📖 Переведите на русский: 'Qui est ta fille?'", "correct": "Кто твоя дочь"},
        {"id": 95, "type": "text_input", "question": "📖 Переведите на русский: 'La gare est là'", "correct": "Вокзал там"},
        {"id": 96, "type": "text_input", "question": "📖 Переведите на русский: 'Notre école'", "correct": "Наша школа"},
        {"id": 97, "type": "text_input", "question": "📖 Переведите на русский: 'La pomme est très bonne'", "correct": "Яблоко очень вкусное"},

        # ============================================================
        # ЧАСТЬ 6: ПЕРЕВОД С РУССКОГО (text_input)
        # ============================================================
        {"id": 98, "type": "text_input", "question": "🔄 Переведите на французский: 'его книги'", "correct": "ses livres"},
        {"id": 99, "type": "text_input", "question": "🔄 Переведите на французский: 'Ив свободен'", "correct": "Yves est libre"},
        {"id": 100, "type": "text_input", "question": "🔄 Переведите на французский: 'Он работает здесь'", "correct": "Il travaille ici"},
        {"id": 101, "type": "text_input", "question": "🔄 Переведите на французский: 'Закройте дверь!'", "correct": "Fermez la porte"},
        {"id": 102, "type": "text_input", "question": "🔄 Переведите на французский: 'Приносить письма'", "correct": "apporter les lettres"},
        {"id": 103, "type": "text_input", "question": "🔄 Переведите на французский: 'Наша школа там'", "correct": "Notre école est là"}
    ],
    "question": "Пройдите все 103 вопроса теста!",
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