def stock_availability(boxes, command, *args):
    if command == "delivery":
        return boxes + list(args)

    if not args:
        return boxes[1:]

    if str(args[0]).isnumeric():
        sold = int(args[0])
        return boxes[sold:]

    return [el for el in boxes if el not in args]


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
