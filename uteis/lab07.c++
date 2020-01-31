#include <bits/stdc++.h>
using namespace std;
int combo, hit=0, vr=0, vk=0, ryu=50, ken=50;
void get_combo(int r, int k, int h){
  int x, aux, sum=h;
  if(h>0) aux=1;
  else if(h<0) aux=-1;
  else aux=0;
  while(r+sum>0 and k-sum>0){
    cin >> x;
    sum+=x;
    //cout << x*aux << endl;
    if(x*aux<0){
      hit=x;
      combo=sum-x;
      //cout << hit << " " << combo << endl;
      return;
    }
    if(x>0) aux=1;
    else aux=-1;
  }
  hit=0;
  combo=sum;
  if(r+sum<=0) vk++;
  else vr++;
}
int main(){
  while(vk+vr<2){
    get_combo(ryu, ken, hit);
    if(combo>0) {
      cout << "Ken: " << ken << " - " << combo << " = " << ken-combo<< endl;
      ken-=combo;
    }
    else {
      cout << "Ryu: " << ryu << " - " << -combo << " = "<< ryu+combo << endl;
      ryu+=combo;
    }
    if(ken<=0 or ryu<=0) ken=50, ryu=50;
  }
  if(vr==2) cout << "Ryu ganhou";
  else if (vk==2) cout << "Ken ganhou";
  else cout << "empatou";
  return 0;
}
