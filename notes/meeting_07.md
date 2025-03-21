# Meeting 7

We demo the automation test-setup we created.

You are not feeding into the code. 

Try to see how it works on a real repo.
- See what comes out, and if you get real errors.
Third file:
- If exists, provide the pairwise comments if for same code.

Categories the semantic. Use these to filter out waht is "good enough". Use the automatic semantic analysis to categories "this is fine", "this is a mess" and "this is somewhere in the middle". 
Then you can probe into these categories to make sure that is.

Then you can say for the good category that "here it is usefull"

Then for the bad you can investigate.

You can say stuff like "for this code" all of these are 20% score. Then you probe this, it fits. And then you can say stuff like "we therefore say here it concludes we assume it does nice." We did so and so many commits, and then we can say xx% fits.

We can use it to flag for review of human. If it is a bad score, then maybe look.

By using the comparison, you can come up with another system to create a confidence score for the comment. 


You need to find ways to build trust in the fact that it builds usefull things.

Good to do automatic scoring so you can work on large amounts.
- But also need to do manual on this to ensure that you can count on the score.

You would be able to end thesis like:
"Here we can see that with a it of tinkering we got 70% percent of comments close to the meaning of a human, and we did a system to do trustworthyness score. We see a correlation between the trustworthyness and the semantic, and therefore we see confidence in the direction that this is something that could be implemented in the software lifecycle.

The interesting part is to be able to test your blackbox so you can open up the talk about how it could be committed into a lifecycle.

## Interview with CGI developer
Its an add-on that we could avoid. It would be an interesting conversation for a conceptual way of view, but not necessary for our thesis.

Better than interview, is to make this system with trustworthyness that analysis on 1000 commits and say we get 70%. This is if we get semantic comparison to work.
- Otherway interview is interesting.


# Opsummering
## Semantic analysis
hvis vi kan få det til at virke, skal vi ikke kun have en score, men også validere den.
det kan gøres ved at indentificere nogle kategorier fx.
- good
- medium
- bullshit
  
Vi validere ved at tage stikprøver af commentarere der lande inde for en af kategorierne, og vurdere om de passer ind i kategorien.

Det gør at vi bruge store data til at beskirve kvaliteten af produktet.

## Validation score
Som en fed feature skulle agenten, baseret på vores analyser, kunne score sine egne kommentare, og levere den score med i sin pull request, så udviklere ikke behøver at forholde sig til kommentarene, med mindre de er under en vis score.

## Interview
Hvis vi får semantic analyse til at virke, så kan interviewet bruges til at validere hvorvidt vores produkt har sin gang i industrien

Hvis ikke vi for semantisk analyse til at virke, så kan det være at vi skal bruge interviewet til at validere productets funktion.

# Roadmap:

- semantisk analyse
- Få styr på eksisterende litteratur
- Lav produktet færdigt
    - map litteratur til vores test score
- add on/ diskuter - trust score
- bench marking



Til paolo!
- Når vi bruger 3rd party libraries, hvordan håndtere vi det i vores akademiske projekt
- Skal vi beskrive dem? Hvor meget? Skal vi være skeptiske, vurdere deres brug osv.