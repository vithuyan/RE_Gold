ballots = [{'gold': 'Smudge', 'silver': 'Tigger', 'bronze': 'Simba'},
           {'gold': 'Bella', 'silver': 'Lucky', 'bronze': 'Tigger'},
           {'gold': 'Bella', 'silver': 'Boots', 'bronze': 'Smudge'},
           {'gold':'Boots', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Lucky', 'silver': 'Felix', 'bronze': 'Bella'},
           {'gold': 'Smudge', 'silver': 'Simba', 'bronze': 'Felix'}]


can_list = {}
for vote in ballots:
    for place, name in vote.items():
        if place == 'gold' and name in can_list:
            can_list[name] += 3
        if place == 'gold' and name not in can_list:
            can_list[name] = 3
        if place == 'silver' and name in can_list:
            can_list[name] += 2
        if place == 'silver' and name not in can_list:
            can_list[name] = 2
        if place == 'bronze' and name in can_list:
            can_list[name] += 1
        if place == 'bronze' and name not in can_list:
            can_list[name] = 1

current_score = 0
for name, points in can_list.items():
    if points > current_score:
        current_score_winner = name
        current_score = points            
