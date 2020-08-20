import React, {useState, useEffect} from 'react';
import ReactDOM from 'react-dom';

import ControlBar from './cardsTable/ControlBar'
import {apiUserCardsList} from './index';
import {Card} from '../cards';
import {TableHead, TableRow} from './index'
import CardsContainer from '../hoc/CardsContainer';
import Classes from './userCards.module.css'


const e = React.createElement
const userCardsElement = document.getElementById("userCards")

export function UserCardList(props){
  const [cards, setCards] = useState([])
  const [cardsDidSet, setCardsDidSet] = useState(false)
  const [nextUrl, setNextUrl] = useState(null)
  const [display, setDisplay] = useState(["visual"])
  const [order, setOrder] = useState("date_added")
  const [total, setTotal] = useState(0)

  const changeDisplayFormat = (props) =>{
      setDisplay(props)
  }
  const deleteCard = (props) =>{
    const tempCards = [...cards]
    const filteredCards = tempCards.filter(card => card.id !== props);
    setCards(filteredCards)
  }
  const changeOrder = (props,cardList = [...cards]) =>{
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
      return
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
          setTotal(response.count)
          setCardsDidSet(true)
        } else {
          alert("There was an error")
        }
      }
      apiUserCardsList(props.user,handleCardsLookUp,null)
    }
  }, [props.user, cardsDidSet])
  
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
      apiUserCardsList(props.user, handleLoadNextResponse,nextUrl)
    }
  }

  let userCards = <CardsContainer children={cards.map((item,index) => {
      return <Card card={item} callbackHandler={handleBackendUpdate} onDelete={deleteCard} key={item.id}/>
  })}/>  ;

  if (display === "visual"){
      userCards = <CardsContainer children={cards.map((item,index) => {
          return <Card card={item} callbackHandler={handleBackendUpdate} onDelete={deleteCard} key={item.id}/>
      })}/>  
  }else if(display === "list"){
      userCards = 
      <React.Fragment>
          <TableHead changeOrder={changeOrder}/>
          <div className={Classes.rowContainer}>
            {cards.map((item,index) => {
                return <TableRow callbackHandler={handleBackendUpdate} onDelete={deleteCard} card={item} key={item.id}/>
            })}
          </div>
      </React.Fragment>
  }
  return(
      <React.Fragment> 
          <ControlBar changeOrder={changeOrder} switchDisplay={changeDisplayFormat} totalCards={total} />
          {userCards}
          {nextUrl !== null && <button onClick={handleLoadNext} className='btn next'>Load next</button>}         
      </React.Fragment>
  )
}

function UserCardsApp(props){
    return(
        <UserCardList  user={props.user} />
    )
}
if(userCardsElement){
    ReactDOM.render(e(UserCardsApp,userCardsElement.dataset), userCardsElement)
  }
export default UserCardsApp;