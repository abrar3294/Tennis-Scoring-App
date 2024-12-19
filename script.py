def tennis_game():
    scores = {0: "0", 1: "15", 2: "30", 3: "40"}
    player1_pts = 0
    player2_pts = 0
    player1_set = 0
    player2_set = 0
    player1_match = 0
    player2_match = 0

    while True:
        point = input("\nWho scored the point?: ")
        if point == '1':
            player1_pts += 1
        elif point == '2':
            player2_pts += 1
        else:
            print("\ninvalid input - enter 1 for player 1 and 2 dor player 2")
            continue 

        if player1_pts == 3 and player2_pts == 3:
            print("\nDeuce! The next player to get a 2-point lead wins!")
        elif player1_pts > 3 and player1_pts - player2_pts == 1:
            print("\nPlayer 1 has the advantage!")
        elif player2_pts > 3 and player2_pts - player1_pts == 1:
            print("\nPlayer 2 has the advantage!")
        elif player1_pts >= 4 and player1_pts - player2_pts >= 2:
            print("\nPlayer 1 wins the game!")
            player1_set += 1
            player1_pts = 0
            player2_pts = 0
            if player1_set >= 6 and player1_set - player2_set >= 2:
                print("\nPlayer 1 wins the 1st match")
                player1_match += 1
                player1_set = 0 
                player2_set = 0
                if player1_match == 2:
                    print("\nPlayer 1 wins the 2nd match - he wins!!!")
                    break
        elif player2_pts >= 4 and player2_pts - player1_pts >= 2:
            print("\nPlayer 2 wins the game!")
            player2_set += 1
            player1_pts = 0
            player2_pts = 0
            if player2_set >= 6 and player2_set - player1_set >= 2:
                print("\nPlayer 2 wins the 1st match")
                player2_match += 1
                player1_set = 0
                player2_set = 0
                if player2_match == 2:
                    print("\nPlayer 2 wins the 2nd match - he wins!!!")
                    break
        
        print("\n===============Tennis Game===============")
        print(f"Point Score:   Player 1 = {scores.get(player1_pts, "40+")}, Player 2 = {scores.get(player2_pts, "40+")}")
        print(f"Set Score:     Player 1 = {player1_set}, Player 2 = {player2_set}")
        print(f"Matches won:   Player 1 = {player1_match}, Player 2: {player2_match}")
        print(f"==========================================\n")

tennis_game()        


