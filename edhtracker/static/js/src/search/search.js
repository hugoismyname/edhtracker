import React, { useState,useEffect} from 'react';
import ReactDOM from 'react-dom';
import {Card} from '../cards'
import {searchCards} from './index'
import CardsContainer from '../hoc/CardsContainer'
import Classes from './search.module.css'

const e = React.createElement
const searchResultsElement = document.getElementById("searchResults")

function Search(props){
    const [cards,setCards] = useState([])
    const [searchParams, setSearchParams] = useState(props.searchparam)
    const [cardsDidSet, setCardsDidSet] = useState(false)
    const [nextUrl, setNextUrl] = useState(null)
    const [message, setMessage] = useState(false)
   
    function onSearch(props){
      event.preventDefault()
        const searchWord = event.target.value
        
        if (searchWord.length >= 3 ){
          setMessage(false)
          setSearchParams(searchWord)
          console.log(searchParams)
          setNextUrl(null)
          setCardsDidSet(false)
        }
    }

    useEffect(() => {
        if (cardsDidSet === false && searchParams !== null){
          const handleCardsLookUp = (response, status) => {
            if (status === 200){
              setNextUrl(response.next)
              setCardsDidSet(true)
              setCards(response.results)
            } else if(status === 204) {
              setMessage(true)
            }
          }
          searchCards(handleCardsLookUp,nextUrl,searchParams)
        }
      }, [cardsDidSet,message])

    const handleLoadNext = (event) => {
        event.preventDefault()
        if (nextUrl !== null) {
          const handleLoadNextResponse = (response, status) =>{
            if (status === 200){
              setNextUrl(response.next)
              const newCards = [...cards].concat(response.results)
              setCards(newCards)
              setCardsDidSet(false)
            } else {
              alert("There was an error")
            }
          }
          searchCards(handleLoadNextResponse,nextUrl,searchParams)
        }
        
      }
    return(
        <React.Fragment>
            <div className={Classes.searchBar}>
              <input className={Classes.searchText} onChange={onSearch}></input>
              <button className={Classes.searchButton} ><i className="fa fa-search"></i></button>
            </div>
            
            {
            message != false && 
              <div className={Classes.orangePaint}>
                <div className={Classes.paintText} >
                    <span className={Classes.paintTitle} ><strong>0 Cards Found</strong><br/> Consider Broadening Your Search Criteria.</span>
                </div>
              </div>
            }

            <CardsContainer children={cards.map((item,index) => {
                return <Card card={item} key={item.id}/>
            })}/>

            {nextUrl !== null && <button onClick={handleLoadNext} className='btn btn-outline-primary'>Load next</button>}

        </React.Fragment>    )
}
if(searchResultsElement){
  ReactDOM.render(e(Search,searchResultsElement.dataset), searchResultsElement)
}

export default Search;