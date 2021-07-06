# HAHA 2021

## About

Data used in the 2021 edition of HAHA. The corpus is a CSV file that contains the following columns:

- **id** - Unique identifier for the tweet.
- **text** - Text of the tweet.
- **is_humor** - Binary value (0 or 1) indicating if the tweet is humorous or not.
- **votes_no**, votes_1...votes_5 - Number of votes received for not humorous, or for the ratings 1 to 5.
- **humor_rating** - Real value (between 1 and 5) representing the average score the annotators gave to the tweet (NULL if the tweet was not considered humorous).
- **humor_mechanism** - Label for humor mechanism. Only a subset of the tweets have the humor mechanism annotated, and there is only one label per tweet.
- **humor_target** - Zero or more labels for humor target, separated by ";". All the tweets that have humor mechanism, were also annotated for humor targets.

### Humor mechanism

Each tweet that has been annotated for humor mechanism contains exactly one label. The possible labels are:

- **absurd** - Humor comes from a logic inconsistency within the reasoning.
- **analogy** - It is a comparison between dissimilar elements with comedic effect.
- **embarrassment** - In the punchline one of the participants ashames or embarrasses another one.
- **exaggeration** - There is a situation or comparison that is exaggerated.
- **insults** - There are insults to the characters in the joke or to real life people.
- **irony** - They say something but mean the opposite, or they describe a contradictory situation.
- **misunderstanding** - Humor comes from a participant understanding a question or a situation wrong.
- **parody** - The text is similar to another known text or work (for example a song, a saying, or a movie dialog) but it's modified to make it humorous.
- **reference** - It describes a real life situation, generally mundane, that the reader might feel identified with or not, but when the reader feels identified with the situation it results in a humorous effect.
- **stereotype** - Humor comes from using a social group, etchniticy or profession to remark a stereotypical characteristic.
- **unmasking** - Humor comes from a character acting in a way and at some time they show their intentions or characteristics were different than initially thought.
- **wordplay** - They use word ambiguity, made up words or combinations of words to give a humorous sense.

### Humor target

Each tweet that has been annotated for humor mechanism has also been annotated for humor target, and can contain zero or more target labels. The possible labels are the following:

- age
- body shaming
- ethnicity/origin
- family/relationships
- health
- lgbt
- men
- professions
- religion
- self-deprecating
- sexual aggressors
- social status
- substance use
- technology
- women

The tweets can have zero or more labels. Multiple labels are allowed, and in this case they are separated by ";". For example: body shaming; family/relationships

## Overview paper: Coming soon
