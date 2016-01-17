Title: QIP 2016
Date: 2016-01-16
Slug: qip-2016-conference
Category: Quantum
Status: published

Last week I attended the [QIP 2016 conference](https://ucalgary.ca/qip2016/) on
quantum information processing. It started out as two days of turorial sessions
at the University of Calgary and then moved to the main venue in the beautiful
Banff, Alberta:

![QIP 2016 Venue in Banff]({filename}/images/qip2016.jpg)

Even though my background is in information security and cryptography, it's one
of my life goals to understand how nature works. So I've applied to grad school
to study quantum computing. It's the perfect intersection of physics and
computer science, so my existing computer science background will remain useful.
I'm not abandoning infosec – there's lots of infosec-like parts to quantum
information, like quantum cryptography and post-quantum cryptography – and my
hope is to bring some of the quantum formalisms back over to classical infosec
and make the computers we use right now more secure.

Being a newcomer to quantum information, I knew I wouldn't understand, nor care
about, most of the results being presented there. I went to get a glimpse at the
frontier of quantum information research, mainly to see if I would like it
there. Moreover, I went there to see what got the researchers excited.
Excitation is contagious, and I wanted to pick some of it up.

I was right that I wouldn't understand most of it. While everyone in the room
was scrutinizing the presenters' sketch proofs, I was busy trying to reverse
engineer the formal definitions of things like "conditional mutual information"
and "semidefinite programming." I kept a list of the unknown terms I heard most
frequently, and now I have a solid list of things to study before I go to grad
school.

Another thing I picked up was a new appreciation for topics I used to think were
boring and artificial. Error correcting codes are one example. I used to think
they were an artificial solution to an artificial problem. We can't build
reliable communications channels, so we have to apply some extra engineering
effort to reliably send information through them. Nothing fundamental; all
boring. At QIP, I saw that error correction is actually much more fundamental
than I'd ever thought. It's really about the *ways in which information can be
stored* in a medium, how information can be spread out so that it is not all in
one place. This becomes immediately clear in the quantum realm, where your
information is not just bits but entangled qubits and the no-cloning theorem
means you can't just deal with errors by storing lots of copies of the same
information.

All information is encoded with some sort of error correcting code, we usually
just never notice it because the codes are so familiar. The bit that the coin
resting on your desk represents with its heads-or-tails state is
error-correcting encoded: the intricate patterns on the two surface make it easy
for you to distinguish the two sides and the energy required to flip the coin
over makes it easy for you to determine which side is facing up, even when the
coin is damaged or there's an earthquake shaking your desk. Once you start
looking for them, you'll see codes are everywhere. What I thought was an
artificial and boring subject turns out to be fundamentally necessary for our
world to work.

My favorite thing about QIP was that all of the papers are open-access. Every
paper presented is up on the [arXiv](http://arxiv.org/), and most of the talks
cited the work they were based on by their arXiv identifier code. Way to go,
quantum information community, for doing an excellent job of making it easy for
a newcomer to get started in your field.

With some luck, I'll be back for QIP in 2017.
