# Slackbucket

Slackbucket is a bot that is the spiritual successor of bukket, our beloved chat bot. 

## Usage

```
/path/to/slackbucket $ python bucket.py -c /path/to/config.yaml
```

##  Goals

- Our own maintainable bucket codebase.
- A functional bot that's easy to contribute and add functionality to
- Something that could potentially cross multiple communication mediums (slack, discord, irc)
- A project that's just for fun


## Non-goals

- A can-do-everything bot
- Something that will do code deployments for you

## Architectural Concepts

The idea behind this version of bucket is to make it ultra extensible. In fact, given the primary goal, every single thing that slackbucket can do should be done through a plugin-type architecture, including most core functionality.

Slackbucket's core will handle a few basic situations: calling procedures pre-start, post-start, and same for shutdown; determining if slackbucket is being commanded or if something should be a trigger.
