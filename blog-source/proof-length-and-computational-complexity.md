Title: The Connection Between Logic, Math, and Computation
Date: 2016-11-05
Slug: short-proofs-and-computational-complexity
Category: Computer Science
Status: draft

1. If you equate "in a language" with theoremhood and "not in a language" with
   non-theoremhood, then computation (transcript of decider TM) is exactly
   proofs. Undecidable languages have theorems without proofs (and nontheorems
   without disproofs). Can we state Godel's incompleteness theorem this way?
    (theorems are semi-decidable, if it's complete then fully decidable)

        Ah... no, nontheoremhood (always false) is that the thing with the not
        symbol in front of it is in the language.

        completeness is for all WFF x, either x in L or not(x) in L.
        consistency is there is no WFF x such that x in L and not(x) in L.
        If we can talk about turing machines then "M halts" has a proof or
        disproof which we could find in finite time by brute forcing.
        Thus if the system is complete, consistent, and sound (we need soundness in order for "M halts has
        a proof" to imply "M halts"), then it can't be powerful enough to talk
        about Turing machines.

        Informally, a soundness theorem for a deductive system expresses that
        all provable sentences are true.

1. We're interested in "short" and "efficiently verifiable" proofs which gives
   us NP.
