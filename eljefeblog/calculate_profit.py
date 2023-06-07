def calculate_profit(info):
    return round(info['sell_price']*info['sold_number'] - info['cost_price']*info['stock_number'])

calculate_profit({'cost_price': 12.33, 'sell_price': 89.03, 'stock_number': 1433, 'sold_number': 1200})    
