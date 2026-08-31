import itertools


# ==========================================
# Завдання 1: Ітератор «Ланцюжок доручень»
# ==========================================
class ChainOfOrders:
    def __init__(self, people: list):
        self.people = list(people)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if not self.people or self.index >= len(self.people):
            raise StopIteration

        # Якщо всього один елемент у списку
        if len(self.people) == 1:
            self.index += 1
            return f"{self.people[0]} каже: теля прив'язав!"

        current_person = self.people[self.index]

        # Останній у ланцюжку
        if self.index == len(self.people) - 1:
            self.index += 1
            return f"{current_person} каже: теля прив'язав!"

        # Перший або проміжний
        next_person = self.people[self.index + 1]
        self.index += 1

        # Граматична форма для давального відмінка
        next_person_dative = self._to_dative(next_person)
        return f"{current_person} каже {next_person_dative}: передай далі!"

    @staticmethod
    def _to_dative(name: str) -> str:
        """Допоміжний метод для відмінювання імен у давальний відмінок."""
        if name.endswith("о"):
            return name[:-1] + "ві"  # Батько -> Батькові, Василько -> Василькові
        elif name.endswith("ик"):
            return name + "у"  # Михайлик -> Михайлику
        elif name.endswith("а"):
            return name[:-1] + "і"  # Горпина -> Горпині
        return name


# ==========================================
# Завдання 2: Генератор «Чутка по селу»
# ==========================================
def village_rumor(start_message: str, people: list):
    if not people:
        return

    history = []
    for i, person in enumerate(people):
        if i == 0:
            yield f'{person} каже: "{start_message}"'
            history.append(f"(переказав {person})")
        elif i == len(people) - 1:
            history_str = " ".join(history)
            yield f'{person} переказує: "{start_message} {history_str} (і всі дізналися!)"'
        else:
            history_str = " ".join(history)
            yield f'{person} переказує: "{start_message} {history_str}"'
            history.append(f"(переказав {person})")


# ==========================================
# Завдання 3: Генераторний вираз
# ==========================================
events = [
    "Михайлик передав доручення",
    "Василько відмовився",
    "Грицько передав доручення",
    "Оленка прив'язала теля",
    "Данилко передав доручення",
]

# Генераторний вираз
count = sum(1 for event in events if "передав доручення" in event)


# ==========================================
# Завдання 4: Нескінченний генератор
# ==========================================
def toloka_queue(workers: list):
    if not workers:
        return
    while True:
        for worker in workers:
            yield f"Черга: {worker}"


# ==========================================
# Завдання 5: Ліниве читання
# ==========================================
def find_calf(log):
    for line in log:
        if "прив'язав" in line or "прив'язала" in line:
            yield line
            break


# ==========================================
# Перевірка виконання всіх завдань
# ==========================================
if __name__ == "__main__":
    print("--- Завдання 1 ---")
    chain = ChainOfOrders(["Дід", "Батько", "Михайлик", "Василько"])
    for message in chain:
        print(message)

    print("\n--- Завдання 2 ---")
    for version in village_rumor("Теля втекло!", ["Горпина", "Параска", "Явдоха", "Оксана"]):
        print(version)

    print("\n--- Завдання 3 ---")
    print(f"Доручення передавали {count} рази")

    print("\n--- Завдання 4 ---")
    queue = toloka_queue(["Іван", "Марія", "Степан"])
    for turn in itertools.islice(queue, 7):
        print(turn)

    print("\n--- Завдання 5 ---")
    journal = [
        "Михайлик отримав доручення",
        "Михайлик передав Василькові",
        "Василько загрався",
        "Василько передав Оленці",
        "Оленка прив'язала теля біля хліва",
        "Оленка пішла додому",
        "Дід заспокоївся",
    ]
    result = next(find_calf(journal))
    print(result)