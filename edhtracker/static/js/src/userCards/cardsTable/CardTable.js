import React from 'react';
import Classes from './cardTable.module.css'
import {apiUserCardsDelete, apiUserCardsUpdate} from '../index'

export function TableHead(){
    return(
        <ul className={Classes.tableHead}>
            <li className={Classes.tableCount}>QTY</li>
            <li className={Classes.tableName}>NAME</li>
            <li className={Classes.tableSet}>SET</li>
            <li className={Classes.tableDate}>DATE ADDED</li>
            <li className={Classes.tableType}>TYPE</li>
        </ul>
    )
}
export function TableRow(props){

    const deleteCard = () =>{
        apiUserCardsDelete(props.callbackHandler,props.card['id'])
        props.onDelete(props.card['id'])
    }

    const updateCard = (event) =>{
        const card_count = event.target.value
        apiUserCardsUpdate(props.callbackHandler,props.card['id'],{'card_count': card_count})
    }

    return(
        <ul className={`${Classes.tableHead} ${Classes.tableRow}`}>
            <li className={Classes.tableCount}>
                <input type="number" min="1" max="99" maxLength="3" onChange={updateCard} defaultValue={props.card["card_count"]}/>
            </li>
            <li className={Classes.tableName}>{props.card["name"]}</li>
            <li className={Classes.tableSet}>{props.card["set"]}</li>
            <li className={Classes.tableDate}>{props.card["date_added"]}</li>
            <li className={Classes.tableType}>{props.card["type_line"]}</li>
            <span onClick={deleteCard} className={Classes.removeCard}></span>
        </ul>
    )
}
