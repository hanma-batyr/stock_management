class BudgetTracker:
    def __init__(self):
        # Инициализация бюджетного трекера с нулевым бюджетом и пустыми доходами и расходами
        self.budget = 0
        self.incomes = {}
        self.expenses = {}
        self.translation = {}

    def display_budget(self):
        # Вывод общего бюджета
        print(f"Общий бюджет: {self.budget}")

    def add_income(self, category, amount):
        # Добавление дохода и обновление бюджета
        if category in self.incomes:
            self.incomes[category] += amount
        else:
            self.incomes[category] = amount
        self.budget += amount

    def add_expense(self, category, amount):
        # Добавление расхода и обновление бюджета
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.budget -= amount

    def display_statistics(self):
        # Вывод статистики доходов и расходов
        print("\nСтатистика доходов:")
        for category, amount in self.incomes.items():
            print(f"{category}: {amount}")

        print("\nСтатистика расходов:")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount}")

    def add_translation(self, category, amount):
        # Добавление транзакции и обновление бюджета
        if category in self.translation:
            self.translation[category] -= amount
        else:
            self.translation[category] = amount
        self.budget -= amount

    def display_translation(self):
        # Вывод истории транзакций
        print("\nИстория транзакций:")
        for category, amount in self.translation.items():
            print(f"{category}: {amount}")


def main():
    # Создание объекта бюджетного трекера
    budget_tracker = BudgetTracker()

    while True:
        # Вывод меню пользователю
        print("\n1. Вывести общий бюджет")
        print("2. Добавить доход")
        print("3. Добавить расход")
        print("4. Вывести статистику")
        print("5. Перевод")
        print("6. Показать историю транзакций")
        print("0. Выход")

        # Получение выбора пользователя
        choice = input("Выберите действие: ")

        if choice == "1":
            budget_tracker.display_budget()
        elif choice == "2":
            # Получение информации о доходе от пользователя и добавление его в бюджет
            category = input("Введите категорию дохода: ")
            amount = float(input("Введите сумму дохода: "))
            budget_tracker.add_income(category, amount)
        elif choice == "3":
            # Получение информации о расходе от пользователя и добавление его в бюджет
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            budget_tracker.add_expense(category, amount)
        elif choice == "4":
            # Вывод статистики
            budget_tracker.display_statistics()
        elif choice == "5":
            # Получение информации о транзакции от пользователя и добавление ее в бюджет
            category = input("Введите данные транзакции: ")
            amount = float(input("Введите сумму транзакции: "))
            budget_tracker.add_translation(category, amount)
        elif choice == "6":
            budget_tracker.display_translation()
        elif choice == "0":
            # Выход из программы
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
