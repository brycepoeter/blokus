import React from 'react'
import './Square.css'

export default function Square({i, color}) {
    const fill = (color === 'red' || color === 'blue') ? color : 'beige'
    const dimensions = window.width > window.height ? window.width : window.height
    return (
    <div
    className='square' 
    id={i}
    style={{
        backgroundColor: fill,
        border: '0.5px solid black',
        width: `${dimensions}px`,
        height: `${dimensions}px`
    }}
    
    >

    </div>)
}