# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 22:06:07 2017

@author: Mathias Berg
"""


t,b,f,c = raw_input().strip().split(' ')
t,b,f,c = [int(t),int(b),int(f),int(c)]
# your code goes here

n=t+1
bf=max(b,f)
if bf>(n-1)*(n-2)/2:
  print -1
elif bf>(n-2)*(n-3)/2 and c>0:
  print -1
elif c>(n-1)*(n-2):
  print -1
else:
  # chain for bf (except root)
  i=2
  while i*(i-1)/2<bf:
    i+=1
  if i*(n-i-1)*2<c:
    print -1
  else:
    edg=[set([]) for _ in xrange(n+1)]
    # adding tree edges
    for j in xrange(1,i+1):
      edg[j].add(j+1)
    for j in xrange(i+2,n+1):
      edg[1].add(j)
    # adding forward edges
    j=1
    k=3
    while b>0:
      edg[k].add(j)
      b-=1
      if k<i+1:
        k+=1
      else:
        j+=1
        k=j+2
    j=1
    k=3
    while f>0:
      edg[j].add(k)
      f-=1
      if k<i+1:
        k+=1
      else:
        j+=1
        k=j+2
    j=2
    k=i+2
    while c>0:
      edg[j].add(k)
      c-=1
      if c>0:
        edg[k]=j
        c-=1
      if k<n:
        k+=1
      else:
        j+=1
        k=i+2
    print n
    for j in xrange(1,n+1):
      print len(edg[j]),
      for num in edg[j]:
        print num,
      print  