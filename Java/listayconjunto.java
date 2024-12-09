import java.util.Arrays;
import java.util.Scanner;
public class listayconjunto{
    public static void MostrarVector(String[] v) {
        for (int i = 0; i < v.length; i++) {
            System.out.print(v[i] +  " ");
        }
    }

    public static boolean PalabraConjunto(String palabras, String[] conjunto) {
        boolean encontrado = false;
        for (int j = 0; j < conjunto.length; j++){
            if (conjunto[j].equals(palabras)){
                encontrado = true;
            }
        }
        return encontrado;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String [] conjunto = new String[5];
        String [] lista = new String[5];
        Arrays.fill(conjunto, "");
        for (int i = 0; i < 5; i++){
            boolean encontrado = false; 
            System.out.print("Ingresa una palabra : ");
            String palabras = sc.nextLine();
            lista[i] = palabras;
            PalabraConjunto(palabras, conjunto);
            if (PalabraConjunto(palabras,conjunto) == false){
                conjunto[i] = palabras;
            }
            
        }
        System.out.print("conjunto : ");
        MostrarVector(conjunto);
        System.out.print("\nlista : ");
        MostrarVector(lista);

    }
}