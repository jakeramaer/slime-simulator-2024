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

## Inner Workings of Each Particle

Each particle in the slime simulator represents an agent that mimics the behavior of a slime mold. The movement and interaction of these particles are influenced by several factors:

### Particle Initialization

Each particle is initialized with the following attributes:
- `id`: A unique identifier for the particle.
- `pos`: The current position of the particle in the grid.
- `angle`: The direction in which the particle is moving, represented as an angle.
- `vel`: The velocity vector calculated from the angle.
- `radius`: The radius of the particle's influence.
- `col`: The color of the particle.
- `sensor_size`: The size of the sensor used to detect trails.
- `sensor_angle`: The angle between the particle's direction and the sensor.
- `sensor_distance`: The distance from the particle's center to the sensor.

### Sensing

Particles sense their environment to detect trails left by other particles. This is done using three sensors:
- **Front Sensor (F)**: Located directly in front of the particle.
- **Left Sensor (FL)**: Located at an angle to the left of the front sensor.
- **Right Sensor (FR)**: Located at an angle to the right of the front sensor.

Each sensor detects the concentration of trails in its vicinity by summing up the values in the grid within the sensor's area.

### Movement

The particle's movement is influenced by the concentration of trails detected by its sensors:
- If the right sensor (FR) detects more trails than the left sensor (FL), the particle turns right.
- If the left sensor (FL) detects more trails than the right sensor (FR), the particle turns left.
- If both sensors detect similar trail concentrations, the particle randomly decides to turn left or right.

The new position of the particle is calculated using its updated angle and velocity, with the position wrapped around the grid using modulo operations to simulate continuous space.

### Depositing Trails

As particles move, they deposit a trail on the grid at their current position. The amount of trail deposited is controlled by the `deposit_amount` parameter and is capped by the `max_deposit` value to prevent over-saturation.

### Trail Decay

Over time, the trails on the grid decay at a rate determined by the `decay_rate` parameter. This decay ensures that the trails fade away, preventing the grid from becoming overly cluttered and allowing new trails to form.

By adjusting these parameters and observing the behavior of the particles, you can explore the dynamic patterns and complex transport networks that emerge from the collective interactions of simple agents.

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

## Controls
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
