import java.util.Scanner;

public class Vocales {
    public static void ContarVocales(String[] nombres , int[] Contador) {
        String[] Cvocales = {"a", "e", "i", "o", "u"};
        for (int i = 0; i < nombres.length; i++) {
            int suma = 0;
            String nom = nombres[i];
            for (int j = 0; j < nom.length(); j++) {
                String letra = String.valueOf(nom.charAt(j)); 
                for (int k = 0 ; k < Cvocales.length ; k++) {
                    String vocal = Cvocales[k];
                    if (letra.equals(vocal)) {
                        suma++;
                    }
                }
            }
            Contador[i] = suma;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Cuantos nombres vas a ingresar? : ");
        int n = sc.nextInt();
        String[] nombres = new String[n];
        int[] Contador = new int[n];
        for (int i = 0; i < n; i++) {
            System.out.print("Ingresa el " + (i + 1) + " Nombre : ");
            nombres[i] = sc.next().toLowerCase();
        }
        ContarVocales(nombres,Contador);
        
        for(int i = 0 ; i < n ; i++){
            System.out.println("el nombre " + nombres[i] + " tiene " + Contador[i] + " Vocales." );
        }

    }
}
