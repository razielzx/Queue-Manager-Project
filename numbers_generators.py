def turn_generator():
    """Function to yield a counter that represents a turn at any store

    Yields:
        int: Integer that represent the current turn
    """
    
    turn = 0
    while True:
        turn += 1
        yield turn

def greeting_decorator(function, letter):
    """Functon to greet the customer and ask to wait

    Args:
        function (generator): Represent the greeting and gives the turn number to the customer
    """
    
    def greet_turn():
        turn = next(function)
        
        print(f"\nHello customer your turn is the number : {letter}-{turn}")
        print("Please be patient")
        
    return greet_turn    

# Creating generator instances for each store
perfumery_turn = turn_generator()
drugstore_turn = turn_generator()
cosmetics_turn = turn_generator()

# Decorating the greeting functions with the generators
greet_perfumery_turn = greeting_decorator(perfumery_turn, "P")
greet_drugstore_turn = greeting_decorator(drugstore_turn, "D")
greet_cosmetics_turn = greeting_decorator(cosmetics_turn, "C")