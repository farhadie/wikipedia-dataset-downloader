#!/usr/bin/env python
import sys, codecs, re
import wikipedia
from multiprocessing import Process


def func(part, total):
    write = codecs.open("output"+str(part), "w", "utf-8")
    read = open("train.id", 'r').readlines()
    start = (part-1) * len(read) / total
    end = (part * len(read) / total)
    err_cntr = 0
    for page_id in read[start:end]:
        try:
            x = wikipedia.page(pageid=page_id)
            content = x.content
        except:
            err_cntr +=1
            print("page not found: "+ page_id)
            continue
        content = re.sub(r'(?s)(\n\n\n=+ (?!Personal life|Early life|Background|Childhood|Birth|Biography).+? ==).*?((?=\n\n\n==)|$)', '', content)
        content = re.sub(r'(?s)(\n+=+ .+? =+)', '', content)
        content = re.sub(r'\n+', ' ', content)
        content = re.sub(r' +', ' ', content)
        write.write(page_id[:-1] + '\t' + content + '\n')
    print("total error: " + str(err_cntr))

if __name__ == '__main__':
    process = []
    parts = int(sys.argv[1])
    for i in range(1, 1 + parts):
        process.append(Process(target=func, args=(i, parts)))
    for proc in process:
        proc.start()
    for proc in process:
        proc.join()

