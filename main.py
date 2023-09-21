import os

from NetscapeBookmarksFileParser import (
    creator, NetscapeBookmarksFile, BookmarkShortcut, BookmarkFolder,
    BookmarkItem
)

from github import Auth, Github


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

bookmarks = NetscapeBookmarksFile()
final = creator.create_file(bookmarks)

item = BookmarkItem()
item.name = "untitled"
folder = BookmarkFolder(item)

for star in g.get_user().get_starred():

    bmk_shrt = BookmarkShortcut()
    bmk_shrt.name = star.name
    bmk_shrt.href = star.html_url
    bmk_shrt.tags = star.topics
    bmk_shrt.comment = star.description

    if star.archived:
        bmk_shrt.tags.append("archived")

    folder.items.append(bmk_shrt)

final = final + creator.folder_creator(folder)

print("".join(final))
