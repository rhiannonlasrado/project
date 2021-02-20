import React from 'react'
import Todo from './Todo'

export default function TodoList({todos, toggleTodo}) {
    return (
        todos.map(todo => {
            return <Todo key={todo} toggleTodo={toggleTodo} todo={todo} />
        })
    )
}
