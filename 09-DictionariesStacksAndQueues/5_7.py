def hotel_list(hotels):
    list = ""
    i = 0
    for dict in hotels:
        if i == len(hotels)-1:
            list += dict['name']
        else:
            list += f"{dict['name']}, "
        i += 1
    return list
    
def avg_price(hotels):
    total_value = 0
    i = 0
    for dict in hotels:
        total_value += dict['price']
        i += 1
    avg = total_value / i
    
    return avg
    
hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

cheaper = ""
if avg_price(hotels_in_Krakow) > avg_price(hotels_in_Sopot):
    cheaper = "Sopot"
else:
    cheaper = "Krakow"

msg = f"""
Hotels in Krakow: {hotel_list(hotels_in_Krakow)}
Average hotel price in Krakow: {avg_price(hotels_in_Krakow)}
Hotels in Sopot: {hotel_list(hotels_in_Sopot)}
Average hotel price in Sopot: {avg_price(hotels_in_Sopot)}
Cheaper hotels in: {cheaper}
"""

print(msg)


