import busca.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Puzzle implements Estado{
    final int dimensao;
    final int matriz[][];
    int linha;
    int coluna;
    final String op;
    
    /**
     * Construtor para estado inicial
     * @param n - dimensao da matriz
     * @param op - verbose da transição
     */
    public Puzzle(int n, String op){
        this.dimensao = n;
        matriz = new int[n][n];
        this.op = op;
        inicializa();
    }
    
    /**
     * Construtor para os estados sucessores
     * @param matriz
     * @param linha
     * @param coluna
     * @param op 
     */
    public Puzzle(int [][] matriz, int linha, int coluna, String op){
        this.matriz = matriz;
        this.linha = linha;
        this.coluna = coluna;
        this.op = op;
        this.dimensao = matriz.length;
    }
    
    private void inicializa(){
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
    
    public int[][] clonar(){
        int nova[][] = new int[this.dimensao][this.dimensao];
        for(int i = 0;i < this.dimensao;i++){
            for(int j = 0; j < this.dimensao; j++){
                nova[i][j] = this.matriz[i][j];
            }
        }
        return nova;
    }
    
    public void cima(List<Estado> visitados){
        if(this.linha == 0) return;
        
        int matrizTmp[][] = this.clonar();
        
        matrizTmp[this.linha][coluna] = matrizTmp[this.linha-1][coluna];
        matrizTmp[this.linha-1][coluna] = 0;
        
        Puzzle novo = new Puzzle(matrizTmp, this.linha-1, this.coluna, "Indo para cima");
        
        if(!visitados.contains(novo)){
            visitados.add(novo);
        } else {
            System.gc();
        }
    }
    
    public void baixo(List<Estado> visitados){
        if(this.linha == this.dimensao-1) return;
        int matrizTmp[][] = this.clonar();
        
        matrizTmp[this.linha][coluna] = matrizTmp[this.linha+1][coluna];
        matrizTmp[this.linha+1][coluna] = 0;
        
        Puzzle novo = new Puzzle(matrizTmp, this.linha+1, this.coluna, "Indo para baixo");
        if(!visitados.contains(novo)){
            visitados.add(novo);
        } else {
            System.gc();
        }
    }
    
    public void esquerda(List<Estado> visitados){
        if(this.coluna == 0) return;
        int matrizTmp[][] = this.clonar();
        
        matrizTmp[this.linha][this.coluna] = matrizTmp[this.linha][this.coluna-1];
        matrizTmp[this.linha][this.coluna-1] = 0;
        
        Puzzle novo = new Puzzle(matrizTmp, this.linha, this.coluna-1, "Indo para esquerda");
        if(!visitados.contains(novo)){
            visitados.add(novo);
        } else {
            System.gc();
        }
    }
    
    public void direita(List<Estado> visitados){
        if(this.coluna == this.dimensao-1) return;
        int matrizTmp[][] = this.clonar();
        
        matrizTmp[this.linha][this.coluna] = matrizTmp[this.linha][this.coluna+1];
        matrizTmp[this.linha][this.coluna+1] = 0;
        
        Puzzle novo = new Puzzle(matrizTmp, this.linha, this.coluna+1, "Indo para direita");
        if(!visitados.contains(novo)){
            visitados.add(novo);
        } else {
            System.gc();
        }
    }

    @Override
    public String getDescricao() {
        return "Problema do puzzle de NxN";
    }

    @Override
    public boolean ehMeta() {
        int [][] meta = new int[this.dimensao][this.dimensao];
        int temp = 0;
        for(int i = 0; i < this.dimensao;i++){
            for(int j = 0; j < this.dimensao; j++){
                meta[i][j] = temp++;
            }
        }
        Puzzle pMeta = new Puzzle(meta,0,0,"Estado Final");
        return this.matriz.equals(pMeta);
    }

    @Override
    public int custo() {
        return 1;
    }

    @Override
    public List<Estado> sucessores() {
        List<Estado> visitados = new LinkedList<Estado>();
        
        cima(visitados);
        baixo(visitados);
        esquerda(visitados);
        direita(visitados);
        
        return visitados;
    }
    
    @Override
    public String toString() {
        StringBuffer temp = new StringBuffer();
        temp.append(op+"\n");
        for(int i = 0; i < this.dimensao; i++){
            for(int j = 0; j < this.dimensao; j++){
                temp.append(this.matriz[i][j]+"\t");
            }
            temp.append("\n");
        }
        //System.out.println("\n0 = ["+this.linha+","+this.coluna+"]\n");
        temp.append("\n0 = ["+this.linha+","+this.coluna+"]\n");
        return temp.toString();
    }
    
    @Override
    public boolean equals(Object o){
        if(o instanceof Puzzle){
            Puzzle e = (Puzzle) o;
            
            for(int i = 0; i < this.dimensao; i++){
                for(int j = 0; j < this.dimensao; j++){
                    if(e.matriz[i][j] != this.matriz[i][j])
                        return false;
                }
            }
            return true;
        }
        return false;
    }
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);        
        System.out.println("Dimensão da matriz: ");        
        int dimensao = teclado.nextInt();
        Puzzle estadoInicial = new Puzzle(dimensao, "Estado Inicial");        
        Nodo n = new BuscaLargura(new MostraStatusConsole()).busca(estadoInicial);
        
        if (n == null){
            System.out.println("sem solucao");
        } else {
            System.out.println("solucao:\n" + n.montaCaminho() + "\n\n");
        }
        
    }
}
