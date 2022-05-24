DEPOSIT = 1
WITHDRAWAL = 2
TRANSFER = 3
HOLD = 4

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Пополнение'),
    (WITHDRAWAL, 'Вывод'),
    (TRANSFER, 'Зачисление на баланс'),
    (HOLD, 'На удержании'),
)
