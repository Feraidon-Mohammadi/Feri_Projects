export default function Joke(props) {
  // if (props.setup !== undefined) {
  //   return (
  //     <div className="joke">
  //       <p>Setup: {props.setup}</p>
  //       <p>Punchline: {props.punchline}</p>
  //     </div>
  //   );
  // } else {
  //   return (
  //     <div className="joke">
  //       <p>Punchline: {props.punchline}</p>
  //     </div>
  //   );
  // }

  // ?. ist der Optional-Chaining-Operator und ?? der Nullish-Coalescing-Operator
  // Wir transformieren jeden Kommentar in ein separates li-Element.
  const commentItems =
    props.comments?.map((comment, index) => <li key={index}>{comment}</li>) ?? [];

  return (
    <div className="joke">
      {props.setup !== undefined && <p>Setup: {props.setup}</p>}
      {/* {props.setup !== undefined ? <p>Setup: {props.setup}</p> : false} */}
      <p>Punchline: {props.punchline}</p>
      {commentItems.length > 0 && <ul className="comments">{commentItems}</ul>}
    </div>
  );
}
