Title: Mandatory Backdoors are a Tax on Encryption
Date: 2016-03-29
Slug: economics-of-mandatory-backdoors
Category: Security and Cryptography
Status: published

There are plenty of good arguments against mandatory crypto backdoors. All of
the ones I've seen invoke at least one of the following assumptions:

1. We can't trust the government that's holding the keys.
2. The government holding the keys can't keep their computer systems secure.
3. The government doesn't really need crypto backdoors.
4. The "bad guys" can write their own un-backdoored encryption tools and use those.
5. It's technically infeasible to backdoor a cryptosystem in a secure way.

Let's build an even stronger argument against mandated backdoors. We'll be
*insanely* generous to the government and negate all of those assumptions.
Assume the following:

1. The government is 100% trustworthy.
2. The government is capable of securing computer systems and protecting keys.
3. The government really needs crypto backdoors.
4. The "bad guys" will use U.S.-based commercial cryptography products.
5. It's possible to backdoor a cryptosystem in a way that's secure, but it's
   more difficult and expensive than if the system weren't backdoored.

Here's an argument against crypto backdoors that works even under these highly
optimistic assumptions: *Mandated crypto backdoors are like a tax on the use of
cryptography, which incentivizes companies to produce less-secure products.*

If we decide to obligate crypto backdoors then any company who uses cryptography
in their products must be prepared to add the backdoor feature to their product.
By assumption (5), doing so will incur an additional cost. The company must
divert engineering resources away from other things – things that will likely
bring the company more profit – towards adding the backdoor, which will bring
the company no additional profit, since from the user's perspective it is the
same. The company is therefore paying a tax, in the form of opportunity cost, to
use encryption in their product.

In response to this tax, companies can either compromise on security by deciding
not to use encryption at all or by spending less engineering and quality
assurance effort on the parts of their product that involve cryptography (making
vulnerabilities more likely), or by choosing not to compromise on security,
carefully implementing the backdoor, and accepting the loss in profit.

It's clear from the economic incentives that software written by companies
mandated to add backdoors will tend to be less secure.

The true cost of mandatory backdoors is now in plain view. In order to
circumvent my argument, the government (and by extension, the people) must be
willing to reimburse software companies for the added cost to design, implement,
review, and test the backdoor. This could amount to billions of dollars if the
government wants backdoors in everything. That's money that could be spent on
healthcare, disease research, and other things that *actually save lives*. Even
if the government can convince us of assumptions (1), (2), (3), (4), and (5),
they *still have to convince us that they can save more lives using the access
those backdoors provide than we could save by spending that money elsewhere.*
