# Instructions of deployment for i18n-files

## Process
0. Perform *git pull* to synchronize your local repository
1. Get the translation table to be released from Daniela.
2. Verify that languages you want to include are correctly stated in bottle_app.py
3. Verify that column headers of languages you want to add contain correct locale in Excel sheet.
4. Run xls2po.py (requires the library polib)
5. Test translations locally by clicking randomly on pages and languages. If everything is alright, continue; else: contact Daniela.
6. If you added new languages, add them to the local git repository
7. Commit and push/create pull request to have the translations enter the repository for final deployment by Felix (message him!)

## Future changes

A change to a more common deployment system for .po/.mo is highly appreciated. We consider transifex, but had no time to set it up, yet. If you want to help, please contact Felix.
