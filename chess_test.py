# Piece names and valid board coordinates
valid_pieces = ["pawn", "rook", "king", "queen", "knight"]
valid_coordinates = {f"{chr(c)}{r}" for c in range(ord('a'), ord('h') + 1) for r in range(1, 9)}

# coordinate arrangement
def coord_to_index(coord):
    return ord(coord[0]) - ord('a'), int(coord[1]) - 1

def index_to_coord(row, col):
    return f"{chr(row + ord('a'))}{col + 1}"

# white piece input
def white_input(user_input):
    try:
        piece, coordinate = user_input.split()
        if piece not in valid_pieces:
            return False, "Invalid piece type. Choose from: pawn, rook."
        if coordinate not in valid_coordinates:
            return False, "Invalid coordinate. Use coordinates like 'a1' or 'h8'."
        return True, ""
    except ValueError:
        return False, "Input must be in the format '(piece) (coordinate)'."

# black piece input
def black_input(user_input, black_pieces, white_coordinate):
    if user_input == "done":
        if len(black_pieces) >= 1:
            return True, ""
        else:
            return False, "You must add at least one black piece before typing 'done'."
    try:
        piece, coordinate = user_input.split()
        if piece not in valid_pieces:
            return False, "Invalid piece type. Choose from: pawn, rook, knight, queen, king."
        if coordinate not in valid_coordinates:
            return False, "Invalid coordinate. Use coordinates like 'a1' or 'h8'."
        if any(pos == coordinate for _, pos in black_pieces):
            return False, f"A piece is already at coordinate '{coordinate}'."
        if coordinate == white_coordinate:
            return False, f"white piece's already at the coordinate ({white_coordinate})."
        return True, ""
    except ValueError:
        return False, "Input must be in the format '(piece) (coordinate)' or 'done'."

#  pawn Rule
def pawn_rules(white_coordinate, black_pieces):
    captures = []
    row, col = coord_to_index(white_coordinate)
    possible_targets = [(row - 1, col + 1), (row + 1, col + 1)]
    for target in possible_targets:
        if 0 <= target[0] < 8 and 0 <= target[1] < 8:  
            target_coord = index_to_coord(*target)
            if target_coord in [pos for _, pos in black_pieces]:
                captures.append(target_coord)
    return captures

# rook with obstruction handling
def rook_captures(white_coordinate, black_pieces):
    captures = []
    row, col = coord_to_index(white_coordinate)
    black_positions = {coord_to_index(coord): piece for piece, coord in black_pieces}

    # Rook moves in four directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dr, dc in directions:
        r, c = row, col
        while True:
            r += dr
            c += dc
            if r < 0 or r >= 8 or c < 0 or c >= 8:  
                break
            if (r, c) in black_positions:  
                captures.append(index_to_coord(r, c)) 
                break

    return captures

# Main program

if __name__ == "__main__":
    # Step 1: White piece input
    while True:
        white_input = input("Enter the white piece and its coordinate (e.g., 'rook a1'): ").strip().lower()
        is_valid, error_message = white_input(white_input)
        if is_valid:
            white_piece, white_coordinate = white_input.split()
            print(f"White piece '{white_piece}' added at coordinate '{white_coordinate}'.")
            break
        else:
            print(f"Error: {error_message}")

    # Step 2: Black piece inputs
    black_pieces = []
    print("Enter the black pieces one by one (e.g., 'pawn b2'). Type 'done' when finished:")
    while True:
        black_input = input("Black piece: ").strip().lower()
        is_valid, error_message = black_input(black_input, black_pieces, white_coordinate)
        if black_input == "done" and is_valid:
            print("Finished adding black pieces.")
            break
        elif is_valid:
            black_piece, black_coordinate = black_input.split()
            black_pieces.append((black_piece, black_coordinate))
            print(f"Black piece '{black_piece}' added at coordinate '{black_coordinate}'.")
            if len(black_pieces) == 16:
                print("Maximum number of black pieces (16) reached.")
                break
        else:
            print(f"Error: {error_message}")

    # Step 3: Determine capturable black pieces
    capturable_pieces = []
    if white_piece == "pawn":
        capturable_pieces = pawn_rules(white_coordinate, black_pieces)
    elif white_piece == "rook":
        capturable_pieces = rook_captures(white_coordinate, black_pieces)

    # Results
    print(f"\nWhite piece: {white_piece} at {white_coordinate}")
    print("Black pieces:")
    for bp, pos in black_pieces:
        print(f"  {bp} at {pos}")

    if capturable_pieces:
        print("\nCapturable black pieces:")
        for pos in capturable_pieces:
            print(f"  Black piece at {pos}")
    else:
        print("\nNo capturable black pieces.")


