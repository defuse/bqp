Title: Is Quantum Key Distribution Worth Using?
Date: 2017-03-09
Slug: when-is-quantum-key-distribution-worth-using
Category: Security and Cryptography
Status: published
Image: images/fibre.jpg

Even though general-purpose quantum computers seem pretty far off, there are
already some companies selling quantum key distribution (QKD) products today.
That means there are some people in the world who will have to decide whether or
not to use QKD to protect their company's communications. This is a post written
for those people.

Most importantly, if you're going to use QKD at all, you should always have
a layer of conventional cryptography running underneath so that if the QKD fails
for some reason, you can fall back on the security of conventional cryptography.
The commercial products I've seen have this built in, but you'll need to make
sure it's implemented with standard widely-reviewed cryptography libraries.

When you're using conventional cryptography and QKD at the same time, you get
security that's as good as the strongest one. But in practice if you choose to
use both, you'll have to split your defense resources. This means that you can
end up worse off because the money you spent on the QKD system could have been
spent discovering that severe flaw lurking in your conventional crypto code. The
extra money you're spending on QKD could also be spent on more effective
defenses like security training for employees or something like that.

Even though QKD is always used in combination with conventional cryptography, it
wouldn't be fair to compare conventional cryptography to QKD+conventional. If
you're deciding how much of your defense resources to allocate to QKD vs.
conventional, the fair comparison is between QKD and conventional crypto.

What we'll compare are QKD and conventional crypto's ability to set up a private
and authenticated "secure channel" between two parties, Alice and Bob. There are
two different scenarios that matter:

1. *Private setup scenario:* Alice and Bob get to talk to each other in private
   and then want to set up a secure channel they can keep talking over after
   they've separated.
2. *Public setup scenario:* Alice and Bob get to meet each other *in public* and
   want to set up a secure channel. For example, they might meet in a grocery
   store so that they can recognize each other and talk to each other, but the
   adversary could be listening in on their conversation from across the aisle.

All of the cryptography that's around for setting up secure channels effectively
happens in one scenario or the other, so looking at how QKD and conventional
cryptography perform in each will make a fair comparison. You can build a secure
channel in each scenario with either QKD or conventional cryptography, but they
will rely on different assumptions, and we obviously want to pick the one whose
assumptions are most likely to be true.

Conventional Cryptography
---------------------------

In the private setup scenario, the best Alice and Bob can do with conventional
cryptography is to exchange some secret key in private and then build the secure
channel out of a cipher like AES and some hash function like BLAKE2. If the
adversary compromises Alice or Bob and steals the secret key, they'll be able to
decrypt all future messages. If Alice and Bob design their protocol properly,
they can make it  so that an adversary who compromises them can't decrypt past
messages (e.g. by hashing their session key to make the next one and destroying
the old one). And, obviously, Alice and Bob need to implement the crypto
correctly, or there will be problems.

So, to build a secure channel in the private setup scenario, conventional
cryptography needs to assume:

1. The *symmetric* crypto primitives (e.g. AES and BLAKE2) are secure.
2. The adversary is computationally bound, e.g. to a maximum of 2<sup>96</sup> operations.
3. The implementation doesn't have security weaknesses.

In the public setup scenario, conventional cryptography needs to make all the
same assumptions, except it needs one extra ingredient: public key encryption.
Breaking public key encryption seems to be a [different kind of computational
problem](https://windowsontheory.org/2013/10/07/structure-vs-combinatorics-in-computational-complexity/)
than breaking symmetric encryption. The problems that arise from public key
encryption are more structured, for example RSA is based on factoring integers
and so a lot of number theory tricks can be used to break it faster.

So, to build a secure channel in the public setup scenario,
conventional cryptography needs to assume:

1. The *symmetric* crypto primitives (e.g. AES and BLAKE2) are secure.
2. The *public key encryption* crypto primitives (e.g. RSA or X25519) are secure.
3. The adversary is computationally bound, e.g. to a maximum of 2<sup>96</sup> operations.
4. The implementation doesn't have security weaknesses.

It's worth pointing out that the public key encryption primitives we most rely
on today (RSA, Diffie-Hellman, elliptic curves, etc.) can all be broken by
a quantum computer if one is ever built, but there are new kinds of public key
encryption [being developed](https://pqcrypto.org/) that should be secure
against quantum computers.

Quantum Key Distribution
--------------------------

QKD schemes like BB84 generally assume Alice and Bob can already talk to each
other over an authenticated (but potentially wiretapped) channel and then
provide information-theoretic security under that assumption. To fit QKD into
our more realistic public and private setup scenarios, Alice and Bob will have
to build the authenticated channel themselves.

In the secret setup scenario, Alice and Bob can exchange enough key material
that they can use some kind of information-theoretically-secure authentication
scheme in the first run of the QKD protocol. In the first run of the protocol,
they can exchange some extra key material to be used for the authentication in
the second run, and so on. In this scenario, QKD looks more like key expansion:
Alice and Bob exchange keys in private once, and then QKD provides
information-theoretic security into the future.

So, to build a secure channel in the private setup scenario, QKD
needs to assume simply that:

1. The implementation doesn't have security weaknesses.

In the public setup scenario, Alice and Bob will need to rely on conventional
cryptography to create the authenticated channel. To do this, Alice and Bob
*don't* need public key encryption. They can pick a hash-based digital signature
scheme like SPHINCS that only relies on the security of a hash function.
Furthermore, they only need to rely on it once in the first run of the protocol,
since after that they can switch to an information-theoretically-secure
authentication scheme by sharing some extra key material to use for
authentication in future runs of the protocol.

So, to build a secure channel in the public setup scenario, QKD
needs to assume:

1. The *symmetric* crypto primitives (e.g. BLAKE2) are secure *during the first
   run of the protocol*.
3. The adversary is computationally bound, e.g. to a maximum of 2<sup>96</sup>
   operations *during the first run of the protocol*.
3. The implementation doesn't have security weaknesses.

Compare these lists of assumptions to the ones above for conventional
cryptography. In the private setup scenario, perfectly-implemented QKD
eliminates our reliance on any kind of computational-hardness-based
cryptography. In the public setup scenario, perfectly-implemented QKD eliminates
our reliance on public key cryptography and eases our reliance on symmetric
cryptography.

Implementation Vulnerabilities
--------------------------------

From the analysis I've given so far, one might be tempted to conclude that QKD
is better because it eliminates assumptions. In both setup scenarios QKD builds
a secure channel assuming less than conventional cryptography, so it's more
likely to be secure. The problem with this view is that it neglects a comparison
between how hard it is to implement conventional cryptography securely vs. how
hard it is to implement QKD securely.

We all know how hard it is to write conventional crypto code. The mantra we
repeat over and over is "Don't roll your own crypto." Even projects like
OpenSSL—that nearly all of us depend on in one way or another—are repeatedly
found to contain vulnerabilities. There's a good amount of crypto-like software
involved in doing QKD, too. After Alice and Bob are finished exchanging photons
(or whatever), they have to do some security-critical postprocessing to detect
possible eavesdroppers and agree upon a key. I'm not sure if a QKD system has
ever been broken because of mistakes in that code, but I have no reason to
believe it will be any less buggy than conventional crypto code tends to be.

In addition to software errors, QKD will suffer from *physical* implementation
problems. An adversary attacking a QKD implementation generally has optical
access to parts like the single-photon detectors that are crucial to the
security of the QKD protocol. This opens up totally new kinds of attacks. For
example, it's possible to [blind single-photon detectors and then take control
of them](http://www.nature.com/nphoton/journal/v4/n10/abs/nphoton.2010.214.html)
or just insert a backdoor into the system by [damaging some of its parts with
a laser](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.94.030302).
What's happening here is that a QKD protocol is proven secure assuming some
theoretical model of its implementation components and these attacks show that
the components can be made to act differently than the models predict. Those
differences lead to security vulnerabilities.

Conventional cryptography can have side-channel vulnerabilities, which are
a kind of physical implementation problem. But that's pretty much the extent to
which conventional crypto is vulnerable to remote physical attacks (Update: See
also the [WALNUT Attack](https://spqr.eecs.umich.edu/walnut/)). If you shine
a super-high-power laser down a conventional fiber-optic line, it's probably not
going to burn anything that's important to security. At best you'll burn out the
sensor and cause a denial of service attack. Moreover, there's a clear rule for
avoiding side-channel vulnerabilities in conventional cryptography: don't make
branches or memory lookups based on sensitive data. The physical attacks on QKD
systems seem to be a lot more diverse, and I'm skeptical that there's an easy
way to eliminate them completely. So although QKD elimintates some computational
hardness assumptions, it seems a lot harder to get the physical implementation
right.

There is such a thing as "device-independent" quantum key distribution, which
remains secure even if the adversary can make limited modifications to the
device. It would prevent these kinds of vulnerabilities too but I'm not aware of
any commercial QKD systems using it.

The Bottom Line
---------------

I personally place a lot of trust in our current best symmetric cryptography.
I don't think AES or SHA3 will ever be broken. On the other hand I wouldn't bet
that the kinds of public-key encryption that quantum computers can break (RSA,
elliptic curves, etc.) will stay secure for more than 10 years from now. Our top
priority should be to cautiously settle on post-quantum replacements.

Once we have good post-quantum public-key encryption, I think I'll trust the
computational hardness assumptions more than our ability to make
vulnerability-free QKD devices. When computational hardness assumptions are
broken, they're broken slowly and incrementally. Factoring is a great example:
we started migrating away from it (or to higher key sizes) because attacks got
better, and we migrated faster than the attacks improved. So hardness
assumptions will give warning before they fail; it would be more catastrophic if
we suddenly found a vulnerability in some QKD hardware that's been deployed
already to millions of users, with no possibility of a software patch.

To conclude, if you're still interested in using QKD then here are some things
to consider:

1. Could you get a better return on your investment by migrating to post-quantum
   cryptography instead?
2. Would it be better to invest in some other kind of security, like security
   awareness training for your staff?
3. Will you have conventional cryptography running underneath the QKD so that
   you'll fall back on that if the QKD gets breached?
4. Has the code/hardware postprocessing logic for your vendor's device been
   audited by a competent third-party security consultancy?
5. Has the QKD hardware been audited by a competent third-party team of [quantum
   hackers](http://www.vad1.com/lab/)?
6. How quickly will you be able to replace the QKD devices if a physical
   implementation vulnerability is found in the future? Will your QKD supplier
   give you free replacements when vulnerabilities are found?

Extra Reading
--------------

- [Challenges to Physical Security of Today’s Quantum Technologies](https://www.youtube.com/watch?v=YaiYn6sQqlw) (90 minute talk).
- [Attacks on practical quantum key distribution systems (and how to prevent them)](https://arxiv.org/abs/1512.07990)
- [Secure quanutm key distribution](https://arxiv.org/abs/1505.05303)
- [The black paper of quantum cryptography: real implementation problems](https://arxiv.org/abs/0906.4547).
- [The Case for Quantum Key Distribution](https://arxiv.org/abs/0902.2839).
