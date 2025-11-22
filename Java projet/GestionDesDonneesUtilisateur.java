import java.util.Scanner;

public class GestionDesDonneesUtilisateur {

    public static void main(String[] args) {
        // On va créer un objet Scanner qui va permettre de lire les entrées de la personne
        Scanner scanner = new Scanner(System.in);
        
        // Demander le nom de la personne qui utilise le programme
        System.out.print("Entrez votre nom : ");
        String nom = scanner.nextLine();  // Type "String" pour le nom (string permet de collecter des caractères)
        
        // Demander l'âge de la personne
        System.out.print("Entrez votre âge : ");
        int age = scanner.nextInt();  // Type "int" pour l'âge (int permet de collecter des nombre)
        
        // Demander la taille de la personne
        System.out.print("Entrez votre taille en mètres : ");
        double taille = scanner.nextDouble();  // Type double pour la taille (Pour la précision en décimale)
        
        // Calculer l'année de naissance en fonction de l'age que la personne nous donne
        int anneeActuelle = 2025;  // On suppose que l'année actuelle est 2025
        int anneeNaissance = anneeActuelle - age;
        
        // Afficher les informations
        System.out.println("\nInformations");
        System.out.println("Votre nom est : " + nom);
        System.out.println("Votre age est : " + age + " ans");
        System.out.println("Votre taille est : " + taille + " m");
        System.out.println("Vous êtes né(e) en " + anneeNaissance + " !");
        
        // Fermer le scanner
        scanner.close();
    }
}
