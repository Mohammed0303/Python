import sys

user1 = input("Enter player1 name: ")
user2 = input("Enter player2 name: ")
user1_answer = input("%s, do you want to choose rock, paper or scissors?: "  %user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?: " %user2)

def compare(u1, u2):
    if u1 == u2:
        return("it's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return ("Rock wins!")
        else:
            return ("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return ("scissors wins!")
        else:
            return ("Rocks wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return ("Paper wins!")
        else:
            return ("Scissors wins!")
    else:
        return ("Invalid input! You have entered t=rock,paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))