def oxford_comma(lst):
    if not str:
        return ""
    elif len(lst)==1:
        return lst[0]
    elif len(lst)==2:
        return " and ".join(lst)
    else:
        return ", ".join(lst[:-1])+ f", and {lst[-1]}"
result = oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits", "lychees", "pomelos"])
print(result)
