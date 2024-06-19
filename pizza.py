# Atividade Bimestral - Padrão de Projeto
# Alunos: Victor Hugo M Z Zuleta e Zander do Vale Bernardino
# Seguindo todas as especificações do PDF, vamos determinar as classes.

class Pizza: #Componente do lanche
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost
    
class Plate(Pizza): #Componente Concreto
    cost = 0.0

class Decorator(Pizza): #Decorator
    def __init__(self, pizza):
        self.additional = pizza

    def getTotalCost(self):
        return self.additional.getTotalCost() + Pizza.getTotalCost(self)
    
    def getDescription(self):
        return self.additional.getDescription() + ' ' + Pizza.getDescription(self)
    
class Calabresa(Decorator): #DecoradorConcreto1
    cost = 5.00
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class StuffedCrust(Decorator): #DecoradorConcreto2
    cost = 12.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class CreamCheese(Decorator): #DecoradorConcreto3
    cost = 7.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Cheese(Decorator): #DecoradorConcreto4
    cost = 1.50
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Tomatoes(Decorator): #DecoradorConcreto5
    cost = 2.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Pinneaple(Decorator): #DecoradorConcreto6 (eww)
    cost = 8.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class Chicken(Decorator): #DecoradorConcreto7
    cost = 6.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class DarkChocolate(Decorator): #DecoradorConcreto7
    cost = 10.00
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)

class WhiteChocolate(Decorator): #DecoradorConcreto7
    cost = 9.50
    def __init__(self, Pizza):
        Decorator.__init__(self, Pizza)



# Aqui são feitos alguns testes para ver se o código está funcionando.
# Cliente 1: quer uma pizza doce
pizza_doce = DarkChocolate(WhiteChocolate(Plate()))
print(pizza_doce.getDescription() + ": $" + str(pizza_doce.getTotalCost()))

# Cliente 2: quer uma pizza salgada com borda recheada
pizza_salg_borda = StuffedCrust(Calabresa(Chicken(Tomatoes(Cheese(Plate())))))
print(pizza_salg_borda.getDescription() + ": $" + str(pizza_salg_borda.getTotalCost()))

# Client 3: está com muita fome.
pizza_suprema = StuffedCrust(Calabresa(Cheese(Pinneaple(Chicken(DarkChocolate(WhiteChocolate(Tomatoes(CreamCheese(Plate())))))))))
print(pizza_suprema.getDescription() + ": $" + str(pizza_suprema.getTotalCost()))

# Assim, o código está finalizado!