class Category:
    funds = 0
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        dict = {"amount": amount, "description": description}
        self.funds += amount
        self.ledger.append(dict)

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) is True:
            dict = {"amount": -(amount), "description": description}
            self.funds -= amount
            self.ledger.append(dict)
            return True
        else:
            return False

    def transfer(self, amount, budget):
        withdrow_desc = "Transfer to " + str(budget.name)
        deposit_desc = "Transfer from " + str(self.name)
        if self.check_funds(amount) is True:
            self.withdraw(amount=amount, description=withdrow_desc)
            budget.deposit(amount=amount, description=deposit_desc)
            return True
        return False

    def get_balance(self):
        return self.funds

    def __str__(self):
        title_length = len(self.name)
        left = (30 - title_length) // 2
        right = 30 - title_length - left
        title_line = '*' * left + self.name + '*' * right
        str_var = ""
        for i in self.ledger:
            # amount = str(i["amount"])
            amount = "{:.2f}".format(i["amount"])[:7]
            description = str(i["description"])[:23]
            value =  description + amount.rjust(30 - (len(description))) + "\n"
            str_var += value
        total = "Total: " + "{:.2f}".format(self.funds)
        final_print = title_line + "\n" + str_var + total

        return final_print

def create_spend_chart(categories):
    tittle = "Percentage spent by category\n"
    spend = {}
    if len(categories) <= 4:
        sum_list = []
        for budget in categories:
            for i in budget.ledger:
                value = i["amount"]
                name_ = budget.name
                if value < 0:
                    if name_ not in spend:
                        spend[name_] = value
                    else:
                        spend[name_] += value
                    # spend["Catagory"] = name_
                    # spend["spent"] = value
                    print(name_)
                    print(value)
            sum_list.append(budget.get_balance())
        print(sum_list)
        print(spend)
        sum = 0
        values = []
        items = []
        for item in spend:
            sum += spend[item]
        for item in spend:
            spend[item] = int(round(((spend[item]) / sum) * 100, 1))
            values.append(spend[item])
            items.append(item)
        print(spend)
        print(values)
        print(items)

        # percentage = []
        # for i, j in zip(sum_list, values):
        #     cal = int(round((j/(j-i)) * 100, -1))
        #     percentage.append(cal)
        # print(percentage)

        i = 100
        while i >= 0:
            cat_spaces = " "
            for total in values:
                if total >= i:
                    cat_spaces += "o  "
                else:
                    cat_spaces += "   "
            tittle += str(i).rjust(3) + "|" + cat_spaces + "\n"
            i -= 10

        dashes = "-" + "---"* (len(items))
        maxi = max(items, key=len)
        print(maxi)
        x_axis =""
        for x in range(len(maxi)):
            nameStr = '     '
            for name in items:
                if x >= len(name):
                    nameStr += "   "
                else:
                    nameStr += name[x] + "  "

            if (x != len(maxi) -1 ):
                nameStr += "\n"

            x_axis += nameStr

        tittle += dashes.rjust((len(dashes))+4) + "\n" + x_axis
        return tittle
    else:
        return False




# clothes = Category("cloth")
food = Category("food")
# # fuck = Category("fuck")
# # fuck.deposit(500, "massage")
# # fuck.transfer(80, food)
# # food.deposit(5, "hi")
# # # food.deposit(100)
# # food.withdraw(5, "fuck")
# # food.deposit(82, "fuulkjfflkas jsfjskladfj kafsjf j;a sfl h;jkh; c")
# # food.transfer(20, clothes)
# # clothes.withdraw(20)
# # print(food.get_balance())
# # print(food)
# # print(clothes)
# # print(create_spend_chart([clothes, food, fuck]))

entertainment = Category("entertainment")

business = Category("business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))

v = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(v)
