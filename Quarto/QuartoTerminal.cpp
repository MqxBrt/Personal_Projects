#include <iostream>
#include <cmath>
using namespace std;

//variables globales
int pieces[16];
int choixpiece;
int valid;
int cases[16];
int choixcase;
bool tour=true;
//true=j1; false=j2
int totaltour=0;
  //quand =16, fin jeu sur égalité


void affpi(int p)
{if (p>8) {cout<<"(N ";} else {cout<<"(B ";};
  if ((p<5)||((p>8)&&(p<13))) {cout<<"━ ";} else {cout<<"✚ ";};
  if ((p==3)||(p==4)||(p==7)||(p==8)||(p==11)||(p==12)||(p==15)||(p==16)) {cout<<"▅ ";} else {cout<<"● ";};
  if (p%2==0)  {cout<<"✘)";} else {cout<<"✔)";};
}



void affcas(int cases[16])
{for (int k=0; k<64; k++) {cout<<"-";}; cout<<endl;
  for (int i=0; i<16; i++)
    {int a=cases[i];
      if (a==0&&i<9) {cout<<"|     "<<i+1<<"     |    ";}
      else if (a==0) {cout<<"|     "<<i+1<<"    |    ";}
      else if (a<10) {cout<<"| "; affpi(a); cout<<" |    ";}
      else {cout<<"| "; affpi(a); cout<<" |    ";};
      if ((i+1)%4==0) {cout<<endl;
        for (int k=0; k<64; k++) {cout<<"-";};
        cout<<endl;
      };
    };
}
        


void legende(int pieces[16])
{cout<<" "<<endl;
    cout<<"Legende des pieces : "<<endl;
    cout<<"--------------------"<<endl;
    cout<<"B/N : Blanche/Noire,     ✚/━ : Grande/Petite,    ▅/● : Carrée/Ronde,    ✔/✘ : Pleine/Trouée"<<endl;
    cout<<" "<<endl;
  for (int i=0; i<16; i++)
    {int p=i+1;
      if (pieces[i]==1)
        {
          affpi(p);
        cout<<" : "<<p<<"   ";
        if (p<10) {cout<<" ";};
        if (p%4==0) {cout<<endl<<endl;};
        }
      else if (p%4==0) {cout<<endl<<endl;}
      else if (p<10) {cout<<"                 ";}
      else {cout<<"                 ";};
    };
}


 
//regarde si la pièce est disponible
void checkpiece(int *choixpiece)
{while (pieces[*choixpiece-1]==0 ||  (*choixpiece)<1 || (*choixpiece)>16)
{std::cout<<"Cette piece est deja utilisee ou non valide"<<std::endl;
  std::cin>>*choixpiece;};}


//regarde si la case n'est pas occupée
void checkcase(int *choixcase)
{while (cases[*choixcase-1]!=0 || (*choixcase)<1 || (*choixcase)>16)
{std::cout<<"Cette case est deja utilisee ou non valide"<<std::endl;
  std::cin>>*choixcase;};}


//converti un entier <16 en binaire
int conv(int a)
{a--;
int b=0;
    if (a/8==1) {b+=1000; a=a%8;};
    if (a/4==1) {b+=100; a=a%4;};
    if (a/2==1) {b+=10; a=a%2;};
    if (a/1==1) {b+=1;};
return b;}



//fonction qui regarde si les pieces ont AU MOINS 1 particularité identique
bool commun(int a, int b, int c, int d)
{if (a==0 || b==0 || c==0 || d==0) {return false;};
a=conv(a);
b=conv(b);
c=conv(c);
d=conv(d);
for (int i=0; i<4; i++) {
        if ((a%2==b%2)&&(a%2==c%2)&&(a%2==d%2)) {return true;};
        a/=10;
        b/=10;
        c/=10;
        d/=10;};
 
return false;}



//check de victoire sur les 10 alignements possibles
bool checkwin(int cases[16],int pieces[16])
{    //lignes
if (commun(cases[0],cases[1],cases[2],cases[3])) {return true;};
if (commun(cases[4],cases[5],cases[6],cases[7])) {return true;};
if (commun(cases[8],cases[9],cases[10],cases[11])) {return true;};
if (commun(cases[12],cases[13],cases[14],cases[15])) {return true;};
        //colonnes
if (commun(cases[0],cases[4],cases[8],cases[12])) {return true;};
if (commun(cases[1],cases[5],cases[9],cases[13])) {return true;};
if (commun(cases[2],cases[6],cases[10],cases[14])) {return true;};
if (commun(cases[3],cases[7],cases[11],cases[15])) {return true;};
        //diagonnales
if (commun(cases[0],cases[5],cases[10],cases[15])) {return true;};
if (commun(cases[3],cases[6],cases[9],cases[12])) {return true;};
return false;}



//permet de dire à l'utilisateur la forme de la pièce
void forme(int p)
{if (p>8) {std::cout<<"noire, ";} else {std::cout<<"blanche, ";};
  if ((p<5)||((p>8)&&(p<13))) {std::cout<<"petite, ";} else {std::cout<<"grande, ";};
  if ((p==3)||(p==4)||(p==7)||(p==8)||(p==11)||(p==12)||(p==15)||(p==16)) {std::cout<<"carree, ";} else {std::cout<<"ronde, ";};
  if (p%2==0)  {std::cout<<"et trouee."<<std::endl;} else {std::cout<<"et pleine."<<std::endl;};
}



int main()
//initialise les tableaux (cases vides et pièces disponibles)
{for (int i=0; i<16; i++) {pieces[i]=1;};
  for (int i=0; i<16; i++) {cases[i]=0;};
 system("clear");
  cout<<endl<<endl<<endl;
  affcas(cases);
  cout<<endl;
  legende(pieces);


  
//déroulement de la partie tant que personne n'a gagné ou que le plateau n'est pas plein
  while (totaltour<16 && !checkwin(cases, pieces))
    {
      cout<<endl<<"* Debut du tour "<<totaltour+1<<" *"<<endl<<endl;
  //partie 1, choix de la pièce
  if (tour) {cout<<"Joueur 1, choissisez la piece pour le joueur 2 : ";}
  else {cout<<"Joueur 2, choissisez la piece pour le joueur 1 : ";};
  //validation de la pièce choisie
  cin>>choixpiece;
  valid=choixpiece;
  do {choixpiece=valid;
  checkpiece(&choixpiece);
  cout<<"Vous avez choisis la piece ";
  forme(choixpiece);
  cout<<"Pour valider, entrez de nouveau le numero choisis : ";
  cin>>valid;}
  while (valid!=choixpiece);
  pieces[choixpiece-1]=0;

  cout<<endl;
  tour=!tour;
  //partie 2, placement de la pièce
    if (tour) {cout<<"Joueur 1, choissisez la case ou poser la piece : ";}
    else {cout<<"Joueur 2, choissisez la case ou poser la piece : ";};
  cin>>choixcase;
  checkcase(&choixcase);
  cases[choixcase-1]=choixpiece;

  system("clear");
  cout<<endl<<endl<<endl;
  affcas(cases);
  cout<<endl;
  legende(pieces);
  
  totaltour++;
  };


    //fin de la partie
  system("clear");
  cout<<endl<<endl<<endl;
  affcas(cases);
  cout<<endl;
    if (totaltour>15) {cout<<"Egalite ! Le plateau est plein."<<endl;}
    else if (tour) {cout<<"Le Joueur 1 remporte la partie";}
    else {cout<<"Le Joueur 2 remporte la partie";};
    cout<<endl<<endl;
  }

