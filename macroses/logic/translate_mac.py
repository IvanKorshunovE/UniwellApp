import re

a = 'MM INTR month 15.19 - month 30.99 with timer'
b = 'MM INTR 3 months 14.97 - 3 months 68.16 with timer with upsell (EUR)'
#
# regex = r"\d+\.\d+"
# result_a = list(map(float, re.findall(regex, a)))
# result_b = list(map(float, re.findall(regex, b)))
#
# print(result_a)  # Output: [15.19, 30.99]
# print(result_b)  # Output: [14.97, 68.16]



def find_float(id_product):
    regex = r"\d+\.\d+"
    return list(map(float, re.findall(regex, id_product)))[1]


id_refund_amount = find_float(id_product)