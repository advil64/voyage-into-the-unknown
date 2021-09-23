# Voyage Into the Unknown
### Advith Chegu & Naveenan Yogeswaran

**Question 1**: Why does re-planning only occur when blocks are discovered on the current path? Why not whenever knowledge of the environment is updated?

**Answer**: Because A* finds the optimal path, it shouldn't matter if there are any obstacles that are not in the path as we will continue on our current path. It would be a waste of time to re-plan every time there's an update in the environment as planning takes at best $O(n)$ each time and if there are at most $n$ blocked nodes, we can see that this situation would quickly rise to exponential time. 

**Question 2**: Will the agent ever get stuck in a solvable maze? Why or why not?

**Answer**: The only time the agent gets stuck in a maze is when its neighbors are arranged in a way that it is blocked from progressing even if it back tracks. Let's take an example of an unsolvable maze:

```
[0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 1, 1, 0, 1, 1]
[1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
[1, 1, 0, 1, 1, 0, 0, 0, 1, 0]
[1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
[1, 1, 0, 1, 1, 0, 1, 1, 1, 0]
[0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
[1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
```

We clearly see that the above maze is not solvable because once the agent takes a step to the right, there is no additional step to take other than back to the start and once it back tracks there is no way to move forward. Now lets see an example of a solvable maze:

```
[0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
[1, 0, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
```

Once we run repeated A* we find the following path:

```
[2, 1, 0, 0, 0, 0, 0, 0, 0, 1]
[2, 2, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 2, 1, 0, 0, 1, 1, 0, 0, 1]
[1, 2, 1, 0, 0, 0, 0, 0, 0, 1]
[0, 2, 2, 2, 2, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 2, 2, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 2, 1, 0, 0, 0]
[1, 0, 0, 0, 0, 2, 2, 2, 0, 0]
[1, 0, 0, 0, 0, 0, 0, 2, 1, 0]
[0, 0, 0, 0, 0, 1, 0, 2, 2, 2]
```

Now although the agent had to recalculate **4** times due to obstacles in its original path, our agent is always going to move backwards and find a different path each time. We do this by first checking if the current path is blocked and returning the section before the blocked node.

```python
if complete_grid.gridworld[curr[0]][curr[1]] == 1:
    # update our knowledge of blocked nodes
    discovered_grid.update_grid_obstacle(curr)
    # remove the path starting with the blocked node
    path = path[:index]
    return path
```

Then we go back and create a new path (avoiding the visited neighbor nodes) using repeated A*.

```python
last_node = new_path.pop()
last_unblock = last_node.curr_block
# append the rest to the final path
final_path.extend(new_path)
# check if the path made it to the goal node
if last_unblock == (dim-1, dim-1):
    final_path.append(last_node)
    break
# create a new path from the last unblocked node
new_path = path_planner(last_unblock, discovered_grid, dim, euclidian)
```

By using this smart method of backtracking in the case of a blockage in the path, we can avoid getting stuck in a solvable maze as we can always move back node by node to check if there are any unvisited paths that were missed in the first go around.