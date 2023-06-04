import random
from numpy.random import choice
import matplotlib.pyplot as plt


# Read data from file
file_capacity = open('./c.txt', 'r')
file_weight = open('./w.txt', 'r')
file_value = open('./v.txt', 'r')
file_out = open('./out.txt', 'w')
########################################

c = int(file_capacity.readline())
w = []
v = []
for line in file_weight:
    w.append(int(line))
for line in file_value:
    v.append(int(line))

print('Capacity :', c)
print('Weight :', w)
print('Value : ', v)

########################### Taking input from the user ###########################
populationSize = int(input('Size of population : '))
genNumber = int(input('Max number of generation : '))

######## Step 1 ==> Generate population
def generatePopulation(populationSize):
    population =  []
    for i in range(populationSize):
        temp = []
        for j in range(len(w)):
            temp.append(random.randint(0, 1))
        population.append(temp)
    return population

population = generatePopulation(populationSize)
##########################################################################################


age = []
for i in range(len(population)):
    age.insert(i,0)

def value_weight_calculate(population):
    fitness_weight = []
    value = []
    weight = []

    for i, chrom in enumerate(population):
        ft = 0
        wt = 0
        for j, gene in enumerate(chrom):
            ft += gene * v[j]
            wt += gene * w[j]
        value.append(ft)
        weight.append(wt)
    fitness_weight.append(value)
    fitness_weight.append(weight)
    return fitness_weight

######## Calculate the fitness value
def FitnessCalculate(population):
    fitness = []
    popNew = value_weight_calculate(population)
    weight = popNew[1]
    value = popNew[0]

    for index,i in enumerate(weight):
        if (i > c):
            fitness_value = 0
            fitness.append(fitness_value)
        else:
            fitness_value = value[index]
            fitness.append(fitness_value)

    return fitness

## Parent Selection by Roulette method
def RouletteSelection(pop):
    rate = []
    parent = []
    population_index = pop.copy()
    fitness = FitnessCalculate(pop)
    # Values chance to index num
    for i in range(len(population_index)):
        population_index[i] = i
    ### Rate calculate
    total = sum(fitness)
    for x in fitness:
        rate.append(x/total)
    ### Select 2nd parent
    draw = choice(population_index, 2, p=rate)
    first = draw[0]
    second = draw[1]
    parent.append(pop[first])
    parent.append(pop[second])
    return parent
###############################################

## Parent Selection by Tournament method
def TournamentSelection(pop,k):
    size = populationSize
    parent = []
    #     k chromosome Select
    for i in range(int(k)):
        index = random.randint(0, size-1)
        parent.append(pop[index])

    #     fitness check
    k_chrom_value = FitnessCalculate(parent)
    parent_new = []

    for i in range(2):
        max_index = 0
        max = 0
        for index,first in enumerate(k_chrom_value):
            if first > max :
                max_index = index
                max = first

        parent_new.append(parent[max_index])
        k_chrom_value[max_index] = 0

    return parent_new
################################################


def Crossover(parent,n):
    lenght = len(parent[0])
    first_parent = parent[0]
    second_parent = parent[1]
    first_child = []
    second_child = []
    points = []
    start = 0
    for i in range(n):
        points.append(random.randrange(start ,int(lenght)))
        start = points[i]
    start = 0
    end = points[-1]
    for i in range(n):
        if end == points[i]:
            first_child.append(first_parent[start : points[i]] + second_parent[points[i] : ])
            second_child.append(second_parent[start: points[i]] + first_parent[points[i]: ])

            break

        first_child.append(first_parent[start: points[i]] + second_parent[points[i]: points[i + 1]])
        second_child.append(second_parent[start: points[i]] + first_parent[points[i]: points[i + 1]])
        start = points[i + 1]

    # Merge these s-arrays
    first_child2 = []
    second_child2 = []
    for i in first_child:

        first_child2 = first_child2 + i
    for i in second_child:
        second_child2 = second_child2 + i
    new_parents = []
    new_parents.append(first_child2)
    new_parents.append(second_child2)
    return new_parents

### Mutation Method
def Mutation(pop,prob):
    probability = choice([0,1], 1, p= [1 - prob, prob])
    chromosome_index = random.randint(0,int(len(pop)-1))
    gen_index = random.randint(0,int(len(pop[0])-1))
    if probability[0] == 1:
        # mutatitioned chromosome age set 0
        age[chromosome_index] = 0
        if pop[chromosome_index][gen_index] == 1:
            pop[chromosome_index][gen_index] = 0
        else:
            pop[chromosome_index][gen_index] = 1

    return pop


### Fitness Selection Method
def FitnessSelection(pop,parent):
    k_chrom_value = FitnessCalculate(pop)

    for i in range(2):
        min_index = 0
        min = 99999
        for index, first in enumerate(k_chrom_value):
            if first < min:
                min_index = index
                min = first

        pop[min_index] = parent[i]
        k_chrom_value[min_index] = 99999

    return pop


### Age base selection method
def AgeBasedSelection(pop,parent):
    for index,value in enumerate(age):
        age[index] = value + 1

    for i in range(2):
        max_index = 0
        max = 0
        for index, first in enumerate(age):
            if first > max:
                max_index = index
                max = first

        pop[max_index] = parent[i]
        age[max_index] = 0
    return pop

###########################################################
def Elitisim(pop,nextPop):
    k_chrom_value_pop = FitnessCalculate(pop)
    k_chrom_value_nextPop = FitnessCalculate(nextPop)

    #Worst value next pop
    min_index = 0
    min = 99999
    for index, first in enumerate(k_chrom_value_nextPop):
        if first < min:
            min_index = index
            min = first

    #Best value pop
    max_index = 0
    max = 0
    for index, first in enumerate(k_chrom_value_pop):
        if first > max:
            max_index = index
            max = first

    nextPop[min_index] = pop[max_index]
    #age set 0
    age[min_index] = age[max_index]

    return nextPop
###########################################################



###########################################################
print('\nParent Selection\n---------------------------')
print('(1) Roulette-wheel Selection')
print('(2) K-Tournament Selection')

parentSelection = int(input('Which one? '))

if parentSelection == 2:
    k = int(input('k=? (between 1 and ' + str(len(w)) + ') '))

print('\nN-point Crossover\n---------------------------')
n = int(input('n=? (between 1 and ' + str(len(w) - 1) + ') '))
print('\nMutation Probability\n---------------------------')
mutProb = float(input('prob=? (between 0 and 1) '))
print('(1) Age-based Selection')
print('(2) Fitness-based Selection')
survivalSelection = int(input('Which one? '))
elitism = str(input('Elitism? (Y or N) ' ))
print('\n----------------------------------------------------------')
print('initalizing population')
print('evaluating fitnesses')
###########################################################

x = 0
plot_value_list = []
plot_generation_list = []
while (x < genNumber):
    pop_copy = population.copy()
    if parentSelection == 2:
        parent = TournamentSelection(population, k)
    else:
        parent = RouletteSelection(population)

    crossover_parent = Crossover(parent,n)
    population = Mutation(population,mutProb)
    if survivalSelection == 2:
        population = FitnessSelection(population,crossover_parent)
    else:
        population = AgeBasedSelection(population,crossover_parent)


    if elitism == "Y":
        population = Elitisim(pop_copy,population)
    x += 1
    plot_generation_list+=[x]


    values = FitnessCalculate(population)
    max_index = 0
    max = 0
    for index, first in enumerate(values):
        if first > max:
            max_index = index
            max = first

    value = str(max)
    plot_value_list += [value]


##################################################################
weight = value_weight_calculate(population)
values = FitnessCalculate(population)
max_index = 0   
max = 0
for index, first in enumerate(values):
    if first > max:
        max_index = index
        max = first
chromosome = str(population[max_index])
value = str(max)
weight = str(weight[1][max_index])


file_out.write('chromosome:' +chromosome+'\n')
file_out.write('weight:'+ weight +'\n')
file_out.write('value:'+ value)
file_out.close()
plt.xlabel("Generation")
plt.ylabel("Best Value")
plt.title("Knapsack Problem")

# Convert integers to sort by value in y-axis
plot_value_list = [int(i) for i in plot_value_list]
plt.plot(plot_generation_list,plot_value_list)

plt.show()