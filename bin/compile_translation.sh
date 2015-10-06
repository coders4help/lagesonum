#!/bin/sh

for lang in lagesonum/locales/*/LC_MESSAGES/*.po
do
	msgfmt --strict -o ${lang%/*}/messages.mo ${lang}
done
