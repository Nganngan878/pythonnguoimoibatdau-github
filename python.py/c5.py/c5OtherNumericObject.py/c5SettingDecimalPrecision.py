import decimal
decimal.Decimal(1)/ decimal.Decimal(7)
decimal.getcontext().prec=4
decimal.Decimal(1)/decimal.Decimal(7)
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))
