def find_duplicates_in_array(array):
    # O(n)
    existing_elements = set()
    duplicates = set()
    for element in array:
        if element in existing_elements:
            duplicates.add(element)
        else:
            existing_elements.add(element)

    return list(duplicates)