import java.util.Arrays;
import java.util.Scanner;
public class potitos{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean continuar = true;  
        do {
            System.out.println("");
            System.out.print("Ingresa el numero de casos : ");
            int n = sc.nextInt();
            String[] acepta = new String[20];
            Arrays.fill(acepta, " ");
            String[] rechaza = new String[20];
            Arrays.fill(rechaza, " ");
            int contador = 0;
            if (n > 0) {
                for (int i = 0; i < n; i++) {
                    System.out.print("Se comio el potito : ");
                    String res = sc.next().toUpperCase();
                    boolean darlefinal = true;
                    if (res.equals("SI")) {
                        do {
                            System.out.print("Ingresa el ingrediente : ");
                            String palabra = sc.next().toUpperCase();
                            if (palabra.equals("FIN")) {
                                darlefinal = false;
                            } else {
                                if (contador < acepta.length) {
                                    acepta[contador] = palabra;
                                    contador++;
                                }
                            }
                        } while (darlefinal);
                    } else if (res.equals("NO")) { 
                        do {
                            System.out.print("Ingresa el ingrediente : ");
                            String palabra = sc.next().toUpperCase();
                            if (palabra.equals("FIN")) {
                                darlefinal = false;
                            } else {
                                if (contador < rechaza.length) {
                                    rechaza[contador] = palabra;
                                    contador++;
                                }
                            }
                        } while (darlefinal);
                    }
                }
                Arrays.sort(acepta);
                Arrays.sort(rechaza);
                for (int k = 0; k < rechaza.length; k++) {
                    if (!rechaza[k].equals(" ")) {
                        boolean encontrado = false;
                        for (int j = 0; j < acepta.length; j++) {
                            if (rechaza[k].equals(acepta[j])) {
                                encontrado = true;
                            }
                        }
                        if (!encontrado) {
                            System.out.print(rechaza[k] + " ");
                        }
                    }
                }
                System.out.println("");

            } else {
                continuar = false;
            }
        } while (continuar);
    }
}