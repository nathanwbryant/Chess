def coordinates_on_same_diagonal(conflict_square_coords, square_coords):
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coordinates are on the same diagonal
    if abs(conflict_file_num - origin_file_num) != abs(conflict_rank_num - origin_rank_num): # if 1 doesnt equal 1
        raise ValueError("Coordinates are not on the same diagonal")

    # Determine the direction of the diagonal
    if (conflict_file_num < origin_file_num and conflict_rank_num < origin_rank_num): # conflict is down to the left
        direction = "descending backwards"

    elif (conflict_file_num < origin_file_num and conflict_rank_num > origin_rank_num): # 
        direction = "descending forwards"

    elif (conflict_file_num > origin_file_num and conflict_rank_num > origin_rank_num): # 
        direction = "ascending forwards"

    else:
        direction = "ascending backwards"

    # Generate all coordinates on the same diagonal
    result = []
    for d in range(1, 8):
        if direction == "ascending forwards":
            new_file_num, new_rank_num = conflict_file_num + d, conflict_rank_num + d     
            
        elif direction == "ascending backwards":
            new_file_num, new_rank_num = conflict_file_num + d, conflict_rank_num - d 

        elif direction == "descending backwards":
            new_file_num, new_rank_num = conflict_file_num - d, conflict_rank_num - d     

        else:
            new_file_num, new_rank_num = conflict_file_num - d, conflict_rank_num + d     
            
        if 0 < new_file_num <= 8 and 0 < new_rank_num <= 8:
            result.append(f"{chr(new_rank_num+64)}{new_file_num}")
        
        else:
            break

    return result 

# Example usage
conflict_square_coords = (3, 4) 
square_coords = (6, 7)           
print(coordinates_on_same_diagonal(conflict_square_coords, square_coords))
