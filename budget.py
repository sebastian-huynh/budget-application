def create_spend_chart(categories):
  num_of_categories = int()
  category_name = str()
  category_name_list = list()
  category_spent = float()
  category_spent_list = list()
  category_0s = int()
  category_0s_list = list()
  bar_graph = str()
  total_spent = float()
  
  for category in categories:
    num_of_categories += 1
    category_name = category.name
    category_name_list.append(category_name)
  
    for i in category.ledger:
      if i.get("amount") < 0:
        category_spent += i.get("amount")
        total_spent += i.get("amount")
    category_spent_list.append(round(category_spent, 2))
    category_spent = 0
    
  total_spent = round(total_spent, 2)

  for i in category_spent_list:
    category_0s = int((i/total_spent)*10)
    category_0s_list.append(category_0s)
  
  bar_graph += "Percentage spent by category" + "\n"
  
  bar_graph += "100| "  
  for index, i in enumerate(category_0s_list):
    if i == 10:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 90| "  
  for index, i in enumerate(category_0s_list):
    if i == 9:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 80| "  
  for index, i in enumerate(category_0s_list):
    if i == 8:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 70| "  
  for index, i in enumerate(category_0s_list):
    if i == 7:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 60| "  
  for index, i in enumerate(category_0s_list):
    if i == 6:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 50| "  
  for index, i in enumerate(category_0s_list):
    if i == 5:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 40| "  
  for index, i in enumerate(category_0s_list):
    if i == 4:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 30| "  
  for index, i in enumerate(category_0s_list):
    if i == 3:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 20| "  
  for index, i in enumerate(category_0s_list):
    if i == 2:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += " 10| "  
  for index, i in enumerate(category_0s_list):
    if i == 1:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += "  0| "  
  for index, i in enumerate(category_0s_list):
    if i == 0:
      bar_graph += "o  "
      category_0s_list[index] -= 1
    else:
      bar_graph += "   "
  bar_graph += "\n"

  bar_graph += "    -"
  dashes = "---"*(num_of_categories)
  bar_graph += dashes + "\n"

  longest_name = len(max(category_name_list, key=len))
  for index, name in enumerate(category_name_list):
    while len(name) < longest_name:
      name += " "
    category_name_list[index] = name

  x = longest_name
  y = 0
  while x > 0:
    bar_graph += "     "
    for i in category_name_list:
      bar_graph += i[y] + "  "
    bar_graph += "\n"
    y += 1
    x -= 1

  bar_graph = bar_graph.rstrip()
  bar_graph += "  "
  
  return bar_graph

class Category:

  def __init__(self, name):
    self.ledger = []
    self.name = name

  def get_balance(self):
    self.balance = 0
    for i in self.ledger:
      self.balance += i.get("amount")
    return self.balance

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def deposit(self, amount, *args):
    description = str()
    arg = ()
    if len(args) != 0:
      for i in args:
        arg = args
        description = arg[0]
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, *args):
    if (self.check_funds(amount)) is False:
      return False
    else:
      description = str()
      arg = ()
      if len(args) != 0:
        for i in args:
          arg = args
          description = arg[0]

      amount_negative = -amount

      self.ledger.append({
        "amount": amount_negative,
        "description": description
      })
      return True

  def transfer(self, amount, category):
    first_category = self.name
    second_category = category.name
    if (self.check_funds(amount)) is False:
      return False
    else:
      self.withdraw(amount, "Transfer to " + str(second_category))
      category.deposit(amount, "Transfer from " + str(first_category))
      return True
      
  def __str__(self):
    final_string = str()
    final_string += self.name.center(30, "*") + "\n" 
    for i in self.ledger:
      final_string += str(i.get('description'))[:23].ljust(23, ' ')
      final_string += ("%.2f" % i.get('amount')).rjust(7, ' ')
      final_string += "\n"
    final_string += "Total: " + ("%.2f" % self.get_balance())
    return final_string