import random
import numpy as np

job_times = [4, 6, 5, 3, 7]
machines = 3
population_size = 10
generations = 100

def initialize_population(jobs, machines, pop_size):
    return [np.array([(task, random.randint(0, machines - 1)) for task in range(len(jobs))]) for _ in range(pop_size)]

def fitness(chromosome):
    load_distribution = [0] * machines
    for task, assigned_machine in chromosome:
        load_distribution[assigned_machine] += job_times[task]
    return 1 / (sum([load**2 for load in load_distribution]) + 0.01)

def crossover(parent1, parent2):
    split1, split2 = sorted(random.sample(range(len(parent1)), 2))
    child1 = np.concatenate((parent1[:split1], parent2[split1:split2], parent1[split2:]))
    child2 = np.concatenate((parent2[:split1], parent1[split1:split2], parent2[split2:]))
    return child1, child2

def mutate(chromosome):
    pos = random.randint(0, len(chromosome) - 1)
    chromosome[pos] = (chromosome[pos][0], random.randint(0, machines - 1))
    return chromosome

def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    selection_point = random.uniform(0, total_fitness)
    cumulative = 0
    for individual, score in zip(population, fitness_values):
        cumulative += score
        if cumulative > selection_point:
            return individual

population = initialize_population(job_times, machines, population_size)

for _ in range(generations):
    fitness_scores = [fitness(ind) for ind in population]
    next_generation = []
    for _ in range(population_size // 2):
        parent1 = roulette_selection(population, fitness_scores)
        parent2 = roulette_selection(population, fitness_scores)
        offspring1, offspring2 = crossover(parent1, parent2)
        offspring1, offspring2 = mutate(offspring1), mutate(offspring2)
        next_generation.extend([offspring1, offspring2])
    population = next_generation

optimal_solution = max(population, key=lambda ind: fitness(ind))
print("Optimal job distribution (job_id, machine_id):")
print(optimal_solution)
