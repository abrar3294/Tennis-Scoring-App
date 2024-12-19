def tennis_game():
    scores = {0: "0", 1: "15", 2: "30", 3: "40"}
    player1_pts = 0
    player2_pts = 0
    player1_set = 0
    player2_set = 0
    player1_match = 0
    player2_match = 0

    def scoring_logic():
        nonlocal player1_pts, player2_pts, player1_set, player2_set, player1_match, player2_match
        if player1_pts == 3 and player2_pts == 3:
            print("Deuce! The next player to get a 2-point lead wins!")
        elif player1_pts > 3 and player1_pts - player2_pts == 1:
            print("Player 1 has the advantage!")
        elif player2_pts > 3 and player2_pts - player1_pts == 1:
            print("Player 2 has the advantage!")
        elif player1_pts >= 4 and player1_pts - player2_pts >= 2:
            print("Player 1 wins the game!")
            player1_set += 1
            player1_pts = 0
            player2_pts = 0
            if player1_set >= 6 and player1_set - player2_set >= 2:
                print("Player 1 wins the 1st match")
                player1_match += 1
                player1_set = 0 
                player2_set = 0
                if player1_match == 2:
                    print("Player 1 wins the contest")
                    return True
        elif player2_pts >= 4 and player2_pts - player1_pts >= 2:
            print("Player 2 wins the game!")
            player2_set += 1
            player1_pts = 0
            player2_pts = 0
            if player2_set >= 6 and player2_set - player1_set >= 2:
                print("Player 2 wins the 1st match")
                player2_match += 1
                player1_set = 0
                player2_set = 0
                if player2_match == 2:
                    print("Player 2 wins the contest")
                    return True
        else:
            print(f"Score: Player 1 = {scores.get(player1_pts, '40+')}, Player 2 = {scores.get(player2_pts, '40+')}")

    def display_score():
        nonlocal player1_pts, player2_pts
        point = input("Who scored the point? Enter 1 for Player 1, 2 for Player 2: ").strip()
        if point == "1":
            player1_pts += 1
        elif point == "2":
            player2_pts += 1
        else:
            print("Invalid input - please enter 1 for Player 1 or 2 for Player 2.")
            return False
        return True

    while True:
        if not display_score():
            continue
        if scoring_logic():
            break

tennis_game()        


