

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from utils.utils1 import *

matplotlib.use('Agg')

WORLD_SIZE = 5
A_POS = [0, 1]
A_PRIME_POS = [4, 1]
B_POS = [0, 3]
B_PRIME_POS = [2, 3]
DISCOUNT = 0.9
Grid_World = (WORLD_SIZE , WORLD_SIZE)

ACTIONS = [np.array([0, -1]),
           np.array([-1, 0]),
           np.array([0, 1]),
           np.array([1, 0])]

ACTION_PROB = 0.25

def random_policy_value():
    A = -1 * np.eye(WORLD_SIZE * WORLD_SIZE)
    b = np.zeros(WORLD_SIZE * WORLD_SIZE)
    
    """
    bellman equation을 이용한 Ax = b 선형방정식 최적해 solution
    """

    x = np.linalg.solve(A, b)
    print("solution1\n", x)
    draw_image_1(np.round(x.reshape(WORLD_SIZE, WORLD_SIZE), decimals=2))
    plt.savefig('./images/linear_system.png')
    plt.close()
    
def value_iteration():
    new_state_values = np.zeros((WORLD_SIZE, WORLD_SIZE))
    while True:
        state_values = new_state_values.copy()
        old_state_values = state_values.copy()
        
        """
        value iteration을 활용한 grid world 최적화 코드 작성
        """

        max_delta_value = abs(old_state_values - new_state_values).max()
        if max_delta_value < 1e-4:
            break
    draw_image_2(np.round(new_state_values, decimals=2))
    print("solution2\n", new_state_values)
    plt.savefig('./images/value_iteration.png')
    plt.close()

if __name__ == '__main__':
    random_policy_value()
    value_iteration()
