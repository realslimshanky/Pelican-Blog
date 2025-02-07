Title: Google Summer of Code 2018 with Debian - Final Report
Date: 2018-08-13
Modified: 2018-08-13
Category: GSoC
Tags: GSoC, Google, Debian, KIVY, Salsa
Slug: gsoc-2018-final-report
Authors: Shashank Kumar
Summary: Three weeks of Google Summer of Code went off to be life-changing for me. I learned a lot about soft skills and project management as well. This here is the summary of my work which also serves as my Final Report of Google Summer of Code 2018.
Cover: /images/gsocanddebian.png

Three weeks of Google Summer of Code went off to be life-changing for me. This here is the summary of my work which also serves as my Final Report of Google Summer of Code 2018.

![GSoC and Debian]({static}/images/gsocanddebian.png)

### Preperations

My project is **Wizard/GUI helping students/interns apply and get started** and the final application is named **New Contributor Wizard**. It originated as the brainchild and Project Idea of [Daniel Pocock](https://wiki.debian.org/SummerOfCode2018/Projects/WizardForStudentsAndNewInterns) for GSoC 2018 under Debian. I prepared the application task for the same and shared my journey through Open Source till GSoC 2018 in two of my blogs, [**From Preparations to Debian to Proposal**](https://blog.shanky.xyz/gsoc-2018-blog-1-from-preparations-to-debian-proposal.html#gsoc-2018-blog-1-from-preparations-to-debian-proposal) and [**The Application Task and Results**](https://blog.shanky.xyz/gsoc-2018-blog-2-the-application-task-and-results.html#gsoc-2018-blog-2-the-application-task-and-results).

### Project Overview

![Sign Up Screen]({static}/images/gsoc-final-report-application-screen-signup.png)

New Contributor Wizard is a GUI application build to help new contributors get started with Open Source. It was an idea to bring together all the Tools and Tutorials necessary for a person to learn and start contributing to Open Source. The application contains different courseware sections like `Communication`, `Version Control System` etc. and within each section, there are respective Tools and Tutorials.

A Tool is an up and running service right inside the application which can perform tasks to help the user understand the concepts. For example, encrypting a message using the primary key, decrypting the encrypted message using the private key, and so on, these tools can help the user better understand the concepts of encryption.

A tutorial is comprised of lessons which contain text, images, questions and code snippets. It is a comprehensive guide for a particular concept. For example, Encryption 101, How to use git?, What is a mailing list? and so on.

In addition to providing the Tools and Tutorials, this application is build to be progressive. One can easily contribute new Tutorials by just creating a JSON file, the process of which is documented in the project repository itself. Similarly, a documentation for contributing Tools is present as well.

### Project Details

- **GSoC Project Page** - [GSoC Projects #5056989357408256](https://summerofcode.withgoogle.com/projects/#5056989357408256)

- **Project Respository** - [New Contributor Wizard on Debian Salsa](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard)

- **Issue/Bug Tracker** - [New Contributor Wizard on Debian Redmine](https://outreach-lab.debian.net/redmine/projects/new-contributor-wizard)

- **Communication** - Private thread with mentors for daily updates, [Debian Outreach Mailing List](https://lists.debian.org/debian-outreach/) for weekly updates and [Jitsi Meet](https://meet.jit.si) for conference calls.

### Programming Language and Tools

**For Development**

- [Python](https://docs.python.org)
- [Kivy](https://kivy.org/docs)
- [Request](http://docs.python-requests.org/en/master)
- [Python GnuPG](https://pythonhosted.org/python-gnupg)
- [Cython](http://docs.cython.org/en/latest)

**For Testing**

- [Pylint](https://pylint.readthedocs.io/en/latest)
- [Pytest](https://docs.pytest.org/en/latest)
- [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest)
- [IPDB](https://github.com/gotcha/ipdb)

**Environment**

- [Pipenv](https://docs.pipenv.org/) for Python Virtual Environment
- [Debian 9](https://wiki.debian.org/DebianStretch) for Project Development and testing

**Version Control System**

- [Git](https://git-scm.com/)

For pinned dependencies and sub-dependencies one can have a look at the [Pipfile](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/blob/master/Pipfile) and [Pipfile.lock](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/blob/master/Pipfile.lock)

### My Contributions

The project was just an idea before GSoC and I had to make all the decisions for the implementation with the help of mentors whether it was Design or Architecture of the application. Below is the list of my contributions in shape of merge requests and every merge request contains UI, application logic, tests, and documentation. My contributions can also be seen in [**Changelog**](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/blob/master/changelog) and [**Contribution Graph**](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/graphs/master) of the application.

##### Sign Up

Sign Up is the first screen a user is shown and asks for all the information required to create an account. It then takes the user to the Dashboard with all the courseware sections.

**Merge request** - [Adds SignUp feature](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/4)

**Redmine Issue** - [Create SignUp Feature](https://outreach-lab.debian.net/redmine/issues/8)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_signup.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Sign In

Alternate to Sign Up, the user has option to select Sign In to use existing account in order to access the application.

**Merge Request** - [Adds SignIn feature](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/5)

**Redmine Issue** - [Create SignIn Feature](https://outreach-lab.debian.net/redmine/issues/9)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_signin.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Dashboard

The Dashboard is said to be the protagonist screen of the application. It contains all the courseware sessions and their respective Tools and Tutorials.

**Merge Request** - [Adds Dashboard feature](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/6)

**Redmine Issue** - [Implementing Dashboard](https://outreach-lab.debian.net/redmine/issues/25)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_dashboard.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding Tool Architecture

Every courseware section can have respective Tools and Tutorials. To add Tools to a section I devised an architecture and implemented on `Encryption` to add 4 different Tools. They are:

- Create Key Pair
- Display and manage Key Pair
- Encrypt a message
- Decrypt a message

**Merge Request** - [Adding encryption tools](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/7)

**Redmine Issue** - [Adding Encryption Tools](https://outreach-lab.debian.net/redmine/issues/28)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_encryption_tools.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding Tutorial Architecture

Similar to Tools, Tutorials can be found with respect to any courseware section. I have created a Tutorial Parser, which can take a JSON file and build GUI for the Tutorial easily without any coding required. This way folks can easily contribute Tutorials to the project. I added `Encryption 101` Tutorial to showcase the use of Tutorial Parser.

**Merge Request** - [Adding encryption tutorials](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/9)

**Redmine Issue** - [Adding Encryption Tutorials](https://outreach-lab.debian.net/redmine/issues/31)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_encryption_tutorials.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding 'Invite Contributor' block to Tools and Tutorials

In order to invite the contributor to New Contributor Wizard, every Tools and Tutorials menu display an additional block by linking the project repository.

**Merge Request** - [Inviting contributors](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/10)

**Redmine Issue** - [Inviting contributors to the project](https://outreach-lab.debian.net/redmine/issues/54)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_invite_contributors.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding How To Use

One of the courseware section `How To Use` help the user understand about different sections of the application in order to get the best out of it.

**Merge Request** - [Updating How To Use](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/15)

**Redmine Issue** - [Adding How To Use in the application ](https://outreach-lab.debian.net/redmine/issues/53)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_how_to_use.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding description to all the modules

All the courseware sections or modules need a simple description to describe what the user will learn using it's Tutorials and Tools.

**Merge Request** - [Description added to all the modules](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/20)

**Redmine Issue** - [Add a introduction/description to all the modules](https://outreach-lab.debian.net/redmine/issues/57)

**Feature In Action** (updated working of the feature)

<video width="400" controls loop>
  <source src="{static}/videos/GSoC_final_description_to_all_modules.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

##### Adding Generic Tools and Tutorials Menu

This feature allows the abstraction of Tools and Tutorials architecture I mentioned earlier so that the Menu architecture can be used by any of the courseware sections following the DRY approach.

**Merge Request** - [Adding Generic Menu](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/13)

**Redmine Issue** - [Adding Tutorial and Tools menu to all the modules](https://outreach-lab.debian.net/redmine/issues/49)

##### Tutorial Contribution Doc

A tutorial in the application can be added using just a JSON file. As mentioned earlier, it is made possible using the Tutorial Parser. A comprehensive ocumentation is added to help the users understand how they can contribute Tutorials to the application for the world to take advantage of.

**Merge Request** - [Tutorial contribution docs](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/16)

**Redmine Issue** - [Add documentation for Tutorial development](https://outreach-lab.debian.net/redmine/issues/45)

##### Tools Contribution Doc

A tool in the application is build using Kivy lang and Python. A comprehensive documentation is added to the project in order for folks to contribute Tools for the world to take advantage of.

**Merge Request** - [Tools contribution docs](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/17)

**Redmine Issue** - [Add documentation for Tools development](https://outreach-lab.debian.net/redmine/issues/44)

##### Adding a License to project

After having discussions with the mentors and a bit of research, GNU GPLv3 was finalized as the license for the project and has been added to the repository.

**Merge Request** - [Adds License to project](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/11)

**Redmine Issue** - [Add a license to Project Repository](https://outreach-lab.debian.net/redmine/issues/10)

##### Allowing different timezones during Sign Up

Sign Up feature is refactored to support different timezones from the user.

**Merge Request** - [Allowing different timezones during signup](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests/18)

**Redmine Issue** - [Allow different timezones](https://outreach-lab.debian.net/redmine/issues/56)

##### All other contributions

Here's a list of all the merge request I raised to develop a feature or fix an issue with the application - [All merge request by Shashank Kumar](https://salsa.debian.org/new-contributor-wizard-team/new-contributor-wizard/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=realslimshanky-guest)

Here are all the issues/bug/features I created, resolved or was associated to on the Redmine - [All the redmine issue associated to Shashank Kumar](https://outreach-lab.debian.net/redmine/projects/new-contributor-wizard/issues?utf8=%E2%9C%93&set_filter=1&f%5B%5D=status_id&op%5Bstatus_id%5D=o&f%5B%5D=assigned_to_id&op%5Bassigned_to_id%5D=%3D&v%5Bassigned_to_id%5D%5B%5D=8&f%5B%5D=&c%5B%5D=tracker&c%5B%5D=status&c%5B%5D=priority&c%5B%5D=subject&c%5B%5D=assigned_to&c%5B%5D=updated_on&group_by=&t%5B%5D=)

### Packaging

The application has been packaged for PyPi and can be installed using either `pip` or `pipenv`.

Package - [new-contributor-wizard](https://pypi.org/project/new-contributor-wizard/)

Packaging Tool - [setuptools](https://pypi.org/project/setuptools/)

### To Do List

- [Add more tools and tutorials to the project](https://outreach-lab.debian.net/redmine/issues/59)
- [GUI popup for text manipulation in input boxes throughout the application](https://outreach-lab.debian.net/redmine/issues/55)
- [Packaging the application for Debian after the Kivy package for python3 is upgraded](https://outreach-lab.debian.net/redmine/issues/60)

### Weekly Updates And Reports

These report were send daily to private mentors mail thread and weekly on Debian Outreach mailing list.

- [Week 1 and 2](https://lists.debian.org/debian-outreach/2018/05/msg00069.html)
- [Week 3](https://salsa.debian.org/snippets/126)
- [Week 4](https://salsa.debian.org/snippets/127)
- [Week 5](https://salsa.debian.org/snippets/128)
- [Week 6](https://salsa.debian.org/snippets/129)
- [Week 7](https://salsa.debian.org/snippets/130)
- [Week 8](https://salsa.debian.org/snippets/131)
- [Week 9](https://salsa.debian.org/snippets/132)
- [Week 10](https://salsa.debian.org/snippets/133)
- [Week 11](https://salsa.debian.org/snippets/134)
- [Week 12](https://salsa.debian.org/snippets/135)

### Talk Delivered On My GSoC Project

On 12th August 2018, I gave a talk on **How my Google Summer of Code project can help bring new contributors to Open Source** during a meetup in Hacker Space, Noida, India. Here are the [slides](https://slides.com/realslimshanky/gsoc) I prepared for my talk and a collection of [photographs](https://drive.google.com/folderview?id=1Dcpbw0QsmW8OL8B5XYbmov83A7k8dbeM) of the event.

### Summary

New Contributor Wizard is ready for the users who would like to get started with Open Source as well as to the folks who would like to contribute Tools and Tutorials to the application as well.

### Acknowledgment

I would like to thank Google Summer of Code for giving me the opportunity of giving back to the community and Debian for selecting me for the project.

I would like to thank [Daniel Pocock](https://danielpocock.com/) for his amazing blogs and ideas he comes up which end up inspiring students and result in a project like above.

I would like to thank [Sanyam Khurana](https://www.sanyamkhurana.com/) for constantly motivating me by reviewing every single line of code which I wrote to come up with the best solution to put in front of the community.

Thanks to all the loved ones who always believed in me and kept me motivated.
