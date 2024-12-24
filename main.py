# Домашнее задание по теме "Оператор "with"


class WordsFinder:
    def __init__(self, *filenames):
        self.file_names = filenames

    def get_all_words(self):
        all_words = {}

        punctuation_to_remove = [',', '.', '=', '!', '?', ';', ':', '-', '(', ')']

        for filename in self.file_names:
            with open(filename, encoding='utf-8') as f:
                content = f.read()

            # Удаляем знаки препинания
            for punc in punctuation_to_remove:
                content = content.replace(punc, '')

            # Приводим к нижнему регистру и разбиваем на слова
            words = content.lower().split()

            all_words[filename] = words

        return all_words

    def find(self, word):
        result = {}
        word = word.lower()

        for filename, words in self.get_all_words().items():
            try:
                index = words.index(word)
                result[filename] = index + 1  # Индексация начинается с 1
            except ValueError:
                pass  # Слово не найдено, ничего не добавляем в результат

        return result

    def count(self, word):
        result = {}
        word = word.lower()

        for filename, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[filename] = count

        return result



# Создание экземпляра класса
finder2 = WordsFinder('test_file.txt')

# Получение всех слов
print(finder2.get_all_words())

# Поиск позиции первого вхождения слова 'TEXT'
print(finder2.find('TEXT'))

# Подсчет количества вхождений слова 'teXT'
print(finder2.count('teXT'))



