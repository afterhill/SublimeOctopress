import sublime, sublime_plugin
import datetime
import pinyin

header = '''---
layout: post
categories: blog
date: dummy_date
comments: true
author: Meng Jue
website: b.imf.cc
title: dummy_title
---
'''


def make_pinyin(title_input):
    p = pinyin.Pinyin()
    return p.get_pinyin(title_input)


def replace_with_real_title(title, header2):
    header3 = header2.replace('dummy_title', title)
    return header3


def replace_with_real_datetime():
    now1 = datetime.datetime.now()
    target_string = now1.strftime('%Y-%m-%d %H:%M:%S')
    header2 = header.replace('dummy_date', target_string)
    return header2


def make_post_date():
    now = datetime.datetime.now()
    file_date = now.strftime("%Y-%m-%d")
    return file_date


def make_file_name(title_input):
    jek_date = make_post_date()
    jek_title = make_pinyin(title_input)
    # jek_title = title_input.lower().replace(' ', '-')
    jek_file_type = '.md'
    jek_post_title = jek_date + '-' + jek_title + jek_file_type
    return jek_post_title


class MakeOctopressPostCommand(sublime_plugin.WindowCommand):
    def on_done(self, title):
        header2 = replace_with_real_datetime()
        header3 = replace_with_real_title(title, header2)
        new_post = self.window.new_file()
        post_title = make_file_name(title)
        new_post.set_name(post_title)
        edit = new_post.begin_edit()
        new_post.insert(edit, 0, header3)
        new_post.end_edit(edit)

    def run(self):
        self.window.show_input_panel("Post Title:", "", self.on_done, None, None)
