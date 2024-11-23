# container_opti
Trying to formulate a container optimization model. Curious to think more about this porblem after watching this video. - https://www.youtube.com/watch?v=KgE_iK_NGmE

On second thought. Is it an optimization model or a simulation?


## Formulation of the problem

### What to optimize?
Minimize work done by a crane to unload their containers from a cargo ship in its route.

### Variables

Ship: S 

### Constraints
1. The ship can hold finite amount of containers
2. The ship has to deliver all the cargo by the end of the trip
3. A crane can handle 1 container at a time
4. The weight of the ship has to be balanced in 3 dimensions
---
- There are 2 types of containers, 20ft and 40ft
- There are 17 types of containers and there is a matrix of which container can be placed near another

### Simplification assumptions
- The ship is assumed to be cuboid

### Plan forward

- Step 1
    - Bunch of containers and space in the ship -- arrange them to balance weight
        - create ship class and space
        - create container and weight
        - create function to place container in ship
        - formulate optimization equation to find a acceptable fit
- Step 2
    - Use this optimization function to simulate a route
- Step 3
    - Simulate world trade! LFG!

### Rough work 
A `ship` full of `containers` has multiple `trips` between any 2 `ports` in a `route` and at every port a `crane` will unload containers,
