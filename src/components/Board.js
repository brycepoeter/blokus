import React from 'react'
import Square from './Square'

function renderSquare(i, color) {
    return (
        <div style = {{width: `${100/14}%`, height: `${100/14}%`}}>
            <Square i={i} color={color}/>
        </div>
    )
}

export default function Board({colorsInfo}) {
    const squares = []
    for (let i = 0; i < 14 ** 2; i++) {
        squares.push(renderSquare(i, 'black'))
    }

    return (
        <div
            style={{
                width: "100%",
                height: "100%",
                display: 'flex',
                border: '0.5px solid black',
                flexWrap: 'wrap'
            }}
        >
            {squares}
        </div>
    )
}