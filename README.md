Living review to be built inputing smaller text files to the skeleton of the living review: review_msm.tex.

# Using git and GitHub

If you need to: create an account in github and learn the basics with the [basic github resources](https://help.github.com/articles/git-and-github-learning-resources/), [tryGit](https://try.github.io/levels/1/challenges/1) and [a cheat sheet](https://zeroturnaround.com/rebellabs/git-commands-and-best-practices-cheat-sheet/).

Github provides free account upgrades to students and anyone working at a educational/research institute, which allow you to have your own private repositories. To get this upgrade, once you have a personal account, go to this page and fill in the form: https://education.github.com/discount_requests/new

The recommended steps to contribute to the Living review repository are:

1. Fork and clone: Get a copy of the GitHub repository 
1. Update your personal copy
1. Track upstream: keeping your copy up-to-date with the main one
1. Steps to follow when working on a new (big) feature: Branch, Contribute, Commit, (Merge) and Push.
1. Submit a Pull Request to the main repository.

## Fork and clone: Get a copy of the Living Review from the GitHub repository 

Once you have your GitHub account and are familiar with the basic git vocabulary, create your own copy of the repository:

1. Go to https://github.com/FaradayInstitution/msm_living_review/

2. Click 'Fork' there (right upper corner).
 
The next step is to get a copy of the review into your computer:

1. Open git-bash where you want to clone the repository.

2. Clone there your repository. From your OWN local repository (below change [git username] by your github username:

```   
>  git clone https://[git username]@github.com/[git username]/msm_living_review/
```

You'll be prompt for your GitHub username and password.

## Updating your review copy.

Ensure that the remote is the correct one: 
```
> git remote -v
```

If you need to reset the remote link:
```
> git remote set-url origin https://[git username]@github.com/[git username]/msm_living_review
```
   
Update your personal copy:

```
> git push origin master
```

## Track upstream: keeping your copy up-to-date with the main one

This instructions follow the recommendations on [syncing a fork from GitHub](ttps://help.github.com/articles/syncing-a-fork/). To make sure that your version remains up to date with
the master version, set the upstream tracking:

```
> git remote add --track master upstream https://[username]@github.com/FaradayInstitution/msm_living_review/
```

Now, every time you need to apply the changes that have been made to the master version to yours, open git-bash at your directory with the review and run:

```
> git fetch upstream
> git merge upstream/master
```

## Working on a new (big) feature

### Branch, contribute and Commit

To start working on new feature, create a separate feature branch:

    git checkout -b feature

You can check the branches you have by:

    git branch

And switch between them with:

    git checkout master
    git checkout feature

Once some changes have been made in the branch, stage them
and commit:

    git add .
    git commit -m "Add a comment here"

### (Merge and) Push

You can push changes with:

    git push origin feature

Alternatively, you can merge the changes with the master
branch first, and then push:

    git checkout master
    git merge feature
    git push origin master

## Submit a Pull Request

When you are ready to update the main Living review code, go to your GitHub msm_living_review page, click "New pull request" to create a Pull Request from your
latest commit. It will be applied by someone with
administrator master version  rights after review.
