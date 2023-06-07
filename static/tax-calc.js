function tcalc () {
  // (A) ITEM PRICE + TAX PERCENTAGE
  var price = document.getElementById("taxprice").value,
      percent = document.getElementById("taxperc").value;
  price = parseFloat(price);
  percent = parseFloat(percent);

  // (B) CALCULATE TAX AMOUNT
  var tax = (price / 100) * percent,
      grand = price * ((100 + percent) / 100);

  // (C) ROUND OFF
  // CREDITS - https://www.jacklmoore.com/notes/rounding-in-javascript/
  var roundoff = function (amount, places) {
    let ea = "e" + places,
        eb = "e-" + places;
    return Number(Math.round(amount + ea) + eb);
  };

  // (D) SET CALCULATED VALUES TO HTML FIELDS
  document.getElementById("taxamt").value = roundoff(tax, 2);
  document.getElementById("taxgrand").value = roundoff(grand, 2);
  return false;
}
