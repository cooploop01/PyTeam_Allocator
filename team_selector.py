import random
players = ["Martin", "Craig", "Sue",
           "Claire", "Dave", "Alice",
           "Sonakshi", "Harry", "Jack",
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "William",
           "Ada", "Grace", "Jean",
           "Marissa", "Alan"]
print("\nWelcome to Team Allocator!")
while True:
    random.shuffle(players)
    team1 = players[:len(players)//2]
    print("Team 1 captain: " + random.choice(team1))
    print("\nTeam 1:")
    for player in team1:
        print(player)
    team2 = players[len(players)//2:]
    print("\nTeam 2 captain: " + random.choice(team2))
    print("\nTeam 2:")
    for player in team2:
        print(player)
    response = input("\nPick teams again? Type y or n: ")
    if response == "n":
        print('Thank you. Goodbye!')
        break
