# children instead of pets and parents instead of owners
child_0 = {
    'name': 'arsha', 
    'parent': 'samaneh',
    }
child_1 = {
    'name': 'samyar', 
    'parent': 'meysam',
    }
child_2 = {
    'name': 'koroosh', 
    'parent': 'hamed',
    }
child_3 = {
    'name': 'amir hosein', 
    'parent': 'hojat',
    }
child_4 = {
    'name': 'mahdi', 
    'parent': 'rohallah',
    }
child_5 = {
    'name': 'arash', 
    'parent': 'tahereh',
    }

children = [child_0, child_1, child_2, child_3, 
            child_4, child_5]
for child in children :
    cil_mes = f"His name is : {child['name'].title()}"
    par_mes = f"His parent is : {child['parent'].title()}\n"
    print(cil_mes)
    print(par_mes)