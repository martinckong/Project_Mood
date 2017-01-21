import tone2

count = 1
totalsongs = 10

while count <= totalsongs:
    tone2.runscript("file%d" % count, "output%d.txt" % count)
    count += 1
