import unittest
from arrays import index_of_min, index_of

def test_index_of_min():
	assert index_of_min([1, 2, 3, 5]) == 0
	assert index_of_min([5, 65, 2, 90]) == 2

def test_index_of():
	assert index_of([1, 2, 3, 5], 3) == 2
	assert index_of([5, 65, 2, 90], 4) == -1

def test_compare_arrays():
	assert compare_arrays([1, 2, 3], [1, 2, 3, 4]) == 1
	assert compare_arrays([1, 2, 3, 4], [1, 2, 3]) == -1
	assert compare_arrays([7, 8, 9], [1, 2, 3, 4]) == 1
	assert compare_arrays([1, 2, 3, 4], [7, 8, 9]) == -1
	assert compare_arrays([7, 8, 9], [1, 2, 3]) == -1
	assert compare_arrays([1, 2, 3], [7, 8, 9]) == 1

def test_get_mode():
	assert get_mode("random") == "random"
	assert get_mode("keyboard") == "keyboard"
	assert get_mode("a") == "Invalid mode, try again: "

def test_find_maxs():
	assert find_maxs([1, 2, 3, 4]) == [2, 3, 4]
	assert find_maxs([1, 1, 1, 1]) == [1, 1, 1]

def test_find_sequence():
	assert find_sequence([1, 1, 1, 5]) == [1, 1, 1]
	assert find_sequence([2, 2, 1, 5]) == [2, 2]
	assert find_sequence([4, 2, 1]) == [4]
	
if __name__ == "__main__":
	test_index_of_min()
	test_index_of()
	print('Everything passed')

