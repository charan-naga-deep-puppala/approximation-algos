def greedy_set_cover(universe, subsets, cost):

    covered = set()  
    selected_sets = set()  
    normalized_cost = {tuple(sorted(k)): v for k, v in cost.items()}

    while covered != universe:
        cost_effectiveness = {
            tuple(sorted(subset)): normalized_cost.get(tuple(sorted(subset)), float('inf')) / len(subset - covered)
            if len(subset - covered) > 0 else float('inf')
            for subset in subsets
        }
        best_subset = min(cost_effectiveness, key=cost_effectiveness.get)
        selected_sets.add(best_subset)
        covered.update(best_subset)
        subsets.remove(set(best_subset))

    return selected_sets

universe = {'a','b','c','d','e','f'}
subsets = [{'a','b','c'}, {'c','f'}, {'e','f'}, {'d','e'}, {'b','d','e'}]
cost = {
    tuple(sorted(['a','b','c'])): 10,
    tuple(sorted(['c','f'])): 10,
    tuple(sorted(['e','f'])): 8,
    tuple(sorted(['d','e'])): 10,
    tuple(sorted(['b','d','e'])): 11
}

selected = greedy_set_cover(universe, subsets, cost)
print("Selected subsets:", selected)
