# Chaos-Driven-Optimization-for-N-Queens-CDONQ
# Abstract

CDO-NQ is a novel optimization algorithm inspired by chaos theory and genetic algorithms. Specifically designed for solving the N-Queens problem, CDO-NQ introduces controlled chaos to efficiently explore the solution space. This documentation provides a comprehensive overview of the algorithm's principles, components, and usage.

# Introduction

The N-Queens problem involves placing N queens on an N×N chessboard without any two queens threatening each other. CDO-NQ leverages chaos theory to introduce perturbation and genetic algorithm operators for evolving solutions. The algorithm aims to find optimal or near-optimal solutions to the N-Queens problem efficiently.

# Algorithm Overview

CDO-NQ operates in a generational manner, iteratively perturbing the population using chaos-driven mechanisms and applying genetic algorithm operators to evolve solutions. The main components include initialization, chaos-driven perturbation, genetic algorithm operators (crossover and mutation), fitness evaluation, and reproduction.

# Main Components

## 1. Initialization
The population is initialized with random N-Queens configurations. The population size and other relevant parameters can be configured.

## 2. Chaos-Driven Perturbation
Chaos theory is applied to perturb the population, introducing controlled chaos to explore the solution space. The chaos_coefficient parameter determines the extent of perturbation.

## 3. Genetic Algorithm Operators
### 3.1 Crossover

A one-point crossover is performed on pairs of individuals from the population, combining elements of both parents to create offspring.

### 3.2 Mutation

Random mutations are introduced with a probability determined by the mutation_rate parameter. This ensures diversity in the population.

## 4. Fitness Evaluation
Fitness is calculated for each individual based on the number of non-attacking pairs of queens. The goal is to maximize fitness, indicating a better solution.

## 5. Reproduction
Individuals are selected for reproduction based on their fitness, and genetic algorithm operators are applied to create offspring. The new generation replaces the old one.

# Parameters

- `population_size`: Size of the population.
- `generations`: Number of generations to run the algorithm.
- `chaos_coefficient`: Controls the degree of chaos introduced during perturbation.
- `mutation_rate`: Probability of mutation for each gene.
