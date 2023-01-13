import random

welcomePrompt = "Hello and welcome to blackjack!"

print (welcomePrompt)

numbers = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'King', 'Queen']

suits = ['Spades', "Hearts", "Clubs", "Diamonds"]

decision = None

stand = False
total = 0
computerTotal = 0
while stand == False and total < 21:
    decision = input("Press h to hit, or press s to stand: ")
    if decision == "h":
        numberRolled = numbers[random.randint(0, len(numbers) - 1)]
        suitRolled = suits[random.randint(0, len(suits) - 1)]
        print("Your card is a " + str(numberRolled) + " of " + suitRolled)
        if not str(numberRolled).isnumeric():
            if numberRolled == "Ace":
                if total + 11 > 21:
                    total += 1
                    print ("Your total is " + str(total))
                else:
                    total += 11
                    print ("Your total is " + str(total))
            else:
                total += 10 
                print ("Your total is " + str(total))
        else:
            total += numberRolled
            print ("Your total is " + str(total))
    elif decision == "s":
        print("You decided to stand")
        print("Your final number is " + str(total))
        stand = True
        
        while computerTotal < 22 and computerTotal <= total:
            numberRolledByComputer = numbers[random.randint(0, len(numbers) - 1)]
            suitRolledByComputer = suits[random.randint(0, len(suits) - 1)]
        
            print ("The computer's card is "+ str(numberRolledByComputer) + " of " + suitRolledByComputer)
            
            if not str(numberRolledByComputer).isnumeric():
                if numberRolledByComputer == "Ace":
                    if computerTotal + 11 > 21:
                        computerTotal += 1
                        print ("The computer's total is " + str(computerTotal))
                    else:
                        computerTotal += 11
                        print ("The computer's total is " + str(computerTotal))
                else:
                    computerTotal += 10 
                    print ("The computer's total is " + str(computerTotal))
            else:
                computerTotal += numberRolledByComputer
                print ("The computer's total is " + str(computerTotal))
        break
    else: 
        print("Invalid Choice. Please Try again.")

if total == 21 and stand == True:
    print("Blackjack!")
elif computerTotal > total and computerTotal <= 21 and stand == True:
    print("The computer won!")
elif computerTotal > 21 and stand == True:
    print("The computer went over!")
    print("You win!")
else:
    print("You went over!")
