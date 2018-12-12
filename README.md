I implemented the task with Flask framework (Python)

Flask is not very robust however it’s simple, convenient and should be enough for this simple task.

I deployed the app with docker on the 2 ec2 instances you provided. The docker container runs as a daemon in the background. Also , the container will restart if it crashes, or if the system docker is running on is rebooted.

The implementation is quite simple using txt file to save the message passed in the post request. It’s not best practice at all. A better way would be to use AWS SQS service (if I was provided with one) for managing the “communication messages” between the instances. That way it would be scalable.


Now you can send HTTP requests like you described in the instructions.
