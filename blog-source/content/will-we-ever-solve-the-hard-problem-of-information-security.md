Title: Will we ever solve the hard problem of information security?
Date: 2017-01-13
Slug: will-we-ever-solve-the-hard-problem-of-information-security
Category: Security and Cryptography
Image: images/doors.jpg
Status: published

The sad reality of today is that all the programs we rely on are vulnerable to
some sort of attack. A good chunk of computer science academia is trying its
best to figure out what we need to do to to be able to write secure programs. On
top of that, there's an industry full of companies building products and
services to help deal with broken code. Despite all of this effort, clever
hackers still find mistakes in our code and ways to get around our defenses.

A lot of us in the industry (myself included) feel like we are waiting for some
kind of technical innovation or scientific revolution that will finally make it
cheap and easy to write correct programs. As soon as we make the discovery, the
technical aspect of hacking will no longer be a problem, and we'll be left only
with the human aspects of security (social engineering, phishing, etc.). Some of
us even optimistically think we'll find technical solutions to those problems,
too. But are the breakthroughs we hope for possible, or are we stuck with the
status quo forever?

Two visions of the future
-------------------------

![Two visions of the future]({filename}/images/dartboard/visions.jpg)

I have two extreme visions of the future, and there's a spectrum of possible
futures that lie in between the two. The first vision is that our dream comes
true: we discover some algorithm or prove some theorem that makes security easy.
We finally "figure out" how to write correct code, and after we rebuild all of
our systems to work within the new framework, we won't have these problems
anymore.

The second vision is that our dream is fundamentally impossible in the sense
that there are provable mathematically-rigorous limitations on our abilities to
write secure programs. The worst outcome might be that, for the kinds of things
we want to use computers for, "secure" programs simply don't exist (a
mathematical possibility). Less worse, the concrete computational complexity of
writing secure programs might be astronomical.

Reality lies somewhere in between these two extremes.

We certainly *hope* that we live in the first kind of world. Indeed, most
defensive security research, like attempts to automatically make insecure
programs secure (antivirus, ASLR, return-oriented programming defenses, etc.)
seem to presuppose that we live in the first kind of world. If we just keep
trying, we'll eventually find a way. But maybe these attempts are futile. Maybe
we fundamentally *can't* solve our problems, and by necessity, the arms race
between attacker and defender will turn out to be perpetual.

Despite our hopes, our collective experience seems to suggest we're more likely
to be living in the second kind of world. Maybe we can *prove* that we live in
the second kind of world. Such a proof would be extremely valuable, because we
could use it rule out approaches to securing ourselves that are fundamentally
unsound. What would the proof look like?

The obvious place to start is with computability theory. It's undecidable
whether an arbitrary computer program is correct. It's undecidable whether an
arbitrary computer program contains a vulnerability, even for very narrow
definitions of vulnerability. So, following this reasoning, should we conclude
that we're in the second kind of world and just give up? No! Just look at how
much value we get from using computer programs even though we're not *certain*
they're correct. The fact that Excel has bugs in some of its macro functions
doesn't mean companies can't make effective use of it to calculate their
employees' payroll. To get around the undecidability barrier, we need to look at
the problem differently.

A caricature of the software development industry
-------------------------------------------------

Let's draw a caricature of how the software development industry works. As every
student learns in their "Introduction to Software Engineering" course, there are
different people involved in the process of developing a computer program. They
sometimes go by different names, but we'll call them,

1. The *users*, who have a real-world problem to solve and want a program to
   help them,

2. The *developers*, who write the code to implement the program,

3. The *testers*, who try to find the mistakes in the program before the users
   run into them.

We can "pseudomathematically" model the situation like this:

1. The users provide a description of some functionality, *F*, that they want.
   It's often never made explicit, but the users also have some security
   requirements, *S*, in mind.

2. There's a randomized algorithm *D*, corresponding to the software developers,
   that takes the desired functionality *F* and the security requirements *S* as
   input and spits out a program *D(F, S)* that supposedly satisfies both
   requirements.

3. There's another randomized algorithm *Q*, corresponding to the quality
   assurance testers, which takes *F*, *S*, and a program as input, and decides
   whether the program really satisfies *F* and *S*. As soon as *Q(F, S, D(F,
   S))* accepts, the program *D(F, S)* is deemed ready for production use.

The users want a program *p* for which *F(p)* is true and *S(p)* is true, but
what they *actually* get is a program *p* for which *Q(F, S, p)* is true. If *Q*
isn't good at checking *F* and *S*, then there's a good chance they're not
getting what they want. Even today we often conflate *Q(F, S, p)* with *F(p)*
and *S(p)* actually being true, i.e. we use programs *as if* they are correct
and secure, even though we know they probably aren't... at least we're taught
otherwise by getting hacked.

*F* and *S* are intuitive fuzzy concepts. The whole difficulty of programming is
turning the fuzzy *F* into a formal, concrete, highly-specific set of rules to
implement something that's "*F* enough" to satisfy the users. Same for *S*,
nobody's ever written out a complete formal definition of "security." We just
have to hope that everyone's intuitions about the problem, shared through the
English language (or whichever language you speak), ends up being good enough.

Let's think of the developers as darts players, and let's lay out the space of
all possible programs on a dartboard. Upon seeing *F*, the developers will
choose a particular approach to solving the problem. They will pick a language
to write the program in, draw up a design for the internals of the program,
select the algorithms they're going to use, and so on. The chosen design space
will be our dartboard. Behind the dartboard there's a backboard (full of
nonsensical programs) to protect the wall from errant darts, but the developers'
darts almost always land inside the circle:

![Dartboard]({filename}/images/dartboard/dartboard-1.png)

 The bull's eye of the dartboard contains the programs that are really
correct and secure according to *F* and *S*:

![Dartboard]({filename}/images/dartboard/dartboard-2.png)

The region around the bull's eye is partitioned into into three areas:

1. Programs that implement the correct functionality but aren't secure (bugs
   that only crop up under adversarial conditions),

2. Programs that are secure but implement the wrong functionality (benign bugs),
   and,

3. Programs that are neither secure nor implement the correct functionality.

![Dartboard]({filename}/images/dartboard/dartboard-3.png)

Containing the bull's eye is the "circle of acceptance", which are all the
programs that will pass QA's test and be deemed ready for production use. Of
course, QA isn't perfect, so some incorrect and insecure programs slip in:

![Dartboard]({filename}/images/dartboard/dartboard-4.png)

The act of software development consists of throwing a dart at the board, trying
to hit the bull's eye. We're not *terrible* darts players, so programs near the
bull's eye (almost-secure and almost-correct programs) are more likely than ones
far away from it. The probability distribution over where the dart lands might
look something like this:

![fat probability distribution]({filename}/images/dartboard/distribution-1.png)

Today, most of our darts miss the bull's eye. What can we do to make more of our
darts land in the bull's eye?

How do we improve?
-------------------

The first step is to make sure that there really *is* a bull's eye. Humans are
excellent at holding on to contradictory ideas without ever realizing they're in
conflict. Quite often, our intuitive *F*'s and *S*'s contradict each other but
we don't realize it. For example, "a super-optimized processor that makes the
most efficient use of its time and energy" satisfying the security requirement
"processes must be isolated from one another" is flatly contradictory, but
decades after the invention of the microprocessor, we're only just now realizing
it thanks to side-channel attack research.

Once we're sure that there is a bull's eye, we want to make it as big as
possible relative to the dartboard. The more dartboard the bull's eye
encompasses, the more likely the dart throwers are to hit it on their first try.
If we zoom out and look at the entire backboard, we'll find other dartboards
corresponding to different design decisions. For example, one approach is to use
the PHP language and `mysql_real_escape_string()` to escape data for insertion
into SQL queries, and another approach is to use prepared statements in the Rust
language. The latter's bull's eye will be easier to hit. There are lots of
different design spaces and each one has a different sized bull's eye:

![Dartboard]({filename}/images/dartboard/dartboard-5.png)

The problem with making the bull's eye bigger is that every developer has
a comfort zone. They're better at working in some design spaces over others. It
costs money to transform a PHP expert into a Rust expert, and it can't happen
overnight. So *how* we make the bull's eye bigger has to be in line with our
economic reality.

We want the circle of acceptance to hug the bull's eye tight. Making the bull's
eye bigger helps with that, because it's sandwiched between the bull's eye and
the edge of the dartboard. We tighten the circle of acceptance itself by
becoming more skeptical and deeming fewer programs as production-ready. For
example, we might accept only formally verified programs, exiling all error to
mistakes in translating the intuitive *F* and *S* into formal statements. But
formal verification is expensive; the way we constrict the circle of acceptance
needs to be in line with economic reality, too.

We can try to be better dart throwers. Maybe, through better education and
aligning of economic incentives, we can produce developers that can hit those
tiny bull's eyes and businesses that are willing to pay the price for secure
software. My prediction is that we're unlikely to see technological
breakthroughs here. We'd need to see massive advances in cognitive science to
have any hope of teaching someone how to program in C++ without also making them
ultra-likely to write programs with memory corruption vulnerabilities. Becoming
better dart throwers boils down to recognizing when the bull's eye we're going
for is small and investing massive amounts of time and money into making sure it
gets hit:

![skinny probability distribution]({filename}/images/dartboard/distribution-2.png)

The last way we can get better is a bit of a cheat: change the problem. We can
talk to the users and convince them that their *F* and *S* are too hard, and if
they could only be happy with the different *F'* and *S'* then we could actually
give them what they want. Alas, this won't be possible in general. We use
computers because of the value they provide, and we can't just rearrange the way
our whole society works so that the problems we to solve are easy to program.

Now that we have a nice picture in our minds, let's return to the question of
whether or not we should expect to see some kind of holy grail security
breakthrough in the future.

So, which world do we live in?
------------------------------

The darts analogy tells us what questions we need to answer. Ultimately, we want
to know whether there is a dartboard (a design space) with a bull's eye big
enough for us to hit every time. The three questions we need answers to are:

1. **The human developer probability distribution question:** What is the
   probability distribution over the outcomes of *D(F, S)* when *F* and *S* are
   real-world intuitive functionality and security requirements and *D* is
   a team of human programmers?

2. **The technologically-expanding bull's eye question:** How large, relative to
   the design space, can we make the set of functional and secure programs, by
   way of changing our choice of design space? Remember that the design spaces
   we choose need to be economically feasible.

3. **The technologically-constricting circle of acceptance question:** How
   tightly can we make the circle of acceptance hug the bull's eye, by way of
   improving our quality assurance technology? Remember that our QA technology
   needs to be economically feasible, too.

It's easy to find research towards answering the latter two questions, and it's
harder to find research towards answering the first. That's not really
surprising, given that the first question goes beyond pure math and involves
human subjects. If you've done any security research, I encourage you to take
a moment and think about which of the above questions your research has helped
to answer.

We optimistically hope that we live in a world like the first kind, where
a breakthrough will fix all of our security problems. But that's only the case
if all of the above questions have a favorable answer. We try our best to force
favorable answers, but perhaps we've been too optimistic. My personal opinion is
that we need to try harder to supply unfavorable answers. Without an
understanding of our limitations, it might be like we're all running on
treadmills without realizing it. We think we're making progress towards
a breakthrough without realizing we're going nowhere. I want us to look for
unfavorable answers to the three questions.

As an example, and to clarify what I'm advocating for, the research I'm
imagining would try to prove something like a "typo theorem." A typo theorem
would say...

> *In all known Turing-complete programming languages, all secure programs
> implementing functionality F are a "typo" (small source code change) away from
> being insecure.*

In principle, someone could write down a formal version of this typo theorem and
take a shot at proving it. Who knows, it might even be true!

We should move forward with optimism, hoping that one day things will get
better. But we should not have *blind optimistic faith*. For all the effort we
put into making things better, we should be putting at least half as much into
showing that we fundamentally can't. We need to go beyond breaking individual
defense mechanisms and show that *all* defenses of certain kinds will fail. By
doing this, we'll get a much better appreciation for the hard problems we're up
against, and it's the only way we'll ever stop putting forward "solutions" that
don't really help.

*I'm curious, what do you think?* Are you holding out hope for big
breakthroughs? Or do you think that the status quo is pretty much it, modulo
minor improvements? You can leave a comment below.
