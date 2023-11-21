Dragon Sprint 5
===============
* Assignment: Dragon Sprint 5
* Complexity: medium
* Time: 34 min


Functional Requirements
-----------------------
1. Add the ability to move in 3 dimensions

     a. Going higher, you add ``z`` (flying)
     b. As you go deeper, you subtract ``z`` (diving)

2. Can't go beyond the screen area:

     a. ``x`` axis from 0 to 1920
     b. ``y`` axis from 0 to 1080
     c. ``z`` axis from -100 to +100

3. If the character reaches the edge of the screen, then by moving further,
    the position will be set to the marginal value in a given axis.
    For example, the dragon is in position ``x=1, y=2`` and moves left at 10
    then after the move it will end in position ``x=0, y=2``.


Use Case
--------
1. Create dragon with name "Wawelski"
2. Set Dragon's initial position to x=50, y=120
3. Set new position to x=10, y=20
4. Get current position
5. Move dragon left by 10 and down by 20
6. Move dragon left by 10 and right by 15
7. Move dragon right by 15 and up by 5
8. Move dragon down by 5
9. Dragon makes damage (random 5-20)
10. Dragon takes 10 damage
11. Dragon takes 20 damage
12. Dragon takes 30 damage
13. Dragon takes 40 damage
14. Dragon takes 50 damage


Non-Functional Requirements
---------------------------
 1. Commit and push the current state of the repository
 2. Modify the game code from the previous version of the task
 3. Save the code to solve the task in the ``dragon`` directory
 4. When finished, add all files from ``dragon`` to the repository
 5. Commit and push changes to a central repository (Github)


Solution
--------
* Note, that this will spoil your fun and learning
* :download:`Solution <assignments/dragon_sprint_5.py>`
