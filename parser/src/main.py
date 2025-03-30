from fastapi import FastAPI, UploadFile, File, Query
import fitz

from src.mappers.income_statement import Company
from src.services import parsers

app = FastAPI()


@app.post("/income")
async def parse(file: UploadFile = File(...), company: Company = Query(...)):
    try:
        if not file.filename.endswith(".pdf"):
            raise ValueError("The uploaded file is not a PDF.")

        pdf_file = await file.read()
        doc = fitz.open(stream=pdf_file, filetype="pdf")

        return parsers.parse_income_statement(doc, company.value)

    except Exception as e:
        print(e)
        return {"error": "Failed to parse PDF", "status": 500}
    

