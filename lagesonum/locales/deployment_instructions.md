If not yet installed, install [translate-toolkit](http://translate-toolkit.readthedocs.org/en/stable-1.13.0/):
    *sudo apt-get install translate-toolkit*

This program provides [csv2po](http://translate-toolkit.readthedocs.org/en/latest/commands/csv2po.html) which we will need later on.
[msgfmt](http://gnuwin32.sourceforge.net/packages/gettext.htm) should already be installed on your (unix) system.

0. Perform *git pull* to synchronize your local repository
1. Get the translation table to be released from Daniela.
2. Erase all columns not having complete translation or ID, so esp. the description.
3. Create pairwise .csv files for one source language (e.g. Deutsch) and each target language (Arab, English, Esperanto usw.). Each of these csv files has [three columns](http://translate-toolkit.readthedocs.org/en/latest/commands/csv2po.html): id, source, target language. The files are to be named according to their target language
4. Create a further .csv where the source language is the target language and choose English as source language.
5. For input.csv in csv_files: *csv2po input.csv output.po* where output.po follows the convention de_DE.po
6. For input.po in po_files: *msgfmt input.po -o messages.mo*  (don't change the name of messages.mo).
7. Place messages.mo in the respective *folder lagesonum/locales/$i18n-code/LC_MESSAGES* . The corresponding .po file should also be placed in this folder.
8. Commit and push/create pull request to have the translations enter the repository for final deployment by Chris (message him on slack!)

This deployment method is only temporary and definitely needs improvement, see [issue #7](https://github.com/fzesch/lagesonum/issues/7)

Also, with designated translators for each language, direct .po-deployment would be possible in the future.