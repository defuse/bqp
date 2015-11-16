#!/bin/bash
cp pelicanconf.py pelicanconf-publish.py
echo 'RELATIVE_URLS = False' >> pelicanconf-publish.py
pelican -s pelicanconf-publish.py content
rm pelicanconf-publish.py
