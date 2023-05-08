def game(terra, power):
    for k in terra:
        for v in k:
            if power >= v:
                power += v
            else:
                break
    return power

print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))
    
        
            
                