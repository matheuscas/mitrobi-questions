from duplicate_items.find_duplicates_in_array import find_duplicates_in_array


def test_array_with_no_duplicates():
    assert find_duplicates_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == []


def test_array_with_duplicates():
    assert find_duplicates_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5,
                                                                                                        6, 7, 8, 9, 10]