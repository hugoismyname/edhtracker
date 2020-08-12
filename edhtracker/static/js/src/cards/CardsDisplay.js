import React,{useEffect,useState} from 'react';
import ReactDOM from 'react-dom';
import {apiCardsLookUp} from './lookUp';
import Classes from './cards.module.css';
import {apiAddCard} from '../userCards'


const e = React.createElement
const allCardsElement = document.getElementById("allCards")


export function Card(props){
  const [cardId, setCardId] = useState(props.card['card_id'] ? props.card['card_id'] : props.card['id'] )
  const [message, setMessage] = useState(false)
  const [cardAmount, setCardAmount] = useState(1)

  const addCard = (event) =>{
    setMessage(true)
    setTimeout( () => {
      setMessage(false);
    }, 500);

    apiAddCard(() =>{},{"card":cardId,"card_count":cardAmount})
  }
  const changeInput = (event) =>{
    if(event.target.innerText == '+'){
      setCardAmount(parseInt(cardAmount) + 1)
    }else if(event.target.innerText == '-' && cardAmount != 1 ){
      setCardAmount(parseInt(cardAmount) - 1)
    }
  }
  const handleChange = (event) =>{
    setCardAmount(event.target.value)
  }
  return(
    <React.Fragment>
      <div className={Classes.cardWrapper} >
        <img src={`/static/card_images/${props.card['img_url']}.jpg`} alt={props.card['name']}/>
        <div className={Classes.editCard} >
          <a href={`/card_detail/${cardId}`}>
            {props.card['name']}
          </a>
          <div className={Classes.qty}>
            <div onClick={changeInput} className={Classes.minus}>-</div>
            <input className={Classes.count} onChange={handleChange} type="number" value={cardAmount} min="1" max="99"  maxLength="3" />
            <div onClick={changeInput} className={Classes.plus}>+</div>
          </div>
          <div className={Classes.buttonWrapper}>
            <button onClick={addCard} value={cardId} className={Classes.addCardButton} >ADD CARD</button>
            {message && 
              <span className={Classes.cardAdded}> Card Added To Inventory.</span>
            }
          </div>
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