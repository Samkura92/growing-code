def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_types = seed_type.capitalize()
    if unit == "packets":
        print(seed_types, "seeds: ", quantity, unit, "available")
    elif unit == "grams":
        print(seed_types, "seeds: ", quantity, unit, "total")
    elif unit == "area":
        print(seed_types, "seeds: ", "covers", quantity, "square area")
    else:
        print(unit.capitalize(), "unit type")
