# Meeting w Paolo Wednesday 2. April
## Agenda
- demo of semantic score
- DocTide
    - is it appropriate to have a name for the product, for clarity reasons?
- How are we doing in the process
    - Our test setup framework is done - It works with public repo like flask
    - we believe to have the source for the background and related work sections
    - Should we have research questions?
- Next steps
    - Improve on the LLM agent
        - deployment
        - Naive approach not working: context window limits -> Abstract syntax tree

## Notes from the meeting
Do baseline based on your own. -> Make labels.
- Lav stikprøver -> Manual labeling. Vi laver stikprøver og vurderer hvor grænsen går for godt, dårligt og middel.

Name -> Its your thing. Do whatever you want.

Paolo asks -> "What are you trying to test"
- We want to assess the skill of creating comments, and compare to commits that does not have comments.
- You need to target these commits.

Paolo suggests -> Step back, look at research question. What step do you need to do to be able to say that doctide works great.
- Break it down into steps like
  - Does the comments fit with what is written by humans.
  - Does it work/ scale on live repo
  - Maybe -> Is it over eager or under eager? Does it comment the right places. (Lukas thought)
- Main point! -> Break down the tests into atomic parts, where you answer one thing at a time.

Spend time articulating the research questions.

Make sure that the repositories you select is selected with reason.
Important part of thesis.
-> We considere x y z, we picked this because it has better function levels comments and so on.

Paolo thinks we are in a good point.
We have a month and something.

What paolo would do:
- Go backwards from the deadline, and see when we need to be done with things.
- Have thought about research question, and what do we want to build to work towards that.
- Agree on research questions, figure out what we need to do this.

Dont forget -> Priority
- Step back, do planning for future.
- Research questions.

Building blocks allows for -> The steps youd dont finish can be discussed in future work.