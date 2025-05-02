# Choice of LLM

- Just say that you started with this specific LLM without reasoning. Then during validation say you compared to other. → Keep it short.
- In discussion, do something like “what about other LLM”, and then say that qualitatively say that we could see that these could not do correct format.

# How to handle support for multiple languages

- Write that you had the notion about writing modular product. Similar to above, “what about other languages” section. This is just a proof of concept, refer to how you could do to let it implement more languages.

# How to get around using ChatGpt

- Put a disclaimer in methodology.

# The report

- Size → See guidelines
    - Paolo says use as indication, he doesn’t really care. not 200, not 5, but he cares more about the: “have you said what you want to say?”, “do you have more to say”
    - Usually less is harder, so dont feel constrained. → But also dont try to write bullshit to fill out.

# The exam

- Format is up to us.
    - Usually. Come in, joined presentation → And then get examined at the same time. They will make sure to direct questions to the individual.
- We tell him what format we want.
- Presentation, 10-15 minutes.
    - Show off, show something interesting about your thesis you want to show or talk about.
    - Dont skip on the why, the research question. The presentation should be able to stand alone.
    - Show a demo of your prototype please → Very potent
        - Often paolo is connected, and you can join with zoom and share your screen.
- Questions → What ever you write is open for questions.
    - If you write ci/cd or automation. Its good to understand what that is, why, and the higher level.
- Any paper used, they can ask “what is this paper about”. → If it is a big part of project, you need to know very well, if its little use, at least just know what its about and what it gives.
- A more ambitous question could be:
    - Semantic score: You used this technique, did you concider alternatives.
    - General at the end: “How do you see this going forward” “how do you see this emmbedded”.

# Using agent architecture

Where you write that you use the method from paper x → just write a line like “we chose to use the phrase phase instead of module, as it fits better with our project”. 

# Question regarding agency

An autonomous agent is a system situated within and a part of an environment that senses that
environment and acts on it, over time, in pursuit of its own agenda and so as to effect what it
senses in the future.

Ikke alle aktions er autonomous agenter → Aktions giver muligheden for at sence environmentent. Men hvis de ikke selv påvirker environmentet, så er det ikke en autonomous agent.

- Noget som generer en report, eller et lille info check. Linters and so on, er ikke aktions.

- No other entity is required to feed it input, or to interpret and use its
output.
    - Is our agent then first an agent with the use of the github runner, because that is what enables it to sense and get “triggered” by environment?
    - And can it still be an agent when we decide to keep the human in the loop with the pull request?
- Each acts so that its current actions may effect its later
sensing, that is its actions effect its environment
    - But not without human interaction in our case
- Finally, each acts continually over some period
of time. A software agent, once invoked, typically runs until it decides not to. An artificial life
agent often runs until it's eaten or otherwise dies.
    - We have a simple agent - our planing module is quiet concise and since it is a repeated job, the plan does not change - but because our time restrcition we do not have implemented reflection of the generated output, which could have lead to more decition.
    - Is it very little agent like, that our agent starts, does work, dies? Or could we just say that is when it decides to die.
