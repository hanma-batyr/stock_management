class Budget:
    def __init__(self):
        self.budget = 0

    def display_budget(self):
        print(f"Общий бюджет: {self.budget}")


class IncomeManager:
    def __init__(self):
        self.incomes = {}

    def add_income(self, category, money):
        self.float_int_money(money)
        if category in self.incomes:
            self.incomes[category] += money
        else:
            self.incomes[category] = money

    @staticmethod
    def float_int_money(money):
        if not isinstance(money, (int, float)):
            raise ValueError("Введите правильное значение!")


class ExpenseManager:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, money):
        self.float_int_money(money)
        if category in self.expenses:
            self.expenses[category] += money
        else:
            self.expenses[category] = money

    @staticmethod
    def float_int_money(money):
        if not isinstance(money, (int, float)):
            raise ValueError("Введите правильное значение!")


class TransactionHistory:
    def __init__(self):
        self.translation = {}

    def add_translation(self, category, money):
        self.float_int_money(money)
        if category in self.translation:
            self.translation[category] -= money
        else:
            self.translation[category] = money

    @staticmethod
    def float_int_money(money):
        if not isinstance(money, (int, float)):
            raise ValueError("Введите правильное значение!")

    def display_translation(self):
        print("\nИстория транзакций:")
        for category, money in self.translation.items():
            print(f"{category}: {money}")


budget = Budget()
income_manager = IncomeManager()
expense_manager = ExpenseManager()
transaction_history = TransactionHistory()

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
        budget.display_budget()
    elif choice == "2":
        category = input("Введите категорию дохода: ")
        money = float(input("Введите сумму дохода: "))
        income_manager.add_income(category, money)
        budget.budget += money
    elif choice == "3":
        category = input("Введите категорию расхода: ")
        money = float(input("Введите сумму расхода: "))
        expense_manager.add_expense(category, money)
        budget.budget -= money
    elif choice == "4":
        print("\nСтатистика доходов:")
        for category, money in income_manager.incomes.items():
            print(f"{category}: {money}")

        print("\nСтатистика расходов:")
        for category, money in expense_manager.expenses.items():
            print(f"{category}: {money}")
    elif choice == "5":
        category = input("Введите данные пользователя: ")
        money = float(input("Введите сумму: "))
        transaction_history.add_translation(category, money)
        budget.budget -= money
    elif choice == "6":
        transaction_history.display_translation()
    elif choice == "0":
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
