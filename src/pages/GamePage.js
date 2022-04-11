import React from 'react'
import Board from '../components/Board'
import PiecePen from '../components/PiecePen'


export default function GamePage() {

    const heightRatio = window.width * 3 / 14
    const heightPct = heightRatio * 100

    return (
        <div
        style={{
            width: '100vw',
            height: `${heightPct}vw`,
            display: 'flex'
        }}>
        <div className="spacer" style = {{width: "8.33%"}}/>
        <div style = {{width: "16.66%"}}>
            <PiecePen color='blue'/>
        </div>
        <div className="spacer" style = {{width: "8.33%"}}/>
        <div style = {{width: "33.33%"}}>
            <Board/>
        </div>  
        <div className="spacer" style = {{width: "8.33%"}}/>
        <div style = {{width: "16.66%"}}>
            <PiecePen color='red'/>
        </div>
        <div className="spacer" style = {{width: "8.33%"}}/>
        </div>
    )
}
