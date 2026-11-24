" Learning log
# Learning log

## Week 1, Session 1 (November 16, 2026)

**What I did**
- Installed VS Code and learned to work in its built-in terminal.
- Practiced six basic commands for moving around and creating files.
- Confirmed Git was installed.
- In GitHub, made my email address private and blocked command-line pushes that would expose it.
- Told Git who I am (name and private email) and set the main branch name to "main."

**Commands learned**
- pwd: print working directory (shows which folder I am in)
- ls: list what is in a folder
- ls -la ~: list everything in my home folder, including hidden files, with details
- cd: change directory (move into a folder)
- mkdir: make directory (create a folder)
- touch: create an empty file with the name I give it
- clear: wipe the terminal panel so it is easier to read (does not delete any files)

**What broke, and how I fixed it**
- Nothing broke.

**What I learned**
- A folder path is the full address of a folder, such as /Users/wlittman/projects. The ~ symbol is shorthand for my home folder.
- Next focus: connecting each short command to its full name, so the commands become second nature.

**In one sentence**
I can tell the machine what to do, rather than clicking through what the machine has set in place.

## Week 1, Session 2 (November 17, 2026)

**What I did**
- Turned a practice folder into a Git repository and made seven commits.
- Practiced the full loop: save, check, stage, commit.
- Viewed changes side by side in VS Code's Source Control panel.
- Fixed the message of my most recent commit with git commit --amend.

**What broke, and how I fixed it**
- Typed q at the normal prompt and got "command not found." Learned that q only exits Git's reading mode.
- Opened a read-only comparison view and could not edit it. Learned it shows the committed version, and closed the tab.

**What I learned**
- Staging marks a changed file to go into the next commit. Committing saves that snapshot permanently in the repository's history.
- The full loop: save the file, git status to check what changed, git add to stage it, git commit -m "message" to save the snapshot.
- Good commit messages start with an action word in the present tense ("Add," "Fix") and describe what the change does. Several of my practice messages did not, which taught me why it matters: a clear history is easier for me and others to read.
- git commit --amend replaces the most recent commit, but only before it has been pushed.
- The q key exits Git's reading mode (when I see : or END). At the normal prompt, it is not a command.

**In one sentence**
Git saves a dated snapshot of my work every time I commit, with a note saying what changed, so I can see the whole history and go back.

## Week 1, Session 3 (November 18, 2026)

**What I did**
- Installed the GitHub command-line tool (gh) and signed it in to my account.
- Created a portfolio folder and copied in four builds: the contract review playbook, the NDA evaluation rubric, the AI vendor scanner, and the weekly regulatory watch.
- Left out the HubSpot terms PDF, because it is HubSpot's document; the README will link to their public page instead.
- Exported the NDA rubric from Claude as Markdown and moved it into the portfolio.
- Added a .gitignore file so secret-key files and Mac system files are never published.
- Ran a safety check for secrets before publishing. Every match was a key name, code that reads keys from the environment, or the scanner's own detection logic. No actual keys.
- Made the first commit and published the portfolio as a public GitHub repository.

**What broke, and how I fixed it**
- Downloaded GitHub Copilot by mistake instead of the command-line tool. Recognized it, quit without signing in, and installed the correct tool from GitHub's official releases page.
- macOS blocked the installer as unverified. Confirmed it came from GitHub's official page, then allowed it in Privacy & Security.
- Mistyped a folder name (fernway-test instead of fernway-tests). Fixed it with the Up arrow and Tab completion.
- Copied a folder without -R, which only works for files. Added -R.
- The publish command failed on the --source option. Retyped it carefully as --source=. and it worked.

**What I learned**
- cp copies a file; cp -R copies a folder and everything inside it (recursive).
- rm deletes immediately, with no Trash, so I check the path before pressing Return.
- A trailing slash on a folder name can change what cp copies.
- The rubric said to keep test cases private, which conflicts with publishing it. I updated the note to explain the trade-off: public test cases can end up in AI training data, so scores on a published case are illustrative only.

**In one sentence**
Today I published a portfolio of my legal AI work from the command line, checking first that nothing private or belonging to someone else went public.

## Week 1, Session 4 (November 19, 2026)

**What I did**
- Created a branch (add-readmes) and wrote a README for each build in my portfolio.
- Pushed the branch to GitHub, opened a pull request, reviewed the changes, and merged it into main.
- Created a GitHub profile introduction using a repository named after my username (wlittman).
- Added a one-line bio to my GitHub profile and pinned my portfolio.

**What broke, and how I fixed it**
- In VS Code's Open Folder window, my README file was grayed out. Learned that the window only selects folders, and opened the folder itself.
- A commit page on GitHub showed my README as raw text. Learned that commit pages show the raw changes, while the normal file view formats the Markdown.
- Skipped the pull request review at first. Went back and reviewed the merged pull request's "Files changed" tab.
- Several files had been committed before I saved my edits, including .gitignore, which was empty in the first commit. Found them with git status, checked each with git diff, confirmed no .DS_Store files had been published, fixed a typo (.DS-Store instead of .DS_Store), and committed the saved versions.

**What I learned**
- A branch is not a folder. It is a separate line of history; Git swaps the files in the same folder to match the branch I am on.
- A pull request is a proposal to merge changes from a branch into main. It lets a team review a change before it is merged.
- Reviewing the "Files changed" tab is like reviewing a redline: every addition and deletion is marked, I review it before accepting it, and the history keeps a permanent record.
- origin is the standard name for a project's GitHub copy. The GitHub tool set it up for me when I created the repository.
- git push -u links a local branch to its GitHub twin, so later pushes and pulls know where to go.
- I can stage only some changes by naming specific files with git add, instead of staging everything with git add .
- Git only sees saved changes. Always save with ⌘S before committing, and watch for the dot on a file's tab.
- Run git status before every commit. It caught changes I did not know were there.

**In one sentence**
Today I learned to propose, review, and accept changes the way software teams do, and I gave my GitHub profile a professional introduction.

## Week 2, Session 1 (November 23, 2026)

- Learned the eight core Python ideas the agent is built from: variables, strings (text), lists, dictionaries, `if`, loops, functions and reading files. Also previewed APIs, tokens, JSON and schemas (a fixed, predictable format for answers).
- A virtual environment is a private toolbox of packages for one project. It differs from my sandbox, which is a scratch folder for my own practice files: a virtual environment keeps each project's tools separate, while the sandbox keeps my experiments separate.
- Checked my Python version and installed the current release.
- Created a separate repository for the Contract Intake Agent, apart from my portfolio.
- Created and saved `.gitignore` before the first commit, to keep `.env`, `.venv/`, `__pycache__/` and `.DS_Store` off GitHub. Confirmed with `cat .gitignore` and `git status`.
- Created and activated the virtual environment, and installed the Python extension for VS Code.
- Wrote my first program, `hello.py`, using variables and an f-string, then committed it and published the repository to GitHub.
- What broke: nothing unexpected. I broke `hello.py` on purpose by deleting a closing quotation mark, read the `SyntaxError: unterminated string literal` message, and fixed it.

**Questions**

1. A variable is a labeled box that holds a value, like a defined term in a contract. Unlike a defined term, its value can be changed later in the program.
2. The error message named the problem (an unterminated string literal, meaning text that was opened but never closed) and the line where it happened, so I knew what to fix.

## Week 2, Session 2 (November 24, 2026)

- Made a plain-text copy of the Project Falcon NDA with the Mac's `textutil` tool, so Python could read it.
- Built `nda_basics.py` in four parts, running and checking each part before adding the next:
  - Part A: read the NDA from a file and counted its words (2,334).
  - Part B: checked for five key terms using a list, a loop, and `if`/`else`.
  - Part C: stored the results in a dictionary, pairing each term with True or False.
  - Part D: packaged the check as a reusable function, `check_terms`, and confirmed it gives the same result as Part C.
- Added comments to `nda_basics.py` and `hello.py` explaining each section in my own words, then committed and pushed.
- What I learned about word matching:
  - False negative: the check reported "return or destroy" as not found, but the NDA has a Return and Destruction clause worded differently ("return to the Disclosing Party or destroy").
  - False positive: "term" was reported as found, but those letters appear inside many words ("terms," "determine," "terminate"), so the result proves little.
  - Word matching sees letters, not meaning. It cannot reliably find clauses, and it cannot judge whether a clause meets my playbook. That is why Session 4 uses Claude.

**Questions**

1. A list is an ordered collection of items in square brackets, such as `["confidential", "residuals"]`. A dictionary pairs labels with values in curly braces, such as `{"confidential": True}`, like a filled-in form.
2. Indentation shows which lines belong to the line above, such as the steps inside a loop or an `if`. Python requires it, so wrong indentation causes an error.
3. I predicted "return or destroy" would be found, because the NDA has a Return and Destruction clause. It was a false negative: the clause uses different wording, so the exact-phrase check missed it.

