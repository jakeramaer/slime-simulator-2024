# Slime Simulator 2024

This project is inspired by the paper "Applications of Multi-Agent Slime Mould Computing" by Jeff Jones from the Centre for Unconventional Computing, University of the West of England.

<p align="center">
    <img src="resources/slime.gif" width="500" />
</p>

## Slime Mould Overview

We simulate the behavior of slime molds, specifically Physarum polycephalum, using a multi-agent approach. The slime mold functions as a living computational material influenced by external stimuli. This simulation explores the self-organizing and adaptive behaviors of slime molds to form complex transport networks.

Slime molds are fascinating single-celled organisms that can solve complex problems such as finding the shortest path in a maze or optimizing networks. The slime mold adapts its body plan in response to environmental stimuli like nutrient attractants, repellents, and hazards during its growth and foraging activities.

## Features

- Real-time simulation of slime mold behavior
- Visual representation of particle trails and sensor areas
- Adjustable parameters for sensitivity, decay rate, and more
- Interactive controls for adding particles, resetting the simulation, and toggling views

## Installation

To run this simulation, you need to have Python installed along with the Pygame library. You can install Pygame using pip:

```bash
pip install pygame
```

## Usage

To start the simulation, run the slime_simulator.py script:

```bash
python slime.py
```

Controls
- Q: Toggle view of the sensory areas of particles
- W: Toggle view of the actual particles
- 1: Add a single particle to the center of the simulation
- 2: Add 100 particles to the center of the simulation
- R: Reset the simulation
- A: Double the decay rate
- Z: Halve the decay rate
- S: Double the sensitivity
- X: Halve the sensitivity

<p align="center">
    <img src="resources/balls.gif" width="500" />
</p>

## Parameters

You can adjust the following parameters to customize the simulation:

- width: Width of the simulation grid
- height: Height of the simulation grid
- grid_size: Size of each grid cell
- show_dots: Boolean to toggle the display of particles
- show_sensors: Boolean to toggle the display of sensory areas
- radius: Initial radius for particle distribution
- n: Number of initial particles
- col: Color of particles
- decay_rate: Rate at which trails decay
- sensitivity: Sensitivity of particles to trails
- max_deposit: Maximum deposit amount for trails
- deposit_amount: Amount deposited by particles
