class BudgetTracker:
    def __init__(self):
        self.budget = 0
        self.incomes = {}
        self.expenses = {}
        self.translation = {}

    def display_budget(self):
        print(f"Общий бюджет: {self.budget}")

    def add_income(self, category, money):
        if category in self.incomes:
            self.incomes[category] += money
        else:
            self.incomes[category] = money
        self.budget += money

    def add_expense(self, category, money):
        if category in self.expenses:
            self.expenses[category] += money
        else:
            self.expenses[category] = money
        self.budget -= money

    def display_statistics(self):
        print("\nСтатистика доходов:")
        for category, money in self.incomes.items():
            print(f"{category}: {money}")

        print("\nСтатистика расходов:")
        for category, money in self.expenses.items():
            print(f"{category}: {money}")

    def add_translation(self, category, money):
        if category in self.translation:
            self.translation[category] -= money
        else:
            self.translation[category] = money
        self.budget -= money

    def display_translation(self):
        print("\nИстория транзакцией:")
        for category, money in self.translation.items():
            print(f"{category}: {money}")


def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n1. Вывести общий бюджет")
        print("2. Добавить доход")
        print("3. Добавить расход")
        print("4. Вывести статистику")
        print("5. Перевод")
        print("6. Показать историю транзакций")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            budget_tracker.display_budget()
        elif choice == "2":
            category = input("Введите категорию дохода: ")
            money = float(input("Введите сумму дохода: "))
            budget_tracker.add_income(category, money)
        elif choice == "3":
            category = input("Введите категорию расхода: ")
            money = float(input("Введите сумму расхода: "))
            budget_tracker.add_expense(category, money)
        elif choice == "4":
            budget_tracker.display_statistics()
        elif choice == "5":
            category = input("Введите данные пользователя: ")
            money = float(input("Введите сумму: "))
            budget_tracker.add_translation(category, money)

        elif choice == "6":
            budget_tracker.display_translation()

        elif choice == "0":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
