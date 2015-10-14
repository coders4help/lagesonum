# Instructions of deployment for i18n-files

## Process
0. Perform ```git pull``` to synchronize your local repository

1. If you want to help, translating, please update translations at
   [Transifex Project page](https://www.transifex.com/coders4help/lagesonum-1/)
   (requires Transifex login, which can easily created)

2. If you help translating: make sure you have tx client installed:
   ```pip3 install -r requirements.txt```


3. Update .po-files: ````tx pull````

   requires to configure tx client, e.g. by creating ```~/.transifexrc```:
    ```
    [https://www.transifex.com]
    hostname = https://www.transifex.com
    username = YOURUSERNAME
    password = YOURPASSWORD
    token =
    ```

   If you want to test (new) translations and don't have a Transifex login, but think there's a new translation available, please file an issue on GitHub, for someone updating .po files in repository.

4. ```python bin/compile_translations.py``` (no matter, if you pulled new .po files; .mo files are no longer maintained in repository)

5. Test translations locally by clicking randomly on pages and languages. If everything is alright, continue; else: contact Daniela.

6. If you added new languages, add them to the local git repository

7. Commit (.po), push + create pull request to have the translations enter the repository for final deployment by Felix (message him!)

   Please try to keep .po and code changes in separate commits, if not related to each other.
   I.e. if you update .po and change unrelated source code, please submit in 2 commits.
   If you, OTOH, update .po in connection with source code making use of the change in .po, please consider submitting in 1 commit.
   It helps us to keep overview :)
