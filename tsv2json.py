f = open("articles.json", 'w')
with open("articles.tsv", "r") as ins:
    array = []
    for line in ins:
        l = line.split('\t')
        f.write(r'{"doc_id": "%s", "content": "%s"}' % (l[0], l[1][:-1].replace(r'"', r'\"').replace(r"\'", r"'")))
        f.write('\n')
f.close()