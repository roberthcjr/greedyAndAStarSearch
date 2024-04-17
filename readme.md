<!-- Readme about gredy best first search and A* search -->
# Greedy Best First Search and A* Search
This project implements Greedy Best First Search and A* Search algorithms in Python. Both algorithms are implemented in a generic way, so they can be used for any graph and any heuristic function. The project includes a sample graph and heuristic function to demonstrate the working of the algorithms.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Conventional Commit
This project uses [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) messages to make it easier to understand the changes made in the project.

### Project Structure
The project structure is as follows:
- `src.main.py`: This file contains the main code that uses the Greedy Best First Search and A* Search algorithms.
- `src.shared.distancias.py`: This file contains the graph that contains the distancies.
- `src.helpers.search.py`: This file contains the method to search. Can do Greedy First Search and A* search
- `src.helpers.map.py`: This file contains methods to create a html file with a map
- `src.utils.comparations`: This file contains methods to define what search type is and find the minimal distance and its city
- `src.utils.getters`: This file contains a method to get the cost and path

### Prerequisites
You need to have Python installed on your machine. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

### Installing
Follow the below steps to set up the project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/roberthcjr/greedyAndAStarSearch.git

2. Install virtualenv (optional)
    ```bash
    pip install virtualenv

3. Create a virtual environment:
    ```bash
    virtualenv venv

4. Activate the virtual environment:
    ```bash
    source venv/bin/activate

5. Install dependencies:
    ```bash
    pip install -r requirements.txt

6. Run the project:
    ```bash
    python main.py

## Authors
- [Robert Junior](https://github.com/roberthcjr/)
