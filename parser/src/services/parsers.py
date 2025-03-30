from src.utils import utils
from src.mappers.income_statement import earnings_mapper, TableLocation, TextLocation, taxes_mapper, social_contributions_mapper
from src.models.income_statement import Earning, Deduction, Details

def parse_income_statement(doc, company):
    resp = {
        "earning" : Earning(),
        "deduction": Deduction()
    }


    earning_map = earnings_mapper[company]
    tax_map = taxes_mapper[company]
    sc_map = social_contributions_mapper[company]

    for page in doc: 
        text = page.get_text(sort=True)
        text = text.split("\n")
        text = [x for x in text if x.strip()]
        tables = []
        for table in page.find_tables().tables:
            tables.append(table.to_pandas())

        for field, pos in earning_map.items():
            if type(pos) is TextLocation:
                setattr(resp["earning"], field, utils.get_text_value(text[pos.text], pos))
            elif type(pos) is TableLocation:
                setattr(resp["earning"], field, utils.get_table_value(tables[pos.table], pos))
        
        for field, pos in tax_map.items():
            if type(pos) is TextLocation:
                setattr(resp["deduction"].tax, field, utils.get_text_value(text[pos.text], pos))
            elif type(pos) is TableLocation:
                setattr(resp["deduction"].tax, field, utils.get_table_value(tables[pos.table], pos))
        
        for field, pos in sc_map.items():
            if type(pos) is TextLocation:
                setattr(resp["deduction"].socialSecurityContribution, field, utils.get_text_value(text[pos.text], pos))
            elif type(pos) is TableLocation:
                setattr(resp["deduction"].socialSecurityContribution, field, utils.get_table_value(tables[pos.table], pos))
        
        desc = tables[5].iat[0, 1].split("\n")
        desc = [x for x in desc if x.strip()]
        vals = tables[5].iat[0, 2].split("\n")
        vals = [x for x in vals if x.strip()]
        
        i = 0
        ded = {}
        earn = {}
        for val in vals:
            amt = utils.parse_german_number(val)
            if amt < 0:
                ded[desc[i]] = amt
            else:
                earn[desc[i]] = amt
            i+= 1

        setattr(resp["deduction"], "additional", ded)
        setattr(resp["earning"], "additional", earn)

        monYear = resp["earning"].description.split(" ")
        details = Details()
        details.month = monYear[0]
        details.year = int(monYear[1])
        details.gross = resp["earning"].gross
        details.deduction = round(resp["earning"].gross - resp["earning"].paid, 2)
        details.paid = resp["earning"].paid

        resp["details"] = details


        return resp