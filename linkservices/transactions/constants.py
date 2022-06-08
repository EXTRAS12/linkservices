DEPOSIT = 1
WITHDRAWAL = 2
TRANSFER = 3
PURCHASE = 4
EXTENSION = 5

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Пополнение'),
    (WITHDRAWAL, 'Вывод'),
    (TRANSFER, 'Зачисление на баланс'),
    (PURCHASE, 'Покупка'),
    (EXTENSION, 'Продление'),
)
