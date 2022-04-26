from fastapi import FastAPI, HTTPException, status
from regex import F
from wortliste import *
from typing import Optional
from pydantic import BaseModel
import starlette.responses as _responses


app = FastAPI()


#this is the documentation for the API
@app.get("/")
def root():
    return _responses.RedirectResponse("/redoc")






@app.get("/wort")
def wort():
    return {'word': random.choice(duden)}


#return multiple words with the function zufallswoerter(n) from wortliste.py
@app.get("/zufallswoerter/{n}")
def zufallswoerter(n: int):
    try:
        return {'words': random.sample(duden, k=n)}
    except:
        ValueError
        raise HTTPException(status_code=404, detail=f"There are only {len(duden)} words in the data set")



@app.get("/anfangsbuchstaben/{m}/{n}")
def anfangsbuchstaben(m: str, n: int):
    try:
        a = list(filter(lambda x: x.lower().startswith(m), duden))
        return {'words': random.sample(a, k=n)}
    except:
        ValueError
        raise HTTPException(status_code=404, detail=f"There are only {len(a)} words starting with {m} in the data set")



@app.get("/endbuchstaben/{m}/{n}")
def endbuchstaben(m: str, n: int):
    try:
        h = list(filter(lambda x: x.lower().endswith(m), duden))
        return {'words': random.sample(h, k=n)}
    except:
        ValueError
        raise HTTPException(status_code=404, detail=f"There are only {len(h)} words ending with {m} in the data set")



@app.get("/enthalt_buchstaben/{m}/{n}")
def enthaelt_buchstaben(m: str, n: int):
    try:
        a = list(filter(lambda x: m in x.lower(), duden))
        return {'words': random.sample(a, k=n)}
    except:
        ValueError
        raise HTTPException(status_code=404, detail=f"There are only {len(a)} words containing {m} in the data set")



@app.get("/anzahl_buchstaben/{m}/{n}")
def anzahl_buchstaben(m: int, n: int):
    try:
        a = []
        for i in duden:
            if len(i) == m:
                a.append(i)
        return {'words': random.sample(a, k=n)}
    except:
        ValueError
        #return f"There are only {len(a)} words with {m} letters in the data set"

        raise HTTPException(status_code=404, detail=f'There are only {len(a)} words with {m} letters in the data set')
        











@app.get("/substantiv/{n}")
def substantiv(n: int):
    try:
        #return only words that start with a capital letter
        a = list(filter(lambda x: x[0].isupper(), duden))
        return {'words': random.sample(a, k=n)}

    except:
        ValueError
        #return f"There are only {len(a)} nouns in the data set"
        raise HTTPException(status_code=404, detail=f'There are only {len(a)} nouns in the data set')
        



@app.get("/substantiv_enthaelt/{m}/{n}")
def substantiv_enthaelt(m: str, n: int):
    try:
        a = []
        for i in duden:
            if m in i.lower() and i[0].isupper():
                a.append(i)
        return {'words': random.sample(a, k=n)}

    except:
        ValueError
        #return f"There are only {len(a)} nouns with the letter {m} in the data set"
        raise HTTPException(status_code=404, detail=f'There are only {len(a)} nouns with the letters {m} in the data set')
        


# m = anzahl buchstaben, n = anzahl worte
@app.get("/substantiv_anzahl/{m}/{n}")
def substantiv_anzahl(m: int, n: int):
    try:
        a = []
        for i in duden:
            if len(i) == m and i[0].isupper():
                a.append(i)
        return {'words': random.sample(a, k=n)}
    except:
        ValueError
        #return f"There are only {len(a)} nouns that are {m} letters long" 
        raise HTTPException(status_code=404, detail=f'There are only {len(a)} nouns that are {m} letters long')
           


#m = anzahl buchstaben, n = anzahl worte
@app.get("/substantiv_ende/{m}/{n}")
def substantiv_ende(m: str, n: int):
    try:
        a = []
        for i in duden:
            #only words that start with a capital letter
            if i[0].isupper() and i.endswith(m):
                a.append(i)
        return {'words': random.sample(a, k=n)}

    except:
        ValueError
        #return f"There are only {len(a)} nouns ending with {m} in the data set"
        raise HTTPException(status_code=404, detail=f'There are only {len(a)} nouns ending with {m} in the data set')



#m = anzahl buchstaben, n = anzahl worte
@app.get("/substantiv_start/{m}/{n}")
def substantiv_start(m: str, n: int):
    try:
        a = []
        for i in duden:
            #only words that start with a capital letter
            if i[0].isupper() and i.startswith(m):
                a.append(i)
        return {'words': random.sample(a, k=n)}

    except:
        ValueError
        #return f"There are only {len(a)} nouns starting with {m} in the data set"

        raise HTTPException(status_code=404, detail=f'There are only {len(a)} nouns starting with {m} in the data set')

        



    
                           