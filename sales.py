def sales_tax(total):
    my_sales = total * (.06)
    return round(my_sales,2)

def total_after(my_sales, total):
    return(round(my_sales + total,2))
    