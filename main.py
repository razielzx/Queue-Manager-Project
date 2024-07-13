import numbers_generators
import display


def main():
    
    print('\n<<<<<<Welcome to the General Store>>>>>>')
    
    while True:
        
        display.display_options()
        try:
            customer_input = int(input("\nSelect the area you would like to pick your turn: "))
            
            if customer_input == 1:
                numbers_generators.greet_cosmetics_turn()
            elif customer_input == 2:
                numbers_generators.greet_perfumery_turn()
            elif customer_input == 3:
                numbers_generators.greet_drugstore_turn()
            elif customer_input == 4:
                print("\nExiting program...")
                break
            else:
                print("\nInvalid area, please select one of the following options")        
        except ValueError:
            print("Invalid input, only numbers")
            
            
if __name__=="__main__":
    main()