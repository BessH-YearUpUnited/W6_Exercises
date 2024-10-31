class Tea:
    '''varieties of tea for my tea shop'''
    def __init__(self, name, allergen='none'):
        self.name = name
        self.allergen = allergen
    def brew(self):
        print(f'How about a nice cup of {self.name}?')
        print(f'Please collect your tea from the counter')    
    def restock(self):
        print(f'Tea emergency! We are out of {self.name}, which is a {self.type} variety')
        print("Sorry, we only have teabags")

class BlackTea(Tea):
    '''varieties of black tea'''
    def __init__(self, name, allergen, strength, caffeinated='y'):
        super().__init__(name, allergen)
        self.strength = strength
        self.caffeinated = caffeinated

bl_asm = BlackTea('Assam', 'none', 'full-bodied')

print(f'''
Name: {bl_asm.name}
Known allergens?: {bl_asm.allergen}
Strength: {bl_asm.strength}
Caffeinated: {bl_asm.caffeinated}
      ''')





# gr_jas = Tea('jasmine green tea', 'green')
# oo_peo = Tea('white peony oolong', 'oolong')
# bl_alm = Tea('almond darjeeling', 'black', 'tree nut')

# gr_jas.restock()

# print(gr_jas.name, gr_jas.looseleaf)
# print(oo_peo.name, oo_peo.looseleaf)
# print(bl_alm.name, bl_alm.looseleaf)





# print(f'Can I have a cup of {gr_jas.name}?')
# oo_peo.brew()

# gr_jas.restock()

# print(f'''
# Inventory:''')
# print(gr_jas.name, '- allergen:', gr_jas.allergen, '- in stock? :', gr_jas.instock)
# print(oo_peo.name, '- allergen:', oo_peo.allergen, '- in stock? :', oo_peo.instock)
# print(bl_alm.name, '- allergen:', bl_alm.allergen, '- in stock? :', bl_alm.instock, '\n')
