import art

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide 
}

def calculator():
  print(art.logo)
  
  num1 = float(input("What's the first number?: "))
  
  continues = True
  
  while continues:
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    
    num2 = float(input("What's the next number?: "))
    
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    want_to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ")
  
    if want_to_continue == 'n':
      continues = False
      calculator() 
    else:
      num1 = answer 

calculator() 