def cakes(recipe, available):
    final_amount = -1
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        amount = available[ingredient] // recipe[ingredient]
        if final_amount == -1:
            final_amount = amount
        else:
            final_amount = min(final_amount, amount)
    return final_amount
