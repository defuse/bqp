Title: Is Quantum Key Distribution Worth Using?
Date: 2017-03-09
Slug: when-is-quantum-key-distribution-worth-using
Category: Security and Cryptography
Status: draft
Image: images/fibre.jpg

Even though general-purpose quantum computers seem pretty far off, there are
already some companies selling quantum key distribution (QKD) products today.
That means there are some people in the world who will have to decide whether or
not to use QKD to protect their company's communications. This is a post written
for those people.

Most importantly, if you're going to use QKD at all, you should always have
a layer of conventional cryptography running underneath so that if the QKD fails
for some reason, you can fall back on the security of conventional cryptography.

When you're using conventional cryptography and QKD at the same time, you get
security that's as good as the strongest one. But in practice if you choose to
use both, you'll have to split your defense resources. This means that you can
end up worse off because the money you spent on the QKD system could have been
spent discovering that severe flaw lurking in your conventional crypto code. The
extra money you're spending on QKD could also be spent on better
security-improving programs like anti-phishing training for your company's
employees, or something like that.

Even though QKD is always used in combination with conventional cryptography, it
wouldn't be fair to compare QKD to QKD+conventional. If you're deciding how much
of your defense resources to allocate to QKD vs conventional, the fair
comparison is between QKD and conventional crypto.

What we'll compare are QKD and conventional crypto's ability to set up a secure
authenticated channel between to parties, Alice and Bob. There are basically two
different scenarios that matter:

1. *Private setup scenario:* Alice and Bob get to talk to each other in private
   and then want to set up a secure authenticated channel to keep talking in
   private after they've separated.
2. *Public setup scenario:* Alice and Bob get to talk to each other *in public*
   and then want to set up a secure authenticated channel. For example, they
   might meet in a grocery store and can recognize each other and talk, but have
   to assume the adversary is listening to their conversation through the aisle.

In order to construct a secure channel in these different setup scenarios, both
QKD and conventional cryptography need to rely on different assumptions.

Conventional Cryptography
---------------------------

In the private setup scenario, the best Alice and Bob can do with conventional
cryptography is to exchange some secret key in the private setup and then build
the secure channel out of a cipher like AES and some hash function like BLAKE2.
If either of Alice and Bob get compromised, the adversary will be able to
decrypt all future messages. If Alice and Bob design their protocol properly,
they can make it  so that an adversary who compromises one of them can't decrypt
past messages (e.g. by hashing their session key to make the next one and
destroying the old one). And, obviously, Alice and Bob need to implement the
crypto correctly, or there will be problems.

So, to build a secure authenticated channel in the private setup scenario,
conventional cryptography needs to assume:

1. The *symmetric* crypto primitives (AES, BLAKE2) are secure.
2. The adversary is computationally bound, e.g. to a maximum of 2<sup>80</sup> operations.
3. The implementation doesn't have security weaknesses.

In the public setup scenario, conventional cryptography needs to make all the
same assumptions, except it needs one extra ingredient: public key encryption.
Breaking public key encryption seems to be a different kind of problem than
breaking symmetric encryption. The problems that arise from public key
encryption are more structured, for example RSA is based on factoring integers,
and so a lot of number theory tricks can be used to speed it up.

So, to build a secure authenticated channel in the public setup scenario,
conventional cryptography needs to assume:

1. The *symmetric* crypto primitives (e.g. AES, BLAKE2) are secure.
2. The *public key encryption* crypto primitives (RSA, X25519) are secure.
3. The adversary is computationally bound, e.g. to a maximum of 2<sup>80</sup> operations.
4. The implementation doesn't have security weaknesses.

It's worth pointing out that the public key encryption primitives we mostly rely
on today (RSA, Diffie-Hellman, elliptic curves, etc.) can all be broken by
a quantum computer if one is ever built, but there are new kinds of public key
encryption being developed that should be secure against quantum computers.

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

So, to build a secure authenticated channel in the private setup scenario, QKD
needs to assume simply that:

1. The implementation doesn't have security weaknesses.

In the public setup scenario, Alice and Bob will need to rely on conventional
cryptography to create the authenticated channel. To do this, Alice and Bob
*don't* need public key encryption. They can pick a hash-based digital signature
scheme like SPHINCS that only relies on the security of a hash function.
Furthermore, they only need to rely on it once in the first run of the protocol,
since after that they can switch to an information-theoretically-secure
authentication scheme.

So, to build a secure authenticated channel in the public setup scenario, QKD
needs to assume:

1. The *symmetric* crypto primitives (e.g. BLAKE2) are secure during the first
   run of the protocol.
3. The adversary is computationally bound, e.g. to a maximum of 2<sup>80</sup>
   operations during the first run of the protocol.
3. The implementation doesn't have security weaknesses.

Compare these lists of assumptions to the ones above. In the private setup
scenario, perfectly-implemented QKD eliminates our reliance on any kind of
computational-hardness-based cryptography. In the public setup scenario,
perfectly-implemented QKD eliminates our reliance on public key cryptography.

Implementation Issues
---------------------

From the analysis I've given so far, one might be tempted to conclude that QKD
is better because it only eliminates assumptions. In both setup scenarios QKD
builds a secure channel assuming less than conventional cryptography, so it's
more likely to be secure. The problem with this view is that it neglects
a comparison between how hard it is to implement conventional cryptography
securely vs. how hard it is to implement QKD securely.

We all know with how hard it is to write conventional crypto code. The mantra we
repeat over and over is "Don't roll your own crypto." Even projects like
OpenSSL—that nearly all of us depend on in one way or another—are repeatedly
found to contain vulnerabilities. There's a good amount of software involved in
doing QKD, too. After Alice and Bob are finished exchanging photons (or
whatever), they have to do some security-critical postprocessing (called
information reconciliation and privacy amplification). That code is just as
liable to be buggy, so QKD is probably going to suffer from the same kinds
implementation difficulties as we see with conventional crypto.

In addition to software errors, QKD will suffer from *physical* implementation
problems. An adversary attacking a QKD implementation generally has optical
access to parts like the single-photon detectors that are crucial to the
security of the QKD protocol. This opens up totally new kinds of attacks. For
example, it's possible to [blind single-photon detectors and then take control
of them](http://www.nature.com/nphoton/journal/v4/n10/abs/nphoton.2010.214.html)
or just insert a backdoor into the system by [damaging some of its parts with
a laser](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.94.030302).
What's happening here is that a QKD protocol is proven secure assuming some
theoretical model of its components. What these attacks show is that the
components can be made to act differently than the models predict, and those
differences are enough to break the protocol's security.

Conventional cryptography can have side-channel vulnerabilities, which are
a kind of physical implementation problem. But that's pretty much the extent to
which conventional crypto is vulnerable. If you shine a super-high-power laser
down a conventional fiber-optic line, it's probably not going to burn anything
that's important to security. At best you'll burn out the sensor and cause
a denial of service attack. Moreover, there's a clear rule for avoiding
side-channel vulnerabilities in conventional cryptography: Don't make branches
or memory lookups based on sensitive data. The physical attacks on QKD systems
seem to be a lot more diverse, and I doubt there's an easy way to eliminate
them. So although QKD elimintates some computational hardness assumptions, it
seems a lot harder to get the physical implementation of the QKD protocol right.

There is such a thing as "device-independent" quantum key distribution, which
remains secure even if the adversary can make limited modifications to the
device. It would also be secure against these kinds of vulnerabilities, but I'm
not aware of any commercial QKD system that uses it.

The Bottom Line
---------------

I think it's safe to rely on our current best symmetric cryptography. I don't
think AES or SHA3 will ever be broken. I wouldn't bet on the kinds of public-key
encryption that quantum computers can break (RSA, elliptic curves, etc.)
remaining secure for more than 10 years from now. Our top priority should be to
cautiously settle on some post-quantum replacements for them. Once we have good
post-quantum public-key encryption, I think I'll trust the computational
hardness assumptions much more than QKD. When computational hardness assumptions
are broken, they come slowly and incrementally. Factoring is a great example: we
started migrating away from it (or to higher key sizes) because attacks got
better, and we migrated faster than the attacks improved. So hardness
assumptions will give warning before they fail; it would be more catastrophic if
we suddenly found a loophole in some QKD hardware that's been deployed already
to millions of users, with no possibility of a software patch.


If you're intrested in using QKD for real, then here are some things to
consider?

1. Could you get a better return on your money by migrating to post-quantum
   cryptography instead?
2. Would it be better to invest in some other kind of security, like security
   awareness training for your staff?
3. Will you have conventional cryptography running underneath the QKD so that
   you'll fall back on that if the QKD gets breached?
4. Has the code/hardware postprocessing logic for your vendor's device been
   audited by a competent third-party auditing service?
5. Has the QKD hardware been audited by a competent team of [quantum
   hackers](http://www.vad1.com/lab/)?

Extra Reading
--------------

- [Attacks on practical quantum key distribution systems (and how to prevent them)](https://arxiv.org/abs/1512.07990)
- [Secure quanutm key distribution](https://arxiv.org/abs/1505.05303)
- [The black paper of quantum cryptography: real implementation problems](https://arxiv.org/abs/0906.4547).
- [The Case for Quantum Key Distribution](https://arxiv.org/abs/0902.2839).
