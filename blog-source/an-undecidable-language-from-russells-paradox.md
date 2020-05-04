Title: Proving Undecidability Using Russell's Paradox
Date: 2016-04-17
Slug: an-undecidable-language-from-russells-paradox
Category: Complexity Theory
Status: draft

TODO: preamble about complexity classes

Let Σ<sup>\*</sup> be the set of all strings over the language Σ = {0, 1}. Let
LanguageDescribedBy be a function from Σ<sup>\*</sup> into the set of all
languages, i.e. for any string s in Σ<sup>\*</sup>, LanguageDescribedBy(s) is
the language described by s. This could be instantiated, for example, by
interpreting the string s as a Turing Machine taking the language that Turing
Machine decides.

A language L ⊆ Σ<sup>\*</sup> is said to *contain a description of itself* if
there exists an x ∈ L such that LanguageDescribedBy(x) = L.

We can try to get Russell's paradox by considering the set of all languages who
do not contain descriptions of themselves, i.e. NoParadox
= { L | ¬∃x∈L(LanguageDescribedBy(x) = L) }. This doesn't lead to a paradox,
however, since NoParadox is a set of languages, and languages only contain
strings, so it clearly doesn't contain itself.

To get a paradox, we need to consider the set of all language descriptions that
describe a language that doesn't contain a description of itself. In math,
Paradox = { s | ¬∃x∈L(LanguageDescribedBy(x) = LanguageDescribedBy(s)) }.

Assuming Paradox is describable (i.e. decidable for a suitably chosen definition
of LanguageDescribedBy), we have Russell's paradox. For if Paradox contains
a description of itself, blah blah

finite space heirarchy
