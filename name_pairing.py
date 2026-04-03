REMOVE_CHARS = [".", ",", "!", "?", "(", ")"]
REPLACE_CHARS = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ý": "y"}

def standardize_names(names_list):
    standardized = []

    for name in names_list:
        name = name.strip().lower()

        for char in REMOVE_CHARS:
            name = name.replace(char, "")

        for old, new in REPLACE_CHARS.items():
            name = name.replace(old, new)

        standardized.append(name)

    return standardized

def file_to_list(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read().splitlines()

    except FileNotFoundError:
        return "Error: File not found."


# TODO: rename sim1 sim2
def get_similarity(name1, name2):
    similarity = 0.0
    sim1 = 0
    sim2 = 0

    for character in name1:
        if character in name2:
            sim1 += 1

    for character in name2:
        if character in name1:
            sim2 += 1

    sum = sim1 + sim2
    length_of_both= len(name1) + len(name2)

    if length_of_both != 0:
        similarity = sum / length_of_both

    return similarity

def get_max(list):
    max = list[0]
    max_on_index = 0

    #TODO: len(list) alebo len(list)+1??
    for indx in range(0, len(list)):
        if list[indx] > max:
            max = list[indx]
            max_on_index = indx

    return max_on_index

def pair_names(to_assign, reference):
    pairs = []

    # TODO: co ked neni v to_assign nic???
    if not to_assign:
        return pairs

    to_assign = standardize_names(to_assign)

    for name in to_assign:
        similarities = []

        for ref in reference:
            similarities.append(get_similarity(name, ref))

        best_index = get_max(similarities)
        pairs.append((name, reference[best_index]))

    return pairs

def main(to_assign_file_name:str, reference_file_name:str):
    path_to_assign = "data/" + to_assign_file_name
    path_reference = "data/" + reference_file_name
    
    raw_to_assign = file_to_list(path_to_assign)
    raw_reference = file_to_list(path_reference)

    if raw_to_assign is None or raw_reference is None:
        return []

    to_assign = standardize_names(raw_to_assign)
    reference = standardize_names(raw_reference)

    return (pair_names(to_assign, reference))

assign = "to_assign_names.txt"
ref = "reference_names.txt"

print(main(assign, ref))
