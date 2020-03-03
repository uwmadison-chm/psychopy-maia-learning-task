#!/usr/bin/env python3

import numpy as np
import pandas as pd

def build_order(trials, offset=0, length=8):
    def semirand(length, how_many):
        s = np.mod(np.arange(length), how_many)
        np.random.shuffle(s)
        return s
    
    # Gain, look, loss trials evenly
    kind = semirand(trials, 3)
    
    # Left or right position evenly
    position = semirand(trials, 2)
    
    # For every gain/look/loss trial, 80% of trials will return feedback as
    # expected, 20% will be reversed. -1 is the 20%, +1 the 80%.
    result = np.random.choice([1,-1], size=trials, p=[0.8, 0.2])

    # Each kind gets a pair of (different) correct and incorrect stimuli
    # We keep simulation run stimuli different from actual run by adding 12.
    stim_start = 1
    stim_start += offset
    stim_nums = list(range(stim_start, stim_start + length))
    np.random.shuffle(stim_nums)
    stim_names = [f"stimuli/tunga_{x:02}.bmp" for x in stim_nums]

    # Now pick stimuli pairs
    nums = [
        stim_nums[0:2],
        stim_nums[2:4],
        stim_nums[4:6],
    ]
    names = [
        stim_names[0:2],
        stim_names[2:4],
        stim_names[4:6],
    ]

    # Insert stimuli, iterating over the trials
    stim_left = []
    stim_right = []
    stim_left_name = []
    stim_right_name = []
    correct = []
    for i in range(trials):
        this_kind = kind[i]
        this_position = position[i]
        this_result = result[i]
        this_stims = nums[this_kind]
        this_stim_names = names[this_kind]

        if this_position == 0:
            stim_left.append(this_stims[0])
            stim_right.append(this_stims[1])
            stim_left_name.append(this_stim_names[0])
            stim_right_name.append(this_stim_names[1])
            if this_result > 0:
                correct.append('left')
            else:
                correct.append('right')
        else:
            stim_left.append(this_stims[1])
            stim_right.append(this_stims[0])
            stim_left_name.append(this_stim_names[1])
            stim_right_name.append(this_stim_names[0])
            if this_result > 0:
                correct.append('right')
            else:
                correct.append('left')
    
    return pd.DataFrame({
        'kind': kind,
        'position': position,
        'result': result,
        'stim_left': stim_left,
        'stim_right': stim_right,
        'stim_left_name': stim_left_name,
        'stim_right_name': stim_right_name,
        'correctAns': correct,
        })


for session in range(3):
    for i in range(100):
        order = build_order(72, offset=session)
        order.to_csv(f"orders/session{session + 1}/order{i:03d}.csv", index=False)
