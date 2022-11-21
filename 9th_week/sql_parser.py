def sql_parse(sql):

    wordlist = sql.split()
    idx = 0
    for word in wordlist:
        select_items = []
        from_items = []
        where_items = []
        order_items = []
        limit_items = []

        wordlist[idx] = word.strip(",")

        if word.upper() == "SELECT":
            wordlist[idx] = word.upper()
        if word.upper() == "FROM":
            wordlist[idx] = word.upper()
        if word.upper() == "WHERE":
            wordlist[idx] = word.upper()
        if word.upper() == "AND":
            wordlist[idx] = word.upper()
        if word.upper() == "OR":
            wordlist[idx] = word.upper()
        if word.upper() == "ORDER":
            wordlist[idx] = word.upper()
        if word.upper() == "BY":
            wordlist[idx] = word.upper()
        if word.upper() == "ASC":
            wordlist[idx] = word.upper()
        if word.upper() == "DESC":
            wordlist[idx] = word.upper()
        if word.upper() == "LIMIT":
            wordlist[idx] = word.upper()
        idx += 1

    if "DESC" in wordlist:
        order = "DESC"
    else:
        order = "ASC"

    sel_index = wordlist.index("SELECT")
    from_index = wordlist.index("FROM")
    if "WHERE" in wordlist:
        where_index = wordlist.index("WHERE")
    else:
        where_index = None
    if "ORDER" in wordlist:
        order_index = wordlist.index("ORDER")
    else:
        order_index = None
    if "LIMIT" in wordlist:
        limit_index = wordlist.index("LIMIT")
    else:
        limit_index = None

    select_items = list(wordlist[sel_index + 1 : from_index])
    from_items = list(wordlist[from_index + 1 : where_index])
    if "WHERE" in wordlist:
        where_items = list(wordlist[where_index + 1 : order_index])
    if "ORDER" in wordlist:
        order_items = list(wordlist[order_index + 2 : limit_index])
    if "LIMIT" in wordlist:
        limit_items = list(wordlist[limit_index + 1])
    print(select_items)
    print(from_items)
    print(where_items)
    print(order_items)
    print(limit_items)
    print(order)

    sql_dict = {"fields": select_items, "table": from_items[0], "where": where_items}

    print(sql_dict)

    idx = 0

    for item in where_items:
        print(item)
        if "=" in item:
            new_str = ""
            i = 0
            while i < len(item):
                new_str += item[i]
                if i < (len(item) - 1):
                    if item[i + 1] == "=":
                        new_str += " "
                        new_str += "="
                        new_str += " "
                        i += 1
                i += 1
            where_items[idx] = new_str
        idx += 1
    print(where_items)
    temp_where = []
    for item in where_items:
        if "=" in item:
            if item == "=":
                pass
            temp_where = item.split()
            intermediate_where = []
            # for item in where_items:
            #     print(temp_where)
    return sql_dict


sql = "select fname, lname, address, price from table where price=24.4 and fname = 'Keith' order by price desc limit 1"
query1 = "SELECT first_name, last_name, email FROM Cohorts WHERE first_name='John'"
query2 = "SELECT city, state from Customers where state='UT' ORDER BY city ASC"
query3 = "SELECT * FROM Courses ORDER BY name ASC LIMIT 20"
query = 'SELECT name, make, model, price FROM Products  WHERE price = 49.99 ORDER BY price DESC LIMIT 5'


my_dict = sql_parse(query)

print(my_dict)