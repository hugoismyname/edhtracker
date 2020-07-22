import React,{useEffect,useState} from 'react';
import ReactDOM from 'react-dom';
import {apiCardsLookUp} from './lookUp';
import Classes from './cards.module.css';
import Aux from '../hoc/ReactAux';
import CardModal from './cardModal/CardModal';

const e = React.createElement
const allCardsElement = document.getElementById("allCards")


export function Card(props){
  const [cardId, setCardId] = useState(props.card['card_id'] ? props.card['card_id'] : props.card['id'] )
  const displayModalHandler = () =>{
      props.displayModal( 
        {"cardId": cardId,
          "cardName": props.card['name']
        })
  }
  return(
    <Aux>
      <div className={Classes.cardWrapper} >
        <a href={`/card_detail/${cardId}`}>
          <img src={`/static/card_images/${props.card['img_url']}.jpg`} alt={props.card['name']}/>
        </a>
        <div className={Classes.editCard} >
            <button onClick={displayModalHandler} value={cardId} className={Classes.addCardButton} >ADD CARD</button>
        </div>
      </div>
    </Aux>
  )
}

function CardList(props){
  const [cards, setCards] = useState([])
  const [cardsDidSet, setCardsDidSet] = useState(false)
  const [display, setDisplay] = useState(["visual"])
  const [color, setColor] = useState("WHITE")
  const [colorIndex, setColorIndex] = useState(0)
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

  const changeColorDisplayedHandler = (event,color,index) =>{
    event.preventDefault()
    setColor(color)
    setColorIndex(index)
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
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"WHITE",0)}} href="#">WHITE </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"BLUE",1)}}>BLUE </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"BLACK",2)}}>BLACK </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"RED",3)}}>RED </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"GREEN",4)}}>GREEN </a><br/>
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"MULTICOLORED",5)}}>MULTICOLORED </a>  | 
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"COLORLESS",6)}}>COLORLESS </a>  |   
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"ARTIFACT",7)}}>ARTIFACT </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"LANDS",8)}}>LANDS </a>  |  
          <a onClick={(e) =>{changeColorDisplayedHandler(e,"ALL CARDS",9)}}>ALL CARDS</a>
      </div>
      <div className="set-title-wrapper"> 
        <h2 className="set-title"><span>{color}</span></h2>
      </div>
      {
        cards.map((list,index)=>{
          return(
            <div className={(index === colorIndex) ? Classes.cardsContainer : Classes.hidden} children={list.map((item,index) => {
              return <Card displayModal={displayModalHandler} card={item} key={item.id}/>
            })}/>
          )
        })
      }
      <CardModal 
        onClose={closeModalHandler}
        isVisible={cardInfo["isVisible"]} 
        cardName={cardInfo["cardName"]} 
        cardId={cardInfo["cardId"]} 
        show={cardInfo["backdropShow"]}
      />
    </React.Fragment>
  )
}
if(allCardsElement){
  ReactDOM.render(e(CardList,allCardsElement.dataset), allCardsElement)
}