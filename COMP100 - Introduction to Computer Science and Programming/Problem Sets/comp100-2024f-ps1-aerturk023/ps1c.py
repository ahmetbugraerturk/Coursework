# PART C: Critical Decision
def simulate_growth(total_bacteria, total_white_cells, white_cell_growth_rate, bacterial_growth_rate, days=30):
    """Simulate the growth of bacteria and white cells over a number of days."""
    
    currentWC = total_white_cells
    currentB = total_bacteria
    for i in range(days):
        currentWC = int(currentWC * (1+white_cell_growth_rate))
        currentB = int(currentB * (1+bacterial_growth_rate))
    return (currentWC, currentB)

def wc_count_is_acceptable(total_bacteria, total_white_cells):
    """Check if the white cell count is within an acceptable range compared to the bacteria count."""
    
    if total_bacteria-1000<total_white_cells and total_bacteria+1000>total_white_cells:
        return True
    else:
        return False

def find_acceptable_wc_growth_rate(total_bacteria, total_white_cells, bacterial_growth_rate):
    #max 1
    
    minRate = 0
    maxRate = 1
    rate = 0.5
    
    currentWC = total_white_cells
    currentB = total_bacteria
    
    for i in range(500):
        rate = (minRate+maxRate)/2
        currentWC, currentB = simulate_growth(total_bacteria, total_white_cells, rate, bacterial_growth_rate)
        if wc_count_is_acceptable(currentB, currentWC):
            return (currentB, currentWC, rate)
        elif currentB-1000>currentWC:
            minRate = rate
        else:
            maxRate = rate
    
    return None