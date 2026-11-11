# Source context 1

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/004/original/M01-round-06-response.md`

Original SHA-256: `9fb8abbde279c6c61c9294fa24f57a84ed140e921eeacb056c83cf88f885e55d`

Original lines: 836–1065.

836	q=m(A-1)=9(1+\eta)^2>9.
837	$$
838	
839	Then
840	
841	$$
842	A=1+\frac qm,
843	\qquad
844	2m\log\left(1+\frac qm\right)<\log m.
845	\tag{9.1}
846	$$
847	
848	Every admissible tuple must produce real variables
849	
850	$$
851	D,\alpha,r,u,v,n,\tau,i,a,b,h,x
852	$$
853	
854	satisfying the following.
855	
856	## 9.1 Dimension and one-copy constraints
857	
858	$$
859	D\in\mathbb N,
860	\qquad
861	D>m,
862	$$
863	
864	$$
865	\boxed{
866	\frac{D^2}{m}
867	\le
868	\alpha
869	\le
870	\frac{AD(D+1)}{m}-D
871	<
872	D^2.
873	}
874	\tag{9.2}
875	$$
876	
877	Also
878	
879	$$
880	r=\frac{\alpha}{D},
881	\quad
882	u=\alpha-1,
883	\quad
884	v=D-r,
885	\quad
886	n=D^2-1.
887	$$
888	
889	## 9.2 Mixing and block positivity
890	
891	$$
892	\boxed{
893	Dr^2\le\tau\le\sqrt A\,Dr^2.
894	}
895	\tag{9.3}
896	$$
897	
898	Define
899	
900	$$
901	h=\frac{\tau}{D}-r^2\ge0.
902	$$
903	
904	Positivity of
905	
906	$$
907	J=
908	\begin{pmatrix}r&z^*\\z&B\end{pmatrix}
909	$$
910	
911	implies
912	
913	$$
914	B\succeq\frac{zz^*}{r}.
915	$$
916	
917	Hence
918	
919	$$
920	\boxed{
921	h\le rv,
922	\qquad
923	a\ge\frac{h^2}{r^2}.
924	}
925	\tag{9.4}
926	$$
927	
928	## 9.3 Trace-purity and rank constraints
929	
930	$$
931	b=i-1,
932	\qquad
933	a=i-\frac{2\tau}{D}+r^2.
934	$$
935	
936	For \(P\),
937	
938	$$
939	\boxed{
940	\frac{u^2}{n}\le b\le u.
941	}
942	\tag{9.5}
943	$$
944	
945	For \(B\),
946	
947	$$
948	\boxed{
949	\frac{v^2}{m(m-1)}
950	\le a\le v^2.
951	}
952	\tag{9.6}
953	$$
954	
955	Contraction adds
956	
957	$$
958	\boxed{i\le\alpha.}
959	\tag{9.7}
960	$$
961	
962	## 9.4 Alignment bounds
963	
964	Define
965	
966	$$
967	H_{\rm cen}
968	=
969	\frac{uv}{n}
970	+
971	\sqrt{
972	\left(a-\frac{v^2}{n}\right)
973	\left(b-\frac{u^2}{n}\right)
974	}.
975	\tag{9.8}
976	$$
977	
978	Then
979	
980	$$
981	\boxed{
982	0\le x
983	\le
984	\min\left\{
985	H_{\rm cen},
986	\epsilon(D^2-\alpha),
987	v,
988	i-r
989	\right\}.
990	}
991	\tag{9.9}
992	$$
993	
994	Here:
995	
996	* \(x\le v\) follows from \(0\le P\le I\);
997	* \(x\le i-r\) follows from \(r+x=\operatorname{Tr}(JS)\le i\).
998	
999	## 9.5 Exact symmetric-Bell endpoints
1000	
1001	Define
1002	
1003	$$
1004	\begin{aligned}
1005	\gamma_{\rm req}(i,\tau)
1006	={}&
1007	(D+2)i+(D+1)\tau\\
1008	&+\frac12B_0(D,\alpha)\\
1009	&-
1010	\frac{A}{2m}
1011	\alpha D(D+1)(D+3),
1012	\end{aligned}
1013	\tag{9.10}
1014	$$
1015	
1016	and
1017	
1018	$$
1019	\begin{aligned}
1020	\gamma_{\rm up}(i,\tau)
1021	=\frac12\Bigg[
1022	&\frac{A}{m}
1023	(\alpha+D)(D+2)(D+3)\\
1024	&-
1025	\left(
1026	D^2+4D+\alpha^2+2(D+4)\alpha
1027	\right)\\
1028	&-2i-4\tau
1029	\Bigg].
1030	\end{aligned}
1031	\tag{9.11}
1032	$$
1033	
1034	Then
1035	
1036	$$
1037	\boxed{
1038	\gamma_{\rm req}(i,\tau)
1039	\le r+x
1040	\le
1041	\gamma_{\rm up}(i,\tau).
1042	}
1043	\tag{9.12}
1044	$$
1045	
1046	Equivalently, scalar feasibility requires
1047	
1048	$$
1049	\boxed{
1050	\max\{0,\gamma_{\rm req}-r\}
1051	\le x
1052	\le
1053	\min\{
1054	H_{\rm cen},
1055	\epsilon(D^2-\alpha),
1056	v,
1057	i-r,
1058	\gamma_{\rm up}-r
1059	\}.
1060	}
1061	\tag{9.13}
1062	$$
1063	
1064	No lower bound on \(i\) or \(\tau\) has been substituted inside a nonmonotone expression in this system.
1065	
