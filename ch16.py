from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.lgbayesiannetwork import LGBayesianNetwork
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.pgmlearner import PGMLearner
from libpgm.tablecpdfactorization import TableCPDFactorization
import json
import math
import sys

if len(sys.argv) != 2:  # the program name and the datafile
  # stop the program and print an error message
  sys.exit("usage: ch16.py datafile.txt ")

filename = sys.argv[1]

try:
    f = open(filename, 'r') # opens the input file
except IOError:
    print ("Cannot open file %s" % filename)
    sys.exit("BYE!")

#load data
nd = NodeData()
skel = GraphSkeleton()
nd.load(filename)
skel.load(filename)
#load B Network
skel.toporder()
bn = DiscreteBayesianNetwork(skel, nd)

#set up function
jp=[]
temp=[]
cal=[]
#initiralization
sc={}
for i in range(len(bn.V)):
    sc[bn.V[i]]='0'
    temp.append(bn.V[i])
temp.append('p')
jp.append(temp)
temp=[]
val=['0','1']
node=len(bn.V)

#recursion
def recur(sc, temp, number, bn, val, jp):
    if number!=0:
        for i in range(2):
            sc[bn.V[len(bn.V)-number]]=val[i]
            recur(sc, temp, number-1, bn, val, jp)
    else:
        result=[]
        p=1
        temp=[]
        for j in range(len(bn.V)):
            pa=bn.Vdata[bn.V[j]]['parents']
            if pa:
                fn=TableCPDFactorization(bn)
                evidence={}
                for k in range(len(pa)):
                    evidence[pa[k]]=sc[pa[k]]
                query ={bn.V[j]:list(sc[bn.V[j]])}
                result.append(fn.specificquery(query, evidence))
            else:
                if sc[bn.V[j]]=='0':
                    result.append(bn.Vdata[bn.V[j]]['cprob'][0])
                else:
                    result.append(bn.Vdata[bn.V[j]]['cprob'][1])
            temp.append(sc[bn.V[j]])
            p=p*result[j]
        temp.append(p)
        jp.append(temp)
        #temp=[]

recur(sc,temp,node,bn,val,jp)
for i in range(len(jp)):
    print(jp[i])
