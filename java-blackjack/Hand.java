import java.util.ArrayList;

// Class implementing a hand
public class Hand {
  // Attributes
  ArrayList<Card> hand = new ArrayList<Card>();

  // Adds the card to the hand
  public void add(Card card) {
    this.hand.add(card);
  }

  // Removes the i cards of the hand
  public void remove(int i) {
    this.hand.remove(i);
  }

  // Returns the i card of the hand
  public Card get(int i) {
    return this.hand.get(i);
  }

  // Returns the size of the hand
  public int size() {
    return this.hand.size();
  }

  // Returns an array with the two possible values of the hand (identical if there's no Ace in the hand)
  public ArrayList<Integer> value() {
    int aceCount = 0;
    ArrayList<Integer> resTab = new ArrayList<Integer>();
    int resVal1 = 0;
    int resVal2 = 0;
    for (int i = 0; i < this.hand.size(); i++) {
      if (this.hand.get(i).getVisible()) {
        // Increases the counter if there's an Ace
        if (this.hand.get(i).getValue() == 0) {
          aceCount++;
        }
        // If more than one Ace, count it as 1
        if (aceCount > 1 && this.hand.get(i).getValue() == 0) {
          resVal1 += 1;
          resVal2 += 1;
        }
        // If it's the first Ace, count it as 1 and 11
        if (aceCount == 1 && this.hand.get(i).getValue() == 0) {
          resVal1 += 1;
          resVal2 += 11;
        } 
        // No Ace in hand
        else {
          resVal1 += this.hand.get(i).getValue();
          resVal2 += this.hand.get(i).getValue();
        }
      }
    }
    resTab.add(resVal1);
    resTab.add(resVal2);
    return resTab;
  }

  // Returns the best value between the two possible in the hand
  public int bestValue() {
    ArrayList<Integer> values = this.value();
    if (values.get(0) > 21 && values.get(1) > 21) {
      return -1;
    } 
    else if (values.get(0) == 21 || values.get(1) == 21) {
      return 21;
    } 
    else if (values.get(0) > 21) {
      return values.get(1);
    } 
    else if (values.get(1) > 21) {
      return values.get(0);
    } 
    else {
      return Math.max(values.get(0), values.get(1));
    }
  }

  // toString method
  public String toString() {
    String resString = "";
    for (int i = 0; i < this.hand.size(); i++) {
      resString += this.hand.get(i).toString();
    }
    return resString;
  }
}
