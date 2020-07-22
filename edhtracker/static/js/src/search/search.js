import React, { useState,useEffect} from 'react';
import ReactDOM from 'react-dom';
import {SearchBar} from './index'
import {Card} from '../cards'
import {searchCards} from './index'
import CardsContainer from '../hoc/CardsContainer'
import {CardModal} from '../cards'

const e = React.createElement
const searchResultsElement = document.getElementById("searchResults")

function Search(props){
    const [cards,setCards] = useState([])
    const [cardsDidSet, setCardsDidSet] = useState(false)
    const [nextUrl, setNextUrl] = useState(null)
    const [searchParams, setSearchParams] = useState(props.searchparam)
    const [cardInfo, setCardInfo] = useState(
        {"cardName":"",
        "cardId":"",
        "isVisible": "none",
        "backdropShow":false}
        )
      const displayModalHandler = (props) =>{
        setCardInfo(
          {"cardId":props.cardId,
          "cardName": props.cardName,
          "backdropShow":true})
      }
      const closeModalHandler = () =>{
        setCardInfo({"cardName":"", "isVisible": "none","backdropShow":false})
      }
    function onSearch(props){
        console.log(props)
        setSearchParams(props)
    }

    useEffect(() => {
        if (cardsDidSet === false && searchParams !== null){
          const handleCardsLookUp = (response, status) => {
            if (status === 200){
              setNextUrl(response.next)
              setCardsDidSet(true)
              setCards(response.results)
            } else {
              alert("There was an error")
            }
          }
          searchCards(handleCardsLookUp,nextUrl,searchParams)
        }
      }, [cardsDidSet,searchParams ,nextUrl])

    const handleLoadNext = (event) => {
        event.preventDefault()
        if (nextUrl !== null) {
          const handleLoadNextResponse = (response, status) =>{
            if (status === 200){
              setNextUrl(response.next)
              const newCards = [...cards].concat(response.results)
              setCards(newCards)
            } else {
              alert("There was an error")
            }
          }
          searchCards(handleLoadNextResponse,nextUrl,searchParams)
        }
        
      }
    return(
        <React.Fragment>
            <SearchBar onSearch={onSearch}/>
            <CardModal 
              onClose={closeModalHandler}
              isVisible={cardInfo["isVisible"]} 
              cardName={cardInfo["cardName"]} 
              cardId={cardInfo["cardId"]} 
              show={cardInfo["backdropShow"]}
            />
            <CardsContainer children={cards.map((item,index) => {
                return <Card displayModal={displayModalHandler} card={item} key={item.id}/>
            })}/>
            {nextUrl !== null && <button onClick={handleLoadNext} className='btn btn-outline-primary'>Load next</button>}
        </React.Fragment>    )
}
if(searchResultsElement){
  ReactDOM.render(e(Search,searchResultsElement.dataset), searchResultsElement)
}

export default Search;