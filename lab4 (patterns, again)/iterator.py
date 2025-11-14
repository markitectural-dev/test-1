class WordsCollection:
    """Коллекция слов, по которой можно итерироваться."""
    def __init__(self, words):
        self._words = words

    def __iter__(self):
        # Каждый раз при for возвращаем новый итератор
        return WordsIterator(self._words)


class WordsIterator:
    """Простой итератор по списку слов."""
    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._words):
            word = self._words[self._index]
            self._index += 1
            return word
        # Сигнал Python'у, что элементы закончились
        raise StopIteration

if __name__ == "__main__":
    print("=== ITERATOR ===")
    words = WordsCollection(["Python", "Patterns (again)", "Are", "Cool"])
    for w in words:
        print("Слово:", w)
