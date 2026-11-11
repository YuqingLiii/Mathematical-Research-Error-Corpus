#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstring>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <thread>
#include <tuple>
#include <vector>
using namespace std; namespace fs=std::filesystem;
static constexpr array<int,10> slopes={3,1,20,-20,490,-490,12090,-12090,300187,-300187};
static constexpr int TMIN=-3800000, TMAX=3800000, TN=TMAX-TMIN+1;
#pragma pack(push,1)
struct GH{int32_t t;uint8_t count;uint8_t pad[3];};
struct PL{int32_t Q;int8_t sign;uint8_t pad[3];};
struct Stream2{int32_t t;int32_t dQ6;int16_t dQr;int8_t q;int8_t sigma;uint32_t pad;};
struct Stream3{int32_t t;int32_t dQ61;int32_t dQ62;int16_t dQr1;int16_t dQr2;int8_t q;uint8_t pattern;uint16_t pad;};
#pragma pack(pop)
static_assert(sizeof(GH)==8);static_assert(sizeof(PL)==8);static_assert(sizeof(Stream2)==16);static_assert(sizeof(Stream3)==20);
string path_for(const string&d,int x,int y){if(x>y)swap(x,y);return d+"/s_"+to_string(x)+"_"+to_string(y)+".bin";}
int parity_perm(const array<int,10>&p){int z=0;for(int i=0;i<10;i++)for(int j=i+1;j<10;j++)z+=p[i]>p[j];return z&1;}
void gen_subset(const string&path,const array<int,10>&R,vector<uint8_t>&cnt,vector<int32_t>&Qs,vector<int8_t>&Sg,vector<int32_t>&touch){
 touch.clear();array<int,10> p; iota(p.begin(),p.end(),0);
 do{int t=0,Q=0;for(int k=0;k<10;k++){int r=R[p[k]],s=slopes[k];t+=s*r;Q+=s*r*r;}int idx=t-TMIN;if(idx<0||idx>=TN){cerr<<"t range "<<t<<"\n";exit(9);}uint8_t c=cnt[idx];if(c==0)touch.push_back(idx);if(c<3){Qs[(size_t)idx*3+c]=Q;Sg[(size_t)idx*3+c]=parity_perm(p)?-1:1;}if(c<255)cnt[idx]=c+1;}while(next_permutation(p.begin(),p.end()));
 sort(touch.begin(),touch.end());ofstream out(path,ios::binary|ios::trunc);uint32_t n=touch.size();out.write((char*)&n,4);for(int idx:touch){GH g{idx+TMIN,cnt[idx],{0,0,0}};out.write((char*)&g,8);if(cnt[idx]<=3)for(int z=0;z<cnt[idx];z++){PL p1{Qs[(size_t)idx*3+z],Sg[(size_t)idx*3+z],{0,0,0}};out.write((char*)&p1,8);}cnt[idx]=0;}
}
struct Reader{ifstream in;uint32_t left=0;GH g{};PL p[3]{};bool ok=false;int x,y,ps;Reader(const string&f,int xx,int yy,int pss):in(f,ios::binary),x(xx),y(yy),ps(pss){in.read((char*)&left,4);adv();}void adv(){if(!left){ok=false;return;}in.read((char*)&g,8);if(g.count<=3)for(int z=0;z<g.count;z++)in.read((char*)&p[z],8);left--;ok=true;}};
int placement_sign(int del,int x,int y){vector<int> a;for(int r=0;r<13;r++)if(r!=del&&r!=x&&r!=y)a.push_back(r);a.push_back(x);a.push_back(y);vector<int>b;for(int r=0;r<13;r++)if(r!=del)b.push_back(r);array<int,13>pos{};for(int k=0;k<12;k++)pos[b[k]]=k;int inv=0;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++)inv+=pos[a[i]]>pos[a[j]];int s=(inv&1)?-1:1;if(del&1)s=-s;return s;}
struct Tot{vector<uint64_t>hist=vector<uint64_t>(1000);uint64_t s2=0,b2=0,m2=0,z2=0,s3=0,t3=0,b3=0,m3=0,z3=0;array<uint64_t,4>pat{};int min2a=INT32_MAX,max2a=INT32_MIN,min2b=999,max2b=-999,min3a=INT32_MAX,max3a=INT32_MIN,min3b=999,max3b=-999;};
Tot scanq(const string& dir,int del,int q,ofstream* o2,ofstream* o3){
    vector<Reader> r;
    for(int y=0;y<13;y++){
        int x=y+q;
        if(x<0||x>=13||x==del||y==del) continue;
        r.emplace_back(path_for(dir,x,y),x,y,placement_sign(del,x,y));
    }
    struct N{int t,k;bool operator>(const N&o)const{return t>o.t;}};
    priority_queue<N,vector<N>,greater<N>> pq;
    for(int k=0;k<(int)r.size();k++) if(r[k].ok) pq.push({r[k].g.t,k});
    Tot out;
    while(!pq.empty()){
        int t=pq.top().t;
        vector<int> ids;
        int n=0;
        while(!pq.empty()&&pq.top().t==t){
            int k=pq.top().k; pq.pop(); ids.push_back(k); n+=r[k].g.count;
        }
        if(n>=(int)out.hist.size()) out.hist.resize(n+1);
        out.hist[n]++;
        if(n==2||n==3){
            struct M{int Q,R,c;};
            array<M,3> m{};
            int nm=0;
            for(int k:ids) for(int z=0;z<r[k].g.count;z++){
                int Q=r[k].p[z].Q;
                int R=r[k].x*r[k].x-r[k].y*r[k].y;
                int c=r[k].p[z].sign*r[k].ps;
                bool f=false;
                for(int j=0;j<nm;j++) if(m[j].Q==Q&&m[j].R==R){m[j].c+=c;f=true;break;}
                if(!f) m[nm++]={Q,R,c};
            }
            int nn=0;
            for(int j=0;j<nm;j++) if(m[j].c) m[nn++]=m[j];
            nm=nn;
            sort(m.begin(),m.begin()+nm,[](auto&a,auto&b){return tie(a.Q,a.R)<tie(b.Q,b.R);});
            if(n==2){
                out.s2++;
                if(!nm) out.z2++;
                else if(nm==1) out.m2++;
                else{
                    int d6=m[1].Q-m[0].Q, dr=m[1].R-m[0].R, sg=m[0].c*m[1].c;
                    Stream2 z{t,d6,(int16_t)dr,(int8_t)q,(int8_t)sg,0};
                    if(o2) o2->write((char*)&z,sizeof(z));
                    out.b2++;
                    out.min2a=min(out.min2a,d6); out.max2a=max(out.max2a,d6);
                    out.min2b=min(out.min2b,dr); out.max2b=max(out.max2b,dr);
                }
            }else{
                out.s3++;
                if(!nm) out.z3++;
                else if(nm==1) out.m3++;
                else if(nm==2) out.b3++;
                else{
                    int pat=((m[1].c*m[0].c)<0?1:0)|((m[2].c*m[0].c)<0?2:0);
                    int a1=m[1].Q-m[0].Q, a2=m[2].Q-m[0].Q;
                    int r1=m[1].R-m[0].R, r2=m[2].R-m[0].R;
                    Stream3 z{t,a1,a2,(int16_t)r1,(int16_t)r2,(int8_t)q,(uint8_t)pat,0};
                    if(o3) o3->write((char*)&z,sizeof(z));
                    out.t3++; out.pat[pat]++;
                    out.min3a=min(out.min3a,min(a1,a2)); out.max3a=max(out.max3a,max(a1,a2));
                    out.min3b=min(out.min3b,min(r1,r2)); out.max3b=max(out.max3b,max(r1,r2));
                }
            }
        }
        for(int k:ids){r[k].adv(); if(r[k].ok) pq.push({r[k].g.t,k});}
    }
    return out;
}

int main(int argc,char**argv){if(argc<4){cerr<<"usage: del tempdir outdir\n";return 1;}int del=stoi(argv[1]);string dir=argv[2],outdir=argv[3];fs::create_directories(dir);fs::create_directories(outdir);vector<pair<int,int>>pairs;for(int x=0;x<13;x++)for(int y=x+1;y<13;y++)if(x!=del&&y!=del)pairs.push_back({x,y});atomic<int>nx{0};vector<thread>th;int nth=min(5,(int)thread::hardware_concurrency());auto t0=chrono::steady_clock::now(); bool scan_only=(getenv("SCAN_ONLY")!=nullptr); if(!scan_only) for(int z=0;z<nth;z++)th.emplace_back([&]{vector<uint8_t>cnt(TN);vector<int32_t>Qs((size_t)TN*3);vector<int8_t>Sg((size_t)TN*3);vector<int32_t>touch;touch.reserve(2000000);while(1){int k=nx++;if(k>=(int)pairs.size())break;auto[x,y]=pairs[k];array<int,10>R;int p=0;for(int rr=0;rr<13;rr++)if(rr!=del&&rr!=x&&rr!=y)R[p++]=rr;gen_subset(path_for(dir,x,y),R,cnt,Qs,Sg,touch);}});for(auto&t:th)t.join();auto t1=chrono::steady_clock::now();ofstream o2(outdir+"/s2_i"+to_string(del)+".bin",ios::binary|ios::trunc),o3(outdir+"/s3_i"+to_string(del)+".bin",ios::binary|ios::trunc);Tot A;for(int q=-12;q<=12;q++)if(q){Tot b=scanq(dir,del,q,&o2,&o3);if(b.hist.size()>A.hist.size())A.hist.resize(b.hist.size());for(size_t k=0;k<b.hist.size();k++)A.hist[k]+=b.hist[k];A.s2+=b.s2;A.b2+=b.b2;A.m2+=b.m2;A.z2+=b.z2;A.s3+=b.s3;A.t3+=b.t3;A.b3+=b.b3;A.m3+=b.m3;A.z3+=b.z3;for(int p=0;p<4;p++)A.pat[p]+=b.pat[p];A.min2a=min(A.min2a,b.min2a);A.max2a=max(A.max2a,b.max2a);A.min2b=min(A.min2b,b.min2b);A.max2b=max(A.max2b,b.max2b);A.min3a=min(A.min3a,b.min3a);A.max3a=max(A.max3a,b.max3a);A.min3b=min(A.min3b,b.min3b);A.max3b=max(A.max3b,b.max3b);}o2.close();o3.close();auto t2=chrono::steady_clock::now();cout<<"deleted "<<del<<" gen_sec "<<chrono::duration<double>(t1-t0).count()<<" scan_sec "<<chrono::duration<double>(t2-t1).count()<<"\n";uint64_t co=0,as=0;for(size_t k=1;k<A.hist.size();k++)if(A.hist[k]){cout<<"H "<<k<<" "<<A.hist[k]<<"\n";co+=A.hist[k];as+=k*A.hist[k];}cout<<"coords "<<co<<" assignments "<<as<<" size2 "<<A.s2<<" binom2 "<<A.b2<<" mono2 "<<A.m2<<" zero2 "<<A.z2<<"\n";cout<<"size3 "<<A.s3<<" tri3 "<<A.t3<<" binom21 "<<A.b3<<" mono3 "<<A.m3<<" zero3 "<<A.z3<<"\n";cout<<"tripat "<<A.pat[0]<<" "<<A.pat[1]<<" "<<A.pat[2]<<" "<<A.pat[3]<<"\n";cout<<"ranges2 "<<A.min2a<<" "<<A.max2a<<" "<<A.min2b<<" "<<A.max2b<<"\n";cout<<"ranges3 "<<A.min3a<<" "<<A.max3a<<" "<<A.min3b<<" "<<A.max3b<<"\n";for(auto[x,y]:pairs)fs::remove(path_for(dir,x,y));fs::remove(dir);}
