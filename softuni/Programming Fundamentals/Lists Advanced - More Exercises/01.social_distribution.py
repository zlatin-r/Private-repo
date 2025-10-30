population = list(map(int, input().split(", ")))
min_wealth = int(input())

if sum(population) < len(population) * min_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i] < min_wealth:
            richest_index = population.index(max(population))
            difference = min_wealth - population[i]
            
            population[richest_index] -= difference
            population[i] += difference
    
    print(population)
    