# Solution to "Build A Budget App Project", 08/05/2025

# INSTRUCTIONS: Complete the Category class. It should be able to instantiate objects
# based on different budget categories like food, clothing, and entertainment. When
# objects are created, they are passed in the name of the category. The class should
# have an instance variable called ledger that is a list. The class should also contain
# the following methods: deposit, withdraw, get_balance, transfer, check_funds.
# Besides the Category class, create a function (outside of the class) called create_spend_chart
# that takes a list of categories as an argument. It should return a string that is a bar chart.

# MORE INFO: https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-budget-app-project/build-a-budget-app-project




class Category:
    def __init__(self, type):
        # basic category info
        self.balance = 0
        self.spent = 0
        self.type = type
        self.ledger = []

    def __str__(self):
        # out collects lines for budget output
        out = []

        # formatting title line
        x = (30 - len(self.type)) / 2
        if x%1 == 0:
            a = b = int(x)
        elif x%1 != 0:
            a = int(x + 0.5)
            b = int(x - 0.5)
        out.append('*'*a + self.type + '*'*b)

        # formatting description and amount for each transaction
        for i in self.ledger:
            desc = ''
            amt = str(f"{i['amount']:.2f}")
            y = 0
            z = 7 - len(amt)
            if len(i['description']) < 23:
                desc = i['description']
                y = 23 - len(i['description'])
            else:
                desc = i['description'][:23]
            out.append(desc + ' '*(y+z) + amt)
        out.append('Total: ' + str(self.balance))
        return '\n'.join(out)

    def deposit(self, amount, description=''):
        # add deposit to balance and append ledger
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description=''):
        # check for sufficient funds
        if not self.check_funds(amount):
            return False
        # subtract withdrawal from balance and append to ledger
        self.balance -= amount
        self.spent = amount
        self.ledger.append({'amount': -1 * amount, 'description': description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target):
        # check for sufficient funds
        if not self.check_funds(amount):
            return False
        # subtract transfer from source category's balance and append to ledger
        self.balance -= amount
        self.ledger.append({'amount': -1*amount, 'description': f'Transfer to {target.type}'})
        # add transfer to target category's balance and append to ledger
        target.balance += amount
        target.ledger.append({'amount': amount, 'description': f'Transfer from {self.type}'})
        return True

    def check_funds(self, amount):
        return amount <= self.balance

def create_spend_chart(categories):
    # graph collects lines for bar graph output
    graph = []

    # format expense and category data
    expenses = [cat.spent for cat in categories]
    total = sum(expenses)
    percent = [int(100*i/total)//10*10 for i in expenses]
    upto = max([len(cat.type) for cat in categories])
    cats = [categories[i].type+' '*(upto-len(categories[i].type)) for i in range(len(categories))]

    # title
    graph.append('Percentage spent by category')

    # construct each line with percent, y-axis, and appropriate dots
    for i in range(100, -1, -10):
        line = f"{str(i).rjust(3)}|"
        for p in percent:
            line += " o " if p >= i else "   "
        line += " "
        graph.append(line)

    # x-axis
    graph.append('    -' + '---'*len(expenses))

    # construct each line with appropriate letters for writing categories vertically
    for i in range(upto):
        line = '     '
        for x in range(len(categories)):
            line += f'{cats[x][i]}  '
        graph.append(line)

    return '\n'.join(graph)

** end of main.py **

