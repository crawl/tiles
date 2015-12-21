from git import *
repo = Repo("/Users/christopherhamons/Programming/crawl-ref/")
assert repo.bare == False

tree = repo.heads.master.commit.tree
iterator = tree.trees[0]["source"]["rltiles"].traverse()

authors = []
commits = []

for x in iterator:
   fullPath = "/Users/christopherhamons/Programming/crawl-ref/"+x.path
   print fullPath
   history =  repo.git.log("--format=short", fullPath)
   for line in history.split('\n'):
      if line.startswith("Author:"):
         if line not in authors:
            authors.append(line)
      if line.startswith("    "):
         if line not in commits:
            commits.append(line)
   print
print authors
print commits