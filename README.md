##SublimeOctopress

Tools for working with Octopress in Sublime Text 2

###Installation
* Install [Package Control](http://wbond.net/sublime_packages/package_control/installation) and restart when it tells you to.
    * Add Repository - https://github.com/mengjuesh/SublimeOctopress
    * Install Package - SublimeOctopress

###Current capabilities:
* make a new post : supply a title and get back a new document with really conventional Jekyll filename and yaml header (based on octopress)
    * command palette = Octopress: New Post
    * Tools > Octopress > New Post

###Feature

* generate conventional Jekyll filename with chinese and english combination:    

```     
before:(you just type the article title as below)
简单才是最美Simple is The Best

After:(plugin will generate the Jekyll/Octopress conventionally file for you)
jian-dan-cai-shi-zui-mei-simple-is-the-best.md
```

* populate the Jekyll YAML header in the fresh file

```
---
layout: post
categories: blog
date: 2013-01-05 05:36:25
comments: true
author: Meng Jue
website: b.imf.cc
---
```

###References
*   [glenrobertson's PythonOpenModule](https://github.com/SublimeText/PythonOpenModule) for general organization and user prompt creation.
*   [titoBouzout's Camaleon](https://github.com/SublimeText/Camaleon) for menu nesting.
*   [Sublime Text 2 API docs](http://www.sublimetext.com/docs/2/api_reference.html)
*   [SublimeJekyll](https://github.com/mengjuesh/SublimeJekyll)
*   [xpinyin](https://github.com/lxneng/xpinyin)

Contact: MengJue (AT) outlook.com
