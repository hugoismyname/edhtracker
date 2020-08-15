import React,{useEffect,useState} from 'react';
import ReactDOM from 'react-dom';

import {apiCardsLookUp} from './lookUp';
import {apiAddCard, apiUserCardsUpdate} from '../userCards'

import Classes from './cards.module.css';


const e = React.createElement
const allCardsElement = document.getElementById("allCards")


export function Card(props){
  // ['card_id], ['card_count'] refers to cards in a users inventory, both usercards and normal cards have
  // ['id'] values. important to check first for card_id to determine wether its usercard or not
  const [cardId, setCardId] = useState(props.card['card_id'] ? props.card['card_id'] : props.card['id'] )
  const [cardAmount, setCardAmount] = useState(props.card['card_count'] ? props.card['card_count'] : 1)
  const [message, setMessage] = useState(false)

  const addCard = () =>{
    const handleBackend = (response,status) =>{
      if(status === 201){
        setMessage('Card added to your inventory')
        setTimeout( () => {
          setMessage(false);
        }, 5000);
      }else {
        setMessage('An error occured')
        setTimeout( () => {
          setMessage(false);
        }, 5000);
      }
    }
    apiAddCard(handleBackend,{"card":cardId,"card_count":cardAmount})
  }
  const deleteCard = () =>{
    const handleBackend = (response,status) =>{
      if(status === 201){

      }else {
        setMessage('An error occured')
        setTimeout( () => {
          setMessage(false);
        }, 5000);
      }
    }
    apiAddCard(handleBackend,{"card":cardId,"card_count":cardAmount})
  }

  const updateCard = (cardAmount) =>{
    console.log(cardAmount)
    const handleBackendUpdate = (response,status) =>{
      if(status === 204){
      }else {
        setMessage('An error occured')
        setTimeout( () => {
          setMessage(false);
        }, 5000); 
      }
    }
    apiUserCardsUpdate(handleBackendUpdate,props.card['id'],{"card_count":cardAmount})
  }

  const changeInput = (event) =>{
    if(event.target.innerText == '+'){
      const newCardAmount = parseInt(cardAmount) + 1
      setCardAmount(parseInt(cardAmount) + 1)
      if(props.card['card_id']){
        updateCard(newCardAmount)
      }
    }else if(event.target.innerText == '-' && cardAmount != 1 ){
      const newCardAmount = parseInt(cardAmount) - 1
      setCardAmount(parseInt(cardAmount) - 1)
      if(props.card['card_id']){
        updateCard(newCardAmount)
      }
    }
  }

  let editCard;

  if(props.card['card_id']){
    editCard =
    <React.Fragment>
      <div className={Classes.userQty}>
        <div onClick={changeInput} className={Classes.userMinus}>-</div>
        <div className={Classes.userCount} >{cardAmount}</div>
        <div onClick={changeInput} className={Classes.userPlus}>+</div>

      </div>
      <div className={Classes.buttonWrapper}>
        <button onClick={deleteCard} value={cardId} className={Classes.removeButton} >REMOVE CARD</button>
        {message && 
          <span className={Classes.cardAdded}>{message}</span>
        }
      </div>
    </React.Fragment>
  }else{
    editCard =
    <React.Fragment>
      <div className={Classes.qty}>
        <div onClick={changeInput} className={Classes.minus}>-</div>
        <div className={Classes.count} >{cardAmount}</div>
        <div onClick={changeInput} className={Classes.plus}>+</div>
      </div>
      <div className={Classes.buttonWrapper}>
        <button onClick={addCard} value={cardId} className={Classes.addCardButton} >ADD CARD</button>
        {message && 
          <span className={Classes.cardAdded}>{message}</span>
        }
      </div>
    </React.Fragment> 
  }

  return(
    <React.Fragment>
      <div className={Classes.cardWrapper} >
        <img src={`/static/card_images/${props.card['img_url']}.jpg`} alt={props.card['name']}/>
        <div className={Classes.editCard} >
          <a href={`/card_detail/${cardId}`}>
            {props.card['name']}
          </a>
          {editCard}
        </div>
      </div>
    </React.Fragment>
  )
}

function CardList(props){
  const [cards, setCards] = useState([])
  const [cardsDidSet, setCardsDidSet] = useState(false)
  const [color, setColor] = useState({'color': 'ALL CARDS','cards': 9} )

  const changeColorDisplayedHandler = (event,color,index) =>{
    event.preventDefault()
    setColor({'color': color,
              'cards': index 
    })
  }
  useEffect(() => {
    if (cardsDidSet === false){
      const handleCardsLookUp = (response, status) => {
        if (status === 200){
          setCards(response)
          setCardsDidSet(true)
        } else {
          alert("There was an error")
        }
      }
      apiCardsLookUp(handleCardsLookUp,props.setname)
    }
  }, [])
  return(
    <React.Fragment>
      <div className={Classes.colorLinkWrapper}>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"WHITE",0)}}>WHITE</a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"BLUE",1)}}>BLUE </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"BLACK",2)}}>BLACK </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"RED",3)}}>RED </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"GREEN",4)}}>GREEN </a><br/>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"MULTICOLORED",5)}}>MULTICOLORED </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"COLORLESS",6)}}>COLORLESS </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"ARTIFACT",7)}}>ARTIFACT </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"LANDS",8)}}>LANDS </a><span></span>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"ALL CARDS",9)}}>ALL CARDS</a>
      </div>
      <h2 className={Classes.colorTitle}><span>{color['color']}</span></h2>
      {
        cards.map((list,index)=>{
          return(
            <div key={index} className={(index === color['cards']) ? Classes.cardsContainer : Classes.hidden} children={list.map((item,index) => {
              return <Card  card={item} key={item.id}/>
            })}/>
          )
        })
      }
    </React.Fragment>
  )
}
if(allCardsElement){
  ReactDOM.render(e(CardList,allCardsElement.dataset), allCardsElement)
}