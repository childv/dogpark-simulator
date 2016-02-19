Rachel Moore and Veronica Child
CS 111, Andy Exley
6/7/15
readme.txt

Concept:
Our program is a dog park simulation; the goal is to keep the park running for 4 minutes.
The game begins with 4 dogs that move and interact with each other. A dog will leave
when their energy is below zero; to give them energy, click the "FEED DOGS" button
and bones will randomly appear. When a dog collides with a bone, they will gain energy
and the bone will disappear. Dog will poop every 25 seconds; the user may clean up
the poop by clicking on it. If the number of poop present is twice as much as the number
of dogs, the game will end. The user may add dogs by clicking the "ADD DOG" button.
Note that the 'ADD DOG' button refreshes every 10 seconds, so the user can only add dogs
in 10 second intervals.

Objects (Classes):
The dog object has several different types of movement; the random "__move" function, the
"play" function, and movement when they're next to the edge of the screen or a tree
(the "move_tree" function) to avoid getting stuck. You may get the dog's
current mood, energy, and name by clicking on them. The dog's energy determines their
mood, movement (the dogs stop moving below 3) and whether they leave the park (below 0).
The dogs lose energy when they are close enough to another dog to play and, by default,
every 25 seconds. They gain energy when they interact with a bone. The dogs randomly
move within the dog park.

The tree object gets the tree image and draws the tree in the specified location. It is
meant to be static.

The poop object is created every 25 seconds next to each dog and disappears when
the user clicks on it.

The bone object is created when the user clicks "FEED DOG" on the display. They appear
in random positions and disappear when dogs collide with them.

The bark object is created when two dogs are playing and displays "RUFF" on the screen
above each dog.

The start screen and end screen are called in the main function. The start screen
explains the basic idea of the game at the beginning, and the end screen is called
either after 4 minutes or if there is too much poop or too few dogs remain.

The status screen is called whenever a dog is clicked. It gives the name, energy, mood
and image of the dog.

Main Function:
The main function initializes the start screen, draws all the objects, keeps track of
all the events, keeps track of all the collisions and calls the appropriate methods when
each object collides. 

Bugs:
One of the main problems is having our dogs get stuck when playing with another dog or
when colliding with a tree. For this reason, we have functions within the dog class,
such as "collide_tree" and "move_tree", that determine whether a dog is stuck by
counting the number of times a dog has successively collided with a particular tree and
then move them away. While this method has worked, dogs will occasionally become stuck.
An added dog may also get stuck when, while trying to move into the dog park from
the portal, encounter another nearby dog and begin to play, the added dog may get stuck
in the portal. Nevertheless, the program will continue to run, and there is a chance
that the dogs may unstick themselves after 30 seconds or so.
