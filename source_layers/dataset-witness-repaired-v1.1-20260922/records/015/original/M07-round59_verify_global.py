#!/usr/bin/env python3
import argparse, numpy as np
p=argparse.ArgumentParser();p.add_argument('path');a=p.parse_args()
dt=np.dtype([('d6','<i4'),('dr','<i2'),('pad','<i2'),('plus','<u8'),('minus','<u8')])
x=np.memmap(a.path,dtype=dt,mode='r')
keys=len(x); plus=minus=matches=both=maxm=0; c1=0;c2=0
chunk=200_000
idx=1
for lo in range(0,keys,chunk):
    z=x[lo:lo+chunk]
    ps=z['plus'].astype(object); ns=z['minus'].astype(object)
    plus += sum(ps); minus += sum(ns)
    ms=[min(int(pp),int(nn)) for pp,nn in zip(ps,ns)]
    matches += sum(ms); both += sum(1 for v in ms if v); maxm=max(maxm,max(ms,default=0))
    for d6,dr,pp,nn in zip(z['d6'],z['dr'],ps,ns):
        base=(int(d6)<<16)|((int(dr)+32768)&0xffff)
        c1 += idx*base
        c2 += idx*(3*int(pp)+5*int(nn))
        idx += 1
print('keys',keys)
print('plus',plus)
print('minus',minus)
print('matches',matches)
print('bothkeys',both)
print('maxm',maxm)
print('checksum_index_base',c1)
print('checksum_index_3p5n',c2)
