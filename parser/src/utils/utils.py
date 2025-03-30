import re

def parse_german_number(raw_amount: str) -> float:
    raw_amount = re.sub(r"[^\d,.-]", "", raw_amount)  
    raw_amount = raw_amount.replace(".", "")  
    raw_amount = raw_amount.replace(",", ".")  

    return float(raw_amount) 

def get_table_value(df, loc):
    value = df.iat[loc.row, loc.column]
    if loc.convert:
        return parse_german_number(value)
    else:
        return value
    
def get_text_value(text, loc):
    words = text.split(" ")
    words = [x for x in words if x.strip()]
    value = ""
    for pos in loc.words:
        if loc.spaces:
            value+= " "
        value+= words[pos]
    value = value.strip()
    if loc.convert:
        return parse_german_number(value)
    else:
        return value
