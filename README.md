# mlh-hackathon


Ths project is meant to help people dive deep into the world of CV.

What our project does is lessen the amount of effort it takes to add motion controls to their game projects.

We have built two seperate things.

We have built a client that allows for the easy plugin of existing PYGAME projects. You simply need to add a game into the right place, and our client is going to be
be able to add the game into the list of existing games. This makes it easier to manage all of your games, and keeps them all in one place. Instead of
having to run pygame files from command line, you can just run our launcher, and it'll help initialize all the games from it.

The second part is adding logic that allows a webcam to capture a user's hands. Using openCV, it takes note of the position of the user's hands. If it sees that the
player's hands are oriented in a certain way, then it sends that to the backend logic of our program. The backend then checks the positions against a database
of positions. If it matches a predefined position, then it uses pycontroller to simulate keyboard input using that position. This allows users to easily add motion
controls, as they have a list of pre-defined positions that they simply need to select from. If however, a user wants to add their own positions/movements, that is also
relatively easy to do. The user simply has to push their positions to the database, and then import those positions into our checker. It's quite simple and quick
and allows for minimal effort from our end user. They can focus on the game development cycle, and less about how to implement motion controls. We believe
that this is how game development should be approached. It's less about a developer questioning the ability to execute what idea they have in their head because
they feel that they don't have a deep understanding of the tech needed to implement said ideas. 


In order to run our program install the requirements.txt. Then execute the mainlogic.py file.


Once in the program, there are three options. You can go to the prebundled game, which is tetris, you can go to the testing screen, or you can exit the program.




The testing screen is where a user can see whether or not their gestures pass the gesture test. They can run tests against their gestures to see whether or not they
pass the test. This is a great way to speed up development to see if there are any kinks in the product. In the checker.py file, where the test lives, you can see
the tests objects. This is for displaying the results of the tests on the screen. Change the object in order to see the results of different tests. The actual logic for the tests are handled elsewhere, in the hand_signs.py file.


In hand_signs.py you can find the test_for_gestures method. Here you need to simply apply the geometric tests to pass in order to verify that a hand gesture has been
made. In this V1, we have not added the full database of different gestures, but we have a few defaults packed in. Edit them with your geometric positions, and that is all.


Loading in a game is quite simple too. In V1, he have hard coded the actions into the tetris file, but in V2, we plan to have the hand gestures as an abstracted layer over the game object, making it even easier to sideload games. Simply drop your project into a folder, change where the menu_objects points to (it's the last line).


In order to add motion controls to your game, all you need to do is add our boilerplate code to the game, in the main execution loop. 










