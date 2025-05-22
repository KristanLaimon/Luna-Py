// @ts-nocheck
import { useState } from "react";

export default Counter(){
  const [count, setCount] = useState(0);

  return (
    <h1>Counter {count}</h1>
    <button onClick={() => setCount(count + 1)}></button>
  )
}

