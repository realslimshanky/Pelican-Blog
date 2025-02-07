Title: Recovering commit after git reset --hard
Date: 2018-03-21
Modified: 2018-03-26
Category: Git
Tags: Git, VCS, Linux
Slug: recovering-commit-after-git-reset--hard
Authors: Shashank Kumar
Summary: An hour left for project demonstration and while making few important changes you did something very veerryy aweful. It's --hard to recover but not impossible. This is how you can get the commit back from hell.
Cover: images/recovering-commit-after-git-reset--hard.png

##### Problem statement

One not-so-fine day when you are working on your project and do a `git reset --hard HEAD~n` because, well, you skipped breakfast, your brain is not working properly and you don't want to take the high road of debugging commits. You sadly lost some of your important commits and you forgot to create a backup branch.

Before we move on, if you don't know what `git reset` do checkout [this documentation](https://git-scm.com/docs/git-reset).

##### Where do the commit go?

After you do `git reset --hard HEAD~n` the current branch's HEAD is placed to the requested commit i.e. `HEAD~n` and all the top level commits which were made afterwards are discarded or become 'dangling object' in the eyes of Git. Now, Git places dangling object inside `.git/lost-found/` directory. Phew, it's a relief to know that Git is not deleting anything permanently even though it's not present in any of the branches. All we have to learn is how to probe further and get the commit back.

##### Option 1 - reflog

[Reference logs](https://git-scm.com/docs/git-reflog) or reflogs keeps a log of changes happening with project with respect to the tip of all the branches. So whenever you are adding a new commit, checking out another branch etc. reflogs are updated.

That means, reflog must have peeked while we were busy screwing up the project and can help us out in telling us what exactly we did. By doing a simple `git reflog` you might see something simliar of a structure.

```
04fa8ba HEAD@{0}: reset: moving to HEAD~1
aab9d00 HEAD@{1}: commit: just add it okay
```

The log is maintained in reverse chronological order and hence `HEAD@{0}` becomes the latest activity we did and it is exactly where we messed up i.e. `reset: moving to HEAD~1`. If you go a little further down you'll find the `commit:` with the message you gave. This is our dangling commit we were looking all around for. The important thing to notice here is the short hash i.e. `aab9d00` in above case. Now simply do a `git reset --hard aab9d00` by replacing `aab9d00` with your short hash for the commit and you'll find yourself back in time where no one knows you did anything wrong ;)

##### Option 2 - fsck

[`fsck`](https://git-scm.com/docs/git-fsck) checks the objects present inside Git database i.e. it probes whether or not something messy happened inside `.git` directory of your repository. Since we already know that dangling commits are saved inside `.git/lost-found/` we can use `fsck` to find out more about them. Doing a `git fsck --lost-found` will result in something similar to the following result.

```
Checking object directories: 100% (256/256), done.
dangling commit aab9d002015a9bb8d4f66c2e378a7da5f7077e0c
dangling commit 9489726b0d165d4a18c677f703e4dc757617781a
```

Here, `fsck` is first checking the database and then because of the flag we gave i.e. `--lost-found` it goes on and prints the dangling objects. In above case we have 2 `dangling commit` which might happen something if you have been mischievous for more than one time. No worries, let's look inside individual commits and see why they were created using `git show aab9d002015a9bb8d4f66c2e378a7da5f7077e0c`. You have to replace 3rd argument or long hash i.e. `aab9d002015a9bb8d4f66c2e378a7da5f7077e0c` evertime to probe individual dangling commits. It'll show you something similar to the result below.

```
Author: Shashank Kumar <abc@shanky.xyz>
Date:   Tue Mar 20 23:53:33 2018 +0530

    addind new file

diff --git a/n b/n
new file mode 100644
index 0000000..b14df64
--- /dev/null
+++ b/n
@@ -0,0 +1 @@
+Hi
```

We get a very descriptive message with `git show` which contains date, time, commit message and diff in the commit. After you get the commit you were looking for, simply repeat the process but this time with long hash i.e. `git reset --hard aab9d002015a9bb8d4f66c2e378a7da5f7077e0c`. Phew!

##### Conclusion

- Shit go wrong all the time
- Hack all you want for all you need your machine to do
- An Open Source software just saved you from spending a lot of money on data recovery. Embrace it!
