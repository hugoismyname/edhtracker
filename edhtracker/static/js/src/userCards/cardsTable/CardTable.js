import React from 'react';
import Classes from './cardTable.module.css'
import {apiUserCardsDelete, apiUserCardsUpdate} from '../index'

export function TableHead(props){
    const changeOrderHandler = (event) =>{
        console.log(event.target.getAttribute('data-dbsort'))
        props.changeOrder(event.target.getAttribute('data-dbsort'))
    }
    return(
        <ul className={Classes.tableHead}>
            <li data-dbsort="card_count" onClick={changeOrderHandler} className={`${Classes.tableCount} ${Classes.columnHeader}`}>QTY</li>
            <li data-dbsort="name" onClick={changeOrderHandler} className={`${Classes.tableName} ${Classes.columnHeader}`}>NAME</li>
            <li data-dbsort="set" onClick={changeOrderHandler} className={`${Classes.tableSet} ${Classes.columnHeader}`}>SET</li>
            <li data-dbsort="date_added" onClick={changeOrderHandler} className={`${Classes.tableDate} ${Classes.columnHeader}`}>DATE ADDED</li>
            <li data-dbsort="type_line" onClick={changeOrderHandler} className={`${Classes.tableType} ${Classes.columnHeader}`}>TYPE</li>
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
            <li className={Classes.tableName}><a href={`/card_detail/${props.card['card_id']}`}>{props.card["name"]}</a></li>
            <li className={Classes.tableSet}>{props.card["set"]}</li>
            <li className={Classes.tableDate}>{props.card["date_added"]}</li>
            <li className={Classes.tableType}>{props.card["type_line"]}</li>
            <span onClick={deleteCard} className={Classes.removeCard}></span>
        </ul>
    )
}
