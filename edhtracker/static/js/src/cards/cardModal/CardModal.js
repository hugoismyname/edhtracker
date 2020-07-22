import React,{useState} from 'react';
import Classes from './cardModal.module.css'
import Aux from '../../hoc/ReactAux'
import Backdrop from '../../UI/Backdrop'
import {apiAddCard} from '../../userCards'

function CardModal(props){
  const [cardAmount, setCardAmount] = useState(1)
  const cardId = props.cardId

  const handleSubmit = (event) =>{
    event.preventDefault()
    apiAddCard(() =>{},{"card":cardId,"card_count":cardAmount})
    props.onClose()
  }

  const handleChange = (event) =>{
    console.log(event.target.value)
    setCardAmount(event.target.value)
  }

  return(
    <Aux>
      <Backdrop clicked={props.onClose} show={props.show}></Backdrop>
      <form style={{ display: props.isVisible}} id={Classes.cardUpdateModal}>
        <div className={Classes.closeButton}><span onClick={props.onClose}>x</span></div>
        <h3 >{props.cardName}</h3>
        <div className={Classes.cardQuantity}>
          <h4>Quantity</h4>
          <input type="number" name="cardCount" min="1" max="99" maxLength="3" onChange={handleChange} value={cardAmount}/>
        </div>
        <button onClick={handleSubmit} type="submit" className={Classes.saveButton}>ADD CARD</button>
      </form>
    </Aux>
    
  )
}

export default CardModal;