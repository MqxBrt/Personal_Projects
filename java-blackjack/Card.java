// Class implementing a card
public class Card {
  // Attributes
  int rank;
  int suit;
  boolean visible;

  // Constructor
  public Card(int rank, int suit) {
    this.rank = rank;
    this.suit = suit;
    this.visible = true;
  }

  // Returns the rank of the card
  public String getRank() {
    switch (this.rank) {
      case 0:
        return "A";
      case 1:
        return "2";
      case 2:
        return "3";
      case 3:
        return "4";
      case 4:
        return "5";
      case 5:
        return "6";
      case 6:
        return "7";
      case 7:
        return "8";
      case 8:
        return "9";
      case 9:
        return "10";
      case 10:
        return "J";
      case 11:
        return "Q";
      case 12:
        return "K";
    }
    return "Error";
  }

  // Returns the suit of the card
  public String getSuit() {
    switch (this.suit) {
      case 0:
        return "♣";
      case 1:
        return "♦";
      case 2:
        return "♥";
      case 3:
        return "♠";
    }
    return "Error";
  }

  // Returns the value of the card
  public int getValue() {
    switch (this.rank) {
      case 0:
        return 0;
      case 1:
        return 2;
      case 2:
        return 3;
      case 3:
        return 4;
      case 4:
        return 5;
      case 5:
        return 6;
      case 6:
        return 7;
      case 7:
        return 8;
      case 8:
        return 9;
      case 9:
        return 10;
      case 10:
        return 10;
      case 11:
        return 10;
      case 12:
        return 10;
    }
    return 1;
  }

  public boolean getVisible() {
    return this.visible;
  }

  public void setVisible(boolean visible) {
    this.visible = visible;
  }

  // The following methods are both toString() for the Card class. The first uses brackets, integers and ASCII symbol. The second uses Unicode character of each card
  
  /*
  // Simple cards toString method
  public String toString() {
    if (this.visible) {
      return "[" + getRank() + getSuit() + "]";
    } else {
      return "[??]";
    }
  }
  */

  // Unicode cards toString method
  public String toString() {
    if (this.visible) {
      // Front of the card
      return Unicode.getString(this);
    } else {
      // Back of the card
      return "🂠 ";
    }
  }
  
}