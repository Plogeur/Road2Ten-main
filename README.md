# Road2Ten (R2T)

Road2Ten is IA project designed to optimize the breeding process of Dragodindes (a fictional creature from the game Dofus). The model try to find the best breedind paths to archive with a minimal breeding the 10th generation (begining to the 1st one).

## Table of Contents

- [Overview](#Overview)
- [Installation](#Installation)
- [Features](#Features)
- [Models](#Models)
- [Results](#Results)
- [License](#License)

## Overview

The project encompasses various models, both machine learning-based and traditional, designed to progressively achieve a new generation of Dragodindes. The breeding process, including the probability determination for color outcomes based on parental colors and genealogical data, is derived from the formulas and information provided on [this website](https://felis-silvestris.lescigales.org/).

However, there are a few key differences :
- Capacities are not considered.
- Times are not present (in the standart model) / time are present but change (in the time model)

## Installation

This project requires Python 3.10 or latest.

To set up the project, run the following commands:

```bash
git clone https://github.com/Plogeur/Road2Ten.git
cd Road2Ten
pip install -r requirements.txt
```

## Features

- Calculate breeding probabilities for single-color and bi-color Dragodindes.
- Account for genealogical influence up to great-grandparents.
- Handle special cases for specific color combinations.

## Models

The project includes three traditional models and one machine learning model based on Proximal Policy Optimization (PPO):

- Random Model: Breeds Dragodindes randomly, without any specific strategy.

- Best Generation Model: Focuses on breeding only with the best actual generation of Dragodindes.

- Select and Purify Model: Aims to selectively breed and purify specific colors or generations of Dragodindes to more accurately achieve the final generation.

- PPO Model: A reinforcement learning model that rewards actions leading to new generations or successful purification of Dragodindes, optimizing the breeding process over time.

## Results 

![results](https://github.com/user-attachments/assets/16c9178a-af02-4905-b054-7fc9df4b9f8b)
