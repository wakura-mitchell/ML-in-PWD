import random
from deap import base, creator, tools, algorithms

# Define the chromosome representation
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Initialize the toolbox
toolbox = base.Toolbox()

# Define the attributes and their ranges
num_resources = 10  # Number of resources to allocate
toolbox.register("resource", random.randint, 0, 1)  # Binary representation for resource allocation
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.resource, n=num_resources)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Define the fitness function
def evaluate(individual):
    # Calculate the efficiency of resource distribution based on your specific criteria
    efficiency = sum(individual) / float(num_resources)  # Example: Ratio of allocated resources
    return efficiency,

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

# Set the population size and number of generations
population_size = 50
num_generations = 100

# Create the initial population
population = toolbox.population(n=population_size)

# Run the genetic algorithm
for generation in range(num_generations):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fitnesses = toolbox.map(toolbox.evaluate, offspring)
    for ind, fit in zip(offspring, fitnesses):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=population_size)

# Get the best individual from the final population
best_individual = tools.selBest(population, k=1)[0]
best_efficiency = evaluate(best_individual)[0]

print("Best Efficiency:", best_efficiency)
print("Allocation:", best_individual)