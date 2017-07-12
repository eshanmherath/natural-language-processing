__author__ = 'eshan'

def are_they_same(character_1, character_2):
    if character_1 == character_2:
        return True
    else:
        return False


def get_diagonal_value(matrix, row_position, column_position):
    return matrix[row_position-1][column_position-1]


def get_minimum_plus_one(matrix, row_position, column_position):

    minimum = matrix[row_position][column_position-1]

    if matrix[row_position-1][column_position-1] < minimum:
        minimum = matrix[row_position-1][column_position-1]

    if matrix[row_position-1][column_position] < minimum:
        minimum = matrix[row_position-1][column_position]

    return minimum + 1


print("########################################")
print("#### Levenshtein Distance Calculator ####")
print("########################################")

first_word = input("Enter first word : ")
second_word = input("Enter second word : ")

print("Calculating distance for transforming '" + first_word + "' to '" + second_word + "'")

characters_in_first_word = len(first_word)
characters_in_second_word = len(second_word)

columns = characters_in_first_word+1
rows = characters_in_second_word+1

distance_matrix = [[0 for x in range(columns)] for y in range(rows)]

print("\nfilling the first row")
for i in range(columns):
    distance_matrix[0][i] = i
print(distance_matrix)

print("\nfilling the first column")
for i in range(rows):
    distance_matrix[i][0] = i
print(distance_matrix)

print("\nfilling the remaining distances")

for row_index in range(1, rows):
    for column_index in range(1, columns):
        first_word_character = first_word[column_index-1]
        second_word_character = second_word[row_index-1]
        print("considering " + first_word_character + " -> " + second_word_character)

        if are_they_same(first_word_character, second_word_character):
            distance_matrix[row_index][column_index] = get_diagonal_value(distance_matrix, row_index, column_index)
        else:
            distance_matrix[row_index][column_index] = get_minimum_plus_one(distance_matrix, row_index, column_index)

print('\nfinal distance matrix\n')
for i in range(rows):
    for j in range(columns):
        print(distance_matrix[i][j], end=" "),
    print('')

print('')
print("Levenshtein distance for transforming '" + first_word + "' to '" + second_word + "' is : " + str(distance_matrix[rows-1][columns-1]))

