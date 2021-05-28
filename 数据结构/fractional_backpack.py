"""背包问题"""

# 商品价格，重量
goods = [(60, 10), (120, 30), (100, 20)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]
    total_v = 0
    for i, (price, weight) in enumerate(goods):
        if w >= weight: 
            m[i] = 1
            total_v += price
            w -= weight
        else:
            m[i] = w / weight
            total_v += m[i] * price
            break
    return m, total_v


print(fractional_backpack(goods, 50))
