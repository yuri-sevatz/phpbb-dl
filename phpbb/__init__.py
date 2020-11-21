#!/usr/bin/env python
from cvm.dom import Selector
from cvm.view import Field, View, Page, Group


class Login(Page):
    def __init__(self):
        self.username = Field(Selector.CSS, "input[name=login]")
        self.password = Field(Selector.CSS, "input[name=password]")
        self.submit = Field(Selector.XPATH, ".//button[span[text() = 'Log in']]")


class Index(Page):
    def __init__(self):
        self.threads = Group(ForumItem(Selector.CSS, ".node-body"))


class ForumItem(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.title = Field(Selector.CSS, ".node-main .node-title a")
        self.time = Field(Selector.CSS, ".node-extra time")


class Forum(Page):
    def __init__(self):
        self.title = Field(Selector.CSS, '.p-title')
        self.topics = Group(TopicItem(Selector.CSS, ".js-threadList .structItem"))
        self.nav = Nav(Selector.CSS, ".pageNav")


class TopicItem(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.title = Field(Selector.CSS, ".structItem-title a:not(.labelLink)")
        self.time = Field(Selector.CSS, ".structItem-cell--latest time")


class Topic(Page):
    def __init__(self):
        self.title = Field(Selector.CSS, '.p-title')
        self.posts = Group(Post(Selector.CSS, ".message--post"))
        self.nav = Nav(Selector.CSS, ".pageNav")


class Post(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.time = Field(Selector.CSS, ".message-attribution time")
        self.body = Group(Field(Selector.CSS, ".message-body"))
        self.attachments = Group(Attachment(Selector.CSS, ".message-attachments .attachment"))
        self.videos = Group(Video(Selector.CSS, ".message-body .bbMediaWrapper video"))


class Attachment(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.filename = Field(Selector.CSS, ".attachment-name")
        self.download = Field(Selector.CSS, ".attachment-name a")
        self.preview = Field(Selector.TAG, ".attachment-icon")


class Video(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.source = Field(selector.CSS, "source")


class Nav(View):
    def __init__(self, selector: Selector, value: str):
        super().__init__(selector, value)
        self.first = Field(Selector.CSS, ".pageNav-page:first-of-type a")
        self.prev = Field(Selector.CSS, "a.pageNav-jump.pageNav-jump--prev")
        self.next = Field(Selector.CSS, "a.pageNav-jump.pageNav-jump--next")
        self.last = Field(Selector.CSS, ".pageNav-page:last-of-type a")
