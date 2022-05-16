discount = 0.6
costs = [99,199,299,399,499]
print("Без скидки | Сумма скидки | Новая цена")
for i in range(5):
    print(costs[i], "|", round(costs[i] * discount,2), "|", round(costs[i] * (1-discount),2))