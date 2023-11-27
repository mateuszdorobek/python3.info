Dragon Sprint 6
===============
* Assignment: Dragon Sprint 6
* Complexity: medium
* Time: 34 min


Functional Requirements
-----------------------
1. Add statuses that are updated based on life:

     a. "Full Health" - when health points are 100%
     b. "Injured" - when life points are 99% - 75%
     c. "Badly Wounded" - when health points are 74% - 25%
     d. "Near Death" - when health points are 24% - 1%
     e. "Dead" - when life points are below or equal to 0%

2. Add textures that update based on life:

     a. Alive texture: ``img/dragon/alive.png``
     b. dead texture: ``img/dragon/dead.png``

3. When your hit points drop to or below zero:

     a. no more damage can be dealt to the creature
     b. the creature cannot deal damage
     c. the creature cannot move

Use Case
--------
1. Create dragon with name "Wawelski"
2. Set Dragon's initial position to x=50, y=100
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
* :download:`Solution <assignments/dragon_sprint_6.py>`
