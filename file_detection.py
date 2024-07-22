# Returns the list of squares that cannot be accessed by the piece on origin square behind the conflict square

def coordinates_on_same_file(square_coords, conflict_square_coords):
    conflict_rank_num, conflict_file_num = conflict_square_coords
    origin_rank_num, origin_file_num = square_coords

    # Ensure coords are on the same file only
    if not abs(conflict_rank_num - origin_rank_num) > 0 or not abs(conflict_file_num - origin_file_num) == 0:
        raise ValueError("Coordinates are not on the same file")
    
    # Determine the direction from origin square
    if origin_rank_num < conflict_rank_num:
        direction = "ascending"
    
    else:
        direction = "descending"

    # Generate all coordinates on the same rank
    result = []
    for d in range(1,8):
        if direction == "ascending":
            new_rank_num = conflict_rank_num + d
        
        elif direction == "descending":
            new_rank_num = conflict_rank_num - d

        if 0 < new_rank_num <= 8:
            result.append(f"{chr(new_rank_num+64)}{origin_file_num}")

        else: 
            break

    return result  

print(coordinates_on_same_file((2,4), (4,4)))