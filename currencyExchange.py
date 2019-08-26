print('purchase - p\nsale - s')
currencies = {'EUR', 'USD', 'CHF'}

while True:
    purchaseOrSale = input('If you want to buy the currency input "p"\nIf you want to sale the currency input "s" ')
    print('Availible cuurency:\nEUR/USD/CHF')
    if purchaseOrSale == 'p':
        currency = None
        while currency is None:
            userCurrency = input('What currency do you want to buy? ')
            if userCurrency not in currencies:

                print('The currency is not available in this counting room')
            else:
                currency = userCurrency
        amount = float(input('How much money do you want to change? '))
        if currency == 'EUR':
            print(f'You can buy {(amount / 4.29): .2f} Euros')
        elif currency == 'USD':
            print(f'You can buy {(amount / 3.79): .2f} American Dolars')
        elif currency == 'CHF':
            print(f'You can buy {(amount / 3.82): .2f} Swiss Franks')

    elif purchaseOrSale == 's':
        currency = input('Jaką walutę chcesz sprzedać? ')
        amount = float(input('W jakiej ilości chcesz wymienić wybraną walutę? '))
        if currency == 'EUR':
            print(f'You can sell {amount} EURO for {(amount * 4.29): .2f} zł.')
        elif currency == 'USD':
            print(f'You can sell {amount} American Dollars for {(amount * 3.79): .2f} zł.')
        elif currency == 'CHF':
            print(f'You can sell {amount} Swiss Franks for {(amount * 3.82): .2f} zł.')
        else:
            print('The currency is not available in this counting room')
    else:
        print('Unsupported command')
