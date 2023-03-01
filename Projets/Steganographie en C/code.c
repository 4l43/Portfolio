#include <stdlib.h>
#include <stdio.h>

struct header {
    char type[2];
    int taille;
    int offset;
    int hauteur;
	int longueur;
    int BitsParPixls;
    int padding;

};

typedef struct header header;


int hexDec(unsigned char tab[4]){
	int nb = 0, i = sizeof(int)-1;
	for (i = sizeof(int)-1; i>=0;i--){
		nb = nb*256+tab[i];
    }
	return nb;
}

//lecture de l'entete :
header lecture_header(char nom[]){
    header h;
    unsigned char temp[4];
    FILE *img=NULL;
    img = fopen(nom,"rb");
    
    fread(temp,sizeof(char)*2,1,img);
    h.type[0]=temp[0];
    h.type[1]=temp[1];

    fread(temp,sizeof(int),1,img);
    h.taille=hexDec(temp);
    
    fseek(img,10,SEEK_SET);
    fread(temp,sizeof(int),1,img);
    h.offset=hexDec(temp);
    
    fseek(img,18,SEEK_SET);
    fread(temp,sizeof(int),1,img);
    h.longueur=hexDec(temp);
    h.hauteur=fread(&temp,sizeof(int),1,img);
    h.hauteur=hexDec(temp);
    

    fseek(img,28,SEEK_SET);
    fread(temp,sizeof(int),1,img);
    h.BitsParPixls=hexDec(temp);

    h.padding = h.hauteur%4;

    fclose(img);
    

    return h;
}

int hide(){
		
    //demandons à l'utilisateur le fichier à modifier 
    char nom[40];
    printf("Entrer le nom du fichier a modifier : \n");
    scanf("%s",nom);
    
    
	header h = lecture_header(nom);
	int tailleMAX = (h.longueur * h.hauteur)/3/4;

	//demandons la chaine de caracter a cacher
	char *phrase = malloc(sizeof(char)*tailleMAX);
	int *phraseBin = malloc(sizeof(int)*tailleMAX);
	printf("Entrer la phrase a cacher \n max %d cahracteres : \n ",tailleMAX*4);
	scanf("%s",phrase);
	
	
	//transformons la chaine en binaire
	int i= 0,j=0,temp;
	do {
	for (int z=7;z>=0;z--){
            temp=phrase[j]>>z&1;
            
            if(z%2!=0 && temp == 1){
				phraseBin[i]=2;
			} 
			
			if(z%2!=0 && temp == 0){
				phraseBin[i]=0;
			} 
			
            if(z%2==0 && temp == 1){
				phraseBin[i]=phraseBin[i]+1;
				i++;
			} 
            
			if(z%2==0 && temp == 0){
				phraseBin[i]=phraseBin[i];
				i++;
			} 
        }
        j++;
	}while(i!= tailleMAX);
    
    //steganoggraphions !!
    stegano(nom,phraseBin);	
	
	return 0;
	}



int stegano(char nom[],int *tabcode){
   header h;
   h= lecture_header(nom);
   FILE *img=NULL;
   img = fopen(nom,"rb");
   //fichier ou l'on va appliquer la stegano :
   FILE *img2=NULL;
   img2 = fopen("fichier_stega.bmp","wb");

   //copions l'image dans un tableau 
   int i;
   int *tab1 = malloc(sizeof(int)*h.taille);
   
   for (i = 0; i < h.taille; i++){
      tab1[i] = fgetc(img);
   }


   //applicons la stegano:
   int j=0,L=0,k=0;

   for(i = h.offset-1; i < h.taille; i=i+h.padding){
         for(L = 1; L<=h.longueur; L++){
            i=i+3;
            for(k=0;k<4;k++){
				if(tabcode[j]==k){
					tab1[i] = ((tab1[i]%4)*4)+k;
				}
            }
            j++;
         }
   }

	for (i = 0; i < h.taille; i++){
		  fprintf(img2,"%c",tab1[i]);
	   }

	free (tab1);
	fclose (img);
	fclose (img2);
	return 0;
}

int main(){
    hide();
    return 0;
}
