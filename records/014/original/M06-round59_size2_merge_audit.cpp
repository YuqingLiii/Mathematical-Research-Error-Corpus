#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <queue>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
#pragma pack(push,1)
struct O{int32_t d6;int16_t dr;int16_t pad;uint64_t plus,minus;};
#pragma pack(pop)
static_assert(sizeof(O)==24);
struct R{ifstream in;O z{};bool ok=false;R(const string&f):in(f,ios::binary){adv();}void adv(){ok=(bool)in.read((char*)&z,sizeof(z));}};
struct N{int32_t d6;int16_t dr;int i;bool operator>(const N&o)const{return tie(d6,dr)>tie(o.d6,o.dr);}};
struct Top{uint64_t m,p,n;int32_t d6;int16_t dr;array<uint64_t,13> pp{},mm{};};
string s128(unsigned __int128 x){if(!x)return"0";string s;while(x){s.push_back('0'+x%10);x/=10;}reverse(s.begin(),s.end());return s;}
int main(int ac,char**av){
 if(ac<15){cerr<<"usage: out.bin row0.keys ... row12.keys\n";return 1;}
 string outpath=av[1]; vector<R>r;for(int i=2;i<ac;i++)r.emplace_back(av[i]); if(r.size()!=13){cerr<<"need 13 rows\n";return 2;}
 ofstream out(outpath,ios::binary|ios::trunc);
 priority_queue<N,vector<N>,greater<N>>q;for(int i=0;i<13;i++)if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});
 uint64_t keys=0,plus=0,minus=0,M=0,both=0,maxm=0; unsigned __int128 chkbase=0,chkpn=0; vector<Top>top;
 while(!q.empty()){
  int32_t d6=q.top().d6;int16_t dr=q.top().dr;uint64_t p=0,m=0;array<uint64_t,13>pp{},mm{};vector<int>ids;
  while(!q.empty()&&q.top().d6==d6&&q.top().dr==dr){int i=q.top().i;q.pop();p+=r[i].z.plus;m+=r[i].z.minus;pp[i]=r[i].z.plus;mm[i]=r[i].z.minus;ids.push_back(i);}
  O z{d6,dr,0,p,m};out.write((char*)&z,sizeof(z));keys++;plus+=p;minus+=m;uint64_t mt=min(p,m);M+=mt;if(mt){both++;maxm=max(maxm,mt);top.push_back({mt,p,m,d6,dr,pp,mm});if(top.size()>80){nth_element(top.begin(),top.begin()+40,top.end(),[](auto&a,auto&b){return a.m>b.m;});top.resize(40);}}
  uint64_t base=((uint64_t)(uint32_t)d6<<16)|(uint16_t)((int)dr+32768); chkbase+=(unsigned __int128)keys*base; chkpn+=(unsigned __int128)keys*(3*(unsigned __int128)p+5*(unsigned __int128)m);
  for(int i:ids){r[i].adv();if(r[i].ok)q.push({r[i].z.d6,r[i].z.dr,i});}
 }
 out.close();sort(top.begin(),top.end(),[](auto&a,auto&b){return a.m>b.m;});
 cout<<"keys "<<keys<<" plus "<<plus<<" minus "<<minus<<" M "<<M<<" bothkeys "<<both<<" maxm "<<maxm<<"\n";
 cout<<"checksum_index_base "<<s128(chkbase)<<"\n";
 cout<<"checksum_index_3p5n "<<s128(chkpn)<<"\n";
 for(size_t k=0;k<min<size_t>(top.size(),20);k++){auto&z=top[k];cout<<"KEY "<<z.d6<<" "<<z.dr<<" match "<<z.m<<" plus "<<z.p<<" minus "<<z.n<<"\nP";for(auto x:z.pp)cout<<" "<<x;cout<<"\nM";for(auto x:z.mm)cout<<" "<<x;cout<<"\n";}
}
