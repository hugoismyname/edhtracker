import React,{useEffect,useState} from 'react';
import ReactDOM from 'react-dom';
import {lookUpDeckRecs} from './index'
import CardsContainer from '../hoc/CardsContainer'
import {Card} from '../cards';
import Classes from './decksRec.module.css' 

const e = React.createElement
const decksRecElement = document.getElementById("decksRec")

function DecksRec(props){
    const [commanderData, setCommanderData] = useState([])
    const [commanderDataDidSet, setCommanderDataDidSet] = useState(false)

    useEffect(() => {
      if (commanderDataDidSet === false){
        const handleCardsLookUp = (response, status) => {
          if (status === 200){
            setCommanderData(response)
            setCommanderDataDidSet(true)
          } else if (status === 204){
            setCommanderData(response)
            setCommanderDataDidSet(true)
          }else{
            alert("There was an error")
          }
        }
        lookUpDeckRecs(handleCardsLookUp,props.username)
      }
    }, [])
    let commanderRecs =
      <div className={Classes.noCommanders}>
        <span>Please  </span>
          <a href='/login/' className={Classes.link}> LOG IN </a>
        <span>or add cards to your inventory to get recommendation</span>
      </div>
    if (props.username != ""){
      commanderRecs = 
      <CardsContainer children={commanderData.map((item,index) => {
        return (
          <div className={Classes.cardsOuterWrapper} key={item.id}>
            <Card card={item} key={item.id}/>
            <div className={Classes.cardsOwned}><p>{item.cards_owned}</p> out of <p>{item.total_cards}</p></div>
          </div>
        )
      })}/>
    }
    return( 
      <React.Fragment>
        {commanderRecs}
      </React.Fragment>

    )
}

if(decksRecElement){
    ReactDOM.render(e(DecksRec,decksRecElement.dataset), decksRecElement)
  }