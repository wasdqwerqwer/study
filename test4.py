import csv

import matplotlib.pyplot as plt

sale_data = []
optimal_weight = 0
min_difference = -1


with open("sample_data.csv", encoding = 'utf-8-sig') as data:
    reader = csv.DictReader(data)
    for row in reader:
        price = int(row['price'])
        sale_qty = int(row['sale_qty'])
        sale_data.append({
            'price': price,
            'qty': sale_qty
        })
        plt.scatter(price, sale_qty)

    for n in range(-100,101):
        if n == 0:
            continue
        for mn in range(1,101):
            weight = mn / (n * 1000)

            sum_difference = 0

            for data in sale_data:
                estimate_qty = abs(weight * sale.get('price'))
                difference = abc(estimate_qty - sale.get('qty'))
                sum_difference += difference

            if min_difference < 0 or min_difference > sum_difference:
                min_difference = sum_difference
                optimal_weight = weight

    optimal_xaxis = []
    optimal_yaxis = []
    for price in range(10000, 100000, 1000):
        optimal_xaxis.append(price)
        optimal_yaxis.append(optimal_weight * price)
    print(optimal_xaxis, optimal_yaxis)
    plt.show()

