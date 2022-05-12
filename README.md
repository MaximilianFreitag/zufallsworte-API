
## Deutsche Zufallsworte API

__________________________________________________


API Docs --> https://zufallsworte.herokuapp.com/


<br>

![image_cover](https://user-images.githubusercontent.com/46624616/165381268-82eef7fe-7b8d-4515-a06d-aec7d3d62518.png)


<br>

__________________________________________________


<!-- How to use -->
## How to use (For the full docs please visit the hyperlink above)
   
<br>
Return 4 random german word

    https://zufallsworte.herokuapp.com/zufallswoerter/4
    
    --> {"words":["Katze","Maus","fliegen","schön"]}

<br> 

Return 6 random german words starting with au 
 
    https://zufallsworte.herokuapp.com/anfangsbuchstaben/au/6
    
    --> {"words":["Ausbildung","Aufstellung","aufstehen","Ausweis","aufrunden","Ausgang"]}

<br> 

Return 3 random german nouns that have the letters "ee" in them 

    https://zufallsworte.herokuapp.com/substantiv_enthaelt/ee/3
    
    --> {"words": ['Meer', 'Idee', 'Ostsee'] }


<br>

__________________________________________________


<br>


<!-- GETTING STARTED -->
## Running the API locally on your computer


1. Git clone the repository to your Desktop and install uvicorn and fast api 
   ```sh
   git clone https://github.com/MaximilianFreitag/zufallsworte-API.git
   pip install uvicorn
   pip install fastapi
   ```

2. cd into the folder "zufallsworte-API" on your desktop
   ```sh
   cd zufallsworte-API
   ```
   
3. Open up the terminal and run following command and visit the resulting localhost URL
   ```sh
   uvicorn main:app --reload
   ```



__________________________________________________

<br>

### Current bugs: 🐞

To-Do:

- None



<br>
__________________________________________________

<br>
<br>

### To-Do list: (Improvements and functionality)

- [ ] Placeholder
- [ ] Placeholder


<br>
<br>

__________________________________________________
<br />
<br />
#API #Duden #Wortgenerator #Python #Informatik #JSON 
<br />
<br />



## License
This project falls under the MIT license.



__________________________________________________

<br>
<br>
<br>
<br>
