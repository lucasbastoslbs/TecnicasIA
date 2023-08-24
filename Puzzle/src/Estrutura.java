
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Matriz{
    int dimensao;
    int matriz[][];
    int linha;
    int coluna;
    public Matriz(int n){
        this.dimensao = n;
        matriz = new int[n][n];
        this.inicializa();
    }
    
    public Matriz cloneMat(){
        Matriz nova = new Matriz(this.dimensao);
        for(int i = 0;i < this.dimensao;i++){
            for(int j = 0; j < this.dimensao; j++){
                nova.matriz[i][j] = this.matriz[i][j];
            }
        }
        nova.dimensao = this.dimensao;
        nova.linha = this.linha;
        nova.coluna = this.coluna;
        return nova;
    }
    
    public int[][] clonar(){
        int nova[][] = new int[this.dimensao][this.dimensao];
        for(int i = 0;i < this.dimensao;i++){
            for(int j = 0; j < this.dimensao; j++){
                nova[i][j] = this.matriz[i][j];
            }
        }
        return nova;
    }
    
    public void cima(){
        if(this.linha == 0) return;
        this.matriz[linha][coluna] = this.matriz[linha-1][coluna];
        this.matriz[linha--][coluna] = 0;
    }
    
    public void baixo(){
        if(this.linha == this.dimensao-1) return;
        this.matriz[linha][coluna] = this.matriz[linha+1][coluna];
        this.matriz[linha++][coluna] = 0;
    }
    
    public void esquerda(){
        if(this.coluna == 0) return;
        this.matriz[linha][coluna] = this.matriz[linha][coluna-1];
        this.matriz[linha][coluna--] = 0;
    }
    
    public void direita(){
        if(this.coluna == this.dimensao-1) return;
        this.matriz[linha][coluna] = this.matriz[linha][coluna+1];
        this.matriz[linha][coluna++] = 0;
    }
    
    public void exibir(){
        for(int i = 0; i < this.dimensao; i++){
            for(int j = 0; j < this.dimensao; j++){
                System.out.print(this.matriz[i][j]+"\t");
            }
            System.out.println("");
        }
        System.out.println("\n0 = ["+this.linha+","+this.coluna+"]");
    }
    
    public void inicializa(){
        ArrayList<Integer> lista = new ArrayList<Integer>();
        for(int i = 0; i < this.dimensao*this.dimensao;i++){
            lista.add(i);
        }
        Collections.shuffle(lista);        
        for(int i = 0; i < this.dimensao; i++){
            for(int j = 0; j < this.dimensao; j++){
                this.matriz[i][j] = lista.get((i*this.dimensao) + j);
                if(this.matriz[i][j] == 0){
                    this.linha = i;
                    this.coluna = j;
                }
            }
        }
    }
}

public class Estrutura {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);        
        System.out.println("Dimensão da matriz: ");        
        int dimensao = teclado.nextInt();
        Matriz mat = new Matriz(dimensao);
        mat.exibir();
        mat.direita();
        mat.exibir();
    }
}
