import React, {useState, useEffect} from 'react';
import ControlBar from './ControlBar'
import {apiUserCardsList} from './index';
import {Card} from '../cards';
import {TableHead, TableRow} from './index'
import CardsContainer from '../hoc/CardsContainer';
import Aux from '../hoc/ReactAux'
import {CardModal} from '../cards'


export function UserCardList(props){
  const [cards, setCards] = useState([])
  const [cardsDidSet, setCardsDidSet] = useState(false)
  const [nextUrl, setNextUrl] = useState(null)
  const [display, setDisplay] = useState(["visual"])
  const [order, setOrder] = useState("date_added")
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
  const changeDisplayFormat = (props) =>{
      setDisplay(props)
  }
  const deleteCard = (props) =>{
    const tempCards = [...cards]
    const filteredCards = tempCards.filter(card => card.id !== props);
    setCards(filteredCards)
  }
  const changeOrder = (props,cardList = [...cards]) =>{
    console.log(props)
    if(order === props){
      cardList.sort((a, b) => (a[props] < b[props]) ? 1 : -1)
      setOrder(`-${props}`)
    }else if(props === "same"){
      cardList.sort((a, b) => (a[order] > b[order]) ? 1 : -1)
    }else{
      cardList.sort((a, b) => (a[props] > b[props]) ? 1 : -1)
      setOrder(props)
    }
    setCards(cardList)
  }

  const handleBackendUpdate = (response, status) =>{
    // backend api response handler
   if(status === 204){

    }else if(status === 200){

    }else {
      alert("An error occured please try again")
    }
  }
  useEffect(() => {
    if (cardsDidSet === false){
      const handleCardsLookUp = (response, status) => {
        if (status === 200){
          setNextUrl(response.next)
          setCards(response.results)
          setCardsDidSet(true)
        } else {
          alert("There was an error")
        }
      }
      apiUserCardsList(props.username,handleCardsLookUp,null)
    }
  }, [props.username, cardsDidSet])
  
  const handleLoadNext = (event) => {
    event.preventDefault()
    if (nextUrl !== null) {
      const handleLoadNextResponse = (response, status) =>{
        if (status === 200){
          setNextUrl(response.next)
          const newCards = [...cards].concat(response.results)
          changeOrder("same",newCards)
        } else {
          alert("There was an error")
        }
      }
      apiUserCardsList(props.username, handleLoadNextResponse,nextUrl)
    }
  }

  let userCards = <CardsContainer children={cards.map((item,index) => {
      return <Card displayModal={displayModalHandler} onAdd={handleBackendUpdate} card={item} key={item.id}/>
  })}/>  ;

  if (display === "visual"){
      userCards = <CardsContainer children={cards.map((item,index) => {
          return <Card displayModal={displayModalHandler} onAdd={handleBackendUpdate} card={item} key={item.id}/>
      })}/>  
  }else if(display === "list"){
      userCards = 
      <Aux>
          <TableHead/>
          <CardsContainer children={cards.map((item,index) => {
              return <TableRow callbackHandler={handleBackendUpdate} onDelete={deleteCard} card={item} key={item.id}/>
          })}/>
      </Aux>
  }
  return(
      <Aux> 
          <ControlBar changeOrder={changeOrder} switchDisplay={changeDisplayFormat} />
          <CardModal 
            onClose={closeModalHandler}
            isVisible={cardInfo["isVisible"]} 
            cardName={cardInfo["cardName"]} 
            cardId={cardInfo["cardId"]} 
            show={cardInfo["backdropShow"]}
          />
          {userCards}
          {nextUrl !== null && <button onClick={handleLoadNext} className='btn btn-outline-primary'>Load next</button>}         
      </Aux>
  )
}