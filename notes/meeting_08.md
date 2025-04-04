# Meeting 8
- Når vi bruger 3rd party libraries, hvordan håndtere vi det i vores akademiske projekt
- Skal vi beskrive dem? Hvor meget? Skal vi være skeptiske, vurdere deres brug osv.
- Kan papers blive "for gamle" når det handler om ting som dokumentations principper?
- Og er preliminary/ conference papers gode nok?
## Litteratur
- looking at why we have chosen to make an automated system, and what that actually means, we have looked at this paper: https://ieeexplore.ieee.org/abstract/document/5387726
    - takeaways:
    - "automation is seen as a practical approach to increasing productivity and quality."
    - We want to use this to show how our approach differs from the more popular approach of integrating documentation assistance in IDEs, like co-pilot, and why this is not an automated workflow.
- https://link.springer.com/chapter/10.1007/978-3-319-19243-7_10
    - This is a preliminary articel, but it has some good points to reference in our intro:
    - source 8 from 1983: "Lacking and outdated documentation is one of the main causes of the high cost of software maintenance"
    - source 6 from 2007: After anayzing three opensource, they conclude that new code is not commented.
## Content
- Background and related work overview.
- our methode:
    - experiment
    - explain our incremental data driven approach, how detailed?

## Notes from meeting
- 3rd party. Always good to have a sound rational for why you do something. Don't write if you don't know. But always good to have a sentence for the why. Not all libraries, but just explain for what is relevant for our project. Langchain f.eks. would probably be good to explain. 

- If the paper has relevance for our project, there is no aging. 
- If you cite any paper, then it means that it is fair game that you should have an understanding of what is discussed in there. They will ask at the exam, and it would be bad if you simple could answer "i dont remmeber". -> Dont Cite stuff just to have stuff to cite.

- Not problem with preliminary, but you can see if there is a follow up paper released. And just present it as what it is, a preliminary study with preliminary findings. 
  - Check what she has published afterwards. -> Paolo says it probably is a phd student. Look into Hadar

### Background and related work
- You should always have a related work section, no matter what.
- Background you can decide.

Related work:
  - People who have done related to yours. Who worked with automating documentation. Or similar.
  - Survey showing that documentation is usable.
  - Your job with this is for example look at other papers who have looked at llm for documentation, and then explain how we allign with that or build upon that.

Background:
- Knowledge that the reader of our thesis need to know to understand our thesis.
  - E.g. maybe the levels of documentation that we need in our thesis. If there is a paper that have described the categorisation that we use then this would be background.
  - Knowledge about LLM and agents is background. Not motivate. -> Motivation is not background. Background is "what is a LLM agent". The "why use an llm agent" that is in another section .-> Probably design section.

In design section you can say stuff like "following the process described here" we have embedded the LLM in our agent.

Should we include steps, or just end product.

Building a toolbox for working with psycological safety. -> Look at this for structure.
- Different cycles. 
E.g.
- Proof of concept
- Then embed
- Evaluating


So look at the project we have done, not just a product. 


