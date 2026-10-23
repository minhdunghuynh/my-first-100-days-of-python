#FUNCTIONS:------------------------------------------------------------------------
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

#M-FUNCTIONS ------------------------------------------------------------------------
def m_plus():
    return ram_cal + result

def m_minus():
    return ram_cal - result

def m_r():
    print(ram_cal)

def m_c():
    return ram_cal - ram_cal

#PROGRAM------------------------------------------------------------------------
# VARIABLES
print("Calculator ver 1.0.1")

ram_cal = 0
while True:
    n1 = float(input("Type in the first number\n"))
    method_calculation = input('Type in "+", "-", "*", or "/" for your chosen method\n')
    n2 = float(input('Type in the second number\n'))
    # CONDITIONS:------------------------------------------------------------------------
    if method_calculation == "+":
        result = add(n1, n2)
        print(result)
    elif method_calculation == "/" and n2 == 0:
        print("ERROR")
        continue
    elif method_calculation == "-":
        result = sub(n1, n2)
        print(result)
    elif method_calculation == "*":
        result = mul(n1, n2)
        print(result)
    elif method_calculation == "/":
        result = div(n1, n2)
        print(result)
    else:
        print("ERROR")
        continue
    # M FUNC CONDITIONS:------------------------------------------------------------------------
    memory_func = input('Choose function:\n M+\n M-\n MR\n or MC\n')
    memory_func = memory_func.lower()
    if memory_func == "m+":
        ram_cal = m_plus()
    elif memory_func == "m-":
        ram_cal = m_minus()
    elif memory_func == "mr":
        m_r()
    elif memory_func == "mc":
        ram_cal = m_c()
    else:
        print("ERROR")
        continue






