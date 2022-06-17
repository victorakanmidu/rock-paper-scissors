import random
def startGame():
    
    print("====================================== \n")
    print("ROCK PAPER SCISSORS \n")
    print("Welcome player, you're playing against CPU. \n\nSelect R for (Rock), P for (Paper), or S for (Scissors) \n")
    print("======================================")
    print("R  (Rock)\n")
    print("P  (Paper)\n")
    print("S  (Scissors)\n")
    print("E for (EXIT) \n")

    #set game options
    gameChoices = ["R","P","S"]

    #Get CPU choice
    cpuChoice = random.choice(gameChoices)

    #Get Player 1 choice 
    playerChoice =  input("Select option above:\n")
    
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
  
    
    if playerChoice: 
        if playerChoice in gameChoices:
            if playerChoice == cpuChoice:
                print("===============================")
                print("Player  ==>  %s " %playerChoice)
                print("CPU ==> %s " %cpuChoice)
                print("This is a tie, game will now restart")
                restartGame = input("Press any key to restart \n")
                startGame()
            elif playerChoice == "R" and cpuChoice == "P":
                print("===============================")
                print("Player  ==>  %s " %playerChoice)
                print("CPU ==> %s " %cpuChoice)
                print("Paper beats Rock, CPU is the winner ")
            elif playerChoice == "P" and cpuChoice == "S":
                print("===============================")
                print("Player  ==>  %s " %playerChoice)
                print("CPU ==> %s " %cpuChoice)
                print("Scissors beats Paper, CPU is the winner ")
            elif playerChoice == "S" and cpuChoice == "R":
                print("===============================")
                print("Player  ==>  %s " %playerChoice)
                print("CPU ==> %s " %cpuChoice)
                print("Rock beats Scissors, CPU is the winner ")
            else:
                print("===============================")
                print("Player  ==>  %s " %playerChoice)
                print("CPU ==> %s " %cpuChoice)
                print("%s beats %s, Player wins the game" %(playerChoice,cpuChoice))
        else:
            print("Please select a valid option. Select R for (Rock), P for (Paper), or S for (Scissors)")
 

startGame()
 
