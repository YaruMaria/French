import re
import json


# Собираем все тексты из reading_data.py
def extract_all_words():
    from reading_data import READINGS

    all_words = set()

    # Обходим все части книги
    for book_id, book_data in READINGS.items():
        parts = book_data.get('parts', {})
        for part_num, part_data in parts.items():
            text = part_data.get('text', '')

            # Извлекаем все слова из HTML-текста (убираем теги)
            clean_text = re.sub(r'<[^>]+>', ' ', text)

            # Разбиваем на слова (только буквы, апострофы, дефисы)
            words = re.findall(r"[a-zA-ZÀ-ÿ'’\-]+", clean_text.lower())

            for word in words:
                # Очищаем от лишних символов
                word = word.strip("'’")
                if len(word) > 1 or word in ['a', 'y', 'z']:  # пропускаем слишком короткие
                    all_words.add(word)

    # Сохраняем в файл
    word_list = sorted(list(all_words))

    with open('all_words.txt', 'w', encoding='utf-8') as f:
        for word in word_list:
            f.write(word + '\n')

    print(f"Найдено уникальных слов: {len(word_list)}")
    print("Список сохранён в all_words.txt")


if __name__ == "__main__":
    extract_all_words()