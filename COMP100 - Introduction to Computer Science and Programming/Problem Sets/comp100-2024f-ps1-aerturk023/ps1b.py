# PART B: Mounting Infection
def wc_count_with_bacterial_growth(total_bacteria, total_white_cells, white_cell_growth_rate, bacterial_growth_rate):
    
    currentWC = total_white_cells
    currentB = total_bacteria
    day = 0
    while currentWC <= currentB:
        currentWC = int(currentWC * (1+white_cell_growth_rate))
        currentB = int(currentB * (1+bacterial_growth_rate))
        day += 1
        if day >= 90:
            day = None
            break
    return day