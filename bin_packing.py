import random

item_sizes = [7, 5, 3, 2]
bin_capacity = 10
population_size = 10
generations = 100

def initialize_population(items, pop_size):
    pop = []
    for _ in range(pop_size):
        bins = [[]]
        for item in items:
            allocated = False
            for container in bins:
                if sum(container) + item <= bin_capacity:
                    container.append(item)
                    allocated = True
                    break
            if not allocated:
                bins.append([item])
        pop.append(bins)
    return pop

def fitness(bins):
    num_bins = len(bins)
    unused_space = sum(bin_capacity - sum(bin_) for bin_ in bins)
    return 1 / (num_bins + (unused_space / 100) + 0.01)

def crossover(parent1, parent2):
    split = random.randint(1, min(len(parent1), len(parent2)) - 1)
    offspring1 = parent1[:split] + parent2[split:]
    offspring2 = parent2[:split] + parent1[split:]
    return offspring1, offspring2

def mutate(bins):
    if len(bins) < 2:
        return bins
    source_bin = random.choice(bins)
    if not source_bin:
        return bins
    element = random.choice(source_bin)
    source_bin.remove(element)
    reassigned = False
    for container in bins:
        if sum(container) + element <= bin_capacity:
            container.append(element)
            reassigned = True
            break
    if not reassigned:
        bins.append([element])
    return bins

def roulette_selection(pop, fitness_values):
    total_fitness = sum(fitness_values)
    selection = random.uniform(0, total_fitness)
    cumulative = 0
    for candidate, score in zip(pop, fitness_values):
        cumulative += score
        if cumulative > selection:
            return candidate

population = initialize_population(item_sizes, population_size)

for _ in range(generations):
    fitness_scores = [fitness(ind) for ind in population]
    next_gen = []
    for _ in range(population_size // 2):
        parent1 = roulette_selection(population, fitness_scores)
        parent2 = roulette_selection(population, fitness_scores)
        offspring1, offspring2 = crossover(parent1, parent2)
        offspring1, offspring2 = mutate(offspring1), mutate(offspring2)
        next_gen.extend([offspring1, offspring2])
    population = next_gen

optimal_bins = max(population, key=lambda c: fitness(c))
print("Optimal bin configuration:")
for index, container in enumerate(optimal_bins):
    print(f"Bin {index + 1}: {container} (Filled {sum(container)}/{bin_capacity})")
