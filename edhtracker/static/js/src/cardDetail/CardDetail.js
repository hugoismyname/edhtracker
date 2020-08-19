import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";
import { lookUpcardsInDeck } from "./lookUp";
import CardsContainer from "../hoc/CardsContainer";
import { Card } from "../cards";
import Classes from "./cardDetail.module.css";

const e = React.createElement;
const cardDetailElement = document.getElementById("card_detail");

function CardDetail(props) {
  const [cardsInDeck, setCardsInDeck] = useState([]);
  const [cardsInDeckDidSet, setCardsInDeckDidSet] = useState(false);

  useEffect(() => {
    if (cardsInDeckDidSet === false) {
      const handleCardsLookUp = (response, status) => {
        if (status === 200) {
          setCardsInDeck(response);
          setCardsInDeckDidSet(true);
        } else {
          alert("There was an error");
        }
      };
      lookUpcardsInDeck(handleCardsLookUp, props.pk, props.username);
    }
  }, []);

  let Cards_list;

  // Accepts the array and key
  const groupBy = (array, key) => {
    // Return the end result
    const groupArray = array.reduce((result, currentValue) => {
      // If an array already present for key, push it to the array. Else create an array and push the object
      (result[currentValue[key]] = result[currentValue[key]] || []).push(
        currentValue
      );
      // Return the current iteration `result` value, this will be taken as next iteration `result` value and accumulate
      return result;
    }, {}); // empty object is the initial value for result object
    console.log(groupArray);
    return Object.entries(groupArray).sort();
  };
  if (props.username) {
    Cards_list = (
      <React.Fragment>

        {cardsInDeck.map((ownedAndMissing, index) => {
          return (
            <div>
              {Object.entries(groupBy(ownedAndMissing, "type")).map(
                (typeList, index) => {
                  return (
                    <React.Fragment key={index}>
                      <div>
                        <h2 className={Classes.typeHeader}>{typeList[1][0]}</h2>
                        <div className={Classes.tabber}><span>Needed</span><span>Owned</span></div>
                      </div>
                      <CardsContainer>
                        {typeList[1][1].map((item) => {
                          return (
                            <Card
                              card={item}
                              key={item.id}
                            />
                          );
                        })}
                      </CardsContainer>
                    </React.Fragment>
                  );
                }
              )}
            </div>
          );
        })}
      </React.Fragment>
    );
  } else {
    Cards_list = Object.entries(groupBy(cardsInDeck, "type")).map(
      (typeList, index) => {
        return (
          <React.Fragment key={index}>
            <h2 className={Classes.typeHeader}>{typeList[1][0]} </h2>
            <CardsContainer>
              {typeList[1][1].map((item) => {
                return (
                  <Card
                    card={item}
                    key={item.id}
                  />
                );
              })}
            </CardsContainer>
          </React.Fragment>
        );
      }
    );
  }

  return (
    <React.Fragment>
      {Cards_list}
    </React.Fragment>
  );
}

if (cardDetailElement) {
  ReactDOM.render(e(CardDetail, cardDetailElement.dataset), cardDetailElement);
}
export default CardDetail;
