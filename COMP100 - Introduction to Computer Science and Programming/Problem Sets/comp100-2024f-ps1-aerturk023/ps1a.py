# PART A: Initial Struggle
def wc_count_no_bacterial_growth(total_bacteria, total_white_cells, white_cell_growth_rate):
    
    currentWC = total_white_cells
    day = 0
    while currentWC <= total_bacteria:
        currentWC = int(currentWC * (1+white_cell_growth_rate))
        day += 1
        if day >= 90:
            day = None
            break
    return day