# returns the inaccessable squares as the origin square to the conflict square

def coordinates_on_same_rank(square_coords, conflict_square_coords):
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coords are on the same rank only
    if not abs(conflict_file_num - origin_file_num) > 0 or not abs(conflict_rank_num - origin_rank_num) == 0:
        raise ValueError("Coordinates are not on the same rank")
    
    # Determine the direction from origin square
    if origin_file_num < conflict_file_num:
        direction = "ascending"
    
    else:
        direction = "descending"

    # Generate all coordinates on the same rank
    result = []
    for d in range(1,8):
        if direction == "ascending":
            new_file_num = conflict_file_num + d
        
        elif direction == "descending":
            new_file_num = conflict_file_num - d

        if 0 < new_file_num <= 8:
            result.append(f"{chr(origin_rank_num+64)}{new_file_num}")

        else: 
            break

    return result  

print(coordinates_on_same_rank((1,5), (1,2)))