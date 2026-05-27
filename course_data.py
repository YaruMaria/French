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
# ---------- ДЕНЬ 13: УРОК 7 (Звуки [œ], [ə], беглое e) ----------
COURSE_DAYS[13] = {
    "title": "Урок 7: Звуки [œ], [ə] и беглое e",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "гласный [œ]",
            "russian": "отсутствует",
            "letters": "eu<br>œu",
            "notes": "• Буквосочетания eu, œu читаются как [œ] перед всеми произносимыми согласными, кроме z.<br>• 'Дыхните' на очки, зафиксируйте губы, произнесите [ɛ] — получится [œ]!<br>• Не ориентируйтесь на русскую букву ё!"
        },
        {
            "sound": "гласный [ə] (беглый)",
            "russian": "отсутствует",
            "letters": "e",
            "notes": "• Тот же звук, что [œ], но никогда не удлиняется.<br>• Читается в односложных словах: le, ce, de.<br>• На конце слова после двух согласных перед другим словом.<br>• В быстрой речи может выпадать."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "🎯 Как произнести звук [œ]",
            "text": "1️⃣ 'Дыхните' на воображаемые стекла очков — губы займут правильное положение.<br>"
                    "2️⃣ Зафиксируйте это положение губ.<br>"
                    "3️⃣ Не меняя положения губ, произнесите звук [ɛ].<br><br>"
                    "Получится французский [œ]!<br>"
                    "⚠️ Не ориентируйтесь на русское ё: souffleur [suflœr] ≠ суфлёр!"
        },
        {
            "subtitle": "📝 Беглое [ə] (e muet)",
            "text": "Звук [ə] читается:<br><br>"
                    "• В односложных служебных словах: <b>le [lə], ce [sə], de [də]</b><br>"
                    "• На конце слова после двух согласных перед другим словом: <b>le livre de Pierre [ləlivrədəpjɛr]</b><br>"
                    "• В безударном слоге в неодносложном слове: <b>première [prəmjɛr], petite [pətit]</b><br><br>"
                    "В быстрой речи [ə] может выпадать между согласными, окруженными гласными.<br>"
                    "Пример: <b>samedi [samdi]</b> (вместо [samədi])"
        },
        {
            "subtitle": "📚 Определенный артикль и предлог de",
            "text": "• <b>le [lə]</b> — определенный артикль мужского рода единственного числа<br>"
                    "• <b>ce [sə]</b> — этот, эта, это (мужской род)<br>"
                    "• <b>de [də]</b> — предлог принадлежности: <b>la malle de Pierre</b> — чемодан Пьера"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Прочитайте. Затем послушайте и повторите:",
            "text": "• [te – tœ], [se – sœ], [me – mœ], [ke – kœ]<br>"
                    "• [ɛr – œr], [lɛr – lœr], [mɛr – mœr], [tɛr – tœr]"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочтите и выучите:",
            "text": "• heure [œr] — час<br>"
                    "• leur [lœr] — их<br>"
                    "• beurre [bœr] — масло<br>"
                    "• sœur [sœr] — сестра<br>"
                    "• cœur [kœr] — сердце<br>"
                    "• fleur [flœr] — цветок<br>"
                    "• peur [pœr] — страх<br>"
                    "• elle a des amies [ɛl a dez ami] — у нее есть подруги<br>"
                    "• il a peur [il a pœr] — он боится<br>"
                    "• directeur [dirɛktœr] — директор<br>"
                    "• il pleure [il plœr] — он плачет<br>"
                    "• il pleut [il plø] — идет дождь<br>"
                    "• a — имеет"
        },
        {
            "subtitle": "🎧 Упражнение № 4. Прочтите и запомните:",
            "text": "a) Односложные служебные слова:<br>"
                    "• le [lə] — определенный артикль мужского рода<br>"
                    "• ce [sə] — этот, эта, это (м.р.)<br>"
                    "• de [də] — предлог принадлежности<br><br>"
                    "b) Существительные (запомните род):<br>"
                    "• le ciel — небо<br>"
                    "• le détail — подробность<br>"
                    "• ce rêve — эта мечта<br>"
                    "• ce travail — эта работа<br>"
                    "• le livre — книга<br>"
                    "• le café — кафе, кофе<br>"
                    "• le cœur — сердце<br>"
                    "• ce guide — этот гид<br>"
                    "• ce verre — этот стакан<br>"
                    "• le frère de Pierre — брат Пьера<br>"
                    "• le stade — стадион<br>"
                    "• le père de Nana — отец Наны"
        },
        {
            "subtitle": "🎧 Упражнение № 7. Прочтите и запомните новые слова:",
            "text": "• première [prəmjɛr] — первый, -ая, -ое (ж.р.)<br>"
                    "• petite [pətit] — маленький, -ая, -ое (ж.р.)<br>"
                    "• regarder [rəgarde] — смотреть<br>"
                    "• mercredi [mɛrkrədi] — среда"
        }
    ],
    "vocabulary": [
        {"fr": "heure", "tr": "[œr]", "ru": "час"},
        {"fr": "leur", "tr": "[lœr]", "ru": "их"},
        {"fr": "beurre", "tr": "[bœr]", "ru": "масло"},
        {"fr": "sœur", "tr": "[sœr]", "ru": "сестра"},
        {"fr": "cœur", "tr": "[kœr]", "ru": "сердце"},
        {"fr": "fleur", "tr": "[flœr]", "ru": "цветок"},
        {"fr": "peur", "tr": "[pœr]", "ru": "страх"},
        {"fr": "directeur", "tr": "[dirɛktœr]", "ru": "директор"},
        {"fr": "il pleure", "tr": "[il plœr]", "ru": "он плачет"},
        {"fr": "il pleut", "tr": "[il plø]", "ru": "идет дождь"},
        {"fr": "il a peur", "tr": "[il a pœr]", "ru": "он боится"},
        {"fr": "elle a", "tr": "[ɛl a]", "ru": "у нее есть"},
        {"fr": "le", "tr": "[lə]", "ru": "определенный артикль м.р."},
        {"fr": "ce", "tr": "[sə]", "ru": "этот, эта, это (м.р.)"},
        {"fr": "de", "tr": "[də]", "ru": "предлог принадлежности"},
        {"fr": "le ciel", "tr": "[lə sjɛl]", "ru": "небо"},
        {"fr": "le détail", "tr": "[lə detaj]", "ru": "подробность"},
        {"fr": "ce rêve", "tr": "[sə rɛv]", "ru": "эта мечта"},
        {"fr": "ce travail", "tr": "[sə travaj]", "ru": "эта работа"},
        {"fr": "le livre", "tr": "[lə livr]", "ru": "книга"},
        {"fr": "le café", "tr": "[lə kafe]", "ru": "кафе, кофе"},
        {"fr": "le cœur", "tr": "[lə kœr]", "ru": "сердце"},
        {"fr": "ce guide", "tr": "[sə gid]", "ru": "этот гид"},
        {"fr": "ce verre", "tr": "[sə vɛr]", "ru": "этот стакан"},
        {"fr": "le frère de Pierre", "tr": "[lə frɛr də pjɛr]", "ru": "брат Пьера"},
        {"fr": "le stade", "tr": "[lə stad]", "ru": "стадион"},
        {"fr": "le père de Nana", "tr": "[lə pɛr də nana]", "ru": "отец Наны"},
        {"fr": "première", "tr": "[prəmjɛr]", "ru": "первая"},
        {"fr": "petite", "tr": "[pətit]", "ru": "маленькая"},
        {"fr": "regarder", "tr": "[rəgarde]", "ru": "смотреть"},
        {"fr": "mercredi", "tr": "[mɛrkrədi]", "ru": "среда"},
        {"fr": "samedi", "tr": "[samdi]", "ru": "суббота"},
        {"fr": "le bracelet", "tr": "[lə braslɛ]", "ru": "браслет"},
        {"fr": "la fenêtre", "tr": "[la fənɛtr]", "ru": "окно"},
        {"fr": "ma petite", "tr": "[ma pətit]", "ru": "моя маленькая"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Звуки [ɛ] и [œ]", "url": "/static/audio/lesson7_1.mp3"},
        {"title": "Упражнение №2: Слова со звуком [œ]", "url": "/static/audio/lesson7_2.mp3"},
        {"title": "Упражнение №4: Служебные слова", "url": "/static/audio/lesson7_3.mp3"},
        {"title": "Упражнение №7: Беглое e", "url": "/static/audio/lesson7_4.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается буквосочетание 'eu' в слове 'fleur'?",
         "options": ["[ø]", "[œ]", "[ə]", "[y]"], "correct": "[œ]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как правильно произнести звук [œ]?",
         "options": ["Как русское ё", "Как [ɛ] с округленными губами", "Как [o]", "Как [u]"], "correct": "Как [ɛ] с округленными губами"},
        {"id": 3, "type": "quiz", "question": "🔊 Как читается артикль 'le'?",
         "options": ["[le]", "[lə]", "[lɛ]", "[lœ]"], "correct": "[lə]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается предлог 'de'?",
         "options": ["[de]", "[də]", "[dɛ]", "[dœ]"], "correct": "[də]"},
        {"id": 5, "type": "quiz", "question": "🔊 Как читается слово 'première'?",
         "options": ["[premjɛr]", "[prəmjɛr]", "[prɛmjɛr]", "[pʁemjɛr]"], "correct": "[prəmjɛr]"},
        {"id": 6, "type": "quiz", "question": "🔊 Почему звук [ə] называется 'беглым'?",
         "options": ["Он всегда произносится", "Он может выпадать в речи", "Он всегда ударный", "Он читается как [e]"], "correct": "Он может выпадать в речи"},

        # ========== УПРАЖНЕНИЕ №3: ПЕРЕВОД ФРАЗ ==========
        {"id": 7, "type": "text_input", "question": "📖 Переведите на русский: 'Il a quatre filles'", "correct": "У него четыре дочери"},
        {"id": 8, "type": "text_input", "question": "📖 Переведите на русский: 'La fleur est très belle'", "correct": "Цветок очень красивый"},
        {"id": 9, "type": "text_input", "question": "📖 Переведите на русский: 'Nana est malade. Elle a peur. Elle pleure.'", "correct": "Нана больна. Она боится. Она плачет"},
        {"id": 10, "type": "text_input", "question": "📖 Переведите на русский: 'Ma sœur travaille. Elle est directeur.'", "correct": "Моя сестра работает. Она директор"},

        # ========== УПРАЖНЕНИЕ №5: ПЕРЕВОД ФРАЗ ==========
        {"id": 11, "type": "text_input", "question": "📖 Переведите на русский: 'le fils de ma sœur'", "correct": "сын моей сестры"},
        {"id": 12, "type": "text_input", "question": "📖 Переведите на русский: 'le travail de ma fille'", "correct": "работа моей дочери"},
        {"id": 13, "type": "text_input", "question": "📖 Переведите на русский: 'le cœur de la capitale'", "correct": "сердце столицы"},
        {"id": 14, "type": "text_input", "question": "📖 Переведите на русский: 'Fermez ce livre!'", "correct": "Закройте эту книгу"},
        {"id": 15, "type": "text_input", "question": "📖 Переведите на русский: 'Apportez le café et le verre!'", "correct": "Принесите кофе и стакан"},
        {"id": 16, "type": "text_input", "question": "📖 Переведите на русский: 'Quittez le stade!'", "correct": "Покиньте стадион"},

        # ========== УПРАЖНЕНИЕ №6: ПЕРЕВОД ФРАЗ ==========
        {"id": 17, "type": "text_input", "question": "📖 Переведите на русский: 'le livre de Pierre'", "correct": "книга Пьера"},
        {"id": 18, "type": "text_input", "question": "📖 Переведите на русский: 'il a quatre filles'", "correct": "у него четыре дочери"},
        {"id": 19, "type": "text_input", "question": "📖 Переведите на русский: 'les vestes sales'", "correct": "грязные куртки"},

        # ========== УПРАЖНЕНИЕ №8: ЗАПОЛНИТЕ ПРОПУСКИ ==========
        {"id": 20, "type": "text_input", "question": "✍️ Заполните пропуск: 'Répétez ______ adresse!' (leur)", "correct": "leur"},
        {"id": 21, "type": "text_input", "question": "✍️ Заполните пропуск: 'La robe de votre ______ est très belle.' (sœur)", "correct": "sœur"},
        {"id": 22, "type": "text_input", "question": "✍️ Заполните пропуск: 'La ______ est petite: le père, la mère et leur fils.' (famille)", "correct": "famille"},
        {"id": 23, "type": "text_input", "question": "✍️ Заполните пропуск: 'Regardez! La rivière ______ là.' (est)", "correct": "est"},

        # ========== УПРАЖНЕНИЕ №10: ПЕРЕВОД ФРАЗ ==========
        {"id": 24, "type": "text_input", "question": "📖 Переведите на русский: 'Le bracelet de ma petite sœur est ici.'", "correct": "Браслет моей маленькой сестры здесь"},
        {"id": 25, "type": "text_input", "question": "📖 Переведите на русский: 'Arrivez samedi et restez à Paris!'", "correct": "Приезжайте в субботу и оставайтесь в Париже"},
        {"id": 26, "type": "text_input", "question": "📖 Переведите на русский: 'Il a peur de fermer sa fenêtre.'", "correct": "Он боится закрыть свое окно"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 27, "type": "quiz", "question": "📖 Как переводится 'sœur'?",
         "options": ["Брат", "Сестра", "Мать", "Отец"], "correct": "Сестра"},
        {"id": 28, "type": "quiz", "question": "📖 Как переводится 'cœur'?",
         "options": ["Кровь", "Сердце", "Голова", "Рука"], "correct": "Сердце"},
        {"id": 29, "type": "quiz", "question": "📖 Как переводится 'peur'?",
         "options": ["Радость", "Страх", "Грусть", "Гнев"], "correct": "Страх"},
        {"id": 30, "type": "quiz", "question": "📖 Что означает 'il pleure'?",
         "options": ["Он смеется", "Он плачет", "Он боится", "Он спит"], "correct": "Он плачет"},
        {"id": 31, "type": "quiz", "question": "📖 Что означает 'il pleut'?",
         "options": ["Идет снег", "Идет дождь", "Ветрено", "Солнечно"], "correct": "Идет дождь"},
        {"id": 32, "type": "quiz", "question": "📖 Как переводится 'directeur'?",
         "options": ["Учитель", "Директор", "Врач", "Инженер"], "correct": "Директор"},

        # ========== ПЕРЕВОД С РУССКОГО (слова, text_input) ==========
        {"id": 33, "type": "text_input", "question": "🔄 Напишите по-французски 'час'", "correct": "heure"},
        {"id": 34, "type": "text_input", "question": "🔄 Напишите по-французски 'масло'", "correct": "beurre"},
        {"id": 35, "type": "text_input", "question": "🔄 Напишите по-французски 'цветок'", "correct": "fleur"},
        {"id": 36, "type": "text_input", "question": "🔄 Напишите по-французски 'страх'", "correct": "peur"},
        {"id": 37, "type": "text_input", "question": "🔄 Напишите по-французски 'он боится'", "correct": "il a peur"},
        {"id": 38, "type": "text_input", "question": "🔄 Напишите по-французски 'он плачет'", "correct": "il pleure"},
        {"id": 39, "type": "text_input", "question": "🔄 Напишите по-французски 'идет дождь'", "correct": "il pleut"},
        {"id": 40, "type": "text_input", "question": "🔄 Напишите по-французски 'сестра'", "correct": "sœur"},
        {"id": 41, "type": "text_input", "question": "🔄 Напишите по-французски 'сердце'", "correct": "cœur"},

        # ========== ПЕРЕВОД С РУССКОГО (фразы, text_input) ==========
        {"id": 42, "type": "text_input", "question": "🔄 Переведите на французский: 'У него есть подруги'", "correct": "Il a des amies"},
        {"id": 43, "type": "text_input", "question": "🔄 Переведите на французский: 'Закройте эту книгу!'", "correct": "Fermez ce livre"},
        {"id": 44, "type": "text_input", "question": "🔄 Переведите на французский: 'Принесите кофе!'", "correct": "Apportez le café"},
        {"id": 45, "type": "text_input", "question": "🔄 Переведите на французский: 'Браслет моей маленькой сестры'", "correct": "Le bracelet de ma petite sœur"},
        {"id": 46, "type": "text_input", "question": "🔄 Переведите на французский: 'Приезжайте в субботу'", "correct": "Arrivez samedi"},
        {"id": 47, "type": "text_input", "question": "🔄 Переведите на французский: 'Он боится закрыть окно'", "correct": "Il a peur de fermer la fenêtre"}
    ],
    "question": "Пройдите все 47 карточек практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 14: УРОК 8 ----------
# ---------- ДЕНЬ 14: УРОК 8 (Звуки [ʃ], [ʒ] и долгий [a:]) ----------
COURSE_DAYS[14] = {
    "title": "Урок 8: Звуки [ʃ], [ʒ] и долгий гласный [a:]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "согласный [ʃ]",
            "russian": "[ш] как в слове меньше, но мягче и короче",
            "letters": "ch",
            "notes": "• Буквосочетание ch читается как [ʃ].<br>• Французский [ʃ] мягче русского [ш] и примерно вдвое короче.<br>• Пример: chaise [ʃɛz] — стул."
        },
        {
            "sound": "согласный [ʒ]",
            "russian": "[ж] как в слове ближний, но мягче и короче",
            "letters": "G, g (перед e, i, y)<br>J, j",
            "notes": "• Буква g читается как [ʒ] перед e, i, y.<br>• Буква j читается как [ʒ] во всех позициях.<br>• Если слово оканчивается на [ʒ], ударный гласный удлиняется.<br>• Пример: visage [vizaːʒ] — лицо."
        },
        {
            "sound": "гласный [a:] (долгий)",
            "russian": "[а] как в слове бак, но вдвое длиннее",
            "letters": "Â, â<br>À, à (в некоторых случаях)",
            "notes": "• Буква â читается как долгий [a:].<br>• Звук теряет долготу в конце слова.<br>• Пример: gare [ga:r] — вокзал, pâle [pa:l] — бледный."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "📝 Правила чтения буквы G",
            "text": "Буква <b>G</b> читается по-разному в зависимости от следующей гласной:<br><br>"
                    "• <b>G → [g]</b> перед a, o, u: <b>gare, garder</b><br>"
                    "• <b>G → [ʒ]</b> перед e, i, y: <b>général, geste, gymnastique</b><br>"
                    "• Буквосочетание <b>gu → [g]</b> (u не читается): <b>guerre</b>"
        },
        {
            "subtitle": "📝 Род французских существительных",
            "text": "В словарях французского языка род обозначается:<br>"
                    "<b>m</b> — masculin (мужской род)<br>"
                    "<b>f</b> — féminin (женский род)<br><br>"
                    "Примеры: <b>livre m</b> — книга (в русском женский род!)<br>"
                    "<b>chaise f</b> — стул (в русском мужской род!)<br><br>"
                    "⚠️ Запоминайте род французских слов — он часто не совпадает с русским!"
        },
        {
            "subtitle": "⏳ Долгий гласный [a:]",
            "text": "Французский звук [a:] примерно вдвое длиннее русского [а].<br><br>"
                    "Сравните:<br>"
                    "• <b>patte [pat]</b> — лапа (краткий)<br>"
                    "• <b>pâte [pa:t]</b> — тесто (долгий)<br><br>"
                    "• <b>mal [mal]</b> — боль (краткий)<br>"
                    "• <b>mâle [ma:l]</b> — самец (долгий)"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Прочтите, стараясь запомнить слова:",
            "text": "• la chaise [la ʃɛz] — стул<br>"
                    "• marcher [marʃe] — ходить, шагать<br>"
                    "• chaque [ʃak] — каждый, -ая, -ое<br>"
                    "• cher [ʃɛr] — дорогой (м.р.)<br>"
                    "• chère [ʃɛr] — дорогая (ж.р.)<br>"
                    "• cacher [kaʃe] — прятать<br>"
                    "• chercher [ʃɛrʃe] — искать"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочтите и проследите, как образуется форма глагола:",
            "text": "• travailler [travaje] — il travaille [il travaj] — он работает<br>"
                    "• arriver [arive] — elle arrive [ɛl ariv] — она приезжает<br>"
                    "• parler [parle] — il parle [il parl] — он говорит<br>"
                    "• chercher [ʃɛrʃe] — elle cherche [ɛl ʃɛrʃ] — она ищет<br>"
                    "• cacher [kaʃe] — il cache [il kaʃ] — он прячет<br>"
                    "• marcher [marʃe] — elle marche [ɛl marʃ] — она шагает"
        },
        {
            "subtitle": "🎧 Упражнение № 5. Запомните новые слова:",
            "text": "• général [ʒeneral] m — генерал<br>"
                    "• geste [ʒɛst] m — жест<br>"
                    "• Gérard [ʒerar] — Жерар (имя)<br>"
                    "• gymnastique [ʒimnastik] f — гимнастика, зарядка<br>"
                    "• je [ʒə] — я<br>"
                    "• jamais [ʒamɛ] — никогда<br>"
                    "• jeudi [ʒødi] m — четверг<br>"
                    "• jeter [ʒəte] — бросать<br>"
                    "• jeune [ʒœn] — молодой<br>"
                    "• déjeuner [deʒœne] — обедать<br><br>"
                    "⚠️ Если слово оканчивается на [ʒ], ударный гласный удлиняется:<br>"
                    "• visage [vizaːʒ] m — лицо"
        },
        {
            "subtitle": "🎧 Упражнение № 8. Прочтите:",
            "text": "а) С долгим [a:]:<br>"
                    "• âge [aːʒ] m — возраст<br>"
                    "• bâtir [baːtir] — строить<br>"
                    "• grâce [graːs] f — грация<br>"
                    "• pâle [paːl] — бледный<br>"
                    "• théâtre [teɑːtr] m — театр<br><br>"
                    "б) Сравните долготу и краткость:<br>"
                    "• patte [pat] f — лапа ↔ pâte [paːt] f — тесто<br>"
                    "• ma [ma] — моя ↔ mât [maː] m — мачта<br>"
                    "• mal [mal] m — боль ↔ mâle [maːl] m — самец"
        }
    ],
    "vocabulary": [
        {"fr": "chaise", "tr": "[ʃɛz]", "ru": "стул (ж.р.)"},
        {"fr": "marcher", "tr": "[marʃe]", "ru": "ходить, шагать"},
        {"fr": "chaque", "tr": "[ʃak]", "ru": "каждый, каждая"},
        {"fr": "cher", "tr": "[ʃɛr]", "ru": "дорогой (м.р.)"},
        {"fr": "chère", "tr": "[ʃɛr]", "ru": "дорогая (ж.р.)"},
        {"fr": "cacher", "tr": "[kaʃe]", "ru": "прятать"},
        {"fr": "chercher", "tr": "[ʃɛrʃe]", "ru": "искать"},
        {"fr": "travailler", "tr": "[travaje]", "ru": "работать"},
        {"fr": "il travaille", "tr": "[il travaj]", "ru": "он работает"},
        {"fr": "arriver", "tr": "[arive]", "ru": "приезжать"},
        {"fr": "elle arrive", "tr": "[ɛl ariv]", "ru": "она приезжает"},
        {"fr": "parler", "tr": "[parle]", "ru": "говорить"},
        {"fr": "il parle", "tr": "[il parl]", "ru": "он говорит"},
        {"fr": "elle cherche", "tr": "[ɛl ʃɛrʃ]", "ru": "она ищет"},
        {"fr": "il cache", "tr": "[il kaʃ]", "ru": "он прячет"},
        {"fr": "elle marche", "tr": "[ɛl marʃ]", "ru": "она шагает"},
        {"fr": "général", "tr": "[ʒeneral]", "ru": "генерал (м.р.)"},
        {"fr": "geste", "tr": "[ʒɛst]", "ru": "жест (м.р.)"},
        {"fr": "Gérard", "tr": "[ʒerar]", "ru": "Жерар"},
        {"fr": "gymnastique", "tr": "[ʒimnastik]", "ru": "гимнастика (ж.р.)"},
        {"fr": "je", "tr": "[ʒə]", "ru": "я"},
        {"fr": "jamais", "tr": "[ʒamɛ]", "ru": "никогда"},
        {"fr": "jeudi", "tr": "[ʒødi]", "ru": "четверг (м.р.)"},
        {"fr": "jeter", "tr": "[ʒəte]", "ru": "бросать"},
        {"fr": "jeune", "tr": "[ʒœn]", "ru": "молодой"},
        {"fr": "déjeuner", "tr": "[deʒœne]", "ru": "обедать"},
        {"fr": "visage", "tr": "[vizaːʒ]", "ru": "лицо (м.р.)"},
        {"fr": "fromage", "tr": "[frɔmaːʒ]", "ru": "сыр (м.р.)"},
        {"fr": "sage", "tr": "[saːʒ]", "ru": "послушный, мудрый"},
        {"fr": "neige", "tr": "[nɛːʒ]", "ru": "снег (ж.р.)"},
        {"fr": "âge", "tr": "[aːʒ]", "ru": "возраст (м.р.)"},
        {"fr": "collège", "tr": "[kɔlɛːʒ]", "ru": "колледж (м.р.)"},
        {"fr": "étage", "tr": "[etaːʒ]", "ru": "этаж (м.р.)"},
        {"fr": "plage", "tr": "[plaːʒ]", "ru": "пляж (ж.р.)"},
        {"fr": "bagage", "tr": "[bagaːʒ]", "ru": "багаж (м.р.)"},
        {"fr": "image", "tr": "[imaːʒ]", "ru": "изображение (ж.р.)"},
        {"fr": "pâte", "tr": "[paːt]", "ru": "тесто (ж.р.)"},
        {"fr": "patte", "tr": "[pat]", "ru": "лапа (ж.р.)"},
        {"fr": "mât", "tr": "[maː]", "ru": "мачта (м.р.)"},
        {"fr": "mâle", "tr": "[maːl]", "ru": "самец (м.р.)"},
        {"fr": "pâle", "tr": "[paːl]", "ru": "бледный"},
        {"fr": "grâce", "tr": "[graːs]", "ru": "грация (ж.р.)"},
        {"fr": "théâtre", "tr": "[teɑtr]", "ru": "театр (м.р.)"},
        {"fr": "bâtir", "tr": "[batir]", "ru": "строить"},
        {"fr": "Charles", "tr": "[ʃarl]", "ru": "Шарль"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Звук [ʃ]", "url": "/static/audio/lesson8_1.mp3"},
        {"title": "Упражнение №5: Звук [ʒ]", "url": "/static/audio/lesson8_2.mp3"},
        {"title": "Упражнение №8: Долгий [a:]", "url": "/static/audio/lesson8_3.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается буквосочетание 'ch' во французском?",
         "options": ["[k]", "[ʃ]", "[tʃ]", "[ç]"], "correct": "[ʃ]"},
        {"id": 2, "type": "quiz", "question": "🔊 Когда буква 'g' читается как [ʒ]?",
         "options": ["Перед a, o, u", "Перед e, i, y", "В конце слова", "Перед согласными"], "correct": "Перед e, i, y"},
        {"id": 3, "type": "quiz", "question": "🔊 Как читается буква 'j' во французском?",
         "options": ["[ʒ]", "[j]", "[dʒ]", "[g]"], "correct": "[ʒ]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается буква 'â'?",
         "options": ["[a] краткий", "[a:] долгий", "[ɑ]", "[ə]"], "correct": "[a:] долгий"},
        {"id": 5, "type": "quiz", "question": "🔊 В чем разница между 'patte' и 'pâte'?",
         "options": ["Смысл разный, произношение одинаковое", "Разная долгота гласного", "Разные согласные", "Разное ударение"], "correct": "Разная долгота гласного"},

        # ========== УПРАЖНЕНИЕ №3: ПЕРЕВОД ФРАЗ ==========
        {"id": 6, "type": "text_input", "question": "📖 Переведите на русский: 'Pierre marche vite'", "correct": "Пьер идет быстро"},
        {"id": 7, "type": "text_input", "question": "📖 Переведите на русский: 'Anne cherche ce livre'", "correct": "Анна ищет эту книгу"},
        {"id": 8, "type": "text_input", "question": "📖 Переведите на русский: 'Elle cache la clé'", "correct": "Она прячет ключ"},
        {"id": 9, "type": "text_input", "question": "📖 Переведите на русский: 'Ma chère amie arrive chaque hiver'", "correct": "Моя дорогая подруга приезжает каждую зиму"},
        {"id": 10, "type": "text_input", "question": "📖 Переведите на русский: 'Cette chaise est très chère'", "correct": "Этот стул очень дорогой"},
        {"id": 11, "type": "text_input", "question": "📖 Переведите на русский: 'Sa fille travaille chaque mercredi'", "correct": "Его дочь работает каждую среду"},

        # ========== УПРАЖНЕНИЕ №6: СЛОВА СО ЗВУКОМ [ʒ] НА КОНЦЕ ==========
        {"id": 12, "type": "text_input", "question": "📝 Допишите перевод: 'fromage' — сыр", "correct": "сыр"},
        {"id": 13, "type": "text_input", "question": "📝 Допишите перевод: 'sage' — ...", "correct": "мудрый, послушный"},
        {"id": 14, "type": "text_input", "question": "📝 Допишите перевод: 'neige' — ...", "correct": "снег"},
        {"id": 15, "type": "text_input", "question": "📝 Допишите перевод: 'âge' — ...", "correct": "возраст"},
        {"id": 16, "type": "text_input", "question": "📝 Допишите перевод: 'collège' — ...", "correct": "колледж"},
        {"id": 17, "type": "text_input", "question": "📝 Допишите перевод: 'étage' — ...", "correct": "этаж"},
        {"id": 18, "type": "text_input", "question": "📝 Допишите перевод: 'plage' — ...", "correct": "пляж"},
        {"id": 19, "type": "text_input", "question": "📝 Допишите перевод: 'bagage' — ...", "correct": "багаж"},
        {"id": 20, "type": "text_input", "question": "📝 Допишите перевод: 'image' — ...", "correct": "изображение"},

        # ========== УПРАЖНЕНИЕ №7: ОТМЕТЬТЕ ПРОИЗНОШЕНИЕ [g] ИЛИ [ʒ] ==========
        {"id": 21, "type": "quiz", "question": "🔊 Как читается 'gymnastique'?",
         "options": ["[g]", "[ʒ]"], "correct": "[ʒ]"},
        {"id": 22, "type": "quiz", "question": "🔊 Как читается 'glace'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 23, "type": "quiz", "question": "🔊 Как читается 'génie'?",
         "options": ["[g]", "[ʒ]"], "correct": "[ʒ]"},
        {"id": 24, "type": "quiz", "question": "🔊 Как читается 'gare'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 25, "type": "quiz", "question": "🔊 Как читается 'guerre'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 26, "type": "quiz", "question": "🔊 Как читается 'mage'?",
         "options": ["[g]", "[ʒ]"], "correct": "[ʒ]"},
        {"id": 27, "type": "quiz", "question": "🔊 Как читается 'regarder'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 28, "type": "quiz", "question": "🔊 Как читается 'grammaire'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 29, "type": "quiz", "question": "🔊 Как читается 'gai'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},
        {"id": 30, "type": "quiz", "question": "🔊 Как читается 'cage'?",
         "options": ["[g]", "[ʒ]"], "correct": "[ʒ]"},
        {"id": 31, "type": "quiz", "question": "🔊 Как читается 'geste'?",
         "options": ["[g]", "[ʒ]"], "correct": "[ʒ]"},
        {"id": 32, "type": "quiz", "question": "🔊 Как читается 'fatigué'?",
         "options": ["[g]", "[ʒ]"], "correct": "[g]"},

        # ========== УПРАЖНЕНИЕ №9: ПЕРЕВОД ФРАЗ ==========
        {"id": 33, "type": "text_input", "question": "📖 Переведите на русский: 'Il aime les théâtres de Paris'", "correct": "Он любит театры Парижа"},
        {"id": 34, "type": "text_input", "question": "📖 Переведите на русский: 'Elle cherche ses bagages'", "correct": "Она ищет свой багаж"},
        {"id": 35, "type": "text_input", "question": "📖 Переведите на русский: 'Gérard est sage et calme'", "correct": "Жерар мудрый и спокойный"},
        {"id": 36, "type": "text_input", "question": "📖 Переведите на русский: 'Le général arrive jeudi'", "correct": "Генерал приезжает в четверг"},
        {"id": 37, "type": "text_input", "question": "📖 Переведите на русский: 'Anne imite ses gestes'", "correct": "Анна подражает его жестам"},
        {"id": 38, "type": "text_input", "question": "📖 Переведите на русский: 'Nana est jeune et très belle'", "correct": "Нана молода и очень красива"},
        {"id": 39, "type": "text_input", "question": "📖 Переведите на русский: 'Il a le visage pâle'", "correct": "У него бледное лицо"},
        {"id": 40, "type": "text_input", "question": "📖 Переведите на русский: 'Ce fromage est très cher'", "correct": "Этот сыр очень дорогой"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 41, "type": "quiz", "question": "📖 Как переводится 'chaise'?",
         "options": ["Стол", "Стул", "Кровать", "Шкаф"], "correct": "Стул"},
        {"id": 42, "type": "quiz", "question": "📖 Как переводится 'chercher'?",
         "options": ["Прятать", "Искать", "Находить", "Терять"], "correct": "Искать"},
        {"id": 43, "type": "quiz", "question": "📖 Как переводится 'visage'?",
         "options": ["Тело", "Лицо", "Голова", "Рука"], "correct": "Лицо"},
        {"id": 44, "type": "quiz", "question": "📖 Как переводится 'fromage'?",
         "options": ["Хлеб", "Масло", "Сыр", "Молоко"], "correct": "Сыр"},
        {"id": 45, "type": "quiz", "question": "📖 Как переводится 'neige'?",
         "options": ["Дождь", "Ветер", "Снег", "Солнце"], "correct": "Снег"},
        {"id": 46, "type": "quiz", "question": "📖 Как переводится 'plage'?",
         "options": ["Гора", "Лес", "Пляж", "Река"], "correct": "Пляж"},
        {"id": 47, "type": "quiz", "question": "📖 Как переводится 'jeune'?",
         "options": ["Старый", "Молодой", "Высокий", "Низкий"], "correct": "Молодой"},
        {"id": 48, "type": "quiz", "question": "📖 Как переводится 'jeudi'?",
         "options": ["Вторник", "Среда", "Четверг", "Пятница"], "correct": "Четверг"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 49, "type": "text_input", "question": "🔄 Напишите по-французски 'стул'", "correct": "chaise"},
        {"id": 50, "type": "text_input", "question": "🔄 Напишите по-французски 'искать'", "correct": "chercher"},
        {"id": 51, "type": "text_input", "question": "🔄 Напишите по-французски 'прятать'", "correct": "cacher"},
        {"id": 52, "type": "text_input", "question": "🔄 Напишите по-французски 'работать'", "correct": "travailler"},
        {"id": 53, "type": "text_input", "question": "🔄 Напишите по-французски 'дорогой'", "correct": "cher"},
        {"id": 54, "type": "text_input", "question": "🔄 Напишите по-французски 'лицо'", "correct": "visage"},
        {"id": 55, "type": "text_input", "question": "🔄 Напишите по-французски 'сыр'", "correct": "fromage"},
        {"id": 56, "type": "text_input", "question": "🔄 Напишите по-французски 'возраст'", "correct": "âge"},
        {"id": 57, "type": "text_input", "question": "🔄 Напишите по-французски 'этаж'", "correct": "étage"},
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'пляж'", "correct": "plage"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'багаж'", "correct": "bagage"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'я'", "correct": "je"},
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'никогда'", "correct": "jamais"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'молодой'", "correct": "jeune"},
        {"id": 63, "type": "text_input", "question": "🔄 Напишите по-французски 'театр'", "correct": "théâtre"},
        {"id": 64, "type": "text_input", "question": "🔄 Напишите по-французски 'бледный'", "correct": "pâle"},
        {"id": 65, "type": "text_input", "question": "🔄 Напишите по-французски 'тесто'", "correct": "pâte"}
    ],
    "question": "Пройдите все 65 карточек практики!",
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
# ---------- ДЕНЬ 16: ТЕСТ 4 (Уроки 7-8 / дни 13-14) ----------
COURSE_DAYS[16] = {
    "title": "Тест 4: Уроки 7-8 (Звуки [œ], [ə], [ʃ], [ʒ], [a:])",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        # ============================================================
        # ЧАСТЬ 1: ДИКТАНТ СЛОВ ИЗ УРОКА 7 (звуки [œ], [ə])
        # ============================================================
        {"id": 1, "type": "text_input", "question": "📝 Напишите по-французски: 'час'", "correct": "heure"},
        {"id": 2, "type": "text_input", "question": "📝 Напишите по-французски: 'масло'", "correct": "beurre"},
        {"id": 3, "type": "text_input", "question": "📝 Напишите по-французски: 'сестра'", "correct": "sœur"},
        {"id": 4, "type": "text_input", "question": "📝 Напишите по-французски: 'сердце'", "correct": "cœur"},
        {"id": 5, "type": "text_input", "question": "📝 Напишите по-французски: 'цветок'", "correct": "fleur"},
        {"id": 6, "type": "text_input", "question": "📝 Напишите по-французски: 'страх'", "correct": "peur"},
        {"id": 7, "type": "text_input", "question": "📝 Напишите по-французски: 'директор'", "correct": "directeur"},
        {"id": 8, "type": "text_input", "question": "📝 Напишите по-французски: 'он плачет'", "correct": "il pleure"},
        {"id": 9, "type": "text_input", "question": "📝 Напишите по-французски: 'идет дождь'", "correct": "il pleut"},
        {"id": 10, "type": "text_input", "question": "📝 Напишите по-французски: 'он боится'", "correct": "il a peur"},
        {"id": 11, "type": "text_input", "question": "📝 Напишите по-французски: 'первая'", "correct": "première"},
        {"id": 12, "type": "text_input", "question": "📝 Напишите по-французски: 'маленькая'", "correct": "petite"},
        {"id": 13, "type": "text_input", "question": "📝 Напишите по-французски: 'смотреть'", "correct": "regarder"},
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски: 'среда'", "correct": "mercredi"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски: 'браслет'", "correct": "bracelet"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски: 'окно'", "correct": "fenêtre"},

        # ============================================================
        # ЧАСТЬ 2: ДИКТАНТ СЛОВ ИЗ УРОКА 8 (звуки [ʃ], [ʒ], [a:])
        # ============================================================
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски: 'стул'", "correct": "chaise"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски: 'ходить, шагать'",
         "correct": "marcher"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски: 'каждый'", "correct": "chaque"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски: 'дорогой'", "correct": "cher"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски: 'прятать'", "correct": "cacher"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски: 'искать'", "correct": "chercher"},
        {"id": 23, "type": "text_input", "question": "📝 Напишите по-французски: 'работать'", "correct": "travailler"},
        {"id": 24, "type": "text_input", "question": "📝 Напишите по-французски: 'он работает'",
         "correct": "il travaille"},
        {"id": 25, "type": "text_input", "question": "📝 Напишите по-французски: 'приезжать'", "correct": "arriver"},
        {"id": 26, "type": "text_input", "question": "📝 Напишите по-французски: 'генерал'", "correct": "général"},
        {"id": 27, "type": "text_input", "question": "📝 Напишите по-французски: 'жест'", "correct": "geste"},
        {"id": 28, "type": "text_input", "question": "📝 Напишите по-французски: 'гимнастика'",
         "correct": "gymnastique"},
        {"id": 29, "type": "text_input", "question": "📝 Напишите по-французски: 'я'", "correct": "je"},
        {"id": 30, "type": "text_input", "question": "📝 Напишите по-французски: 'никогда'", "correct": "jamais"},
        {"id": 31, "type": "text_input", "question": "📝 Напишите по-французски: 'четверг'", "correct": "jeudi"},
        {"id": 32, "type": "text_input", "question": "📝 Напишите по-французски: 'бросать'", "correct": "jeter"},
        {"id": 33, "type": "text_input", "question": "📝 Напишите по-французски: 'молодой'", "correct": "jeune"},
        {"id": 34, "type": "text_input", "question": "📝 Напишите по-французски: 'обедать'", "correct": "déjeuner"},
        {"id": 35, "type": "text_input", "question": "📝 Напишите по-французски: 'лицо'", "correct": "visage"},
        {"id": 36, "type": "text_input", "question": "📝 Напишите по-французски: 'сыр'", "correct": "fromage"},
        {"id": 37, "type": "text_input", "question": "📝 Напишите по-французски: 'послушный, мудрый'",
         "correct": "sage"},
        {"id": 38, "type": "text_input", "question": "📝 Напишите по-французски: 'снег'", "correct": "neige"},
        {"id": 39, "type": "text_input", "question": "📝 Напишите по-французски: 'возраст'", "correct": "âge"},
        {"id": 40, "type": "text_input", "question": "📝 Напишите по-французски: 'этаж'", "correct": "étage"},
        {"id": 41, "type": "text_input", "question": "📝 Напишите по-французски: 'пляж'", "correct": "plage"},
        {"id": 42, "type": "text_input", "question": "📝 Напишите по-французски: 'багаж'", "correct": "bagage"},
        {"id": 43, "type": "text_input", "question": "📝 Напишите по-французски: 'театр'", "correct": "théâtre"},
        {"id": 44, "type": "text_input", "question": "📝 Напишите по-французски: 'бледный'", "correct": "pâle"},
        {"id": 45, "type": "text_input", "question": "📝 Напишите по-французски: 'тесто'", "correct": "pâte"},

        # ============================================================
        # ЧАСТЬ 3: ФОНЕТИКА И ПРАВИЛА (quiz)
        # ============================================================
        {"id": 46, "type": "quiz", "question": "🔊 Как читается буквосочетание 'eu' в слове 'fleur'?",
         "options": ["[ø]", "[œ]", "[ə]", "[y]"], "correct": "[œ]"},
        {"id": 47, "type": "quiz", "question": "🔊 Как читается артикль 'le'?",
         "options": ["[le]", "[lə]", "[lɛ]", "[lœ]"], "correct": "[lə]"},
        {"id": 48, "type": "quiz", "question": "🔊 Почему звук [ə] называется 'беглым'?",
         "options": ["Он всегда произносится", "Он может выпадать в речи", "Он всегда ударный", "Он читается как [e]"],
         "correct": "Он может выпадать в речи"},
        {"id": 49, "type": "quiz", "question": "🔊 Как читается буквосочетание 'ch' во французском?",
         "options": ["[k]", "[ʃ]", "[tʃ]", "[ç]"], "correct": "[ʃ]"},
        {"id": 50, "type": "quiz", "question": "🔊 Когда буква 'g' читается как [ʒ]?",
         "options": ["Перед a, o, u", "Перед e, i, y", "В конце слова", "Перед согласными"],
         "correct": "Перед e, i, y"},
        {"id": 51, "type": "quiz", "question": "🔊 Как читается буква 'j' во французском?",
         "options": ["[ʒ]", "[j]", "[dʒ]", "[g]"], "correct": "[ʒ]"},
        {"id": 52, "type": "quiz", "question": "🔊 Как читается буква 'â'?",
         "options": ["[a] краткий", "[a:] долгий", "[ɑ]", "[ə]"], "correct": "[a:] долгий"},
        {"id": 53, "type": "quiz", "question": "🔊 В чем разница между 'patte' и 'pâte'?",
         "options": ["Смысл разный, произношение одинаковое", "Разная долгота гласного", "Разные согласные",
                     "Разное ударение"], "correct": "Разная долгота гласного"},

        # ============================================================
        # ЧАСТЬ 4: ТРАНСКРИПЦИЯ (text_input)
        # ============================================================
        {"id": 54, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'fleur'", "correct": "[flœr]"},
        {"id": 55, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'sœur'", "correct": "[sœr]"},
        {"id": 56, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'cœur'", "correct": "[kœr]"},
        {"id": 57, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'première'",
         "correct": "[prəmjɛr]"},
        {"id": 58, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'chaise'", "correct": "[ʃɛz]"},
        {"id": 59, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'visage'", "correct": "[vizaːʒ]"},
        {"id": 60, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'fromage'", "correct": "[frɔmaːʒ]"},
        {"id": 61, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'âge'", "correct": "[aːʒ]"},
        {"id": 62, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'pâte'", "correct": "[paːt]"},
        {"id": 63, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'théâtre'", "correct": "[teɑtr]"},

        # ============================================================
        # ЧАСТЬ 5: ПЕРЕВОД ФРАЗ (text_input)
        # ============================================================
        {"id": 64, "type": "text_input", "question": "📖 Переведите на русский: 'Il a quatre filles'",
         "correct": "У него четыре дочери"},
        {"id": 65, "type": "text_input", "question": "📖 Переведите на русский: 'La fleur est très belle'",
         "correct": "Цветок очень красивый"},
        {"id": 66, "type": "text_input",
         "question": "📖 Переведите на русский: 'Ma sœur travaille. Elle est directeur.'",
         "correct": "Моя сестра работает. Она директор"},
        {"id": 67, "type": "text_input", "question": "📖 Переведите на русский: 'Fermez ce livre!'",
         "correct": "Закройте эту книгу"},
        {"id": 68, "type": "text_input", "question": "📖 Переведите на русский: 'Pierre marche vite'",
         "correct": "Пьер идет быстро"},
        {"id": 69, "type": "text_input", "question": "📖 Переведите на русский: 'Anne cherche ce livre'",
         "correct": "Анна ищет эту книгу"},
        {"id": 70, "type": "text_input", "question": "📖 Переведите на русский: 'Cette chaise est très chère'",
         "correct": "Этот стул очень дорогой"},
        {"id": 71, "type": "text_input", "question": "📖 Переведите на русский: 'Le général arrive jeudi'",
         "correct": "Генерал приезжает в четверг"},
        {"id": 72, "type": "text_input", "question": "📖 Переведите на русский: 'Nana est jeune et très belle'",
         "correct": "Нана молода и очень красива"},
        {"id": 73, "type": "text_input", "question": "📖 Переведите на русский: 'Il a le visage pâle'",
         "correct": "У него бледное лицо"},
        {"id": 74, "type": "text_input", "question": "📖 Переведите на русский: 'Ce fromage est très cher'",
         "correct": "Этот сыр очень дорогой"},
        {"id": 75, "type": "text_input", "question": "📖 Переведите на русский: 'Le bracelet de ma petite sœur est ici'",
         "correct": "Браслет моей маленькой сестры здесь"},
        {"id": 76, "type": "text_input", "question": "📖 Переведите на русский: 'Il a peur de fermer sa fenêtre'",
         "correct": "Он боится закрыть свое окно"},

        # ============================================================
        # ЧАСТЬ 6: ПЕРЕВОД С РУССКОГО (text_input)
        # ============================================================
        {"id": 77, "type": "text_input", "question": "🔄 Переведите на французский: 'У него есть подруги'",
         "correct": "Il a des amies"},
        {"id": 78, "type": "text_input", "question": "🔄 Переведите на французский: 'Закройте эту книгу!'",
         "correct": "Fermez ce livre"},
        {"id": 79, "type": "text_input", "question": "🔄 Переведите на французский: 'Моя сестра работает'",
         "correct": "Ma sœur travaille"},
        {"id": 80, "type": "text_input", "question": "🔄 Переведите на французский: 'Он ищет свой багаж'",
         "correct": "Il cherche ses bagages"},
        {"id": 81, "type": "text_input", "question": "🔄 Переведите на французский: 'Она прячет ключ'",
         "correct": "Elle cache la clé"},
        {"id": 82, "type": "text_input", "question": "🔄 Переведите на французский: 'Приезжайте в субботу'",
         "correct": "Arrivez samedi"},
        {"id": 83, "type": "text_input", "question": "🔄 Переведите на французский: 'Он боится закрыть окно'",
         "correct": "Il a peur de fermer la fenêtre"},
        {"id": 84, "type": "text_input", "question": "🔄 Переведите на французский: 'Этот сыр очень дорогой'",
         "correct": "Ce fromage est très cher"},

        # ============================================================
        # ЧАСТЬ 7: ОПРЕДЕЛЕНИЕ РОДА СЛОВ (quiz)
        # ============================================================
        {"id": 85, "type": "quiz", "question": "📚 Какого рода слово 'visage' (лицо)?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 86, "type": "quiz", "question": "📚 Какого рода слово 'fromage' (сыр)?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 87, "type": "quiz", "question": "📚 Какого рода слово 'neige' (снег)?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 88, "type": "quiz", "question": "📚 Какого рода слово 'plage' (пляж)?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 89, "type": "quiz", "question": "📚 Какого рода слово 'chaise' (стул)?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},

        # ============================================================
        # ЧАСТЬ 8: ДОПОЛНИТЕЛЬНЫЕ ВОПРОСЫ (quiz)
        # ============================================================
        {"id": 90, "type": "quiz", "question": "📖 Как переводится 'jamais'?",
         "options": ["Всегда", "Никогда", "Иногда", "Часто"], "correct": "Никогда"},
        {"id": 91, "type": "quiz", "question": "📖 Как переводится 'je'?",
         "options": ["Ты", "Он", "Я", "Она"], "correct": "Я"},
        {"id": 92, "type": "quiz", "question": "📖 Как переводится 'jeune'?",
         "options": ["Старый", "Молодой", "Красивый", "Умный"], "correct": "Молодой"},
        {"id": 93, "type": "quiz", "question": "📖 Как переводится 'chaque'?",
         "options": ["Каждый", "Некоторые", "Разные", "Все"], "correct": "Каждый"},
        {"id": 94, "type": "quiz", "question": "📖 Что означает 'elle cherche'?",
         "options": ["Она прячет", "Она ищет", "Она находит", "Она теряет"], "correct": "Она ищет"},
        {"id": 95, "type": "quiz", "question": "📖 Что означает 'il cache'?",
         "options": ["Он ищет", "Он находит", "Он прячет", "Он теряет"], "correct": "Он прячет"},
        {"id": 96, "type": "quiz", "question": "📖 Как переводится 'grâce'?",
         "options": ["Грация", "Благодарность", "Милость", "Слава"], "correct": "Грация"},
        {"id": 97, "type": "quiz", "question": "📖 Как переводится 'bâtir'?",
         "options": ["Строить", "Ломать", "Чинить", "Красить"], "correct": "Строить"},

        # ============================================================
        # ЧАСТЬ 9: ПЕРЕВОД С РУССКОГО (слова, text_input)
        # ============================================================
        {"id": 98, "type": "text_input", "question": "🔄 Напишите по-французски 'никогда'", "correct": "jamais"},
        {"id": 99, "type": "text_input", "question": "🔄 Напишите по-французски 'молодой'", "correct": "jeune"},
        {"id": 100, "type": "text_input", "question": "🔄 Напишите по-французски 'каждый'", "correct": "chaque"},
        {"id": 101, "type": "text_input", "question": "🔄 Напишите по-французски 'работать'", "correct": "travailler"},
        {"id": 102, "type": "text_input", "question": "🔄 Напишите по-французски 'искать'", "correct": "chercher"},
        {"id": 103, "type": "text_input", "question": "🔄 Напишите по-французски 'прятать'", "correct": "cacher"},
        {"id": 104, "type": "text_input", "question": "🔄 Напишите по-французски 'лицо'", "correct": "visage"},
        {"id": 105, "type": "text_input", "question": "🔄 Напишите по-французски 'снег'", "correct": "neige"},
        {"id": 106, "type": "text_input", "question": "🔄 Напишите по-французски 'возраст'", "correct": "âge"},
        {"id": 107, "type": "text_input", "question": "🔄 Напишите по-французски 'этаж'", "correct": "étage"},
        {"id": 108, "type": "text_input", "question": "🔄 Напишите по-французски 'пляж'", "correct": "plage"},
        {"id": 109, "type": "text_input", "question": "🔄 Напишите по-французски 'багаж'", "correct": "bagage"},
        {"id": 110, "type": "text_input", "question": "🔄 Напишите по-французски 'театр'", "correct": "théâtre"},
        {"id": 111, "type": "text_input", "question": "🔄 Напишите по-французски 'бледный'", "correct": "pâle"},
        {"id": 112, "type": "text_input", "question": "🔄 Напишите по-французски 'тесто'", "correct": "pâte"}
    ],
    "question": "Пройдите все 112 вопросов теста!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 17: УРОК 9 ----------
# ---------- ДЕНЬ 17: УРОК 9 (Звуки [ø], [y], [u] и полугласный [ɥ]) ----------
COURSE_DAYS[17] = {
    "title": "Урок 9: Звуки [ø], [y], [u] и полугласный [ɥ]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "гласный [ø]",
            "russian": "отсутствует",
            "letters": "eu<br>œu",
            "notes": "• Буквосочетания eu, œu читаются как [ø] на конце слов и перед [z].<br>• Прием: настройтесь на свист губами → произнесите [e] → получится [ø]!"
        },
        {
            "sound": "гласный [y]",
            "russian": "отсутствует (не путать с русским [у]!)",
            "letters": "U, u<br>Ü, ü",
            "notes": "• Прием: настройтесь на свист губами → произнесите [i] → получится [y]!<br>• Не отождествляйте с русским звуком в слове 'ю'!"
        },
        {
            "sound": "полугласный [ɥ]",
            "russian": "отсутствует",
            "letters": "ui<br>ue<br>ua",
            "notes": "• Это звук [y], произнесенный предельно кратко перед гласным.<br>• Пример: nuit [nɥi] — ночь, pluie [plɥi] — дождь."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "🎯 Как произнести звук [ø]",
            "text": "1️⃣ Приготовьтесь свистнуть — одними губами, без пальцев!<br>"
                    "2️⃣ Запомните положение губ, посмотрите в зеркало.<br>"
                    "3️⃣ Не меняя положения губ, произнесите звук [e].<br><br>"
                    "Получится французский [ø]!<br>"
                    "Примеры: deux [dø] — два, bleu [blø] — синий"
        },
        {
            "subtitle": "🎯 Как произнести звук [y]",
            "text": "1️⃣ Снова настройтесь на свист губами.<br>"
                    "2️⃣ Не меняя положения губ, произнесите звук [i].<br><br>"
                    "Получится французский [y]!<br>"
                    "⚠️ Не путайте с русским 'ю'! revue [rəvy] ≠ 'ревю'!<br>"
                    "Примеры: tu [ty] — ты, musique [myzik] — музыка"
        },
        {
            "subtitle": "🎯 Полугласный [ɥ]",
            "text": "Звук [ɥ] — это [y], произнесенный предельно кратко перед гласным.<br><br>"
                    "Начните выговаривать [y], но только начните, и сразу переходите к следующему гласному.<br>"
                    "Примеры:<br>"
                    "• nuit [nɥi] — ночь<br>"
                    "• pluie [plɥi] — дождь<br>"
                    "• nuage [nɥaʒ] — облако"
        },
        {
            "subtitle": "📝 Буква X на конце слов",
            "text": "Буква <b>x</b> на конце слов <b>не читается</b>.<br><br>"
                    "Примеры:<br>"
                    "• paix [pɛ] — мир<br>"
                    "• deux [dø] — два<br>"
                    "• heureux [œrø] — счастливый"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Произнесите:",
            "text": "[te – tø], [le – lø], [ne – nø], [ve – vø], [ke – kø], [de – dø]"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочтите слова и постарайтесь запомнить их:",
            "text": "• deux [dø] — два, две<br>"
                    "• bleu [blø] (м.р.), bleue [blø] (ж.р.) — синий, голубой<br>"
                    "• feu [fø] — огонь<br>"
                    "• jeu [ʒø] — игра<br>"
                    "• il veut [il vø] — он хочет<br>"
                    "• il peut [il pø] — он может<br>"
                    "• paresseux [parɛsø] (м.р.), paresseuse [parɛsøz] (ж.р.) — ленивый"
        },
        {
            "subtitle": "🎧 Упражнение № 3. Прочтите, стараясь запомнить новые слова. Обратите внимание на примеры с конечной x:",
            "text": "• paix [pɛ] f — мир<br>"
                    "• je veux [ʒə vø] — я хочу<br>"
                    "• je peux [ʒə pø] — я могу<br>"
                    "• adieux ! [adjø] — прощайте!<br>"
                    "• monsieur [məsjø] m — господин, месье<br>"
                    "• messieurs [mesjø] — господа<br>"
                    "• affreux [afrø] m, affreuse [afrøz] f — ужасный<br>"
                    "• capricieux [kaprisjø] m, capricieuse [kaprisjøz] f — капризный<br>"
                    "• délicieux [delisjø] m, délicieuse [delisjøz] f — восхитительный<br>"
                    "• fameux [famø] m, fameuse [famøz] f — знаменитый<br>"
                    "• heureux [œrø] m, heureuse [œrøz] f — счастливый<br>"
                    "• merveilleux [mɛrvɛjø] m, merveilleuse [mɛrvɛjøz] f — чудесный<br>"
                    "• nerveux [nɛrvø] m, nerveuse [nɛrvøz] f — нервный<br>"
                    "• précieux [presjø] m, précieuse [presjøz] f — драгоценный"
        },
        {
            "subtitle": "🎧 Упражнение № 6. Произнесите:",
            "text": "[ti – ty], [li – ly], [vi – vy], [si – sy], [ki – ky], [ri – ry], [mi – my], [ni – ny], [fi – fy], [ʒi – ʒy]"
        },
        {
            "subtitle": "🎧 Упражнение № 7. Прочтите и запомните новые слова:",
            "text": "• une [yn] — неопределенный артикль ж.р.<br>"
                    "• tu [ty] — ты<br>"
                    "• tu as [ty a] — у тебя есть<br>"
                    "• musique [myzik] f — музыка<br>"
                    "• musée [myze] m — музей<br>"
                    "• revue [rəvy] f — журнал, обозрение<br>"
                    "• rue [ry] f — улица<br>"
                    "• sur [syr] — на (предлог)<br>"
                    "• sûr [syr] m, sûre [syr] f — уверенный<br>"
                    "• lune [lyn] f — луна<br>"
                    "• fumer [fyme] — курить"
        },
        {
            "subtitle": "🎧 Упражнение № 9. Произнесите:",
            "text": "[y – a – ɥa], [y – ε – ɥε], [y – e – ɥe], [y – a – ɥa], [y – i – ɥi], [y – œ – ɥœ]"
        },
        {
            "subtitle": "🎧 Упражнение № 10. Прочтите и постарайтесь запомнить новые слова:",
            "text": "• je suis [ʒə sɥi] — я есть<br>"
                    "• je suis sûr [ʒə sɥi syr] — я уверен<br>"
                    "• je suis prêt [ʒə sɥi prɛ] — я готов<br>"
                    "• je suis surpris [ʒə sɥi syrpri] — я удивлен<br>"
                    "• nuit [nɥi] f — ночь<br>"
                    "• pluie [plɥi] f — дождь<br>"
                    "• huit [ɥit] — восемь<br>"
                    "• manuel [manɥɛl] m — учебник<br>"
                    "• nuage [nɥaʒ] m — туча, облако<br>"
                    "• fructueux [fryktɥø] m, fructueuse [fryktɥøz] f — плодотворный"
        }
    ],
    "vocabulary": [
        {"fr": "deux", "tr": "[dø]", "ru": "два, две"},
        {"fr": "bleu", "tr": "[blø]", "ru": "синий, голубой (м.р.)"},
        {"fr": "bleue", "tr": "[blø]", "ru": "синяя, голубая (ж.р.)"},
        {"fr": "feu", "tr": "[fø]", "ru": "огонь"},
        {"fr": "jeu", "tr": "[ʒø]", "ru": "игра"},
        {"fr": "il veut", "tr": "[il vø]", "ru": "он хочет"},
        {"fr": "il peut", "tr": "[il pø]", "ru": "он может"},
        {"fr": "je veux", "tr": "[ʒə vø]", "ru": "я хочу"},
        {"fr": "je peux", "tr": "[ʒə pø]", "ru": "я могу"},
        {"fr": "paresseux", "tr": "[parɛsø]", "ru": "ленивый (м.р.)"},
        {"fr": "paresseuse", "tr": "[parɛsøz]", "ru": "ленивая (ж.р.)"},
        {"fr": "paix", "tr": "[pɛ]", "ru": "мир"},
        {"fr": "adieux", "tr": "[adjø]", "ru": "прощайте"},
        {"fr": "monsieur", "tr": "[məsjø]", "ru": "господин, месье"},
        {"fr": "messieurs", "tr": "[mesjø]", "ru": "господа"},
        {"fr": "affreux", "tr": "[afrø]", "ru": "ужасный (м.р.)"},
        {"fr": "affreuse", "tr": "[afrøz]", "ru": "ужасная (ж.р.)"},
        {"fr": "capricieux", "tr": "[kaprisjø]", "ru": "капризный (м.р.)"},
        {"fr": "capricieuse", "tr": "[kaprisjøz]", "ru": "капризная (ж.р.)"},
        {"fr": "délicieux", "tr": "[delisjø]", "ru": "восхитительный (м.р.)"},
        {"fr": "délicieuse", "tr": "[delisjøz]", "ru": "восхитительная (ж.р.)"},
        {"fr": "fameux", "tr": "[famø]", "ru": "знаменитый (м.р.)"},
        {"fr": "fameuse", "tr": "[famøz]", "ru": "знаменитая (ж.р.)"},
        {"fr": "heureux", "tr": "[œrø]", "ru": "счастливый (м.р.)"},
        {"fr": "heureuse", "tr": "[œrøz]", "ru": "счастливая (ж.р.)"},
        {"fr": "merveilleux", "tr": "[mɛrvɛjø]", "ru": "чудесный (м.р.)"},
        {"fr": "merveilleuse", "tr": "[mɛrvɛjøz]", "ru": "чудесная (ж.р.)"},
        {"fr": "nerveux", "tr": "[nɛrvø]", "ru": "нервный (м.р.)"},
        {"fr": "nerveuse", "tr": "[nɛrvøz]", "ru": "нервная (ж.р.)"},
        {"fr": "précieux", "tr": "[presjø]", "ru": "драгоценный (м.р.)"},
        {"fr": "précieuse", "tr": "[presjøz]", "ru": "драгоценная (ж.р.)"},
        {"fr": "une", "tr": "[yn]", "ru": "неопределенный артикль ж.р."},
        {"fr": "tu", "tr": "[ty]", "ru": "ты"},
        {"fr": "tu as", "tr": "[ty a]", "ru": "у тебя есть"},
        {"fr": "musique", "tr": "[myzik]", "ru": "музыка (ж.р.)"},
        {"fr": "musée", "tr": "[myze]", "ru": "музей (м.р.)"},
        {"fr": "revue", "tr": "[rəvy]", "ru": "журнал, обозрение (ж.р.)"},
        {"fr": "rue", "tr": "[ry]", "ru": "улица (ж.р.)"},
        {"fr": "sur", "tr": "[syr]", "ru": "на (предлог)"},
        {"fr": "sûr", "tr": "[syr]", "ru": "уверенный (м.р.)"},
        {"fr": "sûre", "tr": "[syr]", "ru": "уверенная (ж.р.)"},
        {"fr": "lune", "tr": "[lyn]", "ru": "луна (ж.р.)"},
        {"fr": "fumer", "tr": "[fyme]", "ru": "курить"},
        {"fr": "je suis", "tr": "[ʒə sɥi]", "ru": "я есть"},
        {"fr": "je suis sûr", "tr": "[ʒə sɥi syr]", "ru": "я уверен"},
        {"fr": "je suis prêt", "tr": "[ʒə sɥi prɛ]", "ru": "я готов"},
        {"fr": "je suis surpris", "tr": "[ʒə sɥi syrpri]", "ru": "я удивлен"},
        {"fr": "nuit", "tr": "[nɥi]", "ru": "ночь (ж.р.)"},
        {"fr": "pluie", "tr": "[plɥi]", "ru": "дождь (ж.р.)"},
        {"fr": "huit", "tr": "[ɥit]", "ru": "восемь"},
        {"fr": "manuel", "tr": "[manɥɛl]", "ru": "учебник (м.р.)"},
        {"fr": "nuage", "tr": "[nɥaʒ]", "ru": "облако, туча (м.р.)"},
        {"fr": "fructueux", "tr": "[fryktɥø]", "ru": "плодотворный (м.р.)"},
        {"fr": "fructueuse", "tr": "[fryktɥøz]", "ru": "плодотворная (ж.р.)"}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Звуки [ø]", "url": "/static/audio/lesson9_1.mp3"},
        {"title": "Упражнение №2: Слова со звуком [ø]", "url": "/static/audio/lesson9_2.mp3"},
        {"title": "Упражнение №3: Слова с конечной x", "url": "/static/audio/lesson9_3.mp3"},
        {"title": "Упражнение №6: Звуки [y]", "url": "/static/audio/lesson9_4.mp3"},
        {"title": "Упражнение №7: Слова со звуком [y]", "url": "/static/audio/lesson9_5.mp3"},
        {"title": "Упражнение №9: Полугласный [ɥ]", "url": "/static/audio/lesson9_6.mp3"},
        {"title": "Упражнение №10: Слова с [ɥ]", "url": "/static/audio/lesson9_7.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается 'eu' в слове 'deux' (на конце)?",
         "options": ["[œ]", "[ø]", "[ə]", "[y]"], "correct": "[ø]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как произнести звук [ø]?",
         "options": ["Как русское 'ё'", "Настройка на свист + [e]", "Как [œ]", "Как [y]"], "correct": "Настройка на свист + [e]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как произнести звук [y]?",
         "options": ["Как русское 'у'", "Настройка на свист + [i]", "Как [u]", "Как [ø]"], "correct": "Настройка на свист + [i]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается буква 'u' в слове 'tu'?",
         "options": ["[u]", "[y]", "[ø]", "[œ]"], "correct": "[y]"},
        {"id": 5, "type": "quiz", "question": "🔊 Как читается 'ui' в слове 'nuit'?",
         "options": ["[ui]", "[ɥi]", "[y]", "[wi]"], "correct": "[ɥi]"},
        {"id": 6, "type": "quiz", "question": "📚 Читается ли буква 'x' на конце слов?",
         "options": ["Да, всегда", "Нет, не читается", "Только в заимствованиях", "Только перед гласной"], "correct": "Нет, не читается"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 7, "type": "quiz", "question": "📖 Как переводится 'deux'?",
         "options": ["Один", "Два", "Три", "Четыре"], "correct": "Два"},
        {"id": 8, "type": "quiz", "question": "📖 Как переводится 'bleu'?",
         "options": ["Красный", "Синий", "Зеленый", "Желтый"], "correct": "Синий"},
        {"id": 9, "type": "quiz", "question": "📖 Что означает 'il veut'?",
         "options": ["Он может", "Он хочет", "Он знает", "Он идет"], "correct": "Он хочет"},
        {"id": 10, "type": "quiz", "question": "📖 Что означает 'il peut'?",
         "options": ["Он хочет", "Он может", "Он должен", "Он знает"], "correct": "Он может"},
        {"id": 11, "type": "quiz", "question": "📖 Как переводится 'heureux'?",
         "options": ["Грустный", "Счастливый", "Злой", "Усталый"], "correct": "Счастливый"},
        {"id": 12, "type": "quiz", "question": "📖 Как переводится 'paresseux'?",
         "options": ["Умный", "Ленивый", "Красивый", "Добрый"], "correct": "Ленивый"},
        {"id": 13, "type": "quiz", "question": "📖 Как переводится 'capricieux'?",
         "options": ["Спокойный", "Капризный", "Веселый", "Грустный"], "correct": "Капризный"},
        {"id": 14, "type": "quiz", "question": "📖 Как переводится 'délicieux'?",
         "options": ["Вкусный", "Восхитительный", "Кислый", "Горький"], "correct": "Восхитительный"},
        {"id": 15, "type": "quiz", "question": "📖 Как переводится 'merveilleux'?",
         "options": ["Обычный", "Чудесный", "Плохой", "Скучный"], "correct": "Чудесный"},
        {"id": 16, "type": "quiz", "question": "📖 Как переводится 'nerveux'?",
         "options": ["Спокойный", "Нервный", "Медленный", "Быстрый"], "correct": "Нервный"},
        {"id": 17, "type": "quiz", "question": "📖 Как переводится 'précieux'?",
         "options": ["Дешевый", "Драгоценный", "Простой", "Обычный"], "correct": "Драгоценный"},
        {"id": 18, "type": "quiz", "question": "📖 Как переводится 'tu'?",
         "options": ["Я", "Ты", "Он", "Она"], "correct": "Ты"},
        {"id": 19, "type": "quiz", "question": "📖 Как переводится 'musique'?",
         "options": ["Музей", "Музыка", "Учебник", "Журнал"], "correct": "Музыка"},
        {"id": 20, "type": "quiz", "question": "📖 Как переводится 'musée'?",
         "options": ["Музыка", "Музей", "Улица", "Луна"], "correct": "Музей"},
        {"id": 21, "type": "quiz", "question": "📖 Как переводится 'rue'?",
         "options": ["Площадь", "Улица", "Дом", "Мост"], "correct": "Улица"},
        {"id": 22, "type": "quiz", "question": "📖 Как переводится 'lune'?",
         "options": ["Солнце", "Луна", "Звезда", "Небо"], "correct": "Луна"},
        {"id": 23, "type": "quiz", "question": "📖 Как переводится 'nuit'?",
         "options": ["День", "Ночь", "Утро", "Вечер"], "correct": "Ночь"},
        {"id": 24, "type": "quiz", "question": "📖 Как переводится 'pluie'?",
         "options": ["Снег", "Дождь", "Ветер", "Гроза"], "correct": "Дождь"},
        {"id": 25, "type": "quiz", "question": "📖 Как переводится 'huit'?",
         "options": ["Шесть", "Семь", "Восемь", "Девять"], "correct": "Восемь"},
        {"id": 26, "type": "quiz", "question": "📖 Как переводится 'nuage'?",
         "options": ["Солнце", "Облако", "Дождь", "Ветер"], "correct": "Облако"},

        # ========== УПРАЖНЕНИЕ №4: ПЕРЕВОД ФРАЗ ==========
        {"id": 27, "type": "text_input", "question": "📖 Переведите на русский: 'Le ciel est bleu'", "correct": "Небо голубое"},
        {"id": 28, "type": "text_input", "question": "📖 Переведите на русский: 'Il est gai et heureux'", "correct": "Он веселый и счастливый"},
        {"id": 29, "type": "text_input", "question": "📖 Переведите на русский: 'Madame est très nerveuse et capricieuse'", "correct": "Мадам очень нервная и капризная"},
        {"id": 30, "type": "text_input", "question": "📖 Переведите на русский: 'Ce livre est rare et précieux'", "correct": "Эта книга редкая и драгоценная"},
        {"id": 31, "type": "text_input", "question": "📖 Переведите на русский: 'Gérard a des idées merveilleuses'", "correct": "У Жерара чудесные идеи"},
        {"id": 32, "type": "text_input", "question": "📖 Переведите на русский: 'Je peux quitter la clinique mercredi'", "correct": "Я могу покинуть клинику в среду"},
        {"id": 33, "type": "text_input", "question": "📖 Переведите на русский: 'Il veut visiter Paris, cette fameuse capitale'", "correct": "Он хочет посетить Париж, эту знаменитую столицу"},

        # ========== УПРАЖНЕНИЕ №5: ПЕРЕВОД С РУССКОГО ==========
        {"id": 34, "type": "text_input", "question": "🔄 Переведите на французский: 'Я хочу приехать в четверг.'", "correct": "Je veux arriver jeudi"},
        {"id": 35, "type": "text_input", "question": "🔄 Переведите на французский: 'Пьер болен, но он может работать.'", "correct": "Pierre est malade, mais il peut travailler"},
        {"id": 36, "type": "text_input", "question": "🔄 Переведите на французский: 'Небо чудесное.'", "correct": "Le ciel est merveilleux"},
        {"id": 37, "type": "text_input", "question": "🔄 Переведите на французский: 'Она спокойна и счастлива.'", "correct": "Elle est calme et heureuse"},
        {"id": 38, "type": "text_input", "question": "🔄 Переведите на французский: 'Ваш сын капризный, он плачет, он хочет покинуть коллеж.'", "correct": "Votre fils est capricieux, il pleure, il veut quitter le collège"},
        {"id": 39, "type": "text_input", "question": "🔄 Переведите на французский: 'У мадам чудесное лицо.'", "correct": "Madame a un visage merveilleux"},

        # ========== УПРАЖНЕНИЕ №8: ПЕРЕВОД ФРАЗ ==========
        {"id": 40, "type": "text_input", "question": "📖 Переведите на русский: 'Tu as une amie'", "correct": "У тебя есть подруга"},
        {"id": 41, "type": "text_input", "question": "📖 Переведите на русский: 'Elle visite les musées et les théâtres de Paris'", "correct": "Она посещает музеи и театры Парижа"},
        {"id": 42, "type": "text_input", "question": "📖 Переведите на русский: 'La musique est merveilleuse'", "correct": "Музыка чудесная"},
        {"id": 43, "type": "text_input", "question": "📖 Переведите на русский: 'La revue est sur la table'", "correct": "Журнал на столе"},
        {"id": 44, "type": "text_input", "question": "📖 Переведите на русский: 'Il cherche cette fameuse rue'", "correct": "Он ищет эту знаменитую улицу"},
        {"id": 45, "type": "text_input", "question": "📖 Переведите на русский: 'Je regarde la lune'", "correct": "Я смотрю на луну"},
        {"id": 46, "type": "text_input", "question": "📖 Переведите на русский: 'Fumez là!'", "correct": "Курите там"},

        # ========== УПРАЖНЕНИЕ №11: ЗАПОЛНИТЕ ПРОПУСКИ ==========
        {"id": 47, "type": "text_input", "question": "✍️ Заполните пропуск: 'manuel, revue, ______' (livre)", "correct": "livre"},
        {"id": 48, "type": "text_input", "question": "✍️ Заполните пропуск: 'deux, quatre, ______' (huit)", "correct": "huit"},
        {"id": 49, "type": "text_input", "question": "✍️ Заполните пропуск: 'nuage, lune, ______' (ciel)", "correct": "ciel"},
        {"id": 50, "type": "text_input", "question": "✍️ Заполните пропуск: 'rivière, ______' (mer)", "correct": "mer"},
        {"id": 51, "type": "text_input", "question": "✍️ Заполните пропуск: 'monsieur, ______' (madame)", "correct": "madame"},
        {"id": 52, "type": "text_input", "question": "✍️ Заполните пропуск: 'capricieux, ______' (nerveux)", "correct": "nerveux"},
        {"id": 53, "type": "text_input", "question": "✍️ Заполните пропуск: 'délicieuse, ______' (merveilleuse)", "correct": "merveilleuse"},
        {"id": 54, "type": "text_input", "question": "✍️ Заполните пропуск: 'sage, ______' (calme)", "correct": "calme"},
        {"id": 55, "type": "text_input", "question": "✍️ Заполните пропуск: 'jeudi, samedi, ______' (mercredi)", "correct": "mercredi"},
        {"id": 56, "type": "text_input", "question": "✍️ Заполните пропуск: 'chercher, ______' (cacher)", "correct": "cacher"},
        {"id": 57, "type": "text_input", "question": "✍️ Заполните пропуск: 'gai, ______' (heureux)", "correct": "heureux"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'два'", "correct": "deux"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'синий'", "correct": "bleu"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'счастливый'", "correct": "heureux"},
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'капризный'", "correct": "capricieux"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'чудесный'", "correct": "merveilleux"},
        {"id": 63, "type": "text_input", "question": "🔄 Напишите по-французски 'ты'", "correct": "tu"},
        {"id": 64, "type": "text_input", "question": "🔄 Напишите по-французски 'музыка'", "correct": "musique"},
        {"id": 65, "type": "text_input", "question": "🔄 Напишите по-французски 'музей'", "correct": "musée"},
        {"id": 66, "type": "text_input", "question": "🔄 Напишите по-французски 'улица'", "correct": "rue"},
        {"id": 67, "type": "text_input", "question": "🔄 Напишите по-французски 'луна'", "correct": "lune"},
        {"id": 68, "type": "text_input", "question": "🔄 Напишите по-французски 'ночь'", "correct": "nuit"},
        {"id": 69, "type": "text_input", "question": "🔄 Напишите по-французски 'дождь'", "correct": "pluie"},
        {"id": 70, "type": "text_input", "question": "🔄 Напишите по-французски 'восемь'", "correct": "huit"},
        {"id": 71, "type": "text_input", "question": "🔄 Напишите по-французски 'облако'", "correct": "nuage"},
        {"id": 72, "type": "text_input", "question": "🔄 Напишите по-французски 'я хочу'", "correct": "je veux"},
        {"id": 73, "type": "text_input", "question": "🔄 Напишите по-французски 'я могу'", "correct": "je peux"},
        {"id": 74, "type": "text_input", "question": "🔄 Напишите по-французски 'я есть'", "correct": "je suis"},
        {"id": 75, "type": "text_input", "question": "🔄 Напишите по-французски 'я уверен'", "correct": "je suis sûr"},
        {"id": 76, "type": "text_input", "question": "🔄 Напишите по-французски 'я готов'", "correct": "je suis prêt"}
    ],
    "question": "Пройдите все 76 карточек практики!",
    "correct_answer": "готово"
}

# ---------- ДЕНЬ 18: УРОК 10 ----------
# ---------- ДЕНЬ 18: УРОК 10 (Носовые гласные [ɛ̃] и [œ̃]) ----------
COURSE_DAYS[18] = {
    "title": "Урок 10: Носовые гласные [ɛ̃] и [œ̃]",
    "type": "lesson",
    "has_alphabet": False,
    "sounds_table": [
        {
            "sound": "носовой гласный [ɛ̃]",
            "russian": "отсутствует",
            "letters": "in, im<br>ain, aim<br>ein",
            "notes": "• Буквосочетания читаются как [ɛ̃] на конце слога или перед согласной (кроме m, n).<br>• 'Мычите с открытым ртом' → произнесите [ɛ] → получится [ɛ̃]!<br>• Никакого призвука [n] на конце быть не должно!"
        },
        {
            "sound": "носовой гласный [œ̃]",
            "russian": "отсутствует",
            "letters": "un, um",
            "notes": "• Буквосочетания un, um читаются как [œ̃] на конце слога или перед согласной.<br>• Прием: 'мычите с открытым ртом' + [œ] → [œ̃]"
        },
        {
            "sound": "сочетание [jɛ̃]",
            "russian": "",
            "letters": "ien",
            "notes": "Буквосочетание ien на конце слога читается как [jɛ̃]."
        },
        {
            "sound": "сочетание [jɛn]",
            "russian": "",
            "letters": "ienn",
            "notes": "Буквосочетание ienn в любой позиции читается как [jɛn] (с чистым, не носовым [ɛ])."
        }
    ],
    "grammar_blocks": [
        {
            "subtitle": "🎯 Как произнести носовой гласный [ɛ̃]",
            "text": "Носовые гласные — воздух проходит через рот И через нос!<br><br>"
                    "Прием 'мычания с открытым ртом':<br>"
                    "1️⃣ Представьте, что вы не расслышали вопрос и переспрашиваете, издавая 'ммм...' с закрытым ртом.<br>"
                    "2️⃣ Потяните этот звук как можно дольше.<br>"
                    "3️⃣ Не переставая тянуть, откройте рот.<br>"
                    "4️⃣ Затем придайте органам речи положение для звука [ɛ].<br><br>"
                    "Получится носовой [ɛ̃]!<br>"
                    "⚠️ Никакого призвука [n] на конце быть не должно!"
        },
        {
            "subtitle": "🎯 Как произнести носовой гласный [œ̃]",
            "text": "Используйте тот же прием 'мычания с открытым ртом':<br><br>"
                    "1️⃣ 'Мычите с открытым ртом'<br>"
                    "2️⃣ Не прекращая мычания, произнесите звук [œ]<br><br>"
                    "Получится носовой [œ̃]!<br>"
                    "Примеры: un [œ̃] — один, brun [brœ̃] — коричневый"
        },
        {
            "subtitle": "🔗 Связывание (liaison) с носовыми гласными",
            "text": "Если носовой гласный [ɛ̃] или [œ̃] на конце слова оказывается перед гласным следующего слова,<br>"
                    "то между ними вставляется звук <b>[n]</b> или <b>[m]</b> (в зависимости от написания).<br><br>"
                    "Примеры:<br>"
                    "• le train arrive [lə trɛ̃ n ariv] — поезд прибывает<br>"
                    "• une faim affreuse [yn fɛ̃ m afrøz] — ужасный голод<br>"
                    "• un écrivain [œ̃ n ekrivɛ̃] — писатель"
        },
        {
            "subtitle": "📝 Неопределенный артикль",
            "text": "• <b>un</b> [œ̃] — неопределенный артикль мужского рода единственного числа<br>"
                    "• <b>une</b> [yn] — неопределенный артикль женского рода единственного числа<br><br>"
                    "Примеры: un livre [œ̃ livr] — книга, une chaise [yn ʃɛz] — стул"
        },
        {
            "subtitle": "🎧 Упражнение № 1. Произнесите, четко противопоставляя чистый звук [ɛ] носовому [ɛ̃]:",
            "text": "[ɛ — ɛ̃], [mɛ — mɛ̃], [tɛ — tɛ̃], [vɛ — vɛ̃], [lɛ — lɛ̃], [dɛ — dɛ̃], [rɛ — rɛ̃], [sɛ — sɛ̃], [kɛ — kɛ̃]"
        },
        {
            "subtitle": "🎧 Упражнение № 2. Прочтите слова, стараясь запомнить их:",
            "text": "• vin [vɛ̃] m — вино<br>"
                    "• fin [fɛ̃] f — конец<br>"
                    "• faim [fɛ̃] f — голод<br>"
                    "• matin [matɛ̃] m — утро<br>"
                    "• le matin [lə matɛ̃] — утром<br>"
                    "• magasin [magazɛ̃] m — магазин<br>"
                    "• jardin [ʒardɛ̃] m — сад<br>"
                    "• médecin [medsɛ̃] m — врач<br>"
                    "• train [trɛ̃] m — поезд<br>"
                    "• pain [pɛ̃] m — хлеб<br>"
                    "• vingt [vɛ̃] — двадцать<br>"
                    "• demain [dəmɛ̃] — завтра<br>"
                    "• écrivain [ekrivɛ̃] m — писатель<br>"
                    "• peintre [pɛ̃tr] m — художник"
        },
        {
            "subtitle": "🎧 Упражнение № 5. Прочтите по горизонтали, сравнивая, как звучат слова:",
            "text": "• Parisien [parizjɛ̃] m — парижанин<br>"
                    "• Lucien [lysjɛ̃] — Люсьен<br>"
                    "• chrétien [kretjɛ̃] m — христианский<br>"
                    "• italien [italjɛ̃] m — итальянский<br>"
                    "• Parisienne [parizjɛn] f — парижанка<br>"
                    "• Lucienne [lysjɛn] — Люсьенна<br>"
                    "• chrétienne [kretjɛn] f — христианская<br>"
                    "• italienne [italjɛn] f — итальянская"
        },
        {
            "subtitle": "🎧 Упражнение № 6. Прочтите:",
            "text": "[œ — œ̃], [lœ — lœ̃], [dœ — dœ̃], [kœ — kœ̃], [fœ — fœ̃], [bœ — bœ̃]"
        },
        {
            "subtitle": "🎧 Упражнение № 7. Прочтите и выучите слова:",
            "text": "• brun [brœ̃] m, brune [bryn] f — коричневый, -ая, -ое<br>"
                    "• chacun [ʃakœ̃] m — каждый<br>"
                    "• parfum [parfœ̃] m — духи<br>"
                    "• lundi [lœ̃di] m — понедельник"
        }
    ],
    "vocabulary": [
        {"fr": "vin", "tr": "[vɛ̃]", "ru": "вино (м.р.)"},
        {"fr": "fin", "tr": "[fɛ̃]", "ru": "конец (ж.р.)"},
        {"fr": "faim", "tr": "[fɛ̃]", "ru": "голод (ж.р.)"},
        {"fr": "matin", "tr": "[matɛ̃]", "ru": "утро (м.р.)"},
        {"fr": "le matin", "tr": "[lə matɛ̃]", "ru": "утром"},
        {"fr": "magasin", "tr": "[magazɛ̃]", "ru": "магазин (м.р.)"},
        {"fr": "jardin", "tr": "[ʒardɛ̃]", "ru": "сад (м.р.)"},
        {"fr": "médecin", "tr": "[medsɛ̃]", "ru": "врач (м.р.)"},
        {"fr": "train", "tr": "[trɛ̃]", "ru": "поезд (м.р.)"},
        {"fr": "pain", "tr": "[pɛ̃]", "ru": "хлеб (м.р.)"},
        {"fr": "vingt", "tr": "[vɛ̃]", "ru": "двадцать"},
        {"fr": "demain", "tr": "[dəmɛ̃]", "ru": "завтра"},
        {"fr": "écrivain", "tr": "[ekrivɛ̃]", "ru": "писатель (м.р.)"},
        {"fr": "peintre", "tr": "[pɛ̃tr]", "ru": "художник (м.р.)"},
        {"fr": "Parisien", "tr": "[parizjɛ̃]", "ru": "парижанин (м.р.)"},
        {"fr": "Parisienne", "tr": "[parizjɛn]", "ru": "парижанка (ж.р.)"},
        {"fr": "Lucien", "tr": "[lysjɛ̃]", "ru": "Люсьен"},
        {"fr": "Lucienne", "tr": "[lysjɛn]", "ru": "Люсьенна"},
        {"fr": "chrétien", "tr": "[kretjɛ̃]", "ru": "христианский (м.р.)"},
        {"fr": "chrétienne", "tr": "[kretjɛn]", "ru": "христианская (ж.р.)"},
        {"fr": "italien", "tr": "[italjɛ̃]", "ru": "итальянский (м.р.)"},
        {"fr": "italienne", "tr": "[italjɛn]", "ru": "итальянская (ж.р.)"},
        {"fr": "brun", "tr": "[brœ̃]", "ru": "коричневый (м.р.)"},
        {"fr": "brune", "tr": "[bryn]", "ru": "коричневая (ж.р.)"},
        {"fr": "chacun", "tr": "[ʃakœ̃]", "ru": "каждый"},
        {"fr": "parfum", "tr": "[parfœ̃]", "ru": "духи (м.р.)"},
        {"fr": "lundi", "tr": "[lœ̃di]", "ru": "понедельник (м.р.)"},
        {"fr": "un", "tr": "[œ̃]", "ru": "один, неопределенный артикль м.р."},
        {"fr": "une", "tr": "[yn]", "ru": "одна, неопределенный артикль ж.р."}
    ],
    "audio_tracks": [
        {"title": "Упражнение №1: Звук [ɛ̃]", "url": "/static/audio/lesson10_1.mp3"},
        {"title": "Упражнение №2: Слова с [ɛ̃]", "url": "/static/audio/lesson10_2.mp3"},
        {"title": "Упражнение №5: Буквосочетания ien/ienn", "url": "/static/audio/lesson10_3.mp3"},
        {"title": "Упражнение №6: Звук [œ̃]", "url": "/static/audio/lesson10_4.mp3"},
        {"title": "Упражнение №7: Слова с [œ̃]", "url": "/static/audio/lesson10_5.mp3"}
    ],
    "practice_tasks": [
        # ========== ФОНЕТИКА (quiz) ==========
        {"id": 1, "type": "quiz", "question": "🔊 Как читается 'in' в слове 'vin'?",
         "options": ["[in]", "[ɛ̃]", "[ɛn]", "[ĩ]"], "correct": "[ɛ̃]"},
        {"id": 2, "type": "quiz", "question": "🔊 Как читается 'ain' в слове 'pain'?",
         "options": ["[ɛ̃]", "[ɛn]", "[ain]", "[ɛ̃]"], "correct": "[ɛ̃]"},
        {"id": 3, "type": "quiz", "question": "🔊 Как правильно произнести носовой [ɛ̃]?",
         "options": ["Как [э] + призвук [н]", "Мычание с открытым ртом + [ɛ]", "Как [э] + [н] носовым", "Как [а] носовой"], "correct": "Мычание с открытым ртом + [ɛ]"},
        {"id": 4, "type": "quiz", "question": "🔊 Как читается 'un'?",
         "options": ["[yn]", "[œ̃]", "[un]", "[ɛ̃]"], "correct": "[œ̃]"},
        {"id": 5, "type": "quiz", "question": "🔊 Как читается 'ien' в слове 'Parisien'?",
         "options": ["[jɛ̃]", "[jɛn]", "[iɛ̃]", "[jɛ̃]"], "correct": "[jɛ̃]"},
        {"id": 6, "type": "quiz", "question": "🔊 Как читается 'ienn' в слове 'Parisienne'?",
         "options": ["[jɛ̃]", "[jɛn]", "[jɛn]", "[iɛn]"], "correct": "[jɛn]"},

        # ========== ПЕРЕВОД СЛОВ (quiz) ==========
        {"id": 7, "type": "quiz", "question": "📖 Как переводится 'vin'?",
         "options": ["Хлеб", "Вино", "Поезд", "Конец"], "correct": "Вино"},
        {"id": 8, "type": "quiz", "question": "📖 Как переводится 'train'?",
         "options": ["Поезд", "Машина", "Самолет", "Автобус"], "correct": "Поезд"},
        {"id": 9, "type": "quiz", "question": "📖 Как переводится 'pain'?",
         "options": ["Вино", "Хлеб", "Сыр", "Масло"], "correct": "Хлеб"},
        {"id": 10, "type": "quiz", "question": "📖 Как переводится 'faim'?",
         "options": ["Жажда", "Голод", "Усталость", "Сон"], "correct": "Голод"},
        {"id": 11, "type": "quiz", "question": "📖 Как переводится 'matin'?",
         "options": ["Вечер", "День", "Утро", "Ночь"], "correct": "Утро"},
        {"id": 12, "type": "quiz", "question": "📖 Как переводится 'magasin'?",
         "options": ["Дом", "Школа", "Магазин", "Больница"], "correct": "Магазин"},
        {"id": 13, "type": "quiz", "question": "📖 Как переводится 'jardin'?",
         "options": ["Лес", "Поле", "Сад", "Парк"], "correct": "Сад"},
        {"id": 14, "type": "quiz", "question": "📖 Как переводится 'médecin'?",
         "options": ["Учитель", "Врач", "Инженер", "Художник"], "correct": "Врач"},
        {"id": 15, "type": "quiz", "question": "📖 Как переводится 'demain'?",
         "options": ["Вчера", "Сегодня", "Завтра", "Сейчас"], "correct": "Завтра"},
        {"id": 16, "type": "quiz", "question": "📖 Как переводится 'parfum'?",
         "options": ["Духи", "Парфюм", "Аромат", "Запах"], "correct": "Духи"},
        {"id": 17, "type": "quiz", "question": "📖 Как переводится 'lundi'?",
         "options": ["Вторник", "Среда", "Понедельник", "Четверг"], "correct": "Понедельник"},
        {"id": 18, "type": "quiz", "question": "📖 Как переводится 'chacun'?",
         "options": ["Каждый", "Некоторые", "Все", "Многие"], "correct": "Каждый"},
        {"id": 19, "type": "quiz", "question": "📖 Как переводится 'brun'?",
         "options": ["Коричневый", "Красный", "Синий", "Зеленый"], "correct": "Коричневый"},
        {"id": 20, "type": "quiz", "question": "📖 Как переводится 'Parisien'?",
         "options": ["Парижанка", "Парижанин", "Парижский", "Из Парижа"], "correct": "Парижанин"},
        {"id": 21, "type": "quiz", "question": "📖 Как переводится 'Parisienne'?",
         "options": ["Парижанин", "Парижанка", "Парижский", "Из Парижа"], "correct": "Парижанка"},

        # ========== УПРАЖНЕНИЕ №3: ПРОЧТИТЕ ==========
        {"id": 22, "type": "text_input", "question": "📖 Прочитайте и переведите: 'ce magasin est...'", "correct": "этот магазин"},
        {"id": 23, "type": "text_input", "question": "📖 Прочитайте и переведите: 'le jardin est...'", "correct": "сад"},
        {"id": 24, "type": "text_input", "question": "📖 Прочитайте и переведите: 'le médecin aime...'", "correct": "врач любит"},
        {"id": 25, "type": "text_input", "question": "📖 Прочитайте и переведите: 'ce vin est...'", "correct": "это вино"},

        # ========== УПРАЖНЕНИЕ №4: ДОПИШИТЕ ==========
        {"id": 26, "type": "text_input", "question": "✍️ Допишите: 'Le train arrive...'", "correct": "поезд прибывает"},
        {"id": 27, "type": "text_input", "question": "✍️ Допишите: 'Ce magasin est...'", "correct": "этот магазин"},
        {"id": 28, "type": "text_input", "question": "✍️ Допишите: 'Le jardin est...'", "correct": "сад"},
        {"id": 29, "type": "text_input", "question": "✍️ Допишите: 'Le médecin aime...'", "correct": "врач любит"},
        {"id": 30, "type": "text_input", "question": "✍️ Допишите: 'Ce vin est...'", "correct": "это вино"},
        {"id": 31, "type": "text_input", "question": "✍️ Допишите: 'La faim est...'", "correct": "голод"},

        # ========== УПРАЖНЕНИЕ №8: ОПРЕДЕЛИТЕ РОД СЛОВ ==========
        {"id": 32, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'Parisienne'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 33, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'chaise'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 34, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'musée'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 35, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'Parisien'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 36, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'image'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 37, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'peintre'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 38, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'rue'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 39, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'revue'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 40, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'magasin'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 41, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'table'?",
         "options": ["un", "une"], "correct": "une"},
        {"id": 42, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'médecin'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 43, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'nuage'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 44, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'écrivain'?",
         "options": ["un", "une"], "correct": "un"},
        {"id": 45, "type": "quiz", "question": "📚 Какой артикль нужно поставить перед 'étage'?",
         "options": ["un", "une"], "correct": "un"},

        # ========== УПРАЖНЕНИЕ №9: ПЕРЕВОД ФРАЗ ==========
        {"id": 46, "type": "text_input", "question": "📖 Переведите на русский: 'Lucien arrive lundi'", "correct": "Люсьен приезжает в понедельник"},
        {"id": 47, "type": "text_input", "question": "📖 Переведите на русский: 'Lucienne aime ce parfum'", "correct": "Люсьенна любит эти духи"},
        {"id": 48, "type": "text_input", "question": "📖 Переведите на русский: 'Chacun veut visiter Paris'", "correct": "Каждый хочет посетить Париж"},
        {"id": 49, "type": "text_input", "question": "📖 Переведите на русский: 'Le médecin travaille chaque matin'", "correct": "Врач работает каждое утро"},
        {"id": 50, "type": "text_input", "question": "📖 Переведите на русский: 'Le verre est plein'", "correct": "Стакан полный"},
        {"id": 51, "type": "text_input", "question": "📖 Переведите на русский: 'Nana aime les peintres italiens'", "correct": "Нана любит итальянских художников"},
        {"id": 52, "type": "text_input", "question": "📖 Переведите на русский: 'Une revue chrétienne est sur la table'", "correct": "Христианский журнал на столе"},

        # ========== ПЕРЕВОД С РУССКОГО ==========
        {"id": 53, "type": "text_input", "question": "🔄 Переведите на французский: 'завтра утром'", "correct": "demain matin"},
        {"id": 54, "type": "text_input", "question": "🔄 Переведите на французский: 'каждый понедельник'", "correct": "chaque lundi"},
        {"id": 55, "type": "text_input", "question": "🔄 Переведите на французский: 'этот магазин очень дорогой'", "correct": "ce magasin est très cher"},
        {"id": 56, "type": "text_input", "question": "🔄 Переведите на французский: 'Люсьенна любит эти духи'", "correct": "Lucienne aime ce parfum"},

        # ========== ПЕРЕВОД С РУССКОГО (слова) ==========
        {"id": 57, "type": "text_input", "question": "🔄 Напишите по-французски 'вино'", "correct": "vin"},
        {"id": 58, "type": "text_input", "question": "🔄 Напишите по-французски 'хлеб'", "correct": "pain"},
        {"id": 59, "type": "text_input", "question": "🔄 Напишите по-французски 'утро'", "correct": "matin"},
        {"id": 60, "type": "text_input", "question": "🔄 Напишите по-французски 'магазин'", "correct": "magasin"},
        {"id": 61, "type": "text_input", "question": "🔄 Напишите по-французски 'сад'", "correct": "jardin"},
        {"id": 62, "type": "text_input", "question": "🔄 Напишите по-французски 'врач'", "correct": "médecin"},
        {"id": 63, "type": "text_input", "question": "🔄 Напишите по-французски 'писатель'", "correct": "écrivain"},
        {"id": 64, "type": "text_input", "question": "🔄 Напишите по-французски 'художник'", "correct": "peintre"},
        {"id": 65, "type": "text_input", "question": "🔄 Напишите по-французски 'завтра'", "correct": "demain"},
        {"id": 66, "type": "text_input", "question": "🔄 Напишите по-французски 'духи'", "correct": "parfum"},
        {"id": 67, "type": "text_input", "question": "🔄 Напишите по-французски 'понедельник'", "correct": "lundi"},
        {"id": 68, "type": "text_input", "question": "🔄 Напишите по-французски 'каждый'", "correct": "chacun"},
        {"id": 69, "type": "text_input", "question": "🔄 Напишите по-французски 'коричневый'", "correct": "brun"},
        {"id": 70, "type": "text_input", "question": "🔄 Напишите по-французски 'парижанин'", "correct": "Parisien"},
        {"id": 71, "type": "text_input", "question": "🔄 Напишите по-французски 'парижанка'", "correct": "Parisienne"},
        {"id": 72, "type": "text_input", "question": "🔄 Напишите по-французски 'итальянский'", "correct": "italien"},
        {"id": 73, "type": "text_input", "question": "🔄 Напишите по-французски 'христианский'", "correct": "chrétien"}
    ],
    "question": "Пройдите все 73 карточки практики!",
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
# ---------- ДЕНЬ 20: ТЕСТ 5 (Уроки 9-10 / дни 17-18) ----------
COURSE_DAYS[20] = {
    "title": "Тест 5: Уроки 9-10 (Звуки [ø], [y], [ɥ] и носовые [ɛ̃], [œ̃])",
    "type": "test",
    "is_test": True,
    "practice_tasks": [
        # ============================================================
        # ЧАСТЬ 1: ДИКТАНТ СЛОВ ИЗ УРОКА 9 (звуки [ø], [y], [ɥ])
        # ============================================================
        {"id": 1, "type": "text_input", "question": "📝 Напишите по-французски: 'два'", "correct": "deux"},
        {"id": 2, "type": "text_input", "question": "📝 Напишите по-французски: 'синий'", "correct": "bleu"},
        {"id": 3, "type": "text_input", "question": "📝 Напишите по-французски: 'огонь'", "correct": "feu"},
        {"id": 4, "type": "text_input", "question": "📝 Напишите по-французски: 'игра'", "correct": "jeu"},
        {"id": 5, "type": "text_input", "question": "📝 Напишите по-французски: 'он хочет'", "correct": "il veut"},
        {"id": 6, "type": "text_input", "question": "📝 Напишите по-французски: 'он может'", "correct": "il peut"},
        {"id": 7, "type": "text_input", "question": "📝 Напишите по-французски: 'я хочу'", "correct": "je veux"},
        {"id": 8, "type": "text_input", "question": "📝 Напишите по-французски: 'я могу'", "correct": "je peux"},
        {"id": 9, "type": "text_input", "question": "📝 Напишите по-французски: 'ленивый' (м.р.)", "correct": "paresseux"},
        {"id": 10, "type": "text_input", "question": "📝 Напишите по-французски: 'мир'", "correct": "paix"},
        {"id": 11, "type": "text_input", "question": "📝 Напишите по-французски: 'прощайте'", "correct": "adieux"},
        {"id": 12, "type": "text_input", "question": "📝 Напишите по-французски: 'господин'", "correct": "monsieur"},
        {"id": 13, "type": "text_input", "question": "📝 Напишите по-французски: 'господа'", "correct": "messieurs"},
        {"id": 14, "type": "text_input", "question": "📝 Напишите по-французски: 'ужасный' (м.р.)", "correct": "affreux"},
        {"id": 15, "type": "text_input", "question": "📝 Напишите по-французски: 'капризный' (м.р.)", "correct": "capricieux"},
        {"id": 16, "type": "text_input", "question": "📝 Напишите по-французски: 'восхитительный' (м.р.)", "correct": "délicieux"},
        {"id": 17, "type": "text_input", "question": "📝 Напишите по-французски: 'знаменитый' (м.р.)", "correct": "fameux"},
        {"id": 18, "type": "text_input", "question": "📝 Напишите по-французски: 'счастливый' (м.р.)", "correct": "heureux"},
        {"id": 19, "type": "text_input", "question": "📝 Напишите по-французски: 'чудесный' (м.р.)", "correct": "merveilleux"},
        {"id": 20, "type": "text_input", "question": "📝 Напишите по-французски: 'нервный' (м.р.)", "correct": "nerveux"},
        {"id": 21, "type": "text_input", "question": "📝 Напишите по-французски: 'драгоценный' (м.р.)", "correct": "précieux"},
        {"id": 22, "type": "text_input", "question": "📝 Напишите по-французски: 'ты'", "correct": "tu"},
        {"id": 23, "type": "text_input", "question": "📝 Напишите по-французски: 'музыка'", "correct": "musique"},
        {"id": 24, "type": "text_input", "question": "📝 Напишите по-французски: 'музей'", "correct": "musée"},
        {"id": 25, "type": "text_input", "question": "📝 Напишите по-французски: 'журнал, обозрение'", "correct": "revue"},
        {"id": 26, "type": "text_input", "question": "📝 Напишите по-французски: 'улица'", "correct": "rue"},
        {"id": 27, "type": "text_input", "question": "📝 Напишите по-французски: 'уверенный' (м.р.)", "correct": "sûr"},
        {"id": 28, "type": "text_input", "question": "📝 Напишите по-французски: 'луна'", "correct": "lune"},
        {"id": 29, "type": "text_input", "question": "📝 Напишите по-французски: 'курить'", "correct": "fumer"},
        {"id": 30, "type": "text_input", "question": "📝 Напишите по-французски: 'я есть'", "correct": "je suis"},
        {"id": 31, "type": "text_input", "question": "📝 Напишите по-французски: 'я уверен'", "correct": "je suis sûr"},
        {"id": 32, "type": "text_input", "question": "📝 Напишите по-французски: 'я готов'", "correct": "je suis prêt"},
        {"id": 33, "type": "text_input", "question": "📝 Напишите по-французски: 'я удивлен'", "correct": "je suis surpris"},
        {"id": 34, "type": "text_input", "question": "📝 Напишите по-французски: 'ночь'", "correct": "nuit"},
        {"id": 35, "type": "text_input", "question": "📝 Напишите по-французски: 'дождь'", "correct": "pluie"},
        {"id": 36, "type": "text_input", "question": "📝 Напишите по-французски: 'восемь'", "correct": "huit"},
        {"id": 37, "type": "text_input", "question": "📝 Напишите по-французски: 'учебник'", "correct": "manuel"},
        {"id": 38, "type": "text_input", "question": "📝 Напишите по-французски: 'облако, туча'", "correct": "nuage"},
        {"id": 39, "type": "text_input", "question": "📝 Напишите по-французски: 'плодотворный' (м.р.)", "correct": "fructueux"},

        # ============================================================
        # ЧАСТЬ 2: ДИКТАНТ СЛОВ ИЗ УРОКА 10 (носовые [ɛ̃] и [œ̃])
        # ============================================================
        {"id": 40, "type": "text_input", "question": "📝 Напишите по-французски: 'вино'", "correct": "vin"},
        {"id": 41, "type": "text_input", "question": "📝 Напишите по-французски: 'конец'", "correct": "fin"},
        {"id": 42, "type": "text_input", "question": "📝 Напишите по-французски: 'голод'", "correct": "faim"},
        {"id": 43, "type": "text_input", "question": "📝 Напишите по-французски: 'утро'", "correct": "matin"},
        {"id": 44, "type": "text_input", "question": "📝 Напишите по-французски: 'магазин'", "correct": "magasin"},
        {"id": 45, "type": "text_input", "question": "📝 Напишите по-французски: 'сад'", "correct": "jardin"},
        {"id": 46, "type": "text_input", "question": "📝 Напишите по-французски: 'врач'", "correct": "médecin"},
        {"id": 47, "type": "text_input", "question": "📝 Напишите по-французски: 'поезд'", "correct": "train"},
        {"id": 48, "type": "text_input", "question": "📝 Напишите по-французски: 'хлеб'", "correct": "pain"},
        {"id": 49, "type": "text_input", "question": "📝 Напишите по-французски: 'двадцать'", "correct": "vingt"},
        {"id": 50, "type": "text_input", "question": "📝 Напишите по-французски: 'завтра'", "correct": "demain"},
        {"id": 51, "type": "text_input", "question": "📝 Напишите по-французски: 'писатель'", "correct": "écrivain"},
        {"id": 52, "type": "text_input", "question": "📝 Напишите по-французски: 'художник'", "correct": "peintre"},
        {"id": 53, "type": "text_input", "question": "📝 Напишите по-французски: 'парижанин'", "correct": "Parisien"},
        {"id": 54, "type": "text_input", "question": "📝 Напишите по-французски: 'парижанка'", "correct": "Parisienne"},
        {"id": 55, "type": "text_input", "question": "📝 Напишите по-французски: 'итальянский' (м.р.)", "correct": "italien"},
        {"id": 56, "type": "text_input", "question": "📝 Напишите по-французски: 'христианский' (м.р.)", "correct": "chrétien"},
        {"id": 57, "type": "text_input", "question": "📝 Напишите по-французски: 'коричневый' (м.р.)", "correct": "brun"},
        {"id": 58, "type": "text_input", "question": "📝 Напишите по-французски: 'каждый'", "correct": "chacun"},
        {"id": 59, "type": "text_input", "question": "📝 Напишите по-французски: 'духи'", "correct": "parfum"},
        {"id": 60, "type": "text_input", "question": "📝 Напишите по-французски: 'понедельник'", "correct": "lundi"},

        # ============================================================
        # ЧАСТЬ 3: ФОНЕТИКА И ПРАВИЛА (quiz)
        # ============================================================
        {"id": 61, "type": "quiz", "question": "🔊 Как читается 'eu' в слове 'deux' (на конце)?",
         "options": ["[œ]", "[ø]", "[ə]", "[y]"], "correct": "[ø]"},
        {"id": 62, "type": "quiz", "question": "🔊 Как читается буква 'u' в слове 'tu'?",
         "options": ["[u]", "[y]", "[ø]", "[œ]"], "correct": "[y]"},
        {"id": 63, "type": "quiz", "question": "🔊 Как читается 'ui' в слове 'nuit'?",
         "options": ["[ui]", "[ɥi]", "[y]", "[wi]"], "correct": "[ɥi]"},
        {"id": 64, "type": "quiz", "question": "🔊 Как читается 'in' в слове 'vin'?",
         "options": ["[in]", "[ɛ̃]", "[ɛn]", "[ĩ]"], "correct": "[ɛ̃]"},
        {"id": 65, "type": "quiz", "question": "🔊 Как читается 'un'?",
         "options": ["[yn]", "[œ̃]", "[un]", "[ɛ̃]"], "correct": "[œ̃]"},
        {"id": 66, "type": "quiz", "question": "🔊 Как читается 'ien' в слове 'Parisien'?",
         "options": ["[jɛ̃]", "[jɛn]", "[iɛ̃]", "[jɛ̃]"], "correct": "[jɛ̃]"},
        {"id": 67, "type": "quiz", "question": "🔊 Читается ли буква 'x' на конце слов?",
         "options": ["Да, всегда", "Нет, не читается", "Только в заимствованиях", "Только перед гласной"], "correct": "Нет, не читается"},

        # ============================================================
        # ЧАСТЬ 4: ТРАНСКРИПЦИЯ (text_input)
        # ============================================================
        {"id": 68, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'deux'", "correct": "[dø]"},
        {"id": 69, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'heureux'", "correct": "[œrø]"},
        {"id": 70, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'musique'", "correct": "[myzik]"},
        {"id": 71, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'nuit'", "correct": "[nɥi]"},
        {"id": 72, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'vin'", "correct": "[vɛ̃]"},
        {"id": 73, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'pain'", "correct": "[pɛ̃]"},
        {"id": 74, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'brun'", "correct": "[brœ̃]"},
        {"id": 75, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'parfum'", "correct": "[parfœ̃]"},
        {"id": 76, "type": "text_input", "question": "📝 Запишите транскрипцию слова 'chacun'", "correct": "[ʃakœ̃]"},

        # ============================================================
        # ЧАСТЬ 5: ПЕРЕВОД ФРАЗ (text_input)
        # ============================================================
        {"id": 77, "type": "text_input", "question": "📖 Переведите на русский: 'Le ciel est bleu'", "correct": "Небо голубое"},
        {"id": 78, "type": "text_input", "question": "📖 Переведите на русский: 'Il est gai et heureux'", "correct": "Он веселый и счастливый"},
        {"id": 79, "type": "text_input", "question": "📖 Переведите на русский: 'Je peux quitter la clinique mercredi'", "correct": "Я могу покинуть клинику в среду"},
        {"id": 80, "type": "text_input", "question": "📖 Переведите на русский: 'Tu as une amie'", "correct": "У тебя есть подруга"},
        {"id": 81, "type": "text_input", "question": "📖 Переведите на русский: 'La musique est merveilleuse'", "correct": "Музыка чудесная"},
        {"id": 82, "type": "text_input", "question": "📖 Переведите на русский: 'Je regarde la lune'", "correct": "Я смотрю на луну"},
        {"id": 83, "type": "text_input", "question": "📖 Переведите на русский: 'Lucien arrive lundi'", "correct": "Люсьен приезжает в понедельник"},
        {"id": 84, "type": "text_input", "question": "📖 Переведите на русский: 'Chacun veut visiter Paris'", "correct": "Каждый хочет посетить Париж"},
        {"id": 85, "type": "text_input", "question": "📖 Переведите на русский: 'Le verre est plein'", "correct": "Стакан полный"},
        {"id": 86, "type": "text_input", "question": "📖 Переведите на русский: 'Nana aime les peintres italiens'", "correct": "Нана любит итальянских художников"},

        # ============================================================
        # ЧАСТЬ 6: ПЕРЕВОД С РУССКОГО (text_input)
        # ============================================================
        {"id": 87, "type": "text_input", "question": "🔄 Переведите на французский: 'Я хочу приехать в четверг.'", "correct": "Je veux arriver jeudi"},
        {"id": 88, "type": "text_input", "question": "🔄 Переведите на французский: 'Небо чудесное.'", "correct": "Le ciel est merveilleux"},
        {"id": 89, "type": "text_input", "question": "🔄 Переведите на французский: 'Она спокойна и счастлива.'", "correct": "Elle est calme et heureuse"},
        {"id": 90, "type": "text_input", "question": "🔄 Переведите на французский: 'У мадам чудесное лицо.'", "correct": "Madame a un visage merveilleux"},
        {"id": 91, "type": "text_input", "question": "🔄 Переведите на французский: 'завтра утром'", "correct": "demain matin"},
        {"id": 92, "type": "text_input", "question": "🔄 Переведите на французский: 'каждый понедельник'", "correct": "chaque lundi"},
        {"id": 93, "type": "text_input", "question": "🔄 Переведите на французский: 'этот магазин очень дорогой'", "correct": "ce magasin est très cher"},
        {"id": 94, "type": "text_input", "question": "🔄 Переведите на французский: 'Люсьенна любит эти духи'", "correct": "Lucienne aime ce parfum"},

        # ============================================================
        # ЧАСТЬ 7: ПЕРЕВОД СЛОВ (quiz)
        # ============================================================
        {"id": 95, "type": "quiz", "question": "📖 Как переводится 'heureux'?",
         "options": ["Грустный", "Счастливый", "Злой", "Усталый"], "correct": "Счастливый"},
        {"id": 96, "type": "quiz", "question": "📖 Как переводится 'capricieux'?",
         "options": ["Спокойный", "Капризный", "Веселый", "Грустный"], "correct": "Капризный"},
        {"id": 97, "type": "quiz", "question": "📖 Как переводится 'merveilleux'?",
         "options": ["Обычный", "Чудесный", "Плохой", "Скучный"], "correct": "Чудесный"},
        {"id": 98, "type": "quiz", "question": "📖 Как переводится 'nuit'?",
         "options": ["День", "Ночь", "Утро", "Вечер"], "correct": "Ночь"},
        {"id": 99, "type": "quiz", "question": "📖 Как переводится 'pluie'?",
         "options": ["Снег", "Дождь", "Ветер", "Гроза"], "correct": "Дождь"},
        {"id": 100, "type": "quiz", "question": "📖 Как переводится 'vin'?",
         "options": ["Хлеб", "Вино", "Поезд", "Конец"], "correct": "Вино"},
        {"id": 101, "type": "quiz", "question": "📖 Как переводится 'pain'?",
         "options": ["Вино", "Хлеб", "Сыр", "Масло"], "correct": "Хлеб"},
        {"id": 102, "type": "quiz", "question": "📖 Как переводится 'magasin'?",
         "options": ["Дом", "Школа", "Магазин", "Больница"], "correct": "Магазин"},
        {"id": 103, "type": "quiz", "question": "📖 Как переводится 'jardin'?",
         "options": ["Лес", "Поле", "Сад", "Парк"], "correct": "Сад"},
        {"id": 104, "type": "quiz", "question": "📖 Как переводится 'médecin'?",
         "options": ["Учитель", "Врач", "Инженер", "Художник"], "correct": "Врач"},

        # ============================================================
        # ЧАСТЬ 8: ПЕРЕВОД С РУССКОГО (слова, text_input)
        # ============================================================
        {"id": 105, "type": "text_input", "question": "🔄 Напишите по-французски 'счастливый'", "correct": "heureux"},
        {"id": 106, "type": "text_input", "question": "🔄 Напишите по-французски 'капризный'", "correct": "capricieux"},
        {"id": 107, "type": "text_input", "question": "🔄 Напишите по-французски 'чудесный'", "correct": "merveilleux"},
        {"id": 108, "type": "text_input", "question": "🔄 Напишите по-французски 'ночь'", "correct": "nuit"},
        {"id": 109, "type": "text_input", "question": "🔄 Напишите по-французски 'дождь'", "correct": "pluie"},
        {"id": 110, "type": "text_input", "question": "🔄 Напишите по-французски 'вино'", "correct": "vin"},
        {"id": 111, "type": "text_input", "question": "🔄 Напишите по-французски 'хлеб'", "correct": "pain"},
        {"id": 112, "type": "text_input", "question": "🔄 Напишите по-французски 'магазин'", "correct": "magasin"},
        {"id": 113, "type": "text_input", "question": "🔄 Напишите по-французски 'сад'", "correct": "jardin"},
        {"id": 114, "type": "text_input", "question": "🔄 Напишите по-французски 'врач'", "correct": "médecin"},
        {"id": 115, "type": "text_input", "question": "🔄 Напишите по-французски 'завтра'", "correct": "demain"},
        {"id": 116, "type": "text_input", "question": "🔄 Напишите по-французски 'понедельник'", "correct": "lundi"},
        {"id": 117, "type": "text_input", "question": "🔄 Напишите по-французски 'духи'", "correct": "parfum"},
        {"id": 118, "type": "text_input", "question": "🔄 Напишите по-французски 'коричневый'", "correct": "brun"},
        {"id": 119, "type": "text_input", "question": "🔄 Напишите по-французски 'парижанин'", "correct": "Parisien"},
        {"id": 120, "type": "text_input", "question": "🔄 Напишите по-французски 'итальянский'", "correct": "italien"},
        {"id": 121, "type": "text_input", "question": "🔄 Напишите по-французски 'я уверен'", "correct": "je suis sûr"},
        {"id": 122, "type": "text_input", "question": "🔄 Напишите по-французски 'я готов'", "correct": "je suis prêt"},
        {"id": 123, "type": "text_input", "question": "🔄 Напишите по-французски 'я удивлен'", "correct": "je suis surpris"},

        # ============================================================
        # ЧАСТЬ 9: ОПРЕДЕЛИТЕ РОД СЛОВ (quiz)
        # ============================================================
        {"id": 124, "type": "quiz", "question": "📚 Какого рода слово 'musique'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 125, "type": "quiz", "question": "📚 Какого рода слово 'musée'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 126, "type": "quiz", "question": "📚 Какого рода слово 'revue'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 127, "type": "quiz", "question": "📚 Какого рода слово 'rue'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 128, "type": "quiz", "question": "📚 Какого рода слово 'lune'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 129, "type": "quiz", "question": "📚 Какого рода слово 'nuit'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 130, "type": "quiz", "question": "📚 Какого рода слово 'pluie'?",
         "options": ["Мужской", "Женский"], "correct": "Женский"},
        {"id": 131, "type": "quiz", "question": "📚 Какого рода слово 'parfum'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 132, "type": "quiz", "question": "📚 Какого рода слово 'jardin'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 133, "type": "quiz", "question": "📚 Какого рода слово 'magasin'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 134, "type": "quiz", "question": "📚 Какого рода слово 'médecin'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 135, "type": "quiz", "question": "📚 Какого рода слово 'écrivain'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"},
        {"id": 136, "type": "quiz", "question": "📚 Какого рода слово 'peintre'?",
         "options": ["Мужской", "Женский"], "correct": "Мужской"}
    ],
    "question": "Пройдите все 136 вопросов теста!",
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