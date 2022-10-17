import java.util.ArrayList;
import java.util.Collections;

// Class implementing a deck of cards
public class Deck {
  // Attributes
  ArrayList<Card> deck = new ArrayList<Card>();

  // Constructor
  public Deck(boolean typeOfDeck) {
    if (typeOfDeck) {
      for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 13; j++) {
          Card card = new Card(j, i);
          this.deck.add(card);
        }
      }
    }
  }

  // Returns the i card of the deck
  public Card get(int i) {
    return this.deck.get(i);
  }

  // Adds card to the bottom of the deck
  public void add(Card card) {
    this.deck.add(card);
  }

  // Removes top card and returns it
  public Card distribute() {
    Card card = this.deck.get(0);
    this.deck.remove(0);
    return card;
  }

  // Shuffles the deck
  public void shuffle() {
    Collections.shuffle(this.deck);
  }

  // Empties the deck
  public void empty() {
    this.deck = new ArrayList<Card>();
  }

  // toString method
  public String toString() {
    String resString = "";
    for (int i = 0; i < this.deck.size(); i++) {
      resString += this.deck.get(i).rank + "-" + this.deck.get(i).suit;
      if (i != this.deck.size() - 1) {
        resString += ",";
      }
    }
    return resString;
  }
}