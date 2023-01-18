import datetime as dt


class Record:
    # Везде отсутствуют докстринги, стоит их добавить.
    # Попробуй добавить тайпинг.
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        # Размести выражение в две строки,
        # поместив в одну строку всё до else включительно,
        # это сделает код более читаемым
        self.date = (
            # Текущую дату можно получить используя dt.date.today()
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        # В данном случе Record это переменная, измени имя согласно pep8
        for Record in self.records:
            # Текущую дату можно получить используя dt.date.today()
            if Record.date == dt.datetime.now().date():
                # Все круто, но попробуй переписать этот момент с
                # использованием функции sum и генератора
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # Что если расчет разницы дней вынести в отдельную переменную
            # за пределы if
            #
            # Попробуй избавиться от and
            #
            # Когда используешь многострочную конструкцию в тернарном операторе,
            # то лучше закрывающую скобку оставить в конце выражения.
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                # Тут тоже можно использовать sum + генератор. Попробуешь?
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # Оформи комментарий в соответствии с Docstring Conventions
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # Переменным лучше давать понятные имена, исправь это.
        x = self.limit - self.get_today_stats()
        if x > 0:
            # Перепеши эту строку без использования бэкслеша.
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # https://refactoring.guru/ru/replace-nested-conditional-with-guard-clauses
        else:
            # Скобки тут не нужны,
            # а так же нужно добавить пробел перед возвращаемым значением
            return('Хватит есть!')


class CashCalculator(Calculator):
    # Если коммент не привносит ничего нового в контекст, то он точно не нужен
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # В этом присваивании нет смысла, исправь
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        # Если валюта не известна то этот блок не выполнится.
        #
        # Попробуешь сделать валидацию с использованием словаря !
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # Нули после точки не имеют эффекта
            cash_remained == 1.00
            currency_type = 'руб'
        # Лучше разбить блоки схожие по задачам, так их будет легче читать.
        # (например расчет, валидация и возврат результата)
        if cash_remained > 0:
            # В Я.Практикуме есть требование - не выполнять
            # никаких операций внутри f-string.
            # Вынеси, пожалуйста, операцию round за пределы строки.
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # Эту проверку можно убрать заменив elif на else
        elif cash_remained < 0:
            # Тут нарушена консистентность форматирования строк и
            # требование переноса строк.
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)

    # Ты переопределил метод родительского класса Calculator,
    # теперь он возвращает None, его нужно убрать отсюда.
    def get_week_stats(self):
        super().get_week_stats()
