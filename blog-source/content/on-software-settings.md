Title: On Software Settings
Date: 2016-11-03
Slug: on-software-settings
Category: Software Engineering

The first problem with settings is the "tyranny of the default." Empirically, we
find that users are unaware that the setting exists even if they would have
wanted to toggle it had they known about it. The third-party cookie setting in
your browser is an example. To avoid the tyranny of the default, you can't have
a default; you have to prompt the user for what the setting should be before
they can start using the software.

The second problem with settings is that they cause an exponential blowup in the
complexity of your software. If each setting can take on at least one of two
values, then every setting you add at least doubles the number of cases the
software has to be written to handle. All of those cases have to be tested. In
practice, what ends up happening is that you test a small fraction of all
possible configurations, and then years down the line someone uses
a configuration you hadn't tested and encounters a bug. If I were that user,
I would prefer to be forced to find some workaround for the setting's
nonexistence than to unknowingly use a buggy program.

If the setting is really important to have, enough users will want it that some
fraction of them will bother to email the project developer or open an issue on
GitHub. Until the developers see that signal, though, they should not add the
setting. We should start with correctness, not configurability. From there, the
userbase can rationally decide to buy configuration options at the expense of
reliability.

The same is true of features.
