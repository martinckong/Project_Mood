import tone2

count = 1
totalsongs = 1

while count <= totalsongs:
    tone2.runscript("file%d" % count, "outputdir/output%d.txt" % count)
    count += 1
