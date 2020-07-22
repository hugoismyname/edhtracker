import React, {useEffect,useState} from 'react';
import ReactDOM from 'react-dom';
import Classes from './searchBar.module.css'
import {searchCards} from '../index'

const e = React.createElement
const searchBarElement = document.getElementById("searchbar")

export function SearchBar(){
    const [cards,setCards] = useState([])
    const [cardsDidSet, setCardsDidSet] = useState(false)
    const [searchParams, setSearchParams] = useState(null)
    const [display, setDisplay] = useState("none")

    const closeSearchSuggestion = () =>{
        setTimeout(() => {
            setDisplay("none")
        }, 100);
    }
    const dropdDownSearchHandler = event =>{
        const searchInput = event.target.value.trim()
        
        if(searchInput.length >= 3){
            setSearchParams(searchInput)
            setCardsDidSet(false)
            if(display !== "flex"){
                setDisplay("flex")
            }
        }else if(searchInput.length <= 2){
            setDisplay("none")
        }
    }

    useEffect(() => {
        if (cardsDidSet === false && searchParams !== null){
          const handleCardsLookUp = (response, status) => {
            if (status === 200){
              setCardsDidSet(true)
              setCards(response.results)
            } else {
              alert("There was an error")
            }
          }
          searchCards(handleCardsLookUp,null,searchParams)
        }
      }, [cardsDidSet,searchParams])

    return(
    <div className={Classes.searchContainer}>
        <form className={Classes.searchBar} action="/search/" method="get" autoComplete="off" >
            <input onChange={dropdDownSearchHandler} onBlur={closeSearchSuggestion} name="searchParam" type="text" className={Classes.searchText} placeholder="Search.." />
            <button className={Classes.searchButton} ><i className="fa fa-search"></i></button>
        </form>
        <div  style={{ display: display}} className={Classes.searchSuggestionsContainer}>
            {cards.map((card,index) => { 
                    return (
                    <div  key={card.id}>
                        <a  href={`/card_detail/${card["id"]}`} className={Classes.searchSuggestion}>
                            <img src={`/static/card_images/${card['img_url']}.jpg`} alt={card.name} />                           
                            {card.name}
                        </a>
                    </div>
            )})}
        </div>
    </div>
    )
}
if(searchBarElement){
    ReactDOM.render(e(SearchBar,searchBarElement.dataset), searchBarElement)
}
