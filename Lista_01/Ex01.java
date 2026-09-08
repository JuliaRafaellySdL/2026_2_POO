import java.util.Scanner;

public class Ex01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite seu nome: ");
        String nome = entrada.nextLine();
        System.out.println("Olá, " + nome + "!");
        entrada.close();
    }
}

// javac Ex01.java
// java Ex01