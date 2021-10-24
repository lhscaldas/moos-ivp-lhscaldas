import numpy as np
from numpy.random import randint
from numpy.random import rand
import matplotlib.pyplot as plt
from matplotlib import cm
from math import atan2, pi, sqrt, cos, sin


# plot path and domain
def plot(path_n, restrictions_n):
    # domain
    domain_m = np.zeros((10, 10))
    domain_s = domain_m.reshape((100,))
    restrictions_s = domain_s.copy()
    restrictions_s[restrictions_n] += 1
    restrictions_m = restrictions_s.reshape((10, 10))
    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(restrictions_m, cmap=cm.binary, zorder=0)
    ax.hlines(y=np.arange(0, 10)+0.5, xmin=np.full(10, 0)-0.5,
              xmax=np.full(10, 10)-0.5, color="black", zorder=1)
    ax.vlines(x=np.arange(0, 10)+0.5, ymin=np.full(10, 0)-0.5,
              ymax=np.full(10, 10)-0.5, color="black", zorder=1)
    path_x = [n % 10 for n in path_n]
    path_y = [n//10 for n in path_n]
    ax.plot(path_x, path_y, "o-", zorder=1)
    ax.scatter(path_x[0], path_y[0], marker="^",
               zorder=2, s=100, c="k", label="início")
    ax.scatter(path_x[-1], path_y[-1], marker="X",
               zorder=2, s=100, c="k", label="fim")
    plt.legend()
    plt.show()

def plot_result(path_n, restrictions_n,eval):
    # domain
    domain_m = np.zeros((10, 10))
    domain_s = domain_m.reshape((100,))
    restrictions_s = domain_s.copy()
    restrictions_s[restrictions_n] += 1
    restrictions_m = restrictions_s.reshape((10, 10))
    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(restrictions_m, cmap=cm.binary, zorder=0)
    ax.hlines(y=np.arange(0, 10)+0.5, xmin=np.full(10, 0)-0.5,
              xmax=np.full(10, 10)-0.5, color="black", zorder=1)
    ax.vlines(x=np.arange(0, 10)+0.5, ymin=np.full(10, 0)-0.5,
              ymax=np.full(10, 10)-0.5, color="black", zorder=1)
    path_x = [n % 10 for n in path_n]
    path_y = [n//10 for n in path_n]
    ax.plot(path_x, path_y, "o-", zorder=1)
    ax.scatter(path_x[0], path_y[0], marker="^",
               zorder=2, s=100, c="k", label="início")
    ax.scatter(path_x[-1], path_y[-1], marker="X",
               zorder=2, s=100, c="k", label="fim")
    plt.legend()
    plt.title(f"Comprimento total = {eval:4.6}")
    plt.show()


def multiplot(paths_n, restrictions_n):
    # domain
    domain_m = np.zeros((10, 10))
    domain_s = domain_m.reshape((100,))
    restrictions_s = domain_s.copy()
    restrictions_s[restrictions_n] += 1
    restrictions_m = restrictions_s.reshape((10, 10))
    # plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.matshow(restrictions_m, cmap=cm.binary, zorder=0)
    ax.hlines(y=np.arange(0, 10)+0.5, xmin=np.full(10, 0)-0.5,
              xmax=np.full(10, 10)-0.5, color="black", zorder=1)
    ax.vlines(x=np.arange(0, 10)+0.5, ymin=np.full(10, 0)-0.5,
              ymax=np.full(10, 10)-0.5, color="black", zorder=1)
    for path_n in paths_n:
        path_x = [n % 10 for n in path_n]
        path_y = [n//10 for n in path_n]
        ax.plot(path_x, path_y, "o-", zorder=1)
    ax.scatter(path_x[0], path_y[0], marker="^",
               zorder=2, s=100, c="k", label="início")
    ax.scatter(path_x[-1], path_y[-1], marker="X",
               zorder=2, s=100, c="k", label="fim")
    plt.legend()
    plt.show()


# get full path
def fullPath(path_n):
    path_x = [n % 10 for n in path_n]
    path_y = [n//10 for n in path_n]
    full_path = list()
    for i in range(len(path_n)):
        if path_n[i] not in full_path:
            full_path.append(path_n[i])
        if i < len(path_n)-1:
            x0 = path_x[i]
            x1 = path_x[i+1]
            y0 = path_y[i]
            y1 = path_y[i+1]
            x = x1-x0
            y = y1-y0
            alfa = atan2(y, x)
            l = sqrt(x**2+y**2)
            n = round(l)*5
            if n > 0:
                dl = l/n
                for j in range(1, n):
                    dx = round(x0+j*dl*cos(alfa))
                    dy = round(y0+j*dl*sin(alfa))
                    new_cell = dy*10+dx
                    if new_cell not in full_path:
                        full_path.append(new_cell)
    return full_path


def checkCollision(path_n, restrictions_n):
    n_col = 0
    full_path = fullPath(path_n)
    for node in full_path:
        if node in restrictions_n:
            n_col += 1
    return n_col


def genPaths(begin, end, n_points, n_paths, restrictions_n):
    paths = list()
    for i in range(n_paths):
        ncol = 1
        while(ncol > 0):
            path = list()
            path.append(begin)
            for j in range(n_points-2):
                path.append(randint(begin+1, end))
            path.append(end)
            ncol = checkCollision(path, restrictions_n)
        paths.append(path)
    return paths


def encode(path):
    path_matrix = list()
    for node in path:
        binary = np.binary_repr(node, width=7)
        path_matrix.append([int(x) for x in binary])
    path_matrix = np.array(path_matrix)
    path_string = path_matrix.reshape((35,))
    return path_string.tolist()


def decode(path_s):
    path_v = np.array(path_s)
    path_m = path_v.reshape((5, 7))
    path = list()
    for node in path_m:
        num = int("".join(str(x) for x in node), 2)
        path.append(num)
    return(path)


def multi_encode(paths):
    pop = list()
    for path in paths:
        pop.append(encode(path))
    return pop


def multi_decode(pop):
    paths = list()
    for chromo in pop:
        paths.append(decode(chromo))
    return paths


def length(path_n):
    d = 0
    path_x = [n % 10 for n in path_n]
    path_y = [n//10 for n in path_n]
    for i in range(0, len(path_n)-1):
        x0 = path_x[i]
        y0 = path_y[i]
        x1 = path_x[i+1]
        y1 = path_y[i+1]
        d += sqrt((x1-x0)**2+(y1-y0)**2)
    return d


def objective(path_s, restrictions_n):
    path_n = decode(path_s)
    F = length(path_n) + 300*checkCollision(path_n, restrictions_n)
    return F

# tournament selection
def selection(pop, scores, k=5):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]

# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-2) #7*randint(1, 4)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

# mutation operator
def mutation(bitstring, r_mut, beginend):
    for i in range(len(bitstring)):
        # check for a mutation
        if rand() < r_mut:
            # flip the bit
            bitstring[i] = 1 - bitstring[i]
    begin=[int(x) for x in np.binary_repr(beginend[0], width=7)]
    end=[int(x) for x in np.binary_repr(beginend[1], width=7)]
    bitstring[0:7]=begin
    bitstring[-7:]=end


# genetic algorithm
def genetic_algorithm(objective, restrictions_n, beginend, n_iter, n_pop, r_cross, r_mut):
    # initial population of random bitstring
    paths = genPaths(0, 99, 5, n_pop, restrictions_n)
    pop = multi_encode(paths)
    # keep track of best solution
    best, best_eval = pop[0], objective(pop[0],restrictions_n)
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c,restrictions_n) for c in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
            # print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
            # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut, beginend)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]