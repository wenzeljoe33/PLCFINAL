def expr():
    first()
    var()
    while(next_token is PLUS_PLUS_SIGN or next_token is MINUS_MINUS_SIGN):
        lex()
        first()

def first():
    second()
    while(next_token is PLUS_PLUS_SIGN or next_token is MINUS_MINUS_SIGN):
        lex()
        variables()
        second()
        
def second():
    third()
    while(next_token is TIMES or next_token is GREATER_THAN_EQUAL_TO or next_token is SINGLE_AMPERSAND):
        lex()
        third()

def third():
    fourth()
    while(next_token is PLUS or next_token is MINUS or next_token is LESS_THAN_EQUAL_TO):
        lex()
        fourth()

def fourth():
    fifth()
    if(next_token is MINUS):
        lex()
        variables()
    elif(next_token is PLUS):
        lex()
        variables()
    else:
        lex()
        variables()
        fifth()

def fifth():
    sixth()
    while(next_token is GREATER_THAN or next_token is LESS_THAN ):
        lex()
        sixth()

def sixth():
    seventh()
    while(next_token is DOUBLE_AMPERSAND or next_token is DIVIDE or next_token is SINGE_BAR):
        lex()
        seventh()

def seventh():
    eighth()
    while(next_token is DOUBLE_BAR or next_token is SQUIGLY_BAR):
        lex()
        eighth()

def eighth():
    ninth()
    while(next_token is EQUAL or next_token is SLASH_EQUAL):
        lex()
        ninth()

def variables():
    if(next_token is ZERO_THROUGH_NINE or next_token is A_THROUGH_Z):
       lex()
       while(next_token is LEFT_PAREN):
           lex()
           expr()
           while(next_token is RIGHT_PAREN):
               lex()

    else:
        error()