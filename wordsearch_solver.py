
wordsearch = [
    #  0    1    2    3    4    5    6    7    8    9   
    [ 'Z', 'S', 'S', 'R', 'F', 'T', 'Q', 'D', 'Z', 'F' ],  # 0
    [ 'Y', 'A', 'E', 'G', 'X', 'O', 'P', 'I', 'R', 'X' ],  # 1
    [ 'F', 'X', 'J', 'A', 'D', 'R', 'A', 'O', 'J', 'C' ],  # 2
    [ 'A', 'K', 'Z', 'P', 'L', 'T', 'G', 'R', 'A', 'D' ],  # 3
    [ 'A', 'L', 'R', 'V', 'O', 'O', 'Y', 'W', 'C', 'O' ],  # 4
    [ 'D', 'H', 'V', 'R', 'J', 'I', 'T', 'Q', 'U', 'G' ],  # 5
    [ 'N', 'H', 'R', 'T', 'A', 'S', 'A', 'Y', 'J', 'I' ],  # 6
    [ 'A', 'A', 'E', 'B', 'Y', 'E', 'A', 'G', 'L', 'E' ],  # 7
    [ 'P', 'J', 'X', 'P', 'Q', 'O', 'B', 'J', 'Z', 'N' ],  # 8
    [ 'Q', 'P', 'Y', 'R', 'R', 'T', 'A', 'C', 'A', 'M' ]]  # 9

words = ['PARROT', 'PANDA', 'TORTOISE', 'SEAL', 'CAT', 'DOG', 'EAGLE', 'FROG', 'BEAR']

directions = {
    'WEST':       ( 0, -1),
    'NORTH_WEST': (-1, -1),
    'NORTH':      (-1,  0),
    'NORTH_EAST': (-1,  1),
    'EAST':       ( 0,  1),
    'SOUTH_EAST': ( 1,  1),
    'SOUTH':      ( 1,  0),
    'SOUTH_WEST': ( 1, -1)
    }

width  = len(wordsearch[0][:])
height = len(wordsearch[:][-1])


def search(word, position, direction=None):
    # Base case if whole word is found
    if len(word) == len(position):
        return position

    i_curr, j_curr = position[-1]
    
    # If root character of word, try each direction until the word is found or all directions exhausted
    if not direction:
        for d, c  in directions.items():
            i = i_curr + c[0]
            j = j_curr + c[1]

            # Check for out of bounds on the grid
            if i not in range(height) or j not in range(width):
                continue

            if wordsearch[i][j] == word[len(position)]:
                # Copy list to not mutate original position list
                position_copy = position.copy()
                position_copy.append((i, j))
                searched = search(word, position_copy, direction=d)

                # If character searched does not lead to full word
                if not searched:
                    continue    
                else:
                    return searched

    # if not root character, check next character in the given direction
    else:
        i = i_curr + directions[direction][0]
        j = j_curr + directions[direction][1]

        # Check for out of bounds on the grid
        if i not in range(height) or j not in range(width):
            return None

        if wordsearch[i][j] == word[len(position)]:
            position.append((i, j))
            return search(word, position, direction=direction)
        else:
            return None


if __name__ == '__main__':
    # Iterate over each character and check the first letter of each word
    for i in range(height):
        for j in range(width):
            for word in words:
                if wordsearch[i][j] == word[0]:
                    positions = search(word, [(i, j)])
                    if not positions:
                        continue
                    else:
                        print(f'{word}: {positions}')
                
        




