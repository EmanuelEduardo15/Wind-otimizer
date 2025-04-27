import random

class GeneticOptimizer:
    def __init__(self, wind_field, population_size=50):
        self.wind_field = wind_field
        self.population = [
            [(random.randint(0, len(wind_field)-1), 
              random.randint(0, len(wind_field)-1)) 
             for _ in range(10)]  # 10 turbinas
            for _ in range(population_size)
        ]
        
    def fitness(self, positions):
        return sum(self.wind_field[x][y] for (x,y) in positions)
    
    def evolve(self, generations=100):
        for _ in range(generations):
            self.population.sort(key=self.fitness, reverse=True)
            top_10 = self.population[:10]
            new_population = top_10.copy()
            for _ in range(len(self.population) - 10):
                parent = random.choice(top_10)
                child = [mutate(pos) for pos in parent]
                new_population.append(child)
            self.population = new_population
        return max(self.population, key=self.fitness)

def mutate(position):
    x, y = position
    return (x + random.randint(-1,1), y + random.randint(-1,1))
