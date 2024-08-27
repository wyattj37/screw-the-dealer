#cards represents how many of each card is left in the deck
#edit accordingly

cards = [0,4,1,2,2,2,2,1,4,0,4,2,2]

def ftd_complex(cards_played, first_val, higher_val, lower_val, weight=1):
    total = sum(cards)
    
    first = cards_played[first_val]
    higher = cards_played[higher_val]
    lower = cards_played[lower_val]
    
    sum_higher = sum(cards_played[first_val + 1:])
    sum_lower = sum(cards_played[:first_val])
    
    g1 = first/total
    g2h = higher / (total - first)
    g2l = lower / (total - first)
    told_higher = sum_higher / (total - first)
    told_lower = sum_lower / (total - first)
    
    plus_ev = 4*g1 + 2*(1-g1)*(told_higher*g2h + told_lower*g2l)
    minus_ev = (1-g1) * ( (higher_val - first_val) * told_higher * (1 - g2h) + (first_val - lower_val) * told_lower * (1-g2l) )
    total_ev = weight*plus_ev - minus_ev
    
    return total_ev
    
def find_guess(cards_played):
    #assign weight here
    selflessness_weight = 1
    
    max_ev = -10000
    guesses = [0,0,0]
    for i in range(4,7):
        for j in range(i+1,13):
            for k in range(i):
                if (ftd_complex(cards_played, i, j, k, selflessness_weight) > max_ev):
                    guesses = [i,j,k]
                    max_ev = ftd_complex(cards_played, i, j, k, selflessness_weight) 
                elif (ftd_complex(cards_played, i, j, k, selflessness_weight) == max_ev):
                    sum_1 = cards_played[i] + cards_played[j] + cards_played[k]
                    sum_2 = cards_played[guesses[0]] + cards_played[guesses[1]] + cards_played[guesses[2]]
                    if (sum_1 > sum_2):
                        guesses = [i,j,k]
                        max_ev = ftd_complex(cards_played, i, j, k, selflessness_weight)
    return guesses

print(find_guess(cards))
