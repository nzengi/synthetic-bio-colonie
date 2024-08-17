from genetic_algorithm.population import Population
from genetic_algorithm.fitness import Fitness
from genetic_algorithm.crossover import Crossover
from genetic_algorithm.mutation import Mutation
from synthetic_biology_simulation.genetic_circuits import GeneticCircuit
from synthetic_biology_simulation.circuit_simulation import CircuitSimulation
from robot_control.control import RobotControl
from robot_control.sensors import Sensors

def main():
    # Step 1: Initialize the population
    population = Population(size=10, gene_length=20)
    
    # Step 2: Simulate genetic circuits for each individual
    for individual in population.get_individuals():
        fitness = Fitness.evaluate(individual)
        
        # Create a genetic circuit based on the individual's genes
        circuit = GeneticCircuit(promoter="p1", rbs="r1", cds="c1", terminator="t1")
        simulation_result = CircuitSimulation.simulate(circuit)
        
        # Robot control based on the simulation
        robot = RobotControl()
        environment_input = Sensors.detect_environment()
        action = robot.act(environment_input)
        
        print(f"Individual Fitness: {fitness}, Simulation: {simulation_result}, Robot Action: {action}")

if __name__ == "__main__":
    main()
