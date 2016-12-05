Title: Qubes Backup Encryption added to CrackStation
Date: 2016-11-13
Slug: qubes-backup-encryption-added-to-crackstation
Category: Security and Cryptography

I've added Qubes OS Version 3's backup encryption to my online password cracking
service, [CrackStation](https://crackstation.net/). It was possible to do this
because Qubes' backup encryption does not correctly salt the backup encryption
password.

To crack a Qubes OS backup password, follow the first steps of [these
instructions](https://www.qubes-os.org/doc/backup-emergency-restore-v3/) to
extract the contents of the backup. Copy and paste the contents of
`backup-header.hmac` into the form on CrackStation's homepage. If the password
is in CrackStation's dictionary, and the Qubes user used the default backup
settings, it will find the password in its lookup table, and return it to you.

The Qubes team is actively working on a fix to this problem in [this GitHub
issue](https://github.com/QubesOS/qubes-issues/issues/971). If you have
cryptography experience, and you want to help Qubes fix this problem, please go
read the comments on that issue and lend them a helping hand!

## Technical Details

The contents of `backup-header.hmac` is the output of the command `openssl dgst
-sha512 -hmac '<the password>' backup-header`. This computes the HMAC-SHA512 of
the contents of the `backup-header` file using the password as the HMAC key. By
default, the contents of `backup-header` is
`version=3\nhmac-algorithm=SHA512\ncrypto-algorithm=aes-256-cbc\nencrypted=True\ncompressed=False\n`.
There's no salt involved in the computation of this HMAC, so if the user has
left the Qubes backup settings as their defaults, the HMAC of this file will
have been computed in exactly the same way as the HMACs in CrackStation's hash
database. That's why a simple binary search lookup of the hash in the database
can quickly reverse the hash into its corresponding password.
