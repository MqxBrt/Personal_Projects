// Class containing the Unicode symbols of each card
public class Unicode {

  // Returns the club cards
  public static String clubs(int rank) {
    switch(rank) {
      case 0: return "🃑";
      case 1: return "🃒";
      case 2: return "🃓";
      case 3: return "🃔";
      case 4: return "🃕";
      case 5: return "🃖";
      case 6: return "🃗";
      case 7: return "🃘";
      case 8: return "🃙";
      case 9: return "🃚";
      case 10: return "🃛";
      case 11: return "🃝";
      case 12: return "🃞";
    }
    return "Error";
  }

  // Returns the diamond cards
  public static String diamonds(int rank) {
    switch(rank) {
      case 0: return "🃁";
      case 1: return "🃂";
      case 2: return "🃃";
      case 3: return "🃄";
      case 4: return "🃅";
      case 5: return "🃆";
      case 6: return "🃇";
      case 7: return "🃈";
      case 8: return "🃉";
      case 9: return "🃊";
      case 10: return "🃋";
      case 11: return "🃍";
      case 12: return "🃎";
    }
    return "Error";
  }

  // Returns the heart cards
  public static String hearts(int rank) {
    switch(rank) {
      case 0: return "🂱";
      case 1: return "🂲";
      case 2: return "🂳";
      case 3: return "🂴";
      case 4: return "🂵";
      case 5: return "🂶";
      case 6: return "🂷";
      case 7: return "🂸";
      case 8: return "🂹";
      case 9: return "🂺";
      case 10: return "🂻";
      case 11: return "🂽";
      case 12: return "🂾";
    }
    return "Error";
  }

  // Returns the spade cards
  public static String spades(int rank) {
    switch(rank) {
      case 0: return "🂡";
      case 1: return "🂢";
      case 2: return "🂣";
      case 3: return "🂤";
      case 4: return "🂥";
      case 5: return "🂦";
      case 6: return "🂧";
      case 7: return "🂨";
      case 8: return "🂩";
      case 9: return "🂪";
      case 10: return "🂫";
      case 11: return "🂭";
      case 12: return "🂮";
    }
    return "Error";
  }

  // Return the right Unicode symbol depending on the suit and rank of the card
  public static String getString(Card card) {
    switch (card.suit) {
      case 0: return clubs(card.rank) + " ";
      case 1: return diamonds(card.rank) + " ";
      case 2: return hearts(card.rank) + " ";
      case 3: return spades(card.rank) + " ";
    }
    return "Error";
  }
}
