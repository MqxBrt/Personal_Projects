import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

// Class implementing the logic of the blackjack game
public class Blackjack {
    // Attributes
    final int minBet = 1;
    final int maxBet = 200;
    int earnings = 0;
    int maxEarnings = 10000;
    double currentBet = 0;
    final int dealerStand = 17;
    final int nDecks = 8;
    double balance = 0;
    String username = "";
    Deck deck = new Deck(false);
    Hand player = new Hand();
    Hand dealer = new Hand();

    // Constructor
    public Blackjack() {
        Deck defaultDeck = new Deck(true);
        for (int i = 0; i < nDecks; i++) {
            for (int j = 0; j < 52; j++) {
                this.deck.add(defaultDeck.get(j));
            }
        }
        this.deck.shuffle();
    }

    // Hide previous logs
    public void clearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    // Returns true if input is valid depending on mode
    public boolean validInput(String mode, String input) {
        switch (mode) {
        case "YesNo":
            ArrayList<String> allowedYN = new ArrayList<String>();
            allowedYN.add("y");
            allowedYN.add("n");
            allowedYN.add("Y");
            allowedYN.add("N");
            allowedYN.add("1");
            allowedYN.add("0");
            return allowedYN.contains(input);
        case "Card":
            ArrayList<String> allowedC = new ArrayList<String>();
            allowedC.add("0");
            allowedC.add("1");
            allowedC.add("2");
            return allowedC.contains(input);
        case "Cards":
            ArrayList<String> allowedCS = new ArrayList<String>();
            allowedCS.add("0");
            allowedCS.add("1");
            allowedCS.add("2");
            allowedCS.add("3");
            return allowedCS.contains(input);
        }
        return false;
    }

    // Launches the program
    public int launch() {
        this.clearConsole();
        Scanner userInput = new Scanner(System.in);
        ArrayList<String> affirmative = new ArrayList<String>();
        affirmative.add("y");
        affirmative.add("Y");
        affirmative.add("1");

        // Handle load and new game
        System.out.print("Do you want to load a save? [y/n] ");
        String loadGame = userInput.next();
        while (!validInput("YesNo", loadGame)) {
            System.out.println("[ERROR] Invalid input");
            loadGame = userInput.next();
        }
        if (affirmative.contains(loadGame)) {
            System.out.print("Which game do you want to load? (games are stored in the 'saves' directory) ");
            loadGame = userInput.next();
            this.clearConsole();
            if (this.loadProgress(loadGame) == 1) {
                return 1;
            }
            System.out.print("\nWelcome back " + this.username + "! You have " + (int)this.balance + "$ in your wallet, ready to play? [y/n] ");
        } 
        else {
            this.clearConsole();
            System.out.print("Username: ");
            this.username = userInput.next();

            this.clearConsole();
            System.out.println("Welcome to the Blackjack game " + this.username + ".\n");
            System.out.print("How much would you like to deposit? ");
            this.balance = userInput.nextInt();
            while (this.balance < 0) {
                System.out.println("[ERROR] Invalid input");
                this.balance = userInput.nextInt();
            }
            this.clearConsole();
            this.displayHeader();
            System.out.print("Alright " + this.username + ", you have " + (int)this.balance + "$ in your wallet, ready to play? [y/n] ");
        }

        String input = userInput.next();
        while (!validInput("YesNo", input)) {
            System.out.println("[ERROR] Invalid input");
            input = userInput.next();
        }

        if (affirmative.contains(input)) {
            return this.game();
        } 
        else {
            this.clearConsole();
            this.displayHeader();
            System.out.println("Thanks for playing " + this.username + ", see you soon!");
            return 0;
        }
    }

    // Starts a game
    public int game() {
        this.clearConsole();
        Scanner userInput = new Scanner(System.in);
        boolean exitProgram = false;

        // Will end until user exits or runs out of money
        while (!exitProgram) {
            boolean gameStatus = true;
            boolean dealerOver = false;
            boolean userSurrend = false;
            this.currentBet = 0;

            // Will end once the game is over
            while (gameStatus) {
                int oldBalance = (int)this.balance;
                // Input bet
                this.clearConsole();
                this.displayHeader();
                System.out.println("\t\t\t--BLACKJACK--");
                System.out.println("\tDealer must draw to " + (this.dealerStand - 1) + " and stand on all " + this.dealerStand + "s\n");
                System.out.println("\tYour balance: " + (int)this.balance + "$");
                System.out.print("\nHow much you want to bet? (" + this.minBet + "-" + Math.min(this.maxBet, (int)this.balance) + ") ");
                this.currentBet = userInput.nextInt();
                while (this.currentBet > this.maxBet || this.currentBet < this.minBet || this.currentBet > this.balance) {
                    System.out.println("[ERROR] Invalid input");
                    this.currentBet = userInput.nextInt();
                }
                this.player.add(this.deck.distribute());
                this.player.add(this.deck.distribute());
                this.balance -= this.currentBet;
                this.dealer.add(this.deck.distribute());
                this.dealer.add(this.deck.distribute());
                boolean drawing = true;
                this.dealer.get(1).setVisible(false);
                
                // Will end once the user stops drawing cards
                while (drawing) {
                    // Input choices
                    this.displayBoard();

                    // User at 21, drawing dealer
                    if (this.player.bestValue() == 21) {
                        drawing = false;
                    }
                    // Busted = loss anyway, no matter dealer's hand
                    else if (this.player.bestValue() == -1) {
                        drawing = false;
                        dealerOver = true;
                    }
                    // User can still play
                    else {
                        System.out.println("\n\tWhat do you want to do?");
                        System.out.println("\t\t[0] Surrender (half your bet is refunded)");
                        System.out.println("\t\t[1] Hit (draw a card)");
                        System.out.println("\t\t[2] Stay (lock your hand)");
                        // Check if user has enough money to double
                        if (this.balance >= this.currentBet) {
                            System.out.println("\t\t[3] Double down (double your bet and draw a single card)");
                        }
                        System.out.print("\nYour choice: ");
                        String input = userInput.next();

                        String mode = "";
                        if (this.balance >= this.currentBet) {
                            mode = "Cards";
                        } 
                        else {
                            mode = "Card";
                        }
                        while (!validInput(mode, input)) {
                            System.out.println("[ERROR] Invalid input");
                            input = userInput.next();
                        }
                        int choice = Integer.parseInt(input);
                        if (choice == 0) {
                            userSurrend = true;
                            drawing = false;
                            dealerOver = true;
                        } 
                        else if (choice == 1) {
                            this.player.add(this.deck.distribute());
                        } 
                        else if (choice == 2) {
                            drawing = false;
                        } 
                        else {
                            this.player.add(this.deck.distribute());
                            this.balance -= this.currentBet;
                            this.currentBet += this.currentBet;
                            drawing = false;
                        }
                    }
                }

                // Check dealer hand to decide
                this.dealer.get(1).setVisible(true);
                if (!dealerOver) {
                    while (!dealerOver) {
                        // Draws if dealer did not busted and is below dealerStand
                        if (this.dealer.bestValue() != -1 && this.dealer.bestValue() < this.dealerStand) {
                            this.dealer.add(this.deck.distribute());
                        } 
                        else {
                            dealerOver = true;
                        }
                    }
                }

                // Refresh display before showing results
                this.displayBoard();

                // User surrendered
                if (userSurrend) {
                    System.out.println("\nYou surrendered and lost " + (int)Math.ceil(this.currentBet / 2) + "$...");
                    this.balance += (int)Math.floor(this.currentBet / 2);
                }
                // Draw check
                else if (this.player.bestValue() == this.dealer.bestValue()) {
                    System.out.println("\nDraw, your bet was refunded.");
                    this.balance += this.currentBet;
                }
                // Blackjack check
                else if (this.player.size() == 2 && this.player.bestValue() == 21) {
                    System.out.println("\nYou got a Blackjack and won " + (int)(this.currentBet * 2.5) + "$!");
                    this.balance += (int)(this.currentBet * 2.5);
                }
                // User busted
                else if (this.player.bestValue() == -1) {
                    System.out.println("\nYou busted and lost " + (int)this.currentBet + "$...");
                }
                // Dealer busted
                else if (this.dealer.bestValue() == -1) {
                    System.out.println("\nDealer busted, you won " + (int)this.currentBet * 2 + "$!");
                    this.balance += (int)this.currentBet * 2;
                }
                // Dealer has best score
                else if (this.dealer.bestValue() > this.player.bestValue()) {
                    System.out.println("\nDealer won, you lost " + (int)this.currentBet + "$...");
                }
                // User has best score
                else {
                    System.out.println("\nYou won and got " + (int)this.currentBet * 2 + "$!");
                    this.balance += (int)this.currentBet * 2;
                }
                gameStatus = false;
                this.earnings += (int)this.balance - oldBalance;
                // Reset hands and place cards in the back of the deck in case of a replay
                while (this.player.size() > 0) {
                    Card card = this.player.get(0);
                    card.setVisible(true);
                    this.deck.add(card);
                    this.player.remove(0);
                }
                while (this.dealer.size() > 0) {
                    Card card = this.dealer.get(0);
                    card.setVisible(true);
                    this.deck.add(card);
                    this.dealer.remove(0);
                }
            }

            // Handle save, moneyless and ban
            if (this.earnings >= this.maxEarnings) {
                System.out.println("\nYou won too much money and are now banned from the casino.");
                return 0;
            }
            else {
                if (this.balance > 0) {
                    System.out.print("\nDo you want to play again? [y/n] ");
                    String replay = userInput.next();
                    while (!validInput("YesNo", replay)) {
                        System.out.println("[ERROR] Invalid input");
                        replay = userInput.next();
                    }
                    ArrayList<String> negative = new ArrayList<String>();
                    negative.add("n");
                    negative.add("N");
                    negative.add("0");
                    if (negative.contains(replay)) {
                        exitProgram = true;
                    }
                }
                else {
                    System.out.println("\nYou ran out of money and got kicked out of the casino.");
                    return 0;
                }
            }
        }
        this.clearConsole();
        System.out.print("Do you want to save your progress? [y/n] ");
        String saveGame = userInput.next();
        while (!validInput("YesNo", saveGame)) {
            System.out.println("[ERROR] Invalid input");
            saveGame = userInput.next();
        }
        ArrayList<String> affirmative = new ArrayList<String>();
        affirmative.add("y");
        affirmative.add("Y");
        affirmative.add("1");
        if (affirmative.contains(saveGame)) {
            System.out.print("Enter save name (games are stored in the 'saves' directory) ");
            saveGame = userInput.next();
            this.clearConsole();
            if (this.saveProgress(saveGame) == 1) {
                return 1;
            }
            System.out.println("\nThanks for playing " + this.username + ", see you soon!");
        } 
        else {
            this.clearConsole();
            System.out.println("Thanks for playing " + this.username + ", see you soon!");
        }
        return 0;
    }

    public void displayHeader() {
        System.out.println("[Player: " + this.username + "\tEarnings: " + this.earnings + "]\n\n");
    }

    public void displayBoard() {
        this.clearConsole();
        this.displayHeader();
        System.out.println("\t\t\t--BLACKJACK--");
        System.out.println("\tDealer must draw to " + (this.dealerStand - 1) + " and stand on all " + this.dealerStand + "s\n");
        System.out.println("\tYour bet: " + (int)this.currentBet + "$\t Your balance: " + (int)this.balance + "$\n");

        if (this.dealer.value().get(0) != this.dealer.value().get(1)) {
            System.out.println("\tDealer's hand: (" + this.dealer.value().get(0) + " or " + this.dealer.value().get(1) + ")");
        } 
        else {
            System.out.println("\tDealer's hand: (" + dealer.value().get(0) + ")");
        }
        System.out.println("\t" + this.dealer);

        if (this.player.value().get(0) != this.player.value().get(1)) {
            System.out.println("\tYour hand: (" + this.player.value().get(0) + " or " + this.player.value().get(1) + ")");
        } 
        else {
            System.out.println("\tYour hand: (" + this.player.value().get(0) + ")");
        }
        System.out.println("\t" + this.player);
    }

    // Loads a game from txt file
    public int loadProgress(String fileName) {
        fileName = "saves/" + fileName + ".txt";
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileName));
            StringBuilder sb = new StringBuilder();
            String line = br.readLine();

            while (line != null) {
                sb.append(line);
                line = br.readLine();
            }
            String mySave = sb.toString();
            br.close();

            this.username = mySave.split("/")[0].split(":")[1];
            this.balance = Double.parseDouble(mySave.split("/")[1].split(":")[1]);
            this.earnings = Integer.parseInt(mySave.split("/")[2].split(":")[1]);
            this.deck.empty();
            String[] importedDeck = mySave.split("/")[3].split(":")[1].split(",");
            for (int i = 0; i < importedDeck.length; i++) {    
                int rank = Integer.parseInt(importedDeck[i].split("-")[0]);
                int suit = Integer.parseInt(importedDeck[i].split("-")[1]);
                Card newCard = new Card(rank, suit);
                this.deck.add(newCard);
            }
            System.out.println("Save successfully loaded!");
            return 0;
        } 
        catch (IOException e) {
            System.out.println("[ERROR] Loading failed");
            e.printStackTrace();
            return 1;
        }
    }

    // Saves a game to txt file
    public int saveProgress(String fileName) {
        fileName = "saves/" + fileName + ".txt";
        String newSave = "username:" + this.username + "/balance:" + (int)this.balance + "/earnings:" + this.earnings + "/deck:" + this.deck.toString();

        try {
            FileWriter mySaveFile = new FileWriter(fileName);
            mySaveFile.write(newSave);
            mySaveFile.close();
            System.out.println("Progress successfully saved!");
            return 0;
        } 
        catch (IOException e) {
            System.out.println("[ERROR] Saving failed");
            e.printStackTrace();
            return 1;
        }
    } 
}
