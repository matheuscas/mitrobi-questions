from typing import List

def knapsack(weights: List[int], values: List[int], memo: List[List[int]], capacity: int, num_of_itens: int) -> int:
    if num_of_itens == 0 or capacity == 0:
        return 0

    if memo[num_of_itens][capacity] != -1:
        return memo[num_of_itens][capacity]

    result = 0
    if weights[num_of_itens - 1] > capacity:
        # too heavy
        result = knapsack(weights, values, memo, capacity, num_of_itens - 1)
    else:
        # include item
        result = max(values[num_of_itens - 1] + knapsack(weights, values, memo, capacity - weights[num_of_itens - 1], num_of_itens -1),
                        knapsack(weights, values, memo, capacity, num_of_itens - 1))
    memo[num_of_itens][capacity] = result
    return result

def get_max_value(carrot_types, capacity):
    weights = []
    values = []
    for carrot_type in carrot_types:
        weights.append(carrot_type["kg"])
        values.append(carrot_type["price"])
    num_of_itens = len(weights)
    memo = [[-1 for i in range(capacity + 1)] for j in range(num_of_itens + 1)]
    return knapsack(weights, values, memo, capacity, num_of_itens)

if __name__ == "__main__":
   carrot_types = [{"kg": 5, "price": 100}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]
   capacity = 36
   print(f"Max value is {get_max_value(carrot_types, capacity)}")
