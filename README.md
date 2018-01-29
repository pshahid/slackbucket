# Slackbucket

Slackbucket is a bot that is the spiritual successor of bukket, our beloved chat bot. My primary goal (aside from making our own bucket) with this project is to create a codebase where anyone who knows a little bit of Python could contribute new functionality with minimal effort. That means we sacrifice other things (like flexibility), but that should be ok until it's not!

## Architectural Concepts

The idea behind this version of bucket is to make it ultra extensible. In fact, given the primary goal, every single thing that slackbucket can do should be done through a plugin-type architecture, including most core functionality.

Slackbucket's core will handle a few basic situations: calling procedures pre-start, post-start, and same for shutdown; determining if slackbucket is being commanded or if something should be a trigger.
