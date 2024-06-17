import random

def monty_hall_simulation(num_trials):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_trials):
        prize_door = random.randint(1, 3)
        
        player_choice = random.randint(1, 3)
        
        remaining_doors = [1, 2, 3]
        remaining_doors.remove(player_choice)
        
        if prize_door in remaining_doors:
            remaining_doors.remove(prize_door)
        opened_door = random.choice(remaining_doors)
        
        remaining_doors = [1, 2, 3]
        remaining_doors.remove(player_choice)
        remaining_doors.remove(opened_door)
        switch_choice = remaining_doors[0]
        
        if player_choice == prize_door:
            stay_wins += 1
        
        if switch_choice == prize_door:
            switch_wins += 1

    return stay_wins, switch_wins

num_trials = 10000
stay_wins, switch_wins = monty_hall_simulation(num_trials)

print(f"Количество симуляций: {num_trials}")
print(f"Выигрыши при оставлении выбора: {stay_wins} ({stay_wins / num_trials * 100:.2f}%)")
print(f"Выигрыши при переключении: {switch_wins} ({switch_wins / num_trials * 100:.2f}%)")