#include <algorithm>
#include <array>
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
struct Top{uint64_t m,p,n;int32_t d6;int16_t dr;array<uint64_t,13> pp,mm;};
int main(int ac,char**av){vector<R>r;for(int i=1;i<ac;i++)r.emplace_back(av[i]);priority_queue<N,vector<N>,greater<N>>q;for(int i=0;i<(int)r.size();i++)if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});uint64_t keys=0,plus=0,minus=0,M=0,both=0,maxm=0;vector<Top>top;while(!q.empty()){int d6=q.top().d6,dr=q.top().dr;uint64_t p=0,m=0;array<uint64_t,13>pp{},mm{};vector<int>ids;while(!q.empty()&&q.top().d6==d6&&q.top().dr==dr){int i=q.top().i;q.pop();p+=r[i].z.plus;m+=r[i].z.minus;pp[i]=r[i].z.plus;mm[i]=r[i].z.minus;ids.push_back(i);}keys++;plus+=p;minus+=m;uint64_t z=min(p,m);M+=z;if(z){both++;maxm=max(maxm,z);top.push_back({z,p,m,(int32_t)d6,(int16_t)dr,pp,mm});if(top.size()>50){nth_element(top.begin(),top.begin()+25,top.end(),[](auto&a,auto&b){return a.m>b.m;});top.resize(25);}}for(int i:ids){r[i].adv();if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});}}
sort(top.begin(),top.end(),[](auto&a,auto&b){return a.m>b.m;});cout<<"keys "<<keys<<" plus "<<plus<<" minus "<<minus<<" M "<<M<<" bothkeys "<<both<<" maxm "<<maxm<<"\n";for(size_t k=0;k<min<size_t>(top.size(),20);k++){auto&z=top[k];cout<<"KEY "<<z.d6<<" "<<z.dr<<" match "<<z.m<<" plus "<<z.p<<" minus "<<z.n<<"\nP";for(auto x:z.pp)cout<<" "<<x;cout<<"\nM";for(auto x:z.mm)cout<<" "<<x;cout<<"\n";}}
