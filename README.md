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






