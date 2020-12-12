def main_function():
    variables = []
    strings = open("test.txt", "r")
    buffered_reader = strings.read()
    chars = buffered_reader.splitlines()
    for i in chars:
        check_type(i, variables)

def check_type(statement, vars):
    integer = 'int'    
    if integer in statement:     
        integer_type(statement, vars)
    
def integer_type(statement, vars):
    is_int = any(map(str.isdigit, statement))
    if isinstance(is_int, float):
        print ('Invalid Type: Float')
    else:
        print("\n", statement,  " Integer Type: ",  is_int)
        vars.append((statement.split()[1])) 
        res = any(ele in statement for ele in vars) 
        print("\nTracked variables: ", vars)

main_function()