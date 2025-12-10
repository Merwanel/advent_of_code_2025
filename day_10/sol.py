import collections
import sys
import os
import typing

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.reader import read_lines
from tools.test_utils import shouldBeEqual
import z3


from tools.bit_array import BitArray

def solve(is_part1 = True, fileName: str = ''):
    input_path = os.path.join(os.path.dirname(__file__), fileName)
    ans_part1 = 0
    ans_part2 = 0
    for line in read_lines(input_path):
        line_splitted = line.split(' ')
        target_str, buttons_list, joltage = line_splitted[0], line_splitted[1:-1], line_splitted[-1] 
        
        target_bools = list(map(lambda l: l == '#', target_str[1:-1]))
        target_light = BitArray(len(target_bools))
        for i, val in enumerate(target_bools):
            target_light.set(i, val)

        buttons_list = list(map(lambda L: list(map(int, L[1:-1].split(','))), buttons_list))
        joltage_target = list(map(int, joltage[1:-1].split(',')))
        start_state = BitArray(len(target_bools))
        bfs = collections.deque([(start_state, [])])
        seen = {start_state}
        
        step = 0
        
        if start_state == target_light:
            ans_part1 += 0
            continue
        # logs = []
        found = False
        while not found:
            step += 1
            # logs.append(bfs.copy())
            # if step > 3:
            #     print(f"{line}: Too many steps")
            #     [print(l) for l in logs]
            #     break
            
            size_bfs = len(bfs)
            for _ in range(size_bfs) :
                state, path = bfs.popleft()
                for button in buttons_list:
                    new_state = state.copy()
                    for i in button:
                        new_state.toggle(i)
                    
                    if new_state == target_light:
                        found = True
                        break
                    
                    if new_state not in seen:
                        seen.add(new_state)
                        bfs.append((new_state, path + [button]))
                if found:
                    break
            
        ans_part1 += step
    
        # Part 2: solve A * x = T and minimize sum(x_i)
        # A = joltage effect matrix
        # x = button press counts
        # T = joltage target
        
        solver = z3.Optimize()
        button_press_counts = [z3.Int(f"b_{i}") for i in range(len(buttons_list))]
        
        for b_count in button_press_counts:
            solver.add(b_count >= 0)
        
        num_joltage_counters = len(joltage_target)
        for j in range(num_joltage_counters):
            effect_sum = 0
            for btn_idx, btn_indices in enumerate(buttons_list):
                if j in btn_indices:
                     effect_sum += button_press_counts[btn_idx]
            
            solver.add(effect_sum == joltage_target[j])
            
        total_presses = z3.Sum(button_press_counts)
        solver.minimize(total_presses)
        
        if solver.check() == z3.sat:
            model = solver.model()
            moves = sum(model[b].as_long() for b in button_press_counts)
            ans_part2 += moves
        else:
            print(f"No solution found for line {line_cpt}")


    if is_part1:
        return ans_part1
    
    else :
        return ans_part2
    

if __name__ == "__main__":

    shouldBeEqual(solve, {"is_part1": True, "fileName": 'test_input.txt'}, 7)
    shouldBeEqual(solve, {"is_part1": True, "fileName": 'real_input.txt'}, 457)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'test_input.txt'}, 33)
    shouldBeEqual(solve, {"is_part1": False, "fileName": 'real_input.txt'}, 17576)  
