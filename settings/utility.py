import re


def _convert(list_convert):
    return [itm[0] for itm in list_convert]


def total_coast(list_quantity, list_price):
    order_total_cost = 0

    for ind, itm in enumerate(list_price):
        str_price = re.findall('[0-9]+', list_price[ind])
        real_price = int(''.join(str_price))
        order_total_cost += list_quantity[ind] * real_price
        # print(order_total_cost)
        # order_total_cost = str(order_total_cost)
        # print(len(order_total_cost))
        # if len(order_total_cost) == 4:
        #     return f'{order_total_cost[:1]} {order_total_cost[-3:]}'
        # else:
        #     return f'{order_total_cost[:2]} {order_total_cost[-3:]}'
        # print(f'{order_total_cost[:1]} {order_total_cost[-3:]}')
        # return f'{order_total_cost[:2]} {order_total_cost[-3:]}'

        return order_total_cost


def total_quantity(list_quantity):
    order_total_quantity = 0

    for itm in list_quantity:
        order_total_quantity += itm

        return order_total_quantity


def get_total_cost(DB):
    all_product_id = DB.select_all_product_id()
    all_price = [DB.select_single_product_price(itm) for itm in all_product_id]
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]

    return total_coast(all_quantity, all_price)


def get_total_quantity(DB):
    all_product_id = DB.select_all_product_id()
    all_quantity = [DB.select_order_quantity(itm) for itm in all_product_id]

    return total_quantity(all_quantity)
