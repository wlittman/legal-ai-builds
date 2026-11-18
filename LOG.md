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
