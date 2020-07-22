import React,{useEffect,useState} from 'react';
import ReactDOM from 'react-dom';
import {lookUpcardsInDeck} from './lookUp'
import CardsContainer from '../hoc/CardsContainer'
import {Card} from '../cards';
import Classes from './cardDetail.module.css'
import CardModal from '../cards/cardModal/CardModal';


const e = React.createElement
const cardDetailElement = document.getElementById("card_detail")

function CardDetail(props){
    const [cardsInDeck, setCardsInDeck] = useState([])
    const [cardsInDeckDidSet, setCardsInDeckDidSet] = useState(false)
    const [switchCardsShown, setSwitchCardsShown] = useState([true,false,"Show Cards Owned"])
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
    const changeDisplayHandler = ()=>{
        event.preventDefault()
        const message = switchCardsShown[0] ? "Show Cards Needed" : "Show Cards Owned"
        setSwitchCardsShown([!switchCardsShown[0],!switchCardsShown[1],message])
    }
    useEffect(() => {
      if (cardsInDeckDidSet === false){
        const handleCardsLookUp = (response, status) => {
          if (status === 200){
            setCardsInDeck(response)
            setCardsInDeckDidSet(true)
          }else{
            alert("There was an error")
          }
        }
        lookUpcardsInDeck(handleCardsLookUp,props.pk,props.username)
      }
    }, [])

    let Cards_list;

    const groupByType = (list,listIndex) =>{
        return(
            Object.entries(list).map((subItem,index)=>{
                return(
                    <React.Fragment>
                        <h2 className={Classes.typeHeader}>{subItem[0]}</h2>
                        <CardsContainer key={index}>
                            {
                                subItem[1].map((lastItem)=>{
                                    return <Card displayModal={displayModalHandler} card={lastItem} key={lastItem.id}/>
                                })
                            }
                        </CardsContainer>
                    </React.Fragment>
                )
            })
        )
    }
    if(props.username){
        Cards_list =
        <React.Fragment>
            <a className={Classes.switchCards} onClick={changeDisplayHandler}>{switchCardsShown[2]}</a>
            {cardsInDeck.map((ownedAndMissing,index)=>{
                return(
                    <div className={switchCardsShown[index] == true ? Classes.visible : Classes.hidden}>
                        {ownedAndMissing.map((item)=>{
                            return(
                                groupByType(item)
                            )
                        })}
                    </div>
                )
            })}  
        </React.Fragment>
    } else {
        Cards_list =
        cardsInDeck.map((item)=>{
            return(
                groupByType(item)
            )
        })
    }

    return( 
        <React.Fragment>
            {Cards_list}
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

if(cardDetailElement){
    ReactDOM.render(e(CardDetail,cardDetailElement.dataset), cardDetailElement)
  }
export default CardDetail;
