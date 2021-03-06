Title: My Life and Projects, Right Now
Date: 2016-02-10
Slug: my-life-and-projects-right-now
Category: Software Engineering
Status: published
Image: images/clock.jpg

It's often difficult for me to say "no" to taking on new projects. Some ideas
are so captivating that they beg to be implemented. The problem is, if you are
eager to say "yes" to every interesting project that crosses your path, they'll
quickly fill up your life to the exclusion of important things like spending
time with family and friends.

Recently, I've started saying "no" to everything that gets proposed to me.
I want to trim my obligations down to just a few things that I really care
about. Once I do that, I'll be able to do a really good job of those few things,
while still having time for all of the non-project things in my life. As well as
not taking on any new projects, I've started to "end of life" some of the open
source projects I've become responsible for over the years. These are the ones
that are pretty much "finished" and no longer need to undergo active
development:

## defuse/php-encryption

[defuse/php-encryption](https://github.com/defuse/php-encryption) is one of the
few cryptography libraries for PHP that doesn't get almost everything wrong.
Version 2.0 is in the works, and it's nearly done. It adds support for
encrypting large files without loading them all into memory, as well other
things like composer support that make the library easier to use. It's probably
about 40 hours of work away from completion. Once it's done, I don't expect to
touch it ever again, except to fix bugs. If you need more features, you should
be using [libsodium](https://github.com/jedisct1/libsodium) (it has bindings for
PHP).

## defuse/password-hashing

[defuse/password-hashing](https://github.com/defuse/password-hashing) is
password hashing code in PHP, C#, Java, and Ruby. It's the code that, for a long
time, lived on [CrackStation.net's hashing security
page](https://crackstation.net/hashing-security.htm). I'm ending its life since
it uses PBKDF2 and today we have better options (bcrypt, scrypt, yescrypt,
Argon2, etc.)

I'm happy to announce that just today I signed the git tag for its [version 2.0
release](https://github.com/defuse/password-hashing/tree/v2.0). Version 2 has
been nipping at my free time [since
2014](https://github.com/defuse/password-hashing/issues/28)! Obviously, I'm
relieved to finally have it finished. Version 2.0 makes all of the
implementations compatible with each other, so that you can create hashes in PHP
and check them in C#, or whichever combination you'd like. Having
implementations that are compatible with each other, and tested against each
other, also reduces the chance that any one of them has serious security bugs.

If you want to use PBKDF2 in a PHP, C#, Java, or Ruby project, it's definitely
what you want to be using. But you should try to use the [scrypt in
libsodium](https://download.libsodium.org/doc/password_hashing/index.html)
first, and keep an eye out for the [PHC](https://password-hashing.net/) winner
Argon2.

I don't expect to touch the code any more, at least not until better algorithms
are natively available in those languages. Maybe once PHP, C#, Java, and Ruby
all natively support Argon2 I'll make a version 3.0, that's backwards-compatible
with version 2.0, to make it easy for users to upgrade to the better algorithm.

## The future?

So far I've told you I'm getting rid of the obligations in my life, and I've
mentioned the two projects that I'm putting to rest. What *will* I be working on
in the future?

I'm excited to announce that the University of Waterloo just offered me
admission into an MMath computer science degree in quantum information.
I couldn't be happier about it, because I've always loved physics, and getting
to study physics alongside theoretical computer science sounds like it will be
an amazing experience. I'm planning to meld the mathematics of quantum mechanics
with my infosec background in interesting ways... hopefully some good will come
of it.

So, my current priorities are:

1. [Zcash](https://z.cash/): This is my day job. I work with an [awesome
   team](https://z.cash/team.html) of engineers to build what you might already
   know as Zerocoin or Zerocash. If anything on Earth is better than getting
   paid to learn physics and computer science, it's this job.

2. The [Underhanded Crypto Contest](https://underhandedcrypto.com/): This is
   a contest kind of like the Underhanded C contest, except for cryptography
   protocol designs and implementations. There's a [2016
   contest](https://underhandedcrypto.com/2016/01/17/2016-underhanded-crypto-contest/),
   so if pretending to be the NSA and backdooring stuff is your thing,
   I encourage you to participate!

3. Learning quantum information stuff before I go to Waterloo. I haven't
   accepted Waterloo's offer yet, but it's *very* appealing, and I want to go in
   already knowing a lot about quantum mechanics and the related computer
   science. So, hopefully I'll have some leftover time to do studying.

4. Finishing my Flush+Reload research project. For my undergrad thesis I proved
   that you can use the Flush+Reload side-channel attack can tell which of a set
   of web pages you're visiting, or which of a set of PDF files you're opening,
   from another unprivileged user account on your system. I think this research
   is really important since it shows that Flush+Reload can do way more than
   just steal keys from OpenSSL. Right now the project has been passed on to
   another (very talented) student, so I'm hoping to have time to help them
   polish up the final results. Right now, there's a robust attack tool and good
   repeatable experiment code sitting in a private GitHub repository; I want to
   get that out for the world to play with as soon as possible.

5. [Yescrypt implementations](https://github.com/defuse/yescrypt): I'm
   implementing Solar Designer's yescrypt algorithm in a bunch of different
   languages. Sadly, this is my most neglected project, and I'm really
   disappointed with the feeble amount of time I've put into it. It's important,
   because it gives Solar Designer feedback on how easy it is to implement
   yescrypt and it double-checks the correctness of the reference code.

So, those are the 5 things I'm working on right now. Hopefully this list will
keep getting shorter.
