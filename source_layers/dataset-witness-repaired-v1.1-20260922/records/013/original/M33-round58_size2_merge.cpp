#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
#pragma pack(push,1)
struct O{int32_t d6;int16_t dr;int16_t pad;uint64_t plus,minus;};
#pragma pack(pop)
struct R{ifstream in;O z{};bool ok=false;R(const string&f):in(f,ios::binary){adv();}void adv(){ok=(bool)in.read((char*)&z,sizeof(z));}};
struct N{int32_t d6;int16_t dr;int i;bool operator>(const N&o)const{return tie(d6,dr)>tie(o.d6,o.dr);}};
int main(int ac,char**av){vector<R>r;for(int i=1;i<ac;i++)r.emplace_back(av[i]);priority_queue<N,vector<N>,greater<N>>q;for(int i=0;i<(int)r.size();i++)if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});uint64_t keys=0,plus=0,minus=0,M=0,both=0,maxm=0;while(!q.empty()){int d6=q.top().d6,dr=q.top().dr;uint64_t p=0,m=0;vector<int>ids;while(!q.empty()&&q.top().d6==d6&&q.top().dr==dr){int i=q.top().i;q.pop();p+=r[i].z.plus;m+=r[i].z.minus;ids.push_back(i);}keys++;plus+=p;minus+=m;uint64_t mm=min(p,m);M+=mm;if(mm){both++;maxm=max(maxm,mm);}for(int i:ids){r[i].adv();if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});}}
cout<<"keys "<<keys<<" plus "<<plus<<" minus "<<minus<<" M "<<M<<" bothkeys "<<both<<" maxm "<<maxm<<"\n";}
