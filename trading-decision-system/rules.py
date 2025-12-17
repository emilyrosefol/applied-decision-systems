def trade_decision(trend, structure, momentum):
    """
    Determines whether to trade based on market conditions.

    Parameters:
    - trend: 'bullish' or 'bearish'
    - structure: 'trend' or 'range'
    - momentum: 'strong' or 'weak'
    """

    if trend == "bearish" and structure == "range":
        return "NO TRADE"

    if trend == "bullish" and momentum == "strong":
        return "TRADE"

    return "WAIT"
