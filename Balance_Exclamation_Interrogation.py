# Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

# If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

# Examples
# "!!", "??"     -->  "Right"
# "!??", "?!!"   -->  "Left"
# "!?!!", "?!?"  -->  "Left"
# "!!???!????", "??!!?!!!!!!!"  -->  "Balance"

def balance(left, right):
    dict = {"!":2, "?":3}  # dict que vai guardar os valores de ! e ? como indices
    somaleft = 0  # variavel auxiliar que vai guardar a soma da incidencia de left
    somaright = 0 # variavel auxiliar que vai guardar a soma da incidencia de right
    
    for each in left:
        somaleft += dict[each] # para cada valor em left ele vai verificar o seu valor no dict
                               # e guardar na var auxiliar
    for each in right:          
        somaright += dict[each] # mesma coisa para right
        
    if somaleft > somaright:
        return "Left"
    elif somaright > somaleft:  # comparando a soma para ver qual lado é mais pesado    
        return "Right"
    else:
        return "Balance"