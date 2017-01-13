Title: Will we ever solve the hard problem of information security?
Date: 2017-01-12
Slug: will-we-ever-solve-the-hard-problem-of-information-security
Category: Security and Cryptography
Image: images/doors.jpg
Status: draft

The sad reality of today is that all of the programs we rely on are vulnerable
to some sort of attack. A sizable chunk of computer science's academia is trying
its best to figure out how to write secure programs by doing things like
studying formal verification and coming up with return-oriented programming
countermeasures (to name two of the *many* subdisciplines). There's a whole
industry full of companies building products and services to help us deal with
broken code; things like firewalls and antivirus. Despite *all of this effort*,
clever hackers can *still* find mistakes in our code and ways around our
defenses.

A lot of us in the industry (myself included) generally think that we are
waiting for some kind of technical innovation or scientific revolution that will
finally make it cheap and easy to write correct programs. After we make the
discovery, suddenly the technical aspect of hacking won't be a problem, and
we'll be left only with the human aspects of security (social engineering,
phishing, etc.). Others of us think that some great technological solution will
come along and save us from those kinds of attacks, too. Are we being too
optimistic?

Two visions of the future
-------------------------

![Two visions of the future]({filename}/images/dartboard/visions.jpg)

I have two extreme visions of the future, and I imagine a spectrum of possible
futures that lie in between between. The first vision is that our dream comes
true: we discover some algorithm or prove some theorem that makes security easy.
We finally "figure out" how to write correct code, and after we rebuild all of
our systems to work within the new framework, we won't have these problems
anymore. The second vision is that our dream is fundamentally impossible. There
are true, mathematically-rigorous limitations on our ability to write secure
programs. In the worst case, maybe secure and correct programs don't exist at
all, or slightly less worse, the concrete complexity of finding them is
astronomical. Reality must lie somewhere in between these two extremes.

We certainly *hope* that we live in the first kind of world. Indeed, most
defensive security research, like attempts to automatically make insecure
programs secure (ASLR, ROP defenses, etc.) seem to presuppose that we live in
the first kind of world. If we just keep trying, we'll eventually find a way.
But maybe these attempts are futile. Maybe we fundamentally *can't* solve our
problems, and by necessity, the arms race between attacker and defender will
turn out to be perpetual. I think that despite our hopes, our collective
experiences suggest that we're more likely to be living in the second kind of
world.

Maybe we can *prove* that we live in the second kind of world. Such a proof
would be extremely valuable, because we could use it rule out approaches to
securing ourselves that are fundamentally unsound. Let's think a little bit
about what such a proof would look like.

The obvious place to start is with computability theory. It's undecidable
whether an arbitrary computer program is correct. It's undecidable whether an
arbitrary computer program contains a vulnerability, even for very narrow
definitions of vulnerability. So, following this reasoning, should we conclude
that we're in the second kind of world and just give up? No! Just look at how
much value we get from using computer programs even though we aren't *certain*
they're correct. The fact that Excel has bugs in some of its macro functions
doesn't mean companies can't make effective use of it to calculate their
employees' payroll.

Modelling how we write and use programs
----------------------------------------

To make some progress, we need to weaken our formal requirements. To do that,
let's draw a caricature of how the software development industry works. As every
student learns in their Introduction to Software Engineering course, there are
different people involved in the process of creating a computer program:

1. The *users*, who have a real-world problem to solve, and want a program to help
them.

2. The *developers*, who write the code to implement the program.

3. The *testers*, who try to find the mistakes in the program before the users run
into them.

We can take a shot at "pseudomathematically" modelling the situation like this:

1. The users provide a description of some functionality *F*, that they want.
   It's often never made explicit, but the users also have some security
   requirements, *S*, in mind.

2. There's a randomized algorithm *D*, corresponding to the software developers,
   that takes the desired functionality *F* and the security requirements *S* as
   input and spits out a program *D(F, S)* that supposedly satisfies the
   functionality and security requirements.

3. There's another randomized algorithm *Q*, corresponding to the quality
   assurance testers, which takes *F*, *S* and a program as input, and decides
   whether the program really satisfies *F* and *S*. As soon as *Q(F, S, D(F,
   S))* accepts, the program *D(F, S)* is deemed ready for production use.

Notice that the users want a program *p* for which *F(p)* is true and *S(p)* is
true, but what they *actually* get is a program *p* for which *Q(F, S, p)* is
true. If *Q* isn't good at checking *F* and *S*, then there's a good chance
they're not getting what they want. Even today we often conflate *Q(F, S, p)*
accepting with *F(p)* and *S(p)* actually being true, i.e. we use programs *as
if* they are correct and secure, even though we know they probably aren't, until
we learn otherwise by getting hacked.

Notice also that *F* and *S* are intuitive fuzzy concepts. The whole difficulty
of programming is turning the fuzzy *F* into a formal, concrete, highly-specific
set of rules to implement something that's "*F* enough" to satisfy the users.
Same for *S*, nobody has a formal definition of security. We just have to hope
that everyone's intuition about the problem, shared through the English
language (or whichever language you speak), is good enough.

Let's think of developers as darts players, and let's lay out the space of all
possible programs on a dartboard. Given *F*, some developers will often fix
a particular approach to solving the problem. The developers choose which
language to write the program in, draw up a design for the internals of the
program, and select which algorithms to use to solve the sub-problems.

![Dartboard]({filename}/images/dartboard/dartboard-1.png)

Of course, there is a cork backboard (full of nonsensical programs) to catch
errant darts, but the developers nearly always at hit the board! The bull's eye
of the dartboard contains the programs that are really correct and secure
according to *F* and *S*:

![Dartboard]({filename}/images/dartboard/dartboard-2.png)

Let's partition the region around the bull's eye into into three areas: (1)
programs that implement the correct functionality but aren't secure (bugs that
only crop up under adversarial conditions), (2) programs that are secure but
implement the wrong functionality (benign bugs), and (3) programs that are
neither secure nor implement the correct functionality, probably the most common
kind:

![Dartboard]({filename}/images/dartboard/dartboard-3.png)

Containing the bull's eye is the "circle of acceptance", which are all the
programs that will pass QA's test and be deemed ready for production use. Of
course, QA isn't perfect, so some incorrect and insecure programs slip in:

![Dartboard]({filename}/images/dartboard/dartboard-4.png)

The act of software development consists of throwing a dart at the board, of
course aiming for the bull's eye. We're not bad dart players, so programs near
the bull's eye (almost-secure and almost-correct programs) are more likely than
ones far away from it. The probability distribution over where the dart lands
might look something like this:

![fat probability distribution]({filename}/images/dartboard/distribution-1.png)

Today, most of our darts miss the bull's eye. How can we improve?

How can we improve?
-------------------

The first step is to make sure that there really *is* a bull's eye. Humans are
excellent at holding on to contradictory ideas without ever realizing they're
inconsistent. Quite often, our intuitive *F*'s and *S*'s are really
contradictory, but we don't realize it. For example, "a super-optimized
processor that makes the most efficient use of its time and energy" satisfying
the security requirement "processes must be isolated from one another" is flatly
contradictory, but we're only realizing that just now (side-channels), decades
after the invention of the microprocessor.

Once we're sure that there is a bull's eye, we want to make it as big as
possible relative to the dartboard. The more dartboard the bull's eye
encompasses, the more likely the dart throwers (developers) are to hit it on
their first try. If we zoom out and look at the entire backboard, we'll find
other dartboards corresponding to different design decisions. For example, one
approach is to use the PHP language and `mysql_real_escape_string()` to escape
data for insertion into an SQL query, and another approach is to use prepared
statements in the Rust language. The latter's bull's eye will be easier to hit.

![Dartboard]({filename}/images/dartboard/dartboard-5.png)

The problem with making the bull's eye bigger is that every developer is
inherently more comfortable working in some design spaces rather than others.
PHP experts can't become Rust experts overnight. So how we make the bull's eye
bigger has to be in line with our economic reality.

We want the circle of acceptance to hug the bull's eye tight. Making the bull's
eye bigger helps with that, because it's sandwiched between the bull's eye and
the edge of the dartboard. We tighten the circle of acceptance itself by
becoming more skeptical and deeming fewer programs as production-ready. For
example, we might accept only formally verified programs, exiling all error to
mistakes translating the intuitive *F* and *S* into formal statements. But
again, how we constrict the circle of acceptance needs to be in line with
economic reality.

We can try to be better dart throwers too. Maybe, through better education and
aligning of economic incentives, we can produce developers capable of hitting
those tiny bull's eyes. My personal opinion is that we're unlikely to see
technological breakthroughs here. We'd need to see massive advances in cognitive
science to have any hope of teaching someone how to program in C++ without also
making them ultra likely to write programs with memory corruption
vulnerabilities. So this approach boils down to recognizing that the bull's eye
we're going for is small and that we have to invest massive amounts of time and
money into making sure we hit it.

![skinny probability distribution]({filename}/images/dartboard/distribution-2.png)

The last way we can get better is a bit of a cheat: change the problem. We can
talk to the users and convince them that their *F* and *S* are too hard, and if
they could only be happy with the different *F'* and *S'* then we could actually
give them what they want. Alas, this won't be possible in general. We use
computers because of the value they provide, and we can't just rearrange the way
our whole society works so that the problems we need computers to solve are
easier.

So, which world do we live in?
------------------------------

I claim that the pseudomathematical model given above will help us figure out
which of the two extreme worlds ours is most like. We can now see the questions
we most need answers to:

1. **The human developer problem:** What is the probability distribution over
   the outcomes of *D(F, S)* when *F* and *S* are real-world intuitive
   functionality and security requirements and *D* is a team of human
   programmers?

2. **The technological bull's eye problem:** How large, relative to the set of
   all programs within the chosen design space, can we make the set of
   functional and secure programs, by way of changing our choice of design space
   (in an economically feasible way)?

3. **The technological quality assurance problem:** How closely tightly can we
   make the circle of acceptance hug the bull's eye, by way of improving our
   quality assurance technology?

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
a breakthrough without realizing we're going nowhere.

An example of a result in the unfavorable direction that I'm advocating for here
might be a "typo theorem." A typo theorem would say something like,

> *No matter which programming language you use, all secure programs are only
> a "typo" (small source code change) away from being insecure.*

It doesn't seem at all unreasonable for something like that to be true, and it
even seems to be the kind of thing we could formalize and take a shot at
proving.

We *should* move forward with optimism, believing that one day things will get
better. But I don't think we should have *blind optimistic faith*. For all the
effort we put into making things better, we should be putting at least half as
much effort into showing that we fundamentally can't. This is the only way to
understand the problems we're facing, and it's the only way we'll ever stop
creating "solutions" that eventually get discarded as failures.

*What do you think?* I'm curious what others in the industry think about the
future of information security. Are you holding out hope for big breakthroughs?
Or do you think that the status quo is the best we will be able to do aside from
minor improvements in the future? Leave a comment below.
