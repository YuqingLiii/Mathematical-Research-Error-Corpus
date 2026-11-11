#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
#pragma pack(push,1)
struct S2{int32_t t,d6;int16_t dr;int8_t q,s;uint32_t pad;};
struct O{int32_t d6;int16_t dr;int16_t pad;uint64_t plus,minus;};
#pragma pack(pop)
int main(int ac,char**av){if(ac<3)return 1;ifstream in(av[1],ios::binary|ios::ate);size_t n=(size_t)in.tellg()/sizeof(S2);in.seekg(0);vector<S2>a(n);in.read((char*)a.data(),n*sizeof(S2));sort(a.begin(),a.end(),[](auto&x,auto&y){return tie(x.d6,x.dr,x.s)<tie(y.d6,y.dr,y.s);});ofstream out(av[2],ios::binary|ios::trunc);size_t i=0;uint64_t keys=0,M=0,pl=0,mi=0;while(i<n){int d6=a[i].d6,dr=a[i].dr;uint64_t p=0,m=0;while(i<n&&a[i].d6==d6&&a[i].dr==dr){if(a[i].s>0)p++;else m++;i++;}O z{d6,(int16_t)dr,0,p,m};out.write((char*)&z,sizeof(z));keys++;M+=min(p,m);pl+=p;mi+=m;}cout<<"records "<<n<<" keys "<<keys<<" plus "<<pl<<" minus "<<mi<<" M "<<M<<"\n";}
